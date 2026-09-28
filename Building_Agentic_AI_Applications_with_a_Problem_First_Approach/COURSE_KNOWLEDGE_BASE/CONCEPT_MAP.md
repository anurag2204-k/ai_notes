# Course Concept Map & Architecture Topology

A hierarchical mental map depicting how the concepts, frameworks, and technologies connect across the curriculum.

```
PROBLEM-FIRST SYSTEM DESIGN
│
├── 1. PROBLEM SCOPING & FEASIBILITY
│   ├── Input / Output Framework (Predictability vs Creativity)
│   ├── Deterministic Baseline (Rules & Code) vs Generative Augmentation
│   └── Iterative Architecture (Phase 0: Rule-based -> Phase 1: RAG -> Phase 2: Autonomous)
│
├── 2. FOUNDATION MODEL INTERFACING
│   ├── Prompt Engineering 2025
│   │   ├── In-Context Learning (Few-shot, Deliberate Demonstrations)
│   │   ├── Structured Output Enforcement (JSON Schema, Pydantic Models)
│   │   ├── Reasoning Models (o1, DeepSeek-R1, Chain-of-Thought prompting)
│   │   └── Automated Optimization (DSPy, MIPRO, Prompt Breeder)
│   └── Guardrails & Alignment
│       ├── Input Validation (Jailbreak detection, PII masking)
│       └── Output Moderation (Hallucination filtering, Fact verification)
│
├── 3. WORKFLOW AGENTS (DETERMINISTIC LEVEL 2)
│   ├── Query Classification & Dynamic Routing
│   ├── State Management & Conversation Memory (RunnableWithMessageHistory)
│   └── Controlled Tool Invocation (API calling with strict error handling)
│
├── 4. ENTERPRISE RETRIEVAL-AUGMENTED GENERATION (RAG)
│   ├── Ingestion & Chunking
│   │   ├── Document Parsing (PDFs, Tables, Layout-aware loaders)
│   │   └── Chunking Strategies (Fixed, Semantic Boundary, Hierarchical parent-child)
│   ├── Indexing & Storage
│   │   ├── Vector Embeddings (Dense similarity, text-embedding-3-small)
│   │   └── Vector Stores (ChromaDB, Pinecone, FAISS, Weaviate)
│   ├── Advanced Retrieval Optimization
│   │   ├── Query Rewriting (HyDE - Hypothetical Document Embeddings)
│   │   ├── Hybrid Retrieval (Dense Vector + BM25 Sparse Keyword)
│   │   └── Cross-Encoder Re-Ranking (Cohere / BGE Re-rankers)
│   ├── Corrective RAG (CRAG)
│   │   ├── Document Relevance Grading
│   │   ├── Fallback Live Web Search (Tavily Search API)
│   │   └── Grounded Generation
│   └── Advanced Paradigms
│       ├── Multimodal RAG (Tables, Charts, Document Images)
│       └── GraphRAG (Entity extraction, Knowledge Graph communities)
│
├── 5. AGENT MEMORY & CONTEXT ENGINEERING
│   ├── Short-Term Memory (Context window buffer, sliding token window)
│   ├── Long-Term Memory (Vector-indexed user profile & episodic history)
│   └── Context Budgeting (Needle-in-a-haystack attention optimization)
│
├── 6. AUTONOMOUS AGENTS (LEVEL 3 & 4)
│   ├── Planning Paradigms
│   │   ├── ReAct Loop (Thought -> Action -> Observation -> Reflection)
│   │   ├── Plan-and-Solve (Upfront task decomposition followed by step execution)
│   │   └── Reflection & Self-Correction (Reflexion framework)
│   ├── Orchestration Engines
│   │   ├── LangGraph StateGraph (Nodes, Edges, Conditional Routing, Cycles)
│   │   └── Checkpointing & Human-in-the-Loop Interrupts
│   └── Multi-Agent Collaboration Patterns
│       ├── Supervisor / Orchestrator Pattern (Central controller delegates to specialists)
│       ├── Peer-to-Peer Swarms (Collaborative message passing)
│       └── Deep Research Systems (Planner, Web Scraper, Fact Checker, Writer)
│
├── 7. OPEN INTEROPERABILITY PROTOCOLS
│   ├── Model Context Protocol (MCP)
│   │   ├── MCP Architecture (Host <-> Client <-> Server)
│   │   ├── Standard Tool & Resource Discovery
│   │   └── Building Custom MCP Servers (e.g., Bookmarking, Math, DB)
│   └── Google Agent-to-Agent (A2A) Protocol
│
└── 8. PRODUCTIONIZATION, EVALS & AIOps
    ├── Evaluation Frameworks
    │   ├── Retrieval Quality (Ragas: Context Precision, Context Recall)
    │   ├── Generation Quality (Faithfulness, Answer Relevance)
    │   └── LLM-as-a-Judge Calibration & Trajectory Scoring
    ├── Observability & Tracing (Comet Opik, Langfuse, OpenTelemetry)
    ├── Operational Metrics (Token economics, P95 latency, Cache hit rates)
    └── Build vs Buy vs Fine-Tune (SFT, LoRA/QLoRA, Synthetic Data Generation)
```
