# Module / Lesson Group 08
## Lessons 069–082: Autonomous Agents, Dynamic Planning Protocols, Multi-Agent Systems & Fine-Tuning

### Big Picture
Transitioning to true agentic autonomy. Students explore dynamic ReAct planning loops, open protocols (Model Context Protocol and Google A2A), multi-agent orchestration topologies (Supervisor, Router, Swarm), and production AIOps/fine-tuning decision frameworks.

### Conceptual Flow
```
Core Lecture 7: Types of Agents & Protocols (069) → Core Lecture 8: Planning in Agents (070) → Core Lecture 9: Multi-Agent Systems & Fine-Tuning (071) → Ambient & Sub-Agents (072) → Agent Evaluation Guest Lecture (073) → Multi-Agent Design Patterns (074) → Google AI Co-Scientist Case Study (075) → Enterprise Agent Use Cases (076) → When NOT to Build Level 2 Agents (077) → AI Agent Tech Stack (078) → Agent Monitoring Deep Dive (079) → Open Protocols (MCP & A2A) (080) → Fine-Tuning 101 Guide (081) → Synthetic Data Generation (082)
```

Lecture 7 defines autonomy levels and MCP. Lecture 8 deconstructs ReAct and planning. Lecture 9 explores multi-agent collaboration and fine-tuning. The deep dives (072-082) provide architectural patterns (Supervisor pattern, Google Co-Scientist), evaluation methodologies, and fine-tuning guides (LoRA/QLoRA).

### Key Ideas
- **Level 3 vs Level 4 Autonomy:** Single agent with tools vs multiple specialized agents collaborating over structured protocols.
- **ReAct loop mechanics:** Generating thoughts, executing actions, observing tool outputs, and looping until completion.
- **Model Context Protocol (MCP):** The USB-C of AI systems—standardizing tool exposure across agents and platforms.
- **The Build vs Buy vs Fine-Tune Matrix:** Prompt first, augment with RAG second, fine-tune only when task form/style must be permanently encoded.
- **Multi-Agent Supervisor Pattern:** Central coordinator agent delegates sub-tasks to specialized worker agents.

### How the Pieces Fit Together
Provides the complete architectural theory for **Assignment 3** (Autonomous Deep Research Agent & MCP integration).

### What You Should Know After This Section
- The anatomy and message flow of the Model Context Protocol (Host-Client-Server).
- How to structure an autonomous ReAct loop without entering infinite execution cycles.
- How to build a multi-agent supervisor graph in LangGraph.
- When fine-tuning is required versus when in-context RAG is superior.

### Related Assignments
- Prepare for Assignment 3: Explore the MCP server examples and review the LangGraph multi-agent architecture.

### Important Resources
- [Lecture 7 Slides (Canva)](https://www.canva.com/design/DAGp-2A7DJo/37WmsnH5e5Kya6oFpaItSw/view?utm_content=DAGp-2A7DJo&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h15c38d0fd4)
- [Lecture 9 Slides (Canva)](https://www.canva.com/design/DAGp_pzQIlM/vssS92mY1AzvB2T2Hk-C0g/view?utm_content=DAGp_pzQIlM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he4c0fa00a7)
- [ReAct Paper (arXiv:2210.03629)](https://arxiv.org/abs/2210.03629)

