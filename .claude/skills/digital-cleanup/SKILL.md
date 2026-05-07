---
name: digital-cleanup
agent: many
description: "Auditoría mensual del espacio digital: Desktop, Downloads, Obsidian, Notion, Google Drive. Reporte con métricas y recomendaciones accionables. No borra nada sin confirmación."
---

# Digital Cleanup — Auditoría Mensual del Espacio Digital

Skill de techy para mantener el sistema digital limpio, organizado y funcional.

## Agente: techy

**Principio:** "Simple systems win" — Los sistemas complejos fallan bajo estrés.

## Objetivo

Auditoría sistemática mensual con reporte de hallazgos y recomendaciones. No es limpieza manual — es diagnóstico accionable.

**Frecuencia:** 2º domingo de cada mes (o manual con `/digital-cleanup`)

## Flujo

```
1. Desktop & Downloads — conteo y alerta
  ↓
2. Obsidian — orphan notes + broken links
  ↓
3. Notion — páginas stale >90 días
  ↓
4. Trash + backup check
  ↓
5. Recomendaciones Drive + Browser (manual)
  ↓
6. Reporte en conversación
```

## Áreas y comandos Bash

### 1. Desktop & Downloads

```bash
DESKTOP_COUNT=$(ls ~/Desktop | wc -l | tr -d ' ')
DOWNLOADS_COUNT=$(ls ~/Downloads | wc -l | tr -d ' ')
OLD_DOWNLOADS=$(find ~/Downloads -type f -mtime +30 | wc -l | tr -d ' ')
echo "Desktop: $DESKTOP_COUNT | Downloads: $DOWNLOADS_COUNT | >30 días: $OLD_DOWNLOADS"
```

Alertas: Desktop >10 → limpiar | Downloads >50 → limpieza agresiva

### 2. Obsidian

```bash
VAULT="${LIFEOS_ROOT}/${VAULT_NAME}"
TOTAL=$(find "$VAULT" -name "*.md" -not -path "*/.obsidian/*" | wc -l | tr -d ' ')
echo "Total notas: $TOTAL"
```

Usar Grep para broken links y Glob para orphan notes (notas en `00. Inbox/` sin links entrantes).

### 3. Notion — Stale Pages

Usar `notion-search` para páginas con `last_edited_time` anterior a 90 días. Identificar páginas en DBs activas no tocadas. No archivar — reportar y preguntar.

### 4. Trash & Backup

```bash
TRASH_COUNT=$(ls ~/.Trash 2>/dev/null | wc -l | tr -d ' ')
LAST_BACKUP=$(tmutil latestbackup 2>/dev/null || echo "No disponible")
echo "Trash: $TRASH_COUNT | Último backup: $LAST_BACKUP"
```

Alerta: Trash >100 → recomendar vaciar | Backup >7 días → urgente

## Output

```
🧹 Digital Cleanup Report — [fecha]

📂 Desktop & Downloads
• Desktop: X items [✅ / ⚠️]
• Downloads: Y items (Z >30 días) [✅ / ⚠️]

🔗 Obsidian
• Total notas: X
• Orphan notes: Y (Z%)
• Broken links: W

📝 Notion
• Páginas stale (>90 días): X
• Recomendación: [archivar/revisar]

🗑️ Trash & Backup
• Trash: X items
• Último backup: [fecha]

☁️ Drive (manual)
• Revisa espacio en: {{USER_PRIMARY_EMAIL}}, {{USER_SECONDARY_EMAIL}}, {{USER_PERSONAL_EMAIL}}

🌐 Browser (manual)
• Revisa extensiones en chrome://extensions/ — objetivo: <10 activas

---

💡 Recomendaciones:
[Lista de acciones específicas por área]

🧠 Pregunta clave: ¿Este sistema digital facilita o frena tu ejecución?
```

## Reglas

1. **No borrar nada sin confirmación** — Reportar, recomendar, no ejecutar borrados
2. Reportar números, no opiniones — datos objetivos
3. Cada hallazgo = recomendación concreta con tiempo estimado ("15 min para archivar X")
4. Backup check obligatorio — último backup debe ser <7 días
5. Celebrar lo limpio: "Desktop: 3 items ✅ Impecable"
6. Output directo en conversación (no Telegram)

---

## Known Issues & Learnings

_This section is updated automatically as the skill encounters edge cases, errors, or improvements._

| Date | Issue/Learning | Resolution |
|------|---------------|------------|
| — | No issues recorded yet | — |
