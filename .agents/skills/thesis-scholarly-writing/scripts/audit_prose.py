#!/usr/bin/env python3
"""
Audits thesis LaTeX source files for:
1. Conversational throat-clearing / filler phrases
2. AI hype words and banned promotional rhetoric
3. Excessive itemize/enumerate usage (anti-bullet fatigue)
"""

import sys
import re
from pathlib import Path

FILLERS = [
    (r"شایان ذکر است که", "شایان ذکر است که (Banned filler)"),
    (r"لازم به یادآوری است که", "لازم به یادآوری است که (Banned filler)"),
    (r"بدیهی است که", "بدیهی است که (Banned filler)"),
    (r"همان‌طور که می‌دانیم", "همان‌طور که می‌دانیم (Banned filler)"),
    (r"نکته جالب توجه این است که", "نکته جالب توجه این است که (Banned filler)"),
    (r"باید اشاره کرد که", "باید اشاره کرد که (Banned filler)"),
    (r"جای تأمل دارد که", "جای تأمل دارد که (Banned filler)"),
]

HYPE_WORDS = [
    (r"\bنوین\b", "نوین (Banned; use پیشنهادی / مدرن / پیشرفته / جدید)"),
    (r"\bانقلابی\b", "انقلابی (Banned hype word)"),
    (r"\bشگفت‌انگیز\b", "شگفت‌انگیز (Banned hype word)"),
    (r"\bدگرگون‌ساز\b", "دگرگون‌ساز (Banned hype word)"),
    (r"\bچشمگیر\b", "چشمگیر (Banned; report quantitative delta)"),
    (r"\bفوق‌العاده\b", "فوق‌العاده (Banned hype intensifier)"),
    (r"\bفوق‌سریع\b", "فوق‌سریع (Banned; use زیر میلی‌ثانیه‌ای / بلادرنگ)"),
]

def audit_file(file_path: Path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    issues = []
    itemize_count = 0
    enumerate_count = 0

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("%"):
            continue

        clean_line = re.sub(r"(?<!\\)%.*$", "", line)

        # Check fillers
        for p, desc in FILLERS:
            if re.search(p, clean_line):
                issues.append((idx, "Filler Phrase", desc))

        # Check hype words
        for p, desc in HYPE_WORDS:
            if re.search(p, clean_line):
                issues.append((idx, "Hype Word", desc))

        if r"\begin{itemize}" in clean_line:
            itemize_count += 1
        if r"\begin{enumerate}" in clean_line:
            enumerate_count += 1

    return issues, itemize_count, enumerate_count

def main():
    root_dir = Path("e:/projects/thesis")
    tex_files = sorted(list(root_dir.glob("chapters/*.tex")) + [root_dir / "thesis_full_toc_persian_v3.tex"])

    total_issues = 0
    print("=" * 70)
    print(" " * 15 + "SCHOLARLY PROSE & HYPE AUDIT REPORT")
    print("=" * 70)

    for f in tex_files:
        if not f.exists():
            continue
        issues, item_cnt, enum_cnt = audit_file(f)
        if issues or item_cnt > 2:
            print(f"\n[!] {f.name}: {len(issues)} stylistic issue(s) | {item_cnt} itemize, {enum_cnt} enumerate")
            for line_idx, kind, desc in issues:
                print(f"  Line {line_idx}: [{kind}] {desc}")
            total_issues += len(issues)
        else:
            print(f"[PASS] {f.name}: Clean (0 style violations, {item_cnt} itemize, {enum_cnt} enumerate)")

    print("\n" + "=" * 70)
    print(f"TOTAL STYLE VIOLATIONS: {total_issues}")
    print("=" * 70)

    return 1 if total_issues > 0 else 0

if __name__ == "__main__":
    sys.exit(main())

