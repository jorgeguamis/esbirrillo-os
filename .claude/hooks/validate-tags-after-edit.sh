#!/bin/bash

# Hook: Validate Tags After Edit
# Triggers after Edit or Write tool is used
# Validates frontmatter and tags in Atomic Notes

# Get the file path from environment variable set by Claude Code
# This will be set when the hook is triggered
FILE_PATH="${CLAUDE_TOOL_ARG_file_path:-}"

# If no file path provided, exit silently
if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# Only validate files in Atomic Notes directory
if [[ ! "$FILE_PATH" =~ "1. Atomic Notes/" ]]; then
  exit 0
fi

# Only validate .md files
if [[ ! "$FILE_PATH" =~ \.md$ ]]; then
  exit 0
fi

# Check if file exists
if [ ! -f "$FILE_PATH" ]; then
  exit 0
fi

# Extract frontmatter and check for required tags
has_frontmatter=$(head -n 1 "$FILE_PATH" | grep -c "^---$" || true)

if [ "$has_frontmatter" -eq 0 ]; then
  echo "⚠️ WARNING: No frontmatter found in Atomic Note"
  echo "   File: $FILE_PATH"
  echo "   Atomic Notes should have frontmatter with tags"
  exit 0
fi

# Extract tags section from frontmatter
tags_section=$(awk '/^---$/,/^---$/ {print}' "$FILE_PATH" | grep -A 20 "^tags:" || true)

# Check for required tags
has_type_zettel=$(echo "$tags_section" | grep -c "type/zettel" || true)
has_maturity=$(echo "$tags_section" | grep -c "maturity/" || true)
has_topic=$(echo "$tags_section" | grep -c "topic/" || true)

warnings=()

if [ "$has_type_zettel" -eq 0 ]; then
  warnings+=("Missing required tag: type/zettel")
fi

if [ "$has_maturity" -eq 0 ]; then
  warnings+=("Missing required tag: maturity/* (seedling/budding/evergreen)")
fi

if [ "$has_topic" -eq 0 ]; then
  warnings+=("Missing recommended tags: topic/* (should have 2-4)")
elif [ "$has_topic" -eq 1 ]; then
  warnings+=("Only 1 topic tag found (recommend 2-4 for better discoverability)")
fi

# Check date format (DD-MM-YYYY)
created_date=$(awk '/^---$/,/^---$/ {print}' "$FILE_PATH" | grep "^created:" | cut -d' ' -f2 || true)
if [ -n "$created_date" ]; then
  # Check if date matches DD-MM-YYYY format
  if ! echo "$created_date" | grep -qE "^[0-9]{2}-[0-9]{2}-[0-9]{4}$"; then
    warnings+=("Invalid date format in 'created': $created_date (should be DD-MM-YYYY)")
  fi
fi

updated_date=$(awk '/^---$/,/^---$/ {print}' "$FILE_PATH" | grep "^updated:" | cut -d' ' -f2 || true)
if [ -n "$updated_date" ]; then
  if ! echo "$updated_date" | grep -qE "^[0-9]{2}-[0-9]{2}-[0-9]{4}$"; then
    warnings+=("Invalid date format in 'updated': $updated_date (should be DD-MM-YYYY)")
  fi
fi

# If there are warnings, display them
if [ "${#warnings[@]}" -gt 0 ]; then
  echo ""
  echo "⚠️  FRONTMATTER VALIDATION WARNINGS"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  filename=$(basename "$FILE_PATH")
  echo "File: $filename"
  echo ""
  for warning in "${warnings[@]}"; do
    echo "  • $warning"
  done
  echo ""
  echo "Tip: Consider running validate-frontmatter agent to see detailed recommendations"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
fi

# Exit successfully (don't block the operation)
exit 0
