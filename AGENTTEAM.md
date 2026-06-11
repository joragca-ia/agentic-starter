# Equipo de agentes

> Registro de todos los agentes del proyecto.
> Se actualiza durante el setup inicial (STARTUP.md, Paso 6) y cuando se añaden nuevos agentes.
> Para crear un agente nuevo, seguir las instrucciones en `agents/README.md`.

---

## Agente principal

| Agente | Carpeta | Dominio | Cuándo usarlo |
|--------|---------|---------|---------------|
| [AGENT_NAME] | (raíz) | Todo | Siempre — es el punto de entrada |

---

## Agentes especializados

[Vacío hasta el setup inicial. Se rellenará en el Paso 6 de STARTUP.md si el usuario elige modelo multi-agente.]

| Agente | Carpeta | Dominio | Cuándo delegar |
|--------|---------|---------|----------------|
| — | — | — | — |

---

## Cómo delegar

Delegar no es un cambio automático de programa: es el propio agente adoptando el rol del especialista. Cuando el agente principal decide delegar:

1. Lo anuncia en su respuesta con esta marca, para que quede trazable:
```
[DELEGATE:nombre-agente] — contexto breve de la tarea
```
2. Lee los archivos del agente especializado (`agents/[nombre]/AGENT.md`, `IDENTITY.md`, `SOUL.md` y su `memory/`)
3. Ejecuta la tarea siguiendo esas instrucciones, personalidad y memoria, no las propias
4. Al terminar, actualiza la memoria del especialista si aprendió algo de su dominio y reporta el resultado al usuario
