# Life OS - Tag System Documentation

This document defines the complete tag taxonomy for organizing content in the Life OS vault.

---

## Tag Taxonomy Structure

All tags use the format: `category/value`

---

## Core Tag Categories

### A. Type Tags (Required for all notes)

Defines the content type of the note.

```yaml
type/zettel          # Atomic note (evergreen knowledge, personal insight)
type/hub             # Hub index file with Dataview queries
type/context         # Context file (AI memory for an area)
type/project         # Project documentation
type/sop             # Standard operating procedure
type/framework       # Personal framework or methodology
type/goal            # Goal document
type/how-to          # How-to guide or tutorial
type/template        # Template file
type/daily           # Daily journal entry
type/weekly          # Weekly review
type/monthly         # Monthly review
type/quarterly       # Quarterly review
type/annual          # Annual review
type/source          # Source note (book, course, video reference)
type/person          # Person note (individual referenced)
```

**Rule:** Every note MUST have exactly one `type/*` tag.

---

### B. Topic Tags (Multiple allowed)

Defines the subject matter of the note.

```yaml
topic/ai             # Artificial Intelligence
topic/prompting      # AI prompting techniques
topic/business       # General business concepts
topic/marketing      # Marketing strategies and concepts
topic/sales          # Sales processes and techniques
topic/productivity   # Productivity systems and methods
topic/mindset        # Mindset & psychology
topic/leadership     # Leadership principles
topic/finance        # Financial concepts
topic/health         # Health & wellness
topic/relationships  # Relationships and communication
topic/learning       # Learning methodologies
topic/copywriting    # Copywriting and content creation
topic/offers         # Offer creation and design
topic/content        # Content strategy and creation
```

**Rule:** Add 2-4 topic tags per note for optimal discoverability.

---

### C. Area Tags (Optional - Links to Life OS Areas)

Links the note to a specific Life OS area hub.

```yaml
area/business-360      # Related to {{BUSINESS_PRIMARY}} area
area/business-revolutia # Related to {{BUSINESS_SECONDARY}} area
area/personal          # Related to Personal area
area/health            # Related to Health area
area/finances          # Related to Finances area
area/learning          # Related to Learning area
area/research          # Related to Research area
```

**Rule:** Use area tag when note is specifically relevant to one area.
**Purpose:** Allows hub Dataview queries to aggregate notes by area.

---

### D. Business Tags (Indicates which business applies)

For content specific to one of the two businesses.

```yaml
business/primary         # {{BUSINESS_PRIMARY}} specific
business/secondary   # {{BUSINESS_SECONDARY}} specific
business/both        # Applies to both businesses
```

**Rule:** Business-related notes SHOULD have one business tag.

---

### E. Framework Tags (For structured methodologies)

When a note explains or uses a specific framework.

```yaml
framework/value-equation    # The Value Equation (Hormozi)
framework/magic            # M.A.G.I.C Formula
framework/dream-100        # Dream 100
framework/vivid-vision     # Vivid Vision
framework/life-map         # Life Map (6 pillars)
framework/hormozi          # Alex Hormozi frameworks (general)
```

**Rule:** Only apply when the note directly explains or implements the framework.

---

### F. Status Tags (For projects and goals)

Tracks the current state of actionable items.

```yaml
status/active        # Currently working on
status/paused        # Temporarily on hold
status/completed     # Finished
status/archived      # No longer relevant (moved to 5. Archive/)
status/backlog       # Future consideration
```

**Rule:** Status tags apply to `type/project`, `type/goal`, and `type/sop`.

---

### F. Maturity Tags (For Zettelkasten notes)

Tracks the development level of Atomic Notes.

```yaml
maturity/seedling    # Just captured, needs development
maturity/budding     # Has structure, needs refinement
maturity/evergreen   # Mature, well-developed note
```

**Rule:** Atomic notes (`type/zettel`) MUST have one maturity tag.

---

## Tag Application Rules

### Required Tags

1. **Every note** → At least one `type/*` tag
2. **Atomic notes** (`type/zettel`) → Also need `maturity/*` tag
3. **Projects/Goals/SOPs** → Also need `status/*` tag

### Optional Tags

4. **Topic tags** → 2-4 recommended for discoverability
5. **Business tags** → When content is business-specific
6. **Framework tags** → Only when framework is core to the note

---

## Frontmatter Template

### For Atomic Notes (type/zettel)

```yaml
---
tags:
  - type/zettel
  - maturity/seedling
  - topic/business
  - topic/sales
  - area/business-360
  - business/primary
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**Note:** `area/` tag links the note to the hub, `business/` tag indicates which business it relates to.

### For SOPs/Projects

```yaml
---
tags:
  - type/sop
  - status/active
  - topic/marketing
  - area/business-revolutia
  - business/secondary
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### For Context Files

```yaml
---
tags:
  - type/context
  - area/personal
updated: YYYY-MM-DD
---
```

### For Hub Index Files

```yaml
---
tags:
  - type/hub
  - area/business-360
updated: YYYY-MM-DD
---
```

---

## Migration Guide: Old Tags → New Tags

| Old Format | New Format | Notes |
|------------|-----------|-------|
| `type/zettel` | `type/zettel` | Keep as-is |
| `[[_Marketing]]` | `topic/marketing` | Convert wiki links to tags |
| `[[_Business]]` | `topic/business` | Convert wiki links to tags |
| `[[_Sales]]` | `topic/sales` | Convert wiki links to tags |
| `[[_AI]]` | `topic/ai` | Convert wiki links to tags |
| `360_Degrees` | `business/primary` | Standardize format |
| `SOPs` | `type/sop` | Change to type tag |
| `framework/🌱` | `maturity/seedling` | Remove emoji, use maturity |
| `framework/🍎` | `maturity/evergreen` | Remove emoji, use maturity |

---

## Using Tags in Dataview Queries

### Find all SOPs for {{BUSINESS_PRIMARY}}

```dataview
TABLE file.mtime as "Updated"
FROM "2. Areas"
WHERE contains(tags, "type/sop") AND contains(tags, "business/primary")
SORT file.mtime DESC
```

### Find all Atomic Notes by topic

```dataview
TABLE maturity as "Maturity", topics as "Topics"
FROM "1. Atomic Notes"
WHERE contains(tags, "topic/marketing")
SORT file.mtime DESC
```

### Find all active projects

```dataview
TABLE status as "Status", file.mtime as "Updated"
FROM "2. Areas"
WHERE contains(tags, "type/project") AND contains(tags, "status/active")
SORT file.mtime DESC
```

---

## Best Practices

1. **Be Specific**: Use topic tags that accurately describe the content
2. **Be Consistent**: Use the same tag format across all notes
3. **Be Minimal**: Don't over-tag - 3-5 total tags is usually optimal
4. **Review Regularly**: Update maturity and status tags as notes evolve
5. **Use Templates**: New notes should auto-populate with tag structure

---

## Tag Maintenance

### Monthly Review

- Check for orphaned notes without required tags
- Update maturity tags for Atomic Notes
- Update status tags for projects/goals
- Archive completed or irrelevant content to `5. Archive/`

### Quarterly Review

- Evaluate if new topic tags are needed
- Consolidate redundant tags
- Update this documentation with new patterns

---

**Last updated:** 2026-01-01
