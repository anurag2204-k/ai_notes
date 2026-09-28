# LangGraph StateGraph and Cyclical Workflows

Type: Technical Tutorial & Code Guide

## What it teaches

This lesson teaches the core abstractions of the LangGraph framework. It explains how LangGraph models multi-step agent reasoning as cyclical directed state machines, contrasting it with linear DAG frameworks. It covers StateGraph definitions, node functions, edge routing, and state reducers.

## Key concepts

- LangGraph Core Abstractions: StateGraph, Nodes (pure Python functions), Edges, Conditional Edges, START, and END
- Typed Graph State: Pydantic schemas or TypedDicts defining shared memory across graph execution
- State Reducers: Using operators (e.g., `operator.add`) to append new messages rather than overwriting historical context
- Cyclical Execution: Enabling loopback transitions from tool execution nodes back to agent reasoning nodes

## Important takeaways

- Linear DAGs cannot model real-world agent behavior; cyclical graphs are required for feedback and tool retries.
- LangGraph nodes must be pure functions that take the current state and return incremental state updates.
- Conditional edges inspect state variables to determine deterministic next-step transitions.
- State schemas provide strict type safety and compile-time validation for complex multi-node workflows.

## Connection to section

- Introduced in Sprint 2 as the primary agent execution framework.
- Used to build the single-turn agent in Sprint 2, the multi-turn agent in Sprint 3, and the multi-agent system in Sprint 4.

