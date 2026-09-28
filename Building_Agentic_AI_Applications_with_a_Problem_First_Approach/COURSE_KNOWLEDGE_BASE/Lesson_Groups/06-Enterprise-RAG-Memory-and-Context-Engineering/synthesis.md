# Module / Lesson Group 06
## Lessons 044–055: Enterprise RAG Architecture, Agent Memory Mechanisms & Context Engineering

### Big Picture
Mastering the knowledge foundation of enterprise AI. Moving far beyond naive vector search, this module covers production RAG pipelines, semantic chunking, HyDE query expansion, Corrective RAG (CRAG), GraphRAG, and long-term agent memory architectures.

### Conceptual Flow
```
Core Lecture 5: Enterprise RAG in 2025 (044) → Core Lecture 6: Advanced RAG & Memory (045) → Core Lecture: Context Engineering (046) → Enterprise RAG Guest Lectures (047) → Vector Databases Deep Dive (048) → RAG Evaluation Metrics & Ragas (049) → RAG Optimizations: Semantic Caching & CRAG (050) → Multimodal RAG (051) → GraphRAG Deep Dive (052) → Reading RAG Papers (053) → Agent Memory Frameworks (054) → Landmark Memory Papers: Reflexion & MemGPT (055)
```

Lecture 5 details the end-to-end RAG pipeline and retrieval mathematics. Lecture 6 introduces advanced CRAG and memory structures. Lecture 7 (Context Engineering) optimizes context window attention. The deep dives (047-055) cover vector stores (HNSW), evaluation metrics (Ragas), knowledge graphs (GraphRAG), and episodic memory architectures.

### Key Ideas
- **Garbage In, Garbage Out:** Document parsing and chunking quality dictates 80% of RAG accuracy.
- **Corrective RAG (CRAG):** Ingested documents must be evaluated for relevance before generation; if inadequate, fallback to web search.
- **Hybrid Search:** Combining dense semantic embeddings with sparse keyword BM25 to capture both concepts and exact acronyms/IDs.
- **Agent Memory Hierarchy:** Working context (short-term) vs episodic reflection (medium-term) vs vector user profiles (long-term).
- **Context window budgeting:** Attention degrades over large contexts ('lost in the middle'); prune and prioritize high-signal tokens.

### How the Pieces Fit Together
Establishes the technical foundation for **Assignment 2** (Perplexia AI Part 2), where students implement CRAG routing and document search in LangGraph.

### What You Should Know After This Section
- How to calculate and interpret Ragas metrics (Context Precision, Recall, Faithfulness).
- How the HyDE algorithm generates hypothetical answers to bridge query-document semantic gaps.
- How GraphRAG extracts entities to answer global corpus-wide questions.
- How memory reflection works in the Reflexion framework.

### Related Assignments
- Prepare for Assignment 2: Ingest the annual performance report PDFs and configure vector embeddings.

### Important Resources
- [Lecture 5 Slides (Canva)](https://www.canva.com/design/DAGpcmXbA04/t7rqjR4Gzi19GjA0XUN4_Q/view?utm_content=DAGpcmXbA04&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h9d21093bd3)
- [Lecture 6 Slides (Canva)](https://www.canva.com/design/DAGpn4N8zs4/9V9Q_vg5v62jpLnbXks30g/view?utm_content=DAGpn4N8zs4&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h143e1b5d76)
- [CRAG Research Paper](https://arxiv.org/abs/2401.15884)

