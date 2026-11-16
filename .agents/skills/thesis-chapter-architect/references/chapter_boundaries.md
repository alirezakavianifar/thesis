# Comprehensive Dissertation Chapter Boundaries & Architectural Matrix

This document codifies the mandatory input sources, core deliverables, and strict negative boundaries for every chapter of the doctoral dissertation.

## Epistemological Flowchart

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

---

## Detailed Chapter Specifications

### Chapter 1: کلیات و تبیین مسئله (Problem Formulation & Research Contract)
- **Mandatory Inclusions**:
  1. Industrial and physical CPS context; failure of traditional single-tier planners.
  2. Formal Planning Trilemma: large state-action space vs. hard real-time latency (<50ms) vs. physical safety / reality gap.
  3. Formal Sub-problems 1, 2, and 3.
  4. Research Questions \lr{RQ1} through \lr{RQ6}.
  5. 6 Core Innovations.
  6. Master Alignment Matrix (Table 1.1) mapping chapters, sub-problems, innovations, RQs, and published papers.
  7. Dense, single-paragraph PhD dissertation abstract without bullet points.
- **Strict Negative Boundaries**:
  - ❌ NO code, neural layer topologies, or procedural execution mechanics (belongs to Ch 4).
  - ❌ NO formal induction proofs or complexity lemmas (belongs to Ch 4).
  - ❌ NO empirical benchmark tables or learning curves (belongs to Ch 5).
  - ❌ NO physical domain equations (belongs to Ch 2).

---

### Chapter 2: مبانی نظری و مدل‌سازی سیستم (Theoretical Foundations & Formal Domain Modeling)
- **Mandatory Inclusions**:
  1. Closed-loop MAPE-K autonomic control architecture; taxonomy of uncertainty.
  2. MDP tuple $(S, A, P, R, \gamma)$, Bellman equations, and DQN.
  3. Case Study 1 (DeltaIoT): DAG topology, radio channel propagation, SNR, packet loss, energy, NP-hardness proof.
  4. Case Study 2 (DARTSim): 6-DOF UAV kinematics, corridor tolerances ($v_1, v_2, v_3$), radar models, battery discharge, reality gap definition, hard real-time deadline (<50ms).
- **Strict Negative Boundaries**:
  - ❌ NO novel contributions/algorithms (\lr{RS-DRL}, \rsdrlplus, \sgos, \caepv, \pgalr).
  - ❌ NO empirical benchmark results or curves.
  - ❌ NO comparative literature critiques (belongs to Ch 3).

---

### Chapter 3: پیشینه پژوهش و کارهای مرتبط (Critical Synthesis & Literature Gap Analysis)
- **Mandatory Inclusions**:
  1. 5 foundational review dimensions: adaptation space reduction, advanced RL (exploration, shaping, HER), HER failure analysis in threshold spaces, runtime formal verification (ActivFORMS, SMC, PMC), safety shields and anytime verification.
  2. Detailed analysis of state explosion, verification latency bottlenecks (>100ms vs. hard deadlines), reality gap collapse of static shields, failure data imbalance in operational logs.
  3. Comparative Literature Synthesis Matrix (Table 3.1).
  4. Formal Tripartite Research Gap formulation.
- **Strict Negative Boundaries**:
  - ❌ NO passive textbook summaries.
  - ❌ NO proposed algorithm mechanics or neural loss formulas.
  - ❌ NO thesis empirical benchmark data.

---

### Chapter 4: روش پیشنهادی و معماری دوسطحی (Generic Methodology, Architecture & Formal Proofs)
- **Mandatory Inclusions**:
  1. Tier 1: Baseline \lr{RS-DRL} framework, MAPE-K integration, asynchronous UPPAAL-SMC verification, stochastic reward shaping $R_{shaped}(s, a, s')$, Chernoff-Hoeffding sample bounds.
  2. **Universal Replay Buffer Storage ($r=0$) Rigor**: Both successful ($r=1$) and failed transitions ($r=0$) are stored in $\mathcal{D}$.
  3. Tier 2: Advanced \rsdrlplus architecture, Pattern 1 (\sgos, \mursdrl, \cmrsdrl), Pattern 2 (\caepv, \pgalr, TreeSHAP subspace restriction).
  4. Formal Propositions:
     - Proposition 1: Time complexity $\mathcal{O}(m \cdot K)$, candidate bound $|\mathcal{N}(a_0)| \le 2m + 1$.
     - Proposition 2: Guarded selection rule, monotonic safety preservation in surrogate space, bounded reality gap physical error ($\epsilon_{\max}$).
  5. Comprehensive unified pseudocodes for offline policy synthesis and anytime online decision-making.
- **Strict Negative Boundaries**:
  - ❌ **STRICT DOMAIN-AGNOSTICISM RULE**:
    - Chapter 4 must remain 100% domain-agnostic.
    - Testbed details (DeltaIoT node counts, topologies, DARTSim flight parameters) belong exclusively in Ch 2 & 5!
    - Rely strictly on abstract mathematical entities ($\mathcal{S}$, $\mathcal{A}$, $T_{budget}$, $C_j(s, a) \le 0$).
    - Do NOT embed words like `پروازی` or `ناوگان` into foundational challenge definitions.
  - ❌ NO inlined code function names in prose (e.g. `$SMC\_Verify(s, a)$`). Use formal mathematical symbols ($r_{smc}$).
  - ❌ NO empirical benchmark tables or curves.

---

### Chapter 5: ارزیابی تجربی و تحلیل نتایج (Empirical Proof & Statistical Validation)
- **Mandatory Inclusions**:
  1. Experimental setup, hardware/software specs, hyperparameter calibration, empirical trace descriptions.
  2. Baseline descriptions (ActivFORMS, Q-Learning, PLA, DRL-Baseline, Static Shield).
  3. Part 1: DeltaIoT empirical benchmarks (\lr{RS-DRL}) answering \lr{RQ1}, \lr{RQ2}, \lr{RQ4}.
  4. Part 2: DARTSim CPS UAV benchmarks (\rsdrlplus) answering \lr{RQ1}, \lr{RQ2}, \lr{RQ3}, \lr{RQ5}, \lr{RQ6} (2,000 flights, 70.5% survival rate, $0.485\,\text{ms}$ latency).
  5. Part 3: Cross-domain transferability to DeltaIoT.
  6. Part 4: Comprehensive non-parametric statistical hypothesis testing (Wilcoxon tests $p < 0.001$, Cohen's $d > 0.8$, Holm-Bonferroni FWER corrections).
- **Strict Negative Boundaries**:
  - ❌ NO mathematical re-derivations of Ch 4 formulas.
  - ❌ NO unsupported claims without an explicit table, figure, or p-value.
  - ❌ NO isolated numbers without baseline comparison.

---

### Chapter 6: بحث، نتیجه‌گیری و کارهای آتی (Scholarly Reflection, Validity Threats & Horizons)
- **Mandatory Inclusions**:
  1. Mechanistic theorization: information-theoretic and optimization perspective on *why* RS-DRL and sensitivity-bounded repair work.
  2. Pareto trade-offs between safety, performance, energy, and latency.
  3. Software engineering guidelines for adaptive CPS practitioners.
  4. 4-dimensional threats to validity: internal, external, construct, and conclusion.
  5. 3 concrete future research horizons: MARL in decentralized networks, continual lifelong learning, and generalization to infinite continuous action spaces.
  6. Authoritative concluding synthesis confirming resolution of the research contract.
- **Strict Negative Boundaries**:
  - ❌ NO new empirical figures, raw numbers, or evaluation tables.
  - ❌ NO algorithm re-derivations.
  - ❌ NO superficial summaries.

---

### Appendices (پیوست‌ها): Reproducibility Package & Exhaustive Artifacts
- **Mandatory Inclusions**:
  - Appendix A: Full UML activity diagrams and complete process workflows.
  - Appendix B: Complete algorithmic pseudocode listings and full procedural definitions.
  - Appendix C: Extended raw benchmark logs, parameter sheets, and comprehensive tables.
  - Appendix D: Software artifact package, Docker setup, and open science reproduction instructions.
- **Strict Negative Boundaries**:
  - ❌ Must not contain primary architectural contributions or critical proofs.
  - ❌ Must not contain primary empirical answers to \lr{RQ1}--\lr{RQ6}.

