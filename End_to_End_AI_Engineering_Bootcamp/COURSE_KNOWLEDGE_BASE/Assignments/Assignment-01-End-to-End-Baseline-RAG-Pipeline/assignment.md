# Assignment 1 — Baseline RAG Pipeline & Observability Foundations — Requirements & Specification

### Objectives
Construct a functioning end-to-end baseline RAG application grounded on real-world e-commerce data with quantitative evaluation.

### Requirements & Constraints
1. **Dataset**: Use Amazon Electronics Category (items observed in 2022+). Clean title, features, descriptions, and extract parent ASINs.
2. **Vector Database**: Run Qdrant on `localhost:6333`. Create collection `Amazon-items-collection-01` with vector size 1536 and distance `Cosine`.
3. **Retrieval**: Implement top-k dense vector search (`top_k=5`).
4. **Generation**: Prompt GPT-4o-mini to answer user shopping queries strictly using retrieved product items.
5. **Full-Stack Connection**:
   - Backend: FastAPI route accepting `query` and returning answer string with item metadata.
   - Frontend: Streamlit conversational interface displaying chat history.
6. **Observability**: Ensure all requests appear in LangSmith with input prompt, retrieved context, output, latency, and token metrics.
7. **Evaluation**: Generate at least 20 synthetic Q&A evaluation pairs and calculate RAGAS Faithfulness and Answer Relevance.

### Expected Deliverables
- Complete preprocessing script: `notebooks/week_1/02-RAG-preprocessing-items.ipynb`.
- Baseline RAG notebook: `notebooks/week_1/03-RAG-pipeline.ipynb`.
- RAGAS evaluation notebook: `notebooks/week_1/05-RAG-Evals.ipynb`.
- Functional FastAPI endpoint and Streamlit UI.
