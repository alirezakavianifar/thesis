---
name: Create Diagram Map
overview: Create a high-quality PlantUML diagram map that serves as a navigation figure showing how the Integration Diagram (center) is refined by Diagrams D1-D5 (arranged around it). This is a visual table of contents with radial layout, using dashed arrows labeled "refines", styled consistently with other diagrams, then render to PNG and SVG.
todos:
  - id: create-puml-file
    content: Create diagram-map.puml with radial layout showing Integration Diagram in center and D1-D5 around it with dashed refinement arrows
    status: completed
  - id: verify-layout
    content: Verify the radial layout is balanced and clear, with all refinement relationships properly shown
    status: completed
    dependencies:
      - create-puml-file
  - id: render-png
    content: Render high-quality PNG image using render-local.ps1 script (300 DPI)
    status: completed
    dependencies:
      - verify-layout
  - id: render-svg
    content: Render SVG format for vector output
    status: completed
    dependencies:
      - verify-layout
---

# Create

Diagram Map of RS-DRL Process Models

## Overview

Create a new PlantUML diagram map that serves as a navigation figure showing the abstraction levels and refinement relationships between the Integration Diagram and Diagrams 1-5. Based on [step7.md](.cursor/plans/step7.md), this will be a clean, minimal, thesis-grade visual table of contents.

## Implementation Steps

### 1. Create PlantUML File

- Create `diagram-map.puml` based on the template in step7.md (lines 105-123)
- Use radial layout with Integration Diagram in center and D1-D5 arranged around it
- Apply consistent styling (can use similar settings but adapted for diagram map style)
- Title: "Diagram Map of RS-DRL Process Models"

### 2. Diagram Structure

- Central rectangle: "I\nIntegrated Process View" (or with figure reference placeholder)
- Five rectangles around it:
- D1: RS-DRL Training & Reward Shaping
- D2: Adaptation Option Prediction
- D3: MAPE-K Adaptation Control Loop
- D4: Adaptation Option Verification
- D5: Monitoring & State Construction
- Use dashed arrows labeled "refines" from center (I) to each sub-diagram (D1-D5)
- Include figure number placeholders (Figure X, X+1, etc.) in labels

### 3. Important Design Considerations

- Minimalist design - just boxes and arrows, no internal flow
- Each diagram represented as a single labeled box
- Clear hierarchy with center as high-level view
- Radial/symmetric layout for visual balance
- Dashed arrows to show refinement relationships
- Academic and clean presentation

### 4. Styling Considerations

- May use different styling than activity diagrams (rectangle diagram style)
- Keep colors minimal if used
- Ensure text is clear and readable
- Professional appearance suitable for thesis

### 5. Render High-Quality Images

- Use `render-local.ps1` script to generate PNG output (300 DPI)
- Generate SVG for vector format
- Verify output is clean, readable, and fits one page

## Files to Create/Modify

- `diagram-map.puml` (new file)
- `diagram-map.png` (generated output)
- `diagram-map.svg` (generated output)

## Technical Details

- Use PlantUML rectangle diagram syntax (not activity diagram)
- Dashed arrows: `-[dashed]->`