---
skill: find-broken-links
description: Migration utility to identify and fix broken links after folder reorganization
trigger: "/find-broken-links"
---

# Find Broken Links Skill

Scan vault for broken wikilinks and file paths before/after folder reorganization.

---

## When to Use

- **BEFORE folder reorganization** - Identify links that will break
- **AFTER folder reorganization** - Find and fix broken links
- During periodic vault maintenance
- After bulk file moves or renames

**Trigger:** `/find-broken-links [--fix]`

**Modes:**
- `/find-broken-links` - Scan and report only
- `/find-broken-links --fix` - Scan and prompt for fixes

---

## Data Sources

### Required

**Vault Content:**
- All markdown files in vault
- Wikilinks: `[[Note Name]]`, `[[Folder/Note Name]]`, `[[Note Name|Alias]]`
- File paths in Dataview queries
- Canvas file references (`.canvas` files)

**Known Migrations (from reorganization plan):**
```
2. Areas/ → 2. Areas/
2. Reference/ → 3. Reference/
4. Utilities/ → 4. Utilities/
4. Utilities/ → 4. Utilities/
3. Hubs/ → DELETED (topic indexes)
Boards/ → DELETED (or moved to areas)
```

---

## Process

### Step 1: Scan for Links

**Scan all markdown files:**
```
Search for:
  - Wikilinks: [[...]]
  - Wikilinks with paths: [[folder/note]]
  - Wikilinks with aliases: [[note|alias]]
  - Embedded files: ![[image.png]]
  - Dataview queries with path filters
```

**Extract link patterns:**
```
Group links by:
  - Links to 2. Areas/ (will break after rename)
  - Links to 2. Reference/ (will break after rename)
  - Links to 4. Utilities/ (will break after rename)
  - Links to 4. Utilities/ (will break after merge)
  - Links to 3. Hubs/ (will break - folder deleted)
  - Links to Boards/ (will break - folder deleted/moved)
  - Links to topic hubs: [[_Marketing]], [[_Business]], etc. (old format)
```

---

### Step 2: Categorize Broken Links

**Category 1: Folder Path Changes (Auto-fixable)**
```
Pattern: [[02. Areas/business_primary/...]]
Fix: [[02. Areas/business_primary/...]]

Pattern: [[02. Areas/aprendizaje/Books/...]]
Fix: [[02. Areas/aprendizaje/libros/notas/...]]

Pattern: [[03. Sistema/templates/...]]
Fix: [[03. Sistema/templates/...]]

Pattern: [[03. Sistema/templates/...]]
Fix: [[03. Sistema/templates/...]]
```

**Category 2: Deleted Folders (Manual review needed)**
```
Pattern: [[3. Hubs/Marketing/...]]
Action: Convert to tag-based search or atomic note

Pattern: [[Boards/...]]
Action: Check if moved to area, update path
```

**Category 3: Topic Hub Links (Migrate to tags)**
```
Pattern: [[_Marketing]], [[_Business]], [[_Sales]], [[_AI]]
Action: Convert to topic/* tags (manual - context dependent)
Note: These are semantic links, not file references
```

**Category 4: Canvas Files**
```
Pattern: References in .canvas files (JSON format)
Action: Update file paths in JSON
```

---

### Step 3: Generate Report

**Broken Links Report:**

```markdown
# Broken Links Report
Generated: [Date]

## Summary
- Total links scanned: [N]
- Broken links found: [M]
- Auto-fixable: [X]
- Manual review needed: [Y]

---

## Category 1: Folder Path Changes (Auto-fixable)

### 2. Areas/ → 2. Areas/ ([N] links)
- [File.md:42] `[[02. Areas/business_primary/{{BUSINESS_PRIMARY}}.md]]`
- [Another.md:15] `[[02. Areas/personal/objetivos/2025-Goals.md]]`
- [...]

### 2. Reference/ → 3. Reference/ ([N] links)
- [File.md:10] `[[02. Areas/aprendizaje/Books/Book Name.md]]`
- [...]

### 4. Utilities/ → 4. Utilities/ ([N] links)
- [File.md:20] `[[03. Sistema/templates/Daily Note.md]]`
- [...]

### 4. Utilities/ → 4. Utilities/ ([N] links)
- [File.md:30] `[[03. Sistema/templates/Source Note.md]]`
- [...]

---

## Category 2: Deleted Folders (Manual Review Needed)

### 3. Hubs/ (DELETED - [N] links)
⚠️ These topic hubs no longer exist. Consider:
- Converting to Dataview query by tag
- Linking to specific Atomic Notes instead
- Creating new hub index with tag-based aggregation

- [File.md:5] `[[3. Hubs/Marketing/index.md]]`
  → Suggest: Use Dataview query for `topic/marketing`
- [...]

### Boards/ (DELETED/MOVED - [N] links)
⚠️ Canvas files may have been moved to areas. Verify:

- [File.md:8] `[[Boards/Strategy Canvas.canvas]]`
  → Check: Moved to which area?
- [...]

---

## Category 3: Topic Hub Links ([N] links)

⚠️ Old-format topic references. Context-dependent - review manually:

- [Note.md:12] `[[_Marketing]]`
  → If tagging the note: Add `topic/marketing`
  → If linking to content: Use Dataview query or hub index

- [Note.md:25] `[[_Business]]`
  → Same as above
- [...]

---

## Category 4: Canvas Files ([N] files)

Canvas files with embedded paths (JSON format):

- Boards/Strategy.canvas
  - Contains: 3 references to "2. Areas/"
  - Contains: 1 reference to "4. Utilities/"
- [...]

⚠️ Canvas files need MANUAL editing (JSON format)

---

## Dataview Queries with Hardcoded Paths

Files with Dataview queries that use old paths:

- [Hub_360.md:20]
  ```dataview
  FROM "2. Areas/Business-360"
  ```
  → Should be: `FROM "2. Areas/Business-360"`

- [Dashboard.md:30]
  ```dataview
  FROM "3. Utilities"
  ```
  → Should be: `FROM "4. Utilities"`

---

## Recommendations

**Before Reorganization:**
1. Run `/find-broken-links` to generate this report
2. Review Category 2 & 3 manually (deleted folders, topic links)
3. Decide how to handle topic hub links (convert to tags or hub indexes)
4. Backup Canvas files if manual edits needed

**After Reorganization:**
1. Run `/find-broken-links --fix` to auto-fix Category 1
2. Manually fix Category 2, 3, 4
3. Test all Dataview queries
4. Verify Canvas files still work

```

---

### Step 4: Fix Links (if --fix mode)

**For Category 1 (Auto-fixable):**

```
For each broken link:
  1. Read file
  2. Find exact link string
  3. Replace with new path
  4. Verify link now works
  5. Update file
```

**Search & Replace patterns:**
```
[[02. Areas/         → [[02. Areas/
[[02. Areas/aprendizaje/    → [[02. Areas/aprendizaje/
[[03. Sistema/    → [[03. Sistema/
[[03. Sistema/    → [[03. Sistema/

In Dataview queries:
FROM "2. Areas/     → FROM "2. Areas/
FROM "2. Reference/ → FROM "3. Reference/
FROM "4. Utilities/ → FROM "4. Utilities/
FROM "4. Utilities/ → FROM "4. Utilities/
```

**Batch confirmation:**
```
Found [N] auto-fixable links in [M] files.

Apply fixes?
  [1] Yes, fix all (show me the changes)
  [2] Yes, fix all (silent)
  [3] Show me file-by-file for approval
  [4] Generate fix script (bash) for manual review
  [5] Cancel
```

---

## Output

**Scan Mode (default):**
- Markdown report: `/tmp/broken-links-report.md`
- Summary printed to console
- No files modified

**Fix Mode (--fix):**
- Same report as scan mode
- Files modified with auto-fixes applied
- Summary of changes:
  ```
  ✅ Fixed [N] links in [M] files
  ⚠️ [X] links need manual review
  📄 Report saved: /tmp/broken-links-report.md
  ```

---

## Confirmation

Show {{USER_FIRSTNAME}}:

**Scan Mode:**
1. Summary of broken links found
2. Breakdown by category
3. Path to full report
4. Recommendation: "Run --fix to auto-repair Category 1?"

**Fix Mode:**
1. Summary of fixes applied
2. Files modified
3. Links still needing manual review
4. Next steps for manual fixes

**Ask:** "Review the full report? [Path to report]"

---

## Notes

- **Run BEFORE reorganization:** Identify what will break
- **Run AFTER reorganization:** Fix what broke
- **Canvas files:** Require manual JSON editing - this tool only reports them
- **Topic links:** `[[_Marketing]]` are semantic, not file links - handle contextually
- **Dataview queries:** Auto-fixable but test after changes
- **Backup:** iCloud handles versioning, but report gives you full change list

---

## Technical Implementation

**Link Detection Regex Patterns:**
```regex
Wikilinks: \[\[([^\]]+)\]\]
Wikilinks with alias: \[\[([^\]|]+)\|([^\]]+)\]\]
Embedded files: !\[\[([^\]]+)\]\]
Dataview FROM: FROM\s+"([^"]+)"
```

**Canvas File Parsing:**
```
Canvas files are JSON with "file" keys
Parse JSON, extract all "file" values
Check if paths contain old folder names
Report (don't auto-fix - JSON structure sensitive)
```

---

## Example Usage

**Before Reorganization:**
```bash
/find-broken-links
```
Output: Report showing 47 links that will break after folder renames

**After Reorganization:**
```bash
/find-broken-links --fix
```
Output: Fixed 35 auto-fixable links, 12 need manual review

---

**Created:** 2026-01-01

---

## Known Issues & Learnings

_This section is updated automatically as the skill encounters edge cases, errors, or improvements._

| Date | Issue/Learning | Resolution |
|------|---------------|------------|
| — | No issues recorded yet | — |
