# Assignment 2 Official Solutions

## Official Solution Assets
- **Video Walkthroughs:** `117 [Build] Assignment 2 Solutions 1.mp4` & `118 [Build] Assignment 2 Solutions 2.mp4`
- **Official Solution Code:** Located in `Cohort 3 - Students.zip` -> `Cohort 3 - Students/Assignment 2 - Solutions/`:
  - `LangGraph/code/perplexia_ai/week2/`
    - `part1.py` (Vector store RAG)
    - `part2.py` (Tavily search integration)
    - `part3.py` (Complete LangGraph CRAG StateGraph)
    - `prompts.py` (Document grader and query rewriter prompts)
  - `LangFlow/`
    - `Assignment 2 - Part 1 Solution.json`
    - `Assignment 2 - Part 3 Solutions.json`
- **Google Drive Solutions Link:** [Assignment 2 Solutions Drive](https://drive.google.com/drive/folders/18nh4lZq8mZbPTburDwne5JUnFYU131By?usp=drive_link)

## What the Solution Demonstrates
- Strict document grading using Pydantic output parsers (`score: Literal['yes', 'no']`).
- Building the StateGraph with `StateGraph(AgentState)` and adding conditional edges via `graph.add_conditional_edges()`.
- Instrumenting Opik callbacks: passing `opik_tracer` to monitor LLM token costs across the grading and generation stages.
