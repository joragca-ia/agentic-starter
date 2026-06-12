# Guía de inicio — Léeme primero

Bienvenido. Este es tu sistema de agente de IA personal, listo para configurarse a tu medida.

---

## Qué es esto

Una carpeta con todo lo que necesita un agente de IA para trabajar contigo de forma inteligente y persistente: memoria, procesos documentados, herramientas configuradas y personalidad propia.

Además, el sistema **aprende con el uso**: cuando corriges al agente o resolvéis algo juntos, lo captura para que la próxima vez salga bien a la primera. A los 3 meses trabaja notablemente mejor que el primer día.

No necesitas saber programar. Todo funciona desde el chat.

---

## Cómo empezar

**Paso 1.** Abre esta carpeta con Claude Code. Tienes tres formas de hacerlo, elige la que te resulte más cómoda:

- **Aplicación de escritorio de Claude Code:** ábrela y selecciona "Open folder" (o "Abrir carpeta") apuntando a esta carpeta
- **VS Code:** instala la extensión "Claude Code", abre esta carpeta en VS Code y abre el panel de Claude
- **Terminal:** navega hasta esta carpeta y ejecuta el comando `claude`

> Lo importante es que el asistente tenga acceso de lectura y escritura a esta carpeta: necesita poder crear y editar los archivos de configuración.

**Paso 2.** Escribe en el chat el prompt que corresponda a tu caso:

**Si es un proyecto nuevo** (carpeta vacía o solo con los archivos de esta plantilla):
```
inicializa el proyecto
```

**Si ya tienes un proyecto en marcha** (carpeta con archivos tuyos, código, documentos, etc.):
```
Tengo un proyecto existente en esta carpeta. Aplica el sistema de agente encima de lo que ya hay: no sobreescribas ningún archivo mío, adapta la configuración a lo que encuentres, y cuando acabes marca el sistema como inicializado en MEMORY.md. Sigue el protocolo de STARTUP.md adaptado a este contexto.
```

**Paso 3.** El setup dura menos de 10 minutos y termina con tu primer flujo de trabajo funcionando.

---

## Qué va a pasar durante el setup

1. **Un par de preguntas básicas:** tu nombre, a qué te dedicas, qué quieres conseguir y cómo se va a llamar tu agente. Nada más.
2. **Tus materiales, si los tienes:** web, documentos de marca, procesos escritos... El agente los lee y aprende solo, en vez de preguntártelo todo. Si no tienes nada a mano, no pasa nada.
3. **Eliges tu primer flujo de trabajo:** el agente te propone 4-6 cosas concretas que puede hacer ya por ti, adaptadas a tu caso. Eliges una y la deja funcionando.

El resto de información (herramientas, procesos, equipo, objetivos a largo plazo) el agente la irá aprendiendo poco a poco mientras trabajáis: alguna pregunta corta de vez en cuando, justo cuando le haga falta. Nunca un cuestionario.

---

## Cómo usar el sistema después

Habla con tu agente como lo harías con un colaborador:

- "¿Qué tengo pendiente esta semana?"
- "Ayúdame a redactar un email para [cliente]"
- "Documenta este proceso que te voy a describir"
- "Crea una tarea para [proyecto]"
- "Resume lo que hablamos ayer"

El agente recuerda el contexto entre sesiones gracias a los archivos de `memory/`.

---

## Cómo crecer el sistema

Con el tiempo puedes ir añadiendo:

- **Directivas** en `directives/` — para documentar procesos que se repiten
- **Skills** en `skills/` — para capacidades atómicas reutilizables
- **Agentes especializados** en `agents/` — para dominios con mucha complejidad propia

Cada carpeta tiene un `README.md` que explica cómo hacerlo.

---

## Archivos del sistema

| Archivo | Para qué |
|---------|----------|
| `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` | Punto de entrada que carga el LLM al abrir el proyecto (copias idénticas) |
| `AGENT.md` | Instrucciones del agente (el "cerebro") |
| `STARTUP.md` | Protocolo de inicialización |
| `IDENTITY.md` | Nombre y descripción del agente |
| `SOUL.md` | Personalidad y valores del agente |
| `MEMORY.md` | Índice de memoria activa |
| `TOOLS.md` | Herramientas configuradas |
| `HEARTBEAT.md` | Tareas recurrentes automáticas |
| `AGENTTEAM.md` | Registro de agentes del proyecto |
| `BOOTSTRAP.md` | Instrucciones para cuando el agente reinicia sin contexto |
| `memory/` | Archivos de memoria persistente |
| `directives/` | Procesos documentados (SOPs) |
| `skills/` | Capacidades atómicas |
| `agents/` | Agentes especializados |
