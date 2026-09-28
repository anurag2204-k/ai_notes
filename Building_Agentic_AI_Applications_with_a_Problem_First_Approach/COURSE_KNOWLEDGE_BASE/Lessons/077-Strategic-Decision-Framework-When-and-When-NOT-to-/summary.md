# [077] — [Grow] Strategic Decision Framework: When and When NOT to Build Level 2 Agents

Category:
Grow

Type:
Deep Dive

Available Formats:
- HTML Lesson Page

Associated Source Files:
- `111 [Grow] How, When & When Not to Build Level 2 Agents in Enterprise (A Deep Dive).html`

## What this lesson is about
Technical resource and deep-dive material covering [Grow] Strategic Decision Framework: When and When NOT to Build Level 2 Agents. It provides specialized enterprise knowledge, architectural best practices, and curated frameworks supporting the curriculum.

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
- **Hugging Face Agent Leaderboard:** [https://huggingface.co/spaces/galileo-ai/agent-leaderboard](https://huggingface.co/spaces/galileo-ai/agent-leaderboard)
- **Berkeley’s Tool-Calling Leaderboard:** [https://gorilla.cs.berkeley.edu/leaderboard.html?ref=blog.langchain.dev](https://gorilla.cs.berkeley.edu/leaderboard.html?ref=blog.langchain.dev)
- **Opik:** [https://www.comet.com/site/products/opik/](https://www.comet.com/site/products/opik/)

