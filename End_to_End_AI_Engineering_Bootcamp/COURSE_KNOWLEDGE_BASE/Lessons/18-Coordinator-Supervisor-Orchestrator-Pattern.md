# The Coordinator / Supervisor Orchestrator Pattern

Type: Implementation Guide & State Machine Design

## What it teaches

This lesson teaches how to build a production Coordinator / Supervisor Agent in LangGraph. It details how the coordinator parses user intent, creates multi-step plans, delegates sub-tasks to specialist worker agents, and regains control after worker execution to synthesize the final user response.

## Key concepts

- Supervisor Node Design: High-level planner maintaining overall workflow goals and routing decisions
- Worker Delegation: Passing sub-task state to specialized agents (e.g., Product Q&A Agent, Shopping Cart Agent)
- Control Handback: Worker nodes routing back to the supervisor node upon completion rather than terminating the graph
- Dynamic Re-Planning: Enabling the supervisor to adjust the execution plan if a worker encounters missing data or errors

## Important takeaways

- The Supervisor acts as the conductor of the multi-agent orchestra, preventing workers from executing in uncoordinated loops.
- Workers should be stateless sub-graphs that execute their specific function and report findings back to shared state.
- Explicit router conditions ensure deterministic control flow between supervisor and specialist agents.
- Supervisor planning prompts must include the capabilities and boundaries of each available worker agent.

## Connection to section

- Core architectural centerpiece of Sprint 4.
- Orchestrates the Product Q&A Agent and Shopping Cart Agent in the capstone repository.

