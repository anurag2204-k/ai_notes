# Assignment 1 — Baseline RAG Pipeline & Observability Foundations

## What is this assignment?

Build an end-to-end baseline RAG prototype on the Amazon Electronics catalog dataset. Spin up Qdrant in Docker, ingest and vectorize product items, implement baseline semantic retrieval and prompt synthesis, expose an API endpoint in FastAPI, render results in Streamlit, instrument LangSmith tracing, and benchmark with RAGAS.

## What you need to do

- Download and preprocess the Amazon Electronics catalog dataset (filtering items observed from 2022 onwards).
- Launch Qdrant vector database via Docker Compose and configure the `Amazon-items-collection-01` collection with Cosine similarity.
- Batch-generate dense vector embeddings using OpenAI `text-embedding-3-small` and upload points with rich payloads (ASIN, title, price, image).
- Implement a baseline RAG query function with grounding system prompts.
- Connect the RAG pipeline to a FastAPI backend endpoint and serve a Streamlit frontend chat UI.
- Instrument LangSmith tracing across the backend to capture full run execution trees.
- Synthesize an evaluation dataset from Qdrant payloads and execute automated RAGAS evaluation runs.

## Concepts practiced

- Dataset Cleaning & Filtering (Amazon Reviews 2023)
- Vector Embeddings & Qdrant Collection Management
- Baseline RAG Prompt Grounding
- FastAPI Backend & Streamlit Frontend Architecture
- Distributed Tracing with LangSmith
- Automated Evaluation with RAGAS (Faithfulness, Relevance)

## Related Section

Section 0 — Problem Framing, Infrastructure Setup & RAG Foundations

## Related Lessons

- 003 What is RAG
- 004 Embedding models & vector DB integration
- 005 Implementing basic observability foundations
- 006 Evaluating basic end-to-end retrieval and generation

## Important Resources

- [007 Hands-On Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%200%20–%20Problem%20Framing,%20Infrastructure%20Setup%20&%20RAG%20Foundations/007%20Hands-On%20Section.html)
- [010 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/010%20Sprint%20Review%20Project%20framing,%20tooling%20overview,%20and%20repo%20setup.mp4)
- [013-019 Hands-on Videos 1-7](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)

## Solution

Official solution walkthroughs, reference notebooks, and production code files are detailed in [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-End-to-End-Baseline-RAG-Pipeline/solution.md).

