---
name: Create Adaptation Option Verification Diagram
overview: Create a high-quality PlantUML activity diagram for the Adaptation Option Verification Process (UPPAAL-SMC & Runtime Models) based on step4.md, styled like rs-drl-mape-k-diagram.puml with DPI 300 and professional formatting, including decision logic for training vs planning contexts, then render to PNG and SVG.
todos:
  - id: create-puml-file
    content: Create adaptation-option-verification.puml with structure from step4.md and styling from rs-drl-mape-k-diagram.puml
    status: completed
  - id: add-explanatory-notes
    content: Add proper explanatory notes about verification process, uncertainty handling, and context-dependent outputs
    status: completed
    dependencies:
      - create-puml-file
  - id: render-png
    content: Render high-quality PNG image using render-local.ps1 script (300 DPI)
    status: completed
    dependencies:
      - add-explanatory-notes
  - id: render-svg
    content: Render SVG format for vector output
    status: completed
    dependencies:
      - add-explanatory-notes
---

# Crea

te Adaptation Option Verification Process Diagram

## Overview

Create a new PlantUML activity diagram file that visualizes the Adaptation Option Verification Process (UPPAAL-SMC & Runtime Models) described in [step4.md](step4.md), using the same high-quality styling as [rs-drl-mape-k-diagram.puml](rs-drl-mape-k-diagram.puml). This diagram explains how selected adaptation options are verified for safety and goal compliance.

## Implementation Steps

### 1. Create PlantUML File

- Create `adaptation-option-verification.puml` based on the diagram structure in step4.md (lines 142-198)
- Apply styling from rs-drl-mape-k-diagram.puml:
- DPI 300 settings
- Color scheme (light blue activities, purple partitions, yellow notes)
- Professional formatting (font sizes, padding, shadows)
- Title: "Adaptation Option Verification Process\n(UPPAAL-SMC & Runtime Models)"

### 2. Enhance Diagram Structure

- Convert the basic diagram from step4.md into a properly formatted PlantUML file
- Ensure all partitions are properly structured
- Include decision logic for training vs planning contexts
- Add appropriate explanatory notes

### 3. Key Partitions to Include

- **Verification Trigger**: Receive candidate adaptation option and current system state
- **Runtime Model Manager**: 
- Retrieve runtime model
- Parameterize model with state & adaptation option
- **UPPAAL-SMC Engine**: 
- Execute probabilistic simulations
- Estimate goal satisfaction probabilities
- **Quality Evaluation**: 
- Extract QoS metrics
- Aggregate metrics into quality score
- **Reward / Feedback Interface**: 
- Decision: "Invoked during training?"
- If yes: Generate reward value (for RS-DRL learning loop)
- If no: Generate quality estimate (for adaptation decision justification)

### 4. Important Design Considerations

- This process sits between decision and reward
- Makes uncertainty handling explicit (probabilistic, not deterministic)
- Reusable by both learning (training) and planning contexts
- Clearly isolates formal verification from control logic
- Shows how verification results become learning signals
- No loops (sequential process)

### 5. Render High-Quality Images

- Use `render-local.ps1` script to generate PNG output (300 DPI)
- Generate SVG for vector format
- Verify output quality matches existing diagrams

## Files to Create/Modify

- `adaptation-option-verification.puml` (new file)
- `adaptation-option-verification.png` (generated output)
- `adaptation-option-verification.svg` (generated output)

## Technical Details

- Use same skinparam settings as rs-drl-mape-k-diagram.puml for consistency