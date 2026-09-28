# Understanding the AI Product Lifecycle and Problem Framing

Type: Technical Lecture & Architecture Guide

## What it teaches

This lesson teaches the systemic engineering lifecycle required to build production AI applications. It contrasts exploratory research prototypes with commercial systems that require deterministic performance, cost bounds, and evaluation gates. It details how to frame business problems into technical AI objectives and establish baseline operational KPIs.

## Key concepts

- AI Product Lifecycle: Problem framing, data curation, offline evaluation, prototyping, production hardening, online monitoring
- Technical vs. Business Metrics: Linking latency and hallucination rates directly to business churn and compute budgets
- Feasibility Assessment: Deciding when an LLM is appropriate versus classical rule-based or machine learning solutions
- Iterative Feedback Loops: Using production logs to guide data collection and prompt improvements

## Important takeaways

- Most AI projects fail at the problem-framing stage, not during prompt engineering.
- Always establish clear evaluation benchmarks before writing any application code.
- Production AI requires treating models as stochastic components within deterministic software harnesses.
- Observability and tracing must be planned during architecture scoping, not patched after deployment.

## Connection to section

- Serves as the foundation for the entire course and capstone project.
- Dictates how student assignments are framed, built, and evaluated in later sprints.

