# Sistema de memoria

El agente tiene memoria persistente entre sesiones gracias a estos archivos. Se leen al inicio de cada sesión y se actualizan cuando cambia información relevante.

---

## Archivos core (leer siempre al inicio)

| Archivo | Contiene |
|---------|----------|
| `user.md` | Perfil del usuario: quién es, a qué se dedica, contexto profesional |
| `preferences.md` | Cómo prefiere trabajar: idioma, tono, horarios, estilo de respuesta |

## Archivos contextuales (cargar según el tema)

| Archivo | Cuándo cargarlo |
|---------|-----------------|
| `objectives.md` | Cuando se habla de metas, proyectos o estrategia |
| `active_projects.md` | Cuando se trabaja en proyectos concretos |
| `people.md` | Cuando se mencionan personas, clientes o colaboradores |
| `decisions.md` | Cuando se necesita contexto de decisiones pasadas |

## Logs diarios

`daily_log/YYYY-MM-DD.md` — resúmenes de sesión. Leer el más reciente cuando se necesita recuperar el hilo de lo trabajado anteriormente.

---

## Cómo actualizar la memoria

El agente actualiza estos archivos automáticamente cuando aprende algo nuevo. Si el usuario menciona algo importante que el agente debería recordar, este lo captura sin que se lo pidan.

Para añadir información manualmente: editar el archivo directamente.

---

## Reglas de higiene

La memoria se inyecta en cada sesión: cada línea inútil es un coste permanente. Estas reglas la mantienen sana.

**1. Hechos declarativos, nunca instrucciones.**
"El usuario prefiere respuestas cortas" ✓ — "Responde siempre corto" ✗. "El proyecto usa la herramienta X para tareas" ✓ — "Crea las tareas siempre con X" ✗. Una frase imperativa se relee como orden en sesiones futuras y puede pisar lo que el usuario pide hoy.

**2. Solo hechos durables.**
Si un dato estará obsoleto en una semana (estado de una tarea, "terminé X", contadores, fases), no pertenece a la memoria: va al daily log. Prioriza lo que evita que el usuario tenga que corregirte o recordarte algo otra vez — esa es la memoria más valiosa.

**3. Los procedimientos van a skills o directivas, no a memoria.**
La memoria dice quién es el usuario y cómo están las cosas. El "cómo se hace X" vive en `skills/` y `directives/`.

**4. Memoria acotada.**
Si un archivo de memoria supera ~40 líneas de contenido, consolidar antes de añadir: fusionar entradas que se solapan, borrar las obsoletas. Acumular sin curar degrada todas las sesiones futuras.

**5. Qué no guardar nunca.**
Fallos del entorno, afirmaciones negativas sobre herramientas ("X no funciona"), errores transitorios ya resueltos, narrativas de tareas puntuales. El detalle completo está en `AGENT.md`, sección "Qué NO capturar".

---

## Cómo añadir archivos de memoria

Si el proyecto crece y necesitas un archivo de memoria específico (ej: `clients.md`, `content_strategy.md`), créalo en esta carpeta y añade una entrada en `MEMORY.md` para que el agente sepa cuándo cargarlo.
