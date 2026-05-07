---
skill: quarterly-review
description: Deep quarterly review (90-120 min) analyzing 13 weeks of data, detecting strategic drift, and setting next quarter's direction
trigger: "/quarterly-review" — last week of March, June, September, December
---

# Quarterly Review

The quarterly review is the most important review cadence for detecting multi-week patterns and strategic drift. It synthesizes ~13 weekly reviews, up to 3 monthly reviews, and all context files into a comprehensive assessment.

**Target time:** 90-120 minutes
**Frequency:** 4x/year (end of March, June, September, December)
**First execution:** Q1 2026 — last week of March 2026

---

## When to Use

- **Q1 Review:** Last week of March
- **Q2 Review:** Last week of June
- **Q3 Review:** Last week of September
- **Q4 Review:** Last week of December (can combine with annual review prep)

**Trigger:** `/quarterly-review` command or user requests quarterly review

---

## Data Sources

### Required (Obsidian)

**Weekly Reviews (~13 weeks):**
- `02. Areas/personal/diario/02. Weekly/YYYY-Www.md`
- Calculate week range: Q1 = W01-W13, Q2 = W14-W26, Q3 = W27-W39, Q4 = W40-W52
- Extract: TOP 2 completion rates, energy patterns, wins, frictions, pattern alerts

**Monthly Reviews (up to 3):**
- `02. Areas/personal/diario/03. Monthly/YYYY-MM.md`
- Q1 = Jan, Feb, Mar; Q2 = Apr, May, Jun; etc.
- Extract: Monthly themes, patterns, business metrics

**All 7 Context Files:**
- `02. Areas/personal/Personal.md`
- `02. Areas/business_primary/{{BUSINESS_PRIMARY}}.md`
- `02. Areas/business_secondary/{{BUSINESS_SECONDARY}}.md`
- `02. Areas/salud/Health.md`
- `02. Areas/aprendizaje/Learning.md`
- `02. Areas/finanzas/Finances.md`
- `02. Areas/investigacion/Research.md`

**Pattern Memory:**
- `02. Areas/personal/memory.md` — Known patterns spanning months/years

**Goals:**
- `02. Areas/personal/objetivos/Objetivos 2026.md` — 1-year goals
- `02. Areas/personal/objetivos/Objetivos 2029.md` — 3-year goals (if exists)

**Frameworks:**
- `02. Areas/personal/frameworks/Life Map 2026.md` — Pillar ratings
- `02. Areas/personal/frameworks/Vivid Vision.md` — 3-year vision

**Relationships:**
- `02. Areas/personal/relaciones/` — Key relationship files

### External Sources (MCP)

**Notion Task Databases (5):** Query quarterly task completion rates, delayed projects
**Google Calendar (3 accounts):** Quarterly meeting hours by area, deep work trends
**Fireflies:** Quarterly meeting patterns, client interaction frequency

---

## Process

### Phase 1: Data Aggregation (AI, automated - 5 min)

1. **Get current date and determine quarter:**
   ```bash
   date "+%A, %B %d, %Y"
   # Determine: Q1 (Jan-Mar), Q2 (Apr-Jun), Q3 (Jul-Sep), Q4 (Oct-Dec)
   ```

2. **Load weekly reviews** — Read all available weekly reviews for the quarter
   - Count: How many weeks have reviews? (target: 13/13)
   - Extract from each: TOP 2 completion %, energy averages, pattern alerts, business metrics

3. **Load monthly reviews** — Read 3 monthly reviews for the quarter

4. **Load all context files + memory.md + goals + frameworks**

5. **Query Notion** — Quarterly task completion, delayed projects, habit trends

6. **Query Calendar** — Quarterly meeting hours by account

7. **Query Fireflies** — Key meetings/decisions of the quarter

### Phase 2: AI Analysis (automated - 10 min)

**Goal Progress Assessment:**
- For each 1-year goal, calculate % progress based on 13 weeks of evidence
- Flag: Goals with 0 progress (🔴), goals behind schedule (⚠️), goals on track (✅)

**Energy vs. Output Matrix:**
- Aggregate energy data from weekly reviews
- Map: Where energy went vs. where results came from
- Identify: High energy / low output areas (waste) and low energy / high output areas (leverage)

**Priority Drift Detection:**
- Compare context file stated priorities at start of quarter vs. actual weekly execution
- Calculate: % of weeks each priority received meaningful time
- Flag: Priorities stated but executed <25% of weeks

**Pattern Synthesis:**
- From weekly review pattern alerts, identify patterns that appeared 3+ times
- Cross-reference with memory.md known patterns
- New patterns: Appeared this quarter but not in memory.md

**Financial Summary:**
- Revenue by business area (if trackable)
- Expense trends
- Progress toward annual financial targets

**Life Map Trend:**
- Compare pillar ratings across monthly reviews (if available)
- Identify: Rising, stable, declining pillars

**Relationship Health:**
- Key interactions from Fireflies/weekly reviews
- Energy givers vs. energy drains

### Phase 3: Interactive Review (60-90 min)

Walk through the quarterly review template (11 parts) with the user.

**For each section:**
1. AI presents relevant data and analysis
2. User reflects and provides input
3. AI challenges misalignment and patterns

**Template sections:**
1. **Overview** — Summarize quarter, pride, regret
2. **Goal Progress** — {{BUSINESS_PRIMARY}}, {{BUSINESS_SECONDARY}}, Personal goals assessment
3. **Business Performance** — Revenue, clients, key wins/challenges
4. **Energy vs. Output** — Where effort ≠ results
5. **Misalignment Detection** — Stated priorities vs. actual time
6. **Life Map Check** — Pillar ratings and trends
7. **Financial Health** — Quarterly financial summary
8. **Relationships** — Energy givers/drains, neglected relationships
9. **Pattern Recognition** — Repeated + new patterns
10. **Strategic Adjustments** — STOP / START / CONTINUE
11. **Next Quarter Focus** — Theme, TOP 3, success/failure criteria

### Phase 4: Generate Output (AI, automated - 5 min)

1. **Write quarterly review file:**
   - Location: `02. Areas/personal/diario/04. Quarterly/YYYY-Qn.md`
   - Based on template: `03. Sistema/templates/Quarterly Review.md`

2. **Suggest context file updates:**
   - If priorities shifted → suggest edits to relevant context files
   - If new patterns detected → suggest additions to memory.md

3. **Suggest goal updates:**
   - If goals are no longer relevant → flag for removal/adjustment
   - If new goals emerged → suggest adding to objectives

4. **Update Life Map:**
   - Suggest new pillar ratings based on quarterly evidence

### Phase 5: Confirmation

1. Show complete review to user
2. Ask: "Review ready? Any adjustments needed?"
3. Once approved → Write file
4. Execute context file updates if approved
5. Execute memory.md updates if approved

---

## Output

### File Location
`02. Areas/personal/diario/04. Quarterly/YYYY-Qn.md`
Example: `02. Areas/personal/diario/04. Quarterly/2026-Q1.md`

### Template
Use `03. Sistema/templates/Quarterly Review.md` — 11-part structure with Quick Metrics table.

**Note:** Update broken wikilinks in template:
- `[[02. Areas/personal/context|Personal Context]]` → `[[02. Areas/personal/Personal|Personal Context]]`
- `[[{{BUSINESS_PRIMARY}} Consulting_Context|{{BUSINESS_PRIMARY}} Context]]` → `[[02. Areas/business_primary/{{BUSINESS_PRIMARY}}|{{BUSINESS_PRIMARY}} Context]]`
- `[[Business_Secondary_Context|{{BUSINESS_SECONDARY}} Context]]` → `[[02. Areas/business_secondary/{{BUSINESS_SECONDARY}}|{{BUSINESS_SECONDARY}} Context]]`
- `[[02. Areas/personal/context|Memory/Patterns]]` → `[[02. Areas/personal/memory|Memory/Patterns]]`

---

## Honesty Principles (AMPLIFIED for Quarterly)

**13 weeks of data = no hiding from patterns.**

The quarterly review has the most data and therefore the least room for self-deception. Apply these rules strictly:

- "You said this was priority in January. It's March. 0 progress. Decision time: commit or remove."
- "This pattern appeared in 8 of 13 weekly reviews. It's not an event, it's your default behavior."
- "Energy went to X (40% of quarter) but results came from Y (15% of quarter). You're working hard on the wrong thing."
- "Revenue target was €X for this quarter. Actual: €Y. Gap: Z%. What changes?"

**Pattern Alerts at Quarterly Scale:**
- Weekly pattern (3+ instances in a week) = alert
- Quarterly pattern (3+ instances across weeks) = systemic issue requiring structural change
- Reference memory.md known patterns with quarterly evidence count

**Goal Honesty:**
- Goals with 0 progress for an entire quarter should be challenged: "Is this a real goal or a fantasy?"
- Goals that feel like obligations (user says so in reflection) should be questioned: "Whose goal is this?"
- New goals that emerged organically from actions > stated goals that got no time

---

## Error Handling

**Missing weekly reviews:** Note coverage: "X/13 weeks reviewed (Y%)"
- If <8/13 weeks → "Low coverage — quarterly patterns less reliable"
- Continue with available data

**Missing monthly reviews:** Skip monthly aggregation, rely on weekly data

**Notion/Calendar/Fireflies offline:** Graceful degradation — mark sections as "Data unavailable"

**First quarterly review (Q1 2026):** No previous quarter to compare. Use available weekly reviews (may be <13) and set baseline for future comparisons.

---

## Integration with Other Reviews

**Inputs:** ~13 weekly reviews + 3 monthly reviews
**Outputs:** Informs annual review (Q4 feeds directly into annual)
**Updates:** Context files, memory.md, 1-year goals, Life Map
**Next:** First quarterly review = Q1 2026 (last week of March)

---

## Known Issues & Learnings

_This section is updated automatically as the skill encounters edge cases, errors, or improvements._

| Date | Issue/Learning | Resolution |
|------|---------------|------------|
| — | No issues recorded yet | — |
