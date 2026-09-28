# Naive vs. Advanced Retrieval-Augmented Generation (RAG)

Type: Architecture Lecture

## What it teaches

This lesson deconstructs the architectural progression from naive 'Retrieve-Then-Generate' pipelines to advanced RAG systems. It explains the mechanics of vector lookup, context injection, and parametric vs. non-parametric memory. It systematically catalogs the primary failure modes of naive RAG.

## Key concepts

- Parametric vs. Non-Parametric Memory: LLM internal weights versus external knowledge retrieval
- Naive RAG Pipeline: Vectorize query → Retrieve top-k nearest neighbors → Stuff context into prompt → Generate response
- Core RAG Failure Modes: Retrieval miss, hallucinated context, context overflow, lost-in-the-middle phenomenon
- Grounding Mechanics: Enforcing strict instruction boundaries to prevent parametric hallucinations

## Important takeaways

- Naive RAG fails in production because semantic similarity does not guarantee relevance or factual completeness.
- Context stuffing introduces noise that degrades LLM attention, leading to inaccurate answers.
- Grounding prompts must explicitly forbid the model from speculating beyond retrieved evidence.
- Advanced RAG introduces multi-stage retrieval, re-ranking, and dynamic agent loops to mitigate naive flaws.

## Connection to section

- Explains the motivation for Sprint 0's baseline RAG prototype.
- Sets the stage for the retrieval optimizations and context engineering implemented in Sprint 1.

