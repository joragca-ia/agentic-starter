# Autoarranque del bridge en Mac y Linux

Los scripts listos para usar (`start_telegram_bridge.bat`, `.vbs`, `register_telegram_autostart.ps1`) son para Windows. En Mac y Linux el bridge es el mismo (`execution/telegram_bridge.py`); solo cambia cómo se deja arrancando solo. Dos opciones, de más a menos recomendada.

---

## Mac: launchd

Crear `~/Library/LaunchAgents/com.agente.telegram-bridge.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.agente.telegram-bridge</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>RUTA_ABSOLUTA_DEL_PROYECTO/execution/telegram_bridge.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>RUTA_ABSOLUTA_DEL_PROYECTO</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>RUTA_ABSOLUTA_DEL_PROYECTO/.tmp/telegram_bridge.log</string>
    <key>StandardErrorPath</key>
    <string>RUTA_ABSOLUTA_DEL_PROYECTO/.tmp/telegram_bridge.log</string>
</dict>
</plist>
```

Sustituir `RUTA_ABSOLUTA_DEL_PROYECTO` por la ruta real (sin barra final). `KeepAlive: true` hace que macOS relance el proceso si se cae, igual que el watchdog de Windows.

Activar:
```bash
launchctl load ~/Library/LaunchAgents/com.agente.telegram-bridge.plist
```

Desactivar:
```bash
launchctl unload ~/Library/LaunchAgents/com.agente.telegram-bridge.plist
```

---

## Linux: systemd (usuario)

Crear `~/.config/systemd/user/telegram-bridge.service`:

```ini
[Unit]
Description=Bridge de Telegram del agente

[Service]
WorkingDirectory=RUTA_ABSOLUTA_DEL_PROYECTO
ExecStart=/usr/bin/python3 RUTA_ABSOLUTA_DEL_PROYECTO/execution/telegram_bridge.py
Restart=always
RestartSec=15

[Install]
WantedBy=default.target
```

Activar:
```bash
systemctl --user enable --now telegram-bridge.service
```

---

## Alternativa rápida (Mac y Linux): crontab @reboot

Sin reinicio automático si el proceso se cae, pero es la opción más simple para una primera prueba:

```bash
crontab -e
```

Añadir la línea:
```
@reboot cd RUTA_ABSOLUTA_DEL_PROYECTO && /usr/bin/python3 execution/telegram_bridge.py >> .tmp/telegram_bridge.log 2>&1
```
