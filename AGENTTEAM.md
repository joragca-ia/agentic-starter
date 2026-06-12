# Equipo de agentes

> Registro de todos los agentes del proyecto.
> Se empieza con un solo agente. Los especializados se crean después, cuando un dominio crece lo suficiente (criterio y pasos en `agents/README.md`).

---

## Agente principal

| Agente | Carpeta | Dominio | Cuándo usarlo |
|--------|---------|---------|---------------|
| [AGENT_NAME] | (raíz) | Todo | Siempre — es el punto de entrada |

---

## Agentes especializados

[Vacío al principio: el sistema arranca con un solo agente. Cuando un dominio acumule 3-4 directivas propias y las conversaciones se alarguen en ese tema, crear un especialista siguiendo `agents/README.md` y registrarlo aquí.]

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
