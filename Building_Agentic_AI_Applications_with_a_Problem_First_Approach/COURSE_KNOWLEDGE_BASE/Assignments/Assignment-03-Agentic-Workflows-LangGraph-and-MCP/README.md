# Assignment 3 — Perplexia AI Part 3: Autonomous Agents, Deep Research & Model Context Protocol (MCP)

## What is this assignment?
Assignment 3 represents the apex of the hands-on curriculum. You transform Perplexia AI from a predefined workflow into an **autonomous agentic system** where planning, tool selection, task decomposition, and loop termination are dynamically handled by the AI. You build a dynamic **Tool-Using Agent**, an **Agentic RAG pipeline**, and a multi-agent **Deep Research System**. Furthermore, you implement and connect a custom **Model Context Protocol (MCP)** server, making Perplexia fully extensible using open industry protocols.

## What you need to do
- **Part 1 (Tool-Using Agent & MCP Integration):** Replace hardcoded routers with an autonomous ReAct agent using `bind_tools`. Create a custom MCP server (e.g., Bookmarking or Math server) exposing tools over JSON-RPC.
- **Part 2 (Agentic RAG):** Implement autonomous document research where the agent inspects retrieved documents, realizes what information is missing, reformulates queries, and searches iteratively until the research goal is satisfied.
- **Part 3 (Deep Research Multi-Agent System):** Build a multi-agent collaborative system:
  - *Lead Researcher / Planner Agent:* Decomposes research questions into sub-topics.
  - *Web & Document Search Agent:* Executes multi-source retrieval.
  - *Fact Checker / Critic Agent:* Validates consistency and flags discrepancies.
  - *Report Writer Agent:* Compiles findings into an executive briefing with citations.
- **Part 4 (Testing & Self-Evaluation):** Develop a domain-specific evaluation benchmark with multi-step reasoning queries.

## Concepts being practiced
- ReAct Agent Execution Loops (`create_react_agent` / StateGraph)
- Model Context Protocol (MCP) Client & Server Architecture
- Agentic RAG (Self-directed iterative query expansion)
- Multi-Agent Orchestration (Supervisor Pattern)
- Context Management & Infinite Loop Prevention

## Related Course Lessons
- Lesson `069`: [Core] Lecture 7: Types of Agents & AI Protocols
- Lesson `070`: [Core] Lecture 8: Planning in Agents (ReAct Prompting)
- Lesson `071`: [Core] Lecture 9: Multi-Agent Systems, AIOps & Fine-Tuning
- Lessons `084`, `085`: Assignment 3 Specifications (LangGraph & LangFlow)
- Lesson `087`: [Build][Bonus] Using and Building MCP Servers

## Difficulty / Scope
- **Difficulty:** Advanced
- **Estimated Completion Time:** 8–12 hours
- **Model Recommendation:** Use `gpt-4o` (not mini) for reliable tool-calling and planning precision.

## Important Links
- [Assignment Specifications](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Agentic-Workflows-LangGraph-and-MCP/assignment.md)
- [Official Solution Guide](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Agentic-Workflows-LangGraph-and-MCP/solution.md)
- [Starter Code Package (Google Drive)](https://drive.google.com/drive/folders/1nLPfsGQnqFNpfhocr1JcAU2g183LxDQV?usp=drive_link)
- [Model Context Protocol GitHub](https://github.com/modelcontextprotocol/servers)
- [LangGraph Agentic RAG Documentation](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/)

## Solution
Official walkthrough videos and full source code are provided. See [solution.md](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Agentic-Workflows-LangGraph-and-MCP/solution.md).
