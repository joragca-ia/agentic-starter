#!/usr/bin/env python3
"""
Telegram bridge — conecta este agente con Telegram.

Arranque manual:  python execution/telegram_bridge.py
Arranque automático al encender el ordenador: ver skill
skills/comunicacion/conectar-telegram/SKILL.md.

Requiere TELEGRAM_TOKEN y TELEGRAM_CHAT_ID en el .env de la raíz
del proyecto (los crea setup_telegram.py).
"""

import os
import re
import sys
import json
import html
import time
import socket
import subprocess
import threading
import tempfile
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

try:
    from dotenv import dotenv_values
except ImportError:
    dotenv_values = None

# ── Paths ──────────────────────────────────────────────────────────────────
WORKDIR      = Path(__file__).resolve().parent.parent
ENV_FILE     = WORKDIR / ".env"
TMP          = WORKDIR / ".tmp"
SESSION_FILE = TMP / "telegram_session_id.txt"
LAST_HEARTBEAT = TMP / "telegram_last_heartbeat.txt"
LOCK_PORT    = 47391

INIT_FILES = [
    "IDENTITY.md", "SOUL.md", "MEMORY.md",
    "memory/user.md", "memory/preferences.md",
]

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

TMP.mkdir(exist_ok=True)


def find_claude_bin():
    import shutil
    return shutil.which("claude") or shutil.which("claude.cmd")


CLAUDE_BIN = find_claude_bin()


# ── .env ───────────────────────────────────────────────────────────────────

def load_env():
    if dotenv_values:
        return dotenv_values(ENV_FILE)
    vals = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                vals[k.strip()] = v.strip()
    return vals


# ── Markdown → Telegram HTML ──────────────────────────────────────────────

def md_to_html(text: str) -> str:
    code_blocks = {}
    def protect_block(m):
        key = f"\x00CB{len(code_blocks)}\x00"
        code_blocks[key] = f"<pre><code>{html.escape(m.group(2))}</code></pre>"
        return key
    text = re.sub(r'```(\w*)\n?(.*?)```', protect_block, text, flags=re.DOTALL)

    inline_codes = {}
    def protect_inline(m):
        key = f"\x00IL{len(inline_codes)}\x00"
        inline_codes[key] = f"<code>{html.escape(m.group(1))}</code>"
        return key
    text = re.sub(r'`([^`\n]+)`', protect_inline, text)

    text = html.escape(text, quote=False)
    text = re.sub(r'^#{1,6}\s+(.+)$', r'<b>\1</b>', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text, flags=re.DOTALL)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)

    for key, val in code_blocks.items():
        text = text.replace(html.escape(key, quote=False), val)
    for key, val in inline_codes.items():
        text = text.replace(html.escape(key, quote=False), val)

    return text.strip()


# ── Telegram helpers ──────────────────────────────────────────────────────

def tg(token, method, **params):
    url  = f"https://api.telegram.org/bot{token}/{method}"
    data = json.dumps(params).encode("utf-8")
    req  = urllib.request.Request(url, data=data,
                                  headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode("utf-8"))

def tg_download(token, file_id, dest_path):
    r = tg(token, "getFile", file_id=file_id)
    url = f"https://api.telegram.org/file/bot{token}/{r['result']['file_path']}"
    urllib.request.urlretrieve(url, dest_path)

def send_typing(token, chat_id):
    try:
        tg(token, "sendChatAction", chat_id=chat_id, action="typing")
    except Exception:
        pass

def send_message(token, chat_id, text):
    formatted = md_to_html(text)
    for i in range(0, len(formatted), 4096):
        chunk = formatted[i:i+4096]
        try:
            tg(token, "sendMessage", chat_id=chat_id, text=chunk, parse_mode="HTML")
        except Exception:
            try:
                tg(token, "sendMessage", chat_id=chat_id, text=text[i:i+4096])
            except Exception as e:
                print(f"[bridge] send error: {e}")


# ── Audio (opcional — solo si execution/transcribe_audio.py existe) ───────

def transcribe_audio(audio_path: Path) -> str:
    script = WORKDIR / "execution" / "transcribe_audio.py"
    if not script.exists():
        return ("[No puedo transcribir audio en este sistema: falta "
                 "execution/transcribe_audio.py. Escríbeme el mensaje en texto.]")
    result = subprocess.run(
        [sys.executable, str(script), str(audio_path)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        cwd=str(WORKDIR), timeout=90,
    )
    return (result.stdout or "").strip() or "[Transcripción fallida]"


# ── Sesión persistente con Claude Code ─────────────────────────────────────

_claude_lock = threading.Lock()

def _get_session_id():
    try:
        return SESSION_FILE.read_text(encoding="utf-8").strip() or None
    except Exception:
        return None

def _save_session_id(session_id):
    try:
        SESSION_FILE.write_text(session_id, encoding="utf-8")
    except Exception as e:
        print(f"[bridge] No pude guardar la sesión: {e}")

def _base_cmd():
    if not CLAUDE_BIN:
        raise RuntimeError(
            "No encuentro el comando 'claude' en el PATH. "
            "Instala Claude Code (https://claude.com/claude-code) y vuelve a arrancar el bridge."
        )
    return [
        CLAUDE_BIN, "--print",
        "--input-format",  "stream-json",
        "--output-format", "stream-json",
        "--verbose",
        "--dangerously-skip-permissions",
    ]

def _run_claude(cmd: list, content: str) -> str:
    msg_json = json.dumps({
        "type": "user",
        "message": {"role": "user", "content": content}
    }) + "\n"

    with _claude_lock:
        try:
            result = subprocess.run(
                cmd, input=msg_json,
                capture_output=True, text=True, encoding="utf-8", errors="replace",
                cwd=str(WORKDIR), timeout=300,
            )
        except subprocess.TimeoutExpired:
            return "Timeout (5 min) esperando respuesta."
        except Exception as e:
            return f"[Error invocando claude]: {e}"

    if result.returncode != 0 and not result.stdout.strip():
        return f"[Error claude {result.returncode}]: {(result.stderr or '')[:400]}"

    response_text = ""
    new_session_id = None

    for line in result.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue

        if event.get("session_id"):
            new_session_id = event["session_id"]

        etype = event.get("type", "")
        if etype == "result":
            if event.get("is_error"):
                new_session_id = None
                break
            response_text = event.get("result", "").strip()
            break
        if etype == "assistant" and not response_text:
            for block in event.get("message", {}).get("content", []):
                if block.get("type") == "text":
                    response_text += block.get("text", "")

    if new_session_id:
        _save_session_id(new_session_id)

    return response_text or result.stdout.strip()[:500] or "[Sin respuesta]"

def _init_session():
    files_list = "\n".join(f"{i+1}. {f}" for i, f in enumerate(INIT_FILES))
    init_prompt = (
        "[INIT — no mostrar al usuario]\n"
        "Tienes permisos completos (--dangerously-skip-permissions). Esto significa:\n"
        "- NUNCA pidas permiso para usar herramientas, leer archivos, ejecutar scripts o editar memoria\n"
        "- Sigue igualmente las reglas de confirmación de AGENT.md (sección Autonomía): "
        "para lo que ahí diga 'confirmar siempre', pregunta al usuario en el chat antes de actuar\n\n"
        f"Lee estos archivos en orden antes de atender ningún mensaje:\n{files_list}\n\n"
        "Una vez leídos todos, responde únicamente: OK"
    )
    print("[bridge] Inicializando sesión...")
    result = _run_claude(_base_cmd(), init_prompt)
    print(f"[bridge] Sesión inicializada: {result[:60]}")

def ask(content: str) -> str:
    session_id = _get_session_id()
    if not session_id:
        _init_session()
        session_id = _get_session_id()

    cmd = _base_cmd()
    if session_id:
        cmd += ["--resume", session_id]

    return _run_claude(cmd, content)


# ── Reconexión tras corte (informativo, sin invocar al agente) ────────────

def _update_last_heartbeat():
    try:
        LAST_HEARTBEAT.write_text(datetime.now().isoformat(timespec="seconds"), encoding="utf-8")
    except Exception:
        pass

def _load_last_heartbeat():
    try:
        return datetime.fromisoformat(LAST_HEARTBEAT.read_text(encoding="utf-8").strip())
    except Exception:
        return None

def notify_reconnect(token, chat_id):
    last = _load_last_heartbeat()
    now  = datetime.now()
    if last is None:
        _update_last_heartbeat()
        return
    gap = now - last
    if gap.total_seconds() >= 35 * 60:
        hours = gap.total_seconds() / 3600
        gap_str = f"{int(hours)}h {int((gap.total_seconds() % 3600) / 60)}min"
        send_message(token, chat_id,
            f"Me he reconectado tras estar parado {gap_str}. "
            f"Si tenías tareas programadas en HEARTBEAT.md en ese tiempo, dímelo y las reviso.")
    _update_last_heartbeat()


# ── Heartbeat: ejecuta HEARTBEAT.md aunque no haya sesión abierta ─────────

def _is_no_action(response: str) -> bool:
    clean = response.strip().lower().rstrip(".")
    no_action = ("ok", "nada", "sin acción", "sin accion", "no hay nada",
                 "no hay tareas", "sin tareas", "no hay nada que hacer")
    return clean in no_action or (len(clean) < 80 and any(p in clean for p in no_action))

def heartbeat_loop(token, chat_id, shutdown_flag):
    heartbeat_file = WORKDIR / "HEARTBEAT.md"
    last_fired_minute = -1
    while not shutdown_flag.is_set():
        if heartbeat_file.exists():
            now    = datetime.now()
            minute = now.minute
            if minute in (0, 30) and minute != last_fired_minute:
                last_fired_minute = minute
                timestamp = now.strftime("%Y-%m-%d %H:%M")
                print(f"[heartbeat] {timestamp}")
                prompt = (
                    f"[HEARTBEAT] {timestamp}\n"
                    f"Lee HEARTBEAT.md y ejecuta las tareas programadas para este momento. "
                    f"Si no hay nada que hacer ahora, responde únicamente: 'OK'."
                )
                def run():
                    try:
                        response = ask(prompt)
                        if response and not _is_no_action(response):
                            send_message(token, chat_id, response)
                    except Exception as e:
                        print(f"[heartbeat] Error: {e}")
                    finally:
                        _update_last_heartbeat()
                threading.Thread(target=run, daemon=True).start()
        time.sleep(10)


# ── Procesamiento de mensajes ──────────────────────────────────────────────

def process_message(token, chat_id, msg):
    user     = msg.get("from", {}).get("username") or msg.get("from", {}).get("first_name", "usuario")
    voice    = msg.get("voice") or msg.get("audio")
    photo    = msg.get("photo")
    document = msg.get("document")
    text     = msg.get("text", "").strip()
    caption  = msg.get("caption", "").strip()
    content  = None

    if voice:
        file_id  = voice["file_id"]
        ext      = "oga" if msg.get("voice") else "mp3"
        tmp_path = Path(tempfile.gettempdir()) / f"tg_audio_{file_id[:10]}.{ext}"
        send_typing(token, chat_id)
        try:
            tg_download(token, file_id, tmp_path)
            transcription = transcribe_audio(tmp_path)
            tmp_path.unlink(missing_ok=True)
            content = f"[Audio de {user}, transcrito]: {transcription}"
            print(f"[bridge] {user} [audio]: {transcription[:80]}")
        except Exception as e:
            send_message(token, chat_id, f"Error al procesar el audio: {e}")
            return

    elif photo:
        send_typing(token, chat_id)
        best = max(photo, key=lambda p: p.get("file_size", 0))
        file_id = best["file_id"]
        img_dir = TMP / "telegram_images"
        img_dir.mkdir(exist_ok=True)
        img_path = img_dir / f"tg_photo_{file_id[:16]}.jpg"
        try:
            tg_download(token, file_id, img_path)
            caption_part = f"\nMensaje que acompaña la foto: {caption}" if caption else ""
            content = (
                f"[Foto recibida de {user}]{caption_part}\n"
                f"Lee la imagen con tu herramienta de lectura en la ruta: {img_path}\n"
                f"Analiza su contenido y responde en consecuencia."
            )
            print(f"[bridge] {user} [foto] descargada en: {img_path}")
        except Exception as e:
            send_message(token, chat_id, f"Error al descargar la foto: {e}")
            return

    elif document:
        file_id  = document["file_id"]
        filename = document.get("file_name", f"doc_{file_id[:10]}")
        tmp_path = Path(tempfile.gettempdir()) / filename
        send_typing(token, chat_id)
        try:
            tg_download(token, file_id, tmp_path)
            content = (f"[Archivo recibido de {user}: {tmp_path}]"
                       + (f" Mensaje: {caption}" if caption else ""))
            print(f"[bridge] {user} [doc]: {filename}")
        except Exception as e:
            send_message(token, chat_id, f"Error al descargar el archivo: {e}")
            return

    elif text:
        content = f"[Telegram de {user}]: {text}"
        print(f"[bridge] {user}: {text[:120]}")

    if not content:
        return

    send_typing(token, chat_id)
    response = ask(content)
    print(f"[bridge] -> {response[:100]}...")
    send_message(token, chat_id, response)


# ── Singleton (evita dos bridges a la vez) ─────────────────────────────────

shutdown_flag = threading.Event()

def acquire_singleton():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
    try:
        srv.bind(("127.0.0.1", LOCK_PORT))
        srv.listen(1)
        return srv
    except OSError:
        print("[bridge] Señalizando instancia anterior...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("127.0.0.1", LOCK_PORT))
            s.sendall(b"shutdown")
            s.close()
        except Exception:
            pass
        for _ in range(20):
            time.sleep(0.5)
            try:
                srv2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                srv2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
                srv2.bind(("127.0.0.1", LOCK_PORT))
                srv2.listen(1)
                return srv2
            except OSError:
                continue
        raise RuntimeError("No se pudo adquirir el lock tras 10s")

def listen_for_shutdown(srv):
    srv.settimeout(1.0)
    while not shutdown_flag.is_set():
        try:
            conn, _ = srv.accept()
            data = conn.recv(16)
            conn.close()
            if data == b"shutdown":
                print("\n[bridge] Shutdown recibido. Parando...")
                shutdown_flag.set()
                return
        except socket.timeout:
            continue
        except Exception:
            return


# ── Main ────────────────────────────────────────────────────────────────

def _wait_for_network(max_wait: int = 120) -> bool:
    deadline = time.time() + max_wait
    attempt = 0
    while time.time() < deadline:
        try:
            socket.getaddrinfo("api.telegram.org", 443)
            return True
        except OSError:
            attempt += 1
            print(f"[bridge] Red no disponible ({attempt}), esperando 5s...")
            time.sleep(5)
    return False


def main():
    env     = load_env()
    token   = (env.get("TELEGRAM_TOKEN") or "").strip()
    chat_id = (env.get("TELEGRAM_CHAT_ID") or "").strip()

    if not token or not chat_id:
        print("Falta TELEGRAM_TOKEN o TELEGRAM_CHAT_ID en el .env de la raíz del proyecto.")
        print("Ejecuta primero: python setup_telegram.py")
        sys.exit(1)

    srv = acquire_singleton()
    threading.Thread(target=listen_for_shutdown, args=(srv,), daemon=True).start()

    print(f"[bridge] Arrancando... workdir: {WORKDIR}")

    if not _wait_for_network():
        print("[bridge] Red no disponible tras 120s. Saliendo para que el watchdog relance.")
        sys.exit(1)

    me       = tg(token, "getMe")
    bot_name = me["result"]["username"]
    print(f"[bridge] Bot: @{bot_name}")

    notify_reconnect(token, chat_id)

    # Drenar updates pendientes desde la última vez
    offset = 0
    while True:
        try:
            result  = tg(token, "getUpdates", offset=offset, limit=100, timeout=0)
            updates = result.get("result", [])
            if not updates:
                break
            offset = updates[-1]["update_id"] + 1
        except Exception:
            break

    threading.Thread(target=heartbeat_loop, args=(token, chat_id, shutdown_flag), daemon=True).start()
    print(f"[bridge] Listo. Escuchando en @{bot_name}")

    while not shutdown_flag.is_set():
        try:
            result  = tg(token, "getUpdates", offset=offset, timeout=0)
            updates = result.get("result", [])

            for update in updates:
                offset = update["update_id"] + 1
                msg = update.get("message")
                if not msg:
                    continue
                if str(msg["chat"]["id"]) != chat_id:
                    continue
                threading.Thread(target=process_message, args=(token, chat_id, msg), daemon=True).start()

            if not updates:
                time.sleep(2)

        except KeyboardInterrupt:
            break
        except urllib.error.HTTPError as e:
            print(f"[bridge] HTTP {e.code}: {e}")
            time.sleep(5)
        except Exception as e:
            print(f"[bridge] Error: {e}")
            time.sleep(3)

    srv.close()
    print("[bridge] Parado.")


if __name__ == "__main__":
    main()
