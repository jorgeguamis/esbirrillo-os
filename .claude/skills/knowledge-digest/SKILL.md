---
name: knowledge-digest
agent: dots
description: "Curación de conocimiento para librarian: resumir URLs/contenido, conectar ideas con vault, insight del día, captura de ideas, digest semanal."
---

# Knowledge Digest

Skill de librarian para curar, conectar y sintetizar conocimiento. Cuatro modos de uso.

## Agente: librarian

**Mantra:** "Conocimiento que no se conecta ni se aplica, no existe."

## Modo 1: Resumir contenido

**Input:** URL, artículo, texto de podcast/video

**Flujo:**
1. Fetch contenido (WebFetch para URLs)
2. Extraer 3-5 puntos clave
3. Aplicación práctica al contexto actual de {{USER_FIRSTNAME}}
4. Guardar en Notion Notas DB (si relevante)

**Output:**
```
📌 [Título del contenido]

Puntos clave:
• [Punto 1]
• [Punto 2]
• [Punto 3]

Aplicación para ti:
[Contexto de {{USER_FIRSTNAME}} + cómo aplicar]

Conecta con: [[Nota A]], [[Nota B]]
```

**Notion Notas DB:** `fc7263f5-4e8b-41fd-afbf-aaf856576016`
```
notion-create-pages:
  parent: database_id "fc7263f5-4e8b-41fd-afbf-aaf856576016"
  properties:
    Título: [título]
    Concepto: [extracto accionable]
```

---

## Modo 2: Conectar con vault

**Objetivo:** Dada una idea o concepto, buscar notas relacionadas y sugerir conexiones.

**Flujo:**
1. Extraer keywords del concepto
2. Grep en vault (Atomic Notes + libros/notas)
3. Grep en Notion Notas DB (`fc7263f5-4e8b-41fd-afbf-aaf856576016`)
4. Sugerir conexiones con `[[wikilinks]]`
5. Si aplica, crear links bidireccionales

**Rutas de búsqueda:**
- `01. Atomic Notes/`
- `02. Areas/aprendizaje/libros/notas/`

---

## Modo 3: Insight del día

**Objetivo:** Un concepto de los libros de {{USER_FIRSTNAME}} aplicado al contexto actual.

**Libros disponibles:**
100M Money Models / Los 7 Hábitos / Pensar con Claridad / Esencialismo / Piense y Hágase Rico / 4HWW / Cómo Ganar Amigos / The Power of Discipline / El Libro de Copywriting / Rompe la Barrera del No / Psychology of Money / 100M Offers / 100M Leads / Storytelling Salvaje / Traffic Secrets

**Criterios:**
1. Relevante al contexto actual (proyectos activos, decisiones pendientes, retos)
2. No repetir libro/concepto de los últimos 7 días
3. Aplicación práctica clara

**Output:**
```
💡 Insight del día — [Libro] ([Autor])

"[Cita/concepto clave]"

📌 Aplicación para ti:
[Contexto actual de {{USER_FIRSTNAME}} + cómo aplicar el concepto hoy]

🔗 Conecta con: [notas/frameworks relacionados del vault]
```

---

## Modo 4: Digest semanal

**Objetivo:** Resumen de lo aprendido/capturado en la semana (viernes o domingo).

**Fuentes:**
- Daily notes de la semana (lunes-domingo): Read cada nota de `02. Areas/personal/diario/01. Daily/`
- Notas en `00. Inbox/` creadas esta semana (Glob con mtime filtrado)
- Notion Books DB (`2af048b8-fda3-42a5-9f86-ab6f17879e74`)

**Output:**
```
📚 Knowledge Digest — Semana [DD-DD MMM]

🔥 Highlights:
• [Top 3 insights/aprendizajes de la semana]

📖 Contenido consumido:
• [Lista de fuentes]

💡 Ideas capturadas:
• [Notas nuevas en Inbox]

🔗 Conexiones nuevas:
• [Nuevas relaciones entre conceptos]

⏭️ Para profundizar:
• [Temas pendientes o interesantes para continuar]
```

---

## Modo 5: Captura rápida de idea

**Input:** Idea espontánea de {{USER_FIRSTNAME}} (no lectura específica)

**Flujo:**
1. Identificar tipo: reflexión / acción / proyecto / insight
2. Estructurar (título, concepto, aplicación, siguiente paso)
3. Guardar en:
   - Daily note (reflexiones/contexto del día)
   - `00. Inbox/[título].md` (conceptos densos, frameworks)
   - Notion Notas DB (si es idea accionable)

**Template nota atómica:**
```markdown
---
tags:
  - type/zettel
  - maturity/seedling
  - topic/[área]
created: DD-MM-YYYY
---
# [Título claro]

[Descripción breve del concepto]

## Contexto

[Por qué es relevante ahora]

## Aplicación

[Cómo usarlo]

## Conexiones

- [[nota-relacionada-1]]
```

---

## Notion DBs

| DB | database_id |
|----|-------------|
| Notas | `fc7263f5-4e8b-41fd-afbf-aaf856576016` |
| Bloques de notas | `3571916e-50ae-44a6-9e89-98aa0222ce43` |
| Books | `2af048b8-fda3-42a5-9f86-ab6f17879e74` |

## Reglas

1. Contexto siempre — ningún insight sin aplicación práctica al contexto de {{USER_FIRSTNAME}}
2. Conexiones > contenido aislado — siempre buscar relaciones con vault
3. Accionable > teórico — extractos que se puedan aplicar HOY
4. No duplicar — buscar si ya existe concepto similar antes de crear
5. Brevedad — insights máx 3-5 líneas, extractos máx 3-5 puntos

---

## Known Issues & Learnings

_This section is updated automatically as the skill encounters edge cases, errors, or improvements._

| Date | Issue/Learning | Resolution |
|------|---------------|------------|
| — | No issues recorded yet | — |
