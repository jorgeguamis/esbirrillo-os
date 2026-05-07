---
tags:
  - type/hub
  - area/[AREA_NAME]
updated:
  "{ date:YYYY-MM-DD }":
---

# [Area Name] Hub

> Mission control for [Area Name]. This page aggregates all relevant content using automated Dataview queries.

---

## Quick Access

- [[context|Context File]] (AI reads this for priorities and current state)
- [[projects/|Projects Folder]]
- [[sops/|SOPs Folder]] *(if applicable)*
- [Additional area-specific folders]

---

## Current Focus

**Top Priority:**
[Manual entry - what matters most in this area right now]

**Active Projects:**
[Manual or query-driven list]

---

## SOPs & How-Tos

```dataview
TABLE file.ctime as "Created", file.mtime as "Updated"
FROM "2. Areas/[AREA_NAME]"
WHERE contains(tags, "type/sop") OR contains(tags, "type/how-to")
SORT file.mtime DESC
```

---

## Frameworks

```dataview
TABLE file.ctime as "Created", file.mtime as "Updated"
FROM "2. Areas/[AREA_NAME]"
WHERE contains(tags, "type/framework")
SORT file.name ASC
```

---

## Active Projects

```dataview
TABLE file.ctime as "Created", file.mtime as "Updated", status
FROM "2. Areas/[AREA_NAME]/projects"
WHERE contains(tags, "type/project") AND contains(tags, "status/active")
SORT file.mtime DESC
```

---

## Related Atomic Notes

```dataview
TABLE topics as "Topics", maturity as "Maturity"
FROM "1. Atomic Notes"
WHERE contains(tags, "business/[BUSINESS_TAG]") OR contains(file.outlinks, this.file.link)
SORT file.mtime DESC
LIMIT 20
```

---

## Recent Activity

```dataview
TABLE file.mtime as "Last Updated", tags
FROM "2. Areas/[AREA_NAME]"
WHERE file.name != "Hub_[AREA_NAME]" AND file.name != "context"
SORT file.mtime DESC
LIMIT 10
```

---

## Notes

[Area-specific notes, guidelines, or reminders]

---

**Instrucciones para usar este template:**

1. **Reemplaza [AREA_NAME]:**
   - En el frontmatter: `area/business-360`, `area/personal`, etc.
   - En las queries: `"2. Areas/Business-360"`, etc.
   - En el título del archivo: `Hub_Business-360.md`, `Hub_Personal.md`, etc.

2. **Reemplaza [BUSINESS_TAG]:**
   - Para Business-360: `business/360`
   - Para Business-Business 2: `business/revolutia`
   - Para Personal/Health/etc.: Elimina la query de "Related Atomic Notes" o ajusta el filtro

3. **Ajusta las secciones según el área:**
   - Business areas: Mantén SOPs, Projects, Frameworks
   - Personal/Health: Agrega Goals, Life Map ratings, etc.
   - Learning: Agrega Books, Courses, People sections

4. **Personaliza Quick Access:**
   - Añade links a subcarpetas específicas del área
   - Añade links a goals, frameworks, o documentos clave

5. **Prueba las queries:**
   - Abre el hub en Preview mode
   - Verifica que las Dataview queries devuelvan resultados
   - Ajusta los filtros si es necesario
