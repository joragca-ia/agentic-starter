# Herramientas del proyecto

> Se rellena durante el setup (con los materiales del Paso 2 y el flujo del Paso 4) y se completa progresivamente a medida que aparecen herramientas trabajando.
> Actualizar cuando se añadan o cambien herramientas.

---

## Herramientas activas

| Herramienta | Categoría | Para qué se usa | Integración |
|-------------|-----------|-----------------|-------------|
| — | — | — | Pendiente |

---

## Integraciones disponibles

Catálogo de referencia: integraciones habituales que se pueden conectar según las herramientas del usuario. Los nombres exactos de las herramientas MCP dependen de cada instalación; al activar una, anotar aquí su nombre real y para qué se usa.

### Cómo conectar una integración

1. **Conectores oficiales (recomendado para empezar):** en Claude, abrir Settings > Connectors (o Extensiones, según la versión) y conectar el servicio con su cuenta. Gmail, Google Calendar y Google Drive suelen estar disponibles así, con autenticación de Google.
2. **Servidores MCP:** para herramientas sin conector oficial (Notion, ClickUp, Asana, Slack...), instalar el servidor MCP del servicio siguiendo su documentación. Suele requerir una API key.
3. Tras conectar, actualizar la tabla "Herramientas activas" (estado: Configurada) y anotar en "Notas de configuración" el nombre de las herramientas MCP disponibles.

### Servicios habituales

- **Email:** Gmail (conector oficial), Outlook (MCP según proveedor)
- **Calendario:** Google Calendar (conector oficial)
- **Almacenamiento:** Google Drive (conector oficial), Dropbox / OneDrive (MCP)
- **Tareas y proyectos:** Notion, ClickUp, Asana, Trello (MCP con API key)
- **Comunicación:** Slack (MCP con API key), **Telegram** (script propio incluido en la plantilla, sin API key de terceros — ver más abajo)

### Telegram: hablar con el agente desde el móvil

A diferencia de las demás integraciones, Telegram no necesita un MCP externo: la plantilla incluye su propio script (`execution/telegram_bridge.py`). Para conectarlo, pide "conecta Telegram" o sigue `skills/comunicacion/conectar-telegram/SKILL.md`. Se ofrece automáticamente durante el setup inicial (`STARTUP.md`, Paso 1).

---

## Notas de configuración

[Anotar aquí cualquier detalle de configuración, tokens, endpoints o instrucciones específicas de las integraciones activas.]
