# Punto de entrada

> Este archivo lo carga automáticamente el LLM al abrir el proyecto.
> Claude Code lee `CLAUDE.md`; otros asistentes leen `AGENTS.md` o `GEMINI.md`. Los tres son copias idénticas: si editas uno, replica el cambio en los otros dos.

Al iniciar cualquier sesión:

1. **Lee `AGENT.md` y sigue sus instrucciones.** Es el documento maestro del agente.
2. **Si `IDENTITY.md` contiene "[AGENT_NAME]" sin reemplazar**, o si el usuario pide "inicializa el proyecto" o similar, **ejecuta el protocolo de `STARTUP.md`** antes de cualquier otra cosa.
3. Si inicias sin memoria de sesiones anteriores y no sabes en qué se estaba trabajando, lee `BOOTSTRAP.md` para recuperar el contexto.
