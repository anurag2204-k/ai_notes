# Human-in-the-Loop (HITL) and LangSmith Trace Feedback

Type: System Reliability & Telemetry Guide

## What it teaches

This lesson teaches how to implement human oversight checkpoints and capture qualitative user feedback tied to distributed telemetry. It covers LangGraph execution interrupts for high-impact actions and explains how to link frontend user ratings to backend LangSmith trace runs.

## Key concepts

- Human-in-the-Loop (HITL): Workflow breakpoints pausing graph execution before sensitive tool calls to await human approval
- Graph Interrupts: `interrupt()` functions halting execution while preserving checkpoint state in PostgreSQL
- Trace Attribution: Passing backend `trace_id` to the frontend and sending thumbs-up/down ratings back to `/feedback`
- Flywheel Dataset Generation: Filtering production traces with negative user feedback to build targeted regression evaluation sets

## Important takeaways

- Autonomous agents in high-stakes domains must have explicit human sign-off gates before committing irreversible actions.
- LangGraph checkpointers make human-in-the-loop seamless by persisting state indefinitely while waiting for user interaction.
- Capturing user feedback without trace IDs is useless; feedback must be mathematically attached to the exact LLM run.
- Production feedback loops turn user complaints into automated test cases that permanently prevent repeat errors.

## Connection to section

- Implemented in Sprint 3 to provide real-time feedback collection and safety controls.
- Connected to the Streamlit UI and FastAPI backend feedback endpoints.

