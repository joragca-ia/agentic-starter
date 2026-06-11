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

**Paso 2.** Escribe en el chat:

```
inicializa el proyecto
```

**Paso 3.** El agente te hará preguntas durante 5-10 minutos. Responde con tranquilidad: cuanto más cuentes, mejor se configurará el sistema.

---

## Qué va a pasar durante el setup

El agente te preguntará sobre:
1. Quién eres y a qué te dedicas
2. Para qué quieres este sistema
3. Qué herramientas usas en tu trabajo
4. Tus procesos más repetitivos
5. Tus objetivos
6. Si quieres uno o varios agentes especializados
7. Cómo se va a llamar tu agente y qué personalidad tendrá

Al terminar, habrá creado y rellenado automáticamente todos los archivos de configuración.

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
