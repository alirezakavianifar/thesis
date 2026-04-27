---
name: Create MAPE-K Adaptation Control Loop Diagram
overview: Create a high-quality PlantUML activity diagram for the MAPE-K Adaptation Control Loop based on step3.md, styled like rs-drl-mape-k-diagram.puml with DPI 300 and professional formatting, including loop-backs and Figure 4 traceability, then render to PNG and SVG.
todos:
  - id: create-puml-file
    content: Create mape-k-adaptation-control-loop.puml with structure from step3.md and styling from rs-drl-mape-k-diagram.puml
    status: completed
  - id: fix-loop-back-flows
    content: Fix loop-back arrows (back to Monitor when no adaptation needed and after execution) using proper PlantUML syntax
    status: completed
    dependencies:
      - create-puml-file
  - id: add-traceability-notes
    content: Add proper Figure 4 traceability notes (arrows 1, 4, 5, 6-9) and ensure all annotations are correct
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

# Create MA

PE-K Adaptation Control Loop Diagram

## Overview

Create a new PlantUML activity diagram file that visualizes the MAPE-K Adaptation Control Loop described in [step3.md](step3.md), using the same high-quality styling as [rs-drl-mape-k-diagram.puml](rs-drl-mape-k-diagram.puml). This diagram shows the complete control flow and embeds Diagram 2 as a subprocess.

## Implementation Steps

### 1. Create PlantUML File

- Create `mape-k-adaptation-control-loop.puml` based on the diagram structure in step3.md (lines 164-239)
- Apply styling from rs-drl-mape-k-diagram.puml:
- DPI 300 settings
- Color scheme (light blue activities, purple partitions, yellow notes)
- Professional formatting (font sizes, padding, shadows)
- Title: "MAPE-K Adaptation Control Loop\n(UML Activity Diagram – Fig.4 Traceable)"

### 2. Enhance Diagram Structure

- Convert the basic diagram from step3.md into a properly formatted PlantUML file
- Handle loop-back flows (back to Monitor when no adaptation needed, and after execution)
- Ensure all partitions are properly structured
- Add appropriate notes with Figure 4 traceability references (arrows 1, 4, 5, 6-9)
- Include proper start/stop nodes

### 3. Key Partitions to Include

- **MAPE-K : Monitor**: Observe system, collect metrics, update Knowledge (arrow 1)
- **MAPE-K : Analyze**: 
- Evaluate state against goals (arrow 4)
- Decision node: "Goals violated or at risk?"
- If yes: Trigger adaptation (arrow 5)
- If no: Loop back to Monitor
- **MAPE-K : Plan**:
- Invoke Adaptation Option Predictor (embeds Diagram 2)
- Retrieve trained model (arrow 6)
- Predict adaptation option (arrow 7)
- **MAPE-K : Execute**:
- Retrieve adaptation details (arrow 8)
- Apply adaptation to managed system (arrow 9)
- **Managed System**: System behavior changes, environment reacts
- Loop back to Monitor after execution

### 4. Important Design Considerations

- This is **event-driven control logic**, not continuous optimization
- Shows explicit decision point: "Goals violated or at risk?"
- Embeds Diagram 2 (Adaptation Option Predictor) as a subprocess in Plan phase
- Two loop-back points:

1. When no adaptation needed (back to Monitor from Analyze)
2. After execution completes (back to Monitor from Managed System)

- Clear separation of control logic from learning logic

### 5. Render High-Quality Images

- Use `render-local.ps1` script to generate PNG output (300 DPI)
- Generate SVG for vector format
- Verify output quality matches existing diagrams

## Files to Create/Modify

- `mape-k-adaptation-control-loop.puml` (new file)
- `mape-k-adaptation-control-loop.png` (generated output)
- `mape-k-adaptation-control-loop.svg` (generated output)

## Technical Details

- Use same skinparam settings as rs-drl-mape-k-diagram.puml for consistency
- Include traceability notes referencing Figure 4 arrows: (1), (4), (5), (6), (7), (8), (9)
- Handle loop-back flows properly using explicit activity recreation (as done in Diagram 1)