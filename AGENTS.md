# Agent Instructions & Dissertation Scholarly Guidelines

This document serves as the permanent, authoritative master directive for all AI agents, subagents, and automated workflows operating on this doctoral dissertation repository. All future edits across all chapters, abstracts, appendices, and front matter MUST strictly adhere to the guidelines, architectural conventions, and LaTeX disciplines codified herein and within the modular workspace skills in `.agents/skills/`.

> [!IMPORTANT]
> **Living Document & Dynamic Rule Maintenance Protocol**:
> Whenever a new rule is introduced, a term refined, a word banned, a stylistic constraint added, or a workflow updated, the AI agent **MUST proactively and immediately update `AGENTS.md` and the appropriate skill in `.agents/skills/`**.

---

## 1. Modular Workspace Skills & Progressive Disclosure

To prevent context budget overflows and provide automated verification tooling, detailed procedural checklists and audit scripts are organized into progressive workspace skills:

1. **`thesis-latex-typesetting`** (`.agents/skills/thesis-latex-typesetting/`): XePersian BiDi layout, math-mode numeral formatting, table width constraints, and zero-defect log verification.
2. **`thesis-persian-terminology`** (`.agents/skills/thesis-persian-terminology/`): Complete 45+ term Persian technical dictionary and automated regex scanner (`audit_terms.py`).
3. **`thesis-scholarly-writing`** (`.agents/skills/thesis-scholarly-writing/`): Doctoral prose tone, elimination of AI hype words/fillers, and Anti-Bullet Fatigue discipline (`audit_prose.py`).
4. **`thesis-chapter-architect`** (`.agents/skills/thesis-chapter-architect/`): Epistemological scopes, negative boundaries, and guidelines for authoring chapters and appendices.
5. **`thesis-bibliography-manager`** (`.agents/skills/thesis-bibliography-manager/`): BibTeX integrity, `ieeetr-fa` styling, citation resolution, and footnote conventions (`audit_citations.py`).
6. **`thesis-git-discipline`** (`.agents/skills/thesis-git-discipline/`): Safe version control, 100MB file protection, automated push pipeline, and pre-receive hook defense (`safe_push.py`).
7. **`thesis-build-cleanup`** (`.agents/skills/thesis-build-cleanup/`): Post-compilation build hygiene, automated auxiliary file cleanup (`.aux`, `.log`, `.out`, `.toc`, `.bbl`, `.xdv`, etc.), and pristine workspace maintenance (`clean_build.py`).

---

## 2. Git Remote & Automated Push Workflow

### 2.1 Remote Repository & Size Limit
- Remote: **`https://github.com/alirezakavianifar/thesis.git`**
- GitHub strictly enforces a 100MB file limit. **NEVER** commit large binaries, archives (`.rar`, `.zip`), build dumps, or compiled PDFs.
- Ensure `.gitignore` is verified before staging.

### 2.2 Automated Push on Keyword "push"
When the user uses the keyword **"push"** in a request, you **MUST proactively execute**:
```powershell
python .agents/skills/thesis-git-discipline/scripts/safe_push.py
```
This automatically verifies file sizes, stages changes, generates an inferred semantic commit message, commits, and pushes.

---

## 3. Scholarly Tone, Humanization & Anti-AI Hype Discipline

1. **Authoritative Scholarly Persian**: Evaluate prose from the perspective of an external doctoral examiner. Avoid conversational throat-clearing, run-on sentences, and breathless rhetoric.
2. **Strictly Purged Hype Words (100% Banned)**:
   - `نوین` $\rightarrow$ Use `پیشنهادی`, `مدرن`, `پیشرفته`, or `جدید`.
   - `انقلابی`, `شگفت‌انگیز`, `دگرگون‌ساز`.
   - `چشمگیر` $\rightarrow$ Use `به طور قابل‌ملاحظه‌ای`, `شدید`, or report exact quantitative deltas ($23.22\%$).
   - `فوق‌العاده` $\rightarrow$ Use `با رواداری محدود`, `بسیار باریک`, or state the quantitative bound.
   - Casual prefix `فوق` (`فوق‌سریع`, `فوق‌العاده`).
3. **Elimination of Conversational Fillers**:
   - ❌ Banned: `شایان ذکر است که`, `لازم به یادآوری است که`, `بدیهی است که`, `همان‌طور که می‌دانیم`, `نکته جالب توجه این است که`.
   - ✔️ Use direct, assertive declarative sentences.
4. **Anti-Bullet Fatigue**:
   - Do NOT use fragmented `itemize` / `enumerate` lists for standard expository descriptions or taxonomies.
   - Restructure descriptive lists into flowing narrative paragraphs with bold inline headings: `\paragraph{عنوان مشخص:}`.
   - Bullet lists are strictly reserved for: Research Questions (`RQ1`--`RQ6`), Core Innovations (1--6), formal mathematical proofs, and validity threats.

---

## 4. Persian Technical Terminology Standards

The mandatory vocabulary is strictly enforced. The full table and rationale are in [terminology_dictionary.md](.agents/skills/thesis-persian-terminology/references/terminology_dictionary.md).

- **Core Invariants**:
  - `سیستم` (mandatory) vs ❌ `سامانه` (100% strictly banned).
  - `بلادرنگ` (mandatory) vs ❌ `زمان‌حقیقی`, `زمان واقعی`, `بی‌درنگ`.
  - `سیستم‌های خودوفق` (صفت مرکب برای سیستم‌ها و کنترل‌کننده‌ها) vs ❌ `سیستم‌های خودتطبیق‌پذیر`, `سامانه‌های خودسازگار`.
  - `خودوفقی` (اسم مصدر/قابلیت/پارادایم کلان: `قابلیت خودوفقی`) vs ❌ `خودتطبیقی`, `خودسازگاری`.
  - `انطباق` (اسم مصدر برای چرخه، مراحل، فرامین و انطباق با مشخصه‌ها: `چرخه انطباق`, `فرآیند انطباق`, `طرح انطباق`, `فرمان انطباق`, `انطباق با مشخصه‌ها`, `بردار انطباق`) vs ❌ `تطبیق`.
  - `وفقی` (صفت نسبی برای فضاها، گزینه‌ها، اقدامات و اهداف: `فضای وفقی`, `اقدام وفقی`, `گزینه وفقی`, `اهداف وفقی`, `استنتاج وفقی`) vs ❌ `اقدام انطباقی`, `گزینه‌های انطباقی`, `اهداف انطباقی`, `استنتاج انطباقی`.
  - `تحلیل تطبیقی` vs ❌ `تحلیل انطباقی` (`تطبیق` صرفاً برای ارزیابی مقایسه‌ای).
  - `سازگار با قیود` ($\mathcal{N}_{\text{sat}}$) vs ❌ `سیستم‌های خودسازگار`.
  - `ناهمگام` vs ❌ `غیرهمگام`.
  - `ریسمان` vs ❌ `نخ`.
  - `فرآیند` vs ❌ `پردازه`.
  - `سازوکار` vs ❌ `مکانیسم`.
  - `ایستا` vs ❌ `استاتیک`.
  - `دسته / دسته‌های کوچک داده` vs ❌ `بچ / مینی‌بچ`.
  - `کلیدی / بنیادین` vs ❌ `حیاتی`.
  - `بافر بازپخش` vs ❌ `میانگیر بازپخش`.
  - `کاندیداها / گزینه‌های کاندید` vs ❌ `گزینه‌های نامزد`.
  - `غیربرخط / برخط` vs ❌ `آفلاین / آنلاین`، `برون‌خط`.
  - `سوابق عملیاتی / سوابق غیربرخط` vs ❌ `لاگ`, `وقایع‌نگاشت`.
  - `اعتبارسنجی صوری` vs ❌ mixed `راستی‌آزمایی صوری`.
  - `وارسی مدل (آماری)` vs ❌ `مدل‌چکینگ`.
  - `نمودار` vs ❌ `دیاگرام`.
  - `راه‌انداز` vs ❌ `درایور`.
  - `پشتیبان` vs ❌ `فال‌بک`.
  - `الکترونیک پروازی` vs ❌ `اویونیک`.
  - `کنترل همروندی بدون قفل` vs ❌ `مدیریت همزمانی بدون قفل`.
  - `شرایط رقابتی / وضعیت رقابتی` (\lr{Race Conditions}) vs ❌ `شرایط مسابقه`.
  - `نوسان تأخیر` (\lr{Latency Jitter}) vs ❌ `تأخیر نوسانی`.
  - `اشاره‌گر / تبادل تجزیه‌ناپذیر` (\lr{Atomic Pointer Swap}) vs ❌ `اشاره‌گر اتمیک`، `جابه‌جایی تجزیه‌ناپذیر`.
  - `ریسمان‌امن` (\lr{Thread-Safe}) vs ❌ `نخ‌امن`.
  - `صف وظایف ناهمگام` (\lr{Asynchronous Task Queue}) vs ❌ `صف کاربری ناهمگام`.
  - `قفل انحصار متقابل` (\lr{Mutex}) vs ❌ `قفل انحصاری`.
  - `تزاحم بر سر قفل` (\lr{Lock Contention}) vs ❌ `رقابت بر سر قفل`.
  - `سنتز کنترل‌کننده / سنتز خط‌مشی / سنتز صوری` (\lr{Controller/Policy Synthesis}): مجاز و استاندارد در روش‌های صوری، مهندسی نرم‌افزار خودکار و الگوی معماری \sgos vs ❌ تعمیم به «سنتز داده» (از `تلفیق داده / تجمیع شواهد` استفاده شود)، «سنتز مؤلفه‌ها» (از `ترکیب مؤلفه‌ها / ترکیب‌بندی` استفاده شود)، یا «سنتز ادبیات / سنتز به پرسش‌ها» (از `تلفیق پیشینه پژوهش / تلفیق یافته‌ها` استفاده شود).
  - `تفکیک فاز اجرا از دیرند و تأخیر زمانی`: استفاده از `تأخیر کل تصمیم‌گیری / بدترین حالت تأخیر تصمیم‌گیری / تأخیر کل برنامه‌ریزی` vs ❌ ترکیب حشوآمیز `تأخیر کل زمان اجرا`؛ و پرهیز از تکرار چندباره `زمان اجرا` در یک بند یا جمله واحد (جایگزینی متناسب با `برخط`، `حین اجرا` یا حذف واژه زاید در صورت ووضوح بافت موضوعی).
  - `پرهیز از کاربرد حشوآمیز صفت مرکب «کم‌تأخیر»` (\lr{Low-Latency}):
    - ❌ ممنوعیت همنشینی «کم‌تأخیر» با «بلادرنگ» (مانند `تصمیم‌گیری بلادرنگ و کم‌تأخیر` یا `استنتاج بلادرنگ کم‌تأخیر` $\rightarrow$ استفاده مستقیم از `تصمیم‌گیری بلادرنگ میلی‌ثانیه‌ای` یا `استنتاج بلادرنگ سیاست`).
    - ❌ ممنوعیت ذکر همزمان صفت کیفی مبهم «کم‌تأخیر» در کنار سنجه‌های کمّی صریح (مانند `استنتاج کم‌تأخیر زیر نیم میلی‌ثانیه‌ای` $\rightarrow$ `استنتاج در مقیاس زیر نیم میلی‌ثانیه‌ای`؛ `مستقیم و کم‌تأخیر ($0.2\,\text{ms}$)` $\rightarrow$ `مستقیم با دیرند $0.2\,\text{ms}$`).
    - ❌ ممنوعیت کاربرد «کم‌تأخیر» در عناوین گام‌ها و خط لوله به جای نقش فنی متغیر (مانند `استنتاج کم‌تأخیر ($a^*$):` $\rightarrow$ استفاده از `استنتاج اقدام نامی ($a^*$):`).
    - ✔️ در سایر زمینه‌ها، ترجیح اکید بر استفاده از اصطلاحات معیار مهندسی نظیر `بلادرنگ`، `با کمترین تأخیر` یا بیان صریح کران زمانی/دیرند است.
  - `کاربرد دقیق واژه «استنتاج»` (\lr{Inference}): مجاز و استاندارد صرفاً به عنوان اصطلاح تخصصی یادگیری ماشین و شبکه‌های عصبی عمیق (\lr{Inference} در برابر \lr{Training}: «زمان استنتاج»، «تأخیر استنتاج»، «مسیر استنتاج»، «استنتاج وفقی») vs ❌ کاربردهای حشوآمیز و نامأنوس نظیر `استنتاج تصمیم` (استفاده از `تصمیم‌گیری / اتخاذ تصمیم`)، انباشت مترادف‌های زاید `برنامه‌ریزی، استنتاج و تولید` (استفاده از `برنامه‌ریزی و تولید`)، یا تحمیل ساختار سنگین `با استنتاج مستقیم ... پیشنهاد را ارائه داده` در چکیده (استفاده مستقیم از `ارائه پیشنهاد اولیه (نامی) در مقیاس زیر میلی‌ثانیه‌ای`).
- **Audit & Extraction Tools**:
  - Run `python .agents/skills/thesis-persian-terminology/scripts/audit_terms.py` for mandatory rule violations.
  - Run `python .agents/skills/thesis-persian-terminology/scripts/extract_term_context.py --term "<term>"` (powered by `ripgrep`) to extract surrounding context for nuanced terminology arbitration against literature (see [disambiguation_guide.md](.agents/skills/thesis-persian-terminology/references/disambiguation_guide.md)).

---

## 5. Architectural Scopes & Chapter Negative Boundaries

Each chapter has an immutable scientific nature. For detailed contracts, see [chapter_boundaries.md](.agents/skills/thesis-chapter-architect/references/chapter_boundaries.md).

- **فصل ۱ (کلیات و تبیین مسئله)**: Research Contract, Trilemma, Sub-problems 1--3, \lr{RQ1}--\lr{RQ6}, 6 Innovations, Alignment Matrix. ❌ NO code, NO mathematical proofs, NO empirical result tables, NO physical domain kinematics.
- **فصل ۲ (مبانی نظری و مدل‌سازی)**: Mathematical Foundations (MDP, DRL, SMC), Ground Truth Testbed Models (DeltaIoT DAG, DARTSim 6-DOF). ❌ NO novel proposed algorithms (\lr{RS-DRL}, \rsdrlplus), NO empirical results, NO literature critiques.
- **فصل ۳ (پیشینه پژوهش و کارهای مرتبط)**: 5-Dimensional Critical Taxonomy, Synthesis Matrix (Table 3.1), Tripartite Gap. ❌ NO passive textbook summaries, NO proposed algorithm mechanics, NO thesis experimental data.
- **فصل ۴ (روش پیشنهادی و معماری دوسطحی)**: **100% DOMAIN-AGNOSTIC**. Baseline \lr{RS-DRL}, \rsdrlplus, Patterns \sgos & \caepv (\pgalr), Propositions 1 & 2. ❌ NO testbed-specific numbers/topologies in definitions, NO inlined code function names in prose, NO empirical tables.
- **فصل ۵ (ارزیابی تجربی و تحلیل نتایج)**: DeltaIoT & DARTSim benchmarks, 2,000 flights, ablation studies, Wilcoxon/Cohen's $d$ tests. ❌ NO mathematical re-derivations, NO unsupported assertions, NO missing baselines.
- **فصل ۶ (بحث، نتیجه‌گیری و کارهای آتی)**: Mechanistic theorization, Pareto trade-offs, SE guidelines, 4-dimensional validity threats, 3 future horizons. ❌ NO new empirical figures/tables, NO algorithm re-derivations, NO superficial summaries.
- **پیوست‌ها (ضمائم)**: Appendix A: Full UML Workflows; Appendix B: Full Algorithm Listings; Appendix C: Extended Benchmark Logs; Appendix D: Reproducibility Package.

---

## 6. LaTeX, XePersian & BiDi Typography Guidelines

1. **BiDi Math Mode for Numerals & Metrics**: Under XePersian, bare Persian numbers containing decimals, fractions, thousands commas, decibels, or units reverse digit order. Always typeset in math mode with thin space:
   - `$70.5\%$`, `$137/200$`, `$2{,}000$`, `$0.485\,\text{ms}$`, `$-40\,\text{dB}$`.
2. **Heading Safety (`\texorpdfstring`)**: Wrap math symbols or Latin algorithm macros in `\texorpdfstring{$...$}{...}` in headings to guarantee 0 hyperref token warnings.
3. **Strict Ban on Wrapping Cross-References in `\lr{...}`**:
   - Cross-references must remain bare: `شکل \ref{fig:...}`, `جدول \ref{tab:...}`, `بخش \ref{sec:...}`. Wrapping in `\lr{...}` forces Latin numbers and breaks Persian layout.
4. **Table Sizing**: Always use explicit column widths (`p{...}`), `\small` or `\footnotesize`, preventing overfull `\hbox`.
5. **Footnotes**: Move non-acronym English equivalents to `\LTRfootnote{...}` on first chapter mention. Strip redundant parentheticals on later mentions. Never place `\LTRfootnote` inside headings, captions, or tables.
6. **Zero-Defect Verification Command**:
   ```powershell
   python .agents/skills/thesis-latex-typesetting/scripts/verify_build.py thesis_full_toc_persian_v3.log
   ```
   Acceptable build criteria:
   - `Undefined references: 0`
   - `Undefined citations: 0`
   - `Hyperref warnings: 0`
   - `Overfull \hbox > 10pt: 0` (max overfull bounded strictly $< 10\,\text{pt}$)
   - `Total PDF pages: 164-165`
7. **Mandatory Post-Compilation Cleanup Protocol**:
   - Immediately after each XeLaTeX PDF compilation and verification of `thesis_full_toc_persian_v3.log`, the agent **MUST ALWAYS clean up all intermediate build files**:
     ```powershell
     python .agents/skills/thesis-build-cleanup/scripts/clean_build.py
     ```
   - No PDF generation turn is considered complete until all auxiliary artifacts (`.aux`, `.log`, `.out`, `.toc`, `.lof`, `.lot`, `.bbl`, `.blg`, `.idx`, `.xdv`, etc.) have been purged.

---

## 7. Dynamic Rule Synchronization Protocol

Whenever the author in any session introduces a new rule, refines a term, or adjusts a constraint, the agent must:
1. Apply the requested change to the target dissertation files.
2. Concurrently update `AGENTS.md` and the appropriate skill in `.agents/skills/`.
3. Commit and push the updated files when the user triggers a push.
