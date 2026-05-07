---
skill: weekly-review
description: Combined weekly review + planning in 30-40 min with AI-generated data summaries
trigger: "/weekly-review" or "/weekly-plan" (alias) — Sunday evening or Monday morning
---

# Weekly Review & Planning

Combined skill: Review the current week AND plan the next week in one session.

**Phase 1 (Review):** AI auto-generates data summary from all sources, user answers 5 core reflection questions, AI structures review.
**Phase 2 (Planning):** AI generates next week's plan based on review data, gaps, patterns, and context files.

**Target time:** 30-40 minutes total
**Triggers:** `/weekly-review` (primary), `/weekly-plan` (alias — same skill)

---

## When to Use

**Recommended timing:**
- **Sunday evening** (end of week, review + plan for next)
- **Monday morning** (review → plan sequentially)

**Trigger methods:**
- `/weekly-review` or `/weekly-plan` command
- Automatic suggestion if Sunday and no review exists for current week
- User explicitly asks for weekly review or weekly plan

---

## Data Sources

### Required

**All 7 Context Files:**
- `02. Areas/personal/Personal.md`
- `02. Areas/business_primary/{{BUSINESS_PRIMARY}}.md`
- `02. Areas/business_secondary/{{BUSINESS_SECONDARY}}.md`
- `02. Areas/salud/Health.md`
- `02. Areas/aprendizaje/Learning.md`
- `02. Areas/finanzas/Finances.md`
- `02. Areas/investigacion/Research.md`

**Extract from each:** Stated TOP 3 priorities, active projects, energy patterns

**Daily Notes (This Week):**
- `02. Areas/personal/diario/01. Daily/` - All 7 days from Monday-Sunday
- Date format: DD-MM-YYYY (e.g., 20-01-2026.md to 26-01-2026.md)
- Extract: TOP 2 priorities, completion status, energy levels, wins, frictions, meeting mentions

**Pattern Memory (CRITICAL):**
- `02. Areas/personal/memory.md` - Known patterns to cross-reference
- Extract: Known anti-patterns (procrastination loop, decision delay, betting unproven over proven)
- Use for: Pattern alerts in review + proactive guards in planning

**Task Brainstorm:**
- `_Tasks.md` - Brain dump items organized by urgency
- Check: Incomplete items from urgent/important sections
- Carry over or drop during planning phase

### External Sources (MCP)

**Notion Habit Tracker:** ✅ ACTIVE
- Database: `46964c9bd3e645fcb80e3622e245938b`
- Query last 7 days via `mcp__notion__notion-database-query`
- Extract: All 16 habit completion rates

**Notion Task Databases (5):** ✅ ACTIVE
- Segundo Cerebro — Proyectos: `303b8a2f-e94e-4b6e-b120-1f62142d3be3`
- Segundo Cerebro — Tareas: `195101bc-423c-49c8-bcf6-fc84879f8b3c`
- {{BUSINESS_PRIMARY}} Projects: `2338eff7-5947-8156-b6cc-e6b40e9b1fac`
- {{BUSINESS_PRIMARY}} Project Tasks: `2338eff7-5947-81a9-a627-ef64b1b5209b`
- {{BUSINESS_PRIMARY}} Internal Tasks: `2338eff7-5947-81f1-bdc2-cdc8b31d65aa`

**Google Calendar:** ✅ ACTIVE
- Accounts: {{USER_PRIMARY_EMAIL}}, {{USER_SECONDARY_EMAIL}}, {{USER_PERSONAL_EMAIL}}
- Query last 7 days + next 7 days
- Extract: Meeting hours by calendar, deep work blocks, next week schedule

**Fireflies:** ✅ ACTIVE
- Query last 7 days via `mcp__fireflies__fireflies_get_transcripts`
- Extract: Client calls, action items, key decisions

---

## Process Overview

### REVIEW PHASE (20 min)

#### Phase 1: Data Collection (AI, automated - 2 min)

1. Get current date and week number (use system `date` command — NEVER mental math)
2. Calculate date range (Monday-Sunday of current week)
3. Load all data sources in parallel:
   - Read 7 daily notes from `02. Areas/personal/diario/01. Daily/`
   - Query Notion habits
   - Query Notion task databases (5)
   - Query Calendar events (3 accounts)
   - Query Fireflies transcripts
   - Read all 7 context files
   - Read `02. Areas/personal/memory.md`
   - Read `_Tasks.md`

#### Phase 2: Data Analysis (AI, automated - 3 min)

1. Calculate TOP 2 completion rate
2. Calculate energy averages and deltas
3. Calculate habit completion rates (via Notion)
4. Calculate meeting time by area (via Calendar)
5. Identify deep work blocks
6. Extract meeting summaries (via Fireflies)
7. Detect patterns vs. memory.md
8. Calculate priority gaps (context stated priorities vs. actual daily execution)
9. Cross-reference Fireflies action items with Notion tasks (commitment gaps)

#### Phase 3: User Q&A (Interactive - 10-15 min)

**AI shows data summary (Part 1), then asks 5 core questions:**

1. "Based on your completed TOP 2s [list], what actually moved the needle this week?"
2. "What was noise or time waste? (AI suggests: [activities with low energy/low completion])"
3. "Your observations — any new patterns you noticed?"
4. "{{BUSINESS_PRIMARY}}: What's working / what's stuck / next week's #1 focus?"
5. "{{BUSINESS_SECONDARY}}: What's working / what's stuck / next week's #1 focus?"

**AI asks follow-up based on gap detection:**
- "Priority X had 0 time this week but it's in your context file. Still a priority?"
- "Pattern Y appeared 3 times (evidence: [dates]). Acknowledge or environmental fix?"

### PLANNING PHASE (10-15 min)

#### Phase 4: Generate Plan (AI, automated - 3 min)

Based on ALL review data + user reflections:

1. **Suggest TOP 5 for next week** based on:
   - Stated priorities from context files
   - Incomplete TOP 2s from this week
   - Action items from Fireflies not in system
   - Gap areas needing attention
   - Overdue Notion tasks
   - Incomplete _Tasks.md items

2. **One-sentence week theme** (what makes next week successful?)

3. **For each priority:**
   - Why it matters (connection to annual goal)
   - Done when (specific outcome)
   - Time needed (hours)
   - Best day (based on calendar + energy patterns)

4. **What to say NO to** (noise, time wasters, pattern triggers)

5. **Calendar preview:**
   - Fixed commitments from Google Calendar
   - Available deep work blocks
   - Meeting load analysis (flag if >40%)

6. **Brainstorm items triage:**
   - From _Tasks.md: carry over, drop, or defer each incomplete item

#### Phase 5: Confirmation (Interactive - 5 min)

1. Show complete review + plan to user
2. Ask: "Review + plan ready or need adjustments?"
3. If adjustments → Edit specific sections
4. Once approved → Write to weekly review file
5. Update `_Tasks.md` "Last reviewed" date

**Total time: 30-40 minutes**

---

## Output

### File Location

`02. Areas/personal/diario/02. Weekly/{{YYYY-Www}}.md`
Example: `02. Areas/personal/diario/02. Weekly/2026-W06.md`

### Template

Use the template at `03. Sistema/templates/Weekly Review.md` as the base structure.
The template already includes both review (Parts 1-4) and planning (Part 5) sections.

---

## Priority Gap Detection Logic

### How to Detect Gaps

For each of the 7 context files, extract stated TOP 3 priorities and compare to daily note execution:

**HIGH gap (🔴):** Stated priority with 0 execution time all week
**MEDIUM gap (⚠️):** Stated priority with <20% of expected time
**LOW gap (🟡):** Minor misalignment, <80% of expected time
**ALIGNED (✅):** Priority with >60% time

### Pattern Check (from memory.md)

Compare weekly execution to KNOWN patterns:

**Procrastination Pattern:**
- Trigger: Phone + ambiguity + multiple options → avoidance
- Check: Mentioned procrastination in daily notes? Incomplete TOP 2s? Planning > executing?

**Decision Delay Pattern:**
- Trigger: Confrontation avoidance, sunk cost thinking
- Check: Pending hard conversations? 48-hour rule violated?

**Betting Unproven Over Proven:**
- Pattern: Novelty bias ({{BUSINESS_SECONDARY}}/setup) vs. revenue focus ({{BUSINESS_PRIMARY}} outreach)
- Check: {{BUSINESS_SECONDARY}} hours vs. {{BUSINESS_PRIMARY}} hours ratio

**Strength Utilization:**
- Known strengths: Creativity, charisma, teaching, common sense, learning agility
- Check: Did you leverage strengths or fight weaknesses?

### Commitment Gaps (from Fireflies)

- Extract action items from meeting transcripts
- Cross-reference with Notion tasks
- Flag: commitments made but NOT captured in system

---

## Notion Query Patterns

### Overdue Tasks
```
Use Skill('Notion:notion-database-query') with:
- Each of 5 database IDs
- Filter: Tasks where Status != "Done" AND Due date < today
- Group by: Revenue impact ({{BUSINESS_PRIMARY}}) vs. Personal
```

### Delayed Projects
```
Query projects where Status = Active AND Last Updated > 14 days
Extract: Project name, last update, revenue at risk
```

### Completion Rate
```
Count: Tasks completed this week / total with due dates this week
By workspace: {{BUSINESS_PRIMARY}} vs. Personal
Flag: If <60% (execution problem)
```

### Next Week's Load
```
Tasks with due dates in next 7 days
Estimate total time needed
Compare to available calendar time
```

---

## Google Calendar Query Patterns

### Last Week's Time Analysis
```
mcp__google-workspace__list_events with:
- 3 accounts: {{USER_PRIMARY_EMAIL}}, {{USER_SECONDARY_EMAIL}}, {{USER_PERSONAL_EMAIL}}
- timeMin: Monday of current week
- timeMax: Sunday of current week
Calculate: Total meeting hours by calendar, % of 40-hour week
```

### Next Week's Schedule
```
timeMin: Monday of next week
timeMax: Sunday of next week
Identify: Fixed commitments, deep work blocks (≥2h gaps), total committed hours
```

---

## Fireflies Query Patterns

### Recent Meetings
```
mcp__fireflies__fireflies_get_transcripts with:
- fromDate: Monday of current week (YYYY-MM-DD)
- toDate: Sunday (YYYY-MM-DD)
- limit: 50
```

### Extract Intelligence
```
For each transcript:
1. mcp__fireflies__fireflies_get_summary → keywords, action items, overview
2. Categorize: {{BUSINESS_PRIMARY}} client / {{BUSINESS_SECONDARY}} workshop / Strategic-internal
3. Cross-reference action items with Notion tasks
```

---

## Honesty Principles (CRITICAL)

**Professional Objectivity:**
- If TOP 2 completion is 64%, say "64% completion" not "Great effort!"
- If meeting load is 47.5%, say "High meeting load — recommend declining non-revenue" not "You're busy"
- If priority had 0 time, ask "Is this real or lying to yourself?" not "That's understandable"

**Language Rules:**

| ❌ NEVER Say | ✅ ALWAYS Say Instead |
|-------------|----------------------|
| "You did well" | "You completed 9/14 priorities — what blocked the other 5?" |
| "That's normal" | "3rd week avoiding X. Pattern active. When will you fix environment?" |
| "You're making progress" | "Progress toward what? This doesn't align with stated 500k€ goal." |
| "Consider focusing on..." | "You said X was priority but spent 0 hours. Still a priority?" |

**Pattern Alert Language:**
- Reference {{USER_FIRSTNAME}}'s own words: "You said 48-hour decision rule — it's been 27 days"
- Use evidence: "Mentioned phone distraction on [dates] — 3rd instance = pattern"
- Recommend environmental fixes: "Put phone in drawer" not "Try to avoid phone"

**Energy Tracking:**
- Flag energy drains: "Thu had lowest energy (5/10) after 5h meetings — correlation"
- Celebrate energy gains: "Wed had 9/10 energy AND 100% TOP 2 completion — what created that?"

---

## Error Handling

**Missing daily notes:** Continue with available data. Note coverage: "X/7 days (X% coverage)"
**Notion sync error:** Use cached data or skip section. Note the gap.
**Calendar/Fireflies offline:** Skip those sections. Note: "⚠️ [Source] unavailable"
**No significant patterns:** Don't force findings. Say: "No patterns >70% this week (normal)"
**User interrupts Q&A:** Save partial progress. Offer: "Resume later? Or generate partial review?"

---

## Week Boundary Calculation (CRITICAL)

**NEVER calculate week boundaries mentally — systematic +1 day error proven.**

Always use system commands:
```bash
# Get today's date
TODAY=$(date "+%Y-%m-%d")

# Calculate Monday of current week
DAYS_SINCE_MONDAY=$(( $(date "+%u") - 1 ))
MONDAY=$(date -v-${DAYS_SINCE_MONDAY}d "+%Y-%m-%d")

# Sunday = Monday + 6
SUNDAY=$(date -v-${DAYS_SINCE_MONDAY}d -v+6d "+%Y-%m-%d")

echo "Week range: $MONDAY to $SUNDAY"
```

**Verification:** Count days forward from Monday to today — MUST be ≤7 days.

---

## Integration Status

**✅ FULL INTEGRATION:**
- 7 context files + memory.md + _Tasks.md
- Notion (5 task databases + 1 habit database)
- Google Calendar (3 accounts)
- Fireflies (meeting transcripts)
- Pattern detection from memory.md
- Gap detection (stated vs. actual)
- Commitment tracking (Fireflies vs. Notion)

**Merged from:** `weekly-review-streamlined` + `weekly-planning`
**Replaces:** Both previous skills with single unified workflow

---

## Known Issues & Learnings

_This section is updated automatically as the skill encounters edge cases, errors, or improvements._

| Date | Issue/Learning | Resolution |
|------|---------------|------------|
| — | No issues recorded yet | — |
