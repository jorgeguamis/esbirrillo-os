#!/bin/bash

# Hook: Log Context Changes
# Triggers after Edit or Write tool is used on context files
# Creates timestamped log of changes to context files

# Get the file path from environment variable set by Claude Code
FILE_PATH="${CLAUDE_TOOL_ARG_file_path:-}"

# If no file path provided, exit silently
if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# Only log changes to context files (files with "context" in name)
if [[ ! "$FILE_PATH" =~ context.*\.md$ ]]; then
  exit 0
fi

# Check if file exists
if [ ! -f "$FILE_PATH" ]; then
  exit 0
fi

# Get the log directory
VAULT_PATH="${LIFEOS_ROOT}/${VAULT_NAME}"
LOG_FILE="${LIFEOS_ROOT}/.claude/logs/context-changes.log"

# Ensure log file exists
touch "$LOG_FILE"

# Get timestamp
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Get file basename
FILENAME=$(basename "$FILE_PATH")

# Determine which area this context file belongs to
AREA="Unknown"
if [[ "$FILE_PATH" =~ "Personal" ]]; then
  AREA="Personal"
elif [[ "$FILE_PATH" =~ "Business-360" ]]; then
  AREA="Business-360"
elif [[ "$FILE_PATH" =~ "Business-{{BUSINESS_SECONDARY}}" ]]; then
  AREA="Business-{{BUSINESS_SECONDARY}}"
elif [[ "$FILE_PATH" =~ "Health" ]]; then
  AREA="Health"
elif [[ "$FILE_PATH" =~ "Learning" ]]; then
  AREA="Learning"
elif [[ "$FILE_PATH" =~ "Finances" ]]; then
  AREA="Finances"
elif [[ "$FILE_PATH" =~ "Research" ]]; then
  AREA="Research"
fi

# Determine change type based on environment (if available)
CHANGE_TYPE="Modified"
if [[ "${CLAUDE_TOOL_NAME:-}" == "Write" ]]; then
  if [ ! -f "$FILE_PATH" ]; then
    CHANGE_TYPE="Created"
  fi
fi

# Log the change
echo "[$TIMESTAMP] [$AREA] $CHANGE_TYPE: $FILENAME" >> "$LOG_FILE"

# Optional: Create backup in context-backups directory
BACKUP_DIR="$VAULT_PATH/.claude/logs/context-backups"
mkdir -p "$BACKUP_DIR"

# Create backup filename with timestamp
BACKUP_TIMESTAMP=$(date "+%Y-%m-%d_%H-%M-%S")
BACKUP_FILENAME="${FILENAME%.md}_${BACKUP_TIMESTAMP}.md"
BACKUP_PATH="$BACKUP_DIR/$BACKUP_FILENAME"

# Copy file to backup location
cp "$FILE_PATH" "$BACKUP_PATH" 2>/dev/null || true

# Display confirmation message
echo ""
echo "✓ Context change logged"
echo "  Area: $AREA"
echo "  File: $FILENAME"
echo "  Backup: .claude/logs/context-backups/$BACKUP_FILENAME"
echo ""

# Exit successfully
exit 0
