# Module / Lesson Group 04
## Lessons 023–034: Modern Prompt Engineering, Structured Outputs & Enterprise Workflow Agents

### Big Picture
Transitioning from free-form prompting to deterministic software pipelines. This module covers advanced prompt engineering in 2025, structured JSON/Pydantic outputs, automatic prompt optimization (DSPy), and the architecture of Level 2 Workflow Agents that use deterministic code to route queries and call tools.

### Conceptual Flow
```
Core Lecture 3: Prompt Engineering in 2025 (023) → Core Lecture 4: Enterprise Workflow Agents (024) → Skill-Based Prompting Deep Dive (025) → Automatic Prompt Optimization / DSPy (026) → Prompting Reasoning Models (027) → Prompt Engineering Papers (028) → Enterprise Workflow Architectures (029) → Workflow Evaluation (030) → LLM-as-a-Judge Masterclass (031) → Production Guardrails (032) → Model Context Protocol Intro (033) → Building Agentic AI in 2025 (034)
```

Lecture 3 teaches precise model steering and structured outputs. Lecture 4 wraps those outputs into directed workflow chains. Deep dives (025-034) cover automated tuning (DSPy), reasoning model behavior, evaluation metrics (LLM-as-a-judge), safety guardrails, and standardize tools via MCP.

### Key Ideas
- **Structured outputs are non-negotiable in production:** Always enforce Pydantic/JSON schemas.
- **Workflow Agents (Level 2) are deterministic:** The LLM classifies intent, but hardcoded software routes the execution graph.
- **Automated Prompt Optimization (DSPy):** Compiling prompts algorithmically rather than manual trial-and-error.
- **Guardrails:** Layered defense comprising input validation (regex/PII), prompt guards, and output hallucination verifiers.

### How the Pieces Fit Together
Provides the complete architectural blueprint for **Assignment 1** (Perplexia AI Part 1), where students build a routing agent with memory and tool binding.

### What You Should Know After This Section
- How to force OpenAI models to emit verified JSON adhering to a Pydantic model.
- How to construct a query routing chain in LangChain and LangFlow.
- How to design an LLM-as-a-judge prompt with clear rubrics to avoid scoring drift.
- The architectural role of Model Context Protocol (MCP) in tool discovery.

### Related Assignments
- Prepare for Assignment 1: Design the classification prompt and tool interfaces for Perplexia AI.

### Important Resources
- [Lecture 3 Slides (Canva)](https://www.canva.com/design/DAGosETX17k/uaZhBToUArMTGDOmJCIx2w/view?utm_content=DAGosETX17k&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h4e96cc3f6b)
- [Lecture 4 Slides (Canva)](https://www.canva.com/design/DAGo44zNruc/geNXs6giP4l7HoiAWbTabA/view?utm_content=DAGo44zNruc&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h343ac51335)

