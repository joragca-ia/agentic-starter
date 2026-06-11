# Protocolo de Inicialización

> **Este documento define el proceso de primera configuración del sistema.**
> El agente lo ejecuta una sola vez, en la primera sesión.
> Después actúa como referencia si se necesita reconfigurar algo.

---

## Cuándo ejecutar este protocolo

Ejecuta este protocolo completo si se cumple cualquiera de estas condiciones:
- `memory/user.md` está vacío o contiene solo el template
- `IDENTITY.md` contiene "[AGENT_NAME]" sin reemplazar
- `MEMORY.md` indica "Inicializado: No"
- El usuario dice "inicializa", "configura desde cero" o similar

Si el sistema ya está inicializado (`MEMORY.md` indica "Inicializado: Sí") y el usuario no ha pedido reconfigurar, no lo ejecutes.

---

## Protocolo paso a paso

---

### PASO 0 — Bienvenida

Di al usuario exactamente esto (adaptando el idioma si ya sabes cuál usa):

> "Hola. Soy tu agente de IA y voy a hacerte una serie de preguntas para configurar este sistema a tu medida.
>
> El proceso tarda entre 5 y 10 minutos. Puedes responder con la extensión que quieras: cuanto más cuentes, mejor puedo ayudarte.
>
> ¿Empezamos?"

Espera confirmación antes de continuar.

---

### PASO 1 — Identidad del usuario

Haz estas preguntas en un solo mensaje:

> "Primero, cuéntame un poco sobre ti:
>
> 1. ¿Cuál es tu nombre?
> 2. ¿A qué te dedicas? (empresa, producto o servicio que ofreces, sector)
> 3. ¿Cuál es tu rol? (fundador, CEO, freelance, responsable de marketing, etc.)
> 4. ¿Cuántas personas hay en tu equipo? (si aplica)
> 5. ¿Tienes clientes de empresa a empresa (B2B) o de empresa a consumidor final (B2C)? ¿Cómo es tu cliente tipo?"

Cuando responda, rellena los campos de `memory/user.md` conservando la estructura completa del archivo:
```
# Usuario

- **Nombre:** [nombre]
- **Empresa / Actividad:** [empresa o descripción de actividad]
- **Sector:** [sector]
- **Rol:** [rol]
- **Tamaño del equipo:** [número o descripción]
- **Tipo de cliente:** [B2B / B2C / descripción del avatar]
- **Zona horaria:** [detectar o dejar pendiente si no es deducible]
- **Idioma preferido:** [detectar del idioma en que está respondiendo]

## Contexto profesional

[2-4 frases sobre su actividad, cómo trabaja, qué hace cada día, extraídas de sus respuestas]

## Rol del agente en su trabajo

[Cómo encaja el agente en su día a día. Si aún no está claro, completar tras el Paso 2]
```

---

### PASO 2 — Propósito del sistema

Haz esta pregunta:

> "Ahora cuéntame para qué quieres este sistema. Concretamente:
>
> - ¿Qué problema principal quieres resolver?
> - ¿Qué tareas del día a día te consumen más tiempo o son más tediosas?
> - ¿Hay algo que quieras automatizar?
> - ¿Qué debería poder hacer este agente que ahora haces tú manualmente?"

Cuando responda, rellena estas secciones de `memory/objectives.md` (el archivo ya existe, no lo crees de nuevo; conserva las secciones restantes, que se completan en el Paso 5):

- **Problema principal a resolver:** extraer de la respuesta
- **Tareas candidatas a automatizar:** listar las mencionadas
- **Primer objetivo medible:** extraer o proponer basándote en lo dicho

---

### PASO 3 — Herramientas actuales

Haz esta pregunta:

> "¿Qué herramientas usas en tu trabajo diario? Por ejemplo:
>
> - Gestión de tareas: Notion, ClickUp, Asana, Trello, Monday...
> - Email: Gmail, Outlook, otro...
> - Calendario: Google Calendar, Outlook Calendar, Apple Calendar...
> - Base de datos o CRM de clientes...
> - Almacenamiento: Google Drive, Dropbox, OneDrive...
> - Comunicación interna: Slack, Teams, WhatsApp...
> - Cualquier otra herramienta que uses cada semana"

Cuando responda, actualiza `TOOLS.md` **conservando el resto del archivo** (la sección "Integraciones disponibles" es un catálogo de referencia, no la borres):

1. Rellena la tabla "Herramientas activas" con una fila por herramienta:

| Herramienta | Categoría | Para qué se usa | Integración |
|-------------|-----------|-----------------|-------------|
| [nombre]    | [tipo]    | [uso]           | Pendiente / Configurada |

2. En "Notas de configuración", anota cualquier detalle relevante mencionado y qué integraciones convendría configurar primero.

---

### PASO 4 — Procesos y flujos

Haz esta pregunta:

> "Describe tus 3 a 5 procesos más importantes o repetitivos. Por ejemplo:
>
> - 'Cada semana publico contenido en redes y el proceso es...'
> - 'Cuando llega un lead nuevo, hago esto...'
> - 'Cada lunes reviso mis tareas así...'
> - 'Cuando termino una reunión con un cliente, tardo X tiempo en hacer Y...'
>
> No necesita ser perfecto ni completo. Descríbelos como se te ocurran."

Cuando responda, identifica el proceso más claro y concreto. Crea una directiva de ejemplo en `directives/[nombre-proceso].md` usando el template de `directives/_template.md`.

Dile al usuario qué directiva creaste y para qué proceso.

---

### PASO 5 — Objetivos

Haz esta pregunta:

> "¿Cuáles son tus objetivos? Puedes ser tan concreto o vago como quieras:
>
> - En los próximos 30 días, ¿qué quieres lograr?
> - En los próximos 6 meses?
> - ¿Hay métricas o números concretos que persigues? (ingresos, clientes, tiempo ahorrado, etc.)"

Cuando responda, rellena las secciones restantes de `memory/objectives.md` (ya existen en el archivo, no las dupliques):

- **Objetivos a 30 días:** extraer
- **Objetivos a 6 meses:** extraer
- **Métricas clave:** extraer si las mencionó

---

### PASO 6 — Modelo de agentes

Basándote en los procesos descritos en el Paso 4, propón una de estas opciones:

**Opción A — Un solo agente (tú):**
Apropiado si los procesos son pocos, el usuario trabaja solo, o las tareas son variadas y no tienen un dominio muy específico.

**Opción B — Varios agentes especializados:**
Apropiado si hay dominios claramente diferenciados. Propón roles concretos basados en lo que describió. Ejemplos:
- Si mencionó contenido o redes sociales: "un agente de contenido"
- Si mencionó ventas o clientes: "un agente de ventas / CRM"
- Si mencionó operaciones o tareas internas: "un agente de operaciones"
- Si mencionó desarrollo técnico: "un agente técnico"

Presenta las dos opciones con una recomendación clara basada en lo que contó. Deja que el usuario decida.

Si elige la Opción B, para cada agente propuesto:

1. Copia `agents/_template/` a `agents/[rol]/` (rol en minúsculas, sin espacios: `agents/contenido/`, `agents/ventas/`)
2. En los archivos copiados (`AGENT.md`, `IDENTITY.md`, `SOUL.md`, `MEMORY.md` y los de `memory/`), reemplaza "[AGENT_NAME]" por el nombre del agente y "[dominio]" por su dominio. Si el usuario no propone nombres, usa el rol como nombre (ej: "Contenido") y ofrécele cambiarlo después
3. Completa las secciones del `AGENT.md` del agente con lo que sepas de los procesos descritos en el Paso 4 (responsabilidades, autonomía). Lo que no sepas, déjalo marcado como pendiente
4. Registra el agente en `AGENTTEAM.md` (tabla "Agentes especializados")
5. Añade una fila en la tabla "Delegación" de `AGENT.md` (raíz) indicando qué tareas se delegan a este agente

---

### PASO 7 — Identidad del agente

Haz esta pregunta:

> "Por último, vamos a ponerle nombre y personalidad a tu agente.
>
> - ¿Cómo quieres llamarle? (puede ser un nombre propio, un acrónimo, lo que quieras)
> - ¿Qué tono quieres que tenga? (formal / informal, directo / conversacional, serio / con algo de humor)
> - ¿Cómo describirías su personalidad en 3 palabras?"

Cuando responda:

1. Rellena `IDENTITY.md` con el nombre y descripción elegidos
2. Rellena `SOUL.md` con los principios de personalidad extraídos de la respuesta
3. En `AGENT.md`, reemplaza "[AGENT_NAME]" por el nombre elegido
4. En `AGENTTEAM.md`, reemplaza "[AGENT_NAME]" en la tabla "Agente principal"
5. Elimina o comenta la instrucción "Si IDENTITY.md contiene [AGENT_NAME]..." de `AGENT.md`

---

### PASO 8 — Preferencias de trabajo

Sin hacer preguntas adicionales, rellena `memory/preferences.md` con lo que hayas aprendido durante la conversación:
- Idioma detectado
- Tono preferido (formal / informal)
- Cualquier preferencia mencionada explícitamente
- Horarios si los mencionó
- Cualquier dato de estilo de trabajo

---

### PASO 9 — Cierre y resumen

Antes de presentar el resumen, actualiza `MEMORY.md`, sección "Estado del sistema":

- **Inicializado:** Sí — [fecha de hoy]
- **Última actualización:** [fecha de hoy]

Esto es obligatorio: si no se hace, el sistema intentará volver a ejecutar este protocolo en la próxima sesión.

Después presenta al usuario este resumen:

> "Listo. Aquí está lo que he configurado:
>
> **Tu agente:** [nombre]
>
> **Archivos configurados:**
> - `memory/user.md` — tu perfil
> - `memory/objectives.md` — tus objetivos
> - `memory/preferences.md` — tus preferencias de trabajo
> - `TOOLS.md` — tus herramientas
> - `directives/[nombre].md` — tu primer proceso documentado
> - `IDENTITY.md` y `SOUL.md` — identidad del agente
> - `AGENTTEAM.md` y `agents/` — tu equipo de agentes [incluir solo si se eligió la Opción B en el Paso 6]
>
> **Siguientes pasos sugeridos:**
> 1. [Proponer basándote en los procesos descritos — ej: "Documentar el proceso de X como directiva"]
> 2. [Proponer basándote en las herramientas — ej: "Configurar la integración con Gmail"]
> 3. [Proponer basándote en los objetivos — ej: "Crear el primer skill para automatizar Y"]
>
> **Una cosa más:** este sistema aprende con el uso. Cada vez que me corrijas, descubramos una solución o repitamos un proceso, lo capturo en mis skills y mi memoria para que la próxima vez salga mejor a la primera. Corregirme no es molestarme: es la forma más rápida de entrenarme.
>
> ¿Hay algo que quieras ajustar o añadir antes de empezar a trabajar?"

---

## Post-inicialización

Una vez completado el setup, el agente opera con normalidad:
- Lee `memory/user.md` + `memory/preferences.md` + `MEMORY.md` al inicio de cada sesión
- No vuelve a preguntar información ya capturada
- Actualiza la memoria cuando aprende algo nuevo del usuario o del proyecto