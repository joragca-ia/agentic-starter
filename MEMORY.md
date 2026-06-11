# Memoria activa

> Índice del sistema de memoria. Se actualiza al final de sesiones relevantes.
> Los archivos detallados están en `memory/`.

---

## Estado del sistema

- **Inicializado:** No (ejecutar STARTUP.md)
- **Ultima actualización:** —
- **Sesiones activas:** —

---

## Archivos core (leer siempre al inicio)

- [memory/user.md](memory/user.md) — perfil del usuario
- [memory/preferences.md](memory/preferences.md) — preferencias de trabajo y comunicación

---

## Archivos contextuales (cargar según el tema)

- [memory/objectives.md](memory/objectives.md) — objetivos y métricas clave
- [memory/active_projects.md](memory/active_projects.md) — proyectos en curso y su estado
- [memory/people.md](memory/people.md) — contexto de contactos y colaboradores
- [memory/decisions.md](memory/decisions.md) — decisiones importantes tomadas

---

## Logs diarios

Los resúmenes de sesión se guardan en `memory/daily_log/YYYY-MM-DD.md`.
Son la memoria más reciente y se deben leer cuando se necesita contexto de lo trabajado ayer o esta semana.

---

## Protocolo de actualización

Al final de una sesión relevante:
1. Actualizar los archivos de memoria que hayan cambiado
2. Actualizar este índice si cambió el estado del sistema
3. Si el contexto de la sesión fue largo y complejo, crear `memory/daily_log/YYYY-MM-DD.md` con un resumen

---

## Protocolo de compactación

Cuando el contexto de la conversación sea muy largo (el modelo te avisará o lo notarás por la lentitud):
1. Crear `memory/daily_log/YYYY-MM-DD.md` con todo el contexto relevante de la sesión
2. Actualizar los archivos de memoria afectados
3. Iniciar nueva sesión — la próxima vez, leer el daily_log para recuperar el hilo
