# Tool Use, Function Calling, and ReAct Agent Loops

Type: Code Tutorial & Implementation Guide

## What it teaches

This lesson teaches the mechanics of tool binding, function calling, and constructing autonomous ReAct (Reason + Act) loops in LangGraph. It details how tools are converted into JSON schemas, how LLMs emit tool calls, and how tool execution results are injected back into the reasoning loop.

## Key concepts

- ReAct Framework: Interleaving thought (reasoning trace), action (tool execution), and observation (tool output)
- Tool Specification: Defining tools with explicit type hints, descriptive docstrings, and Pydantic parameter schemas
- ToolNode in LangGraph: Prebuilt or custom execution node that receives tool call payloads and invokes underlying Python functions
- Loopback Edge: Routing ToolNode output back to the agent node so the LLM can evaluate whether additional tools are required

## Important takeaways

- LLMs do not execute code directly; they generate structured JSON payloads representing intended function calls.
- Tool docstrings are prompt instructions: vague docstrings cause tool hallucination and incorrect arguments.
- A ReAct loop allows an agent to recover from empty search results by formulating an alternative query.
- Max iteration guards must always be enforced in conditional edges to prevent infinite execution loops.

## Connection to section

- Implemented in Sprint 2 to build the single-turn ReAct agent with hybrid retrieval tools.
- Extended in Sprint 3 with MCP servers and multiple domain tools.

