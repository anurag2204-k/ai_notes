# Capstone Project — Production Agentic AI E-Commerce Product

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
