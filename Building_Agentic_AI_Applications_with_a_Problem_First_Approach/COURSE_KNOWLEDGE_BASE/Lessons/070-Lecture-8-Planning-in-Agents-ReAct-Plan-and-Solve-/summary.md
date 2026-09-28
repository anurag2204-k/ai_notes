# [070] — [Core] Lecture 8: Planning in Agents (ReAct, Plan-and-Solve & Reflection)

Category:
Core

Type:
Core Lecture

Available Formats:
- HTML Lesson Page

Associated Source Files:
- `102 [Core] Planning in Agents (ReAct Prompting).html`

## What this lesson is about
Core algorithmic mechanics of autonomous agent planning. It examines ReAct (Reasoning + Acting) loops, Plan-and-Solve strategies, Tree-of-Thoughts exploration, and verbal reflection mechanisms that allow agents to self-correct during multi-step executions.

## Key Concepts
- Autonomous ReAct execution loops (Thought -> Action -> Observation)
- Model Context Protocol (MCP) client-server architecture and tool exposure
- Supervisor-Worker and multi-agent coordination patterns
- Cycle termination, state checkpointing, and loop guardrails

## Important Takeaways
- Focus ruthlessly on the user's business problem rather than forcing agentic autonomy where deterministic code suffices.
- Cleanly decouple state management, tool interfaces, and model prompts to maintain maintainable agent codebases.
- Always instrument production observability (token usage, latency, error boundaries) before deploying to users.

## How it connects to the course
- Fits directly into **Module 08** (Week 4) of the curriculum.
- Builds foundational theory and practical patterns directly implemented in Perplexia AI.

## Important Resources
- **Tree of thought:** [https://arxiv.org/abs/2409.11527](https://arxiv.org/abs/2409.11527)
- **hierarchal planning:** [https://arxiv.org/abs/2408.16090](https://arxiv.org/abs/2408.16090)
- **ReAct:** [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)
- **https://www.pinecone.io/learn/langgraph-research-agent/:** [https://www.pinecone.io/learn/langgraph-research-agent/](https://www.pinecone.io/learn/langgraph-research-agent/)
- **[Core] Lecture 8: Planning in Agents (ReAct, Plan-and-Solve & Reflection) Resource:** [https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)

