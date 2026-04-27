
> ❌ **Do NOT keep long, monolithic process-flow diagrams like this in the main chapter.**
> ✅ **Decompose them and align each diagram strictly with its intended section.**

Now let me explain *why* and  *how* , from a supervisor/examiner point of view.

---

## Why this diagram is a problem (even though it’s correct)

The diagram you showed is:

* Technically solid
* Logically consistent
* Well-labeled

**But** it violates two important thesis principles.

### 1. Cognitive overload

An examiner sees this and thinks:

> “I need to read labels, follow arrows, understand states, and remember where I am in the chapter… all at once.”

Long vertical flows:

* Are hard to scan
* Break reading rhythm
* Force back-and-forth between text and figure

Examiners  **do not study figures** , they *consult* them.

---

### 2. Misalignment with chapter structure

You said something crucial:

> *“I want to show each block of process flow in its intended section.”*

Right now, the figure:

* Spans  **monitoring** ,  **preprocessing** ,  **state construction** , **validation**
* But appears as **one visual artifact**

That creates a mismatch:

* **Text is modular**
* **Figure is monolithic**

This is a structural smell.

---

## What examiners expect instead (this is key)

At PhD level, examiners expect:

> **One figure = one conceptual responsibility**

Not:

> “One figure = the whole pipeline”

---

## The best solution (strong recommendation)

### ✅ **Split the process into multiple sectional figures**

Instead of one long diagram, do this:

---

### Figure 5.x.1 — Monitoring and Raw Data Acquisition

*(Section 5.5: Runtime Monitoring and State Construction)*

Shows only:

* Raw data sources
* Metric acquisition
* Initial normalization

👉 Short, readable, contextual

---

### Figure 5.x.2 — Preprocessing and Feature Engineering

*(Still Section 5.5)*

Shows:

* Filtering
* Feature extraction
* Uncertainty annotation (if relevant)

👉 This is where uncertainty starts to appear

---

### Figure 5.x.3 — State Vector Construction and Validation

*(Section 5.6 or 5.6.1)*

Shows:

* State assembly
* Validation rules
* Output as “validated state vector”

👉 This directly feeds decision-making

---

### Optional (Appendix):

**Figure A.1 — End-to-End Monitoring and State Construction Workflow**

This can look  **exactly like the long diagram you already have** .

📌 This is critical:

* You do **not lose information**
* You **gain readability**
* You **signal architectural judgment**

---

## What NOT to do (important)

❌ Do not shrink the diagram to “make it fit”
→ unreadable, examiners hate this

❌ Do not rotate it sideways
→ classic thesis anti-pattern

❌ Do not keep it intact “because it’s accurate”
→ accuracy ≠ usability

---

## How this maps perfectly to your Chapter 5 skeleton

This approach aligns *beautifully* with:

* **Alternative 1** (architecture + appendices)
* **Alternative 2** (clean examiner-safe)

Main chapter:

* Short, section-specific figures

Appendix:

* Full end-to-end workflows

---

## What your supervisor would likely say (verbatim-style)

If you asked them directly, they would say something like:

> “Break it down. I don’t want to decode a poster while reading a chapter.”

---

## Final recommendation (clear and firm)

✅ **Decompose long process-flow diagrams**
✅ **Place each sub-diagram inside its corresponding section**
✅ **Move the full pipeline diagram to an appendix**
✅ **Reference the appendix figure from the section text**

This is **not dumbing down** — it is  **PhD-level clarity** .
