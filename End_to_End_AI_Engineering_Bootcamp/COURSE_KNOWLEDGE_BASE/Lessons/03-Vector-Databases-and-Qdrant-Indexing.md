# Vector Databases and Qdrant Collection Indexing

Type: Technical Tutorial & Implementation Guide

## What it teaches

This lesson teaches vector representation theory, high-dimensional indexing algorithms, and vector database management with Qdrant. It covers distance metrics, HNSW graph structures, and payload filtering. It details the practical engineering required to batch-embed and index large-scale catalog datasets.

## Key concepts

- Vector Embeddings: Dense mathematical representations of semantic meaning in high-dimensional vector spaces (e.g. 1536 dims)
- Distance Metrics: Cosine similarity vs. Dot product vs. Euclidean distance and their normalization constraints
- HNSW (Hierarchical Navigable Small World): Graph-based approximate nearest neighbor (ANN) search algorithm balancing speed and recall
- Qdrant Payload Architecture: Storing metadata (ASIN, title, price, category) directly alongside vector points for pre-filtering

## Important takeaways

- Cosine similarity requires normalized vectors; when using OpenAI embeddings, dot product on normalized vectors is mathematically identical and computationally faster.
- Payload design is critical: storing display metadata inside Qdrant eliminates redundant secondary database queries during inference.
- HNSW indexing parameters (m and ef_construct) control the speed-accuracy tradeoff during search.
- Filtering before retrieval (pre-filtering) prevents searching through irrelevant categories or out-of-stock items.

## Connection to section

- Directly underpins the Amazon Electronics catalog search engine in Sprint 0.
- Forms the vector storage infrastructure upgraded to hybrid search in Sprint 1.

