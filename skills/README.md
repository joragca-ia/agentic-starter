# Sistema de skills

Un skill es una capacidad reutilizable documentada como un paquete: un `SKILL.md` con las instrucciones más archivos de soporte opcionales. Es más pequeño que una directiva (que puede orquestar varios skills) y más específico que un agente.

---

## Filosofía: skills paraguas, no micro-skills

El objetivo de esta carpeta es una **biblioteca de conocimiento a nivel de clase de tarea**, no una lista larga de entradas estrechas donde cada una captura el caso concreto de una sesión.

- Un skill se busca por su **descripción**, no por su nombre exacto. Un skill amplio con subsecciones etiquetadas se encuentra mejor que cinco skills hermanos estrechos.
- El nombre debe ser **a nivel de clase**: `gestionar-newsletters`, no `arreglar-error-newsletter-mayo`. Si el nombre solo tiene sentido para la tarea de hoy, está mal: ese contenido va como subsección o archivo de soporte de un skill más amplio.
- El detalle específico de una sesión (un error concreto, un ejemplo real, un script) va en los **archivos de soporte**, no inflando el `SKILL.md`.

---

## Estructura de un skill

```
skills/[categoria]/[nombre-skill]/
├── SKILL.md          ← instrucciones principales (obligatorio)
├── references/       ← detalle específico: errores documentados, extractos de docs,
│                        peculiaridades de herramientas, notas de dominio
├── templates/        ← archivos base pensados para copiar y modificar
└── scripts/          ← acciones re-ejecutables tal cual (verificaciones, generadores)
```

Solo `SKILL.md` es obligatorio. Las tres carpetas de soporte se crean cuando hacen falta. Cuando añadas un archivo de soporte, añade una línea en `SKILL.md` que apunte a él, para que cualquier sesión futura sepa que existe.

---

## Cuándo crear un skill vs. una directiva

**Crea un skill** cuando:
- La capacidad se puede invocar con un comando corto y parámetros claros
- Se reutiliza en múltiples directivas o contextos
- Tiene inputs/outputs bien definidos
- Ejemplo: "generar caption para Instagram", "transcribir audio", "buscar en la vault"

**Crea una directiva** cuando:
- El proceso tiene varios pasos y decisiones
- Orquesta múltiples skills o herramientas
- Necesita contexto del usuario para ejecutarse
- Ejemplo: "publicar contenido en redes", "procesar transcripción de llamada"

---

## Cómo crear un skill

**Antes de crear, comprobar el orden de preferencia** (ver `AGENT.md`, "Bucle de aprendizaje"):
1. ¿Existe un skill que se pueda actualizar? Actualízalo.
2. ¿Existe un skill paraguas del mismo territorio? Añade una subsección.
3. ¿El contenido es detalle de sesión? Añádelo como archivo de soporte de un skill existente.
4. Solo si nada de lo anterior aplica: crear skill nuevo.

**Para crear uno nuevo:**

1. Crea la carpeta `skills/[categoria]/[nombre-skill]/` (crea la categoría si no existe)
2. Crea `SKILL.md` usando el template de `_template/SKILL.md`. La descripción del frontmatter debe empezar por "Usar cuando..." — es lo que se usa para decidir si el skill aplica
3. Añade una entrada en `_index.md`

### Categorías sugeridas

- `contenido/` — generación y edición de contenido
- `comunicacion/` — email, mensajes, notificaciones
- `conocimiento/` — búsqueda, lectura, síntesis de información
- `tareas/` — gestión de tareas y proyectos
- `media/` — procesamiento de audio, video e imágenes
- `datos/` — procesamiento y transformación de datos

---

## Mantenimiento

- **Si usas un skill y está mal, incompleto o desactualizado: corrígelo en el momento**, sin esperar a que lo pidan. Los skills sin mantener se convierten en pasivos.
- **Nunca borrar: archivar.** Un skill muerto se mueve a `skills/.archive/[nombre-skill]/` (carpeta completa, con sus archivos de soporte). El archivo es recuperable; el borrado no.
- **Revisión periódica:** una vez al mes, la tarea "Mantenimiento de skills" de `HEARTBEAT.md` consolida skills que se solapan y archiva los muertos.

---

## Cómo invocar un skill

Invocar un skill significa que el agente lee el `SKILL.md` correspondiente y ejecuta el proceso documentado con los parámetros dados. La notación es una convención para nombrarlo de forma consistente (el usuario también puede usarla para pedir un skill concreto):

```
[SKILL:nombre-del-skill] param1=valor param2=valor
```

---

## Template

Ver `_template/SKILL.md`.
