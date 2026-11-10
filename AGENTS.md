# Agent Instructions & Dissertation Scholarly Guidelines

This document serves as the permanent, authoritative instruction manual for all AI agents, subagents, and automated workflows operating on this doctoral dissertation repository. All future edits across all chapters, abstracts, appendices, and front matter MUST strictly adhere to the guidelines, vocabularies, architectural conventions, and LaTeX disciplines codified herein.

> [!IMPORTANT]
> **Living Document & Dynamic Rule Maintenance Protocol**:
> This document is a living specification. From now on, whenever the author introduces a new rule, refines a technical term, bans a word, specifies a stylistic constraint, or modifies a workflow during conversation turns, the AI agent **MUST proactively and immediately update `AGENTS.md`** to record and persist the new guideline. No author preference or rule should remain solely in ephemeral conversation memory.

---

## 1. Git Remote & Automated Push Workflow

### 1.1 Remote Repository Configuration
Changes must be pushed to:
**https://github.com/alirezakavianifar/thesis.git**

Ensure the remote `origin` points to this URL. If not configured, use:
```powershell
git remote add origin https://github.com/alirezakavianifar/thesis.git
```
(or `git remote set-url origin https://github.com/alirezakavianifar/thesis.git` to update).

### 1.2 Strict File Size Limits & `.gitignore` Discipline
GitHub enforces a strict 100MB file size limit. **NEVER** commit large binaries, archives (`.rar`, `.zip`, `.jar`), high-resolution media, or compiled outputs (like large `.pdf` files) to the repository.
- Always ensure generated artifacts, build dumps, and large PDFs are properly ignored in `.gitignore` **before** staging changes.

### 1.3 Automated Push Protocol on the Keyword "push"
When the user uses the keyword **"push"** in a request (e.g., "please push these changes", "push", or similar), you **MUST proactively execute** the following workflow without asking for extra confirmation:
1. **Check for Large Files**: Ensure no large files (> 100MB) are accidentally staged. Update `.gitignore` if necessary.
2. **Stage all changes**: `git add .`
3. **Infer Commit Message**: Generate a concise, descriptive, and professional commit message based on recent file modifications and conversation context. Do not prompt the user for a commit message unless they explicitly provide one.
4. **Commit**: `git commit -m "<inferred_message>"`
5. **Push**: `git push` (or `git push -u origin <branch>` if upstream is not set).

### 1.4 Troubleshooting `pre-receive hook declined` (Large File in History)
If a push fails because a large file exceeds GitHub's limits, it is trapped in the *commit history*. To resolve:
1. Identify the last clean remote commit (e.g., `git log origin/master`).
2. Soft reset local commits while preserving working tree changes: `git reset --soft origin/master`
3. Update `.gitignore` to ignore large files.
4. Unstage large files or restage only source `.tex`, `.bib`, `.cls`, `.sty`, and essential scripts.
5. Commit the clean state and push.

---

## 2. Scholarly Tone, Humanization & AI Pattern Elimination

### 2.1 Reader-Centricity & Cognitive Flow
- Always evaluate modified prose from the perspective of a newcomer or a rigorous external doctoral examiner.
- If a sentence is long, convoluted, breathy, or causes excessive cognitive load, break it down into clean, balanced declarative clauses.
- Use natural sentence cadence and authoritative academic Persian.

### 2.2 Complete Ban on AI Hype Words & Promotional Adjectives
Scholarly authority stems from mathematical proof and empirical benchmarks, never from promotional rhetoric.
- ❌ **Strictly Banned Hype Words**:
  - `نوین` (novel / modern)
  - `انقلابی` (revolutionary)
  - `شگفت‌انگیز` (astonishing)
  - `دگرگون‌ساز` (transformative)
  - `چشمگیر` (dramatic / impressive)
  - `فوق‌العاده` (extraordinary)
- ✔️ **Approved Scholarly Equivalents**:
  - `پیشنهادی` (proposed)
  - `توسعه‌یافته` (developed)
  - `سنجیده‌شده` (evaluated)
  - `اثبات‌شده` (proven)
  - `موثر` (effective)

### 2.3 Elimination of the Casual Prefix «فوق»
- ❌ **Banned**: Informal intensifiers such as `فوق‌سریع` or `فوق‌العاده`.
- ✔️ **Approved**: State the quantitative metric directly (e.g., `در زمان استنتاج زیر نیم میلی‌ثانیه` or `با کمترین تأخیر محاسباتی`).

### 2.4 Elimination of Rhetorical Padding & Conversational Fillers
Strip away empty transitions and conversational throat-clearing:
- ❌ **Banned Fillers**:
  - `شایان ذکر است که`
  - `لازم به یادآوری است که`
  - `بدیهی است که`
  - `همان‌طور که می‌دانیم`
  - `نکته جالب توجه این است که`
- ✔️ **Approved**: Direct, assertive declarative sentences.

### 2.5 Elimination of Redundant Adjectives & Pseudo-Philosophical Calques
- ❌ Avoid adding `استاندارد` casually (e.g. `یادگیری تقویتی عمیق استاندارد` $\rightarrow$ `یادگیری تقویتی عمیق`) unless contrasting directly with a modified variant.
- ❌ Avoid opaque, pseudo-philosophical calques such as `چرایی ناکارآمدی رویکردهای یکنواخت پیشین` (use `سنتی` or `تک‌سطحی`).
- ❌ Avoid awkward, unnatural translations like `تفکیک زمانی مسئولیت‌های کنترلی` or `سازماندهی فرایند یکپارچه خودوفقی برپایه خطوط شناور` (use standard software engineering expressions).

---

## 3. The Comprehensive Persian Terminological Dictionary

The following table defines the mandatory, standardized technical vocabulary across the entire dissertation. Any deviation is strictly prohibited.

| Concept | Mandatory Persian Term | Strictly Banned / Avoided | Specific Rule & Technical Rationale |
| :--- | :--- | :--- | :--- |
| **System** | **`سیستم`** | ❌ `سامانه` | Standardized 100% across the thesis (`سیستم‌های خودوفق`, `سیستم هدف`, `سیستم‌های فیزیکی-سایبری`). The word `سامانه` is completely purged. |
| **Real-Time** | **`بلادرنگ`** | ❌ `زمان‌حقیقی`<br>❌ `زمان واقعی`<br>❌ `بی‌درنگ` | Sole official Academy of Persian Language & Literature & IEEE-Iran term. Never use `زمان واقعی` or call Soft-QoS systems (DeltaIoT 8-min period) real-time. Never stack `آنلاین بلادرنگ`. |
| **Self-Adaptive Systems** | **`سیستم‌های خودوفق`** | ❌ `سیستم‌های خودتطبیق‌پذیر`<br>❌ `سامانه‌های خودسازگار` | Established academic compound in Iranian computer software engineering. |
| **Self-Adaptation (Capability)** | **`خودوفقی`** | ❌ `خودتطبیقی`<br>❌ `خودسازگاری` | Refers to the architectural property or capability of the system. |
| **Adaptation (Process / Space)** | **`انطباق`** | ❌ `تطبیق` (in this context) | Dynamic action, search, or execution: `فضای وفقی`, `گزینه‌های وفقی`, `اهداف وفقی`, `طرح‌های انطباق`. |
| **Conformance / Verification** | **`انطباق با مشخصه‌ها`** | ❌ `تطابق` | Conformance to formal specifications, SLAs, or contracts. |
| **Comparative Analysis** | **`تحلیل تطبیقی`** | ❌ `تحلیل انطباقی` | `تطبیق` is strictly reserved for comparative cross-evaluation. |
| **Context / Testbed** | **`بستر / زمینه`** | ❌ `بافتار` | `بافتار` is an awkward calque. Use `بستر` for testbeds (DeltaIoT, DARTSim) and `زمینه` for context. |
| **Asynchronous** | **`ناهمگام`** | ❌ `غیرهمگام` | Standard computer systems term for decoupled background operations. |
| **Thread** | **`ریسمان`** | ❌ `نخ` | `ریسمان کنترلی` for execution threads. |
| **Process / Workflow** | **`فرآیند`** | ❌ `پردازه` (unless OS process) | Used for dynamic workflows, MAPE-K phases, MDP processes (`فرآیند تصمیم‌گیری مارکوف`). |
| **Swimlanes** | **`خطوط شناوری`** | ❌ `خطوط شناور` | UML Activity Diagram swimlanes in Figure 4.2. |
| **Critical** | **`بحرانی` (Strictly Disciplined)** | ❌ Rhetorical intensifiers | **ONLY** permitted in formal technical terms: `مأموریت‌بحرانی`, `مسیر بحرانی`, `گره‌های بحرانی`, `آستانه‌ها/مرزهای بحرانی`. Never `مهلت بحرانی` (use `مهلت زمانی سخت پروازی`) or `چالش‌های بحرانی` (use `چالش‌های بنیادین`). |
| **Vital / Crucial** | **`کلیدی / بنیادین / تعیین‌کننده`** | ❌ `حیاتی` | `حیاتی` is completely banned due to journalistic exaggeration. |
| **Baseline Method** | **`روش پایه‌ای RS-DRL`** | ❌ `متد`, `الگوریتم کلی` | Foundational single-tier algorithmic formulation. |
| **Generalized Architecture** | **`معماری تعمیم‌یافته RS-DRL+`**| ❌ `روش تعمیم‌یافته` | Two-tier contract-anytime software architecture. |
| **Holistic Framework** | **`چارچوب`** | ❌ `فریم‌ورک` | The overarching theoretical and engineering construct. |
| **Architectural Patterns** | **`الگوهای معماری SG-OS و CAE-PV`** | ❌ `روش‌های SG-OS` | Software engineering design patterns. |
| **Distributed Systems** | **`شبکه‌های حسگر توزیع‌شده`** | ❌ Generic `توزیع‌شده` | Use precisely in networking context; avoid confusing with OS distributed systems. |

---

## 4. Architectural Phrasing, Theoretical Precision & Chapter Scopes

### 4.1 Chapter 4 Domain-Agnosticism Rule
- Chapter 4 introduces the proposed method, mathematical formulations, and software architecture.
- **It MUST remain strictly generic and domain-agnostic.**
- Specific empirical testbed details (e.g. DeltaIoT node counts, DARTSim flight aerodynamics, UAV radar radii, battery voltages) belong exclusively in Chapter 2 (System Modeling) and Chapter 5 (Empirical Evaluation), NEVER in Chapter 4!

### 4.2 Universal Replay Buffer Storage ($r=0$) Rigor
- Transition storage in the experience replay buffer $\mathcal{D}$ is universal: **both successful transitions ($r=1$) and failed transitions ($r=0$) are stored**.
- Storing failed transitions is mathematically indispensable for stochastic reward shaping ($\rho$) and local optima escape (Equation 4.6).
- Never state or imply that unverified or failed transitions are discarded.

### 4.3 No Inlined Code Function Names in Flowing Prose
- Never insert raw code-level function signatures with underscores (e.g. `$SMC\_Verify(s, a)$`) into flowing Persian prose.
- In prose, refer to the formal mathematical signal: `ادغام سیگنال اعتبارسنجی صوری ($r_{smc}$) مبتنی بر ابزار...`.
- Reserve procedural calls strictly for pseudocode algorithm environments: `\STATE $r_{smc} \leftarrow SMC\_Verify(s, a)$`.

### 4.4 Section 1.8 Scholarly Roadmap Alignment
- Section 1.8 (`مروری بر فصول رساله`) follows Dr. Omid Gheibi's KU Leuven PhD dissertation structure (*Applying Machine Learning in Self-Adaptive Systems*).
- It integrates publication-linked roadmap narratives and **Table 1.1** (*Master Alignment Matrix*), mapping all chapters to sub-problems, innovations, research questions, and published papers.

### 4.5 PhD Dissertation Abstract Standard
- The abstract must follow the standard single-paragraph PhD dissertation style.
- It must be dense, cohesive, and free of bullet points, concisely synthesizing: (1) core problem & planning trilemma, (2) proposed two-tier architecture, (3) formal model checking integration, (4) dual empirical testbeds (DeltaIoT & DARTSim), and (5) quantitative impact metrics.

---

## 5. Prose Structure & Anti-Bullet Fatigue Discipline

### 5.1 The Anti-Bullet Fatigue Protocol
- Do NOT use fragmented `itemize` bullet lists for standard expository paragraphs, textbook taxonomies, or scenario walkthroughs.
- Convert descriptive lists into flowing narrative paragraphs structured with bold inline headings: `\paragraph{عنوان مشخص:}`.
- Bullet and enumerated lists are **strictly reserved** for:
  1. Formal Research Questions (`RQ1` to `RQ6` and sub-questions).
  2. Core Architectural Innovations (Innovation 1 to 6).
  3. Formal mathematical induction and proof steps (Propositions 1 & 2).
  4. Formal baseline algorithm taxonomies and empirical threats to validity.

### 5.2 Direct, Academic Section & Subsection Titles
- Section headers must be direct, academic, and non-redundant.
- Avoid elongated, breathless titles loaded with buzzwords.
- Example: Use `بیان مساله` instead of elongated multi-clause titles.

---

## 6. LaTeX, XePersian & BiDi Typography Guidelines

### 6.1 Table Width & Margin Overflow Prevention
- Tables must NEVER overflow text margins.
- Always use explicit, bounded column widths:
  ```latex
  \begin{tabular}{|p{2.5cm}|p{6.0cm}|p{5.1cm}|}
  ```
- Use `\small` or `\footnotesize` font scaling within tables to maintain balanced vertical and horizontal spacing.

### 6.2 BiDi Layout, Persian Numerals & Punctuation Direction
- **Percentages & Decimals**: Ensure proper Perso-Arabic bidirectional typesetting (`۷۰/۵٪`, not `٪۵/۷۰`; `۰/۴۸۵ میلی‌ثانیه`).
- **Research Question Numbering**: Numbers must follow the English label properly (`زیرسؤال ۱-۱`, `RQ1`).
- **Punctuation & Parentheses**: Wrap all Latin terms and citations in `\lr{...}` and `\cite{...}` to prevent reversed parentheses or flipped mathematical intervals.

### 6.3 Float Placement & Figure Sizing
- Adjust figure scaling (`[width=0.85\textwidth]` to `[width=0.92\textwidth]`) so figures anchor naturally right after their first reference, preventing unnecessary dedicated blank pages.

### 6.4 Zero-Defect Compilation Command Protocol
After any XeLaTeX compilation, **always** execute the automated log verification script:
```powershell
python scratch/verify_log.py thesis_full_toc_persian_v3.log
```
The build is acceptable ONLY if:
- `Undefined references: 0`
- `Undefined citations: 0`
- `Overfull \hbox > 10pt: 0` (with max overfull strictly bounded).

### 6.5 Strict Ban on Wrapping Cross-References in `\lr{...}`
- **NEVER** wrap cross-references in `\lr{...}` (e.g. ❌ `\lr{\ref{fig:...}}`, ❌ `\lr{\ref{tab:...}}`).
- Wrapping `\ref` inside `\lr{...}` deactivates `\AutoPersianDigits` and forces the Latin font (`Times New Roman`), rendering reference numbers in English ASCII digits (`4-5`), which severely clashes with Persian citations (`[۲]`) and surrounding Persian text.
- XePersian natively handles multi-level counter delimiters via `\SepMark{-}` in `commands.tex`. All cross-references must remain bare: `شکل \ref{fig:...}`, `جدول \ref{tab:...}`, `بخش \ref{sec:...}`.

### 6.6 Numeral & Quantitative Measurement Consistency Protocol
- **Quantitative Units & Latencies**: Never wrap metrics and units in casual `\lr{...}` (e.g. ❌ `\lr{0.1ms}`, ❌ `\lr{0.05ms}`). Use uniform math mode with thin space: `$0.1\,\text{ms}$`, `$0.05\,\text{ms}$`, `$0.3\,\text{ms}$` (or write explicitly in Persian: `۰٫۱ میلی‌ثانیه`).
- **Matrix / Map Dimensions in Tables**: Typeset dimensions in math mode (e.g. `$40 \times 1$`, `$50 \times 50$`), avoiding mixed `\lr{40$\times$1}` in tables containing Persian counts.
- **Latin Acronyms & Model Designators**: Proper Latin identifiers (`\lr{RQ1}`–`\lr{RQ6}`, `\lr{6-DOF}`, `\lr{5G}`, `\lr{DeltaIoTv1}`, `\lr{v1.1}`, `\lr{TreeSHAP}`) legitimately retain English digits and must remain enclosed in `\lr{...}`.
- **Citation Numbering**: In-text citations `\cite{...}` in Persian paragraphs naturally render with Persian numerals (`[۲]`), whereas the English bibliography list (`thebibliography`) retains Latin numerals (`[2]`). Never force `\cite` into `\lr{\cite{...}}`.

---

## 7. Continuous Evolution & Dynamic Rule Synchronization Protocol

### 7.1 Mandatory Rule Persistence Trigger
Whenever the author in future sessions or turns:
1. Pinpoints a new word to ban, discipline, or standardize (e.g. terminology audits).
2. Clarifies an architectural distinction, mathematical notation, or chapter boundary.
3. Requests a structural adjustment (e.g. float placement, table formatting, section naming).
4. Refines a workflow, commit standard, or compilation constraint.

### 7.2 Execution Requirement
The agent **MUST NOT** treat the feedback as a temporary single-turn instruction. The agent must:
1. Apply the requested change to the target dissertation files (`chapters/*.tex`, `thesis_full_toc_persian_v3.tex`, etc.).
2. **Concurrently update `AGENTS.md`** in the appropriate section (or dictionary table), documenting the new rule, the rationale, and the approved/banned variants.
3. Commit and push the updated `AGENTS.md` along with the dissertation files when the user triggers a push.
