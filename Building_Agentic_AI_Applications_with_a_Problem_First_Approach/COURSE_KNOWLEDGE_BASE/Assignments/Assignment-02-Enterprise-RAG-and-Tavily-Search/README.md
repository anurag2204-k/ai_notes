# Assignment 2 — Perplexia AI Part 2: Enterprise RAG, Web Search & Corrective Routing

## What is this assignment?
In Assignment 2, you advance **Perplexia AI** from a simple calculator/memory assistant into a knowledge-grounded enterprise research tool. You integrate two critical data sources: an internal document collection (multi-year enterprise annual performance report PDFs) and real-time external knowledge via the Tavily Search API. Crucially, you implement **Corrective RAG (CRAG)** in **LangGraph**, enabling the system to evaluate retrieved internal documents and fallback gracefully to live web search when internal data is insufficient.

## What you need to do
- **Part 1 (Document Ingestion & Vector RAG):** Ingest annual performance reports (PDFs), chunk them using semantic strategies, index them into ChromaDB/InMemoryVectorStore with OpenAI embeddings, and build an internal retrieval tool.
- **Part 2 (Live Web Search):** Integrate the Tavily Search API to execute real-time web queries with snippet summarization.
- **Part 3 (Corrective RAG - CRAG Routing):** Build a LangGraph cyclic StateGraph with:
  - Document retrieval node.
  - Document relevance evaluator / grading node (LLM as judge assessing whether retrieved chunks answer the query).
  - Conditional edge: If relevant, proceed to generation; if irrelevant or ambiguous, route to Tavily web search.
  - Final answer generation grounded in verified sources with citations.
- **Part 4 (Observability):** Instrument your pipeline with Comet Opik to trace execution steps, latency, and token consumption.

## Concepts being practiced
- Document Chunking, Embedding Models & Vector Stores
- Hybrid Internal vs External Knowledge Routing
- Corrective Retrieval-Augmented Generation (CRAG)
- LangGraph StateGraph, Nodes, Edges, and Conditional Branching
- Observability and Pipeline Tracing (Comet Opik)

## Related Course Lessons
- Lessons `044` & `045`: [Core] Enterprise RAG in 2025 & Advanced RAG / Memory
- Lesson `046`: [Core] Context Engineering in Agents
- Lessons `057`, `058`, `059`, `060`: Assignment 2 Specifications & Tavily Setup
- Lesson `061`: [Build] Comet Opik Setup for LangGraph Tracing

## Difficulty / Scope
- **Difficulty:** Intermediate to Advanced
- **Estimated Completion Time:** 6–8 hours
- **Prerequisites:** Completion of Assignment 1, Tavily API Key, OpenAI API Key, LangGraph installed.

## Important Links
- [Assignment Specifications](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Enterprise-RAG-and-Tavily-Search/assignment.md)
- [Official Solution Guide](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Enterprise-RAG-and-Tavily-Search/solution.md)
- [CRAG Research Paper (arXiv:2401.15884)](https://arxiv.org/abs/2401.15884)
- [Tavily Search API Documentation](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)
- [Comet Opik GitHub](https://github.com/comet-ml/opik)

## Solution
Official solutions and video walkthroughs are available. See [solution.md](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Enterprise-RAG-and-Tavily-Search/solution.md).
