---
description: Run weekly review + plan next week (30-40 min combined). Sunday evening or Monday morning.
---

# Weekly Review & Planning

Run the combined weekly review and planning workflow.

**Skill:** `.claude/skills/weekly-review/SKILL.md`

## Process

### REVIEW PHASE (20 min)
1. **Data Collection** — Load daily notes (Mon-Sun), context files, memory.md, _Tasks.md, Notion habits/tasks, Google Calendar, Fireflies
2. **Data Analysis** — Calculate TOP 2 completion, energy patterns, habit rates, meeting hours, priority gaps, commitment gaps
3. **User Q&A** — Present data summary, ask 5 reflection questions, follow up on gaps/patterns

### PLANNING PHASE (10-15 min)
4. **Generate Plan** — Suggest TOP 5 for next week, calendar preview, brainstorm triage
5. **Confirmation** — Review + approve, write file

## Pre-Flight (CRITICAL)

1. **Get date from system** — `date "+%A, %B %d, %Y"` (NEVER mental math)
2. **Calculate week boundaries** — Use system commands, NEVER calculate manually
3. **Check if review exists** — `02. Areas/personal/diario/02. Weekly/YYYY-Www.md`

## Data Sources

Read ALL before starting:
- `02. Areas/personal/Personal.md`
- `02. Areas/business_primary/{{BUSINESS_PRIMARY}}.md`
- `02. Areas/business_secondary/{{BUSINESS_SECONDARY}}.md`
- `02. Areas/salud/Health.md`
- `02. Areas/aprendizaje/Learning.md`
- `02. Areas/finanzas/Finances.md`
- `02. Areas/investigacion/Research.md`
- `02. Areas/personal/memory.md` (pattern tracking)
- `_Tasks.md` (brainstorm items)
- Daily notes: `02. Areas/personal/diario/01. Daily/DD-MM-YYYY.md` (7 days)

## Output

File: `02. Areas/personal/diario/02. Weekly/YYYY-Www.md`
Template: `03. Sistema/templates/Weekly Review.md`

## Honesty Rules

- Call out drift between stated priorities and actual actions
- Reference {{USER_FIRSTNAME}}'s own rules from memory.md
- Use data, not feelings: "6 hours {{BUSINESS_SECONDARY}}, 4 hours {{BUSINESS_PRIMARY}} — ratio is 60/40, goal is 30/70"
- Pattern detected 3+ times = alert with environmental fix recommendation
