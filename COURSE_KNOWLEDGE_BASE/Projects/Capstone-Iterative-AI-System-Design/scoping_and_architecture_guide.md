# Capstone Scoping & Architectural Design Guide

## Blueprint for a Winning Capstone Architecture

```
[Phase 1: Problem Scoping]
  - Identify non-linear cognitive tasks where rules fail.
  - Define user persona, input modalities, and required SLA.

[Phase 2: Architectural Iterations]
  ┌────────────────────────────────────────────────────────┐
  │ Iteration 1: Deterministic Prompt & Rule Pipeline      │
  │ • Fast baseline, low cost, 0 agentic loops             │
  └──────────────────────────┬─────────────────────────────┘
                             │ (Identify knowledge gaps)
                             ▼
  ┌────────────────────────────────────────────────────────┐
  │ Iteration 2: Enterprise Hybrid RAG + Router            │
  │ • Vector DB + Tavily fallback + HyDE query expansion   │
  └──────────────────────────┬─────────────────────────────┘
                             │ (Identify reasoning bottlenecks)
                             ▼
  ┌────────────────────────────────────────────────────────┐
  │ Iteration 3: Supervisor-Worker Multi-Agent System       │
  │ • LangGraph StateGraph, MCP Tool Servers, Evals        │
  └────────────────────────────────────────────────────────┘

[Phase 3: Operational & Economic Feasibility]
  - Token cost per run = (Input_Tokens * Input_Price) + (Output_Tokens * Output_Price)
  - Latency budget = Σ(LLM time) + Σ(Tool time) + Network overhead
  - Error mitigation: Fallbacks, timeouts, and human intervention gateways.
```
