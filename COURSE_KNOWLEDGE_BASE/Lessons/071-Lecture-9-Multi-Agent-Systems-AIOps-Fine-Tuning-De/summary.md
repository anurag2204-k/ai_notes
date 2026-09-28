# [071] — [Core] Lecture 9: Multi-Agent Systems, AIOps & Fine-Tuning Decisions

Category:
Core

Type:
Core Lecture

Available Formats:
- HTML Lesson Page
- MP4 Video Recording

Associated Source Files:
- `103 [Core] Multi-Agent Systems, AIOps & Fine-Tuning.html`
- `104 [Core] Multi-Agent Systems, AIOps & Fine-Tuning.mp4`

## What this lesson is about
Design principles and topologies for multi-agent systems, AIOps, and fine-tuning. It compares Supervisor-Worker orchestrations, hierarchical teams, and peer-to-peer swarms, while providing a clear decision matrix on when to prompt, when to retrieve, and when to fine-tune.

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
- **slides:** [https://www.canva.com/design/DAGp_pzQIlM/vssS92mY1AzvB2T2Hk-C0g/view?utm_content=DAGp_pzQIlM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he4c0fa00a7](https://www.canva.com/design/DAGp_pzQIlM/vssS92mY1AzvB2T2Hk-C0g/view?utm_content=DAGp_pzQIlM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he4c0fa00a7)

