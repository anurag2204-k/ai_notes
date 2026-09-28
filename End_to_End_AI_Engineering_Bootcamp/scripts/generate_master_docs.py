import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

KB_BASE = r"c:\Users\anurag\Desktop\notes\End_to_End_AI_Engineering_Bootcamp\COURSE_KNOWLEDGE_BASE"

# 1. Generate 04_RESOURCE_INDEX.md
resource_index_content = """# Master Resource Index

This index catalogs the primary technical resources, lecture slide decks, documentation libraries, GitHub repositories, research papers, and official solution videos supporting the End-to-End AI Engineering Bootcamp. Only verified, high-value technical assets are indexed.

---

## Slides / PPTs

### Bootcamp Orientation & Roadmap Deck
- **URL / Path**: [End-to-end AI Engineering bootcamp Prep.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/End-to-end%20AI%20Engineering%20bootcamp%20Prep.pdf)
- **Description**: 19-slide orientation deck introducing instructor Aurimas Griciunas, course structure, timeline, communication channels, and tooling prerequisites.
- **Section Supported**: Orientation, Setup, and Section 0.

### Sprint 0 Info Review: Foundations, Lifecycle & Naive RAG
- **URL / Path**: [Sprint-0-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-0-info-review.pdf)
- **Description**: 122-slide comprehensive lecture deck covering the complete AI product lifecycle, LLM tokenization mechanics, naive RAG architectures, vector embedding theory, LangSmith tracing, and RAGAS evaluation metrics.
- **Section Supported**: Section 0 (Problem Framing, Infrastructure Setup & RAG Foundations).

### Sprint 1 Info Review: Ingestion, Chunking & Hybrid Retrieval
- **URL / Path**: [Sprint-1-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-1-info-review.pdf)
- **Description**: 115-slide technical deck on data ingestion pipelines, HNSW vs Flat index topologies, chunking strategies, Anthropic Contextual Retrieval, TF-IDF / BM25 lexical search, and hybrid fusion algorithms.
- **Section Supported**: Section 1 (Retrieval Quality & Context Engineering).

### Sprint 2 Info Review: Autonomous Agents & Decision Loops
- **URL / Path**: [Sprint-2-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-2-info-review.pdf)
- **Description**: 115-slide master guide detailing Anthropic's agentic design patterns, ReAct loops, tool calling protocols, function schema generation, memory hierarchies, and trajectory evaluations.
- **Section Supported**: Section 2 (Agents & Agentic Systems).

### Sprint 3 Info Review: Multi-Turn State, MCP & Agentic RAG
- **URL / Path**: [Sprint-3-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-3-info-review.pdf)
- **Description**: 77-slide architectural deck covering LangGraph state persistence, checkpointers (PostgresSaver), deep research agent patterns, Model Context Protocol (MCP) client-server architecture, and tool sandboxing.
- **Section Supported**: Section 3 (Moving From Basic To Agentic RAG).

### Sprint 4 Info Review: Multi-Agent Systems & Coordination
- **URL / Path**: [Sprint-4-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-4-info-review.pdf)
- **Description**: 114-slide guide explaining why single agents break down under scale, supervisor/coordinator orchestration topologies, inter-agent state synchronization, and Agent-to-Agent (A2A) communication protocols.
- **Section Supported**: Section 4 (Multi-Agent Systems) and Section 5 (Deployment & Reliability).

---

## Documentation

### LangGraph Framework Documentation
- **URL**: [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)
- **Description**: Definitive documentation for cyclical state machines, StateGraph, conditional edges, and Postgres checkpointers.

### Qdrant Vector Database
- **URL**: [https://qdrant.tech/documentation/](https://qdrant.tech/documentation/)
- **Description**: Core documentation for Qdrant vector indexing, dense-sparse hybrid search, payload filtering, and Python client APIs.

### Model Context Protocol (MCP) Official Specification
- **URL**: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)
- **Description**: Anthropic's open standard for connecting AI systems to external tools, databases, and microservices.

### FastMCP Python Library
- **URL**: [https://github.com/jlowin/fastmcp](https://github.com/jlowin/fastmcp)
- **Description**: High-level, ergonomic Python framework for implementing production MCP servers over HTTP and SSE transports.

### Instructor (Structured Outputs)
- **URL**: [https://python.useinstructor.com/](https://python.useinstructor.com/)
- **Description**: Python library enabling guaranteed Pydantic schema validation and automatic retry loops with LLM function calling.

### RAGAS Evaluation Framework
- **URL**: [https://docs.ragas.io/](https://docs.ragas.io/)
- **Description**: Quantitative evaluation framework for measuring Faithfulness, Answer Relevance, Context Recall, and Context Precision.

### LangSmith Observability Platform
- **URL**: [https://docs.smith.langchain.com/](https://docs.smith.langchain.com/)
- **Description**: Distributed tracing, latency tracking, token cost accounting, and feedback dataset management for LLMs.

### LiteLLM Proxy & Router
- **URL**: [https://docs.litellm.ai/docs/routing](https://docs.litellm.ai/docs/routing)
- **Description**: High-throughput routing library providing load balancing and automated model fallback cascades across 100+ LLMs.

---

## GitHub / Code

### Master Bootcamp Repository
- **URL / Path**: [ai-engineering-bootcamp-cohort-4-main.zip](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/ai-engineering-bootcamp-cohort-4-main.zip) (Extracted in `scratch/repo/`)
- **Description**: Production codebase containing the FastAPI backend (`apps/api`), Streamlit frontend (`apps/chatbot_ui`), FastMCP servers (`apps/items_mcp_server`, `apps/reviews_mcp_server`), Docker configs, and 22 Jupyter notebooks.

### Google Agent Development Kit (ADK)
- **URL**: [https://github.com/google/agent-development-kit](https://github.com/google/agent-development-kit)
- **Description**: Open-source framework for building, testing, and debugging modular AI agents with dedicated web servers.

### FastMCP GitHub Repository
- **URL**: [https://github.com/jlowin/fastmcp](https://github.com/jlowin/fastmcp)
- **Description**: Python implementation of the Model Context Protocol used in the bootcamp's decoupled tool servers.

---

## Papers

### Anthropic: Building Effective Agents
- **URL**: [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)
- **Description**: Landmark research analyzing common agent design patterns: Augmented LLMs, Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, and Evaluator-Optimizer loops.

### Anthropic: Contextual Retrieval
- **URL**: [https://www.anthropic.com/news/contextual-retrieval](https://www.anthropic.com/news/contextual-retrieval)
- **Description**: Research paper demonstrating that prepending document-level context to text chunks prior to embedding reduces retrieval failure rates by up to 49%.

### ReAct: Synergizing Reasoning and Acting in Language Models
- **URL**: [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)
- **Description**: The foundational paper introducing interleaved reasoning traces and tool actions in language models.

### Google AI: Towards an AI Co-Scientist (Multi-Agent Case Study)
- **URL**: [https://arxiv.org/abs/2501.04227](https://arxiv.org/abs/2501.04227)
- **Description**: State-of-the-art case study analyzing large-scale multi-agent collaboration across generation, reflection, and ranking agents.

---

## External Learning Resources

### Amazon Reviews 2023 Dataset Repository
- **URL**: [https://amazon-reviews-2023.github.io/main.html](https://amazon-reviews-2023.github.io/main.html)
- **Description**: Massive academic e-commerce dataset powering the bootcamp capstone, featuring millions of products, categories, and customer reviews.

### OWASP Top 10 for LLM Applications
- **URL**: [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- **Description**: Industry standard framework highlighting prompt injection, sensitive data leakage, and excessive agency vulnerabilities.

---

## Assignments

- **Assignment 0**: [Environment Setup & Repo Scaffolding](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-00-Environment-Setup-and-Repo-Scaffolding/README.md)
- **Assignment 1**: [Baseline RAG Pipeline & Observability](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-End-to-End-Baseline-RAG-Pipeline/README.md)
- **Assignment 2**: [Context Engineering, Hybrid Search & Re-Ranking](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Context-Engineering-Hybrid-Search-Reranking/README.md)
- **Assignment 3**: [Autonomous Agent, LangGraph & Tool Calling](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Autonomous-Agent-LangGraph-Tool-Calling/README.md)
- **Assignment 4**: [Agentic RAG, MCP Microservices & Real-Time Streaming](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-04-Agentic-RAG-MCP-Human-in-the-Loop/README.md)
- **Assignment 5**: [Multi-Agent System Coordination & Transactional Tooling](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-05-Multi-Agent-System-Coordination/README.md)
- **Assignment 6**: [Cloud Deployment, Optimization & Reliability Engineering](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-06-Deployment-Optimization-Fallbacks/README.md)

---

## Solution Videos

- **Sprint 0 Code Walkthroughs**: [013-019 Videos 1-7](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/) (Dataset prep, Qdrant indexing, baseline RAG, LangSmith tracing, RAGAS evals)
- **Sprint 1 Code Walkthroughs**: [022-027 Videos 1-6](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/) (Instructor structured outputs, hybrid search, cross-encoder re-ranking, Jinja2 prompt registries)
- **Sprint 2 Code Walkthroughs**: [031-036 Videos 1-6](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/) (LangGraph StateGraph, tool binding, query expansion, intent router node, ReAct loop)
- **Sprint 3 Code Walkthroughs**: [041-048 Videos 1-8](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/) (PostgresSaver checkpointers, review tools, FastMCP microservices, SSE streaming, LangSmith feedback)
- **Sprint 4 Code Walkthroughs**: [051-058 Videos 1-8](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/) (PostgreSQL shopping cart schema, Shopping Cart Agent, Coordinator Agent, UI synchronization)
- **Sprint 5 Code Walkthroughs**: [062-068 Videos 1-6](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/) (LiteLLM Router fallback cascades, Google ADK migration, remote A2A server, prompt caching)
- **Capstone Build Lab & Demo**:
  - [060 Sprint Build Lab Containerise your capstone and implement CI Pipeline.mp4](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/060%20FEB%2026%20Sprint%20Build%20Lab%20Containerise%20your%20capstone%20and%20implement%20CI%20Pipeline.mp4)
  - [071 MAR 10 Demo Day Present your working AI product to cohort.mp4](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/071%20MAR%2010%20Demo%20Day%20Present%20your%20working%20AI%20product%20to%20cohort.mp4)
"""

with open(os.path.join(KB_BASE, "04_RESOURCE_INDEX.md"), "w", encoding="utf-8") as f:
    f.write(resource_index_content)
print("Generated 04_RESOURCE_INDEX.md")

# 2. Generate 03_ASSIGNMENT_INDEX.md
assignment_index_content = """# Master Assignment & Project Index

This index tracks all practical milestones, engineering assignments, and the capstone project spanning the End-to-End AI Engineering Bootcamp. Every entry links to dedicated requirement specifications, implementation resources, and official codebase solutions.

---

## Assignment Roadmap

| Assignment / Project | Sprint / Section | Main Concepts & Tools | Key Deliverables | Solution Available |
|---|---|---|---|---|
| [Assignment 0](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-00-Environment-Setup-and-Repo-Scaffolding/README.md) | Sprint 0 | UV, Docker Compose, Virtualenv, LLM APIs | Verified `.env`, resolved `uv.lock`, working Docker engine | [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-00-Environment-Setup-and-Repo-Scaffolding/solution.md) |
| [Assignment 1](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-End-to-End-Baseline-RAG-Pipeline/README.md) | Sprint 0 | Amazon Dataset, Qdrant Ingestion, Baseline RAG, LangSmith, RAGAS | Ingestion notebook, baseline RAG API, Streamlit UI, RAGAS evals | [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-End-to-End-Baseline-RAG-Pipeline/solution.md) |
| [Assignment 2](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Context-Engineering-Hybrid-Search-Reranking/README.md) | Sprint 1 | Pydantic, Instructor, Hybrid Search (Dense+Sparse), Re-Ranking, YAML Prompts | Structured output models, Qdrant hybrid collection, Cohere re-ranker, Jinja2 registry | [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Context-Engineering-Hybrid-Search-Reranking/solution.md) |
| [Assignment 3](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Autonomous-Agent-LangGraph-Tool-Calling/README.md) | Sprint 2 | LangGraph StateGraph, Tool Calling, ReAct Loop, Intent Router, Query Expansion | Cyclical LangGraph graph, Intent Router node, ToolNode, FastAPI graph route | [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Autonomous-Agent-LangGraph-Tool-Calling/solution.md) |
| [Assignment 4](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-04-Agentic-RAG-MCP-Human-in-the-Loop/README.md) | Sprint 3 | PostgresSaver Persistence, Multi-Source RAG (Reviews), FastMCP Servers, SSE Streaming | FastMCP microservices (:8001, :8002), SSE streaming generator, LangSmith feedback | [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-04-Agentic-RAG-MCP-Human-in-the-Loop/solution.md) |
| [Assignment 5](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-05-Multi-Agent-System-Coordination/README.md) | Sprint 4 | Multi-Agent Systems, Supervisor Pattern, PostgreSQL Cart Schema, Live Cart Sync | Coordinator Agent, Shopping Cart Agent, PostgreSQL tools, Streamlit live cart UI | [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-05-Multi-Agent-System-Coordination/solution.md) |
| [Assignment 6](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-06-Deployment-Optimization-Fallbacks/README.md) | Sprint 5 | LiteLLM Router, Prompt Caching, Google ADK, Remote A2A Server, Automated CI Evals | Model fallback cascades, ADK agent, remote A2A client/server, `eval_retriever.py` | [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-06-Deployment-Optimization-Fallbacks/solution.md) |
| [Capstone Project](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Projects/Capstone-Production-Agentic-AI-Product/README.md) | Sprint 0-5 | Full End-to-End Autonomous Agentic AI Product Architecture | Containerized multi-agent product (6 services in Docker Compose), Demo Day presentation | [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Projects/Capstone-Production-Agentic-AI-Product/solution.md) |

---

## Detailed Assignment Summaries

### Assignment 0: Development Environment Setup & Project Scaffolding
- **Core Focus**: Scaffolding local repository, installing UV, setting up Docker Compose, managing API keys.
- **Verification**: Running `notebooks/prerequisites/01-llm-apis.ipynb` to verify OpenAI and Google API connectivity.

### Assignment 1: Baseline RAG Pipeline & Observability
- **Core Focus**: Ingesting the Amazon Electronics catalog into Qdrant, generating embeddings, prompting GPT-4o-mini, connecting FastAPI backend to Streamlit frontend, and running RAGAS evals.
- **Verification**: Generating synthetic test sets and verifying Faithfulness >= 0.80 and Answer Relevance >= 0.85 in LangSmith.

### Assignment 2: Context Engineering, Hybrid Search & Re-Ranking
- **Core Focus**: Enforcing Pydantic schemas via Instructor, configuring dense+sparse vector collections in Qdrant, applying cross-encoder re-ranking, and decoupling prompts into YAML/Jinja2 templates.
- **Verification**: Ensuring zero JSON parse errors and demonstrating Top-3 retrieval precision boost over baseline dense search.

### Assignment 3: Autonomous Agent, LangGraph & Tool Calling
- **Core Focus**: Constructing an autonomous cyclical ReAct agent in LangGraph with an Intent Router node to filter off-topic questions and a Query Expansion node to disambiguate composite prompts.
- **Verification**: Querying the agent with ambiguous questions and verifying proper tool invocation and loop termination in LangSmith.

### Assignment 4: Agentic RAG, MCP Microservices & Real-Time Streaming
- **Core Focus**: Multi-turn conversation persistence using PostgreSQL checkpointers (`PostgresSaver`), decoupling catalog and review retrieval into standalone FastMCP servers, and streaming SSE tokens to the frontend.
- **Verification**: Preserving conversation history across browser reloads and submitting user ratings tied directly to backend trace IDs.

### Assignment 5: Multi-Agent System Coordination & Transactional Tooling
- **Core Focus**: Designing a Supervisor / Coordinator agent in LangGraph to orchestrate between a specialized Product Q&A Agent and a transactional Shopping Cart Agent.
- **Verification**: Asking the system to discover a product and add it to the cart in a single conversational prompt, verifying database updates and frontend cart panel synchronization.

### Assignment 6: Cloud Deployment, Optimization & Reliability Engineering
- **Core Focus**: Configuring LiteLLM Router for automated fallback cascades across providers, structuring prompts to maximize prompt caching discounts, testing Google ADK and remote A2A servers, and building CI eval gates.
- **Verification**: Running `eval_retriever.py` in headless Docker containers and validating multi-container deployment via `docker compose up -d`.
"""

with open(os.path.join(KB_BASE, "03_ASSIGNMENT_INDEX.md"), "w", encoding="utf-8") as f:
    f.write(assignment_index_content)
print("Generated 03_ASSIGNMENT_INDEX.md")

# 3. Generate 02_CONCEPT_MAP.md
concept_map_content = """# Master Concept Map & Technical Taxonomy

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
"""

with open(os.path.join(KB_BASE, "02_CONCEPT_MAP.md"), "w", encoding="utf-8") as f:
    f.write(concept_map_content)
print("Generated 02_CONCEPT_MAP.md")

# 4. Generate 00_COURSE_OVERVIEW.md
course_overview_content = """# Course Overview — End-to-End AI Engineering Bootcamp

> **Instructor**: Aurimas Griciunas  
> **Target Audience**: AI Engineers, Software Engineers, and MLOps Practitioners  
> **Course Architecture**: Production Agentic AI, Advanced RAG, Multi-Agent Orchestration, Model Context Protocol (MCP), and Cloud Reliability  
> **Primary Source Codebase**: `ai-engineering-bootcamp-cohort-4-main` (FastAPI, LangGraph, Streamlit, Qdrant, PostgreSQL, Docker)

---

## What This Course Teaches
The **End-to-End AI Engineering Bootcamp** is an intensive, production-focused engineering curriculum designed to bridge the gap between simple LLM prototyping and scalable, enterprise-grade AI systems. 

Taught by industry AI leader Aurimas Griciunas, this program moves far beyond naive 'Retrieve-Then-Generate' wrappers. Practitioners learn to build full-stack, autonomous, multi-agent applications capable of complex planning, multi-source retrieval, transactional tool execution, multi-turn state persistence, and real-time streaming—all hardened with automated CI evaluation gates, LiteLLM fallback routers, and prompt caching cost optimizations.

---

## Course Structure & Curriculum Units

The course is structured around 6 progressive sprints, capped by an end-to-end multi-agent production capstone:

```
Section 0: Problem Framing, Infrastructure Setup & RAG Foundations
   ↓
Section 1: Retrieval Quality & Context Engineering
   ↓
Section 2: Autonomous Agents & Decision Loops
   ↓
Section 3: Moving From Basic To Agentic RAG (Persistence, MCP & Streaming)
   ↓
Section 4: Multi-Agent Systems & Coordination (Supervisor Pattern)
   ↓
Section 5: Production Deployment, Optimization & Reliability Engineering
   ↓
Capstone Product: Autonomous Multi-Agent E-Commerce Shopping Concierge
```

---

## Sprint-by-Sprint Roadmap

### [Section 0: Problem Framing, Infrastructure Setup & RAG Foundations](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Sections/Section-00-Problem-Framing-Infrastructure-Setup-RAG-Foundations/SUMMARY.md)
- **Problem Addressed**: How to structure an AI engineering workspace, ingest large-scale e-commerce data, and establish baseline RAG retrieval with quantitative observability.
- **Key Deliverables**: Docker Compose environment, Amazon Electronics dataset preprocessing, Qdrant vector collection setup, baseline FastAPI/Streamlit RAG pipeline, LangSmith tracing, and RAGAS evaluation benchmark.

### [Section 1: Retrieval Quality & Context Engineering](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Sections/Section-01-Retrieval-Quality-Context-Engineering/SUMMARY.md)
- **Problem Addressed**: Naive vector search misses exact keywords, causes semantic drift, and produces unstructured, hallucinated text outputs.
- **Key Deliverables**: Pydantic structured outputs with Instructor, Anthropic Contextual Retrieval, dense+sparse hybrid search in Qdrant, cross-encoder re-ranking, and decoupled YAML/Jinja2 prompt registries.

### [Section 2: Autonomous Agents & Decision Loops](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Sections/Section-02-Agents-and-Agentic-Systems/SUMMARY.md)
- **Problem Addressed**: Linear RAG pipelines cannot handle multi-step reasoning, query disambiguation, or dynamic information verification.
- **Key Deliverables**: LangGraph cyclical state machines (`StateGraph`), Intent Router node, Query Expansion node, tool binding, and ReAct decision loops.

### [Section 3: Moving From Basic To Agentic RAG](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Sections/Section-03-Moving-From-Basic-To-Agentic-RAG/SUMMARY.md)
- **Problem Addressed**: Stateless agents cannot sustain dialogues; tightly coupled tools create monolithic backends; multi-step reasoning suffers from UI latency.
- **Key Deliverables**: PostgreSQL checkpointer (`PostgresSaver`) for multi-turn persistence, secondary Amazon Reviews Qdrant collection, FastMCP microservices on dedicated ports, Server-Sent Events (SSE) state streaming, and LangSmith user feedback widgets.

### [Section 4: Multi-Agent Systems & Coordination](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Sections/Section-04-Multi-Agent-Systems/SUMMARY.md)
- **Problem Addressed**: Single agents with dozens of tools suffer from context pollution, prompt instruction conflicts, and high hallucination rates.
- **Key Deliverables**: Multi-agent Supervisor / Coordinator pattern in LangGraph, specialized Product Q&A Agent, transactional Shopping Cart Agent with PostgreSQL CRUD tools, and real-time UI cart synchronization.

### [Section 5: Production Deployment, Optimization & Reliability](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Sections/Section-05-Deployment-Optimization-Reliability/SUMMARY.md)
- **Problem Addressed**: Single-provider API outages, runaway token costs, prompt injection attacks, and untested production deployments.
- **Key Deliverables**: Multi-provider fallback cascades with LiteLLM Router, prefix-aligned prompt caching optimizations, Google ADK & remote A2A servers, automated CI evaluation gates (`eval_retriever.py`), and 6-service Docker Compose deployment.

---

## Major Technical Topics Covered
1. **RAG & Search**: Bi-encoders, cross-encoders, HNSW graphs, dense vector indexing, sparse BM25, hybrid search, Contextual Retrieval, late chunking.
2. **Agent Frameworks**: LangGraph, cyclical state machines, StateGraph, state reducers, conditional routing, ReAct loops, Google ADK.
3. **Protocols & Standards**: Model Context Protocol (MCP), FastMCP, Agent-to-Agent (A2A) protocol, Server-Sent Events (SSE).
4. **Data & Storage**: Qdrant Vector Database, PostgreSQL (relational cart schema + LangGraph checkpoints), UV package manager.
5. **Observability & MLOps**: LangSmith distributed tracing, RAGAS automated evaluations (Faithfulness, Relevance), CI/CD regression gating.
6. **Reliability & DevOps**: LiteLLM Router, prompt caching mechanics, OWASP LLM security, Docker Compose containerization.

---

## Core Mental Models to Remember
- **The Principle of Least Autonomy**: Prefer deterministic code and simple prompt chains over autonomous loops whenever possible.
- **Two-Stage Retrieval Architecture**: Cast a wide net fast with hybrid dense+sparse retrieval, then re-rank top candidates with a heavy cross-encoder.
- **Decoupled Tool Services**: Package tools as independent MCP servers to enforce security boundaries and simplify maintenance.
- **Prefix Alignment for Caching**: Keep system prompts and tool schemas static at the head of messages to unlock 50-80% cost and latency discounts.
- **Continuous Evaluation as CI Tests**: Run automated retrieval and generation evaluations on pull requests to prevent regressions.

---

## What You Can Build After Completing This Course
- **Autonomous Multi-Agent Applications**: Architect multi-agent systems using the Supervisor pattern with isolated prompts and specialized toolsets.
- **Enterprise-Grade RAG Systems**: Build hybrid dense+sparse retrieval engines with cross-encoder re-ranking capable of sub-100ms precision queries across millions of documents.
- **Decoupled Tool Microservices**: Package internal APIs and databases into FastMCP servers consumable by any MCP-compliant AI client.
- **Resilient Full-Stack AI Products**: Deploy containerized FastAPI + Streamlit applications equipped with PostgreSQL state persistence, SSE streaming, and LiteLLM fallback routers.
- **Automated CI/CD Evaluation Pipelines**: Implement regression testing gates that mathematically verify retrieval recall and generation faithfulness before production deployments.

---

## Master Assignment & Project Map

| Milestone | Sprint | Focus Area | Deliverable |
|---|---|---|---|
| [Assignment 0](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-00-Environment-Setup-and-Repo-Scaffolding/README.md) | Sprint 0 | Environment Setup | UV virtualenv, Docker Compose, verified API keys |
| [Assignment 1](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-End-to-End-Baseline-RAG-Pipeline/README.md) | Sprint 0 | Baseline RAG & Tracing | Amazon catalog ingestion in Qdrant, baseline RAG API, LangSmith tracing |
| [Assignment 2](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Context-Engineering-Hybrid-Search-Reranking/README.md) | Sprint 1 | Precision Retrieval | Pydantic schemas, Qdrant hybrid search, cross-encoder re-ranking, YAML prompts |
| [Assignment 3](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Autonomous-Agent-LangGraph-Tool-Calling/README.md) | Sprint 2 | Autonomous Agents | LangGraph StateGraph, Intent Router node, Query Expansion, ReAct loop |
| [Assignment 4](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-04-Agentic-RAG-MCP-Human-in-the-Loop/README.md) | Sprint 3 | Multi-Turn & MCP | PostgresSaver checkpointer, FastMCP microservices, SSE streaming, feedback widget |
| [Assignment 5](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-05-Multi-Agent-System-Coordination/README.md) | Sprint 4 | Multi-Agent Systems | Supervisor Agent, Shopping Cart Agent, PostgreSQL tools, real-time UI cart sync |
| [Assignment 6](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-06-Deployment-Optimization-Fallbacks/README.md) | Sprint 5 | Deployment & Reliability | LiteLLM Router fallbacks, prompt caching, Google ADK, remote A2A, CI eval gates |
| [Capstone Project](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Projects/Capstone-Production-Agentic-AI-Product/README.md) | Capstone | Full System Product | Complete 6-service containerized e-commerce autonomous shopping product |

---

## Overall Learning Progression
The course moves systematically from **foundations to advanced autonomy and production reliability**:
1. First, students understand the data fundamentals: embeddings, vector indexing, distance metrics, and naive retrieval.
2. Second, students engineer context: enforcing structured schemas, combining lexical and semantic search, and re-ranking candidates.
3. Third, students introduce autonomy: stateful decision loops that inspect intent, expand queries, and invoke tools.
4. Fourth, students solve the human and distributed systems challenge: multi-turn database persistence, streaming UX, and decoupled MCP tool microservices.
5. Fifth, students scale into multi-agent systems: delegating tasks between a Coordinator and domain specialists with transactional tools.
6. Finally, students harden the product for the real world: multi-provider fallbacks, prompt caching cost optimization, security guardrails, automated CI testing, and multi-container Docker deployments.
"""

with open(os.path.join(KB_BASE, "00_COURSE_OVERVIEW.md"), "w", encoding="utf-8") as f:
    f.write(course_overview_content)
print("Generated 00_COURSE_OVERVIEW.md")
