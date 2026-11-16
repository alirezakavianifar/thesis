#!/usr/bin/env python3
"""
Audits LaTeX files for bare Persian/Arabic numerals or decimals outside math mode
that may flip or corrupt in XePersian RTL output.
"""

import re
import sys
from pathlib import Path

# Persian/Arabic digits: ۰۱۲۳۴۵۶۷۸۹
PERSIAN_DIGITS = r"[\u06F0-\u06F9]"

# Patterns that indicate risky numbers outside math mode:
# 1. Bare decimal numbers: e.g. ۷۰/۵ or ۷۰٫۵
BARE_DECIMAL = re.compile(rf"{PERSIAN_DIGITS}+[/.،٫]{PERSIAN_DIGITS}+")
# 2. Bare units attached: e.g. \lr{0.1ms} or bare numbers before ms/dB
BARE_UNIT_LR = re.compile(r"\\lr\{\s*[0-9.]+\s*(ms|dB|%|s)\s*\}")
# 3. Wrapped ref in lr: \lr{\ref{...}}
WRAPPED_REF = re.compile(r"\\lr\{\s*\\ref\{[^}]+\}\s*\}")

def audit_file(file_path: Path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    issues = []
    for line_idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("%"):
            continue

        # Check for \lr{\ref{...}}
        for m in WRAPPED_REF.finditer(line):
            issues.append((line_idx, "Wrapped \\ref in \\lr{...}", m.group(0), "Use bare \\ref instead"))

        # Check for bare units like \lr{0.1ms}
        for m in BARE_UNIT_LR.finditer(line):
            issues.append((line_idx, "Bare unit in \\lr{...}", m.group(0), "Use math mode: $0.1\\,\\text{ms}$"))

        # Check for bare Persian decimals (strip math mode first)
        line_no_math = re.sub(r"\$[^$]+\$", "", line)
        for m in BARE_DECIMAL.finditer(line_no_math):
            issues.append((line_idx, "Bare Persian decimal/fraction", m.group(0), "Use math mode: e.g. $70.5\\%$"))

    return issues

def main():
    thesis_dir = Path("e:/projects/thesis")
    tex_files = list(thesis_dir.glob("chapters/*.tex")) + [thesis_dir / "thesis_full_toc_persian_v3.tex"]
    
    total_issues = 0
    for f in tex_files:
        if not f.exists():
            continue
        issues = audit_file(f)
        if issues:
            print(f"\n[!] {f.name}: {len(issues)} issue(s)")
            for line_idx, kind, match, fix in issues:
                print(f"  Line {line_idx}: [{kind}] `{match}` -> {fix}")
            total_issues += len(issues)
        else:
            print(f"[OK] {f.name}: Clean (0 BiDi number issues)")

    print(f"\nTotal BiDi numeral issues found: {total_issues}")
    return 1 if total_issues > 0 else 0

if __name__ == "__main__":
    sys.exit(main())

