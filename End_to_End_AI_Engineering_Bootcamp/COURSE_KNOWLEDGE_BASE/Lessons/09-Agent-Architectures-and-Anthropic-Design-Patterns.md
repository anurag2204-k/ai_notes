# Agent Architectures and Anthropic's Agentic Design Patterns

Type: Conceptual Lecture & Architecture Guide

## What it teaches

This lesson teaches the core design patterns of agentic systems based on Anthropic's 'Building Effective Agents' research. It analyzes the spectrum of autonomy—from deterministic augmented LLMs and prompt chains to autonomous orchestrator-worker systems—guiding engineers on when and when NOT to build agents.

## Key concepts

- Spectrum of Autonomy: Augmented LLM → Prompt Chaining → Routing → Parallelization → Orchestrator-Workers → Evaluator-Optimizer
- Principle of Simplicity: Prioritizing deterministic code and simple chains before introducing autonomous loops
- Orchestrator-Workers Pattern: A central coordinator agent dynamically decomposes tasks and delegates to worker sub-agents
- Evaluator-Optimizer Loop: An agent generates a solution, a critic evaluates it against criteria, and feedback refines the output

## Important takeaways

- The most reliable agentic systems often use the simplest viable architecture rather than maximum autonomy.
- Deterministic routing should always be preferred over LLM tool selection when intent boundaries are clear.
- Orchestrator-worker patterns are ideal when task complexity cannot be anticipated in advance.
- Evaluator-optimizer loops are highly effective for code generation, translation, and structured data extraction.

## Connection to section

- Provides the theoretical blueprint for all agent development in Sprints 2, 3, and 4.
- Directly informs the Coordinator-Worker multi-agent architecture built in Sprint 4.

