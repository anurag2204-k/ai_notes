# Assignment 1 — Perplexia AI Part 1: Workflow Agents & Tool Integration

## What is this assignment?
Assignment 1 kicks off the development of **Perplexia AI**—your custom AI search and research assistant. In this initial phase, you build the foundational workflow agent capable of understanding user queries, dynamically routing them to specialized execution paths, executing deterministic external tools (such as a calculator or datetime tool), and maintaining multi-turn conversational memory.

## What you need to do
- **Part 1 (Query Routing):** Construct a query classification prompt that analyzes user input and routes between direct conversational responses and tool execution.
- **Part 2 (Tool Integration):** Implement custom tools (a Calculator tool for arithmetic expressions and optionally a DateTime tool for current timestamp awareness).
- **Part 3 (Conversational Memory):** Integrate stateful conversational memory using `RunnableWithMessageHistory` in LangChain (or Memory components in LangFlow) to maintain chat context across multiple user turns.
- **Part 4 (System Evaluation):** Run the provided test cases to verify that calculation questions trigger tool calls while general knowledge questions produce direct responses with correct historical continuity.

## Concepts being practiced
- In-Context Prompt Engineering & Few-Shot Routing
- Custom Tool Binding and Schema Definition
- Deterministic Routing Chains (LCEL / Runnable Branch)
- Conversational Memory State Management
- Visual vs Code-based Agent Pipeline Construction

## Related Course Lessons
- Lesson `004` & `005`: [Build] LangChain Setup and Interactive Demo
- Lesson `006` & `007`: [Build] LangFlow Setup and Visual Pipeline Demo
- Lesson `023`: [Core] Lecture 3: Prompt Engineering in 2025
- Lesson `024`: [Core] Lecture 4: Building Workflow Agents For The Enterprise
- Lessons `035`, `036`, `037`: Assignment 1 Specifications & Test Benchmarks

## Difficulty / Scope
- **Difficulty:** Introductory to Intermediate
- **Estimated Completion Time:** 4–6 hours
- **Prerequisites:** Python 3.10+, basic familiarity with LCEL or visual node connections in LangFlow, OpenAI API key.

## Important Links
- [Assignment Instructions Page](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-LangChain-and-LangFlow-Basics/assignment.md)
- [Assignment Starter Code & Resources](https://drive.google.com/drive/folders/1TiWFMDmrta6NKQgSA7Vv3jlM0Y1pflOw?usp=sharing)
- [Official Solution Guide](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-LangChain-and-LangFlow-Basics/solution.md)
- [LangChain Custom Tools Documentation](https://python.langchain.com/docs/how_to/custom_tools/)
- [LangChain RunnableWithMessageHistory Guide](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.history.RunnableWithMessageHistory.html)

## Solution
Official walkthrough videos and completed code are available. See [solution.md](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-LangChain-and-LangFlow-Basics/solution.md) for full walkthrough links and repository paths.
