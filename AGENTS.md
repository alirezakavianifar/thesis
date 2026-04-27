# Agent Instructions

## Git Remote

Changes must be pushed to: 

**https://github.com/alirezakavianifar/thesis.git**

Ensure the remote `origin` points to this URL. If not configured, use: `git remote add origin https://github.com/alirezakavianifar/thesis.git` (or `git remote set-url origin <url>` to update).

## .gitignore and Large Files

If `.gitignore` does not exist, create one based on the codebase structure and language. Adapt entries to match the project's technologies and build output locations.

**CRITICAL: File Size Limits**
GitHub has a strict 100MB file size limit. **NEVER** commit large binaries, archives (`.rar`, `.zip`, `.jar`), high-resolution images, or compiled outputs (like large `.pdf` files) to the repository. 
- Always ensure such files are included in `.gitignore` **before** running `git add .`.

## Git Push Workflow and Troubleshooting

When the user uses the keyword "push" in a request (e.g., "please push these changes", "push", or similar), you MUST follow this specific workflow:

1. **Check for Large Files**: Ensure no accidentally generated large files (e.g., binaries, archives, compiled PDFs) are about to be staged. Update `.gitignore` if necessary.
2. **Stage all changes**: standard `git add .`
3. **Infer Commit Message**: Generate a concise, descriptive, and professional commit message based on the recent file changes and conversation context. Do not ask the user for a commit message unless they explicitly provide one.
4. **Commit**: `git commit -m "<inferred_message>"`
5. **Push**: `git push` (or `git push -u origin <branch>` if the upstream is not set).

**Note:** You should proactively execute these commands without asking for extra confirmation if the user explicitly said "push".

**Troubleshooting `pre-receive hook declined` (Large File in History):**
If a push fails because a large file exceeds GitHub's limits, it means the file is in the *commit history*, even if you subsequently added it to `.gitignore` or used `git rm --cached`. To resolve this:
1. Identify the last clean remote commit (e.g., `git log origin/master`).
2. Soft reset to undo local commits but keep working tree changes: `git reset --soft origin/master`
3. Ensure `.gitignore` is correctly updated to ignore the large files.
4. Unstage the large files or unstage everything and selectively restage ONLY source files.
5. Commit the clean state and push.
