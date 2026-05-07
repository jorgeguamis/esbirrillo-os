---
skill: tag-note
description: Help tag an Atomic Note with correct taxonomy based on content analysis
trigger: "/tag-note [note-name]"
---

# Tag Note Skill

Analyze an Atomic Note and suggest appropriate tags based on the Life OS tag taxonomy.

---

## When to Use

- Tagging a newly created Atomic Note
- Updating tags on existing note
- During bulk retagging process
- When unsure which tags to apply

**Trigger:** `/tag-note [note-name]` or `/tag-note` (will ask which note)

---

## Data Sources

### Required

**Tag Taxonomy:**
- `.claude/tag-system.md` - Complete tag taxonomy and rules

**Note to Tag:**
- Full path provided by {{USER_FIRSTNAME}}, or
- Search in `1. Atomic Notes/` folder

**Note Content:**
- Read full note to analyze content
- Review existing tags (if any)

---

## Process

### Step 1: Read Note Content

**If note name provided:**
```
Search for note in:
  1. 1. Atomic Notes/[note-name].md
  2. Full vault search if not in Atomic Notes
```

**If no note name:**
```
Ask {{USER_FIRSTNAME}}: "Which note should I tag?"
  - Accept file path
  - Accept note title
  - Accept wikilink [[Note Name]]
```

**Read note content:**
```
Extract:
  - Title
  - Main topic/subject
  - Business context ({{BUSINESS_PRIMARY}}, {{BUSINESS_SECONDARY}}, both, neither)
  - Frameworks mentioned
  - Current tags (if any)
  - Content maturity (how developed is the note)
```

---

### Step 2: Analyze Content

**Determine Type Tag:**
```
Is it:
  - Personal insight/concept? → type/zettel
  - Step-by-step process? → type/sop or type/how-to
  - Framework explanation? → type/framework
  - Goal document? → type/goal
  - Other? → ask {{USER_FIRSTNAME}}
```

**Determine Maturity Tag (if type/zettel):**
```
Content quality assessment:
  - Just captured, minimal structure → maturity/seedling
  - Has structure, needs examples → maturity/budding
  - Well-developed, clear examples → maturity/evergreen
```

**Determine Topic Tags (2-4 recommended):**
```
Analyze content for:
  - Primary subject (1 tag required)
  - Secondary subjects (1-3 tags recommended)

Match to taxonomy:
  - topic/ai, topic/prompting, topic/business, topic/marketing
  - topic/sales, topic/productivity, topic/mindset, topic/leadership
  - topic/finance, topic/health, topic/relationships, topic/learning
  - topic/copywriting, topic/offers, topic/content
```

**Determine Business Tag (if applicable):**
```
Content mentions:
  - {{BUSINESS_PRIMARY}} services/clients → business/primary
  - {{BUSINESS_SECONDARY}} content → business/secondary
  - Both businesses → business/both
  - Neither (general concept) → no business tag
```

**Determine Framework Tag (if applicable):**
```
Note explains/uses:
  - Value Equation → framework/value-equation
  - M.A.G.I.C Formula → framework/magic
  - Dream 100 → framework/dream-100
  - Vivid Vision → framework/vivid-vision
  - Life Map → framework/life-map
  - Other Hormozi framework → framework/hormozi

Only add if framework is CORE to the note.
```

**Determine Status Tag (if type/project or type/sop):**
```
Current state:
  - Working on it → status/active
  - On hold → status/paused
  - Done → status/completed
  - No longer relevant → status/archived
  - Future idea → status/backlog
```

---

### Step 3: Suggest Tags

**Present suggestions to {{USER_FIRSTNAME}}:**

```
Recommended tags for "[Note Title]":

REQUIRED:
  - type/[TYPE] - [Why this type]
  - maturity/[MATURITY] - [Why this maturity] (if type/zettel)

RECOMMENDED:
  - topic/[TOPIC1] - [Why relevant]
  - topic/[TOPIC2] - [Why relevant]
  - topic/[TOPIC3] - [Why relevant] (if applicable)

OPTIONAL:
  - business/[BUSINESS] - [Why applicable] (if business-specific)
  - framework/[FRAMEWORK] - [Why applicable] (if framework-centric)
  - status/[STATUS] - [Why this status] (if project/sop)

EXISTING TAGS (if any):
  - [List current tags]
  - [Mark which to keep, which to remove]
```

**Explain reasoning:**
```
For each suggested tag:
  - Why this tag applies
  - What content supports this tag
  - Alternative tags considered
```

---

### Step 4: Apply Tags

**Ask {{USER_FIRSTNAME}} for confirmation:**
```
"These are my suggestions. Would you like me to:
  [1] Apply all suggested tags
  [2] Apply with modifications (you specify)
  [3] Cancel (you'll tag manually)"
```

**If [1] - Apply all:**
```
Update note frontmatter:
  - Add/update tags section
  - Preserve other frontmatter fields (created, updated, etc.)
  - Add updated: [today's date]
```

**If [2] - Apply with modifications:**
```
Ask: "Which tags should I modify?"
Apply {{USER_FIRSTNAME}}'s adjustments
Update note frontmatter
```

**If [3] - Cancel:**
```
Confirm: "No tags applied. You can manually add them."
```

---

### Step 5: Verify Migration (if applicable)

**If note had old-format tags:**
```
Check for:
  - [[_Marketing]] → Convert to topic/marketing
  - [[_Business]] → Convert to topic/business
  - [[_Sales]] → Convert to topic/sales
  - [[_AI]] → Convert to topic/ai
  - 360_Degrees → Convert to business/primary
  - framework/🌱 → Convert to maturity/seedling
  - framework/🍎 → Convert to maturity/evergreen

Confirm migration:
  "Migrated old tags:
   - [[_Marketing]] → topic/marketing
   - 360_Degrees → business/primary"
```

---

## Output

**Updated note with:**

✅ Correct `type/*` tag
✅ `maturity/*` tag (if type/zettel)
✅ 2-4 relevant `topic/*` tags
✅ `business/*` tag (if applicable)
✅ `framework/*` tag (if applicable)
✅ `status/*` tag (if project/sop)
✅ Updated `updated` date in frontmatter

**Old-format tags removed/migrated**

---

## Confirmation

Show {{USER_FIRSTNAME}}:
1. **Tags applied:**
   ```yaml
   tags:
     - type/zettel
     - maturity/budding
     - topic/marketing
     - topic/offers
     - business/primary
     - framework/value-equation
   ```
2. **Reasoning:** [Brief explanation of each tag]
3. **Migrations:** [List of old tags converted]

**Ask:** "Tags applied. Does this look correct?"

---

## Notes

- **Be specific:** Choose the most relevant topics, don't over-tag
- **Be consistent:** Use existing tags from taxonomy, don't invent new ones
- **Context matters:** Business tag should only apply if truly business-specific
- **Frameworks:** Only add framework tag if note is ABOUT the framework
- **Ask when unsure:** If content could fit multiple tags, ask {{USER_FIRSTNAME}} to decide

---

## Reference

See `.claude/tag-system.md` for:
- Complete tag taxonomy
- Tag application rules
- Frontmatter templates
- Migration guide

---

**Created:** 2026-01-01

---

## Known Issues & Learnings

_This section is updated automatically as the skill encounters edge cases, errors, or improvements._

| Date | Issue/Learning | Resolution |
|------|---------------|------------|
| — | No issues recorded yet | — |
