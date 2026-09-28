# Pydantic and Structured Outputs with Instructor

Type: Code Tutorial & Best Practice

## What it teaches

This lesson teaches how to force LLMs to generate strictly validated, deterministic JSON structures matching Pydantic models. It explains how Instructor leverages function calling and JSON schema modes to validate outputs and automatically retry when validation rules fail.

## Key concepts

- Structured Output Enforcement: Constraining LLM token sampling to valid JSON conforming to an explicit JSON schema
- Instructor Library: Python wrapper around LLM APIs providing automatic validation, Pydantic coercion, and retry loops
- Self-Correction Retries: Feeding validation error tracebacks back into the model to prompt autonomous schema repair
- Typed Schema Engineering: Defining nested models, optional fields, enums, and field descriptions to guide generation

## Important takeaways

- Unstructured text outputs are unacceptable in production software architectures.
- Instructor eliminates regex parsing hacks and JSON decode exceptions by validating responses at the API boundary.
- Validation errors provide rich, immediate feedback that enables the LLM to correct its own output in a single retry.
- Detailed Field descriptions in Pydantic models act as micro-prompts that significantly improve data extraction accuracy.

## Connection to section

- Introduced in Sprint 1 to structure RAG answers and item recommendation cards.
- Directly enables agent tool argument generation and intent classification in Sprint 2 and 3.

