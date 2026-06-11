# Sistema de directivas

Una directiva es un SOP (Standard Operating Procedure) escrito en Markdown. Es la memoria procedimental del sistema: le dice al agente qué hacer y cómo hacerlo paso a paso en situaciones específicas.

---

## Cuándo crear una directiva

Crea una directiva cuando:
- Un proceso se repite más de 2 veces
- El agente necesita instrucciones específicas para hacerlo bien
- Hay pasos que no son obvios o que implican decisiones concretas
- Quieres que el proceso sea consistente siempre, independientemente del contexto

No crees una directiva para:
- Tareas de una sola vez
- Procesos que cambian constantemente
- Cosas que el agente puede inferir del contexto

---

## Tipos de directivas

**Protocolo de herramienta:** Cómo usar una herramienta o integración específica (ej: `gmail_protocol.md`, `notion_protocol.md`)

**Workflow end-to-end:** Un proceso completo de principio a fin (ej: `publicar_contenido.md`, `onboarding_cliente.md`)

**Criterio de decisión:** Cómo decidir algo en situaciones recurrentes (ej: `priorizar_tareas.md`, `responder_leads.md`)

---

## Cómo crear una directiva

**Paso 1.** Copia `_template.md` y renómbralo con el nombre del proceso (en minúsculas, con guiones):
```
directives/publicar-contenido.md
directives/responder-emails.md
directives/onboarding-cliente.md
```

**Paso 2.** Rellena las secciones del template.

**Paso 3.** No es necesario registrarla en ningún índice: el agente explora `directives/` cuando necesita instrucciones sobre un proceso.

---

## Template

Ver `_template.md`.
