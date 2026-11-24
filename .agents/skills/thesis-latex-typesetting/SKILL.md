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

### 6. Figure Resolution & Size Optimization Standards
To prevent multi-megabyte PDF bloat while maintaining pristine publication quality:
- **Vector PDF for Architecture & Workflow Diagrams**: Diagram generator scripts (`generate_*.py`) must output native `.pdf` vector graphics (`plt.savefig(..., bbox_inches='tight')`). Vector graphics scale infinitely (zero pixelation at 1000% zoom) and reduce diagram size by 80–88% compared to raster bitmaps.
- **Lossless PNG8 Quantization for Line/Scatter Plots**: Raster experimental plots (DeltaIoT, DARTSim) with discrete color lines must be stored in 256-color adaptive palette PNG8 with alpha channels stripped (`optimize_figures.py`), ensuring $PSNR \ge 40.0\,\text{dB}$ (visually lossless).
- **Print Resolution Bounding**: Avoid 700–900 DPI oversampling by bounding maximum raster width to 1800 px (~300 DPI across A4 `\textwidth`).
- **Figure Optimization Tool**: Execute `python .agents/skills/thesis-latex-typesetting/scripts/optimize_figures.py` to audit and optimize figures with automated backups in `figures/.originals/`.

---

## Mandatory Compilation Pipeline (`compile_thesis.ps1`)

> [!IMPORTANT]
> **Strict Compilation Rule**: Whenever compiling the LaTeX dissertation (`thesis_full_toc_persian_v3.tex`), **ALWAYS use the PowerShell script (`compile_thesis.ps1`)**. Do not run raw `xelatex` or `bibtex` commands directly in the terminal.

To execute the complete end-to-end build (XeLaTeX -> BibTeX -> XeLaTeX x2 -> Verification -> Cleanup) in one command:
```powershell
.\compile_thesis.ps1
```
By default, all chapters are compiled as part of the complete dissertation (`thesis_full_toc_persian_v3.tex`).

### Compiling a Specific Chapter
When you need to compile only an individual chapter:
```powershell
.\compile_thesis.ps1 -Chapter 4
.\compile_thesis.ps1 -Chapter 5 -Fast -Open
.\compile_thesis.ps1 -Chapter appendices
```
The script maps `-Chapter <N>` to `chapters/chapter<N>.tex`, outputs `chapter<N>.pdf`, automatically links cross-chapter references via `master_labels.aux` and `xr-hyper` (zero `؟؟` question marks), and synchronizes citation numbering via `master.bbl` and `sync_chapter_bib.py` so in-text citations (`[۲۸]`, `[۲۹]`, ...) and the chapter bibliography match the master dissertation numbering without restarting from `[۱]`.

Optional switches:
- `.\compile_thesis.ps1 -Chapter <N>`: Compiles only the specified chapter (`1` to `6`, or `appendices`).
- `.\compile_thesis.ps1 -Fast`: Quick single pass without BibTeX.
- `.\compile_thesis.ps1 -NoClean`: Retain build artifacts for debugging.
- `.\compile_thesis.ps1 -NoVerify`: Skip Python log verification.
- `.\compile_thesis.ps1 -Open`: Open PDF after compilation.

---

## Build Verification Runbook

After any manual compilation, execute:
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
