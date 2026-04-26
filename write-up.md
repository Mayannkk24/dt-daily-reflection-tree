# Design Rationale: The Reflection Insight Engine

### 1. Psychological Architecture
Instead of basic questions, I implemented a **forced-choice model**. By removing "neutral" options, the tree forces the user to confront their bias toward agency or entitlement. 
- **Axis 1 (Rotter):** Focuses on the 'First Thought'—detecting reflexive locus before cognitive filtering.
- **Axis 3 (Maslow):** Uses 'Mental Imagery' (who is smiling in your head) to detect Radius of Concern.

### 2. Knowledge Engineering vs. AI
While AI (Gemini) was used to iterate on the "Reflection" nodes to ensure an empathetic, non-moralizing tone, the **State Management Engine** is 100% deterministic. 
- **Hallucination Control:** By using a schema-based JSON, I've eliminated the possibility of the agent suggesting invalid psychological advice.
- **Persona Synthesis:** I added a "Persona" logic layer that combines signals across axes to provide a holistic view (e.g., "The Catalyst" vs "The Solo Performer").

### 3. Trade-offs & Craft
I chose a CLI with ASCII progress bars because reflection tools should be distraction-free. The data is separated from the code, meaning this tree could be swapped for a "Leadership Tree" or a "Technical Troubleshooting Tree" without changing the code.