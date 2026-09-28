# [101] — Enterprise Playbook: Production RAG Optimizations (HyDE, Re-Ranking, Self-RAG)

Category:
Grow

Type:
Reference Material

Available Formats:
- HTML Lesson Page

Associated Source Files:
- `145 RAG Optimizations For The Enterprise.html`

## What this lesson is about
Technical resource and deep-dive material covering Enterprise Playbook: Production RAG Optimizations (HyDE, Re-Ranking, Self-RAG). It provides specialized enterprise knowledge, architectural best practices, and curated frameworks supporting the curriculum.

## Key Concepts
- Semantic chunking, chunk overlap, and metadata filtering
- Dense vector embeddings vs BM25 sparse keyword search
- Corrective RAG (CRAG) relevance grading and web search fallbacks
- Retrieval evaluation metrics (Context Precision, Context Recall, Faithfulness)

## Important Takeaways
- Focus ruthlessly on the user's business problem rather than forcing agentic autonomy where deterministic code suffices.
- Cleanly decouple state management, tool interfaces, and model prompts to maintain maintainable agent codebases.
- Always instrument production observability (token usage, latency, error boundaries) before deploying to users.

## How it connects to the course
- Fits directly into **Module 10** (Week 4) of the curriculum.
- Builds foundational theory and practical patterns directly implemented in Perplexia AI.

## Important Resources
- **Query Expansion in LangChain:** [https://python.langchain.com/v0.1/docs/use_cases/query_analysis/techniques/expansion/](https://python.langchain.com/v0.1/docs/use_cases/query_analysis/techniques/expansion/)
- **Hypothetical Document Embeddings for Zero-Shot Dense Passage Retrieval:** [https://arxiv.org/abs/2212.10496](https://arxiv.org/abs/2212.10496)
- **https://weaviate.io/blog/hybrid-search-explained:** [https://weaviate.io/blog/hybrid-search-explained](https://weaviate.io/blog/hybrid-search-explained)
- **https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/:** [https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)
- **Corrective Retrieval-Augmented Generation for Reliable Question Answering:** [https://arxiv.org/abs/2310.10716](https://arxiv.org/abs/2310.10716)
- **Fine-tuning LLMs for Multi-Hop Retrieval-Augmented Generation:** [https://arxiv.org/abs/2403.10131](https://arxiv.org/abs/2403.10131)

