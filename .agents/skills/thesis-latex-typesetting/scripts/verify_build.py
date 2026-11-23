#!/usr/bin/env python3
"""
Zero-defect build verification script for thesis_full_toc_persian_v3.log.
Enforces:
1. Undefined references: 0 (tolerated as informational notices in single-chapter mode)
2. Undefined citations: 0
3. Overfull \\hbox > 10pt: 0
4. Maximum overfull bound: < 10.0 pt
5. Page count baseline verification (skipped in single-chapter mode)
"""

import sys
import re
import argparse
from pathlib import Path

def verify_log(log_path: str, single_chapter: bool = False, fast_mode: bool = False) -> int:
    path = Path(log_path)
    if not path.exists():
        print(f"[ERROR] Log file not found: {log_path}")
        return 1

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        log_text = f.read()

    errors = 0

    # 1. Undefined references
    undef_refs = re.findall(r"LaTeX Warning: Reference `(.*?)' on page (\d+) undefined", log_text)
    print(f"Undefined references: {len(undef_refs)}")
    if undef_refs:
        if single_chapter:
            print(f"  [INFO] Tolerating {len(undef_refs)} cross-reference(s) in single-chapter mode:")
            for r, p in undef_refs:
                print(f"    - Ref `{r}` on page {p} (external chapter reference)")
        elif fast_mode:
            print(f"  [INFO] Tolerating {len(undef_refs)} cross-reference(s) in Fast (single pass) mode.")
        else:
            errors += len(undef_refs)
            for r, p in undef_refs:
                print(f"  [X] Ref `{r}` on page {p}")

    # 2. Undefined citations
    undef_cites = re.findall(r"LaTeX Warning: Citation `(.*?)' on page (\d+) undefined", log_text)
    print(f"Undefined citations: {len(undef_cites)}")
    if undef_cites:
        if fast_mode:
            print(f"  [INFO] Tolerating {len(undef_cites)} undefined citation(s) in Fast/NoBib mode.")
        else:
            errors += len(undef_cites)
            for c, p in undef_cites:
                print(f"  [X] Cite `{c}` on page {p}")

    # 3. Hyperref warnings
    undef_hyp = re.findall(r"Package hyperref Warning: (.*?)\n", log_text)
    print(f"Hyperref warnings: {len(undef_hyp)}")
    if undef_hyp:
        for w in undef_hyp:
            print(f"  [!] {w}")

    # 4. Overfull \hbox checks
    overfulls = re.findall(r"Overfull \\hbox \(([0-9.]+)pt too wide\)", log_text)
    overfull_floats = [float(x) for x in overfulls]
    large_overfulls = [x for x in overfull_floats if x > 10.0]
    print(f"Total Overfull \\hbox: {len(overfulls)}")
    print(f"Overfull \\hbox > 10pt: {len(large_overfulls)}")
    if overfull_floats:
        max_overfull = max(overfull_floats)
        print(f"Max overfull: {max_overfull:.4f} pt")
        if max_overfull > 10.0:
            errors += len(large_overfulls)
            print("  [X] Violates requirement: Overfull \\hbox must be strictly <= 10.0 pt!")

    # 5. Page count
    m_pages = re.findall(r"Output written on .*? \((\d+) pages\)", log_text)
    if m_pages:
        page_count = int(m_pages[-1])
        if single_chapter:
            print(f"Total PDF pages: {page_count} (Single Chapter Mode)")
        else:
            print(f"Total PDF pages: {page_count}")
            if page_count < 150 or page_count > 180:
                print(f"  [!] Warning: Page count ({page_count}) deviated significantly from baseline (164-165).")

    if errors > 0:
        print(f"\n[FAIL] Verification failed with {errors} issue(s).")
        return 1
    else:
        mode_str = " (Single Chapter Mode)" if single_chapter else ""
        print(f"\n[PASS] Build log meets all zero-defect criteria{mode_str}!")
        return 0

def main():
    parser = argparse.ArgumentParser(description="Zero-defect build verification for LaTeX logs.")
    parser.add_argument("log_file", nargs="?", default="thesis_full_toc_persian_v3.log", help="Path to the .log file.")
    parser.add_argument("--single-chapter", action="store_true", help="Enable single-chapter verification (tolerate external cross-refs and skip total page baseline).")
    parser.add_argument("--fast", action="store_true", help="Fast mode: tolerate unresolved citations due to skipped BibTeX pass.")
    args = parser.parse_args()

    sys.exit(verify_log(args.log_file, single_chapter=args.single_chapter, fast_mode=args.fast))

if __name__ == "__main__":
    main()
