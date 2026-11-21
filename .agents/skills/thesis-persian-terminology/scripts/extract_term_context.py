#!/usr/bin/env python3
"""
Fast Context Extraction Tool for Persian Academic Terminology Analysis.
Uses ripgrep (rg) with fallback to native Python regex to search LaTeX files
and format surrounding lines into clean markdown tables for academic evaluation.
"""

import sys
import os
import argparse
import subprocess
import re
from pathlib import Path

def search_with_ripgrep(term: str, target_dir: Path, context_lines: int = 2):
    """Executes ripgrep if available and parses results."""
    cmd = [
        "rg",
        "-n",
        "-C", str(context_lines),
        "--heading",
        term,
        str(target_dir / "chapters"),
        str(target_dir / "thesis_full_toc_persian_v3.tex")
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        return proc.stdout
    except Exception:
        return None

def search_with_python(term: str, target_dir: Path, context_lines: int = 2):
    """Fallback search using native python regex."""
    files = sorted(list((target_dir / "chapters").glob("*.tex")) + [target_dir / "thesis_full_toc_persian_v3.tex"])
    pattern = re.compile(re.escape(term))
    results = []

    for f in files:
        if not f.exists():
            continue
        try:
            lines = f.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            continue

        file_matches = []
        for idx, line in enumerate(lines, start=1):
            if pattern.search(line):
                start = max(0, idx - 1 - context_lines)
                end = min(len(lines), idx + context_lines)
                snippet = " ... ".join([lines[i].strip() for i in range(start, end) if lines[i].strip()])
                file_matches.append((idx, snippet))

        if file_matches:
            results.append((f.name, file_matches))
    return results

def main():
    parser = argparse.ArgumentParser(description="Extract term occurrences and context from thesis files.")
    parser.add_argument("--term", "-t", required=True, help="Persian or Latin term to search for (e.g. 'سنتز')")
    parser.add_argument("--context", "-c", type=int, default=2, help="Number of context lines before and after match")
    parser.add_argument("--dir", "-d", default="e:/projects/thesis", help="Workspace root directory")
    args = parser.parse_args()

    root = Path(args.dir)
    print(f"# Terminology Context Audit: «{args.term}»\n")

    # Try ripgrep first
    rg_output = search_with_ripgrep(args.term, root, args.context)
    if rg_output and rg_output.strip():
        print("```text")
        print(rg_output.strip())
        print("```\n")

    # Format structured table
    matches_data = search_with_python(args.term, root, args.context)
    total_occurrences = sum(len(matches) for _, matches in matches_data)

    print(f"**Total Occurrences Found**: {total_occurrences} across {len(matches_data)} files.\n")
    print("| File | Line | Surrounding Context Snippet | Academic Evaluation |")
    print("| :--- | :--- | :--- | :--- |")

    for fname, matches in matches_data:
        for line_num, snippet in matches:
            clean_snippet = snippet.replace("|", "\\|")
            if len(clean_snippet) > 160:
                clean_snippet = clean_snippet[:157] + "..."
            print(f"| `{fname}` | {line_num} | {clean_snippet} | *Pending Evaluation* |")

if __name__ == "__main__":
    main()
