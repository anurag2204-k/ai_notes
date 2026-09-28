# Server-Sent Events (SSE) and Graph State Streaming

Type: Full-Stack Integration Guide

## What it teaches

This lesson teaches how to eliminate perceived latency in agentic systems by streaming intermediate node events and tokens over Server-Sent Events (SSE). It explains how LangGraph event streams are transformed into SSE packets in FastAPI and consumed reactively in frontend user interfaces.

## Key concepts

- Perceived Latency Problem: Multi-step agent reasoning taking 5-15 seconds, causing poor user UX without real-time feedback
- LangGraph Stream Modes: `stream_mode=['debug', 'values']` yielding node start, updates, tool calls, and final outputs
- Server-Sent Events (SSE): Unidirectional HTTP streaming protocol transmitting real-time text chunks (`data: ...\n\n`)
- Frontend Event Parsing: Intercepting node status events ('Analysing...', 'Searching...') to render interactive UI progress bars

## Important takeaways

- Streaming is not optional for agentic AI: users must see immediate confirmation that the system is actively working.
- SSE is significantly lighter and simpler to implement over standard HTTP than bidirectional WebSockets for conversational agents.
- Separating intermediate status events from final structured payload events ensures clean frontend rendering.
- Yielding tool call previews ('Looking for items: wireless headphones') builds user trust by exposing the agent's reasoning path.

## Connection to section

- Implemented in Sprint 3 across FastAPI (`agent_stream_wrapper`) and Streamlit.
- Maintained across all subsequent multi-agent and production deployment sprints.

