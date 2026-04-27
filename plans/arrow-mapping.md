# Arrow Mapping Reference: Figure 4 Traceability

This document provides a detailed mapping of each arrow number (1-9) from Figure 4 of the RS-DRL paper to the corresponding UML elements and process steps in the PlantUML activity diagram.

## Overview

The arrows in Figure 4 represent data and control flows in the RS-DRL-enhanced MAPE-K control loop. Each arrow is annotated in the PlantUML diagram as a `note` attached to the relevant activity or flow.

## Detailed Arrow Mapping

### Arrow (1): Runtime Data Production

**Figure 4 Description**: Runtime data produced by managed system

**UML Element**: Note attached to "Produce runtime data" activity in Managed System partition

**Process Step**: 
- **Activity**: `Produce runtime data (system state, environment data)`
- **Partition**: Managed System
- **Position**: After "Operate system", before data collection

**Flow Direction**: Managed System → (data available for collection)

**Context**: The managed system executes its normal operations and generates runtime data including system state and environment information. This data becomes available for the monitoring phase.

---

### Arrow (2): Monitor to RS-DRL Data Flow

**Figure 4 Description**: Monitor sends runtime data to RS-DRL

**UML Element**: Note attached to "Receive state vector" activity in RS-DRL Module partition

**Process Step**:
- **Source Activity**: `Extract features / state vector` (in MAPE-K Monitor)
- **Destination Activity**: `Receive state vector` (in RS-DRL Module)
- **Partitions**: MAPE-K Monitor → RS-DRL Module

**Flow Direction**: MAPE-K Monitor → RS-DRL Module

**Context**: After extracting features and creating a state vector, the Monitor forwards this processed data to the RS-DRL module for learning purposes. This enables the RS-DRL module to learn from runtime observations.

---

### Arrow (3): Trained Model Storage

**Figure 4 Description**: Trained model stored in Knowledge

**UML Element**: Note attached to "Store trained model in Knowledge Repository" activity in RS-DRL Module partition

**Process Step**:
- **Activity**: `Store trained model in Knowledge Repository`
- **Partition**: RS-DRL Module
- **Position**: After training/updating DQN

**Flow Direction**: RS-DRL Module → Knowledge Repository

**Context**: After the RS-DRL module completes training or updating the Deep Q-Network (DQN), the trained model is stored in the Knowledge Repository. This makes the model available for the Adaptation Option Predictor to use during planning.

---

### Arrow (4): Monitor to Analyzer Data Flow

**Figure 4 Description**: Runtime data forwarded to Analyzer

**UML Element**: Note attached to "Extract features / state vector" activity in MAPE-K Monitor partition

**Process Step**:
- **Source Activity**: `Extract features / state vector` (in MAPE-K Monitor)
- **Destination Activity**: `Analyze monitored data` (in MAPE-K Analyze)
- **Partitions**: MAPE-K Monitor → MAPE-K Analyze

**Flow Direction**: MAPE-K Monitor → MAPE-K Analyze

**Context**: The Monitor processes collected runtime data and extracts features/state vectors, which are then forwarded to the Analyzer. The Analyzer uses this data to determine if adaptation goals are being violated or are at risk.

---

### Arrow (5): Analyzer to Planner Notification

**Figure 4 Description**: Analyzer notifies Adaptation Option Predictor

**UML Element**: Note attached to "Notify Planner" activity in MAPE-K Analyze partition

**Process Step**:
- **Source Activity**: `Notify Planner` (in MAPE-K Analyze)
- **Destination Activity**: Planning activities (in MAPE-K Plan)
- **Partitions**: MAPE-K Analyze → MAPE-K Plan
- **Trigger Condition**: Goals violated or at risk (yes branch of decision node)

**Flow Direction**: MAPE-K Analyze → MAPE-K Plan

**Context**: When the Analyzer determines that adaptation goals are violated or at risk, it notifies the Planner (Adaptation Option Predictor). This triggers the planning phase where the best adaptation option will be selected.

---

### Arrow (6): Model Retrieval for Planning

**Figure 4 Description**: Predictor retrieves trained RS-DRL model

**UML Element**: Note attached to "Retrieve trained model" activity in MAPE-K Plan partition

**Process Step**:
- **Activity**: `Retrieve trained model`
- **Partition**: MAPE-K Plan (Adaptation Option Predictor)
- **Source**: Knowledge Repository (where model was stored via Arrow 3)

**Flow Direction**: Knowledge Repository → MAPE-K Plan

**Context**: The Adaptation Option Predictor retrieves the trained RS-DRL model from the Knowledge Repository. This model will be used to predict the best adaptation option based on the current system state.

---

### Arrow (7): Adaptation Option Prediction

**Figure 4 Description**: Adaptation option predicted

**UML Element**: Note attached to "Predict best adaptation option" activity in MAPE-K Plan partition

**Process Step**:
- **Activity**: `Predict best adaptation option`
- **Partition**: MAPE-K Plan (Adaptation Option Predictor)
- **Position**: After retrieving trained model

**Flow Direction**: MAPE-K Plan → (prediction result available)

**Context**: Using the retrieved trained RS-DRL model, the Adaptation Option Predictor predicts the best adaptation option for the current system state. This prediction is based on the learned policy from the DQN.

---

### Arrow (8): Adaptation Details Retrieval

**Figure 4 Description**: Executor retrieves adaptation option details

**UML Element**: Note attached to "Retrieve adaptation details" activity in MAPE-K Execute partition

**Process Step**:
- **Source Activity**: `Predict best adaptation option` (in MAPE-K Plan)
- **Destination Activity**: `Retrieve adaptation details` (in MAPE-K Execute)
- **Partitions**: MAPE-K Plan → MAPE-K Execute

**Flow Direction**: MAPE-K Plan → MAPE-K Execute

**Context**: After the adaptation option is predicted, the Executor retrieves the detailed information about the selected adaptation option. This includes the specific actions needed to implement the adaptation.

---

### Arrow (9): Adaptation Application

**Figure 4 Description**: Adaptation applied to managed system

**UML Element**: Note attached to "Apply adaptation to Managed System" activity in MAPE-K Execute partition

**Process Step**:
- **Activity**: `Apply adaptation to Managed System`
- **Partition**: MAPE-K Execute
- **Position**: After retrieving adaptation details

**Flow Direction**: MAPE-K Execute → Managed System

**Context**: The Executor applies the selected adaptation to the Managed System. This changes the system's behavior, configuration, or structure according to the predicted adaptation option. This completes one adaptation episode, and the cycle can repeat.

---

## Summary Table

| Arrow | Flow | Source Partition | Destination Partition | UML Activity/Element |
|-------|------|-----------------|---------------------|---------------------|
| (1) | Runtime data produced | Managed System | - | "Produce runtime data" activity |
| (2) | Monitor → RS-DRL | MAPE-K Monitor | RS-DRL Module | Flow to "Receive state vector" |
| (3) | Model storage | RS-DRL Module | Knowledge Repository | "Store trained model" activity |
| (4) | Monitor → Analyzer | MAPE-K Monitor | MAPE-K Analyze | Flow to "Analyze monitored data" |
| (5) | Analyzer → Planner | MAPE-K Analyze | MAPE-K Plan | "Notify Planner" activity |
| (6) | Model retrieval | Knowledge Repository | MAPE-K Plan | "Retrieve trained model" activity |
| (7) | Option prediction | MAPE-K Plan | - | "Predict best adaptation option" activity |
| (8) | Details retrieval | MAPE-K Plan | MAPE-K Execute | Flow to "Retrieve adaptation details" |
| (9) | Adaptation application | MAPE-K Execute | Managed System | "Apply adaptation" activity |

## Traceability in Academic Writing

When writing about the diagram, you can reference specific arrows to maintain traceability:

- **"As indicated by arrow (1), the managed system produces runtime data..."**
- **"The flow from Monitor to RS-DRL (arrow 2) enables continuous learning..."**
- **"When goals are violated, the Analyzer triggers planning (arrow 5)..."**
- **"The Executor applies the predicted adaptation (arrow 9) to complete the cycle..."**

This mapping ensures that every element in the process diagram can be traced back to the original Figure 4, providing full auditability for academic or research purposes.

