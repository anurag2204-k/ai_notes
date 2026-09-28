# Module / Lesson Group 05
## Lessons 035–043: Assignment 1 Implementation: Building Perplexia AI Part 1 & Enterprise Lifecycle

### Big Picture
Hands-on execution of Assignment 1. Students implement the Perplexia AI router, custom tools, and conversational state in either LangChain or LangFlow. Supported by guest lectures from Microsoft enterprise practitioners and rigorous office hours addressing state management.

### Conceptual Flow
```
Assignment 1 LangChain Specs (035) → Assignment 1 LangFlow Specs (036) → Test Cases Benchmark (037) → Troubleshooting & FAQ (038) → Homework Office Hours (Aug 6): Memory & Routing (039) → Content Office Hours (Aug 7/8): Structured Prompts (040) → Guest Lecture: Agent Development Lifecycle [Sam Julien & Ugo Osuji] (041) → Content Office Hours (Aug 9): Guardrails (042) → Homework Office Hours (Aug 9): Final Submissions (043)
```

Students review assignment specifications and test cases (035-037), resolve execution hurdles using the FAQ (038), receive debugging support in office hours (039-040, 042-043), and gain enterprise perspective on production agent lifecycles from Microsoft leaders (041).

### Key Ideas
- **Router accuracy:** Ensuring edge-case math queries route to tools while conversational prompts retain memory.
- **Stateful memory injection:** Injecting conversation history dynamically via `RunnableWithMessageHistory` without exceeding token limits.
- **Enterprise agent lifecycle:** The shift from prototyping to versioning, continuous evaluation, and telemetry.
- **Graceful degradation:** Catching tool errors and allowing the LLM to explain failures cleanly.

### How the Pieces Fit Together
Successfully produces the working v1 baseline of Perplexia AI, ready to receive knowledge integration in Week 3.

### What You Should Know After This Section
- How to pass all 5 benchmark test cases in Assignment 1.
- How to manage chat session IDs and persist memory across turns.
- How Microsoft approaches enterprise agent lifecycle governance and deployment.

### Related Assignments
- Complete and submit **Assignment 1** (Perplexia AI Part 1).

### Important Resources
- [Assignment 1 Workspace](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-LangChain-and-LangFlow-Basics/README.md)
- [Starter Drive Folder](https://drive.google.com/drive/folders/1TiWFMDmrta6NKQgSA7Vv3jlM0Y1pflOw?usp=sharing)

