---
description: Update a context file based on patterns detected in recent daily notes
---

# Update Context

Analyze recent daily notes to extract emerging patterns, priorities, and changes, then suggest updates to the corresponding context file.

**Usage:** `/update-context [area-name]`

**Examples:**
- `/update-context Personal`
- `/update-context Business-360`
- `/update-context Business-{{BUSINESS_SECONDARY}}`
- `/update-context Health`
- `/update-context Learning`

## Process

### 1. Validate Area

**Check if area is provided:**
- If `$arguments` is empty, show available areas and ask user to choose
- Available areas: Personal, Business-360, Business-{{BUSINESS_SECONDARY}}, Health, Learning, Finances, Research

**Determine context file path:**
```
Personal → 02. Areas/personal/Personal.md
Business-360 → 02. Areas/business_primary/{{BUSINESS_PRIMARY}}.md
Business-{{BUSINESS_SECONDARY}} → 02. Areas/business_secondary/{{BUSINESS_SECONDARY}}.md
Health → 02. Areas/salud/Health.md
Learning → 02. Areas/aprendizaje/Learning.md
Finances → 02. Areas/finanzas/Finances.md
Research → 02. Areas/investigacion/Research.md
```

**Check if context file exists:**
- If not found, ask: "Context file doesn't exist. Create it? (yes/no)"
- If yes, create basic template
- If no, stop command

### 2. Read Recent Daily Notes

**Determine date range:**
- Default: Last 7 daily notes
- Ask user: "Analyze last 7 days of notes? (yes/change)"
- If change: "How many days? (3/7/14/30)"

**Read daily notes:**
- Path: `0. Journal/01. Daily/DD-MM-YYYY.md`
- Read from most recent backwards
- Skip weekends if no notes exist
- If note doesn't exist for a day, skip it

**Extract relevant sections per area:**
- Personal: `## 💪 Personal` section + Energy levels + Evening reflections
- Business-360: `## 📊 {{BUSINESS_PRIMARY}}` section
- Business-{{BUSINESS_SECONDARY}}: `## 🎓 {{BUSINESS_SECONDARY}}` section
- Health: Health-related entries from Personal section
- Learning: Learning-related entries from Personal section
- All: Morning TOP 2 priorities (to see what's actually being prioritized)

### 3. Analyze Patterns

**Pattern detection (CRITICAL - This is the value add):**

**A. Recurring themes (3+ mentions = pattern):**
- What topics/projects appear repeatedly?
- What challenges come up multiple times?
- What wins are repeated?

**B. Priority shifts:**
- Compare stated priorities in context vs. actual work in daily notes
- Identify drift: "Context says X is priority, but daily notes show Y getting time"
- Flag misalignment for user awareness

**C. Energy patterns:**
- Average energy levels over period
- Days with low energy - what was happening?
- Days with high energy - what was different?

**D. Friction points:**
- What blockers appear repeatedly in evening reflections?
- What causes consistent friction?
- Patterns in "things to let go"

**E. Progress indicators:**
- Completed tasks related to stated goals
- Movement on projects
- New initiatives started

**F. New opportunities/threats:**
- Mentions of new potential projects
- Emerging challenges not in current context
- People/resources mentioned repeatedly

### 4. Read Current Context File

**Parse existing context:**
- Current TOP 3 priorities
- Active projects list
- Recent wins and blockers
- Goals (if present)
- Any other structured sections

**Identify what needs updating:**
- Stale priorities (not worked on in daily notes)
- Missing new priorities (worked on but not listed)
- Completed projects still marked active
- New blockers not documented
- Energy/state not reflecting reality

### 5. Generate Update Suggestions

**Create structured diff showing:**

**Section: Current Priorities**
```diff
- OLD PRIORITY 1 (not worked on in 7 days)
+ NEW PRIORITY 1 (worked on 5/7 days)
  PRIORITY 2 (still active, worked on 3/7 days)
+ EMERGING: New thing mentioned 4 times
```

**Section: Active Projects**
```diff
  Project A (progressing - mentioned 3 times)
- Project B (no activity in 7 days - archive?)
+ Project C (new - started DD-MM-YYYY)
```

**Section: Recent Wins & Blockers**
```diff
Wins:
+ [New win from this week]
+ [Another win]

Blockers:
- [Old blocker - resolved]
+ [New recurring blocker - mentioned 3x]
  [Existing blocker - still present]
```

**Section: Energy & Patterns**
```diff
+ Average energy: X/10 (down from Y/10 last period)
+ Pattern: Low energy on days with back-to-back meetings
+ Pattern: High productivity when starting with quick wins
```

**Section: Next Actions**
```diff
- [Old action - completed or stale]
+ [New action based on patterns observed]
+ [Another new action]
```

### 6. Show Diff and Confirm

**Present update preview:**
```
📊 Context Update Analysis for [Area]
Period analyzed: [Start Date] - [End Date] (7 days)

PRIORITIES DRIFT DETECTED:
⚠️ Context says "Client outreach" is priority, but 0 mentions in daily notes
✓ "Workshop prep" not in context, but worked on 5/7 days → Should be priority

SUGGESTED UPDATES:
[Show full diff as above]

PATTERNS DETECTED:
1. Recurring theme: [Theme] (mentioned 4 times)
2. Energy pattern: Low energy on [pattern]
3. Blocker pattern: [Blocker] appeared 3 times

Apply these updates? (yes/edit/cancel)
```

**Handle user response:**
- `yes` → Apply all changes
- `edit` → Ask what to change, then show updated diff
- `cancel` → Don't update, but save analysis as note in area folder

### 7. Update Context File

**If user approves:**
- Read current context file
- Apply suggested changes
- Update `updated: DD-MM-YYYY` in frontmatter
- Preserve any sections not analyzed (don't delete user's custom sections)

**Backup before update:**
- Copy current context to `.claude/logs/context-backups/[area]-[timestamp].md`
- Allows rollback if needed

### 8. Confirm and Next Steps

**Show success message:**
```
✓ Updated: [context file path]
✓ Backup saved: .claude/logs/context-backups/[area]-[timestamp].md
✓ Changes applied: X sections updated

Key changes:
- Priorities realigned with actual work
- New blocker documented: [blocker]
- Energy pattern noted: [pattern]

Next steps:
1. Review updated context file
2. Adjust your work to match priorities (or update priorities again)
3. Run `/morning` tomorrow - it will use updated context
4. Run `/update-context [area]` weekly to stay aligned

Tip: Drift between context and daily notes is normal. This command helps you notice and correct it!
```

## Examples

**Example 1: Personal context drift**
```
/update-context Personal

Analysis shows:
- Context priority "Exercise 4x/week" → Only 1 mention in 7 days
- Actual work: "Course creation" mentioned 5 times but not in priorities
- Energy pattern: Average 6/10 (down from 8/10)
- Blocker: "Too many meetings" mentioned 3x

Suggestion: Reprioritize course creation, address meeting overload
```

**Example 2: Business-360 new project**
```
/update-context Business-360

Analysis shows:
- New client "Acme Corp" mentioned 4 times
- Old project "Client X" no activity in 7 days
- Win: Closed 2 new deals
- Pattern: Sales calls most productive in morning

Suggestion: Add Acme Corp to active projects, archive Client X, note morning sales pattern
```

**Example 3: Health area progress**
```
/update-context Health

Analysis shows:
- Goal "Run 3x/week" → Actual: 4/7 days (exceeding!)
- New habit: Morning stretching mentioned 5x
- Blocker resolved: Knee pain not mentioned
- Energy correlation: Exercise days have +2 energy vs non-exercise days

Suggestion: Celebrate progress, add stretching to habits, note energy correlation
```

## Edge Cases

**No daily notes in period:**
```
⚠️ Found only 2 daily notes in last 7 days.

Not enough data for meaningful pattern detection.

Options:
1. Extend analysis period (try 14 or 30 days)
2. Create more daily notes first
3. Cancel and try again later
```

**Context file is empty/template:**
```
Context file exists but is mostly empty.

Cannot do diff comparison without baseline.

Suggestion:
1. Run analysis anyway to generate initial context
2. Or manually fill context file first, then run update
```

**No mentions of area in daily notes:**
```
⚠️ [Area] not mentioned in any of the 7 daily notes analyzed.

This could mean:
1. This area hasn't been a focus lately (intentional?)
2. You're working on it but not documenting it
3. This area might not be relevant right now

Keep context as-is, or mark this area as inactive?
```

## Integration with Other Commands

**Workflow:**
1. Week starts: `/morning` reads context
2. Daily work: Document in daily notes
3. Week ends: `/update-context [area]` analyzes patterns
4. Review: Weekly review incorporates context insights
5. Repeat

**Synergy with:**
- `/morning` - Uses updated context for better daily briefs
- `/weekly-plan` - Can reference recent context changes
- Evening reflections - Provide data for pattern detection

## Notes

- This command is about **detecting drift** and **pattern recognition**
- It's a mirror: Shows what you're ACTUALLY prioritizing vs. what you SAY you're prioritizing
- Honest over validation: Will call out misalignment
- Run weekly for best results (too frequent = noise, too infrequent = stale context)
- Energy tracking is crucial - this command makes it actionable
- Patterns emerge at 3+ occurrences (one instance = event, three = pattern)
