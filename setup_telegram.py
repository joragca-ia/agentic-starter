"""
setup_telegram.py — Conectar Telegram al sistema agéntico

Ejecutar una sola vez para configurar el canal de comunicación.
No necesitas experiencia técnica. El script te guía paso a paso.

Normalmente no necesitas ejecutar esto a mano: durante el setup inicial
(STARTUP.md) el propio agente hace estos pasos contigo por el chat. Este
script existe como alternativa para quien prefiera hacerlo directamente
en una terminal, o para reconfigurar la conexión más adelante.
"""

import os
import sys

try:
    import requests
except ImportError:
    print("Instalando dependencia requests...")
    os.system(f"{sys.executable} -m pip install requests -q")
    import requests

try:
    from dotenv import set_key, dotenv_values
    DOTENV_AVAILABLE = True
except ImportError:
    print("Instalando dependencia python-dotenv...")
    os.system(f"{sys.executable} -m pip install python-dotenv -q")
    try:
        from dotenv import set_key, dotenv_values
        DOTENV_AVAILABLE = True
    except ImportError:
        DOTENV_AVAILABLE = False


ENV_FILE = ".env"


def leer_env():
    """Lee el .env actual si existe."""
    if not os.path.exists(ENV_FILE):
        return {}
    if DOTENV_AVAILABLE:
        return dotenv_values(ENV_FILE)
    vals = {}
    with open(ENV_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                vals[k.strip()] = v.strip()
    return vals


def escribir_env(key, value):
    """Escribe o actualiza una clave en .env."""
    if DOTENV_AVAILABLE:
        set_key(ENV_FILE, key, value)
        return

    lines = []
    updated = False
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith(f"{key}="):
                lines[i] = f"{key}={value}\n"
                updated = True
                break
    if not updated:
        lines.append(f"{key}={value}\n")
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)


def validar_token(token):
    """Valida el token contra la API de Telegram."""
    try:
        r = requests.get(f"https://api.telegram.org/bot{token}/getMe", timeout=10)
        data = r.json()
        if data.get("ok"):
            return True, data["result"]
        return False, data.get("description", "Token inválido")
    except Exception as e:
        return False, str(e)


def obtener_chat_id(token):
    """Obtiene el chat_id del primer mensaje recibido por el bot."""
    try:
        r = requests.get(f"https://api.telegram.org/bot{token}/getUpdates", timeout=10)
        data = r.json()
        if data.get("ok") and data.get("result"):
            for update in reversed(data["result"]):
                msg = update.get("message") or update.get("channel_post")
                if msg and msg.get("chat", {}).get("id"):
                    return msg["chat"]["id"]
    except Exception:
        pass
    return None


def enviar_mensaje(token, chat_id, texto):
    """Envía un mensaje de prueba."""
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": texto},
            timeout=10
        )
        return r.json().get("ok", False)
    except Exception:
        return False


def main():
    print()
    print("=" * 50)
    print("  Configuración de Telegram")
    print("=" * 50)
    print()

    env = leer_env()
    token = (env.get("TELEGRAM_TOKEN") or "").strip()
    chat_id = (env.get("TELEGRAM_CHAT_ID") or "").strip()

    # --- TOKEN ---
    if token:
        ok, info = validar_token(token)
        if ok:
            print(f"Token ya configurado. Bot: @{info.get('username', '?')}")
        else:
            print(f"El token guardado no funciona: {info}")
            token = ""

    if not token:
        print("Necesitas el token de tu bot de Telegram.")
        print()
        print("Si aun no tienes un bot:")
        print("  1. Abre Telegram y busca @BotFather")
        print("  2. Enviale /newbot")
        print("  3. Sigue los pasos y copia el token que te da")
        print()
        while True:
            token = input("Pega aqui el token del bot: ").strip()
            if not token:
                print("El token no puede estar vacio.")
                continue
            print("Verificando token...")
            ok, info = validar_token(token)
            if ok:
                print(f"Token valido. Bot: @{info.get('username', '?')}")
                escribir_env("TELEGRAM_TOKEN", token)
                break
            else:
                print(f"Token no valido: {info}")
                print("Revisa que lo hayas copiado entero y vuelve a intentarlo.")

    print()

    # --- CHAT ID ---
    if chat_id:
        print(f"Chat ID ya configurado: {chat_id}")
    else:
        print("Ahora necesito saber tu chat_id (el numero que identifica tu conversacion con el bot).")
        print()
        print("Enviame cualquier mensaje a tu bot en Telegram ahora mismo")
        print("(por ejemplo: 'Hola')")
        print()
        input("Pulsa Enter cuando hayas enviado el mensaje...")

        print("Buscando tu chat_id...")
        chat_id = obtener_chat_id(token)

        if chat_id:
            print(f"Chat ID encontrado: {chat_id}")
            escribir_env("TELEGRAM_CHAT_ID", str(chat_id))
        else:
            print()
            print("No he podido detectarlo automaticamente.")
            print("Puedes obtenerlo abriendo esta URL en el navegador:")
            print(f"  https://api.telegram.org/bot{token}/getUpdates")
            print("Busca el numero dentro de: \"chat\":{\"id\": XXXXXXXX}")
            print()
            while True:
                chat_id = input("Pega aqui tu chat_id: ").strip()
                if chat_id.lstrip("-").isdigit():
                    escribir_env("TELEGRAM_CHAT_ID", chat_id)
                    break
                print("Debe ser un numero. Intentalo de nuevo.")

    print()

    # --- TEST ---
    print("Enviando mensaje de prueba...")
    ok = enviar_mensaje(
        token,
        chat_id,
        "Sistema conectado. Tu agente ya puede comunicarse contigo por Telegram."
    )

    print()
    if ok:
        print("Conexion verificada. Has recibido el mensaje en Telegram.")
        print()
        print("Siguiente paso: arrancar el bridge")
        print("  python execution/telegram_bridge.py")
        print()
        print("Para que arranque solo cada vez que enciendas el ordenador,")
        print("ver: skills/comunicacion/conectar-telegram/SKILL.md")
    else:
        print("No se pudo enviar el mensaje de prueba.")
        print("Revisa que el chat_id sea correcto y que hayas enviado un mensaje al bot primero.")

    print()
    print("=" * 50)


if __name__ == "__main__":
    main()
