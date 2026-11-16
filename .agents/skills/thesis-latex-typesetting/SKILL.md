---
name: thesis-latex-typesetting
description: >-
  Zero-defect XeLaTeX and XePersian typesetting, BiDi layout enforcement, math-mode numeral formatting, and build verification for the doctoral dissertation. Use when compiling, checking compilation logs, fixing overfull hboxes, or typesetting mixed Persian-Latin equations, numbers, and cross-references.
---

# XeLaTeX & XePersian Typesetting Skill

This skill enforces zero-defect typesetting disciplines for the doctoral dissertation (`thesis_full_toc_persian_v3.tex`) under XeLaTeX and XePersian.

## Typesetting Disciplines

### 1. BiDi Math-Mode for Numerals & Units
Under XePersian's TeX--XeT engine, bare Persian numbers containing slashes (`/`), decimals, thousands commas, decibels, or latencies reverse digit/segment order.
- Always typeset decimals, fractions, thousands, and latency/decibel metrics in math mode with a thin space `\,` before units:
  - `$70.5\%$` (never bare `۷۰/۵٪`)
  - `$137/200$` (never bare `۱۳۷/۲۰۰`)
  - `$2{,}000$` (never bare `۲،۰۰۰`)
  - `$0.485\,\text{ms}$` or `$200\,\text{ms}$`
  - `$-40\,\text{dB}$` or `$+15\,\text{dB}$`
- Check files with `python .agents/skills/thesis-latex-typesetting/scripts/audit_bidi_numbers.py`.

### 2. Heading Safety with `\texorpdfstring`
Wrap math expressions, custom algorithm macros (`\rsdrlplus`, `\sgos`, etc.), or Latin identifiers in headings:
```latex
\section{تحلیل حساسیت پارامتر \texorpdfstring{$\rho$}{rho} در همگرایی}
```

### 3. Strict Cross-Reference Rule
- **NEVER** wrap cross-references in `\lr{...}` (e.g. ❌ `\lr{\ref{fig:...}}`).
- Wrapping `\ref` in `\lr{...}` deactivates `\AutoPersianDigits` and forces Latin digits (`4-5`).
- Cross-references must remain bare: `شکل \ref{fig:...}`, `جدول \ref{tab:...}`, `بخش \ref{sec:...}`.

### 4. Table Width & Margin Overflow Prevention
- Tables must never overflow text margins.
- Always use bounded column widths:
  ```latex
  \begin{tabular}{|p{2.5cm}|p{6.0cm}|p{5.1cm}|}
  ```
- Use `\small` or `\footnotesize` inside tables.

### 5. Footnote Conventions
- Move non-acronym English equivalents to `\LTRfootnote{...}` on **first mention per chapter**.
- Never place `\LTRfootnote` inside `\section`, `\caption`, `\paragraph`, or `tabular`.

---

## Build Verification Runbook

After any compilation, execute:
```powershell
python .agents/skills/thesis-latex-typesetting/scripts/verify_build.py thesis_full_toc_persian_v3.log
```

The build is acceptable ONLY if:
1. `Undefined references: 0`
2. `Undefined citations: 0`
3. `Hyperref warnings: 0`
4. `Overfull \hbox > 10pt: 0` (max overfull strictly $< 10\,\text{pt}$)
5. `Total PDF pages: 164-165`

### Mandatory Post-Verification Cleanup
Immediately after verifying the log, execute the cleanup protocol (	hesis-build-cleanup):
`powershell
python .agents/skills/thesis-build-cleanup/scripts/clean_build.py
`
