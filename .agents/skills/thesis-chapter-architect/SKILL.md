---
name: thesis-chapter-architect
description: >-
  Enforces chapter-by-chapter epistemological scopes, negative boundaries, input/output contracts, and guides authoring the unwritten sections and appendices of the doctoral dissertation. Use when writing, expanding, or reviewing any specific chapter (Chapters 1-6) or the appendices (Appendices A-D).
---

# Dissertation Chapter Architecture & Boundary Enforcement Skill

This skill governs the epistemological scope, scientific deliverables, negative boundaries, and inter-chapter progression across all chapters of the doctoral dissertation.

## Chapter Responsibilities & Strict Negative Boundaries

| Chapter | Title & Scope | Scientific Deliverable | Strict Negative Boundaries |
| :--- | :--- | :--- | :--- |
| **فصل ۱** | کلیات و تبیین مسئله | Problem Formulation, Trilemma, Sub-problems 1--3, Research Questions \lr{RQ1}--\lr{RQ6}, 6 Core Innovations, Alignment Matrix. | ❌ NO code, NO mathematical proofs, NO empirical result tables, NO physical domain equations. |
| **فصل ۲** | مبانی نظری و مدل‌سازی سیستم | Mathematical Foundations (MDP, DRL, SMC, MAPE-K), Ground Truth Physics & Testbeds (DeltaIoT, DARTSim), NP-Hardness Proof. | ❌ NO novel contributions/algorithms (no \lr{RS-DRL}, \rsdrlplus, \sgos, \caepv), NO empirical results, NO literature critiques. |
| **فصل ۳** | پیشینه پژوهش و کارهای مرتبط | 5-Dimensional Critical Taxonomy, Literature Synthesis Matrix (Table 3.1), Tripartite Research Gap. | ❌ NO passive summaries, NO proposed algorithm details, NO thesis experimental data. |
| **فصل ۴** | روش پیشنهادی و معماری دوسطحی | Generic Methodology, Software Architecture, Patterns \sgos & \caepv (\pgalr), Formal Proofs (Propositions 1 and 2). | ❌ **100% DOMAIN-AGNOSTIC**: NO testbed-specific numbers in definitions, NO inlined code function names in prose, NO empirical benchmark data. |
| **فصل ۵** | ارزیابی تجربی و تحلیل نتایج | DeltaIoT & DARTSim benchmarks, 2,000 physical flights, ablation studies, non-parametric statistical tests (\lr{RQ1}--\lr{RQ6}). | ❌ NO mathematical re-derivations, NO unsupported assertions, NO missing baselines. |
| **فصل ۶** | بحث، نتیجه‌گیری و کارهای آتی | Mechanistic theorization ("Why it works"), Pareto trade-offs, 4-dimensional validity analysis, 3 future research horizons. | ❌ NO new empirical figures/tables, NO algorithm re-derivations, NO superficial summaries. |
| **پیوست‌ها** | پیوست‌ها و ضمائم | Appendix A: Complete UML Workflows<br>Appendix B: Algorithmic Pseudocodes<br>Appendix C: Extended Raw Benchmarks<br>Appendix D: Reproducibility Package. | ❌ NO primary architectural contributions or primary answers to RQs. |

For the full architectural contracts and detailed negative boundaries, consult [chapter_boundaries.md](./references/chapter_boundaries.md).

---

## Authoring Guidelines for Missing Sections in `thesis_full_toc_persian_v3.tex`

1. **Appendices (`chapters/appendices.tex`)**:
   - Currently, Appendices A through D only contain chapter headings.
   - When writing Appendix A, include the complete UML activity diagrams and swimlane workflows.
   - When writing Appendix B, include full algorithmic listings for RS-DRL, RS-DRL+, SG-OS, and CA-EPV / PG-ALR.
   - When writing Appendix C, include full parameter catalog tables and extended per-seed benchmark tables.
   - When writing Appendix D, provide complete Docker instructions, Gymnasium environment interfaces, and UPPAAL-SMC model details.
2. **Front Matter**:
   - Ensure supervisor, advisor, and committee names are properly placed once provided.

