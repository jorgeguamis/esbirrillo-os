---
skill: create-hub-index
description: Generate a hub index file for an area with customized Dataview queries
trigger: "/create-hub-index [area-name]"
---

# Create Hub Index Skill

Generate a hub index file (`Hub_{AreaName}.md`) for a specified area with appropriate Dataview queries.

---

## When to Use

- Creating hub for new area
- Regenerating hub after structure changes
- Adding missing hub to existing area

**Trigger:** `/create-hub-index [area-name]`

**Examples:**
- `/create-hub-index Business-Primary`
- `/create-hub-index Personal`
- `/create-hub-index Research`

---

## Data Sources

### Required

**From {{USER_FIRSTNAME}}:**
- Area name (Business-Primary, Business-{{BUSINESS_SECONDARY}}, Personal, Health, Finances, Learning, Research)

**From vault structure:**
- Area folder path: `2. Areas/[area-name]/`
- Subfolders present (projects/, sops/, clients/, etc.)
- Context file: `2. Areas/[area-name]/context.md`

**Hub Index Template:**
- `4. Utilities/Templates/Hub Index.md`

---

## Process

### Step 1: Validate Area

**Check that area exists:**
```
Path exists: 2. Areas/[area-name]/
Context file exists: 2. Areas/[area-name]/context.md
```

**If area doesn't exist:**
- Ask {{USER_FIRSTNAME}}: "Area '[area-name]' doesn't exist. Should I create it?"
- If yes → create folder + context.md first
- If no → abort

---

### Step 2: Analyze Area Structure

**Detect subfolders:**
```
Scan 2. Areas/[area-name]/ for:
  - projects/
  - sops/
  - clients/
  - courses/
  - workshops/
  - goals/
  - frameworks/
  - etc.
```

**Determine business tag:**
```
If Business-Primary → business/primary
If Business-{{BUSINESS_SECONDARY}} → business/secondary
If Personal/Health/Finances/Learning/Research → no business tag (or ask)
```

---

### Step 3: Customize Hub Template

**Read Hub Index template**

**Customize for this area:**

1. **Replace placeholders:**
   - `[AREA_NAME]` → actual area name (e.g., "Business-Primary")
   - `[area/[AREA_NAME]]` → area tag (e.g., "area/business-360")
   - `[BUSINESS_TAG]` → business tag (e.g., "business/primary") or remove section

2. **Adjust Quick Access links:**
   ```
   Based on detected subfolders, add:
   - [[projects/|Projects Folder]]
   - [[sops/|SOPs Folder]]
   - [[clients/|Clients Folder]]
   - [[goals/|Goals]]
   - [[frameworks/|Frameworks]]
   etc.
   ```

3. **Customize Dataview queries:**
   - Adjust path filters to match area
   - Add/remove query sections based on subfolder structure
   - Ensure business tag filter is correct (or removed)

4. **Add area-specific sections:**
   ```
   For Business areas:
     - Keep SOPs, Projects, Frameworks sections

   For Personal:
     - Add Goals section
     - Add Life Map reference
     - Add Patterns (memory.md)

   For Health:
     - Add Health Metrics
     - Add Workout/Nutrition tracking

   For Learning:
     - Add Books/Courses sections
     - Add People references

   For Research:
     - Add Experiments section
     - Add Research Log
   ```

---

### Step 4: Generate Hub File

**File location:** `2. Areas/[area-name]/Hub_[area-name].md`

**File naming:**
- Business-Primary → `Hub_360-Consulting.md`
- Business-{{BUSINESS_SECONDARY}} → `Hub_Business2.md`
- Personal → `Hub_Personal.md`
- Health → `Hub_Health.md`
- Finances → `Hub_Finances.md`
- Learning → `Hub_Learning.md`
- Research → `Hub_Research.md`

**Content:**
- Use customized template
- Include all relevant Dataview queries
- Add area-specific sections
- Set proper frontmatter tags

---

### Step 5: Test Queries

**Open hub file in Obsidian Preview mode**

**Verify each Dataview query:**
```
For each query:
  - Check if it executes without errors
  - Check if it returns expected results (or empty if no content yet)
  - Adjust filters if needed
```

**Common issues:**
- Path incorrect (folder renamed, etc.)
- Tag format incorrect
- Query syntax error

---

## Output

**Created file:** `2. Areas/[area-name]/Hub_[area-name].md`

**Contains:**
✅ Customized Quick Access links
✅ Working Dataview queries for:
   - SOPs & How-Tos
   - Frameworks
   - Active Projects
   - Related Atomic Notes
   - Recent Activity
✅ Area-specific sections
✅ Proper frontmatter tags

---

## Confirmation

Show {{USER_FIRSTNAME}}:
1. Hub file created at: `2. Areas/[area-name]/Hub_[area-name].md`
2. Sections included:
   - [List of sections]
3. Queries tested: [✅ All working | ⚠️ Some need adjustment]
4. Preview of query results

**Ask:** "Hub created for [area-name]. Open it to review?"

---

## Notes

- **Test queries:** Always test in Preview mode before confirming
- **Customization:** Each area has different needs - adjust template accordingly
- **Updates:** If area structure changes, regenerate hub with this skill
- **Links:** Ensure all internal links use correct paths

---

**Created:** 2026-01-01

---

## Known Issues & Learnings

_This section is updated automatically as the skill encounters edge cases, errors, or improvements._

| Date | Issue/Learning | Resolution |
|------|---------------|------------|
| — | No issues recorded yet | — |
