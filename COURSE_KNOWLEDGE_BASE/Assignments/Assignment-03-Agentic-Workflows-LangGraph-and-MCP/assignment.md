# Assignment 3: Detailed Specifications & Requirements

## Architecture: Autonomous Deep Research Multi-Agent System

```
                      [User Research Topic]
                                │
                                ▼
                     [Research Planner Agent]
                    (Decompose into 3 Sub-Tasks)
                                │
                                ▼
                    [Supervisor / Coordinator]
                   /            |             \
                  ▼             ▼              ▼
           [Search Sub-Agent] [Doc Sub-Agent] [MCP Tool Server]
                  \             |              /
                   \            |             /
                    ▼           ▼            ▼
                   [Fact-Checking / Critic Agent]
                    (Checks consistency & gaps)
                                │
                                ▼
                     [Executive Report Writer]
                    (Structured Markdown Output)
```

---

## Technical Specifications

### Part 1: Autonomous Tool-Using Agent & Custom MCP Server
1. **Dynamic Tool Calling:** Use `ChatOpenAI(model="gpt-4o").bind_tools([calculator_tool, tavily_tool, document_retriever])`.
2. **Custom MCP Server:**
   - Create a custom MCP server script (`bookmarking_mcp_server.py` or `math_server.py`).
   - Implement tools: `add_bookmark(title, url, notes)` and `search_bookmarks(query)`.
   - Connect your LangGraph agent to the MCP client to dynamically discover and invoke MCP server endpoints.

### Part 2: Agentic RAG
1. Implement a self-directed retrieval loop. If the model receives retrieved text that does not answer the core question, it must formulate a refined sub-query rather than producing a fallback hallucination.
2. Cap the loop at a maximum of `max_iterations = 4` to prevent infinite execution cycles.

### Part 3: Deep Research System
1. Build a multi-agent StateGraph with at least three distinct roles:
   - **Planner:** Generates a structured research agenda.
   - **Researcher:** Iteratively queries web and local document vectors.
   - **Writer:** Synthesizes facts, resolves conflicting claims, and structures the final output with footnotes and links.

---

## Evaluation Benchmark & Requirements
- **Complex Query 1:** *"Perform a comprehensive competitive analysis of OpenAI vs Anthropic's enterprise strategies in 2024-2025, detailing model pricing, tool protocols (MCP), and enterprise security guarantees."*
- **Complex Query 2:** *"Analyze our company's annual reports from 2019-2022 to track operating margin trends, and cross-reference with current industry benchmarks found on the web."*
- **Deliverable:** Full Python package (`perplexia_ai/week3/`) and demonstration notebook or LangFlow JSON exports.
