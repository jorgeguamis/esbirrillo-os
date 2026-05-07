---
skill: process-youtube-video
description: Process YouTube videos into structured reference notes with deep analysis, auto-tagging, and connections
trigger: "/process-youtube-video [youtube-url]"
---

# Process YouTube Video Skill

Convert YouTube videos into structured reference notes with deep analysis, automatic connections to atomic notes, intelligent tagging, and selective timestamp extraction.

---

## When to Use

- When {{USER_FIRSTNAME}} wants to process a YouTube video into a structured note
- When learning from video content (any life area: business, personal, health, learning, etc.)
- When capturing knowledge from YouTube to integrate into Life OS

**Trigger:** `/process-youtube-video [YouTube URL]`

**Examples:**
- `/process-youtube-video https://youtube.com/watch?v=CxbHw93oWP0`
- `/process-youtube-video https://youtu.be/CxbHw93oWP0`

---

## Data Sources

### Required
**YouTube URL:** Full YouTube video URL (youtube.com/watch?v= or youtu.be/)

### Automatically Gathered
**Transcript extraction:**
- Python script (`.claude/scripts/get_youtube_transcript.py`)
- Tries Spanish first, English second
- Fallback to manual input if automated extraction fails

**Context for analysis:**
- [[.claude/tag-system.md|Tag System]] - Valid tag taxonomy
- [[01. Atomic Notes/|Atomic Notes]] - For finding connections (52 notes)
- All life areas: business-360, business-revolutia, personal, health, learning, research, finances

---

## Process

### Step 1: Extract Video Information

**Parse YouTube URL:**
1. Extract video ID from URL (supports `youtube.com/watch?v=` and `youtu.be/` formats)
2. Validate URL format

**Attempt automatic transcript extraction:**
```bash
python .claude/scripts/get_youtube_transcript.py [video_id]
```

**If automatic extraction fails:**
- Ask user to provide transcript manually
- Message: "Could not extract transcript automatically. Please copy transcript from YouTube (click 'Show Transcript' below video) and paste it here."

**Fallback:**
If no transcript available at all:
- Ask if user wants to provide manual notes/summary
- Or skip video processing

---

### Step 2: Analyze Content

**Perform deep analysis of transcript:**
1. Extract 5-10 key concepts, frameworks, methodologies
2. Identify main themes and topics
3. Detect relevant frameworks (e.g., Value Equation, MAGIC, etc.)
4. Determine which life area(s) this video applies to:
   - Business ({{BUSINESS_PRIMARY}} or {{BUSINESS_SECONDARY}})
   - Personal development / productivity
   - Health & fitness
   - Learning & education
   - Research & knowledge
   - Finances & investments

**Key insight:** This is NOT just for business content. {{USER_FIRSTNAME}} learns from videos across all life areas.

---

### Step 3: Find Connections to Atomic Notes

**Multi-strategy search:**

**Strategy 1: Title Matching**
```bash
# For each key concept, search atomic note titles
Glob pattern: "1. Atomic Notes/**/*{concept}*.md"
```

**Strategy 2: Content Matching**
```bash
# Search inside atomic notes for concept mentions
Grep with -i flag (case-insensitive) in "1. Atomic Notes/"
```

**Strategy 3: Tag Matching**
- Compare video topics with tags in atomic notes
- Look for overlapping topics

**Scoring system:**
- Title match: 5 points
- Content match with context: 3 points
- Tag overlap: 2 points
- **Threshold:** Include connection if score ≥ 5
- **Limits:** Minimum 3 connections, Maximum 10 connections

**For each connection:**
1. Read the atomic note to validate relevance
2. Write a 1-sentence justification
3. Create wikilink: `[[Note Title]] - Justification`

**If zero connections found:**
- Still create the note
- Add section "Potential Atomic Notes" suggesting concepts that could become new atomic notes

---

### Step 4: Generate Auto-Tags

**Read tag taxonomy:**
```bash
# Get valid tags from tag system
Read: .claude/tag-system.md
```

**Apply mandatory tags:**
- `type/source` (always for YouTube videos)
- `created: DD-MM-YYYY` (format: day-month-year, e.g., 02-01-2026)

**Detect 2-4 topic tags:**
- Pattern matching on transcript keywords
- Semantic analysis with Claude
- Examples: `topic/ai`, `topic/prompting`, `topic/marketing`, `topic/sales`, `topic/productivity`

**Identify life area (NOT just business):**
- `area/business-360` - If relevant to {{BUSINESS_PRIMARY}}
- `area/business-revolutia` - If relevant to {{BUSINESS_SECONDARY}}
- `area/personal` - Personal development, productivity, life optimization
- `area/health` - Health, fitness, nutrition, wellness
- `area/learning` - Learning skills, education, courses
- `area/research` - Research, knowledge management
- `area/finances` - Finances, investments, money management

**Business tags (OPTIONAL - only if clearly business-related):**
- `business/primary` - Specific to {{BUSINESS_PRIMARY}}
- `business/secondary` - Specific to {{BUSINESS_SECONDARY}}
- `business/both` - Relevant to both businesses

**Important:** Most videos will NOT have a business tag (e.g., health, personal development, learning videos).

---

### Step 5: Generate Note Content

**Create frontmatter:**
```yaml
---
up:
related:
tags:
  - type/source
  - topic/[tag1]
  - topic/[tag2]
  - area/[life-area]
  - business/[360|revolutia|both]  # OPTIONAL
author: "[[Author Name or Channel]]"
url: [Full YouTube URL]
title: "[Full Video Title]"
created: DD-MM-YYYY
---
```

**Generate content structure:**

```markdown
# [Video Title]

## Resumen Ejecutivo
[2-3 paragraph synthesis by Claude analyzing the core message, key insights, and overall value of the video]

## Conceptos Clave

### [Concept 1 Name]
**Resumen:** [Brief 1-2 sentence explanation]

**Desarrollo:**
[Detailed analysis of the concept based on transcript]

**Aplicación Práctica:**
- [How to apply this specifically to {{USER_FIRSTNAME}}'s context]
- [Concrete examples or next actions]

[Timestamp ONLY if strictly relevant: [12:34]]

### [Concept 2 Name]
[Same structure...]

## Conexiones
- [[Atomic Note 1]] - [1-sentence justification for the connection]
- [[Atomic Note 2]] - [1-sentence justification]
- [[Atomic Note 3]] - [1-sentence justification]
[Minimum 3, maximum 10 connections]

## Aplicaciones Prácticas
**[Relevant Life Area]:**
- [Specific ways to apply this knowledge]
- [Concrete actions {{USER_FIRSTNAME}} can take]

**Examples of areas:**
- {{BUSINESS_PRIMARY}} (client work, sales, consulting)
- {{BUSINESS_SECONDARY}} (teaching, content, courses)
- Personal Development (productivity, growth, habits)
- Health & Fitness (exercise, nutrition, wellness)
- Learning (new skills, education)
- Finances (investments, money management)
- Research (knowledge, study)

## Potential Atomic Notes
- "[Concept with no match]" - Why this deserves its own atomic note
- "[Another concept]" - Reason
```

**Timestamp guidelines:**
- ONLY include timestamps when strictly relevant:
  - Specific technique demonstration at a moment
  - Key quote that's worth revisiting
  - Critical example at specific time
- DO NOT timestamp every section or concept
- Format: `[MM:SS]` or `[HH:MM:SS]`

---

### Step 6: Confirm with User

**Show preview:**
```
Preview of YouTube note for: "[Video Title]"

Suggested tags:
- type/source
- topic/ai
- topic/prompting
- area/business-revolutia
- business/secondary

Found 5 connections to atomic notes:
- [[Few-Shot Prompting]]
- [[Chain-of-Thought Prompting]]
- [[Prompt Engineering]]
- [[AI]]
- [[{{BUSINESS_SECONDARY}}]]

Concepts for potential new atomic notes:
- "Spartan Tone of Voice"
- "AO Optimization Method"

[Full note preview in markdown]

Save this note to 3. Reference/Youtube/? [Yes/Modify/Cancel]
```

**User options:**
1. **Yes** - Save note as-is
2. **Modify** - Ask for specific changes (tags, connections, content)
3. **Cancel** - Don't save, discard

---

## Output

**File location:** `3. Reference/Youtube/[Video-Title-Sanitized].md`

**File naming:**
- Sanitize title (remove special characters, limit length)
- Examples:
  - `Prompt Engineering Hacks - Nick Saraev.md`
  - `How to Build a Second Brain - Tiago Forte.md`

**Success message:**
```
✓ Note saved: 3. Reference/Youtube/[Video-Title].md
✓ 5 connections added
✓ 4 tags applied

Suggestions:
- Consider creating atomic note for "Spartan Tone of Voice"
- Consider creating atomic note for "AO Optimization"

Run /tag-note to create these atomic notes?
```

---

## Post-Work

**After saving note:**
1. Suggest concepts that should become atomic notes
2. Offer to run `/tag-note` skill to create them
3. If video is part of a series, suggest processing related videos

**If video already processed:**
- Detect existing file at same path
- Ask: "This video was already processed. Update existing note or create new version?"
- Options:
  - Update (merge/replace content)
  - Create v2 (append date to filename)
  - Cancel

---

## Error Handling

### No transcript available
**Message:** "This video has no transcript. Would you like to:"
- A) Provide your own notes/summary for analysis
- B) Skip processing (transcript required for deep analysis)

### Invalid YouTube URL
**Message:** "Invalid YouTube URL. Please provide a valid link."
**Example:** `https://youtube.com/watch?v=abc123`

### Zero connections found
**Action:**
- Still create the note
- Emphasize "Potential Atomic Notes" section
- Suggest running `/tag-note` to create connections later

### Python library not installed
**Message:** "youtube-transcript-api not installed. Installing..."
**Action:** Run `pip install youtube-transcript-api`

### File already exists
**Message:** "A note for this video already exists at 3. Reference/Youtube/[title].md"
**Options:**
- Update existing note
- Create version 2 (with date suffix)
- Cancel

---

## Notes

### Key Principles

1. **Extraction first, manual fallback:** Always try automatic transcript extraction, but have clear fallback to manual input
2. **All life areas:** This is NOT just for business videos - {{USER_FIRSTNAME}} learns from content across all areas of life
3. **Smart connections:** Use multi-strategy search with scoring to find high-quality connections
4. **Preview before save:** ALWAYS show user what will be created before writing the file
5. **Validate wikilinks:** Ensure atomic note exists before creating wikilink
6. **Selective timestamps:** Only add timestamps when they provide real value
7. **Date format:** Always use DD-MM-YYYY (day-month-year)

### Processing Philosophy

**Deep analysis over surface capture:**
- Don't just summarize - analyze and synthesize
- Find connections to existing knowledge (atomic notes)
- Identify practical applications specific to {{USER_FIRSTNAME}}'s context
- Suggest new atomic notes for concepts worth developing

**User experience:**
- Total flow: URL → saved note in <5 minutes
- Clear progress indicators
- Transparent about what's happening (extracting, analyzing, connecting)
- Preview before committing (no surprises)

**Quality thresholds:**
- Minimum 3 connections to atomic notes (or explain why none found)
- 2-4 topic tags (not too few, not too many)
- Clear life area identification
- Timestamps only when truly relevant

---

## Future Enhancements

**Potential improvements for later:**
1. Batch processing multiple videos from a playlist
2. Automatic detection of video series/related content
3. Integration with Notion for task creation from "Aplicaciones Prácticas"
4. Support for other video platforms (Vimeo, Loom, etc.)
5. Summary quality scoring (ask Claude to rate its own analysis)

---

## Examples

**Example 1: Business video**
```
Video: "Prompt Engineering Hacks" by Nick Saraev
Area: business-revolutia (teaching AI)
Tags: type/source, topic/ai, topic/prompting, area/business-revolutia, business/secondary
Connections: [[Few-Shot Prompting]], [[AI]], [[{{BUSINESS_SECONDARY}}]]
```

**Example 2: Personal development video**
```
Video: "Atomic Habits Explained" by James Clear
Area: personal (habits, productivity)
Tags: type/source, topic/productivity, topic/habits, area/personal
Connections: [[Habit Stacking]], [[1% Better]], [[Personal Growth]]
```

**Example 3: Health video**
```
Video: "Science of Sleep Optimization" by Andrew Huberman
Area: health (sleep, wellness)
Tags: type/source, topic/sleep, topic/health, area/health
Connections: [[Sleep]], [[Circadian Rhythm]], [[Health Optimization]]
```

**Example 4: Learning video**
```
Video: "How to Learn Faster" by Ali Abdaal
Area: learning (meta-learning)
Tags: type/source, topic/learning, topic/productivity, area/learning
Connections: [[Active Recall]], [[Spaced Repetition]], [[Learning]]
```

---

This skill transforms YouTube videos from passive consumption into active knowledge integration across ALL of {{USER_FIRSTNAME}}'s life areas.

---

## Known Issues & Learnings

_This section is updated automatically as the skill encounters edge cases, errors, or improvements._

| Date | Issue/Learning | Resolution |
|------|---------------|------------|
| — | No issues recorded yet | — |
