---
description: Run quarterly review (90-120 min). Last week of March, June, September, December.
---

# Quarterly Review

Run the quarterly review — the most important review cadence for detecting multi-week patterns and strategic drift.

**Skill:** `.claude/skills/quarterly-review/SKILL.md`

## When to Run

- **Q1:** Last week of March
- **Q2:** Last week of June
- **Q3:** Last week of September
- **Q4:** Last week of December (can combine with annual review)

## Process

### Phase 1: Data Aggregation (AI, automated)
1. Load ~13 weekly reviews from the quarter
2. Load monthly reviews (up to 3)
3. Load all 7 context files + memory.md
4. Load 1-year goals from `02. Areas/personal/objetivos/Objetivos 2026.md`
5. Query Notion for quarterly task/project completion
6. Query Fireflies for quarter's meeting patterns

### Phase 2: AI Analysis
1. Goal progress vs. 1-year targets (% on track)
2. Energy vs. output analysis (where effort ≠ results)
3. Priority drift detection (stated vs. actual over 13 weeks)
4. Pattern recognition from weekly reviews (3+ occurrences)
5. Financial health summary
6. Life Map pillar trends

### Phase 3: Interactive Deep Reflection (60-90 min)
1. Present data summary
2. Walk through 11-part template with user
3. Each section: AI provides data context, user reflects
4. Detect and challenge misalignment

### Phase 4: Output
1. Write quarterly review file
2. Suggest updates to context files
3. Suggest additions to memory.md
4. Update 1-year goals if needed

## Data Sources

- Weekly reviews: `02. Areas/personal/diario/02. Weekly/YYYY-Www.md` (~13 weeks)
- Monthly reviews: `02. Areas/personal/diario/03. Monthly/YYYY-MM.md` (up to 3)
- All 7 context files
- `02. Areas/personal/memory.md`
- `02. Areas/personal/objetivos/Objetivos 2026.md` (1-year goals)
- `02. Areas/personal/frameworks/Life Map 2026.md`
- `02. Areas/personal/frameworks/Vivid Vision.md`
- Notion task databases (5)
- Google Calendar (3 accounts)
- Fireflies transcripts

## Output

File: `02. Areas/personal/diario/04. Quarterly/YYYY-Qn.md`
Template: `03. Sistema/templates/Quarterly Review.md`

## Honesty Rules

Same as weekly review but amplified:
- 13 weeks of data = no hiding from patterns
- "You said this was priority in January. It's March. 0 progress. Decision time."
- Reference memory.md patterns with quarterly evidence
- Energy vs. output analysis should be brutally honest
