# Assignment 4 — Agentic RAG, MCP Microservices & Real-Time Streaming

## What is this assignment?

Scale the agent architecture to support persistent multi-turn conversations, multiple retrieval tools, decoupled FastMCP microservices, real-time Server-Sent Events (SSE) streaming, and human-in-the-loop feedback logging to LangSmith.

## What you need to do

- Configure PostgreSQL and `PostgresSaver` checkpointer to persist agent state across conversational turns using `thread_id`.
- Index the Amazon Customer Reviews dataset into Qdrant and build a second retrieval tool (`get_formatted_reviews_context`).
- Decouple the two retrieval tools into independent FastMCP servers (`items_mcp_server` on port 8002, `reviews_mcp_server` on port 8001).
- Create a custom MCP Tool Node in LangGraph that queries MCP servers over HTTP/SSE transports.
- Implement an SSE streaming generator (`agent_stream_wrapper`) in FastAPI yielding real-time node lifecycle status updates.
- Add a feedback submission endpoint in FastAPI that attaches user ratings directly to LangSmith trace runs.

## Concepts practiced

- PostgresSaver Checkpointing & Multi-Turn State Persistence
- Multi-Tool Agentic RAG (Catalog + Review Sentiment)
- Model Context Protocol (MCP) & FastMCP Microservices
- Server-Sent Events (SSE) Real-Time State Streaming
- Human Feedback Attribution in LangSmith

## Related Section

Section 3 — Moving From Basic To Agentic RAG

## Related Lessons

- 001 Agent integrations with RAG systems
- 002 Human Feedback and Fault Tolerance in Agentic Systems
- 003 Human in the loop (HITL)
- 004 Model Context Protocol (MCP)

## Important Resources

- [005 Hands-on Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%203%20–%20Moving%20From%20Basic%20To%20Agentic%20RAG/005%20Hands-on%20Section.html)
- [Sprint-3-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-3-info-review.pdf)
- [037 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/037%20FEB%2003%20Sprint%20Review%20Moving%20from%20basic%20to%20agentic%20RAG.mp4)
- [041-048 Hands-on Videos 1-8](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)

## Solution

Official solution walkthroughs, reference notebooks, and production code files are detailed in [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-04-Agentic-RAG-MCP-Human-in-the-Loop/solution.md).

