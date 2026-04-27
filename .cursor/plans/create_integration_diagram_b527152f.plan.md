---
name: Create Integration Diagram
overview: Create a high-quality PlantUML activity diagram that integrates Diagrams 1-5 into a single cohesive view, showing how all subprocesses compose together with clear control flow, data flow, and Figure 4 traceability, styled like rs-drl-mape-k-diagram.puml with DPI 300, then render to PNG and SVG.
todos:
  - id: create-puml-file
    content: Create rs-drl-integrated-system.puml with structure from step6.md and styling from rs-drl-mape-k-diagram.puml, integrating Diagrams 1-5
    status: completed
  - id: fix-loop-back-flows
    content: Fix loop-back arrows (back to system execution when no adaptation needed and after execution) using proper PlantUML syntax
    status: completed
    dependencies:
      - create-puml-file
  - id: add-traceability-notes
    content: Add proper Figure 4 traceability notes (arrows 1-9) and ensure all annotations reference the integrated subprocesses correctly
    status: completed
    dependencies:
      - fix-loop-back-flows
  - id: render-png
    content: Render high-quality PNG image using render-local.ps1 script (300 DPI)
    status: completed
    dependencies:
      - add-traceability-notes
  - id: render-svg
    content: Render SVG format for vector output
    status: completed
    dependencies:
      - add-traceability-notes
---

# Crea

te Integration Diagram - RS-DRL-Based Self-Adaptive System

## Overview

Create a new PlantUML activity diagram file that integrates Diagrams 1-5 into a single cohesive view, showing the orchestration layer of the RS-DRL-based self-adaptive system. This diagram treats each deep-dive diagram as a black box subprocess while maintaining Figure 4 traceability. Based on [step6.md](step6.md) and styled like [rs-drl-mape-k-diagram.puml](rs-drl-mape-k-diagram.puml).

## Implementation Steps

### 1. Create PlantUML File

- Create `rs-drl-integrated-system.puml` based on the diagram structure in step6.md (lines 32-124)
- Apply styling from rs-drl-mape-k-diagram.puml:
- DPI 300 settings
- Color scheme (light blue activities, purple partitions, yellow notes)
- Professional formatting (font sizes, padding, shadows)
- Title: "Integrated RS-DRL–Based Self-Adaptive System\n(Composition of Diagrams 1–5)"

### 2. Enhance Diagram Structure

- Convert the basic diagram from step6.md into a properly formatted PlantUML file
- Handle loop-back flows (back to system execution when no adaptation needed, and after execution)
- Ensure all partitions are properly structured with references to Diagrams 1-5
- Add appropriate notes with Figure 4 traceability references (arrows 1-9)
- Show how each subprocess (Diagrams 1-5) integrates into the overall flow

### 3. Key Partitions to Include

- **Managed System & Environment**: Execute system behavior, generate runtime data (arrow 1)
- **Monitoring & State Construction (Diagram 5)**: Collect, preprocess, extract features, construct state vector (arrows 2, 4)
- **MAPE-K : Analyze (Diagram 3)**: Evaluate goals, decision node, trigger adaptation if needed (arrow 5)
- **MAPE-K : Plan (Diagram 2)**: Invoke predictor, retrieve model (arrow 6), predict option (arrow 7)
- **Adaptation Option Verification (Diagram 4)**: Parameterize model, run UPPAAL-SMC, estimate QoS
- **RS-DRL Training (Diagram 1)**: Receive feedback, store experience, reward shaping, update model, store model (arrow 3)
- **MAPE-K : Execute (Diagram 3)**: Retrieve details (arrow 8), apply adaptation (arrow 9)
- Loop back to system execution

### 4. Important Design Considerations

- This is an orchestration layer - treats Diagrams 1-5 as black box subprocesses
- Shows when each subprocess is activated
- Makes feedback loops explicit (loop back when no adaptation, and after execution)
- Avoids redundancy - doesn't explode internals of each diagram
- Preserves clear responsibility boundaries
- Shows both control flow and data flow
- All Figure 4 arrows (1-9) should be traceable

### 5. Render High-Quality Images

- Use `render-local.ps1` script to generate PNG output (300 DPI)
- Generate SVG for vector format
- Verify output quality matches existing diagrams

## Files to Create/Modify

- `rs-drl-integrated-system.puml` (new file)
- `rs-drl-integrated-system.png` (generated output)
- `rs-drl-integrated-system.svg` (generated output)

## Technical Details

- Use same skinparam settings as rs-drl-mape-k-diagram.puml for consistency
- Include traceability notes referencing Figure 4 arrows: (1), (2), (3), (4), (5), (6), (7), (8), (9)
- Reference Diagrams 1-5 in partition labels where appropriate
- Handle loop-back flows properly using explicit activity recreation (as done in previous diagrams)