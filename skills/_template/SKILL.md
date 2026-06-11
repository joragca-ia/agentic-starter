---
name: nombre-del-skill
description: Usar cuando [situación que activa este skill]. [Qué hace y qué produce, en 1-2 líneas. Esta descripción es lo que se lee para decidir si el skill aplica — clara y accionable.]
---

# [Nombre del skill]

## Qué hace

[Descripción funcional en 2-4 líneas. Qué transforma, qué produce, qué ejecuta.]

---

## Cuándo usarlo / cuándo no

**Usar cuando:**
- [Situación 1]
- [Situación 2]

**NO usar cuando:**
- [Situación donde parece aplicar pero no — y qué hacer en su lugar]

---

## Inputs

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `param1` | texto | Sí | [descripción] |
| `param2` | texto | No | [descripción] — default: `[valor por defecto]` |

---

## Proceso

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

---

## Outputs

| Resultado | Tipo | Descripción |
|-----------|------|-------------|
| `resultado1` | texto | [descripción] |

---

## Side effects

[Qué modifica externamente: archivos creados, APIs llamadas, memoria actualizada.]

Ninguno / [listar side effects]

---

## Errores frecuentes

| Error | Causa | Solución |
|-------|-------|----------|
| [error] | [causa] | [solución] |

---

## Checklist de verificación

Antes de dar el resultado por bueno:

- [ ] [Comprobación 1 — ej: el output tiene el formato esperado]
- [ ] [Comprobación 2 — ej: no se ha modificado nada fuera de lo declarado en side effects]

---

## Archivos de soporte

[Listar aquí los archivos de `references/`, `templates/` o `scripts/` de este skill, con una línea sobre qué contiene cada uno. Si no hay, eliminar esta sección.]

- `references/[tema].md` — [qué contiene]
- `templates/[nombre]` — [para qué se copia]
- `scripts/[nombre]` — [qué ejecuta]

---

## Ejemplo

**Input:**
```
[SKILL:nombre-del-skill] param1="ejemplo real" param2="otro valor"
```

**Output esperado:**
```
[resultado de ejemplo]
```

---

## Directiva relacionada

[Nombre de la directiva que usa este skill, si existe.] Ver `directives/[nombre].md`.

---

## Notas

[Limitaciones, edge cases, dependencias, contexto adicional.]
