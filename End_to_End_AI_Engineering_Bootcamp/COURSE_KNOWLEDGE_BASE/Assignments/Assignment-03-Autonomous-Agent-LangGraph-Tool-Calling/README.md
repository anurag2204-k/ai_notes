# Assignment 3 — Autonomous Agent, LangGraph & Tool Calling

## What is this assignment?

Transform the static RAG pipeline into an autonomous agent using LangGraph. Implement a state machine featuring an Intent Router node to filter irrelevant queries, a Query Expansion node for complex questions, an Agent reasoning node, and a ToolNode wrapping the hybrid retrieval engine into a cyclical ReAct loop.

## What you need to do

- Construct foundational cyclical graphs using LangGraph `StateGraph` and custom Pydantic state schemas.
- Implement a Query Expansion node that rewrites multi-intent user questions into optimized retrieval queries.
- Build an Intent Router node that classifies queries into shopping questions vs. generic conversation, routing non-shopping questions to immediate termination.
- Wrap the Qdrant hybrid retrieval engine as a standardized tool callable via LLM function calling.
- Implement a ReAct agent loop connecting agent reasoning to the ToolNode with loopback edges.
- Migrate the compiled LangGraph workflow into `apps/api/src/api/agents/graph.py`.

## Concepts practiced

- LangGraph StateGraph & State Reducers (`operator.add`)
- Intent Router & Guardrail Nodes
- Query Expansion & Rewriting
- Tool Definition & Binding (`ToolNode`)
- ReAct Decision Loop & Conditional Routing

## Related Section

Section 2 — Agents & Agentic Systems

## Related Lessons

- 001 Agent architecture and decision loops
- 002 Tool use in agents
- 003 Patterns for building Agentic Systems
- 004 Memory in agent systems
- 005 Reflection & Agent evaluation Frameworks

## Important Resources

- [006 Hands-on Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%202%20–%20Agents%20&%20Agentic%20Systems/006%20Hands-on%20Section.html)
- [Sprint-2-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-2-info-review.pdf)
- [028 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/028%20JAN%2027%20Sprint%20Review%20Autonomous%20Agents.mp4)
- [031-036 Hands-on Videos 1-6](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)

## Solution

Official solution walkthroughs, reference notebooks, and production code files are detailed in [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Autonomous-Agent-LangGraph-Tool-Calling/solution.md).

