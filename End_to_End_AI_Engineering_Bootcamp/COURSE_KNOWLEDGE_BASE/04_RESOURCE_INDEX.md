# Master Resource Index

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
