# Assignment 2 — Context Engineering, Hybrid Search & Re-Ranking

## What is this assignment?

Upgrade the baseline RAG pipeline into a high-precision retrieval system. Enforce Pydantic structured outputs with Instructor, implement dense + sparse hybrid search in Qdrant, integrate cross-encoder re-ranking, and decouple prompt templates into version-controlled Jinja2 YAML registries.

## What you need to do

- Define Pydantic schema models for structured RAG responses containing answers and typed item reference lists.
- Integrate Instructor library to guarantee strict schema validation with automatic retry loops.
- Create a new Qdrant collection configured for Hybrid Search supporting both dense vectors and sparse BM25 indices.
- Implement a two-stage retrieval pipeline: retrieve top-20 candidates via hybrid search, then re-rank top-5 using a cross-encoder model.
- Decouple system prompts into `retrieval_generation.yaml` and render dynamic contexts via Jinja2.
- Update the FastAPI backend to return structured JSON and update Streamlit to render product cards with images, prices, and ratings.

## Concepts practiced

- Pydantic Schema Validation & Instructor Library
- Hybrid Search (Dense Semantic + Sparse Lexical BM25)
- Two-Stage Retrieval & Cross-Encoder Re-Ranking
- Decoupled Prompt Management (YAML + Jinja2 Templates)
- Frontend Grounding Cards UI

## Related Section

Section 1 — Retrieval Quality & Context Engineering

## Related Lessons

- 001 RAG Data Ingestion Pipeline
- 002 Pydantic and structured outputs
- 003 Chunking strategies and Contextual embeddings
- 004 Context Engineering and prompt management
- 005 Re-Ranking and Hybrid Retrieval for better relevance

## Important Resources

- [007 Hands-on Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%201%20–%20Retrieval%20Quality%20&%20Context%20Engineering/007%20Hands-on%20Section.html)
- [Sprint-1-info-review.pdf](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint-1-info-review.pdf)
- [020 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/020%20JAN%2020%20Sprint%20Review%20Retrieval%20Quality%20&%20Context%20Engineering.mp4)
- [022-027 Hands-on Videos 1-6](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)

## Solution

Official solution walkthroughs, reference notebooks, and production code files are detailed in [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Context-Engineering-Hybrid-Search-Reranking/solution.md).

