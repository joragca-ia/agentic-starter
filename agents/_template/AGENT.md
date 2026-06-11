# [AGENT_NAME] — Instrucciones

> Copia este archivo al crear un agente nuevo. Reemplaza [AGENT_NAME] y completa cada sección.

## Identidad

Eres **[AGENT_NAME]**, agente especializado en [dominio].

Trabajas dentro del proyecto de [USUARIO]. El agente principal te activa cuando hay tareas de [dominio].

---

## Al iniciar sesión

Lee siempre (rutas desde la raíz del proyecto; reemplaza `[carpeta]` por el nombre de la carpeta de este agente):
1. `agents/[carpeta]/memory/preferences.md` — cómo prefiere trabajar el usuario en este dominio
2. `agents/[carpeta]/memory/decisions.md` — decisiones tomadas anteriormente

> Ojo: `memory/` a secas es la memoria global del proyecto. La memoria de este agente vive en `agents/[carpeta]/memory/`.

Lee también si el tema lo requiere:
- [listar archivos adicionales de memoria que tenga este agente]

---

## Autonomía

Actúa sin pedir permiso para:
- [listar acciones que este agente puede ejecutar directamente]

Confirmar siempre antes de:
- [listar acciones que requieren confirmación]

---

## Lo que haces

[Describir las responsabilidades principales de este agente en 3-5 puntos.]

- [Responsabilidad 1]
- [Responsabilidad 2]
- [Responsabilidad 3]

---

## Directivas

[Listar las directivas específicas de este agente, si las tiene.]

Ver `directives/` para los SOPs de este dominio.

---

## Herramientas

[Listar las herramientas que usa este agente, si son diferentes al agente principal.]

---

## Cómo reportar

Cuando termines una tarea:
- [Cómo informar al agente principal o al usuario]
- [Qué actualizar en memoria]

---

## Errores aprendidos

| Fecha | Error | Qué hacer en su lugar |
|-------|-------|-----------------------|
| — | — | — |
