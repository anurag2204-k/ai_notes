# Assignment 2 — Context Engineering, Hybrid Search & Re-Ranking — Requirements & Specification

### Objectives
Overcome naive vector search limitations by combining lexical precision, cross-encoder re-ranking, and deterministic Pydantic output schemas.

### Requirements & Constraints
1. **Structured Outputs**: Use Pydantic and Instructor to enforce response structure:
   - `answer: str`
   - `references: List[RAGUsedContext]` where each reference includes `id`, `title`, and `reason`.
2. **Hybrid Search**: Configure Qdrant collection `Amazon-items-collection-01-hybrid-search` with:
   - Dense vector: `text-embedding-3-small` (1536 dims).
   - Sparse vector: BM25 / token frequencies.
3. **Re-Ranking**: Apply a cross-encoder model to re-score candidate items, selecting top-k most relevant chunks.
4. **Prompt Registry**: Move hardcoded prompt text to `prompts/retrieval_generation.yaml` and load via Jinja2 template renderer.
5. **UI Grounding**: Render product images, prices, and descriptions in the Streamlit frontend.

### Expected Deliverables
- Working notebooks: `01-Structured-Outputs-Intro.ipynb`, `03-Hybrid-Search.ipynb`, `04-Reranking.ipynb`, `05-Prompt-Management.ipynb`.
- Prompt configuration file: `prompts/retrieval_generation.yaml`.
- Updated backend API returning validated Pydantic JSON objects.
