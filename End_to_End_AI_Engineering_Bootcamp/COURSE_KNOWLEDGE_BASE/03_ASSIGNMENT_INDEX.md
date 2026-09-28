# Master Assignment & Project Index

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
