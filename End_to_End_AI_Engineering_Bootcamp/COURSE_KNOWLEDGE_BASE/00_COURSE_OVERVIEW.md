# Course Overview — End-to-End AI Engineering Bootcamp

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
