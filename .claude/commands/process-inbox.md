---
description: Process items from 00. Inbox/ by classifying them and moving to appropriate locations
---

# Process Inbox

Systematically process all items in the `00. Inbox/` folder, classify them, suggest destinations, and move them with proper frontmatter.

## Process

### 1. List All Inbox Items
- Read all files in `00. Inbox/` directory
- Show count to user
- If empty, say "Inbox is clean! ✨" and stop

### 2. For Each Item (One at a Time)

**Read the file content:**
- Analyze content to determine type
- Check if it already has frontmatter

**Classify the item:**
- **Atomic Note** → Content is evergreen knowledge, concept, or insight
  - Destination: `1. Atomic Notes/`
  - Required tags: `type/zettel`, `maturity/seedling`, 2-4 `topic/*` tags

- **Reference Note** → Content from external source (book, video, article, person)
  - Destination: `3. Reference/[Books|Youtube|People|Courses]/`
  - Required tags: `type/source`, relevant `topic/*` tags

- **Project** → Actionable multi-step initiative
  - Destination: `2. Areas/[area-name]/proyectos/`
  - Required tags: `type/project`, `status/active`, `area/*`, relevant `topic/*`

- **SOP** → Standard operating procedure or process documentation
  - Destination: `2. Areas/[area-name]/sops/`
  - Required tags: `type/sop`, `status/active`, `business/*` if applicable

- **Daily Note Fragment** → Content that belongs in a daily note
  - Destination: Append to relevant daily note in `0. Journal/01. Daily/`
  - Action: Merge, don't create separate file

- **Temporary/Trash** → Low-value capture or no longer relevant
  - Destination: `.trash/`
  - Action: Ask before deleting

**Suggest destination and tags:**
- Show filename, type detected, proposed destination
- Show proposed frontmatter with tags
- Ask: "Move this item? (yes/edit/skip/delete)"

**Handle user response:**
- `yes` → Move file and update/add frontmatter
- `edit` → Ask what to change (destination, tags, filename)
- `skip` → Leave in inbox, process next
- `delete` → Move to `.trash/`

### 3. After Processing All Items

Show summary:
```
Inbox Processing Complete!
- Processed: X items
- Moved: Y items
- Skipped: Z items
- Deleted: W items

Inbox status: [Clean/X items remaining]
```

## Frontmatter Creation Rules

**If file has NO frontmatter:**
```yaml
---
tags:
  - [suggested tags based on classification]
created: DD-MM-YYYY
---
```

**If file has PARTIAL frontmatter:**
- Keep existing tags
- Add missing required tags
- Add `created` date if missing
- Add `updated: DD-MM-YYYY`

## Smart Suggestions

**Area detection:**
- Look for keywords: "360", "client", "consulting" → `area/business-360`
- Look for: "revolutia", "academy", "student", "workshop" → `area/business-revolutia`
- Look for: "health", "workout", "nutrition" → `area/health`
- Look for: "learning", "course", "study" → `area/learning`
- Default to: `area/personal` if unclear

**Topic detection:**
- Analyze content keywords
- Use common topics from `.claude/tag-system.md`
- Suggest 2-4 most relevant topics

**Maturity for Atomic Notes:**
- Default to `maturity/seedling` for new captures
- User can change during "edit" if it's more developed

## Examples

**Example 1: Captured thought about AI**
```
File: "thoughts on prompt engineering.md"
Content: "Prompts should be clear and specific..."

Classification: Atomic Note
Destination: 1. Atomic Notes/Prompt Engineering Clarity.md
Tags: type/zettel, maturity/seedling, topic/ai, topic/prompting
```

**Example 2: Meeting notes**
```
File: "meeting with client X.md"
Content: "Discussed project scope..."

Classification: Project
Destination: 2. Areas/Business-360/proyectos/Client X Project.md
Tags: type/project, status/active, area/business-360, business/primary
```

**Example 3: YouTube video notes**
```
File: "video notes - productivity.md"
Content: "Tips from Ali Abdaal video..."

Classification: Reference Note
Destination: 3. Reference/Youtube/Ali Abdaal Productivity Tips.md
Tags: type/source, topic/productivity, area/learning
```

## Edge Cases

**Duplicate filenames:**
- If destination file exists, ask: "File exists. (merge/rename/skip)"
- `merge` → Append content to existing file with separator
- `rename` → Suggest filename with number suffix
- `skip` → Leave in inbox

**Unclear classification:**
- If unsure, default to Atomic Note in inbox
- Explicitly ask user: "Not sure about this one. What type is it?"
- Show options: zettel/source/project/sop/daily-fragment/trash

**Empty files:**
- Automatically delete without asking
- Mention in summary: "Deleted X empty files"

## Notes

- Process items one at a time to avoid overwhelming user with decisions
- Always show preview of what will happen before executing
- Use wikilink format `[[Note Title]]` when suggesting connections
- After moving, verify file exists at new location
- Keep inbox as clean as possible - encourage processing regularly
- If user skips many items, ask if they want to stop and resume later

## Confirmation

After each successful move:
```
✓ Moved to: [destination]
✓ Tags added: [tags list]
```

After completion:
```
Next steps:
- Review new Atomic Notes and add connections
- Update maturity tags as notes develop
- Process inbox again tomorrow if needed

Tip: Run `/process-inbox` daily to keep inbox at zero!
```
