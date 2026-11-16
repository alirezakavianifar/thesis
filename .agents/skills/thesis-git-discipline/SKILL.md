---
name: thesis-git-discipline
description: >-
  Automates Git version control, 100MB file limit enforcement, clean commit message inference, and safe pushing for the doctoral dissertation repository. Use whenever the user requests to push changes, or when handling git staging and pre-receive hook errors.
---

# Git Discipline & Safe Push Skill

This skill enforces safe version control and automated pushing to the remote GitHub repository:
**`https://github.com/alirezakavianifar/thesis.git`**

## Core Disciplines

### 1. Strict 100MB File Limit & `.gitignore` Guardian
GitHub strictly rejects pushes containing files $>100\,\text{MB}$.
- **NEVER** commit large binaries, compiled PDF outputs (`.pdf`), archives (`.zip`, `.rar`, `.tar`), or build logs (`.log`, `.xdv`, `.aux`).
- Ensure `.gitignore` ignores all generated artifacts before staging.
- The `safe_push.py` script automatically scans the working tree for files $>50\,\text{MB}$ before executing `git add .`.

### 2. Automated Push Workflow on Keyword "push"
When the user requests to "push" (or uses the keyword "push"), execute the automated pipeline:
```powershell
python .agents/skills/thesis-git-discipline/scripts/safe_push.py
```
The script will:
1. Scan for any files $>50\,\text{MB}$ and warn or abort if unignored.
2. Ensure `.gitignore` is comprehensive.
3. Stage changes (`git add .`).
4. Generate a concise, semantic commit message based on modified files.
5. Commit and push (`git push`).

### 3. Troubleshooting `pre-receive hook declined`
If a push is declined due to a large file in history:
1. Identify the last clean remote commit (`git log origin/master`).
2. Soft reset local commits: `git reset --soft origin/master`.
3. Update `.gitignore` to ignore the offending file.
4. Unstage large files: `git restore --staged <large_file>`.
5. Re-commit clean source files and push.

