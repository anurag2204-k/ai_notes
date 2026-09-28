# Capstone Project — Detailed System Requirements & Architecture Specification

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
