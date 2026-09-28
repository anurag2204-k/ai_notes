# Master Concept Map & Technical Taxonomy

This document maps the core engineering mental models and technical architecture underpinning the End-to-End AI Engineering Bootcamp. It visualizes how concepts progress from data foundations and vector retrieval to autonomous agent loops, multi-agent coordination, and production reliability.

---

## 1. High-Level Course Architecture

```
End-to-End AI Engineering Curriculum
│
├── 1. Data Ingestion & Retrieval Foundations (Sprint 0)
│   ├── Dataset Engineering: Schema normalization, filtering (2022+ items), payload extraction
│   ├── Vector Embeddings: High-dimensional representations (1536 dims, Cosine similarity)
│   ├── Vector Indexing: Qdrant HNSW graph index, payload filtering
│   ├── Baseline Grounding: Naive RAG prompt synthesis, context injection
│   └── Foundational Observability: Distributed run traces (LangSmith), automated evals (RAGAS)
│
├── 2. Retrieval Precision & Context Engineering (Sprint 1)
│   ├── Deterministic Contracts: Pydantic schemas, Instructor library, validation retry loops
│   ├── Advanced Chunking: Semantic boundaries, Anthropic Contextual Retrieval (context-prepend)
│   ├── Hybrid Retrieval: Dense semantic search + Sparse lexical search (BM25) in Qdrant
│   ├── Two-Stage Retrieval: Bi-encoder candidate generation → Cross-encoder re-ranking
│   └── Prompt Decoupling: Version-controlled YAML registries, dynamic Jinja2 templating
│
├── 3. Autonomous Agents & Decision Loops (Sprint 2)
│   ├── Spectrum of Autonomy: Augmented LLMs → Prompt Chains → Routing → Orchestrator-Workers
│   ├── LangGraph State Machines: StateGraph, typed state schemas, nodes, conditional edges
│   ├── Guardrail Nodes: Intent Router (filtering non-shopping queries), Query Expansion
│   ├── Tool Calling Protocols: Function schema binding, ToolNode execution, ToolMessage loopbacks
│   └── Agentic Reasoning: Cyclical ReAct loops (Reason + Act + Observe)
│
├── 4. Conversational Systems, Protocols & Streaming (Sprint 3)
│   ├── State Persistence: LangGraph checkpointers, PostgresSaver, thread-partitioned sessions
│   ├── Multi-Source RAG: Catalog item retrieval tool + Customer review sentiment tool
│   ├── Model Context Protocol (MCP): Decoupled FastMCP microservices over HTTP/SSE transports
│   ├── Real-Time Streaming: Server-Sent Events (SSE) broadcasting agent thought states
│   └── Human-in-the-Loop (HITL): Breakpoint interrupts, user feedback attached to trace IDs
│
├── 5. Multi-Agent Systems & Coordination (Sprint 4)
│   ├── Architecture Rationale: Preventing context pollution, tool overload, and prompt drift
│   ├── Topologies: Supervisor / Coordinator pattern vs. Peer-to-Peer vs. Hierarchical teams
│   ├── Specialist Agents: Product Q&A Agent vs. Transactional Shopping Cart Agent (SQL tools)
│   ├── Inter-Agent Orchestration: Task decomposition, sub-task delegation, control handbacks
│   └── Live Frontend Synchronization: SSE cart state updates reflected in real-time UI
│
└── 6. Production Hardening, Optimization & CI/CD (Sprint 5)
    ├── High Availability: LiteLLM Router, multi-provider model fallback cascades
    ├── Cost & Latency Engineering: Prompt caching mechanics, static prefix alignment
    ├── Protocol Interoperability: Google Agent Development Kit (ADK), Remote A2A client/server
    ├── AI Security: Guardrails against prompt injection, least-privilege tool sandboxing
    ├── Continuous Integration (CI): Headless retriever precision/recall evaluation gates
    └── Multi-Container Deployment: 6-service Docker Compose topology with volume persistence
```

---

## 2. Core Mental Models

### Mental Model 1: The Principle of Least Autonomy
*Do not use an autonomous agent when a deterministic function or prompt chain suffices.*
- Start with deterministic code and static routing.
- Add an LLM only where semantic interpretation is necessary.
- Add tool calling only when external data or actions are required.
- Add multi-agent orchestration only when distinct tasks have conflicting system prompts and toolsets.

### Mental Model 2: Two-Stage Information Retrieval
*Broad semantic recall must always be paired with precise cross-encoder re-ranking.*
- **Stage 1 (Broad Recall)**: Hybrid dense vector (semantic concept) + sparse BM25 (exact SKU/keyword) retrieves top-20 candidates in < 30ms.
- **Stage 2 (Deep Precision)**: Cross-encoder re-ranker evaluates joint attention across query-passage pairs, re-scoring top-5 candidates in < 80ms.

### Mental Model 3: Decoupled Protocol Architecture
*Tools should be independent microservices, not monolithic Python library imports.*
- FastMCP servers package tools into dedicated network endpoints.
- Agents discover and invoke tools over standard HTTP/SSE transports.
- Tool failures do not crash the agent backend; tool permissions remain strictly sandboxed.

### Mental Model 4: Prefix-Aligned Prompt Caching
*Dynamic variables placed at the beginning of a prompt destroy cache reuse; static instructions placed first unlock 80% cost savings.*
- **Static Prefix (Cached)**: System role, guidelines, tool schemas, few-shot examples.
- **Dynamic Tail (Uncached)**: User query, timestamps, retrieved document chunks.

### Mental Model 5: Quantitative Evaluation as Software Tests
*Never deploy prompt or model changes without running automated regression test suites.*
- Maintain golden evaluation datasets versioned in code.
- Measure retrieval accuracy (Hit Rate@k, MRR) and generation quality (Faithfulness, Relevance).
- Fail CI pipeline builds automatically if metrics degrade.
