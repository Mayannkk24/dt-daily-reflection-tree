# 🌳 THE DAILY REFLECTION TREE
=========================================
### **Project Status: COMPLETE | Deterministic Knowledge Engine**

## **1. PROJECT OVERVIEW**
-----------------------------------------
This is a **Knowledge Engineering** prototype built for the DT Fellowship Assignment. It is a structured, end-of-day reflection tool that guides employees through a conversation to evaluate their mindset. 

The core of this project is **DETERMINISM**. Unlike a standard AI chatbot, this system uses a pre-defined logical tree to ensure that the reflection is:
* **PREDICTABLE:** Same answers always lead to the same insights.
* **AUDITABLE:** Every branch can be traced back to a specific psychological framework.
* **TRUSTWORTHY:** Zero risk of AI "hallucination" at runtime.

## **2. THE THREE PSYCHOLOGICAL AXES**
-----------------------------------------
The tree is architected to move the employee through three specific spectrums in a strict sequence:

### **AXIS 1: LOCUS (VICTIM ↔ VICTOR)**
* **FRAMEWORK:** Julian Rotter’s *Locus of Control*.
* **GOAL:** Surface whether the employee sees themselves as an agent of change or a victim of circumstances.

### **AXIS 2: ORIENTATION (ENTITLEMENT ↔ CONTRIBUTION)**
* **FRAMEWORK:** *Organizational Citizenship Behavior (OCB)*.
* **GOAL:** Make visible the shift from "What am I owed?" to "What did I give?" without moralizing or shaming.

### **AXIS 3: RADIUS (SELF-CENTRISM ↔ ALTROCENTRISM)**
* **FRAMEWORK:** Maslow’s *Self-Transcendence*.
* **GOAL:** Expand the radius of concern from personal stress to the success of the team and the end-user.

## **3. FOLDER STRUCTURE**
-----------------------------------------

```text
DailyReflectionTree/
├── tree/
│   ├── reflection-tree.json      <-- The "Brain" (Deterministic Data)
│   └── tree-diagram.md           <-- The Visual Logic Flow (Mermaid)
├── agent/
│   └── main.py                   # The Engine (Zero-Dependency Python)
├── transcripts/
│   ├── victor-run.md             # Successful "High Agency" path logs
│   └── victim-run.md             # Struggling "Low Agency" path logs
├── write-up.md                   # Technical and Psychological rationale
└── README.md                     # Documentation

4. EXECUTION INSTRUCTIONS
This agent was developed to be lightweight and portable. It requires no external libraries.

PREREQUISITES
Python 3.x installed.

STEPS TO RUN
Open your terminal.

Navigate to the agent directory:

PowerShell
cd agent
Execute the runner:

PowerShell
python main.py
5. DESIGN & AI COLLABORATION
In strict alignment with the assignment guidelines:

AI AS A POWER TOOL: I utilized LLMs (Gemini/ChatGPT) to iterate on the phrasing of "Reflection Nodes" to ensure the tone felt like a "wise colleague" rather than a manager.

GUARDRAILS AGAINST HALLUCINATION: By encoding the intelligence into a static JSON schema, I ensured the product never "hallucinates" or gives inconsistent feedback.

STRATEGIC DISAGREEMENT: The AI originally suggested allowing free-text input for a better "user experience." I REJECTED this to maintain the deterministic requirement, as free-text requires LLM classification which introduces ambiguity and error.