# Sistema de agentes

Un agente especializado es un sub-agente con dominio propio, memoria propia y lógica de decisión independiente. El agente principal lo activa cuando una tarea pertenece claramente a ese dominio.

---

## Cuándo crear un agente vs. una directiva

**Crea una directiva** cuando:
- El proceso es un SOP concreto y repetible
- No requiere memoria propia ni toma de decisiones complejas
- Se ejecuta directamente desde el agente principal

**Crea un agente** cuando:
- Hay un dominio bien definido con muchas tareas propias (ej: todo lo de contenido, todo lo de ventas)
- Necesita su propia memoria separada de la del agente principal
- La lógica es tan específica que contaminaría el contexto del agente principal
- Se beneficia de una identidad y personalidad diferente

**Regla práctica:** Si tienes más de 3-4 directivas sobre el mismo dominio y las conversaciones se alargan mucho en ese tema, es señal de que necesitas un agente especializado.

---

## Cómo crear un agente nuevo

**Paso 1.** Copia la carpeta `_template/` y renómbrala con el nombre del agente (en minúsculas, sin espacios):
```
agents/contenido/
agents/ventas/
agents/operaciones/
```

**Paso 2.** Rellena los 4 archivos principales:
- `AGENT.md` — instrucciones operativas del agente
- `IDENTITY.md` — nombre, rol, capacidades
- `SOUL.md` — personalidad y valores
- `MEMORY.md` — memoria de sesión (se limpia entre sesiones)

**Paso 3.** Crea los archivos de memoria persistente en `memory/`:
- `preferences.md` — preferencias del usuario relevantes para este dominio
- `decisions.md` — decisiones tomadas en este dominio

**Paso 4.** Registra el agente en `AGENTTEAM.md` (en la raíz del proyecto).

**Paso 5.** Añade la entrada de delegación en `AGENT.md` (raíz), en la sección "Delegación".

---

## Estructura de un agente

```
agents/[nombre]/
├── AGENT.md        ← Instrucciones operativas (DOE)
├── IDENTITY.md     ← Nombre, rol, capacidades
├── SOUL.md         ← Personalidad y valores
├── MEMORY.md       ← Memoria de sesión (volátil)
├── memory/
│   ├── preferences.md   ← Preferencias del usuario para este dominio
│   └── decisions.md     ← Decisiones tomadas en este dominio
└── directives/          ← SOPs específicos del agente (opcional)
    └── [proceso].md
```

---

## Cómo activar un agente

El agente principal lo indica en su respuesta:

```
[DELEGATE:nombre-agente] — contexto de la tarea
```

A continuación, el agente lee `agents/[nombre]/AGENT.md`, `IDENTITY.md`, `SOUL.md` y la carpeta `memory/` del especialista, y ejecuta la tarea siguiendo esas instrucciones y esa memoria en lugar de las suyas. No hay un cambio de programa: es el mismo agente adoptando el rol, las reglas y el contexto del especialista. Ver el detalle en `AGENTTEAM.md`, sección "Cómo delegar".

---

## Template

Ver `_template/` para la estructura base de un agente vacío, lista para copiar.
