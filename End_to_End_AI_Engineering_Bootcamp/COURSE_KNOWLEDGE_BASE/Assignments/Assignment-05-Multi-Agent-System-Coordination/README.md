# Assignment 5 — Multi-Agent System Coordination & Transactional Tooling

## What is this assignment?

Architect a production Multi-Agent System (MAS) in LangGraph using the Supervisor / Coordinator pattern. Create PostgreSQL shopping cart tables and transactional tools, implement a dedicated Shopping Cart specialist agent, design a Coordinator Agent that plans and delegates workflows, and synchronize cart state to the UI in real time.

## What you need to do

- Create relational PostgreSQL tables for shopping cart management (`cart_id`, `user_id`, `asin`, `quantity`, `added_at`).
- Implement three transactional Python tools: `add_to_cart`, `get_cart_contents`, and `remove_from_cart`.
- Build a specialized Shopping Cart Agent with dedicated system prompt and transactional database tools.
- Implement a Coordinator Agent that parses multi-step user prompts, routes intent between Product Q&A and Cart agents, and synthesizes results.
- Integrate Coordinator, Cart Agent, and Q&A Agent into a unified multi-agent LangGraph workflow.
- Update the Streamlit UI to display live shopping cart state synchronized after agent tool actions.

## Concepts practiced

- Multi-Agent Supervisor / Coordinator Architecture
- Agent Specialization & Tool Boundary Segregation
- Transactional Relational Database Tooling
- Inter-Agent Delegation & Handback Flows
- Live UI State Synchronization

## Related Section

Section 4 — Multi-Agent Systems

## Related Lessons

- 01 Multi-agent systems and when to use it
- 02 Planning, delegation, and task routing among agents
- 03 Synchronization and memory sharing
- 04 Agent-to-agent communication protocols (A2A)

## Important Resources

- [05 Hands-on Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%204%20–%20Multi-Agent%20Systems/05%20Hands-on%20Section.html)
- [Sprint-4-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-4-info-review.pdf)
- [049 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/049%20FEB%2017%20Sprint%20Review%20Designing%20and%20orchestrating%20multi-agent%20systems.mp4)
- [051-058 Hands-on Videos 1-8](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)

## Solution

Official solution walkthroughs, reference notebooks, and production code files are detailed in [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-05-Multi-Agent-System-Coordination/solution.md).

