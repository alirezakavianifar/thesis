#!/usr/bin/env python3
"""
Automated safe push script for the thesis repository:
1. Scans for large files (>50MB) to prevent pre-receive hook rejections.
2. Checks git status.
3. Stages changes (git add .).
4. Commits with an inferred or provided commit message.
5. Pushes to remote.
"""

import sys
import subprocess
from pathlib import Path

MAX_FILE_BYTES = 50 * 1024 * 1024  # 50 MB threshold

def check_large_files(root: Path):
    oversized = []
    for p in root.rglob("*"):
        if ".git" in p.parts:
            continue
        if p.is_file():
            try:
                sz = p.stat().st_size
                if sz > MAX_FILE_BYTES:
                    oversized.append((p, sz))
            except Exception:
                pass
    return oversized

def run_git_cmd(args):
    res = subprocess.run(["git"] + args, capture_output=True, text=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def main():
    root = Path("e:/projects/thesis")
    print("[1/5] Scanning for oversized files (>50MB)...")
    oversized = check_large_files(root)
    if oversized:
        print("[ERROR] Found files exceeding size safety threshold:")
        for p, sz in oversized:
            print(f"  - {p.relative_to(root)}: {sz / (1024*1024):.2f} MB")
        print("Please add these to .gitignore or remove them before pushing!")
        return 1

    print("[2/5] Checking repository status...")
    code, status_out, _ = run_git_cmd(["status", "--porcelain"])
    if not status_out:
        print("[INFO] Working tree clean, nothing to commit.")
        return 0

    print("[3/5] Staging changes (git add .)...")
    code, _, err = run_git_cmd(["add", "."])
    if code != 0:
        print(f"[ERROR] git add failed: {err}")
        return 1

    msg = sys.argv[1] if len(sys.argv) > 1 else "docs(thesis): update dissertation sources and workspace skills"
    print(f"[4/5] Committing changes with message: '{msg}'...")
    code, cout, cerr = run_git_cmd(["commit", "-m", msg])
    if code != 0:
        print(f"[ERROR] git commit failed: {cerr or cout}")
        return 1
    print(cout)

    print("[5/5] Pushing to remote repository...")
    code, pout, perr = run_git_cmd(["push"])
    if code != 0:
        print(f"[ERROR] git push failed: {perr or pout}")
        return 1
    print(pout or perr)
    print("\n[SUCCESS] Successfully pushed all changes!")
    return 0

if __name__ == "__main__":
    sys.exit(main())

