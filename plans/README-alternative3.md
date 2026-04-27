# Alternative 3: Decomposed Figures for Cognitive Clarity

This document describes the third alternative structure for Chapter 5, created based on `plans/alternative_3.md` and the plan in `.cursor/plans/create_alternative_3_decomposed_figures_fe333d64.plan.md`. This version addresses cognitive overload from monolithic process-flow diagrams by decomposing them into smaller, section-specific figures.

## File Created

### `chapters/chapter5-alternative3.tex` and `chapters/chapter5-alternative3.pdf`
**Decomposed figure structure with perfect section-figure alignment**
- **Pages**: 20 pages
- **Focus**: One figure = one conceptual responsibility
- **Key principle**: Examiners consult figures, not study them

## Core Problem Addressed

### Issue: Monolithic Process-Flow Diagrams

Current versions contain long vertical process-flow diagrams (e.g., `monitoring-state-construction.pdf`) that:

- Cause cognitive overload for examiners
- Create misalignment between modular text and monolithic figures
- Force readers to decode complex flows while reading
- Break reading rhythm with excessive back-and-forth

### Solution: Decomposed Sectional Figures

Split monolithic diagrams into multiple focused figures:

- Each figure aligned with its corresponding section
- Short, readable, contextual diagrams in main chapter
- Full end-to-end workflow preserved in appendices

## Key Principle

> **One figure = one conceptual responsibility**

Not: "One figure = the whole pipeline"

## Structure Overview

### Section 5.1: Chapter Overview and Architectural Perspective
- Chapter scope and objectives
- Process-oriented organization with decomposed figures
- Architectural baseline

### Section 5.2: System-Level Self-Adaptation Loop
- Managed and managing system abstraction
- Continuous adaptation cycle (Stages 1-9)
- Separation of runtime and learning
- **Figure**: System-level process overview (high-level only)

### Section 5.3: Mapping to MAPE-K Reference Model
- Conceptual mapping to MAPE-K
- Role of RS-DRL within MAPE-K
- Temporal classification
- **Figure**: MAPE-K validation view

### Section 5.4: Runtime Monitoring and State Construction
**Decomposed into 3 focused figures:**

- **Figure 5.4.1**: Monitoring and Raw Data Acquisition
  - Shows: Raw data sources → Sensor Data → Initial collection
  - Excludes: Preprocessing, feature extraction (next figures)
  
- **Figure 5.4.2**: Data Preprocessing and Feature Extraction
  - Shows: Preprocessed Data → Feature Extractor → Feature categories
  - Excludes: Raw acquisition (previous), validation (next)
  
- **Figure 5.4.3**: State Vector Construction and Validation
  - Shows: Features → State Assembly → Validation → Validated State Vector
  - Excludes: Acquisition and preprocessing (previous figures)

- **Reference**: Complete monitoring workflow in Appendix A.1

### Section 5.5: Runtime Analysis and Adaptation Triggering
- Goal evaluation
- Adaptation triggering
- **Figure**: Analysis phase (focused, already appropriately sized)

### Section 5.6: Runtime Planning and Adaptation Option Prediction
**Decomposed into 2 focused figures:**

- **Figure 5.6.1**: Model Retrieval
  - Shows: Adaptation trigger → Knowledge access → Model retrieval
  - Excludes: Q-value evaluation (next)
  
- **Figure 5.6.2**: Adaptation Option Evaluation and Selection
  - Shows: State + Model → Q-value computation → Option selection
  - Excludes: Model retrieval (previous)

- **Reference**: Complete decision workflow in Appendix A.2

### Section 5.7: Adaptation Option Verification
**Decomposed into 3 focused figures:**

- **Figure 5.7.1**: Verification Trigger and Model Setup
  - Shows: Predicted option → Runtime model → Parameterization
  - Excludes: SMC execution (next)
  
- **Figure 5.7.2**: Statistical Model Checking Execution
  - Shows: Parameterized model → UPPAAL-SMC → Simulation results
  - Excludes: Model setup (previous), quality extraction (next)
  
- **Figure 5.7.3**: Quality Evaluation and Feedback Generation
  - Shows: Simulation results → QoS extraction → Decision feedback + Rewards
  - Excludes: SMC execution (previous)

- **Reference**: Complete verification workflow in Appendix B

### Section 5.8: Execution and System Reconfiguration
- Adaptation option retrieval
- Adaptation application
- Loop closure
- **Figure**: Execution phase (focused, already appropriately sized)

### Section 5.9: RS-DRL Feedback and Learning Overview
- Role of feedback
- Reward generation
- Separation of concerns

### Section 5.10: Asynchronous RS-DRL Learning and Policy Update
**Decomposed into 3 focused figures:**

- **Figure 5.10.1**: Experience Collection
  - Shows: Episode initialization → Action selection → Environment interaction
  - Excludes: Replay memory, training (next figures)
  
- **Figure 5.10.2**: Experience Replay and Reward Reshaping
  - Shows: Minibatch sampling → Failure detection → Reward reshaping
  - Highlights: Key innovation (reward-shaping mechanism)
  - Excludes: Q-network training (next)
  
- **Figure 5.10.3**: Q-Network Training and Model Update
  - Shows: Reshaped batch → TD targets → Gradient descent → Model storage
  - Excludes: Experience collection, reward shaping (previous)

- **Reference**: Complete learning workflow in Appendix C

### Section 5.11: Knowledge Management and Process Coordination
- Knowledge as shared memory
- Read-write coordination contracts
- Synchronization of heterogeneous processes

### Section 5.12: Chapter Summary
- Hierarchical process decomposition
- Architectural contributions
- Figure organization principle
- Transition to evaluation

## Figure Decomposition Strategy

### Monolithic → Decomposed Mapping

**Original monolithic diagram**: `monitoring-state-construction.pdf`
**Decomposed into**:
1. `monitoring-data-acquisition.pdf` (data collection only)
2. `monitoring-feature-extraction.pdf` (preprocessing and features only)
3. `monitoring-state-dissemination.pdf` (validation and dissemination only)

**Original monolithic diagram**: `adaptation-prediction.pdf` (already focused, minimal decomposition)
**Decomposed into**:
1. `prediction-model-retrieval.pdf` (model access only)
2. `prediction-option-selection.pdf` (Q-value evaluation and selection only)

**Original monolithic diagram**: `adaptation-verification.pdf`
**Decomposed into**:
1. `verification-trigger.pdf` (initiation and model setup only)
2. `verification-smc.pdf` (statistical checking only)
3. `verification-quality-evaluation.pdf` (already exists, quality extraction only)

**Original monolithic diagram**: `rs-drl-training.pdf`
**Decomposed into**:
1. `training-episode-initialization.pdf` (already exists, experience collection only)
2. `training-experience-storage.pdf` (already exists, replay and reshaping only)
3. `training-q-network.pdf` (already exists, Q-network training only)

## Benefits of Decomposed Figures

### ✅ Cognitive Clarity
- Examiners see one concept per figure
- No need to decode complex flows while reading
- Figures are consulted, not studied

### ✅ Structural Alignment
- Text modularity matches figure modularity
- Each subsection has its own focused figure
- No mismatch between modular text and monolithic visuals

### ✅ No Information Loss
- Full end-to-end workflows preserved in appendices
- Complete technical transparency maintained
- Readers can choose their level of detail

### ✅ PhD-Level Presentation Judgment
- Demonstrates understanding of thesis presentation principles
- Signals architectural maturity
- Shows consideration for examiner experience

### ✅ Reading Rhythm
- Figures don't break flow
- Each figure reinforces its section
- Natural progression through chapter

## Comparison with Other Alternatives

| Aspect | Alternative 1 | Alternative 2 | Alternative 3 |
|--------|---------------|---------------|---------------|
| Main chapter length | 12 pages | 22 pages | 20 pages |
| Figure count (main) | 3 figures | 9 figures | 15 figures (decomposed) |
| Figure complexity | Moderate | High (monolithic) | Low (focused) |
| Figure-section alignment | Good | Good | Perfect (1:1) |
| Cognitive load | Moderate | Moderate-High | Low |
| Information preservation | Split (appendices) | All in main | Split (appendices) |
| Examiner-friendliness | High | High | Very High |
| Best for | Architecture focus | Complete documentation | Examiner review |

## When to Use Alternative 3

### Use Alternative 3 when:
- Examiners prefer short, focused figures
- Cognitive clarity is prioritized
- Chapter has many complex process flows
- Want perfect alignment between text and figures
- Preparing for oral defense (easier to reference specific figures)

### Don't use Alternative 3 when:
- Readers prefer seeing complete workflows in main text
- Figure decomposition creates too many small figures
- Monolithic diagrams are already appropriately sized

## Implementation Notes

### Existing Decomposed Figures (Already Available)

The following decomposed figures already exist in the `figures/` directory:

✅ `monitoring-data-acquisition.pdf`
✅ `monitoring-feature-extraction.pdf`
✅ `monitoring-state-dissemination.pdf`
✅ `prediction-model-retrieval.pdf`
✅ `prediction-option-selection.pdf`
✅ `verification-trigger.pdf`
✅ `verification-smc.pdf`
✅ `verification-quality-evaluation.pdf`
✅ `training-episode-initialization.pdf`
✅ `training-experience-storage.pdf`
✅ `training-q-network.pdf`

These were generated from the original PlantUML source files and are ready to use.

### Appendix Structure

The appendices (referenced but not included in this standalone version) would contain:

- **Appendix A.1**: Complete monitoring and state construction workflow (full `monitoring-state-construction.pdf`)
- **Appendix A.2**: Complete adaptation decision workflow (full `adaptation-prediction.pdf`)
- **Appendix B**: Complete verification workflow (full `adaptation-verification.pdf`)
- **Appendix C**: Complete learning workflow (full `rs-drl-training.pdf`)

## What Supervisors/Examiners Will Say

### Expected Positive Feedback:

> "The figures are much easier to follow. Each one makes a clear point."

> "I appreciate that I can see the big picture in the appendix if needed."

> "This shows good judgment about thesis presentation."

### Avoids Negative Feedback:

❌ "These diagrams are overwhelming."
❌ "I need to decode a poster while reading."
❌ "The figures don't match the section structure."

## Key Design Decisions

### 1. Figure Placement
- Each figure immediately follows the subsection it illustrates
- No figures span multiple subsections
- Clear 1:1 mapping between concepts and visuals

### 2. Figure Captions
- Explicitly state what is shown
- Explicitly state what is excluded
- Reference appendix for complete workflow

### 3. Cross-References
- Main chapter references appendices for full workflows
- Appendices reference main chapter for context
- Bidirectional navigation maintained

### 4. Information Architecture
- **Main chapter**: Architectural concepts with focused visuals
- **Appendices**: Complete workflows with monolithic diagrams
- **No duplication**: Each piece of information has one primary location

## Compilation

The file compiles successfully:

```bash
cd E:\projects\thesis
pdflatex chapters\chapter5-alternative3.tex
```

Output: `chapters/chapter5-alternative3.pdf` (20 pages, 4.4 MB)

All decomposed figures are successfully included from the existing `figures/` directory.

## Summary

Alternative 3 provides a **decomposed figure structure** that:
- Uses focused, single-responsibility figures
- Achieves perfect alignment between text and visuals
- Reduces cognitive load for examiners
- Preserves complete workflows in appendices
- Demonstrates PhD-level presentation judgment
- Makes the chapter easier to read and defend

This version is ideal for examiner review and oral defense, where clear, focused visuals enable quick reference and discussion.
