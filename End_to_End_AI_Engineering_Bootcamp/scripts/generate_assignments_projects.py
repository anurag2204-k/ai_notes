import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

KB_BASE = r"c:\Users\anurag\Desktop\notes\End_to_End_AI_Engineering_Bootcamp\COURSE_KNOWLEDGE_BASE"
ASSIGN_DIR = os.path.join(KB_BASE, "Assignments")
PROJ_DIR = os.path.join(KB_BASE, "Projects")
os.makedirs(ASSIGN_DIR, exist_ok=True)
os.makedirs(PROJ_DIR, exist_ok=True)

assignments = [
    {
        "dir": "Assignment-00-Environment-Setup-and-Repo-Scaffolding",
        "title": "Assignment 0 — Development Environment Setup & Project Scaffolding",
        "num": "0",
        "desc": "Initialize and verify the production-grade local development environment required for the entire bootcamp. Configure the UV package manager, Docker Compose infrastructure, environment secrets, and verify hardware/software dependencies.",
        "tasks": [
            "Install UV package manager and initialize a Python 3.11+ virtual environment.",
            "Install Docker Desktop and verify Docker Compose engine functionality.",
            "Clone the cohort starter repository and review the multi-package workspace structure (`apps/api`, `apps/chatbot_ui`, `notebooks`).",
            "Configure `.env` file with valid API keys for OpenAI, Google GenAI, and LangSmith.",
            "Verify network connectivity and run `make install` or `uv sync` to install project dependencies."
        ],
        "concepts": [
            "Modern Python Tooling (UV package manager)",
            "Containerization Fundamentals (Docker & Docker Compose)",
            "Multi-Project Monorepo Scaffolding",
            "Environment Variable Isolation (.env)"
        ],
        "section": "Section 0 — Problem Framing, Infrastructure Setup & RAG Foundations",
        "lessons": [
            "Setting up your development environment (HTML & Videos 1-4)",
            "001 Understanding the AI product lifecycle"
        ],
        "resources": [
            "[Setting up your development environment..html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Setting%20up%20your%20development%20environment..html)",
            "[011 Sprint Build Lab Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/011%20Sprint%20Build%20Lab%20Set%20up%20development%20environment%20and%20scaffold%20project%20repo.mp4)",
            "[env.example](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/env.example)"
        ],
        "assignment_reqs": """### Objectives
Establish a reproducible local development environment supporting fast dependency resolution, multi-service container orchestration, and isolated API credentials.

### Requirements & Constraints
1. **Python Version**: Must use Python >= 3.11 managed via `uv`.
2. **Container Infrastructure**: Docker Engine with Docker Compose v2 support.
3. **Environment Secrets**: Create `.env` from `env.example` containing:
   - `OPENAI_API_KEY`: Valid key for embedding and LLM inference.
   - `LANGSMITH_API_KEY`: Valid key for tracing.
   - `LANGSMITH_TRACING=true`: Enabled for automatic run capture.
   - `LANGSMITH_PROJECT=ai-engineering-bootcamp`.
4. **Workspace Scaffolding**: Verify the directory layout containing:
   - `apps/api/`: FastAPI backend service.
   - `apps/chatbot_ui/`: Streamlit frontend service.
   - `notebooks/`: Sprint experimentation notebooks.

### Deliverables
- Fully resolved `uv.lock` file.
- Functional Docker container runtime.
- Verified test script checking LLM API connectivity via `notebooks/prerequisites/01-llm-apis.ipynb`.""",
        "solution": """### Official Solution & Implementation
- **Walkthrough Videos**:
  - `Setting up your development environment 1.mp4` (UV installation)
  - `Setting up your development environment 2.mp4` (Docker Engine)
  - `Setting up your development environment 3.mp4` (Git & Repository setup)
  - `Setting up your development environment 4.mp4` (API keys & environment configuration)
  - `011 Sprint Build Lab Set up development environment and scaffold project repo.mp4`
- **Reference Notebook**: [01-llm-apis.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/prerequisites/01-llm-apis.ipynb)
- **Configuration Files**:
  - [pyproject.toml](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/pyproject.toml)
  - [uv.lock](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/uv.lock)
  - [env.example](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/env.example)"""
    },
    {
        "dir": "Assignment-01-End-to-End-Baseline-RAG-Pipeline",
        "title": "Assignment 1 — Baseline RAG Pipeline & Observability Foundations",
        "num": "1",
        "desc": "Build an end-to-end baseline RAG prototype on the Amazon Electronics catalog dataset. Spin up Qdrant in Docker, ingest and vectorize product items, implement baseline semantic retrieval and prompt synthesis, expose an API endpoint in FastAPI, render results in Streamlit, instrument LangSmith tracing, and benchmark with RAGAS.",
        "tasks": [
            "Download and preprocess the Amazon Electronics catalog dataset (filtering items observed from 2022 onwards).",
            "Launch Qdrant vector database via Docker Compose and configure the `Amazon-items-collection-01` collection with Cosine similarity.",
            "Batch-generate dense vector embeddings using OpenAI `text-embedding-3-small` and upload points with rich payloads (ASIN, title, price, image).",
            "Implement a baseline RAG query function with grounding system prompts.",
            "Connect the RAG pipeline to a FastAPI backend endpoint and serve a Streamlit frontend chat UI.",
            "Instrument LangSmith tracing across the backend to capture full run execution trees.",
            "Synthesize an evaluation dataset from Qdrant payloads and execute automated RAGAS evaluation runs."
        ],
        "concepts": [
            "Dataset Cleaning & Filtering (Amazon Reviews 2023)",
            "Vector Embeddings & Qdrant Collection Management",
            "Baseline RAG Prompt Grounding",
            "FastAPI Backend & Streamlit Frontend Architecture",
            "Distributed Tracing with LangSmith",
            "Automated Evaluation with RAGAS (Faithfulness, Relevance)"
        ],
        "section": "Section 0 — Problem Framing, Infrastructure Setup & RAG Foundations",
        "lessons": [
            "003 What is RAG",
            "004 Embedding models & vector DB integration",
            "005 Implementing basic observability foundations",
            "006 Evaluating basic end-to-end retrieval and generation"
        ],
        "resources": [
            "[007 Hands-On Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%200%20–%20Problem%20Framing,%20Infrastructure%20Setup%20&%20RAG%20Foundations/007%20Hands-On%20Section.html)",
            "[010 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/010%20Sprint%20Review%20Project%20framing,%20tooling%20overview,%20and%20repo%20setup.mp4)",
            "[013-019 Hands-on Videos 1-7](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)"
        ],
        "assignment_reqs": """### Objectives
Construct a functioning end-to-end baseline RAG application grounded on real-world e-commerce data with quantitative evaluation.

### Requirements & Constraints
1. **Dataset**: Use Amazon Electronics Category (items observed in 2022+). Clean title, features, descriptions, and extract parent ASINs.
2. **Vector Database**: Run Qdrant on `localhost:6333`. Create collection `Amazon-items-collection-01` with vector size 1536 and distance `Cosine`.
3. **Retrieval**: Implement top-k dense vector search (`top_k=5`).
4. **Generation**: Prompt GPT-4o-mini to answer user shopping queries strictly using retrieved product items.
5. **Full-Stack Connection**:
   - Backend: FastAPI route accepting `query` and returning answer string with item metadata.
   - Frontend: Streamlit conversational interface displaying chat history.
6. **Observability**: Ensure all requests appear in LangSmith with input prompt, retrieved context, output, latency, and token metrics.
7. **Evaluation**: Generate at least 20 synthetic Q&A evaluation pairs and calculate RAGAS Faithfulness and Answer Relevance.

### Expected Deliverables
- Complete preprocessing script: `notebooks/week_1/02-RAG-preprocessing-items.ipynb`.
- Baseline RAG notebook: `notebooks/week_1/03-RAG-pipeline.ipynb`.
- RAGAS evaluation notebook: `notebooks/week_1/05-RAG-Evals.ipynb`.
- Functional FastAPI endpoint and Streamlit UI.""",
        "solution": """### Official Solution & Implementation
- **Source Walkthrough Videos**:
  - `013 Video 1 (Notebook).mp4`: Amazon dataset exploration.
  - `014 Video 2 (Notebook).mp4`: Preprocessing and indexing.
  - `015 Video 3 (Backend).mp4`: RAG pipeline implementation.
  - `016 Video 4 (Frontend).mp4`: Frontend/backend integration.
  - `017 Video 5 (Notebook + Backend).mp4`: LangSmith observability.
  - `018 Video 6 (Notebook).mp4`: Synthetic eval dataset generation.
  - `019 Video 7 (Notebook + Backend).mp4`: RAGAS evaluation execution.
- **Reference Notebooks**:
  - [01-explore-amazon-dataset.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_1/01-explore-amazon-dataset.ipynb)
  - [02-RAG-preprocessing-items.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_1/02-RAG-preprocessing-items.ipynb)
  - [03-RAG-pipeline.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_1/03-RAG-pipeline.ipynb)
  - [04-RAG-Eval-dataset.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_1/04-RAG-Eval-dataset.ipynb)
  - [05-RAG-Evals.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_1/05-RAG-Evals.ipynb)"""
    },
    {
        "dir": "Assignment-02-Context-Engineering-Hybrid-Search-Reranking",
        "title": "Assignment 2 — Context Engineering, Hybrid Search & Re-Ranking",
        "num": "2",
        "desc": "Upgrade the baseline RAG pipeline into a high-precision retrieval system. Enforce Pydantic structured outputs with Instructor, implement dense + sparse hybrid search in Qdrant, integrate cross-encoder re-ranking, and decouple prompt templates into version-controlled Jinja2 YAML registries.",
        "tasks": [
            "Define Pydantic schema models for structured RAG responses containing answers and typed item reference lists.",
            "Integrate Instructor library to guarantee strict schema validation with automatic retry loops.",
            "Create a new Qdrant collection configured for Hybrid Search supporting both dense vectors and sparse BM25 indices.",
            "Implement a two-stage retrieval pipeline: retrieve top-20 candidates via hybrid search, then re-rank top-5 using a cross-encoder model.",
            "Decouple system prompts into `retrieval_generation.yaml` and render dynamic contexts via Jinja2.",
            "Update the FastAPI backend to return structured JSON and update Streamlit to render product cards with images, prices, and ratings."
        ],
        "concepts": [
            "Pydantic Schema Validation & Instructor Library",
            "Hybrid Search (Dense Semantic + Sparse Lexical BM25)",
            "Two-Stage Retrieval & Cross-Encoder Re-Ranking",
            "Decoupled Prompt Management (YAML + Jinja2 Templates)",
            "Frontend Grounding Cards UI"
        ],
        "section": "Section 1 — Retrieval Quality & Context Engineering",
        "lessons": [
            "001 RAG Data Ingestion Pipeline",
            "002 Pydantic and structured outputs",
            "003 Chunking strategies and Contextual embeddings",
            "004 Context Engineering and prompt management",
            "005 Re-Ranking and Hybrid Retrieval for better relevance"
        ],
        "resources": [
            "[007 Hands-on Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%201%20–%20Retrieval%20Quality%20&%20Context%20Engineering/007%20Hands-on%20Section.html)",
            "[Sprint-1-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-1-info-review.pdf)",
            "[020 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/020%20JAN%2020%20Sprint%20Review%20Retrieval%20Quality%20&%20Context%20Engineering.mp4)",
            "[022-027 Hands-on Videos 1-6](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)"
        ],
        "assignment_reqs": """### Objectives
Overcome naive vector search limitations by combining lexical precision, cross-encoder re-ranking, and deterministic Pydantic output schemas.

### Requirements & Constraints
1. **Structured Outputs**: Use Pydantic and Instructor to enforce response structure:
   - `answer: str`
   - `references: List[RAGUsedContext]` where each reference includes `id`, `title`, and `reason`.
2. **Hybrid Search**: Configure Qdrant collection `Amazon-items-collection-01-hybrid-search` with:
   - Dense vector: `text-embedding-3-small` (1536 dims).
   - Sparse vector: BM25 / token frequencies.
3. **Re-Ranking**: Apply a cross-encoder model to re-score candidate items, selecting top-k most relevant chunks.
4. **Prompt Registry**: Move hardcoded prompt text to `prompts/retrieval_generation.yaml` and load via Jinja2 template renderer.
5. **UI Grounding**: Render product images, prices, and descriptions in the Streamlit frontend.

### Expected Deliverables
- Working notebooks: `01-Structured-Outputs-Intro.ipynb`, `03-Hybrid-Search.ipynb`, `04-Reranking.ipynb`, `05-Prompt-Management.ipynb`.
- Prompt configuration file: `prompts/retrieval_generation.yaml`.
- Updated backend API returning validated Pydantic JSON objects.""",
        "solution": """### Official Solution & Implementation
- **Source Walkthrough Videos**:
  - `022 Video 1 (Notebook).mp4`: Structured outputs with Instructor.
  - `023 Video 2 (Notebook).mp4`: Structured outputs in RAG pipeline.
  - `024 Video 3 (Notebook).mp4`: Backend migration of structured outputs.
  - `025 Video 4 (Notebook).mp4`: Frontend grounding UI enhancements.
  - `026 Video 5 (Notebook).mp4`: Hybrid search in Qdrant.
  - `027 Video 6 (Backend).mp4`: Cross-encoder re-ranking and prompt registries.
- **Reference Notebooks**:
  - [01-Structured-Outputs-Intro.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_2/01-Structured-Outputs-Intro.ipynb)
  - [02-Structured-Outputs-RAG-Pipeline.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_2/02-Structured-Outputs-RAG-Pipeline.ipynb)
  - [03-Hybrid-Search.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_2/03-Hybrid-Search.ipynb)
  - [04-Reranking.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_2/04-Reranking.ipynb)
  - [05-Prompt-Management.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_2/05-Prompt-Management.ipynb)
- **Prompt Registry File**: [retrieval_generation.yaml](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_2/prompts/retrieval_generation.yaml)"""
    },
    {
        "dir": "Assignment-03-Autonomous-Agent-LangGraph-Tool-Calling",
        "title": "Assignment 3 — Autonomous Agent, LangGraph & Tool Calling",
        "num": "3",
        "desc": "Transform the static RAG pipeline into an autonomous agent using LangGraph. Implement a state machine featuring an Intent Router node to filter irrelevant queries, a Query Expansion node for complex questions, an Agent reasoning node, and a ToolNode wrapping the hybrid retrieval engine into a cyclical ReAct loop.",
        "tasks": [
            "Construct foundational cyclical graphs using LangGraph `StateGraph` and custom Pydantic state schemas.",
            "Implement a Query Expansion node that rewrites multi-intent user questions into optimized retrieval queries.",
            "Build an Intent Router node that classifies queries into shopping questions vs. generic conversation, routing non-shopping questions to immediate termination.",
            "Wrap the Qdrant hybrid retrieval engine as a standardized tool callable via LLM function calling.",
            "Implement a ReAct agent loop connecting agent reasoning to the ToolNode with loopback edges.",
            "Migrate the compiled LangGraph workflow into `apps/api/src/api/agents/graph.py`."
        ],
        "concepts": [
            "LangGraph StateGraph & State Reducers (`operator.add`)",
            "Intent Router & Guardrail Nodes",
            "Query Expansion & Rewriting",
            "Tool Definition & Binding (`ToolNode`)",
            "ReAct Decision Loop & Conditional Routing"
        ],
        "section": "Section 2 — Agents & Agentic Systems",
        "lessons": [
            "001 Agent architecture and decision loops",
            "002 Tool use in agents",
            "003 Patterns for building Agentic Systems",
            "004 Memory in agent systems",
            "005 Reflection & Agent evaluation Frameworks"
        ],
        "resources": [
            "[006 Hands-on Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%202%20–%20Agents%20&%20Agentic%20Systems/006%20Hands-on%20Section.html)",
            "[Sprint-2-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-2-info-review.pdf)",
            "[028 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/028%20JAN%2027%20Sprint%20Review%20Autonomous%20Agents.mp4)",
            "[031-036 Hands-on Videos 1-6](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)"
        ],
        "assignment_reqs": """### Objectives
Build an autonomous decision-making agent that decides when to retrieve, rewrites queries, and validates output sufficiency before replying.

### Requirements & Constraints
1. **LangGraph State Schema**: Define `State` containing:
   - `messages: Annotated[List[Any], add]`
   - `question_relevant: bool`
   - `iteration: int`
   - `answer: str`
   - `final_answer: bool`
   - `references: Annotated[List[RAGUsedContext], add]`
2. **Intent Router**: Use a lightweight model or prompt to classify `question_relevant`. Route irrelevant queries directly to `END`.
3. **ToolNode**: Bind `get_formatted_item_context` to the agent node.
4. **Conditional Edge (`tool_router`)**:
   - Route to `tools` if tool calls are present in the last message and `iteration <= 2`.
   - Route to `end` if `final_answer` is true, iteration limit exceeded, or no tool calls remain.
5. **Backend Deployment**: Package the graph into `apps/api` and expose via REST endpoint.

### Expected Deliverables
- Exploration notebooks: `01-LangGraph-Intro.ipynb`, `02-Query-Rewriting.ipynb`, `03-Router.ipynb`, `04-Agent-Single-Turn.ipynb`.
- Production backend graph: `apps/api/src/api/agents/graph.py`.""",
        "solution": """### Official Solution & Implementation
- **Source Walkthrough Videos**:
  - `031 Video 1 (Notebook).mp4`: LangGraph building blocks.
  - `032 Video 2 (Backend).mp4`: Tool use and ReAct loop.
  - `033 Video 3 (NotebookBackend).mp4`: Query expansion node.
  - `034 Video 4 (NotebookBackend).mp4`: Intent router node.
  - `035 Video 5 (NotebookBackend).mp4`: Single-turn ReAct agent.
  - `036 Video 6 (NotebookBackend).mp4`: Backend graph migration.
- **Reference Notebooks**:
  - [01-LangGraph-Intro.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/01-LangGraph-Intro.ipynb)
  - [02-Query-Rewriting.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/02-Query-Rewriting.ipynb)
  - [03-Router.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/03-Router.ipynb)
  - [04-Agent-Single-Turn.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/04-Agent-Single-Turn.ipynb)
  - [05-LangGraph-LangChain.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/05-LangGraph-LangChain.ipynb)
  - [06-Tool-Calling.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/06-Tool-Calling.ipynb)
- **Backend Graph Code**: [apps/api/src/api/agents/graph.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/src/api/agents/graph.py)"""
    },
    {
        "dir": "Assignment-04-Agentic-RAG-MCP-Human-in-the-Loop",
        "title": "Assignment 4 — Agentic RAG, MCP Microservices & Real-Time Streaming",
        "num": "4",
        "desc": "Scale the agent architecture to support persistent multi-turn conversations, multiple retrieval tools, decoupled FastMCP microservices, real-time Server-Sent Events (SSE) streaming, and human-in-the-loop feedback logging to LangSmith.",
        "tasks": [
            "Configure PostgreSQL and `PostgresSaver` checkpointer to persist agent state across conversational turns using `thread_id`.",
            "Index the Amazon Customer Reviews dataset into Qdrant and build a second retrieval tool (`get_formatted_reviews_context`).",
            "Decouple the two retrieval tools into independent FastMCP servers (`items_mcp_server` on port 8002, `reviews_mcp_server` on port 8001).",
            "Create a custom MCP Tool Node in LangGraph that queries MCP servers over HTTP/SSE transports.",
            "Implement an SSE streaming generator (`agent_stream_wrapper`) in FastAPI yielding real-time node lifecycle status updates.",
            "Add a feedback submission endpoint in FastAPI that attaches user ratings directly to LangSmith trace runs."
        ],
        "concepts": [
            "PostgresSaver Checkpointing & Multi-Turn State Persistence",
            "Multi-Tool Agentic RAG (Catalog + Review Sentiment)",
            "Model Context Protocol (MCP) & FastMCP Microservices",
            "Server-Sent Events (SSE) Real-Time State Streaming",
            "Human Feedback Attribution in LangSmith"
        ],
        "section": "Section 3 — Moving From Basic To Agentic RAG",
        "lessons": [
            "001 Agent integrations with RAG systems",
            "002 Human Feedback and Fault Tolerance in Agentic Systems",
            "003 Human in the loop (HITL)",
            "004 Model Context Protocol (MCP)"
        ],
        "resources": [
            "[005 Hands-on Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%203%20–%20Moving%20From%20Basic%20To%20Agentic%20RAG/005%20Hands-on%20Section.html)",
            "[Sprint-3-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-3-info-review.pdf)",
            "[037 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/037%20FEB%2003%20Sprint%20Review%20Moving%20from%20basic%20to%20agentic%20RAG.mp4)",
            "[041-048 Hands-on Videos 1-8](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)"
        ],
        "assignment_reqs": """### Objectives
Transform the single-turn agent into a production-grade multi-turn conversational system with decoupled MCP tools and streaming UX.

### Requirements & Constraints
1. **Persistence**: LangGraph compilation must include `PostgresSaver.from_conn_string(...)` checkpointer configured for `postgresql://langgraph_user:langgraph_password@postgres:5432/langgraph_db`.
2. **MCP Architecture**:
   - `items_mcp_server`: FastMCP server exposing `get_formatted_item_context` on port 8000 (mapped to 8002).
   - `reviews_mcp_server`: FastMCP server exposing `get_formatted_reviews_context` on port 8000 (mapped to 8001).
3. **Streaming**: FastAPI must stream SSE chunks:
   - Node status strings: `"Analysing the question..."`, `"Planning..."`, `"Looking for items..."`.
   - Final JSON event: `type: "final_answer"` with `answer`, `used_context`, and `trace_id`.
4. **Feedback Logging**: Frontend must expose thumbs-up/down buttons sending payload `{trace_id, score, comment}` to `/feedback` endpoint, which invokes `langsmith.Client().create_feedback(...)`.

### Expected Deliverables
- MCP server implementations in `apps/items_mcp_server` and `apps/reviews_mcp_server`.
- Streaming wrapper function `agent_stream_wrapper` in `apps/api/src/api/agents/graph.py`.
- Feedback endpoint in `apps/api/src/api/api/processors/submit_feedback.py`.""",
        "solution": """### Official Solution & Implementation
- **Source Walkthrough Videos**:
  - `041 Video 1 (Notebook).mp4`: LangGraph state persistence.
  - `042 Video 2 (Notebook).mp4`: Backend persistence migration.
  - `043 Video 3 (Backend).mp4`: Amazon Reviews collection and tool.
  - `044 Video 4 (Backend).mp4`: Human feedback UI and LangSmith linking.
  - `045 Video 5 (Notebook).mp4`: FastMCP server implementation.
  - `046 Video 6 (Notebook).mp4`: Custom MCP ToolNode in LangGraph.
  - `047 Video 7 (Notebook).mp4`: Graph state streaming mechanics.
  - `048 Video 8 (Backend).mp4`: SSE streaming integration.
- **Reference Notebooks**:
  - [01-Multi-Turn-Agent.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_4/01-Multi-Turn-Agent.ipynb)
  - [02-Multiple-Tools.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_4/02-Multiple-Tools.ipynb)
  - [03-Human-Feedback.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_4/03-Human-Feedback.ipynb)
  - [04-MCP.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_4/04-MCP.ipynb)
  - [05-State-Streaming.ipynb](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/notebooks/week_4/05-State-Streaming.ipynb)
- **Production Code**:
  - [apps/items_mcp_server/src/items_mcp_server/main.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/items_mcp_server/src/items_mcp_server/main.py)
  - [apps/reviews_mcp_server/src/reviews_mcp_server/main.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/reviews_mcp_server/src/reviews_mcp_server/main.py)
  - [apps/api/src/api/agents/graph.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/src/api/agents/graph.py)"""
    },
    {
        "dir": "Assignment-05-Multi-Agent-System-Coordination",
        "title": "Assignment 5 — Multi-Agent System Coordination & Transactional Tooling",
        "num": "5",
        "desc": "Architect a production Multi-Agent System (MAS) in LangGraph using the Supervisor / Coordinator pattern. Create PostgreSQL shopping cart tables and transactional tools, implement a dedicated Shopping Cart specialist agent, design a Coordinator Agent that plans and delegates workflows, and synchronize cart state to the UI in real time.",
        "tasks": [
            "Create relational PostgreSQL tables for shopping cart management (`cart_id`, `user_id`, `asin`, `quantity`, `added_at`).",
            "Implement three transactional Python tools: `add_to_cart`, `get_cart_contents`, and `remove_from_cart`.",
            "Build a specialized Shopping Cart Agent with dedicated system prompt and transactional database tools.",
            "Implement a Coordinator Agent that parses multi-step user prompts, routes intent between Product Q&A and Cart agents, and synthesizes results.",
            "Integrate Coordinator, Cart Agent, and Q&A Agent into a unified multi-agent LangGraph workflow.",
            "Update the Streamlit UI to display live shopping cart state synchronized after agent tool actions."
        ],
        "concepts": [
            "Multi-Agent Supervisor / Coordinator Architecture",
            "Agent Specialization & Tool Boundary Segregation",
            "Transactional Relational Database Tooling",
            "Inter-Agent Delegation & Handback Flows",
            "Live UI State Synchronization"
        ],
        "section": "Section 4 — Multi-Agent Systems",
        "lessons": [
            "01 Multi-agent systems and when to use it",
            "02 Planning, delegation, and task routing among agents",
            "03 Synchronization and memory sharing",
            "04 Agent-to-agent communication protocols (A2A)"
        ],
        "resources": [
            "[05 Hands-on Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%204%20–%20Multi-Agent%20Systems/05%20Hands-on%20Section.html)",
            "[Sprint-4-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-4-info-review.pdf)",
            "[049 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/049%20FEB%2017%20Sprint%20Review%20Designing%20and%20orchestrating%20multi-agent%20systems.mp4)",
            "[051-058 Hands-on Videos 1-8](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)"
        ],
        "assignment_reqs": """### Objectives
Decompose complex e-commerce interactions into specialized, collaborative agents governed by a centralized Coordinator.

### Requirements & Constraints
1. **Shopping Cart DB Tools**: PostgreSQL tables must support atomic insert, select, and delete operations by `user_id`.
2. **Shopping Cart Agent**: Specialized sub-agent with prompt focused strictly on cart management. Has zero access to vector retrieval tools.
3. **Coordinator Agent**:
   - Parses composite queries (e.g., 'Find noise-cancelling headphones and add the top rated one to my cart').
   - Formulates multi-step execution plan.
   - Delegates Step 1 to Product Q&A Agent and Step 2 to Shopping Cart Agent.
   - Regains control after each step to update shared state.
4. **UI Synchronization**: Shopping cart sidebar in Streamlit must automatically re-render current cart contents upon tool completion.

### Expected Deliverables
- Database migration script / tool definitions for shopping cart in PostgreSQL.
- Coordinator and Shopping Cart agent definitions in `apps/api/src/api/agents/agents.py`.
- Multi-agent LangGraph workflow in `apps/api/src/api/agents/graph.py`.
- Synchronized frontend cart panel in `apps/chatbot_ui/src/chatbot_ui/app.py`.""",
        "solution": """### Official Solution & Implementation
- **Source Walkthrough Videos**:
  - `051 Video 1 (Notebook).mp4`: Postgres shopping cart schema & tools.
  - `052 Video 2 (Backend).mp4`: Shopping Cart Agent implementation.
  - `053 Video 3 (Notebook).mp4`: Coordinator Agent planning logic.
  - `054 Video 4 (Backend).mp4`: Multi-agent graph integration.
  - `055 Video 5 (Notebook + Backend).mp4`: Frontend real-time cart sync.
  - `056-058 Videos 6-8`: End-to-end multi-agent coordination.
- **Reference Code**:
  - [apps/api/src/api/agents/graph.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/src/api/agents/graph.py)
  - [apps/api/src/api/agents/agents.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/src/api/agents/agents.py)
  - [apps/chatbot_ui/src/chatbot_ui/app.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/chatbot_ui/src/chatbot_ui/app.py)"""
    },
    {
        "dir": "Assignment-06-Deployment-Optimization-Fallbacks",
        "title": "Assignment 6 — Cloud Deployment, Optimization & Reliability Engineering",
        "num": "6",
        "desc": "Harden, optimize, and containerize the entire multi-agent application for enterprise production. Implement LiteLLM Router model fallback cascades, optimize prompt templates for provider KV prompt caching, refactor warehouse agents into Google ADK services, connect remote A2A servers, and implement automated CI evaluation regression gates.",
        "tasks": [
            "Implement LiteLLM Router in FastAPI backend to establish automated fallback cascades (e.g. GPT-4o → Claude-3-5-Sonnet → Gemini-1.5-Pro).",
            "Audit prompt templates to ensure static system instructions and tool schemas maximize provider prompt cache hit rates.",
            "Reimplement warehouse management agent using Google Agent Development Kit (ADK) and verify via ADK Web Server.",
            "Implement a remote A2A server using `a2a-sdk` and connect LangGraph graph over network sockets.",
            "Configure multi-stage Dockerfiles and `docker-compose.yml` to orchestrate 6 services with persistent storage volumes.",
            "Build an automated evaluation CI gate script (`eval_retriever.py`) that tests retrieval recall and blocks failing builds."
        ],
        "concepts": [
            "Model Fallback Routing (LiteLLM Router)",
            "Prompt Caching Economics & Prefix Alignment",
            "Google Agent Development Kit (ADK) & ADK Web Server",
            "Remote Agent-to-Agent (A2A) Client/Server (`a2a-sdk`)",
            "Production Multi-Container Docker Orchestration",
            "Automated CI Evaluation Regression Gates"
        ],
        "section": "Section 5 — Deployment, Optimization and Reliability",
        "lessons": [
            "01 Deployment architecture patterns for AI Systems",
            "02 Managing latency and cost for AI applications",
            "03 Securing AI systems",
            "04 CI CD for AI applications"
        ],
        "resources": [
            "[05 Hands-on Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%205%20–%20Deployment,%20Optimization%20and%20Reliability/05%20Hands-on%20Section.html)",
            "[docker-compose.yml](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/docker-compose.yml)",
            "[eval_retriever.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/evals/eval_retriever.py)",
            "[059 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/059%20FEB%2024%20Sprint%20Review%20Best%20practices%20for%20cloud%20deployment,%20monitoring%20and%20performance%20tuning.mp4)",
            "[062-068 Hands-on Videos 1-6](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)"
        ],
        "assignment_reqs": """### Objectives
Package the complete system into a resilient, cost-optimized, containerized product protected by automated evaluation gates.

### Requirements & Constraints
1. **Fallback Routing**: Backend must use LiteLLM Router to automatically recover from primary model API rate limits (HTTP 429) or timeouts.
2. **Prompt Caching**: All system prompts must place static instructions first and dynamic user variables at the very end.
3. **Remote A2A**: Implement a remote server with `a2a-sdk` and connect from LangGraph.
4. **Automated CI Evals**: Script `apps/api/evals/eval_retriever.py` must run headless against Qdrant, computing Hit Rate@5 and MRR, exiting with code 1 if Hit Rate < 85%.
5. **Docker Compose**: Entire stack must launch cleanly with a single command: `docker compose up -d`.

### Expected Deliverables
- Multi-stage Dockerfiles (`apps/api/Dockerfile`, `apps/chatbot_ui/Dockerfile`).
- Master `docker-compose.yml` coordinating 6 services.
- Headless retriever evaluation script: `apps/api/evals/eval_retriever.py`.""",
        "solution": """### Official Solution & Implementation
- **Source Walkthrough Videos**:
  - `062 Video 1 (Notebook).mp4`: LiteLLM Router fallback mechanics.
  - `063 Video 2 (Backend).mp4`: FastAPI fallback integration.
  - `064 Video 3 (Backend + Frontend).mp4`: Google ADK migration.
  - `065 Video 4 (Notebook).mp4`: ADK Web Server debugging.
  - `066 Video 5 (Notebook + Backend).mp4`: Remote A2A server and client with a2a-sdk.
  - `067 Video 6 (Backend + CI).mp4`: LangGraph connection to remote A2A server.
  - `068 Video 6 (Notebooks + Cloud).mp4`: Prompt caching caveats and cost tuning.
- **Production Files**:
  - [docker-compose.yml](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/docker-compose.yml)
  - [apps/api/Dockerfile](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/Dockerfile)
  - [apps/chatbot_ui/Dockerfile](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/chatbot_ui/Dockerfile)
  - [apps/api/evals/eval_retriever.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/evals/eval_retriever.py)"""
    }
]

for a in assignments:
    a_dir = os.path.join(ASSIGN_DIR, a["dir"])
    os.makedirs(a_dir, exist_ok=True)
    
    # 1. README.md
    r_lines = []
    r_lines.append(f"# {a['title']}")
    r_lines.append("")
    r_lines.append("## What is this assignment?")
    r_lines.append("")
    r_lines.append(a["desc"])
    r_lines.append("")
    r_lines.append("## What you need to do")
    r_lines.append("")
    for t in a["tasks"]:
        r_lines.append(f"- {t}")
    r_lines.append("")
    r_lines.append("## Concepts practiced")
    r_lines.append("")
    for cp in a["concepts"]:
        r_lines.append(f"- {cp}")
    r_lines.append("")
    r_lines.append(f"## Related Section\n\n{a['section']}\n")
    r_lines.append("## Related Lessons\n")
    for rl in a["lessons"]:
        r_lines.append(f"- {rl}")
    r_lines.append("")
    r_lines.append("## Important Resources\n")
    for ir in a["resources"]:
        r_lines.append(f"- {ir}")
    r_lines.append("")
    r_lines.append(f"## Solution\n\nOfficial solution walkthroughs, reference notebooks, and production code files are detailed in [solution.md](file:///{a_dir.replace(chr(92), '/')}/solution.md).\n")
    
    with open(os.path.join(a_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(r_lines) + "\n")
        
    # 2. assignment.md
    as_lines = []
    as_lines.append(f"# {a['title']} — Requirements & Specification")
    as_lines.append("")
    as_lines.append(a["assignment_reqs"])
    with open(os.path.join(a_dir, "assignment.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(as_lines) + "\n")
        
    # 3. resources.md
    res_lines = []
    res_lines.append(f"# Resources & References — {a['title']}")
    res_lines.append("")
    for ir in a["resources"]:
        res_lines.append(f"- {ir}")
    with open(os.path.join(a_dir, "resources.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(res_lines) + "\n")
        
    # 4. solution.md
    sol_lines = []
    sol_lines.append(f"# Official Solution Walkthrough — {a['title']}")
    sol_lines.append("")
    sol_lines.append(a["solution"])
    with open(os.path.join(a_dir, "solution.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(sol_lines) + "\n")
        
    print(f"Generated assignment folder: {a_dir}")

# Capstone Project
capstone_dir = os.path.join(PROJ_DIR, "Capstone-Production-Agentic-AI-Product")
os.makedirs(capstone_dir, exist_ok=True)

# 1. Project README.md
p_readme = """# Capstone Project — Production Agentic AI E-Commerce Product

## Executive Summary
The Capstone Project represents the synthesis of the entire End-to-End AI Engineering Bootcamp. Students design, build, optimize, and deploy an enterprise-grade Autonomous Agentic E-Commerce System capable of conversational product discovery, review sentiment analysis, real-time shopping cart manipulation, multi-turn state persistence, and decoupled tool execution over Model Context Protocol (MCP) microservices.

## System Objective
Build an AI shopping concierge that autonomously interprets natural language requests, formulates multi-step execution plans, coordinates between specialized worker agents, executes precise hybrid vector queries against the Amazon Electronics catalog, manages user cart transactions in PostgreSQL, streams real-time status updates over Server-Sent Events (SSE), and maintains high reliability via LiteLLM model fallbacks and automated CI evaluation gates.

## Technologies & Stack
- **Framework**: LangGraph (StateGraph cyclical state machines, PostgresSaver checkpointers)
- **Backend**: FastAPI (Python 3.11+, SSE streaming, Pydantic v2 schemas)
- **Frontend**: Streamlit (Reactive chat UI, live cart sidebar, grounding product cards, LangSmith feedback widgets)
- **Vector Database**: Qdrant (Dense + Sparse Hybrid Search, payload filters)
- **Relational Database**: PostgreSQL (LangGraph checkpointers + shopping cart tables)
- **Tool Protocol**: Model Context Protocol (FastMCP microservices running on independent ports)
- **Observability**: LangSmith (Distributed trace trees, user feedback score attribution) & OpenTelemetry
- **Resilience**: LiteLLM Router (Fallback cascades across OpenAI, Anthropic, and Google APIs)
- **Containerization**: Docker & Docker Compose (6-service container topology)

## Key Milestones
1. **Sprint 0**: Project framing, environment setup, Amazon catalog ingestion, and baseline RAG prototype.
2. **Sprint 1**: Pydantic structured outputs, Qdrant hybrid search, cross-encoder re-ranking, and YAML prompt registries.
3. **Sprint 2**: LangGraph ReAct agent loop, intent routing node, and query expansion.
4. **Sprint 3**: Multi-turn persistence with PostgresSaver, second Qdrant review collection, FastMCP microservices, and SSE streaming.
5. **Sprint 4**: Multi-agent Supervisor architecture, specialized Shopping Cart agent, and live UI synchronization.
6. **Sprint 5**: LiteLLM fallback routing, prompt caching optimization, remote A2A protocols, CI evaluation gates, and Dockerized deployment.
"""

# 2. Project requirements.md
p_requirements = """# Capstone Project — Detailed System Requirements & Architecture Specification

## 1. Functional Requirements

### 1.1 Intent Routing & Query Guardrails
- System must intercept incoming user messages with a lightweight `intent_router_node`.
- Queries classified as non-shopping conversation must terminate immediately with appropriate conversational greetings, bypassing expensive vector search and tool iteration loops.

### 1.2 Multi-Turn Conversational Persistence
- Must support uninterrupted multi-turn conversations indexed by unique `thread_id`.
- Graph state must be saved to PostgreSQL via `PostgresSaver` checkpointers after every node transition.
- User context, past recommendations, and intermediate execution thoughts must persist across browser reloads.

### 1.3 Adaptive Multi-Source Retrieval (Agentic RAG)
- **Product Catalog Search**: Must perform hybrid search (dense semantic embedding `text-embedding-3-small` + sparse lexical BM25) in Qdrant with cross-encoder re-ranking.
- **Customer Reviews Search**: Must query a dedicated Amazon Reviews Qdrant collection to assess customer sentiment, common complaints, and verified purchase opinions.
- Both tools must be exposed via independent FastMCP servers (`items_mcp_server` on port 8002, `reviews_mcp_server` on port 8001).

### 1.4 Transactional Shopping Cart Management
- Specialist Shopping Cart Agent must execute transactional SQL operations in PostgreSQL:
  - `add_to_cart(asin: str, quantity: int)`
  - `get_cart_contents()`
  - `remove_from_cart(asin: str)`
- Shopping cart changes must reflect instantly in the Streamlit frontend sidebar.

### 1.5 Real-Time Streaming & UX
- Backend must stream Server-Sent Events (SSE) broadcasting agent thought milestones (`"Analysing question..."`, `"Planning..."`, `"Looking for items..."`).
- Final response payload must deliver structured JSON containing markdown answer text, grounding product cards (images, prices, descriptions), and backend `trace_id`.

### 1.6 User Feedback & Observability
- Frontend must allow users to submit thumbs-up/down ratings linked directly to `trace_id`.
- Backend must log feedback directly into LangSmith run trees for automated error curation.

## 2. Non-Functional & Reliability Requirements

### 2.1 High Availability & Fallback Routing
- Must integrate LiteLLM Router to automatically cascade failed primary API calls (e.g. GPT-4o) to secondary models (Claude-3-5-Sonnet, Gemini-1.5-Pro) on HTTP 429 rate limits or timeouts.

### 2.2 Latency & Cost Optimization
- Prompts must adhere to strict prefix alignment: static instructions and tool definitions at the head, dynamic inputs at the tail, to achieve >= 50% prompt caching hit rate.

### 2.3 Automated CI Evaluation Gates
- Automated test script `eval_retriever.py` must run in CI, validating that Hit Rate@5 across golden test datasets exceeds 85%.

### 2.4 Container Deployment
- The entire system must launch deterministically via `docker-compose.yml` coordinating 6 services:
  1. `streamlit-app` (port 8501)
  2. `api` (port 8000)
  3. `qdrant` (ports 6333, 6334)
  4. `postgres` (port 5433:5432)
  5. `reviews_mcp_server` (port 8001)
  6. `items_mcp_server` (port 8002)
"""

# 3. Project resources.md
p_resources = """# Capstone Project — Resources & References

## Primary Architecture Artifacts
- **Docker Orchestration Specification**: [docker-compose.yml](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/docker-compose.yml)
- **FastAPI Application Backend**: [apps/api/src/api/app.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/src/api/app.py)
- **LangGraph StateGraph Workflow**: [apps/api/src/api/agents/graph.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/src/api/agents/graph.py)
- **Agent Definitions & Prompt Management**: [apps/api/src/api/agents/agents.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/src/api/agents/agents.py)
- **Streamlit Frontend Chat & Cart UI**: [apps/chatbot_ui/src/chatbot_ui/app.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/chatbot_ui/src/chatbot_ui/app.py)
- **Items FastMCP Server**: [apps/items_mcp_server/src/items_mcp_server/main.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/items_mcp_server/src/items_mcp_server/main.py)
- **Reviews FastMCP Server**: [apps/reviews_mcp_server/src/reviews_mcp_server/main.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/reviews_mcp_server/src/reviews_mcp_server/main.py)
- **Automated Retriever Evaluation Script**: [apps/api/evals/eval_retriever.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/evals/eval_retriever.py)

## Showcase & Presentation Recordings
- **Capstone Build Lab Video**: [060 Sprint Build Lab Containerise your capstone and implement CI Pipeline.mp4](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/060%20FEB%2026%20Sprint%20Build%20Lab%20Containerise%20your%20capstone%20and%20implement%20CI%20Pipeline.mp4)
- **Demo Day Presentations**: [071 MAR 10 Demo Day Present your working AI product to cohort.mp4](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/071%20MAR%2010%20Demo%20Day%20Present%20your%20working%20AI%20product%20to%20cohort.mp4)
- **Closing Celebration & Retrospective**: [072 MAR 12 Closing Celebration & Feedback.mp4](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/072%20MAR%2012%20Closing%20Celebration%20&%20Feedback.mp4)
"""

# 4. Project solution.md
p_solution = """# Capstone Project — Production Solution & Code Walkthrough

## 1. Master Architecture Overview
The complete working production solution is encapsulated within the `ai-engineering-bootcamp-cohort-4-main` codebase.

```mermaid
graph TD
    User([End User / Browser]) <--> UI[Streamlit UI :8501]
    UI <-- HTTP / SSE Stream --> API[FastAPI Backend :8000]
    
    subgraph Backend Architecture
        API --> Graph[LangGraph Multi-Agent Workflow]
        Graph --> Router[Intent Router Node]
        Router -->|Product Query| Agent[Product Q&A Agent]
        Router -->|Cart Intent| CartAgent[Shopping Cart Agent]
        Router -->|General| EndNode[END]
        
        Agent --> ToolNode[MCP Tool Execution Node]
        ToolNode <-- HTTP/SSE --> ItemMCP[Items FastMCP Server :8002]
        ToolNode <-- HTTP/SSE --> ReviewMCP[Reviews FastMCP Server :8001]
        
        CartAgent --> SQLTools[Postgres Cart CRUD Tools]
    end
    
    ItemMCP --> Qdrant[(Qdrant Vector DB :6333)]
    ReviewMCP --> Qdrant
    SQLTools --> Postgres[(PostgreSQL DB :5432)]
    Graph <-- Checkpoints --> Postgres
    API --> LangSmith[LangSmith Tracing & Evals]
```

## 2. Key Code Files in the Repository
1. **Multi-Agent State Graph**: [apps/api/src/api/agents/graph.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/src/api/agents/graph.py)
   - Implements `StateGraph(State)` with typed state reducer `operator.add`.
   - Compiles with `PostgresSaver.from_conn_string(...)` checkpointer.
   - Generates Server-Sent Events (SSE) via `agent_stream_wrapper` yielding node lifecycle updates.
2. **Specialized Agents & Prompts**: [apps/api/src/api/agents/agents.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/src/api/agents/agents.py)
   - Decoupled prompt loading from YAML registries.
   - Pydantic models for structured output generation (`RAGUsedContext`).
3. **Decoupled FastMCP Tool Servers**:
   - [apps/items_mcp_server/src/items_mcp_server/main.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/items_mcp_server/src/items_mcp_server/main.py): Item catalog FastMCP server.
   - [apps/reviews_mcp_server/src/reviews_mcp_server/main.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/reviews_mcp_server/src/reviews_mcp_server/main.py): Customer reviews FastMCP server.
4. **Streamlit Frontend Application**: [apps/chatbot_ui/src/chatbot_ui/app.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/chatbot_ui/src/chatbot_ui/app.py)
   - Consumes backend SSE streaming endpoint.
   - Renders product cards with images, prices, and descriptions.
   - Synchronizes live cart contents in the UI sidebar.
   - Provides user thumbs-up/down feedback linked to LangSmith trace IDs.
5. **Multi-Service Container Orchestration**: [docker-compose.yml](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/docker-compose.yml)
   - Spans 6 containers with environment variable injection, port forwards, and persistent volume mounts.
"""

with open(os.path.join(capstone_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(p_readme)
with open(os.path.join(capstone_dir, "requirements.md"), "w", encoding="utf-8") as f:
    f.write(p_requirements)
with open(os.path.join(capstone_dir, "resources.md"), "w", encoding="utf-8") as f:
    f.write(p_resources)
with open(os.path.join(capstone_dir, "solution.md"), "w", encoding="utf-8") as f:
    f.write(p_solution)

print("Generated Projects/Capstone-Production-Agentic-AI-Product")
