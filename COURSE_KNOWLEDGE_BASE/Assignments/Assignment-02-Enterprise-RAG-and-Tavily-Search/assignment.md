# Assignment 2: Detailed Specifications & Requirements

## Architecture: Corrective RAG (CRAG) in LangGraph

```
                 [User Query]
                      │
                      ▼
               [Retrieve Docs]
                      │
                      ▼
             [Grade Relevance]
             /               \
   (Relevant)                 (Not Relevant / Incomplete)
         │                               │
         ▼                               ▼
 [Generate Answer]              [Rewrite / Web Search]
         │                               │
         │                               ▼
         │                       [Generate Answer]
         ▼                               ▼
   [Final Answer Grounded with Citations & Sources]
```

---

## Detailed Task Requirements

### 1. Ingestion Pipeline
- Download the annual performance report PDFs (2019-2022) from the course assets folder.
- Use `PyPDFLoader` or `PDFPlumber` to parse raw text and preserve tabular structures.
- Chunk text using `RecursiveCharacterTextSplitter` with `chunk_size=1000` and `chunk_overlap=200`.
- Generate embeddings using OpenAI `text-embedding-3-small` and index into `Chroma` or `InMemoryVectorStore`.

### 2. Tavily Search Tool
- Configure `TavilySearchResults(max_results=3)`.
- Extract raw content and URL references for attribution.

### 3. LangGraph StateGraph Construction
Define a typed state dictionary:
```python
from typing import TypedDict, List

class AgentState(TypedDict):
    question: str
    generation: str
    web_search: bool
    documents: List[str]
```
- **Node 1 (`retrieve`):** Fetches top-k relevant document chunks from the vector store.
- **Node 2 (`grade_documents`):** Prompts an LLM evaluator to score each document chunk as `yes` or `no` for semantic relevance to the question.
- **Conditional Edge (`decide_to_generate`):**
  - If any document is evaluated as relevant, continue to generation.
  - If all documents are irrelevant, set `web_search=True` and route to `web_search` node.
- **Node 3 (`web_search`):** Rewrites query for web search and queries Tavily.
- **Node 4 (`generate`):** Generates concise final answer strictly referencing the retrieved context.

---

## Evaluation Benchmark & Test Cases

1. **Internal Knowledge Test:**
   - *Query:* *"What were the primary strategic achievements reported in the 2021 annual performance report?"*
   - *Expected Behavior:* Grades documents as relevant; answers purely from PDF vector store; skips Tavily web search.
2. **External Knowledge Test:**
   - *Query:* *"What were the major tech stock market movements yesterday?"*
   - *Expected Behavior:* Grades internal PDFs as irrelevant; triggers Tavily search; generates up-to-date response with live citations.
3. **Ambiguous / Multi-Hop Test:**
   - *Query:* *"How did our 2020 revenue compare to Microsoft's 2024 earnings?"*
   - *Expected Behavior:* Retrieves internal 2020 PDF data, flags missing 2024 Microsoft data, invokes Tavily web search, and synthesizes a comparative table.
