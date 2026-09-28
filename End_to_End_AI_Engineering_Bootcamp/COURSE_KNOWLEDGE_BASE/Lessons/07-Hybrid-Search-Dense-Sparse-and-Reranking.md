# Hybrid Search (Dense + Sparse) and Cross-Encoder Re-Ranking

Type: Architecture & Implementation Guide

## What it teaches

This lesson teaches how to combine dense semantic embeddings with sparse lexical search (BM25) and apply cross-encoder re-ranking. It explains why dense retrieval fails on exact SKU and keyword queries and demonstrates how two-stage retrieval delivers state-of-the-art search relevance.

## Key concepts

- Dense Retrieval: Bi-encoder semantic vector search capturing conceptual meaning and synonyms
- Sparse Retrieval: BM25 / TF-IDF lexical frequency search capturing exact keyword, SKU, and acronym matches
- Hybrid Fusion: Combining dense and sparse score lists using Reciprocal Rank Fusion (RRF) or relative score fusion in Qdrant
- Cross-Encoder Re-Ranking: Applying joint attention across query and document pairs to compute definitive relevance scores

## Important takeaways

- Dense search alone is insufficient for enterprise search; hybrid search is the mandatory baseline.
- Two-stage retrieval balances latency and accuracy: retrieve 25 candidates via fast hybrid search, then re-rank top 5 with cross-encoder.
- Bi-encoders compute vector representations independently; cross-encoders compute all-to-all cross-attention between query and passage.
- Qdrant natively supports dual dense and sparse vector indexing within the same collection.

## Connection to section

- Core technical upgrade implemented in Sprint 1.
- Serves as the high-accuracy retrieval tool passed to autonomous agents in Sprint 2.

