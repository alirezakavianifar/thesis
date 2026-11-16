---
name: thesis-scholarly-writing
description: >-
  Audits, refines, and humanizes academic Persian prose for the doctoral dissertation. Use when drafting or polishing thesis sections, eliminating AI hype words, conversational fillers, or empty rhetorical padding, and converting bullet lists into scholarly narrative paragraphs (Anti-Bullet Fatigue).
---

# Doctoral Scholarly Writing & Humanization Skill

This skill enforces high-impact doctoral prose standards modeled after top European and North American computer software engineering dissertations (e.g. Dr. Omid Gheibi, KU Leuven).

## Scholarly Prose Guidelines

### 1. Reader-Centricity & Cognitive Cadence
- Evaluate modified prose from the perspective of a rigorous external doctoral examiner.
- If a sentence is long, convoluted, breathy, or causes excessive cognitive load, break it down into clean, balanced declarative clauses.
- Use natural sentence cadence and authoritative academic Persian.

### 2. Elimination of AI Hype Words & Promotional Rhetoric
Scholarly authority stems from mathematical proof and empirical benchmarks, never promotional rhetoric.
- ❌ **100% Strictly Purged**:
  - `نوین` $\rightarrow$ Use `پیشنهادی`, `مدرن`, `پیشرفته`, or `جدید`.
  - `انقلابی`, `شگفت‌انگیز`, `دگرگون‌ساز`.
  - `چشمگیر` $\rightarrow$ Use `به طور قابل‌ملاحظه‌ای`, `شدید`, or report exact quantitative deltas ($23.22\%$).
  - `فوق‌العاده` $\rightarrow$ Use `با رواداری محدود`, `بسیار باریک`, or state the quantitative bound.
  - Casual prefix `فوق` (`فوق‌سریع`, `فوق‌العاده`).

### 3. Elimination of Conversational Fillers & Rhetorical Padding
Strip away conversational throat-clearing:
- ❌ **Banned Fillers**:
  - `شایان ذکر است که`
  - `لازم به یادآوری است که`
  - `بدیهی است که`
  - `همان‌طور که می‌دانیم`
  - `نکته جالب توجه این است که`
- ✔️ **Approved**: Direct, assertive declarative sentences.

### 4. Elimination of Redundant Calques & Stiff Pseudo-Philosophy
- ❌ Do NOT add `استاندارد` casually (e.g. `یادگیری تقویتی عمیق استاندارد` $\rightarrow$ `یادگیری تقویتی عمیق`).
- ❌ Avoid opaque, pseudo-philosophical calques such as `چرایی ناکارآمدی رویکردهای یکنواخت پیشین` (use `سنتی` or `تک‌سطحی`).
- ❌ Avoid artificial rhetorical qualifiers such as `موازنه عمیق` or `پیچیدگی عمیق` (use `برقراری موازنه` or `موازنه چندمعیاره/دقیق`).

### 5. The Anti-Bullet Fatigue Protocol
- Do NOT use fragmented `itemize` / `enumerate` bullet lists for standard expository paragraphs, taxonomies, or walkthroughs.
- Convert descriptive lists into flowing narrative paragraphs structured with bold inline headings: `\paragraph{عنوان مشخص:}`.
- Bullet and enumerated lists are **strictly reserved** for:
  1. Formal Research Questions (`RQ1` to `RQ6`).
  2. Core Architectural Innovations (Innovation 1 to 6).
  3. Formal mathematical induction and proof steps (Propositions 1 & 2).
  4. Formal baseline algorithm taxonomies and empirical threats to validity.

---

## Automated Prose Audit Runbook

To scan for banned hype words, fillers, and bullet list density:
```powershell
python .agents/skills/thesis-scholarly-writing/scripts/audit_prose.py
```

