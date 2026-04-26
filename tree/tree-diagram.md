# Visual Logic Map: Daily Reflection Tree

```mermaid
graph TD
    %% Axis 1: Locus of Control
    START((Start)) --> A1_Q1{A1: Handling Friction}
    A1_Q1 -->|Internal| A1_R_INT[Reflection: Agency]
    A1_Q1 -->|External| A1_R_EXT[Reflection: Constraints]
    
    A1_R_INT --> BRIDGE1(Bridge to Axis 2)
    A1_R_EXT --> BRIDGE1

    %% Axis 2: Orientation
    BRIDGE1 --> A2_Q1{A2: Team Contribution}
    A2_Q1 -->|High Effort| A2_R_CON[Reflection: OCB Detected]
    A2_Q1 -->|Minimalist| A2_R_ENT[Reflection: Entitlement Risk]
    
    A2_R_CON --> BRIDGE2(Bridge to Axis 3)
    A2_R_ENT --> BRIDGE2

    %% Axis 3: Radius
    BRIDGE2 --> A3_Q1{A3: Focal Point}
    A3_Q1 -->|Self| A3_R_SELF[Reflection: Narrow Radius]
    A3_Q1 -->|Others| A3_R_ALT[Reflection: Transcendent]
    
    A3_R_SELF --> SUMMARY{Summary Logic}
    A3_R_ALT --> SUMMARY
    
    %% Output
    SUMMARY -->|Synthesis| END((End Session))

    ---

### 2. `transcripts/` Section
You need two files here to show the agent works. Create the `transcripts` folder and save these two files.

#### **File 1: `transcripts/victor-run.md` (The "High Agency" Path)**
```markdown
# Sample Transcript: The Catalyst Persona

**[SYSTEM]:** Welcome. Let's decode today's events into growth signals.
**[SYSTEM]:** Think of a moment today where things felt 'stuck'. What was your first thought?
**USER:** 1. I need to find a workaround.

**[SYSTEM]:** You're seeing the 'internal lever'. Even in friction, you maintain the driver's mindset.
**[SYSTEM]:** Shifting focus: From your power to your presence in the team...
**[SYSTEM]:** Which of these captures your 'extra' effort today?
**USER:** 1. I cleaned up a process/mess I didn't create.

**[SYSTEM]:** That is Organizational Citizenship. You are investing in the ecosystem, not just your role.
**[SYSTEM]:** Final scan: The radius of your concern.
**[SYSTEM]:** When you imagine today's work 'winning', who is smiling in your head?
**USER:** 3. The end-user—their pain point was solved.

**[SYSTEM]:** CORE SIGNALS:
- Locus: Internal
- Orientation: Contribution
- Radius: Altrocentric
**Synthesis:** You operated as a **Catalyst (High Agency + High Team Focus)**.
File 2: transcripts/victim-run.md (The "Low Agency" Path)
Markdown
# Sample Transcript: The Passenger Persona

**[SYSTEM]:** Welcome. Let's decode today's events into growth signals.
**[SYSTEM]:** Think of a moment today where things felt 'stuck'. What was your first thought?
**USER:** 2. I'm waiting for clearance/help.

**[SYSTEM]:** Acknowledge the external constraints, but don't let them define your perimeter of action.
**[SYSTEM]:** Shifting focus: From your power to your presence in the team...
**[SYSTEM]:** Which of these captures your 'extra' effort today?
**USER:** 3. I felt my time was wasted on others' incompetence.

**[SYSTEM]:** Protecting your time is vital, but ensure your boundaries don't become barriers.
**[SYSTEM]:** Final scan: The radius of your concern.
**[SYSTEM]:** When you imagine today's work 'winning', who is smiling in your head?
**USER:** 1. Me—I feel competent and secure.

**[SYSTEM]:** CORE SIGNALS:
- Locus: External
- Orientation: Entitlement
- Radius: Self
**Synthesis:** You operated as a **Passenger (Low Agency - Needs re-centering)**.