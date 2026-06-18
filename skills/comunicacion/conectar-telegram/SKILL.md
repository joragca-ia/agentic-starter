---
name: conectar-telegram
description: Usar cuando el usuario quiere hablar con este agente desde Telegram (móvil o escritorio) en vez de solo desde Claude Code. Se ofrece durante el setup inicial (STARTUP.md) y se puede invocar en cualquier momento si el usuario pide "conecta Telegram" o similar. Guía la creación del bot, valida la conexión y deja el bridge arrancando solo al encender el ordenador.
---

# Conectar Telegram

## Qué hace

Conecta este agente a un bot de Telegram para poder hablarle por mensaje de texto o nota de voz desde el móvil, en vez de tener que abrir Claude Code cada vez. El propio agente guía el proceso paso a paso por el chat: no hace falta que el usuario sepa programar ni que ejecute nada él mismo.

Al terminar, hay un proceso (`telegram_bridge.py`) escuchando los mensajes del bot y respondiendo con este agente, y opcionalmente queda configurado para arrancar solo cada vez que se enciende el ordenador.

---

## Cuándo usarlo / cuándo no

**Usar cuando:**
- Es la primera vez que se hace el setup (`STARTUP.md`, Paso 1) y el usuario dice que sí a la pregunta de Telegram
- El usuario pide en cualquier momento "conecta Telegram", "quiero hablarte desde el móvil" o similar
- El usuario dice que el bot dejó de responder y hay que reconfigurar el token o el chat_id

**NO usar cuando:**
- El usuario no usa Claude Code de forma local con acceso a terminal/Bash (el bridge necesita poder invocar el comando `claude` en esta máquina). Si solo usa el chat web de Claude.ai sin Claude Code instalado, explica que esta función requiere Claude Code y omite el resto del skill.

---

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| Respuesta del usuario a "¿conectamos Telegram?" | sí/no | Sí | Si es "no", no continuar; ofrecerlo más adelante está bien |
| Token del bot | texto | Sí | Lo da @BotFather, se obtiene durante el proceso |
| Confirmación de autoarranque | sí/no | No | Si el usuario no lo pide explícitamente, ofrecerlo igualmente al final — default recomendado: sí |

---

## Proceso

Todo este proceso se hace **conversacionalmente, en el chat**, ejecutando tú mismo (con tus herramientas Bash/Edit) cada paso. No le pidas al usuario que ejecute scripts en una terminal: hazlo tú y cuéntale lo que vas haciendo en 1-2 frases por paso. La alternativa manual (`setup_telegram.py`) existe solo para quien prefiera hacerlo él mismo sin pasar por el chat.

### 1. Crear el bot

Explica en un mensaje corto:

> "Vamos a crearte un bot de Telegram. Tarda 2 minutos:
> 1. Abre Telegram y busca **@BotFather** (tiene una marca de verificación azul)
> 2. Envíale el comando `/newbot`
> 3. Te pedirá un nombre (el que quieras, ej: 'Mi Copiloto') y un username que acabe en `bot` (ej: `micopiloto_bot`)
> 4. Te dará un token con este formato: `1234567890:ABCDefghijKLMnopQRSTuvwXYZ`
>
> Pégamelo aquí cuando lo tengas."

### 2. Validar el token

Cuando el usuario pegue el token, valídalo tú mismo:

```bash
curl -s "https://api.telegram.org/bot<TOKEN>/getMe"
```

- Si `"ok":true` → confirma el nombre del bot al usuario y continúa.
- Si `"ok":false` → dile qué falló (token mal copiado, con espacios, etc.) y pide que lo reenvíe.

Guarda el token en el `.env` de la raíz del proyecto (créalo si no existe):
```
TELEGRAM_TOKEN=<token>
```

### 3. Obtener el chat_id

Pide:

> "Ahora envíale cualquier mensaje a tu bot en Telegram (por ejemplo 'Hola') y dime cuando lo hayas hecho."

Cuando confirme, ejecuta:

```bash
curl -s "https://api.telegram.org/bot<TOKEN>/getUpdates"
```

Extrae `result[].message.chat.id` del JSON (el último mensaje). Si no hay updates, pide que reenvíe el mensaje y reintenta. Añade al `.env`:
```
TELEGRAM_CHAT_ID=<chat_id>
```

### 4. Probar la conexión

Envía un mensaje de prueba real:

```bash
curl -s -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" -d "chat_id=<CHAT_ID>" -d "text=Conectado. Ya puedes hablarme por aquí."
```

Confirma con el usuario que le ha llegado a Telegram antes de seguir.

### 5. Arrancar el bridge ahora

Arráncalo en segundo plano para que funcione ya mismo en esta sesión:

```bash
python execution/telegram_bridge.py
```

(ejecútalo en background; no bloquees el chat esperando a que termine, porque no termina — es un proceso continuo).

### 6. Ofrecer el autoarranque

Pregunta:

> "Por último: ¿quieres que esto arranque solo cada vez que enciendas el ordenador, para no tener que acordarte de lanzarlo? Te lo recomiendo."

**Si dice que sí, en Windows:**
```powershell
powershell -ExecutionPolicy Bypass -File execution\register_telegram_autostart.ps1
```
Si falla por permisos, pide al usuario que abra PowerShell como Administrador y repita el comando él mismo (no puedes elevar permisos por él).

**Si dice que sí, en Mac/Linux:** sigue `references/mac_linux_autostart.md` y configura el método correspondiente (launchd o systemd).

**Si dice que no:** no pasa nada, queda anotado en `TOOLS.md` que el arranque es manual (`python execution/telegram_bridge.py`).

### 7. Registrar en TOOLS.md

Añade una fila en la tabla "Herramientas activas" de `TOOLS.md`:
```
| Telegram | Comunicación | Hablar con el agente desde el móvil | execution/telegram_bridge.py, autoarranque: Sí/No |
```

---

## Outputs

| Resultado | Tipo | Descripción |
|-----------|------|-------------|
| `.env` | archivo | Con `TELEGRAM_TOKEN` y `TELEGRAM_CHAT_ID` |
| Bridge corriendo | proceso | Responde mensajes de Telegram con este agente |
| Autoarranque (opcional) | tarea programada / launchd / systemd | El bridge se relanza solo tras reiniciar el ordenador o si se cae |
| `TOOLS.md` actualizado | archivo | Fila de Telegram en "Herramientas activas" |

---

## Side effects

- Crea o modifica `.env` en la raíz del proyecto (token y chat_id — **nunca subir este archivo a git**, ya está en `.gitignore`)
- Crea `.tmp/telegram_session_id.txt` y `.tmp/telegram_last_heartbeat.txt` (estado interno del bridge)
- Si se activa el autoarranque: registra una tarea programada (Windows) o un agente launchd/servicio systemd (Mac/Linux)

---

## Errores frecuentes

| Error | Causa | Solución |
|-------|-------|----------|
| `"ok":false` al validar el token | Token mal copiado o bot borrado | Pedir que lo copie de nuevo desde BotFather, completo |
| No aparece ningún chat_id en `getUpdates` | El usuario no le ha escrito al bot todavía, o Telegram ya "consumió" el update | Pedir que envíe otro mensaje nuevo y reintentar |
| El bridge no encuentra el comando `claude` | Claude Code no está en el PATH del sistema | Comprobar con `claude --version`; si falla, reinstalar Claude Code asegurando que el instalador lo añade al PATH |
| El bot no responde tras reiniciar el ordenador | Autoarranque no configurado, o falló el registro de la tarea | Repetir el paso 6, o arrancar manualmente con `python execution/telegram_bridge.py` |
| Mensajes duplicados o respuestas cruzadas | Dos bridges corriendo a la vez | El script tiene un lock (puerto 47391) que para la instancia anterior automáticamente; si persiste, reiniciar el ordenador |

---

## Checklist de verificación

- [ ] El bot responde un mensaje de prueba enviado por el usuario desde Telegram, no solo el de validación
- [ ] `.env` tiene `TELEGRAM_TOKEN` y `TELEGRAM_CHAT_ID` y no se ha mostrado el token completo en el chat más de lo necesario
- [ ] `TOOLS.md` refleja el estado real (conectado, con o sin autoarranque)
- [ ] El usuario sabe cómo volver a arrancar el bridge manualmente si algo falla (`python execution/telegram_bridge.py`)

---

## Archivos de soporte

- `references/mac_linux_autostart.md` — autoarranque del bridge en Mac (launchd) y Linux (systemd / cron)
- `execution/telegram_bridge.py` — el bridge: escucha Telegram, mantiene sesión con Claude Code, responde
- `execution/start_telegram_bridge.bat` — bucle de reinicio automático si el bridge se cae (Windows)
- `execution/start_telegram_hidden.vbs` — lanza el bridge sin ventana visible (Windows)
- `execution/register_telegram_autostart.ps1` — registra el arranque automático al iniciar sesión (Windows)
- `setup_telegram.py` (raíz del proyecto) — versión manual del paso 1-4, para quien prefiera hacerlo en terminal sin pasar por el chat

---

## Notas

- El bridge mantiene **una sola sesión** con el agente principal (no enruta a agentes especializados como procesos separados). Si el proyecto tiene agentes en `agents/`, el agente principal sigue pudiendo "adoptar su rol" dentro de la misma sesión, como describe `AGENTTEAM.md`, sección "Cómo delegar".
- El bridge usa `--dangerously-skip-permissions` para no bloquear con prompts de confirmación de la terminal (que nadie vería, porque corre en segundo plano). La seguridad real son las reglas de `AGENT.md` → "Autonomía": el agente debe seguir preguntando por chat antes de acciones que esa tabla marca como "confirmar siempre".
- Si está conectado Telegram, el heartbeat de `HEARTBEAT.md` puede ejecutarse aunque no haya nadie con el chat de Claude Code abierto, porque el propio bridge invoca al agente cada 30 minutos. Sin Telegram, el heartbeat solo se comprueba al abrir una sesión (ver `HEARTBEAT.md`).
- Solo responde al `chat_id` guardado en `.env`: si otra persona encuentra el bot y le escribe, el bridge ignora el mensaje.
