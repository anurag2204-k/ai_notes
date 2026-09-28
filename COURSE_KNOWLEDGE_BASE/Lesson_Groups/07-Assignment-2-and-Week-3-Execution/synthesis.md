# Module / Lesson Group 07
## Lessons 056–068: Assignment 2 Implementation: Corrective RAG (CRAG), Tavily Search & LangGraph

### Big Picture
Implementing Perplexia AI Part 2. Students construct a cyclic LangGraph StateGraph combining internal PDF knowledge retrieval, relevance evaluation, and live web search fallbacks via Tavily. Accompanied by Assignment 1 solution walkthroughs, Comet Opik tracing setup, venture capital AMAs, and intensive office hours.

### Conceptual Flow
```
Assignment 1 Solutions (056) → Assignment 2 LangGraph Specs (057) → Assignment 2 LangFlow Specs (058) → Tavily Search Setup (059) → Assignment 2 Test Cases (060) → Comet Opik Observability (061) → Troubleshooting Guide (062) → Guest Lecture: AI Future [Pritika Mehta] (063) → Homework Office Hours (Aug 13): CRAG Routing (064) → AMA: VC Landscape [Jaya Gupta] (065) → Content Office Hours (Aug 14/15): Evaluation (066) → Content Office Hours (Aug 16): Multimodal (067) → Homework Office Hours (Aug 16): Finalizing A2 (068)
```

Students review the Assignment 1 solution (056) to ensure solid footing, follow specifications for Assignment 2 (057-060), set up observability with Comet Opik (061), and resolve StateGraph routing challenges during live office hours (064, 066-068).

### Key Ideas
- **Cyclic execution in LangGraph:** Managing nodes, state transitions, and conditional edge decisions.
- **Relevance evaluator node:** Grading document chunks and setting boolean flags (`web_search=True`).
- **Tavily Search API:** Fetching clean, LLM-optimized web snippets to answer questions beyond internal documentation.
- **Observability with Comet Opik:** Tracing token expenditure across multi-node LangGraph runs.

### How the Pieces Fit Together
Elevates Perplexia AI from a calculator bot to an enterprise research engine, providing the exact state graph patterns needed for Assignment 3.

### What You Should Know After This Section
- How to define typed dictionaries (`AgentState`) for LangGraph execution.
- How to write deterministic conditional routing functions in LangGraph.
- How to pass all Assignment 2 test cases across internal documents and live web search.
- How venture capital evaluates generative AI startups and defensibility.

### Related Assignments
- Complete and submit **Assignment 2** (Perplexia AI Part 2).

### Important Resources
- [Assignment 2 Workspace](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Enterprise-RAG-and-Tavily-Search/README.md)
- [PDF Dataset Folder](https://drive.google.com/drive/folders/1h-g9aBIa9FWX6Afe2NCxzVkdusokmJpY?usp=sharing)

