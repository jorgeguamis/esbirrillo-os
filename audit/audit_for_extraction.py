#!/usr/bin/env python3
"""
Audit Jorge's `.claude/` and vault to classify each file for extraction
into the esbirrillo-os Starter Kit.

Detects personal strings (names, businesses, emails, Notion IDs, hardcoded
paths) and assigns each file a category:
  - CLEAN          0 hits, drop into kit as-is
  - NEEDS_CLEANUP  1-5 hits, parametrize and include
  - PERSONAL       >5 hits, exclude or rewrite from scratch

Output: markdown report at audit/report.md and CSV at audit/findings.csv
"""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT_PATHS = [
    Path("/Users/jorgeguamis/Desktop/.claude"),
    Path("/Users/jorgeguamis/Desktop/Life OS"),
    Path("/Users/jorgeguamis/Desktop/CLAUDE.md"),
]

OUTPUT_DIR = Path("/Users/jorgeguamis/Desktop/01. Projects/esbirrillo-os/audit")

EXCLUDE_DIRS = {
    ".git", ".obsidian", "node_modules", "_archived", ".trash",
    "logs", "reports", "plans", "agent-memory",
}

INCLUDE_EXTS = {".md", ".py", ".sh", ".json", ".yaml", ".yml", ".toml"}

PATTERNS = {
    "jorge": re.compile(r"\b(?:Jorge|Guamis|jorgeguamis)\b", re.IGNORECASE),
    "business_360": re.compile(r"\b(?:360\s*Consulting|360º|360 Consulting|@360consulting\.io)\b", re.IGNORECASE),
    "revolutia": re.compile(r"\b(?:Revolutia|@revolutia\.ai)\b", re.IGNORECASE),
    "monk": re.compile(r"\b(?:Monktag|Monk(?!\s*ey))\b"),
    "people": re.compile(r"\b(?:Alex Gimeno|Juan Santacruz|Mauro Flecha|Diego Hidalgo|Tobias|Albert Albadalejo|Nuria|Javier Pinilla|Adriana)\b"),
    "clients_360": re.compile(r"\b(?:LabArmonia|ArmoniaBio|Cuchillas Castillo|Burrito Blanco|INCOTEC|Wiempire|CPD|SIE|QEC|Navarrete)\b"),
    "notion_ids": re.compile(r"\b(?:2d21320d-44b1-4a17-8311-fc92269b018e|00995a39-458c-486d-aa25-3301f707d837|2338eff7-5947-81b1-b11c-000b216e501a|a7b99031-cc18-4a26-bc9c-db7128b14af4|c9b88936-3c5c-43fb-8315-847ca5068e4a|d1151886-edaa-4382-bd50-db8983c41eae)\b"),
    "hardcoded_paths": re.compile(r"/Users/jorgeguamis/"),
    "cal_com": re.compile(r"cal\.com/jorge-guamis-360"),
    "personal_email": re.compile(r"jorgeguamis@gmail\.com"),
}

CLEAN_THRESHOLD = 0
CLEANUP_THRESHOLD = 5


@dataclass
class FileFinding:
    path: Path
    total_hits: int = 0
    by_category: dict[str, int] = field(default_factory=lambda: defaultdict(int))
    sample_lines: list[tuple[int, str]] = field(default_factory=list)

    @property
    def category(self) -> str:
        if self.total_hits == CLEAN_THRESHOLD:
            return "CLEAN"
        if self.total_hits <= CLEANUP_THRESHOLD:
            return "NEEDS_CLEANUP"
        return "PERSONAL"


def should_include(path: Path) -> bool:
    if path.suffix not in INCLUDE_EXTS:
        return False
    parts = set(path.parts)
    if parts & EXCLUDE_DIRS:
        return False
    return True


def iter_files(root: Path):
    if root.is_file():
        if should_include(root):
            yield root
        return
    if not root.exists():
        return
    for p in root.rglob("*"):
        if p.is_file() and should_include(p):
            yield p


def scan_file(path: Path) -> FileFinding:
    finding = FileFinding(path=path)
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        finding.sample_lines.append((0, f"<read error: {exc}>"))
        return finding

    for line_num, line in enumerate(text.splitlines(), start=1):
        line_hit = False
        for cat, pattern in PATTERNS.items():
            matches = pattern.findall(line)
            if matches:
                finding.by_category[cat] += len(matches)
                finding.total_hits += len(matches)
                line_hit = True
        if line_hit and len(finding.sample_lines) < 3:
            snippet = line.strip()[:140]
            finding.sample_lines.append((line_num, snippet))
    return finding


def classify_layer(path: Path, finding: FileFinding) -> str:
    """Map a file to its Starter Kit layer based on path + hits."""
    s = str(path)
    if "/templates/" in s:
        return "L1-template"
    if "/skills/" in s:
        return "L2-skill"
    if "/commands/" in s:
        return "L2-command"
    if "/agents/" in s:
        return "L3-agent"
    if "/execution/" in s or "/scripts/" in s:
        return "L1-script"
    if "/hooks/" in s:
        return "L1-hook"
    if "/context/" in s or "/config/" in s:
        return "L1-context"
    if "/02. Areas/" in s:
        if "personal/frameworks/" in s:
            return "L5-framework-filled"
        if "diario/" in s:
            return "L5-journal"
        return "L5-context-file"
    if path.name == "CLAUDE.md":
        return "L1-meta"
    return "other"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    findings: list[FileFinding] = []
    for root in ROOT_PATHS:
        for path in iter_files(root):
            findings.append(scan_file(path))

    findings.sort(key=lambda f: (-f.total_hits, str(f.path)))

    csv_path = OUTPUT_DIR / "findings.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        writer.writerow([
            "path", "category", "layer", "total_hits",
            "jorge", "business_360", "revolutia", "monk",
            "people", "clients_360", "notion_ids",
            "hardcoded_paths", "cal_com", "personal_email",
        ])
        for f in findings:
            writer.writerow([
                str(f.path),
                f.category,
                classify_layer(f.path, f),
                f.total_hits,
                f.by_category.get("jorge", 0),
                f.by_category.get("business_360", 0),
                f.by_category.get("revolutia", 0),
                f.by_category.get("monk", 0),
                f.by_category.get("people", 0),
                f.by_category.get("clients_360", 0),
                f.by_category.get("notion_ids", 0),
                f.by_category.get("hardcoded_paths", 0),
                f.by_category.get("cal_com", 0),
                f.by_category.get("personal_email", 0),
            ])

    counts = defaultdict(int)
    by_layer = defaultdict(lambda: defaultdict(int))
    for f in findings:
        counts[f.category] += 1
        by_layer[classify_layer(f.path, f)][f.category] += 1

    md_path = OUTPUT_DIR / "report.md"
    with md_path.open("w", encoding="utf-8") as fp:
        fp.write("# Audit Report — Esbirrillo OS extraction\n\n")
        fp.write(f"Total files scanned: **{len(findings)}**\n\n")
        fp.write("## Summary by category\n\n")
        fp.write("| Category | Count | Action |\n")
        fp.write("|---|---|---|\n")
        fp.write(f"| CLEAN | {counts['CLEAN']} | Drop into kit as-is |\n")
        fp.write(f"| NEEDS_CLEANUP | {counts['NEEDS_CLEANUP']} | Parametrize and include |\n")
        fp.write(f"| PERSONAL | {counts['PERSONAL']} | Exclude or rewrite from scratch |\n\n")

        fp.write("## Summary by layer\n\n")
        fp.write("| Layer | CLEAN | NEEDS_CLEANUP | PERSONAL | Total |\n")
        fp.write("|---|---|---|---|---|\n")
        for layer in sorted(by_layer.keys()):
            row = by_layer[layer]
            total = row["CLEAN"] + row["NEEDS_CLEANUP"] + row["PERSONAL"]
            fp.write(f"| {layer} | {row['CLEAN']} | {row['NEEDS_CLEANUP']} | {row['PERSONAL']} | {total} |\n")
        fp.write("\n")

        fp.write("## Top 30 most personal files (highest hit count)\n\n")
        fp.write("| File | Layer | Hits | Top categories |\n")
        fp.write("|---|---|---|---|\n")
        for f in findings[:30]:
            top_cats = sorted(f.by_category.items(), key=lambda kv: -kv[1])[:3]
            cats_str = ", ".join(f"{k}({v})" for k, v in top_cats)
            rel = str(f.path).replace("/Users/jorgeguamis/Desktop/", "")
            fp.write(f"| `{rel}` | {classify_layer(f.path, f)} | {f.total_hits} | {cats_str} |\n")
        fp.write("\n")

        fp.write("## CLEAN files (drop in as-is) by layer\n\n")
        clean_by_layer = defaultdict(list)
        for f in findings:
            if f.category == "CLEAN":
                clean_by_layer[classify_layer(f.path, f)].append(f)
        for layer in sorted(clean_by_layer.keys()):
            files = clean_by_layer[layer]
            fp.write(f"### {layer} ({len(files)} files)\n\n")
            for f in files[:50]:
                rel = str(f.path).replace("/Users/jorgeguamis/Desktop/", "")
                fp.write(f"- `{rel}`\n")
            if len(files) > 50:
                fp.write(f"- … and {len(files) - 50} more\n")
            fp.write("\n")

        fp.write("## NEEDS_CLEANUP files (parametrize)\n\n")
        fp.write("| File | Layer | Hits | Sample line |\n")
        fp.write("|---|---|---|---|\n")
        cleanup_files = [f for f in findings if f.category == "NEEDS_CLEANUP"]
        for f in cleanup_files:
            rel = str(f.path).replace("/Users/jorgeguamis/Desktop/", "")
            sample = ""
            if f.sample_lines:
                ln, txt = f.sample_lines[0]
                sample = f"L{ln}: {txt}".replace("|", "\\|")[:80]
            fp.write(f"| `{rel}` | {classify_layer(f.path, f)} | {f.total_hits} | {sample} |\n")
        fp.write("\n")

    print(f"Scanned: {len(findings)} files")
    print(f"  CLEAN:         {counts['CLEAN']}")
    print(f"  NEEDS_CLEANUP: {counts['NEEDS_CLEANUP']}")
    print(f"  PERSONAL:      {counts['PERSONAL']}")
    print(f"\nReport: {md_path}")
    print(f"CSV:    {csv_path}")


if __name__ == "__main__":
    sys.exit(main())
