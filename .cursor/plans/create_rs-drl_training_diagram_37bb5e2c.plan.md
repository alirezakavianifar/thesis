---
name: Create RS-DRL Training Diagram
overview: Create a high-quality PlantUML activity diagram based on step1.md content, styled like rs-drl-mape-k-diagram.puml with DPI 300 and professional formatting, then render to PNG and SVG.
todos:
  - id: create-puml-file
    content: Create rs-drl-training-process.puml with structure from step1.md and styling from rs-drl-mape-k-diagram.puml
    status: completed
  - id: fix-diagram-syntax
    content: Fix loop-back arrows and ensure all PlantUML syntax is correct (partitions, decisions, notes)
    status: completed
    dependencies:
      - create-puml-file
  - id: render-png
    content: Render high-quality PNG image using render-local.ps1 script (300 DPI)
    status: completed
    dependencies:
      - fix-diagram-syntax
  - id: render-svg
    content: Optionally render SVG format for vector output
    status: completed
    dependencies:
      - fix-diagram-syntax
---

# Create

RS-DRL Training & Reward Shaping Process Diagram

## Overview

Create a new PlantUML activity diagram file that visualizes the RS-DRL Training & Reward-Shaping Process described in [step1.md](step1.md), using the same high-quality styling as [rs-drl-mape-k-diagram.puml](rs-drl-mape-k-diagram.puml).

## Implementation Steps

### 1. Create PlantUML File

- Create `rs-drl-training-process.puml` based on the diagram structure in step1.md (lines 146-217)
- Apply styling from rs-drl-mape-k-diagram.puml:
- DPI 300 settings
- Color scheme (light blue activities, purple partitions, yellow notes)
- Professional formatting (font sizes, padding, shadows)
- Title: "RS-DRL Training & Reward Shaping Process\n(UML Activity Diagram – Deep Dive)"

### 2. Enhance Diagram Structure

- Convert the basic diagram from step1.md into a properly formatted PlantUML file
- Fix loop-back arrows to use proper PlantUML syntax (`backward:` or explicit arrows)
- Ensure all partitions are properly closed
- Add appropriate notes where needed (especially for the reward shaping section)

### 3. Key Partitions to Include

- **Episode Control**: Initialize episode, receive state
- **Action Selection**: ε-greedy action selection
- **Environment Interaction**: Execute action, observe reward and next state
- **Replay Memory Management**: Store experience, check buffer fullness, sample minibatch
- **Reward Shaping (Novel Contribution)**: Identify failures, compute K, reshape rewards
- **Model Training (DQN)**: Compute TD targets, loss, gradient descent, update target network
- **Model Repository**: Store updated model
- **Episode Control (loop)**: Check termination, loop back

### 4. Render High-Quality Images

- Use `render-local.ps1` script to generate PNG output (300 DPI)
- Optionally generate SVG for vector format
- Verify output quality matches the existing rs-drl-mape-k-diagram.png

## Files to Create/Modify

- `rs-drl-training-process.puml` (new file)
- `rs-drl-training-process.png` (generated output)
- `rs-drl-training-process.svg` (optional, generated output)

## Technical Details

- Use same skinparam settings as rs-drl-mape-k-diagram.puml for consistency