---
description: Generate daily brief with TOP 2 priorities and quick win. Start each day with clarity.
---

Start the day by generating a focused daily brief.

## Data Sources

Read these files (paths configured per user during `/setup-wizard`):

**Required — Context Files:**
- `02. Areas/personal/Personal.md` — Personal priorities and state
- `02. Areas/personal/North Star.md` — strategic orientation
- For each of the user's businesses: `02. Areas/{business_slug}/Context.md`
- `02. Areas/health/Health.md` — health goals and routines (if exists)
- `02. Areas/learning/Learning.md` — learning focus (if exists)
- `02. Areas/finances/Finances.md` — financial context (if exists)

**Required — Journal Files:**
- Yesterday's daily note: `02. Areas/personal/diario/01. Daily/{{date-1d:DD-MM-YYYY}}.md` (must exist and be complete)
- Today's daily note: `02. Areas/personal/diario/01. Daily/{{date:DD-MM-YYYY}}.md` (check if already exists)
- Last week's review: `02. Areas/personal/diario/02. Weekly/{{date-7d:YYYY-[W]ww}}.md`

**Required — Working Memory:**
- `${USER_CLAUDE_DIR}/memory/working-memory.md`

**Required — Google Calendar (via MCP):**
- Today's schedule from each of the user's configured Google accounts.
- Meeting load and available blocks.
- First-meeting prep needs.

**Required — Notion Tasks (via Notion MCP):**
- Query DBs registered in `.claude/context/notion-registry.md` for: overdue tasks, tasks due today, high-priority incomplete.
- The exact set of DBs is per-user.

**Required — Task Brainstorm:**
- `_Tasks.md` if the user maintains one.
- Surface 🔴 Urgente / 🟡 Importante items the user may have forgotten.

**Required — Fireflies (Yesterday's Meetings via MCP):**
- Query recent meetings from yesterday using `fireflies_search` or `fireflies_get_transcripts`.
- Extract: Action items, decisions made, follow-ups committed.
- If no meetings yesterday, skip silently.

## Validation Steps (MUST RUN FIRST)

### STEP 0 — Calculate and Verify Today's Date Context
**CRITICAL — Do this BEFORE reading any files:**
1. Get day of week from system: `date "+%A, %B %d, %Y"` — never calculate mentally.
2. Calculate week boundaries (Mon-Sun):
   ```bash
   DAYS_SINCE_MONDAY=$(( $(date "+%u") - 1 ))
   MONDAY=$(date -v-${DAYS_SINCE_MONDAY}d "+%Y-%m-%d")
   ```
3. Verify against yesterday's daily note (if yesterday was "Tuesday Jan 13", today is "Wednesday Jan 14").

### STEP 1 — Read This Week's Daily Notes (Monday through Yesterday)
Read all daily notes from current week's Monday through yesterday.

**Extract and document:**
1. Yesterday's stated "Tomorrow's TOP Priority" — strongest signal for today.
2. Active items from each business area mentioned across the week.
3. Health/exercise sessions completed (if user tracks).
4. Energy patterns (averages, dips below 6/10).
5. Uncompleted high-priority tasks carried forward.
6. Friction points repeated 2+ times this week.
7. Pending commitments (promises made, follow-ups owed).

### STEP 2 — Check Yesterday's Note Completion
Verify yesterday's note has Morning + Evening Reflection sections filled.
- If incomplete: tell the user what's missing and stop.
- If complete: proceed.

### STEP 3 — Check if Today's Note Already Exists
- If exists with Morning section filled: show it, ask before overwriting.
- If "no": stop.
- If "yes": overwrite Morning section only.

### STEP 4 — Read Context Files
Read all files in Data Sources. Empty contexts: note + continue.

### STEP 5 — Get Today's Calendar Schedule
For each Google Calendar configured by the user, query today's events:
```
mcp__google-workspace__list_events({
  calendarId: "{{calendar_id}}",
  timeMin: "{{date:YYYY-MM-DD}}T00:00:00Z",
  timeMax: "{{date:YYYY-MM-DD}}T23:59:59Z"
})
```

**Calculate:**
- Total meeting hours today.
- First meeting time (prep alert).
- Back-to-back meetings (energy drain flag).
- Largest uninterrupted deep-work block.
- Meeting load % of work day (8h reference).
- Energy risk flags (>4h meetings = high drain).

### STEP 6 — Get Notion Tasks Status
Query the DBs in `notion-registry.md`. Extract:
- Overdue tasks (Due Date < Today AND Status != Completed).
- Due today (Due Date = Today).
- High-priority incomplete (Priority = High/Urgent AND Status != Completed).
- Delayed projects (no activity >7 days).

Flag for attention:
- Client/committed deliverables overdue (revenue/relationship risk).
- High-priority personal items ignored >3 days.
- Projects with no progress this week.

### STEP 7 — Check Yesterday's Meetings (Fireflies)
Query Fireflies for yesterday's meetings. For each:
1. Get summary via `fireflies_get_summary`.
2. Extract action items, decisions, follow-ups.
3. Note participants + business area.

If meetings found → include "Meeting Recap" section. If none → skip silently.

### STEP 8 — Read Task Brainstorm
If `_Tasks.md` exists:
- 🔴 Urgente — should inform TOP 2.
- 🟡 Importante — mention if relevant.
- 🔄 Recurrentes — flag if due.

## Process

1. **Complete validation steps 0-8.** Don't skip — they prevent stale-context errors.
2. **Analyze constraints:** calendar (deep work blocks, prep needs), task urgency, energy budget.
3. **Analyze weekly data:** which areas need attention based on activity pattern, energy trend, repeated friction.
4. **Select TOP 2:**
   - Yesterday's stated "Tomorrow's TOP Priority" = strongest signal (usually TOP 2 #1).
   - What moves the needle toward annual goals.
   - Active deliverables that need completion.
   - Cross-area priorities if urgent.
   - **NOT what's urgent, but what matters.**
5. **Break down each TOP 2:** 2-4 concrete subtasks, "done when" outcome, "schedule in" block.
6. **Choose Quick Win:** one 10-15 minute task for momentum, from any area.

## Output

Create or update today's daily note: `02. Areas/personal/diario/01. Daily/{{date:DD-MM-YYYY}}.md`

If note doesn't exist: use full template from `03. Sistema/templates/Daily Note.md`.
If note exists and overwrite approved: only update Morning section.

```markdown
## 🌅 Morning

**Time:** [Current time]
**Energy Level (1-10):** [Ask user or estimate from context]
**Current state:** [Brief state based on recent notes or ask]

### Quick Win (10-15 min)
- [ ] [Specific 10-15 min task]

### TOP 2 Priorities
1. **[Primary task — aligned with #1 priority]**
   - [ ] [Concrete subtask]
   - [ ] [Concrete subtask]
   - **Done when:** [Specific outcome]
   - **Time needed:** [Hours] — **Schedule in:** [Specific block from calendar gaps]

2. **[Secondary task]**
   - [ ] [Concrete subtask]
   - [ ] [Concrete subtask]
   - **Done when:** [Specific outcome]
   - **Time needed:** [Hours] — **Schedule in:** [Specific block from calendar gaps]

### If Time Permits
- [ ] [Task from backlog or nice-to-have]

---

## 📅 Today's Schedule

**Meeting Load:** [X hours] ([Y%] of work day)
**Available Deep Work:** [Largest block] ([time range])

### Morning (before 12:00)
- [Time] - [Event] ([Calendar source])

### Afternoon (12:00-18:00)
- [Time] - [Event]

### Evening (18:00+)
- [Time] - [Event]

[If first meeting needs prep:]
**Prep Needed:** [First meeting] at [time] — Review [context/materials] beforehand

[If back-to-back present:]
**Back-to-Back Alert:** [Time range] — Schedule buffer or combine prep

---

[If yesterday meetings present:]
## 📞 Yesterday's Meeting Recap

### [Meeting Title] ([Business area])
- **With:** [Participants]
- **Key decisions:** [Decisions]
- **Action items:**
  - [ ] [Action item]
- **Follow-ups:** [Committed follow-ups with deadlines]

---

## 🚨 Urgent Tasks (from Notion)

[Overdue, Due Today, High Priority Incomplete sections — only show if non-empty]

✅ **All clear** — No urgent tasks flagged
```

## Criteria for Good TOP 2

**Good:** specific, outcome-driven, has a "done when" condition. Examples vary per user role.

**Bad:** "Work on business" (vague), "Answer emails" (noise), "Think about strategy" (not actionable).

## Context File Handling

- Empty/template context: note it + continue. Don't fail.
- Useful context: pull priorities, goals, current state. Reference specific items in TOP 2 explanations.
- Always connect daily work to stated goals: "This supports your goal of [X]."

## Confirm

Show the brief and ask:
> "Here's your focus for today. Does this feel right? Any adjustments?"

## Data Priority Hierarchy

When selecting TOP 2, prioritize sources in this order:
1. Yesterday's "Tomorrow's TOP Priority" (strongest signal — user already decided).
2. Overdue committed deliverables from Notion (relationship/revenue risk).
3. Meeting action items from Fireflies (commitments made to others).
4. 🔴 Urgente items from Task Brainstorm (user flagged these).
5. Context file priorities (stated annual/quarterly goals).
6. Calendar constraints (if 2h available, scale ambition accordingly).
7. Weekly patterns from daily notes (what's getting momentum).

## Energy-Aware Scheduling

- High meeting load (>4h): scale down TOP 2 complexity, focus on completion over ambition.
- Back-to-back meetings: add prep/buffer time to TOP 2 subtasks.
- Morning deep-work block: always try to protect 8-11am if available.
- Post-lunch dip: don't schedule hardest work in 2-3pm range.

## Integration Notes

- **Calendar accounts:** read from user's `.env` or `notion-registry.md` (per-user setup).
- **Notion DBs:** all DB IDs in `notion-registry.md` (per-user).
- **Fireflies:** uses `fireflies_*` MCP tools.
- **Fallback:** if any integration fails, mark `[SKIP: <reason>]` and continue with remaining sources.
