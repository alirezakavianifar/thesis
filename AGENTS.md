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
- ❌ **Strictly Banned Hype Words (100% Purged Across Dissertation)**:
  - `نوین` (novel / modern) $\rightarrow$ Use `پیشنهادی` (proposed), `مدرن` (modern), `پیشرفته` (advanced), or `جدید` (new).
  - `انقلابی` (revolutionary)
  - `شگفت‌انگیز` (astonishing)
  - `دگرگون‌ساز` (transformative)
  - `چشمگیر` (dramatic / impressive) $\rightarrow$ Use `به طور قابل‌ملاحظه‌ای`, `شدید`, or report exact quantitative deltas ($23.22\%$).
  - `فوق‌العاده` (extraordinary) $\rightarrow$ Use `با رواداری محدود`, `بسیار باریک`, or state the quantitative bound.
- ✔️ **Approved Scholarly Equivalents**:
  - `پیشنهادی` (proposed)
  - `توسعه‌یافته` (developed)
  - `سنجیده‌شده` (evaluated)
  - `اثبات‌شده` (proven)
  - `مؤثر / اثرگذار` (effective)

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
- ❌ Avoid artificial rhetorical qualifiers such as `موازنه عمیق` or `پیچیدگی عمیق` (use precise academic terms like `برقراری موازنه` or `موازنه چندمعیاره/دقیق`).
- ❌ Avoid awkward, unnatural translations like `تفکیک زمانی مسئولیت‌های کنترلی` or `سازماندهی فرایند یکپارچه خودوفقی برپایه خطوط شناور` (use standard software engineering expressions).

---

## 3. The Comprehensive Persian Terminological Dictionary

The following table defines the mandatory, standardized technical vocabulary across the entire dissertation. Any deviation is strictly prohibited.

| Concept | Mandatory Persian Term | Strictly Banned / Avoided | Specific Rule & Technical Rationale |
| :--- | :--- | :--- | :--- |
| **System** | **`سیستم`** | ❌ `سامانه` | Standardized 100% across the thesis (`سیستم‌های خودوفق`, `سیستم هدف`, `سیستم‌های فیزیکی-سایبری`). The word `سامانه` is completely purged. |
| **Real-Time** | **`بلادرنگ`** | ❌ `زمان‌حقیقی`<br>❌ `زمان واقعی`<br>❌ `بی‌درنگ` | Sole official Academy of Persian Language & Literature & IEEE-Iran term. Never use `زمان واقعی` or call Soft-QoS systems (DeltaIoT 8-min period) real-time. Never stack `برخط بلادرنگ`. |
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
| **Critical** | **`بحرانی` (Strictly Disciplined)** | ❌ Rhetorical intensifiers<br>❌ Ambiguous `مسیر بحرانی` | **ONLY** permitted in formal technical terms: `گره‌های بحرانی`, `آستانه‌ها/مرزهای بحرانی`. For system classification, prefer **`سیستم‌های فیزیکی-سایبری حساس و بلادرنگ`** or **`بلادرنگ`** over the clunky calque `مأموریت‌بحرانی`. Never `مهلت بحرانی` (use `مهلت زمانی سخت پروازی`), `چالش‌های بحرانی` (use `چالش‌های بنیادین`), `شرایط بحرانی` (use `شرایط تنش شدید محیطی`), or `تنش بحرانی` (use `فراتر رفتن تنش از آستانه بحرانی`). For systems execution paths, avoid `مسیر بحرانی` (which confuses readers with crisis/emergency mode) and use **`مسیر مستقیم کنترل برخط / مسیر زمان اجرای کنترل (\lr{Critical Path})`**. |
| **Speed & Latency** | **`بلادرنگ / کم‌تأخیر / زیر میلی‌ثانیه‌ای / مسیر سریع (Fast Path)`** | ❌ `سریع` (as casual intensifier)<br>❌ `فوق‌سریع` | Never use `سریع` casually for latency (e.g. ❌ `تصمیم‌گیری سریع` $\rightarrow$ `پاسخ‌گویی در مهلت‌های زمانی سخت`, ❌ `استنتاج سریع` $\rightarrow$ `استنتاج نامی زیر میلی‌ثانیه‌ای`, ❌ `مدل‌های سریع` $\rightarrow$ `مدل‌های جانشین تحلیلی و سبک‌وزن`, ❌ `جستجوی سریع` $\rightarrow$ `جستجوی تقلیلی روی زیرفضای حساسیت`, ❌ `استهلاک سریع هزینه` $\rightarrow$ `تحلیل بازه استهلاک آن`). Always state the quantitative metric directly (`زیر میلی‌ثانیه‌ای`, `$0.485\,\text{ms}$`) or use formal engineering terms (`بلادرنگ`, `کم‌تأخیر`, `مسیر سریع`). `سریع` is strictly permitted ONLY in: (1) formal pattern names (`«مسیر سریع» (\lr{Fast Path})`), (2) empirical speedup ratios (`۲۷۰ برابر سریع‌تر`), (3) learning convergence dynamics (`همگرایی سریع‌تر / تسریع همگرایی`), and (4) physical avionics dynamics (`تخلیه سریع باتری`). |
| **Immediate Reward** | **`پاداش آنی`** | ❌ `پاداش لحظه‌ای` (unless contrasting with future cumulative value) | Standard MDP mathematical translation for $R(s, a, s')$. |
| **Vital / Crucial** | **`کلیدی / بنیادین / تعیین‌کننده`** | ❌ `حیاتی` | `حیاتی` is completely banned due to journalistic exaggeration. |
| **Baseline Method** | **`روش پایه‌ای RS-DRL`** | ❌ `متد`, `الگوریتم کلی` | Foundational single-tier algorithmic formulation. |
| **Generalized Architecture** | **`معماری تعمیم‌یافته RS-DRL+`**| ❌ `روش تعمیم‌یافته` | Two-tier contract-anytime software architecture. |
| **Holistic Framework** | **`چارچوب`** | ❌ `فریم‌ورک` | The overarching theoretical and engineering construct. |
| **Architectural Patterns** | **`الگوهای معماری SG-OS و CAE-PV`** | ❌ `روش‌های SG-OS` | Software engineering design patterns. |
| **Distributed Systems** | **`شبکه‌های حسگر توزیع‌شده`** | ❌ Generic `توزیع‌شده` | Use precisely in networking context; avoid confusing with OS distributed systems. |
| **Batch & Mini-batch** | **`دسته / دسته‌های کوچک داده (\lr{Mini-batches}) / اندازه دسته (\lr{Batch Size}) / دسته موازی تانسوری`** | ❌ `مینی‌بچ`<br>❌ `بچ` | Standardized across TMU, Sharif, and UT computing documents. Colloquial transliterations (`مینی‌بچ` / `بچ`) are 100% purged. |
| **Static** | **`ایستا`** | ❌ `استاتیک` | Standard Persian computer systems terminology (`سپرهای ایمنی ایستا`, `اهداف غیربرخط ایستا`). |
| **Mechanism** | **`سازوکار`** | ❌ `مکانیسم` | Official Academy term standardized 100% across the thesis (`سازوکارهای شکل‌دهی پاداش`). |
| **Platform** | **`بستر / سکو`** | ❌ `پلتفرم` | Always use `بستر پیاده‌سازی` or `بستر آزمایشگاهی/محک`. |
| **Mathematical Factor / Multiplier** | **`ضریب`** | ❌ `فاکتور` | Mathematical multipliers ($\gamma, \rho, \beta, \sigma$) must strictly be `ضریب` (`ضریب تنزیل زمانی`, `ضریب شکل‌دهی پاداش`, `ضریب مقیاس`). For environmental conditions, use `عوامل محیطی / متغیرهای کنترلی`. |
| **Replay Buffer** | **`بافر بازپخش`** | ❌ `میانگیر بازپخش` | Established standard term in Iranian AI & DRL departments; `میانگیر` is pedantic and unused in RL. |
| **Candidate Actions / Sets** | **`کاندیداها / گزینه‌های کاندید / مجموعه کاندید`** | ❌ `گزینه‌های نامزد` | In Persian optimization and AI literature, `کاندید` is the universal technical term; `نامزد` connotes marriage or political elections. |
| **Offline / Online** | **`غیربرخط / برخط`** | ❌ `آفلاین / آنلاین`، `برون‌خط` | Standardized across all chapters per Academy/TMU convention; all usages in this dissertation denote pre-deployment training vs. runtime control (zero network-connectivity ambiguity). |
| **Operational / Offline Logs** | **`سوابق عملیاتی / سوابق غیربرخط / سوابق بازپخش`** | ❌ `لاگ`، `لاگ‌ها`، `گزارش` (ambiguous with prose reports)، `وقایع‌نگاشت` (artificial calque) | Standardized formal Persian academic terminology aligned with TMU Persianization policy and existing usage (`سوابق پرواز`، `سوابق مشاهدات`). Anchor with `\LTRfootnote{Operational Logs}` on first chapter mention; reserve `ردپا` exclusively for environmental traces. |
| **Formal Verification / Validation** | **`اعتبارسنجی صوری`** | ❌ Inconsistent mixing with `راستی‌آزمایی صوری` | Standardized as `اعتبارسنجی صوری` for formal verification with UPPAAL-SMC and mathematical feedback signals ($r_{smc}$). |
| **Model Checking (Statistical)** | **`وارسی مدل (آماری)`** | ❌ `مدل‌چکینگ` | Standardized formal methods terminology for statistical model checking (`وارسی مدل آماری`). |
| **Diagram / Activity Diagram** | **`نمودار (فعالیت / جریان)`** | ❌ `دیاگرام` | Formal Persian academic terminology (`نمودار فعالیت`). |
| **Hardware Driver** | **`راه‌انداز (سخت‌افزاری)`** | ❌ `درایور` | Standard Persian systems engineering term (`راه‌اندازهای سخت‌افزاری`). |
| **Fallback (Branch / Rule / Mechanism)** | **`پشتیبان (شاخه / قاعده / سازوکار پشتیبان)`** | ❌ `فال‌بک` | Formal Persian equivalent for fallback control branches (`شاخه پشتیبان`). |
| **Gate (Margin / Stress Gate)** | **`دروازه (تنش / حاشیه)`** | ❌ `گیت` | Formal Persian equivalent for runtime safety gating (`دروازه تنش محیطی`). |
| **Atomic (Pointer Swap / Update)** | **`تجزیه‌ناپذیر`** | ❌ `اتمیک` | Formal Persian concurrency term for lock-free atomic operations (`تبادل تجزیه‌ناپذیر وزن‌ها`). |
| **Scalar** | **`نرده‌ای`** | ❌ `اسکالر` | Official Persian mathematical terminology (`پاداش نرده‌ای`). |
| **Probe (Sensory / Monitoring)** | **`کاوشگر`** | ❌ `پروب` | Standard Persian telemetry term (`کاوشگرهای حسگری / پایش`). |
| **Link (Radio / Network)** | **`پیوند`** | ❌ `لینک` | Standard Persian networking term (`پیوندهای رادیویی`). |
| **Mode (Operational Mode)** | **`حالت`** | ❌ `مد` | Unambiguous formal Persian term for operational system modes (`حالت‌های غیرعملیاتی`). |
| **Calibration** | **`واسنجی`** | ❌ `کالیبراسیون` | Official Academy of Persian Language & Literature term (`خطای واسنجی`). |
| **Catalog (Hyperparameter Catalog)** | **`فهرست جامع`** | ❌ `کاتالوگ` | Formal Persian academic equivalent (`فهرست جامع فراپارامترها`). |
| **Frequency (Control / Update)** | **`بسامد` (کنترلی) / `تواتر` (به‌روزرسانی)** | ❌ `فرکانس` | Official Persian equivalents distinguishing physical rate (`بسامد`) from invocation/update rate (`تواتر`). |
| **Isolate / Isolated / Isolation** | **`مجزا / جدا کردن / جداسازی`** | ❌ `ایزوله / ایزوله‌سازی` | Formal Persian architectural separation terminology (`لایه مجزا`، `جداسازی`). |
| **Theoretical / Theoretically** | **`نظری / به صورت نظری`** | ❌ `تئوریک` | Standard Persian academic writing (`کران نظری`، `به صورت نظری`). |
| **Formulate / Formulation** | **`فرمول‌بندی کردن / فرمول‌بندی`** | ❌ `فرموله / فرمولاسیون` | Consistent Persian academic usage (`فرمول‌بندی می‌شود`). |
| **Avionics** | **`الکترونیک پروازی`** | ❌ `اویونیک` | Formal Persian aerospace engineering equivalent (avoiding banned `سامانه`). |

---

## 4. Architectural Scopes & The True Nature of Dissertation Chapters

This section establishes the authoritative, permanent specification for the epistemological identity, core scientific responsibilities, strict negative boundaries, and inter-chapter interfaces across all chapters of the doctoral dissertation. All future authoring, automated code generation, and editing across the dissertation MUST strictly respect these boundaries to prevent conceptual leakage, methodological pollution, and structural drift.

### 4.1 The Epistemological Progression & Inter-Chapter Cohesion Architecture

The dissertation follows a strict, coherent progression modeled on high-impact European and North American software engineering doctoral dissertations (e.g., Dr. Omid Gheibi's KU Leuven doctoral model). The logical chain progresses deterministically from problem framing to formal domain truth, critical gap synthesis, domain-agnostic architectural solution, empirical benchmark proof, and reflective scholarly synthesis:

```
[Chapter 1: Research Contract & Trilemma]
        │
        ├──► [Chapter 2: Formal Physics & Testbeds] ──┐
        │                                              │ (Models & Specs)
        ├──► [Chapter 3: Critical Gap Analysis]        │
        │               │                              ▼
        │               └───────────────────► [Chapter 4: Generic Architecture & Proofs]
        │                                              │
        │                                              ▼
        └───────────────────────────────────► [Chapter 5: Empirical Proof & Statistics]
                                                       │
                                                       ▼
                                              [Chapter 6: Synthesis & Validity Threats]
                                                       │
                                              [Appendices: Reproducibility Artifacts]
```

| Chapter | Title & Scope | True Scientific Nature (ماهیت واقعی) | Mandatory Input Sources | Core Scientific Deliverable / Output | Downstream Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **فصل ۱** | کلیات و تبیین مسئله | **Research Contract & Problem Formulation**: Establishes the "Why" and "What", formalizes the Planning Trilemma, and specifies the dissertation's commitments. | Contextual motivation, real-world CPS challenges. | Formulated Sub-problems 1--3, Research Questions \lr{RQ1}--\lr{RQ6}, 6 Core Innovations, Alignment Matrix. | Dictates the scope of all subsequent chapters (Ch 2--6). |
| **فصل ۲** | مبانی نظری و مدل‌سازی سیستم | **Ground Truth & Mathematical Physics**: Establishes formal mathematical foundations and models the physical testbed environments before proposing any solution. | Mathematical systems theory, physical testbed specifications (DeltaIoT, DARTSim). | Formal MDP models, WSN topology equations, 6-DOF flight kinematics, radar models, NP-hardness proof. | Feeds environment models and constraints into Ch 4 and Ch 5. |
| **فصل ۳** | پیشینه پژوهش و کارهای مرتبط | **Critical Synthesis & Gap Justification**: Systematically investigates existing state-of-the-art across 5 dimensions to mathematically and architecturally prove research gaps. | Prior published literature, baseline frameworks (ActivFORMS, PLA, DRL, Shields). | 5-dimensional critical taxonomy, Comparative Matrix (Table 3.1), Tripartite Research Gap. | Scientifically justifies the imperative for Ch 4's contributions. |
| **فصل ۴** | روش پیشنهادی و معماری دوسطحی | **Generic Methodology & Software Architecture**: The intellectual core. Pure domain-agnostic mathematical formulations, architectural patterns, and formal proofs. | Research contract (Ch 1), theoretical foundations (Ch 2), identified gaps (Ch 3). | Baseline \lr{RS-DRL}, \rsdrlplus, Patterns \sgos & \caepv (\pgalr), Formal Proofs (Proposition 1, Theorem 2). | Provides the algorithms, patterns, and mechanisms evaluated in Ch 5. |
| **فصل ۵** | ارزیابی تجربی و تحلیل نتایج | **Empirical Proof & Benchmark Validation**: Concrete experimental execution of Ch 4 algorithms on Ch 2 testbeds, benchmarking against all baselines with statistical rigor. | Architecture & algorithms (Ch 4), testbeds & simulation traces (Ch 2). | DeltaIoT benchmarks, 2,000 DARTSim flights, ablation studies, non-parametric statistical tests (\lr{RQ1}--\lr{RQ6}). | Provides the empirical evidence evaluated and reflected upon in Ch 6. |
| **فصل ۶** | بحث، نتیجه‌گیری و کارهای آتی | **Scholarly Synthesis & Critical Reflection**: Mechanistic theorization, software engineering trade-offs, critical threats to validity, and future horizons. | Empirical results (Ch 5), architectural designs (Ch 4), problem contract (Ch 1). | Mechanistic insights ("Why it works"), Pareto trade-offs, 4-dimensional validity analysis, 3 future research horizons. | Concludes the dissertation and frames future doctoral/postdoctoral inquiries. |
| **پیوست‌ها** | پیوست‌ها و ضمائم | **Reproducibility & Exhaustive Evidence**: Comprehensive operational repositories for 100% independent replication. | Raw logs, extended traces, full codebase scripts. | Complete UML activity diagrams, extended algorithmic listings, parameter tables, replication packages. | Supports long-term academic reproducibility and open science. |

---

### 4.2 Chapter 1: کلیات و تبیین مسئله (Problem Formulation & Research Contract)

- **True Scientific Nature (ماهیت واقعی)**:
  The **Research Contract & Problem Definition** chapter. It establishes the overarching scientific motivation, identifies the fundamental trade-offs in modern computing, and contracts the exact research promises of the PhD dissertation. It must hook both general computer scientists and expert examiners by framing the **Planning Trilemma in Self-Adaptive and Cyber-Physical Systems** (large state-action spaces vs. hard real-time latency vs. physical safety / reality gap).
- **Mandatory Inclusions & Scientific Responsibilities**:
  1. *Motivation & Industrial/Physical Context*: The growing scale of autonomous systems and the failure of traditional single-tier planners.
  2. *The Planning Trilemma*: Formal characterization of the fundamental conflict between scalability, real-time deadlines, and formal safety.
  3. *Sub-problems Formulation*: Precise mathematical/architectural definition of Sub-problem 1 (state-action explosion), Sub-problem 2 (sparse feedback & credit assignment), and Sub-problem 3 (reality gap & hard real-time latency).
  4. *Formal Research Questions*: Unambiguous formulation of \lr{RQ1} through \lr{RQ6}.
  5. *Core Innovations*: Explicit delineation of the 6 foundational innovations.
  6. *Section 1.8 Scholarly Roadmap Alignment*: Must follow Dr. Omid Gheibi's model, integrating publication-linked narratives and **Table 1.1** (*Master Alignment Matrix*) mapping all chapters to sub-problems, innovations, research questions, and published papers.
  7. *PhD Dissertation Abstract Standard*: The abstract must follow the standard single-paragraph PhD dissertation style: dense, cohesive, free of bullet points, synthesizing the trilemma, proposed architecture, formal verification, dual testbeds, and quantitative impact metrics.
- **Strict Negative Boundaries & Forbidden Elements**:
  - ❌ **NO Algorithmic Implementations or Code**: Never insert detailed algorithmic pseudocodes, neural network layer configurations, or procedural execution mechanics (belongs strictly to Ch 4).
  - ❌ **NO Mathematical Proofs**: Never include formal induction steps, convergence proofs, or complexity lemmas (belongs strictly to Ch 4).
  - ❌ **NO Concrete Empirical Result Tables or Curves**: Never report benchmark outcome tables, learning curve plots, or statistical test results (belongs strictly to Ch 5).
  - ❌ **NO Physical Domain Equations**: Never derive radio propagation formulas, WSN interference equations, or aerodynamic 6-DOF flight physics (belongs strictly to Ch 2).

---

### 4.3 Chapter 2: مبانی نظری و مدل‌سازی سیستم (Theoretical Foundations & Formal Domain Modeling)

- **True Scientific Nature (ماهیت واقعی)**:
  The **Ground Truth & Mathematical Physics** chapter. Its exclusive purpose is to formalize the mathematical tools (MDP, DRL, formal verification, MAPE-K) AND rigorously model the physical testbed environments before any novel solution is proposed. It defines the formal ground truth of the systems being managed.
- **Mandatory Inclusions & Scientific Responsibilities**:
  1. *Foundations of Self-Adaptive Systems*: Formal closed-loop autonomic control architectures, MAPE-K reference models, and dynamic adaptation mechanisms.
  2. *Taxonomy of Uncertainty*: Mathematical and operational classification of uncertainty in self-adaptive systems.
  3. *Sequential Decision-Making & DRL*: Formal MDP tuple $(S, A, P, R, \gamma)$, Bellman optimality equations, and Deep Q-Networks (DQN).
  4. *Case Study 1 Modeling (DeltaIoT)*:
     - Topological structure as a directed acyclic graph (DAG).
     - Physical radio channel propagation, interference, signal-to-noise ratio (SNR), and packet delivery probability.
     - Multi-hop queue dynamics, packet loss mechanisms, and energy consumption models.
     - Formal proof of the NP-Hardness of the adaptation optimization problem.
  5. *Case Study 2 Modeling (DARTSim)*:
     - 6-DOF tactical UAV fleet kinematics, aerodynamics, and flight control parameters.
     - Multi-level flight corridor tolerances ($v_1, v_2, v_3$).
     - Sensor radar detection models, battery discharge dynamics, and mission survival definitions.
     - Formalization of the **Reality Gap** between analytical surrogate models and real-world physical dynamics.
     - Formalization of hard real-time control deadlines (<50ms).
- **Strict Negative Boundaries & Forbidden Elements**:
  - ❌ **NO Novel Contributions or Proposals**: MUST NOT introduce or propose the dissertation's novel algorithms (\lr{RS-DRL}, \rsdrlplus, \sgos, \caepv, \pgalr). These belong strictly in Ch 4!
  - ❌ **NO Empirical Benchmark Results**: MUST NOT report experimental performance metrics, learning curves, or comparative outcomes (belongs strictly to Ch 5).
  - ❌ **NO Literature Critiques or Gap Analysis**: MUST NOT engage in comparative literature critiques (belongs strictly to Ch 3).

---

### 4.4 Chapter 3: پیشینه پژوهش و کارهای مرتبط (Critical Synthesis & Literature Gap Analysis)

- **True Scientific Nature (ماهیت واقعی)**:
  The **Critical Gap Justification** chapter. It is an analytical, critical investigation of the state-of-the-art across 5 foundational dimensions, designed to scientifically prove the existence of the research gaps and justify why the proposed paradigm is mathematically and architecturally necessary.
- **Mandatory Inclusions & Scientific Responsibilities**:
  1. *Five Foundational Review Dimensions*:
     - Dimension 1: Runtime adaptation space management (ML-based pruning, online search, heuristic methods, runtime RL).
     - Dimension 2: Advanced reinforcement learning (exploration strategies, reward shaping, hindsight experience replay \lr{HER}).
     - Dimension 3: Mathematical analysis of why \lr{HER} fundamentally fails in threshold-based constrained environments.
     - Dimension 4: Formal verification at runtime (\lr{ActivFORMS}, statistical model checking, probabilistic model checking).
     - Dimension 5: Safety shields, surrogate models, and anytime verification in cyber-physical systems.
  2. *Failure Modes & Scientific Dilemmas*: Detailed analysis of state explosion, verification latency bottlenecks (>100ms vs. hard deadlines), reality gap collapse of static shields, and failure data imbalance in operational logs.
  3. *Master Literature Synthesis Matrix (Table 3.1)*: Comprehensive comparative matrix evaluating dozens of seminal baselines across adaptation latency, formal guarantees, scalability, and reality gap resilience.
  4. *Formal Tripartite Research Gap Formulation*: Rigorous synthesis establishing the exact academic niche and theoretical imperative of \lr{RS-DRL} / \rsdrlplus.
- **Strict Negative Boundaries & Forbidden Elements**:
  - ❌ **NO Passive Summaries**: Must never read like a textbook survey or passive annotated bibliography; every paragraph must critically evaluate limitations.
  - ❌ **NO Proposed Algorithm Details**: MUST NOT disclose the internal algorithmic steps, neural loss equations, or formal proofs of Chapter 4.
  - ❌ **NO Thesis Experimental Data**: MUST NOT report the thesis's empirical results.

---

### 4.5 Chapter 4: روش پیشنهادی و معماری دوسطحی (Generic Methodology, RS-DRL / RS-DRL+ Architecture & Formal Proofs)

- **True Scientific Nature (ماهیت واقعی)**:
  The **Intellectual Heart & Generic Theoretical Contribution** chapter. It contains the formal algorithmic contributions, software architectural design patterns, mathematical formulations, and formal proofs of the dissertation.
- **Mandatory Inclusions & Scientific Responsibilities**:
  1. *Tier 1: Baseline \lr{RS-DRL} Framework*:
     - Architectural integration with MAPE-K control loops (Monitor, Analyze, Plan, Execute).
     - Asynchronous runtime verification with \lr{UPPAAL-SMC} in a decoupled, non-blocking background thread.
     - Stochastic Reward Shaping mechanism: mathematical formulation of $R_{shaped}(s, a, s')$, escaping local optima via shaping factor $\rho$.
     - Formal bound on SMC sample size via Chernoff-Hoeffding bounds.
     - **Universal Replay Buffer Storage ($r=0$) Rigor**: Both successful transitions ($r=1$) and failed transitions ($r=0$) are stored in $\mathcal{D}$. Never state or imply that failed transitions are discarded.
  2. *Tier 2: Advanced \rsdrlplus Architecture*:
     - Architectural resolution of the Planning Trilemma for safety-critical real-time CPS.
     - Pattern 1: Specification-Guided Offline Synthesis (\sgos) comprising Margin-Utility Reward Shaping (\mursdrl) with multi-constraint recovery margin $\mathcal{M}(s, a)$ and Constraint-Margin Replay Buffering (\cmrsdrl).
     - Pattern 2: Contract-Anytime Elastic Policy Verification (\caepv) comprising the Policy-Guided Anytime Local Repair (\pgalr) module and TreeSHAP sensitivity subspace restriction.
  3. *Formal Propositions & Mathematical Proofs*:
     - **Proposition 1**: Formal time complexity proof $\mathcal{O}(m \cdot K)$ and candidate set cardinality bound $|\mathcal{N}(a_0)| \le 2m + 1$.
     - **Proposition / Theorem 2**: Guarded selection rule and formal safety non-degradation guarantee (monotonic safety non-reduction).
  4. *Comprehensive Unified Pseudocodes*: Complete algorithms for offline policy synthesis and anytime online decision-making.
- **Strict Negative Boundaries & Prohibitions (Crucial Rules)**:
  - ❌ **STRICT DOMAIN-AGNOSTICISM RULE**:
    - **Chapter 4 MUST remain 100% generic and domain-agnostic.**
    - Specific empirical testbed details (e.g., DeltaIoT node counts, network topologies, DARTSim flight aerodynamics, UAV radar radii, battery voltages) belong exclusively in Chapter 2 and Chapter 5, **NEVER in Chapter 4**!
    - Formulations must rely strictly on abstract mathematical entities: state space $\mathcal{S}$, action space $\mathcal{A}$, latency budget $T_{budget}$, constraints $C_j(s, a) \le 0$, etc.
    - **Purge Domain-Specific Descriptors (`ناوگان`, `پروازی`, `هوایی`) from General Problem Formulations**: Do not embed words like `پروازی` or `ناوگان` into foundational challenge definitions (use `مهلت‌های زمانی سخت در حلقه‌های کنترل فیزیکی` instead of `مهلت‌های سخت پروازی`). Testbeds like \lr{DARTSim} must function strictly as tangible parenthetical examples (e.g. `(که ناوبری خودگردان در بستر \lr{DARTSim} نمونه‌ای ملموس از آن است)`), never as the problem definition itself. Avoid `ناوگان` (fleet) when referring to single-agent tactical UAV benchmark missions to prevent confusing readers with multi-agent fleet coordination.
  - ❌ **NO Inlined Code Function Names in Flowing Prose**:
    - Never insert raw code-level function signatures with underscores (e.g. `$SMC\_Verify(s, a)$`) into flowing Persian prose.
    - Refer in prose to the formal mathematical signal: `ادغام سیگنال اعتبارسنجی صوری ($r_{smc}$) مبتنی بر ابزار...`.
    - Reserve procedural calls strictly for pseudocode algorithm environments: `\STATE $r_{smc} \leftarrow SMC\_Verify(s, a)$`.
  - ❌ **NO Empirical Benchmark Tables or Evaluation Graphs**: Keep all experimental data, curves, and comparative metrics in Chapter 5.

---

### 4.6 Chapter 5: ارزیابی تجربی و تحلیل نتایج (Empirical Proof, Benchmark Evaluation & Statistical Validation)

- **True Scientific Nature (ماهیت واقعی)**:
  The **Empirical Proof & Benchmark Validation** chapter. It maps the generic algorithms from Chapter 4 onto the formal models from Chapter 2, executes massive simulations, benchmarks against competitive baselines, performs ablation studies, and conducts rigorous non-parametric statistical hypothesis tests to definitively answer \lr{RQ1} through \lr{RQ6}.
- **Mandatory Inclusions & Scientific Responsibilities**:
  1. *Experimental Setup & Calibration*: Hardware/software specifications, hyperparameter tuning, empirical trace descriptions.
  2. *Baseline Methods*: Detailed description of comparative baselines (\lr{ActivFORMS}, Q-Learning, PLA, DRL-Baseline, Static Shield).
  3. *QoS & Learning Metrics*: Quantitative tracking of packet loss, latency, energy, flight survival rate, corridor violations, decision variance, and real-time inference latency ($0.485\,\text{ms}$).
  4. *Part 1: DeltaIoT Empirical Benchmarks (\lr{RS-DRL})*:
     - Learning curves, convergence, and local optima escape (\lr{RQ1}).
     - Multi-objective trade-offs and generalization (\lr{RQ1}, \lr{RQ2}).
     - Comparative benchmarks against 6 baselines (\lr{RQ4}) --- 23.22% packet loss reduction, 39.07% latency reduction.
     - Ablation study on shaping factor $\rho$ (\lr{RQ2}).
     - Scalability analysis in large adaptation spaces up to 4,096 options (\lr{RQ3}).
  5. *Part 2: DARTSim CPS UAV Fleet Benchmarks (\rsdrlplus)*:
     - 2,000 closed-loop physical 6-DOF flights across 200 adversarial tactical scenarios.
     - Taming the Reality Gap: survival rate boosted to 70.5% (vs. 65.0% for traditional safety shields) (\lr{RQ6}).
     - Multi-level corridor tolerance analysis ($v_1, v_2, v_3$) (\lr{RQ1}, \lr{RQ6}).
     - Mission utility and 31% decision variance reduction under failure logs (\lr{RQ6}, \lr{RQ2}).
     - Real-time latency compliance: sub-3.5ms worst-case latency, $0.485\,\text{ms}$ nominal latency (<50ms flight control deadline) (\lr{RQ5}).
     - Offline training overhead amortization ($5.2$ hours training amortized rapidly) (\lr{RQ4}).
     - Ablation study on sensitivity subspace dimension $m$ (\lr{RQ3}, \lr{RQ5}, \lr{RQ6}).
  6. *Part 3: Cross-Domain Transferability to DeltaIoT* (\lr{RQ2}, \lr{RQ3}, \lr{RQ6}).
  7. *Part 4: Comprehensive Non-Parametric Statistical Hypothesis Testing*:
     - Wilcoxon signed-rank tests ($p < 0.001$).
     - Cohen's $d$ effect sizes (large effect $> 0.8$).
     - Holm-Bonferroni family-wise error rate (\lr{FWER}) corrections for \lr{RQ1}--\lr{RQ6}.
- **Strict Negative Boundaries & Forbidden Elements**:
  - ❌ **NO Mathematical Re-derivations**: Do not re-derive the theoretical formulas or proofs established in Chapter 4.
  - ❌ **NO Unsupported Claims**: Every empirical assertion must be backed by a table, figure, or statistical p-value/effect size.
  - ❌ **NO Missing Baseline Context**: Never report numbers in isolation without direct comparison to established baselines.

---

### 4.7 Chapter 6: بحث، نتیجه‌گیری و کارهای آتی (Scholarly Reflection, Threats to Validity & Future Horizons)

- **True Scientific Nature (ماهیت واقعی)**:
  The **Scholarly Synthesis, Critical Reflection & Horizon** chapter. It steps back from empirical details to provide high-level scientific reflection, theorizes why the proposed architecture functions fundamentally, examines software engineering trade-offs, transparently analyzes threats to validity, and articulates three concrete future research directions.
- **Mandatory Inclusions & Scientific Responsibilities**:
  1. *Mechanistic Theorization*: Deep theoretical explanation of *why* \lr{RS-DRL} and sensitivity-bounded repair work (information-theoretic and optimization perspectives).
  2. *Multi-objective Engineering Trade-offs*: Pareto trade-offs between safety, performance, energy, and execution latency.
  3. *Software Engineering Implications*: Architectural guidelines for software engineers developing adaptive CPS.
  4. *Four-Dimensional Threats to Validity*:
     - Internal Validity: Hyperparameter sensitivity, simulator fidelity, stochastic variance.
     - External Validity: Generalizability across CPS domains, robotics, sensor networks, autonomous vehicles.
     - Construct Validity: Alignment between formal specifications and real-world system goals.
     - Conclusion Validity: Statistical power, sample size bounds, effect sizes.
  5. *Three Concrete Future Research Horizons*:
     - Horizon 1: Multi-Agent Reinforcement Learning (\lr{MARL}) in asymmetric decentralized networks.
     - Horizon 2: Continual / Lifelong Learning for non-stationary CPS environments.
     - Horizon 3: Generalization of contract-anytime repair to infinite continuous action spaces.
  6. *Final Dissertation Synthesis*: Authoritative concluding summary confirming the resolution of the research contract.
- **Strict Negative Boundaries & Forbidden Elements**:
  - ❌ **NO New Empirical Data or Benchmark Plots**: Strictly prohibited from introducing new experimental figures, raw numbers, or evaluation tables not presented in Chapter 5.
  - ❌ **NO Algorithm Re-derivations**: Do not repeat algorithm steps or proof lemmas from Chapter 4.
  - ❌ **NO Superficial Summaries**: Must not be a shallow cut-and-paste summary; must provide elevated scholarly reflection.

---

### 4.8 Appendices (پیوست‌ها): Exhaustive Workflows, Extended Data & Reproducibility Package

- **True Scientific Nature (ماهیت واقعی)**:
  The **Reproducibility & Exhaustive Evidence Repository**. It houses materials that are essential for 100% reproducibility and completeness, but whose inclusion in the main chapters would disrupt the narrative cadence.
- **Mandatory Inclusions**:
  1. *Appendix A*: Full UML activity diagrams and complete process workflows.
  2. *Appendix B*: Complete algorithmic pseudocode listings and full procedural definitions.
  3. *Appendix C*: Extended raw benchmark logs, comprehensive evaluation tables, and full parameter sheets.
  4. *Appendix D*: Software artifact package, Docker setup, and open science reproduction instructions.
- **Strict Negative Boundaries**:
  - ❌ Must not contain primary architectural contributions or critical proofs (must remain in Chapter 4).
  - ❌ Must not contain primary empirical answers to \lr{RQ1}--\lr{RQ6} (must remain in Chapter 5).

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
- Avoid elongated, breathless titles loaded with buzzwords, stacked structural nouns (e.g., ❌ `معماری کلان چارچوب پایه‌ای ...`), or stiff relational calques (e.g., ❌ `اصول فرآیندی انطباق`).
- Example: Use `بیان مساله` instead of elongated multi-clause titles, and `معماری سطح بالای \lr{RS-DRL} و تفکیک زمانی فرآیند انطباق` instead of stacked framework/architecture phrasing.

---

## 6. LaTeX, XePersian & BiDi Typography Guidelines

### 6.1 Table Width & Margin Overflow Prevention
- Tables must NEVER overflow text margins.
- Always use explicit, bounded column widths:
  ```latex
  \begin{tabular}{|p{2.5cm}|p{6.0cm}|p{5.1cm}|}
  ```
- Use `\small` or `\footnotesize` font scaling within tables to maintain balanced vertical and horizontal spacing.

### 6.2 BiDi Layout, Persian Numerals & Macro Spacing
- **Math-Mode BiDi Rule for Decimals, Fractions & Thousands**: Under XePersian's TeX--XeT RTL engine, bare Persian numbers containing slashes (`/`), decimals, or thousands commas (`،`) reverse digit/segment order in output (e.g., `۱۳۷/۲۰۰` renders as `۲۰۰/۱۳۷`; `۷۰/۵٪` renders as `۵/۷۰٪`). Always typeset decimals, ratios/fractions, thousands-separated numbers, signed decibels, and millisecond metrics in math mode (`$70.5\%$`, `$137/200$`, `$2{,}000$`, `$-40\,\text{dB}$`, `$+15\,\text{dB}$`, `$200\,\text{ms}$`) with thin space `\,` before `\text{ms}` and `\text{dB}` so `\setdigitfont{XB Niloofar}` renders Persian digits in strict LTR order.
- **Heading Safety with `\texorpdfstring`**: Wrap math expressions (`$\rho$`, `$2{,}000$`) and custom algorithm macros or mixed-script RQ tags inside `\section`, `\subsection`, and `\subsubsection` with `\texorpdfstring{<TeX>}{<PDF bookmark text>}` to guarantee `0` hyperref token warnings.
- **Custom Macro Spacing (`xspace`)**: `commands.tex` loads `\usepackage{xspace}` with `\xspaceaddexceptions{، ؛ » \footnote \LTRfootnote ^^^^200c}` and trailing `\xspace` on custom macros (`\rsdrlplus`, `\sgos`, `\caepv`, `\pgalr`, `\mursdrl`, `\cmrsdrl`) so macros insert automatic spacing before Persian prose without adding unwanted spaces before punctuation, ZWNJ (`^^^^200c`), or footnotes.
- **Research Question Numbering**: Numbers must follow the English label properly (`زیرسؤال ۱-۱`, `RQ1`).
- **Punctuation & Parentheses**: Wrap all Latin terms in `\lr{...}` to prevent reversed parentheses or flipped intervals (while keeping `\ref` and `\cite` outside `\lr{...}`).

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
- `Hyperref warnings: 0`
- `Total Overfull \hbox: 39`, with `Overfull \hbox > 10pt: 0` (max overfull strictly bounded under 10pt; verified baseline: `9.51541 pt` / $9.52\,\text{pt}$).
- `Total PDF pages: 165` (verified baseline after BiDi math-mode fixes, heading `\texorpdfstring` wrapping, citation normalization, and scholarly/terminology `\LTRfootnote` / `\footnote` additions across Chapters 1–6; preserve layout without accidental page drift).

### 6.5 Strict Ban on Wrapping Cross-References in `\lr{...}`
- **NEVER** wrap cross-references in `\lr{...}` (e.g. ❌ `\lr{\ref{fig:...}}`, ❌ `\lr{\ref{tab:...}}`).
- Wrapping `\ref` inside `\lr{...}` deactivates `\AutoPersianDigits` and forces the Latin font (`Times New Roman`), rendering reference numbers in English ASCII digits (`4-5`), which severely clashes with Persian citations (`[۲]`) and surrounding Persian text.
- XePersian natively handles multi-level counter delimiters via `\SepMark{-}` in `commands.tex`. All cross-references must remain bare: `شکل \ref{fig:...}`, `جدول \ref{tab:...}`, `بخش \ref{sec:...}`.

### 6.6 Numeral & Quantitative Measurement Consistency Protocol
- **Quantitative Units & Latencies**: Never wrap metrics and units in casual `\lr{...}` (e.g. ❌ `\lr{0.1ms}`, ❌ `\lr{0.05ms}`). Use uniform math mode with thin space: `$0.1\,\text{ms}$`, `$0.05\,\text{ms}$`, `$0.3\,\text{ms}$` (or write explicitly in Persian: `۰٫۱ میلی‌ثانیه`).
- **Matrix / Map Dimensions in Tables**: Typeset dimensions in math mode (e.g. `$40 \times 1$`, `$50 \times 50$`), avoiding mixed `\lr{40$\times$1}` in tables containing Persian counts.
- **Latin Acronyms & Model Designators**: Proper Latin identifiers (`\lr{RQ1}`–`\lr{RQ6}`, `\lr{6-DOF}`, `\lr{5G}`, `\lr{DeltaIoTv1}`, `\lr{v1.1}`, `\lr{TreeSHAP}`) legitimately retain English digits and must remain enclosed in `\lr{...}`.
- **Citation Numbering**: In-text citations `\cite{...}` in Persian paragraphs naturally render with Persian numerals (`[۲]`), whereas the English bibliography list (`thebibliography`) retains Latin numerals (`[2]`). Never force `\cite` into `\lr{\cite{...}}`.

### 6.7 English Parentheticals, Acronyms & Footnote Convention
- **Prose Non-Acronym English Terms**: Do **not** leave inline English translations/phrases inside parentheses (`(\lr{...})`). Move non-acronym English equivalents (e.g., `\LTRfootnote{Backpropagation}`, `\LTRfootnote{Mini-batches}`, `\LTRfootnote{Critical Path}`) to `\LTRfootnote{...}` on their **first mention per chapter**, and omit parenthetical repeats within the same chapter.
- **Active Uppercase Acronyms**: Short uppercase acronyms reused directly in subsequent prose (e.g., `MDP`, `DRL`, `DQN`, `MAPE-K`, `QoS`, `CPS`, `SAS`, `SMC`, `PBRS`, `FWER`) keep `(\lr{ACRONYM})\LTRfootnote{Full Expansion}` **only on their first chapter mention**; strip duplicate `(\lr{ACRONYM})` parentheticals on later mentions in that chapter.
- **Headings & Captions**: Never place `\LTRfootnote` inside `\section`, `\subsection`, `\subsubsection`, `\paragraph`, or `\caption`, and strip non-acronym English parentheticals from titles/captions (placing `\LTRfootnote{...}` on the first prose mention immediately beneath when needed). Only essential short identifiers (e.g., `\lr{RQ1}`, `\lr{DARTSim}`, `\lr{DeltaIoT}`, `\lr{DQN}`, `\lr{UPPAAL-SMC}`) may appear in headings.
- **Tables & Appositives**: Keep compact English tags inside `tabular` environments untouched (`\LTRfootnote` fails inside `tabular`/`\resizebox`). Rewrite appositive proper nouns in prose without parentheses (e.g., `در شبکه حسگر \lr{DeltaIoT}`), keep version/experiment tags (`(\lr{v1})`, `(\lr{RQ1} تا \lr{RQ6})`, `(\lr{6-DOF C++})`), and never nest `\LTRfootnote` inside `\footnote`.
- **Official Tool URLs & Foreign Authors**: Place `\LTRfootnote{First Last [et al.]}` for foreign author names and `\footnote{<short Persian label>: \lr{\url{...}}}` for primary open-source tools/benchmarks (`DeltaIoT`, `DARTSim`, `UPPAAL-SMC`, `Gymnasium`, `Stable-Baselines3`, `SHAP`) on first chapter mention, keeping URL footnote prefixes concise so URLs stay single-line.

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
