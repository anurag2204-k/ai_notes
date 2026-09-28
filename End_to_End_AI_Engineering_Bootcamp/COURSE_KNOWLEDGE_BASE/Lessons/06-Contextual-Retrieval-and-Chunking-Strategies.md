# Chunking Strategies and Anthropic Contextual Retrieval

Type: Technical Reading & Architecture Guide

## What it teaches

This lesson explores advanced document chunking strategies and Anthropic's landmark Contextual Retrieval technique. It examines how document fragmentation destroys semantic context and demonstrates how prepending document-level context to chunks dramatically boosts retrieval accuracy.

## Key concepts

- Chunking Strategies: Fixed-size chunking, recursive character splitting, document structure-aware splitting, and semantic boundary chunking
- Context Loss Problem: Isolated chunks losing their global referents (e.g., 'the company' instead of 'Apple Inc.')
- Contextual Retrieval: Using a fast LLM to generate 50-100 tokens of document-level context prepended to every chunk before embedding
- Late Chunking: Generating full-document token representations before chunk-pooling to preserve global bidirectional attention

## Important takeaways

- Poor chunking strategy limits downstream retrieval quality more than vector database choice.
- Contextual Retrieval reduces failed retrievals by up to 49% by preserving document context in high-dimensional space.
- Document headers, breadcrumbs, and structural hierarchy should always be preserved in chunk metadata.
- Semantic chunking balances chunk size by splitting text on natural topic transitions rather than arbitrary character counts.

## Connection to section

- Upgrades Sprint 0's naive chunking pipeline into a production-grade ingestion engine in Sprint 1.
- Directly enhances retrieval precision for the e-commerce product catalog.

