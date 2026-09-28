# Section 1 — Retrieval Quality & Context Engineering

## What This Section Is About

This section focuses on elevating raw retrieval accuracy and output reliability to enterprise production standards. Naive RAG systems routinely suffer from semantic drift, missing keyword precision, and unstructured, unpredictable LLM outputs. In this sprint, Aurimas Griciunas guides engineers through advanced context engineering, hybrid search architectures, re-ranking models, structured outputs, and prompt management.

Practitioners transition from plain text responses to deterministic Pydantic schemas using the Instructor library. This ensures that every LLM response strictly conforms to defined JSON models containing citations, product identifiers, and reasoning chains. Furthermore, chunking strategies are thoroughly analyzed—contrasting fixed-size chunking with semantic boundaries, recursive splitting, and Anthropic's Contextual Retrieval technique (prepending chunk-specific context).

To solve the inherent weakness of dense embeddings on specific keywords, SKU numbers, and exact technical terms, students implement Hybrid Retrieval by pairing dense vector search with sparse BM25/lexical indexing directly inside Qdrant. A cross-encoder Re-Ranking stage (using Cohere or sentence-transformers) is added as a secondary filter, dramatically boosting precision@k. Finally, prompts are decoupled from application code into version-controlled Jinja2 templates and YAML configuration registries.

## Main Concepts

- **Structured Outputs with Pydantic & Instructor**: Guaranteeing validated schema compliance and eliminating JSON parse failures
- **Chunking Optimization & Contextual Retrieval**: Recursive chunking, semantic boundaries, and context-prepend strategies
- **Hybrid Retrieval Architecture**: Combining dense semantic embeddings with sparse lexical search (BM25 / TF-IDF) in Qdrant
- **Cross-Encoder Re-Ranking**: Two-stage retrieval where bi-encoders retrieve broad candidates and cross-encoders re-score top-k with joint attention
- **Decoupled Prompt Management**: Version-controlled YAML registries and Jinja2 templates for deterministic prompt rendering
- **Business-Specific Score Boosting**: Applying custom metadata weights (ratings, stock status, freshness) during vector scoring

## Conceptual Flow

```mermaid
graph LR

    s0["Ingestion Pipeline Review"] --> s1["Pydantic & Structured Outputs (Instructor)"]
    s1["Pydantic & Structured Outputs (Instructor)"] --> s2["Chunking Strategies & Contextual Prepending"]
    s2["Chunking Strategies & Contextual Prepending"] --> s3["Hybrid Search (Dense + Sparse Qdrant)"]
    s3["Hybrid Search (Dense + Sparse Qdrant)"] --> s4["Cross-Encoder Re-Ranking (Cohere / Cross-Encoder)"]
    s4["Cross-Encoder Re-Ranking (Cohere / Cross-Encoder)"] --> s5["Prompt Decoupling & Jinja2 Templates"]
    s5["Prompt Decoupling & Jinja2 Templates"] --> s6["Backend & Frontend Integration"]
```

**Progression Sequence**: Ingestion Pipeline Review → Pydantic & Structured Outputs (Instructor) → Chunking Strategies & Contextual Prepending → Hybrid Search (Dense + Sparse Qdrant) → Cross-Encoder Re-Ranking (Cohere / Cross-Encoder) → Prompt Decoupling & Jinja2 Templates → Backend & Frontend Integration

## Important Lessons

### RAG Data Ingestion Pipeline

Details production data ingestion architecture, including document parsing, deduplication, metadata enrichment, and vector database indexing. Demonstrates how poor data ingestion fundamentally limits downstream generation quality regardless of LLM power.

### Pydantic and Structured Outputs

Teaches how to enforce strict JSON schemas on LLM generations using Pydantic models and the Instructor library. Covers schema validation, automatic retry loops on validation errors, and typed field extraction for production APIs.

### Chunking Strategies and Contextual Embeddings

Explores how chunk size and overlap impact semantic preservation and token budgets. Explains Anthropic's Contextual Retrieval technique, where each chunk is prepended with high-level document context prior to embedding generation to preserve contextual meaning.

### Context Engineering and Prompt Management

Focuses on prompt architecture, system instructions, and separating prompt templates from Python business logic. Introduces Jinja2 rendering engines and YAML prompt configuration registries for reproducible experimentation.

### Re-Ranking and Hybrid Retrieval for Better Relevance

Analyzes why bi-encoder vector retrieval struggles with exact keyword matching (SKUs, part numbers) and introduces hybrid search combining dense vectors with sparse BM25 indices. Demonstrates how cross-encoder re-rankers dramatically improve Top-3 relevance.

### (Optional) Automated Prompt Tuning

Surveys programmatic prompt optimization techniques (e.g., DSPy, text-grad, and gradient-free optimization) to systematically maximize evaluation metrics without manual prompt trial-and-error.

## Practical Work

- Configuring Pydantic response models and wrapping OpenAI clients with Instructor for guaranteed schema validation
- Modifying the RAG pipeline to output structured JSON containing product recommendations, reasons, and source ASINs
- Configuring Qdrant for Hybrid Search: creating sparse vectors alongside dense vectors in a single collection
- Integrating a Cross-Encoder Re-Ranking model into the retrieval pipeline to re-score top-20 retrieved candidates down to top-5
- Extracting hardcoded prompts into external YAML configuration files rendered dynamically via Jinja2
- Updating the FastAPI backend to serve structured payloads and updating Streamlit to render product cards with images, prices, and ratings

## Important Takeaways

- Bi-encoders (embedding models) compute independent representations for query and document; cross-encoders compute joint attention across both, providing vastly superior relevance at slightly higher latency.
- Hybrid retrieval (dense + sparse) resolves the 'exact match' blind spot of pure vector search, essential for e-commerce catalog lookups.
- Contextual Retrieval (prepending 50-100 tokens of high-level document summary to each chunk) significantly reduces retrieval failure rates.
- Instructor and Pydantic turn stochastic text models into reliable software components that return strongly-typed objects directly consumed by frontend UIs.
- Prompt templates must be managed like code: decoupled into YAML/Jinja files with strict versioning rather than scattered f-strings across Python modules.
- Two-stage retrieval (retrieve 25 candidates via hybrid search → re-rank top 5 with cross-encoder) delivers the optimal tradeoff between latency and retrieval accuracy.

## Relationship to Previous Sections

Builds directly on Sprint 0's baseline RAG pipeline, Qdrant setup, and LangSmith observability foundations.

## Relationship to Later Sections

Provides the high-precision retrieval tool and structured output mechanisms that Sprint 2 encapsulates into tools for autonomous LangGraph agents.

## What I Should Know After Completing This Section

- [ ] I can define and enforce Pydantic structured output models using Instructor.
- [ ] I understand the difference between bi-encoders and cross-encoders in retrieval pipelines.
- [ ] I can implement hybrid search (dense + sparse) within Qdrant.
- [ ] I can integrate a re-ranking model to refine retrieved candidate contexts.
- [ ] I can manage prompts using external YAML registries and Jinja2 templates.

