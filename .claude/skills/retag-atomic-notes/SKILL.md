---
skill: retag-atomic-notes
description: Bulk retagging assistant for migrating Atomic Notes to new tag taxonomy
trigger: "/retag-atomic-notes"
---

# Retag Atomic Notes Skill

Batch process for retagging Atomic Notes with the new tag taxonomy system.

---

## When to Use

- During initial migration to new tag system
- After adding new tag categories
- When cleaning up inconsistent tags
- Periodic tag audits

**Trigger:** `/retag-atomic-notes`

---

## Data Sources

### Required

**Tag Taxonomy:**
- `.claude/tag-system.md` - Complete tag taxonomy and rules

**Atomic Notes to Process:**
- All notes in `1. Atomic Notes/` folder
- Filter: Untagged OR old-format tags OR incomplete tags

**Processing Strategy:**
- Batch size: 5 notes at a time
- Show progress after each batch
- Allow skip/defer for unclear notes

---

## Process

### Step 1: Scan Atomic Notes

**Identify notes needing retagging:**
```
Scan 1. Atomic Notes/ for:
  - Untagged notes (no tags in frontmatter)
  - Old format tags: [[_Marketing]], 360_Degrees, framework/🌱, framework/🍎
  - Incomplete tags: Missing type/* or maturity/*
  - Inconsistent format: Mixed taxonomy formats
```

**Generate retagging queue:**
```
Create list of notes ordered by priority:
  1. Untagged notes (highest priority)
  2. Old-format tags needing migration
  3. Incomplete tags (missing required fields)
  4. Low priority: Already tagged but could be improved
```

**Show {{USER_FIRSTNAME}} the queue:**
```
Found [N] notes needing retagging:
  - [N] untagged
  - [N] with old-format tags
  - [N] with incomplete tags

Start retagging in batches of 5?
  [1] Yes, start with untagged
  [2] Yes, start with old-format
  [3] Let me review the list first
  [4] Cancel
```

---

### Step 2: Process in Batches

**For each batch of 5 notes:**

1. **Read note content:**
   ```
   For each note:
     - Read full content
     - Extract existing tags
     - Analyze main topic/subject
     - Identify business context
     - Detect frameworks mentioned
     - Assess content maturity
   ```

2. **Suggest tags using `/tag-note` logic:**
   ```
   For each note, determine:
     - type/* (required)
     - maturity/* (required if type/zettel)
     - topic/* (2-4 recommended)
     - business/* (if applicable)
     - framework/* (if applicable)
   ```

3. **Present batch suggestions:**
   ```
   Batch [X] of [Y] - Suggested tags:

   📄 [Note 1 Title]
   Current: [existing tags]
   Suggested:
     - type/zettel
     - maturity/budding
     - topic/marketing
     - topic/offers
     - business/primary
   Reason: [Brief explanation]

   📄 [Note 2 Title]
   Current: [existing tags]
   Suggested:
     - type/framework
     - topic/sales
     - framework/value-equation
   Reason: [Brief explanation]

   [Continue for all 5 notes...]
   ```

---

### Step 3: Batch Confirmation

**Ask {{USER_FIRSTNAME}} for approval:**
```
Batch [X] suggestions ready. What would you like to do?
  [1] Apply all suggestions in this batch
  [2] Review note-by-note (I'll ask about each)
  [3] Skip this batch (defer for manual tagging)
  [4] Modify suggestions (you specify changes)
  [5] Stop retagging process
```

**If [1] - Apply all:**
```
For each note in batch:
  - Update frontmatter tags
  - Remove old-format tags
  - Add updated: [today's date]
  - Preserve other frontmatter fields
```

**If [2] - Review note-by-note:**
```
For each note:
  Show: Title, current tags, suggested tags, reasoning
  Ask: "Apply these tags? [Y/n/modify]"
  If modify: "Which tags should I change?"
  Apply based on response
```

**If [3] - Skip batch:**
```
Add batch notes to "deferred" list
Continue to next batch
```

**If [4] - Modify suggestions:**
```
Ask: "Which notes need different tags?"
Ask: "What tags should [Note X] have instead?"
Apply modified tags
```

**If [5] - Stop:**
```
Show progress: "[N] notes retagged, [M] remaining"
Ask: "Resume later with /retag-atomic-notes?"
```

---

### Step 4: Migration Tracking

**Track old → new conversions:**
```
Log all tag migrations:
  [[_Marketing]] → topic/marketing (N notes)
  [[_Business]] → topic/business (N notes)
  [[_Sales]] → topic/sales (N notes)
  [[_AI]] → topic/ai (N notes)
  360_Degrees → business/primary (N notes)
  framework/🌱 → maturity/seedling (N notes)
  framework/🍎 → maturity/evergreen (N notes)
```

**Verify consistency:**
```
After each batch:
  - Check for tag spelling consistency
  - Verify no old-format tags remain
  - Ensure required tags present (type/*, maturity/* for zettel)
```

---

### Step 5: Progress Updates

**After each batch:**
```
✅ Batch [X] complete!

Progress:
  - [N] notes retagged
  - [M] notes remaining
  - [P] notes deferred

Common tags applied this batch:
  - topic/marketing (3 notes)
  - business/primary (2 notes)
  - maturity/budding (4 notes)

Continue with next batch? [Y/n]
```

---

## Output

**After full retagging process:**

✅ **Notes retagged:** [N] notes
✅ **Tags migrated:**
   - Old format removed: [list of old tags]
   - New format applied: [list of new tags]
✅ **Deferred for manual review:** [M] notes
✅ **Tag distribution:**
   - type/zettel: [N] notes
   - maturity/seedling: [N] notes
   - maturity/budding: [N] notes
   - maturity/evergreen: [N] notes
   - topic/marketing: [N] notes
   - topic/sales: [N] notes
   - [etc.]

**Deferred notes list:**
- [Note 1] - Reason: Unclear topic
- [Note 2] - Reason: Needs content development first
- [Note 3] - Reason: Complex multi-topic note

---

## Confirmation

Show {{USER_FIRSTNAME}}:
1. **Retagging summary:**
   - Total notes processed
   - Tag migrations performed
   - Notes deferred
2. **Tag consistency check:** All notes follow new taxonomy
3. **Recommendations:**
   - Notes that need content development
   - Potential new topic tags to consider
   - Notes that might need splitting

**Ask:** "Retagging complete! Review deferred notes list?"

---

## Notes

- **Batch size:** 5 notes optimal - enough for efficiency, small enough to review
- **Defer when unsure:** Better to ask {{USER_FIRSTNAME}} than guess wrong tags
- **Consistency:** Use exact tag names from taxonomy, don't create new tags
- **Context matters:** Read full note content, don't just guess from title
- **Migration tracking:** Document all old → new tag conversions for reference

---

## Common Old Format Migrations

| Old Format | New Format |
|-----------|-----------|
| `[[_Marketing]]` | `topic/marketing` |
| `[[_Business]]` | `topic/business` |
| `[[_Sales]]` | `topic/sales` |
| `[[_AI]]` | `topic/ai` |
| `360_Degrees` | `business/primary` |
| `{{BUSINESS_SECONDARY}}` | `business/secondary` |
| `framework/🌱` | `maturity/seedling` |
| `framework/🍎` | `maturity/evergreen` |
| `SOPs` | `type/sop` |

---

## Reference

See `.claude/tag-system.md` for:
- Complete tag taxonomy
- Tag application rules
- Frontmatter templates
- Individual note tagging: Use `/tag-note` skill

---

**Created:** 2026-01-01

---

## Known Issues & Learnings

_This section is updated automatically as the skill encounters edge cases, errors, or improvements._

| Date | Issue/Learning | Resolution |
|------|---------------|------------|
| — | No issues recorded yet | — |
