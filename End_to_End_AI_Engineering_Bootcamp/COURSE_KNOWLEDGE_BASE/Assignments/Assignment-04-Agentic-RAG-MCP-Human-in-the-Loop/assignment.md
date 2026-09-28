# Assignment 4 — Agentic RAG, MCP Microservices & Real-Time Streaming — Requirements & Specification

### Objectives
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
- Feedback endpoint in `apps/api/src/api/api/processors/submit_feedback.py`.
