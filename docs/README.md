# RS-DRL-Enhanced MAPE-K Control Loop Process Diagram

## Overview

This repository contains a UML Activity Diagram that represents the **RS-DRL-enhanced MAPE-K control loop** from Figure 4 of the RS-DRL (Reinforcement Learning with Deep Reinforcement Learning) paper. The diagram provides an activity-level view of how a self-adaptive system integrates reinforcement learning with the MAPE-K (Monitor, Analyze, Plan, Execute, Knowledge) control loop.

## What the Diagram Represents

The diagram illustrates a hybrid control-and-learning workflow that combines:

1. **Runtime feedback control loop (MAPE-K)**: Traditional self-adaptation cycle
2. **Learning loop (RS-DRL training and retraining)**: Deep reinforcement learning for adaptation option selection
3. **Decision loop**: Adaptation option prediction and execution

### Key Components

- **Managed System**: The system being adapted, which produces runtime data and receives adaptation actions
- **MAPE-K Partitions**:
  - **Monitor**: Collects and processes runtime data
  - **Analyze**: Detects goal violations or risks
  - **Plan (Adaptation Option Predictor)**: Uses trained RS-DRL model to predict best adaptation options
  - **Execute**: Applies adaptations to the managed system
- **RS-DRL Module**: Reinforcement learning module that trains a Deep Q-Network (DQN) to learn optimal adaptation strategies

### Process Flow

The diagram shows the complete adaptation episode cycle:

1. **Runtime Observation**: System produces runtime data
2. **Learning (optional/episodic)**: RS-DRL module trains/updates the model
3. **Analysis & Decision**: MAPE-K analyzes data and decides if adaptation is needed
4. **Adaptation Execution**: Best adaptation option is applied
5. **Environment/System Change**: System state changes
6. **Repeat**: Cycle continues for next adaptation episode

## Traceability to Figure 4

The diagram is explicitly annotated with **arrow numbers (1-9)** that correspond to the flows described in Figure 4 of the RS-DRL paper. This ensures full traceability between the process diagram and the original architectural figure.

### Arrow Mapping

| Arrow | Flow Description | Source | Destination |
|-------|-----------------|--------|-------------|
| (1) | Runtime data produced | Managed System | - |
| (2) | Monitor sends runtime data to RS-DRL | MAPE-K Monitor | RS-DRL Module |
| (3) | Trained model stored in Knowledge | RS-DRL Module | Knowledge Repository |
| (4) | Runtime data forwarded to Analyzer | MAPE-K Monitor | MAPE-K Analyze |
| (5) | Analyzer notifies Adaptation Option Predictor | MAPE-K Analyze | MAPE-K Plan |
| (6) | Predictor retrieves trained RS-DRL model | Knowledge Repository | MAPE-K Plan |
| (7) | Adaptation option predicted | MAPE-K Plan | - |
| (8) | Executor retrieves adaptation option details | MAPE-K Plan | MAPE-K Execute |
| (9) | Adaptation applied to managed system | MAPE-K Execute | Managed System |

## How to Render the Diagram

### Option 1: Local Rendering (Recommended - No Internet Required)

**Quick Start:**
1. Install Java (if not already installed):
   - Download from [Adoptium](https://adoptium.net/) (Java 17 LTS or newer)
   - Or use Chocolatey: `choco install openjdk` (as Administrator)

2. Use the provided script:
   ```powershell
   # Default rendering (300 DPI for high quality)
   .\render-local.ps1
   
   # Custom DPI (higher = better quality, larger file)
   .\render-local.ps1 -DPI 600
   
   # Different format
   .\render-local.ps1 -Format svg
   ```
   The script will automatically download PlantUML if needed and render your diagram.

**Manual Method:**
1. Download `plantuml.jar` from [PlantUML Releases](https://github.com/plantuml/plantuml/releases/latest)
2. Place it in your project folder
3. Run:
   ```powershell
   # Standard quality
   java -jar plantuml.jar rs-drl-mape-k-diagram.puml
   
   # High quality (300 DPI)
   java -jar plantuml.jar -SDPI=300 rs-drl-mape-k-diagram.puml
   
   # Ultra high quality (600 DPI)
   java -jar plantuml.jar -SDPI=600 rs-drl-mape-k-diagram.puml
   ```

For detailed setup instructions, see [LOCAL_RENDERING_SETUP.md](LOCAL_RENDERING_SETUP.md).

### Option 2: Online PlantUML Server (Easiest - Requires Internet)

1. Visit [PlantUML Online Server](http://www.plantuml.com/plantuml/uml/)
2. Copy the contents of `rs-drl-mape-k-diagram.puml`
3. Paste into the editor
4. The diagram will render automatically
5. Export as PNG, SVG, or other formats

### Option 3: VS Code Extension

1. Install the "PlantUML" extension in VS Code
2. Open `rs-drl-mape-k-diagram.puml`
3. Press `Alt+D` (or right-click and select "Preview PlantUML Diagram")
4. Export the rendered diagram

### Option 4: Command Line (PlantUML Java Tool)

1. Install PlantUML (requires Java):
   ```bash
   # Download from http://plantuml.com/download
   # Or use package manager:
   # macOS: brew install plantuml
   # Linux: sudo apt-get install plantuml
   ```

2. Render the diagram:
   ```bash
   plantuml rs-drl-mape-k-diagram.puml
   ```

3. This generates `rs-drl-mape-k-diagram.png` (or SVG if specified)

### Option 5: Other Tools

- **IntelliJ IDEA**: Built-in PlantUML support
- **Eclipse**: PlantUML plugin
- **Online editors**: [PlantText](https://www.planttext.com/), [PlantUML Editor](https://plantuml-editor.kkeisuke.com/)

## How to Reference in Academic Writing

When describing this diagram in a thesis or paper, you can write:

> "As shown in Figure X, runtime data is first collected from the managed system (Step **1**), forwarded to both the Monitor and the RS-DRL module (Steps **2** and **4**). Once adaptation goals are violated (**5**), the planner retrieves the trained model (**6**) and predicts an adaptation option (**7**), which is then executed (**8–9**)."

### Recommended Citation Style

Refer to this diagram as: **"An activity-level view of the RS-DRL–enhanced MAPE-K control loop."**

This description emphasizes:
- The process/activity perspective (vs. architectural view)
- The integration of RS-DRL with MAPE-K
- The control loop nature of the system

## File Structure

```
.
├── rs-drl-mape-k-diagram.puml    # Main PlantUML diagram source
├── render-local.ps1              # Local rendering script (PowerShell)
├── LOCAL_RENDERING_SETUP.md      # Detailed local rendering setup guide
├── README.md                      # This documentation file
└── arrow-mapping.md              # Detailed arrow mapping reference
```

## Customization Options

### For Paper/Thesis
- Keep labels high-level as shown
- Use the diagram as-is for academic explanation
- Reference as "activity-level view"

### For Implementation Documentation
- Expand sub-activities inside RS-DRL Module (e.g., Replay Memory, Reward Calculator)
- Add object flows (e.g., states, rewards, models)
- Include more detailed decision nodes

### For Teaching/Presentation
- Add colors to partitions (PlantUML supports color syntax)
- Collapse the RS-DRL partition into a single «sub-activity» if needed
- Simplify for one-page conceptual diagram

## Why This Diagram is Faithful to Figure 4

1. **Explicit Managed vs. Managing System Separation**: Clear partition boundaries
2. **Clear Decision Node for Goal Violation**: Explicit if-then-else for adaptation triggers
3. **Distinct Learning Loop and Control Loop**: RS-DRL training loop separate from MAPE-K control loop
4. **Episodic Repetition Clearly Modeled**: Loop back to "Operate system" for next episode
5. **Full Traceability**: Every major flow annotated with Figure 4 arrow numbers

## Additional Resources

- For a **reduced version** suitable for paper page limits, simplify the RS-DRL partition
- For a **BPMN version** with the same numbering, convert the PlantUML syntax to BPMN
- For a **table mapping arrows (1–9) → UML elements**, see `arrow-mapping.md`

## License

This diagram is created for academic/thesis purposes based on the RS-DRL paper's Figure 4. Please cite the original RS-DRL paper when using this diagram.

