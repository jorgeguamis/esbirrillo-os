---
description: Create an Atomic Note from a concept with proper tags and connections
---

# Create Atomic Note

Create a new Atomic Note (Zettelkasten-style evergreen knowledge note) from a concept, automatically finding connections and suggesting proper tags.

**Usage:** `/create-atomic [concept name]`

**Example:** `/create-atomic Context Engineering`

## Process

### 1. Validate Concept

**Check if concept is provided:**
- If `$arguments` is empty, ask: "What concept do you want to create an Atomic Note for?"
- If provided, use `$arguments` as the concept name

**Check if note already exists:**
- Search for existing notes in `1. Atomic Notes/` matching the concept
- Use case-insensitive search
- If exact match found:
  - Show: "⚠️ Note [[ConceptName]] already exists!"
  - Ask: "Do you want to: (open/create-anyway/cancel)"
  - `open` → Show path to existing note
  - `create-anyway` → Continue with modified filename (add " v2" or date)
  - `cancel` → Stop command

### 2. Find Related Atomic Notes

**Multi-strategy search for connections:**

**Strategy 1: Semantic Search (if Serena MCP available)**
- Use Serena to find semantically similar notes in `1. Atomic Notes/`
- Look for conceptual relationships, not just keyword matches

**Strategy 2: Keyword Search**
- Extract keywords from concept name
- Grep for keywords in Atomic Notes content
- Case-insensitive, whole-word matches preferred

**Strategy 3: Tag-Based Search**
- Determine likely topics for this concept
- Find other notes with similar topic tags
- Use Grep to search frontmatter for topic/* tags

**Scoring system:**
- Semantic match (Serena): 5 points
- Title contains keyword: 5 points
- Content mentions concept 3+ times: 3 points
- Content mentions concept 1-2 times: 2 points
- Shared topic tag: 2 points per tag

**Connection threshold:**
- Include connection if score ≥ 5
- Target: Minimum 3 connections, Maximum 10 connections
- If 0 connections found: Note this, suggest creating foundational note

### 3. Suggest Tags

**Read tag system:**
- Reference `.claude/tag-system.md` for valid tags

**Required tags:**
- `type/zettel` (always for Atomic Notes)
- `maturity/seedling` (default for new notes)

**Suggest topic tags (2-4):**
- Analyze concept name and related notes
- Suggest most relevant `topic/*` tags
- Examples: `topic/ai`, `topic/prompting`, `topic/business`, `topic/productivity`

**Optional tags (suggest if clearly applicable):**
- `area/*` - If concept relates to specific life area
- `business/*` - If concept is business-specific
- `framework/*` - If concept IS a framework itself

**Show tag suggestions to user:**
```
Suggested tags for [[Concept Name]]:
Required:
  - type/zettel
  - maturity/seedling

Recommended:
  - topic/ai
  - topic/prompting
  - area/learning

Optional:
  - framework/prp (if this concept is a framework)

Add/remove any tags? (yes/no)
```

### 4. Generate Note Structure

**Create frontmatter:**
```yaml
---
tags:
  - type/zettel
  - maturity/seedling
  - [topic tags]
  - [area tag if applicable]
  - [business tag if applicable]
created: DD-MM-YYYY
updated: DD-MM-YYYY
---
```

**Create content structure:**
```markdown
# [Concept Name]

## Definición

[Brief explanation placeholder - user to fill]

## Contexto

¿Por qué es importante este concepto? ¿Dónde se aplica?

## Aplicaciones

### En Life OS
- [How this applies to your Life OS workflow]

### En [Relevant Area]
- [Specific applications in business/learning/health/etc.]

## Relaciones

### Conceptos Relacionados
[Connections found - auto-generated]

### Contrasta Con
[Optional - concepts this differs from]

## Recursos

### Referencias
- [Links to source notes if applicable]

### Para Profundizar
- [Topics to explore further]

## Notas

[Any additional thoughts or observations]
```

**Auto-fill Connections section:**
```markdown
### Conceptos Relacionados
- [[Related Note 1]] - [1-sentence reason for connection]
- [[Related Note 2]] - [1-sentence reason for connection]
- [[Related Note 3]] - [1-sentence reason for connection]
```

### 5. Create File

**Determine filename:**
- Use concept name as filename
- Sanitize: remove special characters, keep spaces
- Example: "Context Engineering" → `Context Engineering.md`
- If exists, append " v2" or date

**Full file path:**
- `1. Atomic Notes/[Concept Name].md`

**Create file with:**
- Frontmatter with suggested tags
- Content structure with placeholder text
- Auto-filled connections section

### 6. Confirm and Next Steps

**Show success message:**
```
✓ Created: [[Concept Name]]
✓ Location: 1. Atomic Notes/[Concept Name].md
✓ Connections: X notes linked
✓ Tags: [list of tags]

Next steps:
1. Fill in the "Definición" section with core concept
2. Add context about why it matters
3. Develop "Aplicaciones" section with concrete examples
4. Review connections - remove irrelevant, add missing
5. Update maturity tag as note develops (seedling → budding → evergreen)

Tip: Run `/create-atomic [related concept]` for concepts mentioned that deserve their own notes!
```

**Suggest related concepts to create:**
- If connections found mention concepts without notes, suggest them
- Example: "Consider creating notes for: [[Concept X]], [[Concept Y]]"

## Examples

**Example 1: AI concept**
```
/create-atomic Prompt Engineering

Creates:
- File: 1. Atomic Notes/Prompt Engineering.md
- Tags: type/zettel, maturity/seedling, topic/ai, topic/prompting
- Connections: [[Chain-of-Thought Prompting]], [[Few-Shot Prompting]], [[Meta-prompting]]
```

**Example 2: Business concept**
```
/create-atomic Value Equation

Creates:
- File: 1. Atomic Notes/Value Equation.md
- Tags: type/zettel, maturity/seedling, topic/business, topic/sales, framework/value-equation
- Connections: [[Offer Creation]], [[Dream 100]], [[100M Offers]]
```

**Example 3: Personal development**
```
/create-atomic Energy Management

Creates:
- File: 1. Atomic Notes/Energy Management.md
- Tags: type/zettel, maturity/seedling, topic/productivity, topic/mindset, area/personal
- Connections: [[Time Management]], [[Focus]], [[Deep Work]]
```

## Edge Cases

**Zero connections found:**
```
⚠️ No related notes found for this concept.

This might be:
1. A foundational concept for your vault
2. A new area of knowledge you're exploring
3. An orphan concept that needs context

Recommendation:
- Create the note anyway
- In "Relaciones" section, note this is a foundational concept
- As you create more notes, connections will emerge naturally
```

**Too many potential connections (>10):**
- Use scoring system to select top 10
- Mention in note: "Note: X additional related notes exist. Search #topic/[tag] to find them."

**Concept name is too vague:**
- Examples: "idea", "thoughts", "notes"
- Ask user: "That's pretty vague. Can you be more specific about the concept?"
- Suggest: "Try describing it in 2-3 words"

**Duplicate with different wording:**
- Search for synonyms/variations
- If found, ask: "Found [[Similar Concept]]. Is this the same thing?"
- If yes, stop and point to existing note
- If no, continue but suggest linking the two notes

## Notes

- Atomic Notes are evergreen - they should be concept-focused, not time-bound
- Start with `maturity/seedling` - it's okay for notes to be incomplete
- The goal is capture and connect, not perfect from day one
- Connections are more valuable than lengthy content
- Use this command liberally - it's better to have many small connected notes than few large disconnected ones

## Integration with Other Commands

- After creating note, consider using `/tag-note` to refine tags
- Use `/process-inbox` to move captured thoughts into proper Atomic Notes
- Reference new Atomic Notes in daily notes when concepts are applied
