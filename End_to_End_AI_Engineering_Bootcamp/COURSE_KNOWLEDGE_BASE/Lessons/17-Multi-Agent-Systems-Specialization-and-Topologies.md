# Multi-Agent Systems: Specialization and Topologies

Type: Architecture Lecture

## What it teaches

This lesson teaches the fundamental architectural principles of Multi-Agent Systems (MAS). It analyzes why single agents suffer from tool overload, instruction conflict, and context pollution as scopes expand, and contrasts supervisor, hierarchical, and peer-to-peer collaboration topologies.

## Key concepts

- Single-Agent Bottlenecks: Context window bloat, tool selection confusion, conflicting system prompt instructions
- Agent Specialization: Decomposing systems into narrow, expert agents with isolated prompts and dedicated toolsets
- MAS Topologies: Supervisor / Coordinator pattern (central hub), Network / Peer-to-Peer (direct handoffs), Hierarchical (teams of teams)
- Trade-Off Analysis: Balancing task separation benefits against inter-agent communication overhead and token costs

## Important takeaways

- Do not adopt MAS for simple tasks; multi-agent architectures introduce orchestration latency and debugging complexity.
- MAS is essential when tools require incompatible prompt behaviors (e.g., precise SQL execution vs. creative natural language synthesis).
- The Supervisor pattern provides the strongest control and error recovery guarantees for commercial enterprise applications.
- Isolating tools inside specialized agents drastically reduces tool-calling hallucination and argument errors.

## Connection to section

- Foundational theory for Sprint 4.
- Directly dictates the multi-agent architecture built for the e-commerce capstone.

