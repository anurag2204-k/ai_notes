# Assignment 3 — Autonomous Agent, LangGraph & Tool Calling — Requirements & Specification

### Objectives
Build an autonomous decision-making agent that decides when to retrieve, rewrites queries, and validates output sufficiency before replying.

### Requirements & Constraints
1. **LangGraph State Schema**: Define `State` containing:
   - `messages: Annotated[List[Any], add]`
   - `question_relevant: bool`
   - `iteration: int`
   - `answer: str`
   - `final_answer: bool`
   - `references: Annotated[List[RAGUsedContext], add]`
2. **Intent Router**: Use a lightweight model or prompt to classify `question_relevant`. Route irrelevant queries directly to `END`.
3. **ToolNode**: Bind `get_formatted_item_context` to the agent node.
4. **Conditional Edge (`tool_router`)**:
   - Route to `tools` if tool calls are present in the last message and `iteration <= 2`.
   - Route to `end` if `final_answer` is true, iteration limit exceeded, or no tool calls remain.
5. **Backend Deployment**: Package the graph into `apps/api` and expose via REST endpoint.

### Expected Deliverables
- Exploration notebooks: `01-LangGraph-Intro.ipynb`, `02-Query-Rewriting.ipynb`, `03-Router.ipynb`, `04-Agent-Single-Turn.ipynb`.
- Production backend graph: `apps/api/src/api/agents/graph.py`.
