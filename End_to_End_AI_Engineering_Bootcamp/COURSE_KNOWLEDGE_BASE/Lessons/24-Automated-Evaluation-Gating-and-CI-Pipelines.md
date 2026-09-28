# Automated Evaluation Gating and CI/CD Pipelines for AI

Type: MLOps & CI/CD Guide

## What it teaches

This lesson teaches how to construct automated Continuous Integration (CI) evaluation gates for AI software repositories. It demonstrates how to run headless regression tests against golden evaluation datasets on GitHub pull requests, blocking deployments if retrieval recall or generation faithfulness falls below established thresholds.

## Key concepts

- Continuous Evaluation (CI for AI): Treating evaluation datasets and metrics as automated software test suites
- Retriever Precision/Recall Gates: Running automated scripts (`eval_retriever.py`) to verify vector retrieval accuracy on code commits
- Evaluation Thresholds: Setting hard pass/fail criteria (e.g., minimum 85% Hit Rate@5, minimum 90% Faithfulness score)
- Automated GitHub Actions: Triggering headless Dockerized evaluation runs prior to merging code or deploying images

## Important takeaways

- Prompt and code changes must never be merged based on manual gut feeling; quantitative CI gates are mandatory.
- Headless evaluation scripts should evaluate both retrieval (Hit Rate, MRR) and generation (Faithfulness, Relevance).
- Evaluation datasets must be versioned alongside codebase commits in the repository.
- Automated CI testing catches regressions caused by subtle prompt tweaks or embedding model upgrades before users are impacted.

## Connection to section

- Final engineering discipline taught in Sprint 5.
- Validates the completed capstone codebase prior to cohort Demo Day.

