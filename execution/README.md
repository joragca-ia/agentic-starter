# Execution

Scripts deterministas que el agente ejecuta directamente (capa E del framework DOE(S), ver `AGENT.md`). A diferencia de las directivas y skills (que el agente interpreta), estos scripts hacen siempre exactamente lo mismo.

---

## Scripts disponibles

| Script | Para qué |
|--------|----------|
| `telegram_bridge.py` | Conecta el agente con Telegram: escucha mensajes y responde. Ver `skills/comunicacion/conectar-telegram/SKILL.md` |
| `start_telegram_bridge.bat` | Arranca el bridge en bucle (lo reinicia si se cae). Windows |
| `start_telegram_hidden.vbs` | Lanza el bridge sin ventana de consola visible. Windows |
| `register_telegram_autostart.ps1` | Registra el arranque automático del bridge al iniciar sesión. Windows |

---

## Cómo añadir un script nuevo

1. Crear el archivo en esta carpeta
2. Añadir una fila a la tabla anterior
3. Si el script forma parte de un skill, documentarlo en su `SKILL.md` (sección "Archivos de soporte") en lugar de duplicar la explicación aquí
