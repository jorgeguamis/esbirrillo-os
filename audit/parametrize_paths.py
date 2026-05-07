#!/usr/bin/env python3
"""
Parametrize hardcoded paths and personal strings in the kit.

Replaces Jorge-specific values with templated variables so the kit can be
reused by any user. Operates on the kit directory (esbirrillo-os/), NOT on
Jorge's source system.

Variables introduced (Bash-style for shell scripts, Mustache for markdown):
  ${LIFEOS_ROOT}        — workspace root  (was /Users/jorgeguamis/Desktop)
  ${USER_CLAUDE_DIR}    — ~/.claude       (was /Users/jorgeguamis/.claude)
  ${USER_HOME}          — ~                (was /Users/jorgeguamis)
  ${HERMES_HOME}        — ~/.hermes       (was /Users/jorgeguamis/.hermes)
  ${VAULT_NAME}         — vault subdir    (was "Life OS")
  {{USER_NAME}}         — owner full name (was "Jorge Guamis")
  {{USER_FIRSTNAME}}    — owner first     (was "Jorge")

Usage:
  python3 parametrize_paths.py --dry-run
  python3 parametrize_paths.py --apply
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

KIT_ROOT = Path("/Users/jorgeguamis/Desktop/01. Projects/esbirrillo-os")

INCLUDE_EXTS = {".md", ".py", ".sh", ".json", ".yaml", ".yml", ".toml"}
EXCLUDE_DIRS = {".git", "audit", "__pycache__", "node_modules"}

# Order matters: longer/more-specific patterns first to avoid partial overwrites.
SUBSTITUTIONS = [
    # Paths
    (re.compile(r"/Users/jorgeguamis/Desktop/Life OS"), "${LIFEOS_ROOT}/${VAULT_NAME}"),
    (re.compile(r"/Users/jorgeguamis/Desktop/\.claude"), "${LIFEOS_ROOT}/.claude"),
    (re.compile(r"/Users/jorgeguamis/Desktop"), "${LIFEOS_ROOT}"),
    (re.compile(r"/Users/jorgeguamis/\.claude"), "${USER_CLAUDE_DIR}"),
    (re.compile(r"/Users/jorgeguamis/\.hermes"), "${HERMES_HOME}"),
    (re.compile(r"/Users/jorgeguamis/"), "${USER_HOME}/"),
    # Vault path reference
    (re.compile(r"\bLife OS/"), "${VAULT_NAME}/"),
    # Business slugs in folder/tag references (replace before raw name forms)
    (re.compile(r"\bbusiness_360\b"), "business_primary"),
    (re.compile(r"\bbusiness_revolutia\b"), "business_secondary"),
    (re.compile(r"\bbusiness_Monk\b"), "business_tertiary"),
    (re.compile(r"\bbusiness/360\b"), "business/primary"),
    (re.compile(r"\bbusiness/revolutia\b"), "business/secondary"),
    (re.compile(r"\bbusiness/monk\b"), "business/tertiary"),
    # Business names in prose
    (re.compile(r"\b360º Consulting\b"), "{{BUSINESS_PRIMARY}}"),
    (re.compile(r"\b360 Consulting\b"), "{{BUSINESS_PRIMARY}}"),
    (re.compile(r"\b360º\b"), "{{BUSINESS_PRIMARY}}"),
    (re.compile(r"\bRevolutia Academy\b"), "{{BUSINESS_SECONDARY}}"),
    (re.compile(r"\bRevolutia\b"), "{{BUSINESS_SECONDARY}}"),
    (re.compile(r"\bMonktag\b"), "{{BUSINESS_TERTIARY}}"),
    # Personal email and identifiers
    (re.compile(r"jorgeguamis@gmail\.com"), "{{USER_PERSONAL_EMAIL}}"),
    (re.compile(r"jorge@360consulting\.io"), "{{USER_PRIMARY_EMAIL}}"),
    (re.compile(r"jorge\.guamis@revolutia\.ai"), "{{USER_SECONDARY_EMAIL}}"),
    (re.compile(r"cal\.com/jorge-guamis-360"), "{{USER_CAL_URL}}"),
    # Domain-agent names from source system → core/role-based references.
    # These let the residue files describe routing in terms of core roles
    # (the actual user agents are created by /setup-wizard create-my-agent).
    (re.compile(r"\bStark\b"), "{{DOMAIN_AGENT_SALES}}"),
    (re.compile(r"\bShakes\b"), "{{DOMAIN_AGENT_COPY}}"),
    (re.compile(r"\bRevo\b"), "{{DOMAIN_AGENT_PRODUCT}}"),
    (re.compile(r"\bPenny\b"), "{{DOMAIN_AGENT_FINANCE}}"),
    (re.compile(r"\bDots\b"), "librarian"),
    (re.compile(r"\bMany\b"), "techy"),
    (re.compile(r"\bJorge agent\b"), "reviewer agent"),
    (re.compile(r"\bagente Jorge\b"), "agente reviewer"),
    # Personal names — last
    (re.compile(r"\bJorge Guamis\b"), "{{USER_NAME}}"),
    (re.compile(r"\bJorge\b(?!\s+(?:agent|del))"), "{{USER_FIRSTNAME}}"),
]

# Files/patterns we DO NOT touch.
SKIP_PATHS = (
    "audit/",
    "vault-template/03. Sistema/templates/",  # Obsidian Templater syntax — leave intact
    "docs/",                                  # docs about the kit itself — references to the author are intentional
    "README.md",
    "ARCHITECTURE.md",
    ".gitignore",
)


def should_process(path: Path) -> bool:
    if path.suffix not in INCLUDE_EXTS:
        return False
    rel = str(path.relative_to(KIT_ROOT))
    if any(rel.startswith(skip) for skip in SKIP_PATHS):
        return False
    if any(part in EXCLUDE_DIRS for part in path.parts):
        return False
    return True


def process_file(path: Path, apply: bool) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    try:
        original = path.read_text(encoding="utf-8")
    except Exception:
        return counts

    text = original
    for pattern, replacement in SUBSTITUTIONS:
        new_text, n = pattern.subn(replacement, text)
        if n:
            counts[replacement] += n
            text = new_text

    if text != original and apply:
        path.write_text(text, encoding="utf-8")

    return counts


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true")
    group.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    apply = args.apply

    total_files = 0
    touched_files = 0
    total_subs: dict[str, int] = defaultdict(int)
    per_file: list[tuple[Path, int]] = []

    for path in KIT_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if not should_process(path):
            continue
        total_files += 1
        counts = process_file(path, apply=apply)
        if counts:
            touched_files += 1
            file_total = sum(counts.values())
            per_file.append((path, file_total))
            for k, v in counts.items():
                total_subs[k] += v

    per_file.sort(key=lambda kv: -kv[1])

    print(f"Mode: {'APPLY' if apply else 'DRY-RUN'}")
    print(f"Files scanned:  {total_files}")
    print(f"Files {'modified' if apply else 'would be modified'}: {touched_files}")
    print()
    print("Substitutions by token:")
    for tok, n in sorted(total_subs.items(), key=lambda kv: -kv[1]):
        print(f"  {tok:30s} {n:5d}")
    print()
    print("Top 20 files (by # subs):")
    for path, n in per_file[:20]:
        rel = path.relative_to(KIT_ROOT)
        print(f"  {n:4d}  {rel}")


if __name__ == "__main__":
    sys.exit(main())
