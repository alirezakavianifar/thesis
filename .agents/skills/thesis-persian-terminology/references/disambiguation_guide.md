# Persian Academic Terminology Disambiguation & Arbitration Guide

This guide establishes the epistemological criteria for evaluating polysemous, domain-sensitive, or controversial terminology in the doctoral dissertation.

---

## 1. Disambiguation Protocol: «سنتز» vs. Equivalents

The term **سنتز** (*Synthesis*) possesses multiple distinct technical meanings across computer software engineering, formal verification, machine learning, and general academic exposition. It MUST NOT be arbitrarily replaced with a single catch-all word.

### Categorization & Mandatory Usage Rules

| Context & Academic Construct | English Equivalent | Mandatory Persian Term | Strictly Prohibited / Avoided | Technical Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Formal Synthesis / Controller / Policy Synthesis** | *Controller Synthesis*, *Policy Synthesis*, *Reactive Synthesis*, *Program Synthesis* | **`سنتز کنترل‌کننده`** / **`سنتز خط‌مشی / سیاست`** / **`سنتز صوری`** | ❌ `تولید کنترل‌کننده`, `ترکیب خط‌مشی`, `یکپارچه‌سازی صوری` | In formal methods, control theory, and automated software engineering, *Synthesis* specifically refers to the constructive algorithm generating an artifact that formally satisfies a temporal logic / quantitative specification ($\mathcal{M} \models \phi$). |
| **Architectural Pattern Name** | *Specification-Guided Offline Synthesis* (\sgos) | **`الگوی سنتز غیربرخط سیاست با هدایت مشخصه‌ها (\sgos)`** | ❌ Altering the canonical pattern name | Formal design pattern introduced as core Innovation 2 in the dissertation. |
| **Literature / Findings Synthesis** | *Research Synthesis*, *Evidence Synthesis*, *Synthesis Matrix* | **`تلفیق نتایج`** / **`سنتز جامع یافته‌ها`** | ❌ `سنتز ادبیات` (unqualified) | In Chapter 3 and Chapter 6, when synthesizing disparate empirical literature or multi-RQ conclusions, prefer **`تلفیق و جمع‌بندی جامع`** or keep **`سنتز جامع یافته‌ها`** where meta-synthesis is intended. |
| **Component / Service Composition** | *Service Composition*, *Component Composition* | **`ترکیب مؤلفه‌ها`** / **`ترکیب‌بندی معماری`** | ❌ `سنتز مؤلفه‌ها` | Putting pre-existing components together is *Composition* (`ترکیب / ترکیب‌بندی`), not *Synthesis*. |
| **Data / Information Fusion** | *Data Fusion*, *Sensor Fusion*, *Feature Synthesis* | **`تلفیق داده‌ها / تجمیع اطلاعات`** | ❌ `سنتز داده` | Combining multi-source sensory traces is *Fusion / Aggregation* (`تلفیق / تجمیع`), not *Synthesis*. |
| **System Integration** | *System Integration* | **`یکپارچه‌سازی سیستم`** | ❌ `سنتز سیستم` | Unifying disparate subsystems into an operational whole is *Integration* (`یکپارچه‌سازی`). |

---

## 2. Protocol for Other Nuanced Term Pairs

### 2.1 «استنتاج» vs «استنباط» vs «قیاس»
- **`استنتاج`** (*Inference / Deduction*): Direct algorithmic computation, forward pass, or rule deduction (e.g., `زمان استنتاج شبکه عمیق` $\rightarrow 0.485\,\text{ms}$, `موتور استنتاج صوری`).
- **`استنباط`** (*Abduction / Statistical Inference*): Probabilistic estimation from sample data (`استنباط آماری`).
- **`قیاس`** (*Analogy*): Comparing analogous systems.

### 2.2 «ترکیب» vs «ترکیب‌بندی» vs «تلفیق»
- **`ترکیب`** (*Combination*): Combining mathematical terms, weights, or objectives ($\alpha \cdot r_{\text{ext}} + \beta \cdot r_{\text{int}}$).
- **`ترکیب‌بندی`** (*Composition / Choreography*): Structural arrangement of microservices, patterns, or architectural layers.
- **`تلفیق`** (*Integration / Fusion*): Harmonious fusion of distinct paradigms (e.g., `تلفیق روش‌های صوری و یادگیری تقویتی`).

---

## 3. Automated Arbitration Workflow with Academic MCPs

When evaluating an unstandardized or disputed term:
1. **Local Context Extraction**: Run `extract_term_context.py` to extract all occurrences with surrounding lines.
2. **Academic Verification via MCP**:
   - Query `semantic_scholar_search_papers` using `s2-mcp-server` to inspect title/abstract usage in top-tier venues (ACM TOSEM, IEEE TSE, ICSE, CAV).
   - Query `arxiv-mcp-server` for current preprint conventions in `cs.SE` and `cs.AI`.
3. **Structured Reporting**: Produce the 5-column table (`Occurrence`, `Current Term`, `Context & Intended Meaning`, `Academic Evaluation`, `Recommended Alternative`).
4. **Codification**: Add the approved resolution to this guide and update `AGENTS.md`.
