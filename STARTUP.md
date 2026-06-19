# Protocolo de Inicialización

> **Este documento define el proceso de primera configuración del sistema.**
> El agente lo ejecuta una sola vez, en la primera sesión.
> Después actúa como referencia si se necesita reconfigurar algo.

## Principios de diseño (leer antes de ejecutar)

1. **Mínimas preguntas, valor temprano.** El setup completo dura menos de 10 minutos y termina con algo funcionando, no con un cuestionario respondido.
2. **Documentos antes que interrogatorio.** Si el usuario tiene una web, documentos de marca o procesos escritos, leerlos vale más que veinte preguntas y cansa cero.
3. **Un primer flujo funcionando > mil cosas configuradas.** El objetivo del setup es implementar UN flujo de trabajo útil, no mapear toda la empresa.
4. **El resto se aprende poco a poco.** Todo lo que no se pregunta aquí se descubre progresivamente trabajando (ver "Descubrimiento progresivo" al final).

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

### PASO 1 — Bienvenida + lo básico (un solo mensaje)

Abre con este mensaje (adaptando el idioma al del usuario):

> "Hola. Soy tu agente de IA y voy a configurarme a tu medida. Solo necesito un par de cosas básicas; el resto lo iré aprendiendo sobre la marcha mientras trabajamos juntos:
>
> 1. ¿Cómo te llamas?
> 2. ¿A qué te dedicas? (empresa o actividad, sector, tu rol)
> 3. ¿Qué quieres conseguir con este sistema? (el problema u objetivo principal — con una frase vale)
> 4. ¿Qué nombre quieres ponerme? Y si quieres, dime qué tono prefieres: formal, directo, con algo de humor..."

Cuando responda:

1. Rellena en `memory/user.md` los campos que ya sepas (nombre, actividad, sector, rol, idioma detectado). Deja el resto con "—": se completará progresivamente.
2. Rellena en `memory/objectives.md` la sección "Problema principal a resolver". Deja el resto: se completará progresivamente.
3. Rellena `IDENTITY.md` con el nombre elegido y `SOUL.md` con el tono indicado (si no dio detalles de personalidad, usa los principios base del template).
4. En `AGENT.md`, reemplaza "[AGENT_NAME]" por el nombre elegido y elimina o comenta la instrucción "Si IDENTITY.md contiene [AGENT_NAME]...".
5. En `AGENTTEAM.md`, reemplaza "[AGENT_NAME]" en la tabla "Agente principal".
6. Anota en `memory/preferences.md` el idioma y el tono detectados.

> **Por qué Telegram no se pregunta aquí:** preguntarlo en la bienvenida, antes de que el usuario haya visto nada funcionando, es fricción gratuita — sobre todo con perfiles no técnicos. Se ofrece en el Paso 5, una vez ya hay un flujo de trabajo montado y el usuario ha visto valor real.

---

### PASO 2 — Materiales existentes (antes de preguntar nada más)

Pregunta:

> "Perfecto, [nombre]. Antes de hacerte más preguntas: ¿tienes material donde yo pueda leer sobre tu negocio por mi cuenta? Por ejemplo:
>
> - Tu web (pásame la URL)
> - Documentos de marca, presentaciones o propuestas
> - Procesos escritos, manuales, plantillas que uses
> - Cualquier archivo que me dé contexto
>
> Puedes arrastrar archivos aquí mismo o pegarme enlaces. Cuanto más me des, menos te tendré que preguntar. Y si no tienes nada a mano, no pasa nada: seguimos sin ello."

**Si entrega material:**
1. Léelo todo antes de continuar.
2. Extrae y guarda en los archivos correspondientes: contexto profesional → `memory/user.md`; objetivos y métricas mencionados → `memory/objectives.md`; herramientas que aparezcan → tabla de `TOOLS.md`; clientes o colaboradores relevantes → `memory/people.md`; estilo de comunicación de la marca → `memory/preferences.md`.
3. Confirma en 3-4 líneas qué entendiste de su negocio (sin volcar un resumen largo). Pídele que corrija si algo está mal.

**Si no tiene nada:** continúa directamente al Paso 3, sin insistir.

---

### PASO 3 — Menú: elegir el primer flujo de trabajo

Con lo aprendido en los Pasos 1 y 2, propón entre 4 y 6 cosas concretas que podrías hacer por él desde ya, **adaptadas a su caso** (no genéricas). Formato:

> "Con lo que sé hasta ahora, esto es lo que creo que más te serviría:
>
> 1. [Opción adaptada a su negocio — ej: "Redactar las propuestas para tus clientes a partir de tus notas"]
> 2. [Opción — ej: "Procesar los emails y prepararte borradores de respuesta"]
> 3. [Opción — ej: "Resumir tus reuniones y sacar las tareas pendientes"]
> 4. [Opción — ej: "Documentar tus procesos para delegarlos o automatizarlos"]
> 5. [Opción — ej: "Preparar contenido para tus redes a partir de tu material"]
>
> Puedo hacer todas estas cosas y más — estas me han parecido las más útiles para tu caso concreto. ¿Por cuál empezamos? Y si necesitas algo que no está en la lista, pídemelo y vemos cómo montarlo."

Pautas para generar buenas opciones:
- Partir del objetivo del Paso 1 y del material del Paso 2: las opciones deben sonar a SU negocio, con sus palabras.
- Priorizar tareas frecuentes y tediosas (las que ahorran tiempo cada semana) sobre proyectos grandes.
- Cada opción en una línea, en lenguaje de resultado ("prepararte X", "ahorrarte Y"), no de tecnología.

---

### PASO 4 — Implementar el primer flujo

Con la opción elegida:

1. Haz **solo las 2-3 preguntas mínimas** necesarias para ese flujo concreto (cómo lo hace hoy, qué formato quiere, algún ejemplo real si lo tiene). Nada de preguntas que no sirvan para este flujo.
2. Crea la directiva del proceso en `directives/[nombre-flujo].md` usando `directives/_template.md`.
3. Si el flujo necesita una herramienta externa (email, calendario...), anótala en `TOOLS.md` y explícale en 2 líneas cómo conectarla. Si la conexión no es inmediata, diseña el flujo para que funcione ya con lo disponible (ej: con material pegado en el chat) y deja la integración como mejora.
4. **Ejecuta el flujo una primera vez** con un caso real del usuario, o déjalo listo y pídele el primer caso real.

Este es el momento clave del setup: el usuario tiene que ver algo útil funcionando hoy, no una promesa.

---

### PASO 5 — Cierre

1. **Obligatorio:** actualiza `MEMORY.md`, sección "Estado del sistema":
   - **Inicializado:** Sí — [fecha de hoy]
   - **Última actualización:** [fecha de hoy]
   Si no se hace, el sistema intentará volver a ejecutar este protocolo en la próxima sesión.

2. **Obligatorio:** rellena en `MEMORY.md` la sección "Contexto pendiente de descubrir" con los temas que NO se preguntaron, para irlos cubriendo poco a poco (ver lista en "Descubrimiento progresivo").

3. Cierra con un resumen corto (nada de listas largas de archivos):

> "Listo. Soy [nombre] y tu primer flujo de trabajo ya está montado: [flujo].
>
> Una cosa importante: no te he preguntado todo a propósito. Iré aprendiendo de ti poco a poco mientras trabajamos — de vez en cuando te haré alguna pregunta corta cuando me falte contexto, y cada cosa que me corrijas la guardo para no repetirla. Si en cualquier momento tienes documentos, webs o procesos que pasarme, mándamelos y los digiero.
>
> Una última cosa, opcional: si quieres hablarme desde el móvil además de aquí, puedo conectarte por Telegram ahora mismo, se hace en 2 minutos. ¿Lo montamos o lo dejamos para otro día?
>
> ¿Probamos el flujo con un caso real?"

4. Si dice que sí a Telegram: sigue el protocolo completo de `skills/comunicacion/conectar-telegram/SKILL.md` ahora. Si dice que no o lo deja para más adelante: anótalo en "Contexto pendiente de descubrir" de `MEMORY.md` (puede pedirlo cuando quiera diciendo "conecta Telegram") y no insistas.

---

## Descubrimiento progresivo (después del setup)

La información que el setup ya no pregunta se recoge así, repartida en el tiempo:

### Reglas

1. **Máximo 1-2 preguntas de contexto por sesión**, y solo si son relevantes para la tarea en curso. Nunca un bloque de preguntas seguidas.
2. **Preguntar justo cuando hace falta.** Si una tarea toca un área sin contexto (una persona desconocida, una herramienta no registrada, un objetivo sin definir), preguntar lo mínimo en ese momento y guardarlo. El contexto pedido con motivo no frustra; el cuestionario sí.
3. **Capturar sin preguntar siempre que se pueda.** La mayoría del contexto sale solo en las conversaciones de trabajo: preferencias, personas, herramientas, procesos. Guardarlo al vuelo (ver `AGENT.md`, "Bucle de aprendizaje").
4. **Pedir material, no respuestas.** Si el usuario menciona una web, documento o plantilla que existe, pedírselo en vez de hacerle describirlo.
5. **Tachar de la lista.** Cada vez que se cubra un tema, actualizar "Contexto pendiente de descubrir" en `MEMORY.md`.

### Temas pendientes típicos (la lista inicial del Paso 5.2)

- Conexión a Telegram, si no se hizo en el Paso 1 (skill `conectar-telegram`)
- Herramientas que usa cada semana (completar `TOOLS.md`)
- Sus 2-3 procesos más repetitivos (candidatos a directivas nuevas)
- Objetivos a 30 días y 6 meses + métricas (`memory/objectives.md`)
- Equipo, clientes y colaboradores clave (`memory/people.md`)
- Horarios y forma de trabajar (`memory/preferences.md`)
- Si algún dominio crece mucho: ¿conviene un agente especializado? (criterio en `agents/README.md`)

---

## Post-inicialización

Una vez completado el setup, el agente opera con normalidad:
- Lee `memory/user.md` + `memory/preferences.md` + `MEMORY.md` al inicio de cada sesión
- No vuelve a preguntar información ya capturada
- Aplica el descubrimiento progresivo y el bucle de aprendizaje de `AGENT.md`
