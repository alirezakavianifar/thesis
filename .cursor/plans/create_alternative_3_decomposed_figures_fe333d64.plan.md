---
name: Create Alternative 3 Decomposed Figures
overview: Create a third alternative version of Chapter 5 that decomposes long monolithic process-flow diagrams into smaller, section-specific figures aligned with the chapter structure. Each figure will focus on one conceptual responsibility, with the full end-to-end workflow moved to an appendix.
todos: []
isProject: false
---

# Create Chapter 5 Alternative 3: Decomposed Figure Structure

## Overview

Based on `plans/alternative_3.md`, this alternative addresses the problem of long, monolithic process-flow diagrams by decomposing them into smaller, section-specific figures. The key principle is: **One figure = one conceptual responsibility**.

## Problem Being Solved

Current versions contain long vertical process-flow diagrams (e.g., monitoring-state-construction.pdf) that:

- Cause cognitive overload for examiners
- Create misalignment between modular text and monolithic figures
- Force readers to decode complex flows while reading

## Solution Approach

Split monolithic diagrams into multiple sectional figures:

- Each figure aligned with its corresponding section
- Short, readable, contextual diagrams in main chapter
- Full end-to-end workflow preserved in appendix

## Files to Create

### 1. Main Chapter: `chapters/chapter5-alternative3.tex`

Based on Alternative 2 structure but with decomposed figures:

**Section 5.5: Runtime Monitoring and State Construction**

- Figure 5.5.1: Monitoring and Raw Data Acquisition
  - Shows: Raw data sources, metric acquisition, initial normalization
  - Short, focused on data collection only
- Figure 5.5.2: Preprocessing and Feature Engineering
  - Shows: Filtering, feature extraction, uncertainty annotation
  - Focused on transformation steps
- Figure 5.5.3: State Vector Construction and Validation
  - Shows: State assembly, validation rules, output as validated state vector
  - Focused on final construction and validation

**Other sections remain similar to Alternative 2** but with references to appendix for full workflows

### 2. Appendix: `appendices/chapter5-alternative3-appendices.tex`

Contains full end-to-end workflows:

- Appendix A.1: Complete Monitoring and State Construction Workflow (full monolithic diagram)
- Appendix A.2: Complete Adaptation Decision Workflow
- Appendix A.3: Complete Learning Workflow

### 3. Documentation: `plans/README-alternative3.md`

Explains:

- Rationale for decomposed figure approach
- Comparison with other alternatives
- When to use this version
- How it addresses examiner concerns

## Key Differences from Other Alternatives


| Aspect                   | Alternative 1   | Alternative 2   | Alternative 3         |
| ------------------------ | --------------- | --------------- | --------------------- |
| Figure strategy          | Moderate detail | Full diagrams   | Decomposed sectional  |
| Monolithic diagrams      | In main chapter | In main chapter | Moved to appendix     |
| Figure-section alignment | Good            | Good            | Perfect (1:1 mapping) |
| Cognitive load           | Moderate        | Moderate-High   | Low                   |
| Examiner-friendliness    | High            | High            | Very High             |


## Implementation Steps

1. **Create decomposed figure descriptions** in chapter5-alternative3.tex
  - Note: Since we don't have the actual decomposed figure files, we'll reference them conceptually
  - Add notes indicating which figures need to be created from existing monolithic diagrams
2. **Structure main chapter** (22-25 pages estimated)
  - Use Alternative 2 as base structure
  - Replace monolithic figure references with decomposed figure references
  - Add explicit references to appendix for full workflows
3. **Create appendix** with full workflows
  - Include complete end-to-end diagrams
  - Maintain all technical detail
  - Cross-reference back to main chapter sections
4. **Add documentation** explaining the approach

## Benefits of This Approach

1. **Cognitive clarity**: Examiners see one concept per figure
2. **Structural alignment**: Text modularity matches figure modularity
3. **No information loss**: Full workflows preserved in appendix
4. **PhD-level judgment**: Demonstrates understanding of thesis presentation principles
5. **Examiner-friendly**: Figures are consulted, not studied

## Notes

- This alternative requires creating new figure files by decomposing existing monolithic diagrams
- For this implementation, we'll create the LaTeX structure with placeholders/references
- Actual figure decomposition would be done using diagram editing tools
- The approach is compatible with both Alternative 1 and Alternative 2 organizational principles

