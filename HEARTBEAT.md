# Heartbeat — Tareas recurrentes

> Define las tareas recurrentes del agente: qué hace, cuándo y cómo.
> Rellenar y activar después del setup inicial según las necesidades del usuario.
> Las tareas marcadas como [EJEMPLO] son plantillas — adaptar o eliminar.

---

## Cómo funciona

**Importante:** el agente solo está activo cuando hay una sesión abierta. No hay un proceso en segundo plano que ejecute tareas a una hora exacta. El agente comprueba este archivo al inicio de cada sesión (ver `AGENT.md`, sección "Memoria") y ejecuta las tareas cuyo trigger aplique y no se hayan ejecutado ya.

Cada tarea tiene un trigger (cuándo se activa), los pasos a ejecutar y un flag opcional para evitar duplicados.

El trigger puede ser:
- **Periódico:** "una vez al día", "los lunes" — se ejecuta en la primera sesión que se abra dentro del periodo
- **Evento:** "al iniciar sesión", "al cerrar sesión"
- **Manual:** "cuando el usuario diga X"

> Si se necesita ejecución a horas exactas sin sesión abierta, hace falta un automatismo externo (un programador de tareas que abra la sesión). Es una ampliación avanzada, fuera del alcance de esta plantilla.

El flag de deduplicación evita que la tarea se ejecute dos veces el mismo día si el sistema se reinicia:
- Antes de ejecutar, comprobar si existe `.tmp/[nombre]_YYYY-MM-DD.done`
- Si existe: no hacer nada
- Si no existe: ejecutar y luego crear el archivo con timestamp

---

## Tareas configuradas

### [EJEMPLO] Check-in diario

**Trigger:** Al iniciar la primera sesión del día, o manualmente cuando el usuario lo pida.
**Flag:** `.tmp/checkin_YYYY-MM-DD.done`

**Qué hacer:**
1. Leer `memory/active_projects.md` para ver el estado actual
2. Leer los eventos del calendario de hoy (si hay integración configurada en TOOLS.md)
3. Revisar tareas pendientes (si hay integración con gestor de tareas)
4. Presentar al usuario un resumen breve: qué tiene hoy, qué está pendiente

---

### [EJEMPLO] Sync semanal

**Trigger:** Primera sesión de la semana (lunes, o el primer día que se abra sesión), o manualmente cuando el usuario lo pida.
**Flag:** `.tmp/sync_semanal_YYYY-WW.done`

**Qué hacer:**
1. Revisar los objetivos de la semana anterior (`memory/objectives.md`)
2. Revisar proyectos activos (`memory/active_projects.md`)
3. Proponer 3 prioridades para esta semana basándote en los objetivos
4. Preguntar al usuario si las prioridades son correctas

---

### Cierre de sesión

**Trigger:** Al final de una sesión larga o cuando el usuario diga "cerramos" o similar.
**Flag:** (sin flag — ejecutar siempre que se pida)

**Qué hacer:**
1. **Revisión de aprendizaje** (ver `AGENT.md`, "Bucle de aprendizaje"): repasar la sesión buscando señales — ¿el usuario corrigió algo? ¿apareció una técnica nueva? ¿una skill o directiva consultada estaba mal? Si hubo señal, capturarla siguiendo el orden de preferencia (actualizar > añadir soporte > crear). Respetar la lista de "Qué NO capturar".
2. Preguntar al usuario si hay decisiones o información importante que capturar
3. Actualizar `memory/decisions.md` si hubo decisiones relevantes
4. Actualizar `memory/active_projects.md` si cambió el estado de algún proyecto
5. Crear `memory/daily_log/YYYY-MM-DD.md` con resumen de la sesión
6. Actualizar `MEMORY.md` con cualquier pendiente para la próxima sesión

---

### Mantenimiento de skills y memoria (curador)

**Trigger:** Una vez al mes, en la primera sesión del mes.
**Flag:** `.tmp/curador_YYYY-MM.done`

**Qué hacer:**
1. Listar todos los skills de `skills/` y todas las directivas de `directives/`
2. Buscar solapamientos: skills que un mantenedor humano escribiría como uno solo con subsecciones. Si los hay, consolidar: fusionar en el más amplio (o crear un paraguas nuevo), mover el detalle específico a `references/` y archivar los absorbidos
3. Detectar skills con nombre demasiado estrecho (atado a una tarea concreta ya pasada): mover su contenido bajo un paraguas y archivar el original
4. **Archivar, nunca borrar:** los skills muertos van a `skills/.archive/[nombre]/` con su carpeta completa
5. Actualizar `skills/_index.md` para reflejar el estado final
6. Revisar los archivos de `memory/`: consolidar entradas que se solapan, eliminar datos obsoletos (lo que ya caducó), comprobar que no hay instrucciones imperativas disfrazadas de hechos
7. Crear el flag y contar al usuario en 3-4 líneas qué se consolidó o archivó

---

## Añadir nuevas tareas

Copiar este template para cada nueva tarea recurrente:

```markdown
### [Nombre de la tarea]

**Trigger:** [cuándo se activa]
**Flag:** `.tmp/[nombre]_YYYY-MM-DD.done` (opcional)

**Qué hacer:**
1. [paso 1]
2. [paso 2]
3. [crear flag si aplica]
```
