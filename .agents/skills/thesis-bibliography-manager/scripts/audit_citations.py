#!/usr/bin/env python3
r"""
Audits thesis citation keys:
1. Extracts all \cite{key1, key2} from chapters/*.tex and thesis_full_toc_persian_v3.tex.
2. Extracts all @type{key, from References.bib and MyReferences.bib.
3. Reports unresolved citations (missing keys) and unused bibliography entries.
"""

import sys
import re
from pathlib import Path

def parse_bib_keys(bib_path: Path):
    if not bib_path.exists():
        return set()
    with open(bib_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    # Match @article{key, @inproceedings{key, etc.
    keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", content))
    return keys

def extract_tex_cites(tex_path: Path):
    if not tex_path.exists():
        return []
    with open(tex_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Strip comments
    lines = [re.sub(r"(?<!\\)%.*$", "", l) for l in content.splitlines()]
    clean_text = "\n".join(lines)

    # Match \cite{key1, key2}
    raw_cites = re.findall(r"\\cite[^{]*\{([^}]+)\}", clean_text)
    keys = []
    for rc in raw_cites:
        for k in rc.split(","):
            k_clean = k.strip()
            if k_clean:
                keys.append(k_clean)
    return keys

def main():
    root_dir = Path("e:/projects/thesis")
    ref_bib = root_dir / "References.bib"
    myref_bib = root_dir / "MyReferences.bib"

    bib_keys = parse_bib_keys(ref_bib) | parse_bib_keys(myref_bib)
    print(f"Loaded {len(bib_keys)} BibTeX keys from References.bib and MyReferences.bib.")

    tex_files = sorted(list(root_dir.glob("chapters/*.tex")) + [root_dir / "thesis_full_toc_persian_v3.tex"])

    used_keys = set()
    missing_cites = {}

    for tf in tex_files:
        cites = extract_tex_cites(tf)
        for c in cites:
            used_keys.add(c)
            if c not in bib_keys:
                missing_cites.setdefault(tf.name, set()).add(c)

    print(f"Found {len(used_keys)} unique citation keys in LaTeX sources.")

    errors = 0
    if missing_cites:
        print("\n[X] UNRESOLVED CITATION KEYS DETECTED:")
        for fname, keys in missing_cites.items():
            print(f"  File `{fname}`: {len(keys)} missing key(s):")
            for k in sorted(keys):
                print(f"    - {k}")
            errors += len(keys)
    else:
        print("\n[PASS] All citation keys resolve cleanly against BibTeX repositories (0 missing citations)!")

    orphaned = bib_keys - used_keys
    print(f"\n[INFO] {len(orphaned)} bibliography entries exist in .bib that are currently uncited in text.")

    return 1 if errors > 0 else 0

if __name__ == "__main__":
    sys.exit(main())
