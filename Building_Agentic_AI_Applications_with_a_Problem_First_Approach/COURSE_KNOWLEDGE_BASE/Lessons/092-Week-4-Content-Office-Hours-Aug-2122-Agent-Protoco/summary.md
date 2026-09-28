# [092] — Week 4 Content Office Hours (Aug 21/22): Agent Protocols & Production Pitfalls

Category:
Office Hours

Type:
Office Hours

Available Formats:
- MP4 Video Recording
- DOCX Transcribed Q&A Notes

Associated Source Files:
- `134 Week 4 Content Office Hours - Aug 22.mp4`
- `135 Week 4 Content Office Hours - August 21.docx`

## What this lesson is about
Live office hours technical discussion led by the course instructors and TAs. It addresses student implementation bottlenecks, architectural trade-offs, debugging error traces, and concrete system design questions for the cohort.

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
- Fits directly into **Module 09** (Week 4) of the curriculum.
- Builds foundational theory and practical patterns directly implemented in Perplexia AI.

## Important Resources
- No external links required; reference the associated course recordings or slide decks.

