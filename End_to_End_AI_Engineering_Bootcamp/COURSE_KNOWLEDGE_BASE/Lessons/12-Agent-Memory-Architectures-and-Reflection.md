# Agent Memory Architectures and Reflection Frameworks

Type: Architecture Lecture

## What it teaches

This lesson analyzes agent memory systems and reflection mechanisms. It categorizes memory into working, short-term, and long-term stores, explaining how agents maintain context over extended workflows. It also presents reflection loops that enable agents to critique and refine their own intermediate work.

## Key concepts

- Memory Taxonomy: Working memory (current execution state), Short-term memory (session history), Long-term memory (persistent DB)
- Reflection Loops: Self-critique nodes prompting the LLM to verify factual accuracy and constraint compliance before terminating
- Context Window Management: Pruning, summarization, and vector retrieval of past conversational history to prevent context overflow
- Trajectory Evaluation: Evaluating the validity of the intermediate reasoning steps taken rather than just the final answer

## Important takeaways

- Working memory lives in the transient graph state; short-term memory requires session checkpointers; long-term memory requires external databases.
- Reflection loops significantly reduce hallucination rates in complex synthesis tasks at the cost of additional latency.
- Unconstrained memory growth causes context rot: older dialogue turns must be compressed or summarized.
- Agent evaluation requires assessing step efficiency: an agent that uses 10 tool calls to find what could be found in 1 is inefficient.

## Connection to section

- Completes the theoretical foundations of Sprint 2.
- Informs the multi-turn session persistence implemented in Sprint 3.

