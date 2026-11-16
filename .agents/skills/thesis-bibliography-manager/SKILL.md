---
name: thesis-bibliography-manager
description: >-
  Audits, verifies, and formats BibTeX citations and bibliographic entries for the doctoral dissertation. Use when checking for undefined citations, adding new references to References.bib or MyReferences.bib, verifying IEEE-FA formatting, or managing footnote conventions (\LTRfootnote).
---

# Bibliography & Citation Management Skill

This skill manages bibliographic references and citations across `thesis_full_toc_persian_v3.tex`, `chapters/*.tex`, and the dual BibTeX repositories (`References.bib` and `MyReferences.bib`).

## Citation Rules & Guidelines

### 1. Dual BibTeX Structure
- **`MyReferences.bib`**: Contains the author's published and submitted papers (ACM, IEEE, etc.).
- **`References.bib`**: Contains all external literature, baseline papers, and foundational works.
- Both files are compiled using `ieeetr-fa` style:
  ```latex
  \bibliographystyle{ieeetr-fa}
  \bibliography{References,MyReferences}
  ```

### 2. In-Text Citation Formatting
- Citations in Persian text render with Persian digits: `[۲]`.
- **NEVER** wrap `\cite` in `\lr{\cite{...}}`. Keep it bare: `مطابق با پژوهش پیشین \cite{...}`.
- Every citation key used in any `.tex` file must resolve to a valid BibTeX entry with 0 undefined citation warnings.

### 3. Footnote Conventions
- **Prose Non-Acronym English Terms**: Move English equivalents to `\LTRfootnote{...}` on **first mention per chapter**. Omit duplicate parentheticals within the same chapter.
- **Active Uppercase Acronyms**: Reused uppercase acronyms keep `(\lr{ACRONYM})\LTRfootnote{Full Expansion}` on first chapter mention; strip redundant parentheticals on later mentions in that chapter.
- **Foreign Author Names**: Place `\LTRfootnote{First Last [et al.]}` on first mention.
- **Tool URLs**: Use `\footnote{<Short Persian label>: \lr{\url{...}}}` on first mention.
- **Strict Prohibition**: Never place `\LTRfootnote` inside `\section`, `\subsection`, `\subsubsection`, `\paragraph`, `\caption`, or `tabular`.

---

## Automated Citation Audit Runbook

To scan all `.tex` files for unresolved `\cite{...}` keys or orphaned BibTeX entries:
```powershell
python .agents/skills/thesis-bibliography-manager/scripts/audit_citations.py
```

