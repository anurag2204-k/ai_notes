# Capstone Project: Detailed Requirements & Rubric

## Project Structure & 3-Iteration Framework

### Step 1: Problem Scoping (The "Problem-First" Foundation)
- **Problem Statement:** What exact business pain point does this system address? Why have traditional deterministic software systems failed or underperformed?
- **Target Audience & Users:** Who interacts with the system? (Internal domain experts vs end consumers).
- **Data Landscape:** What datasets, schemas, APIs, and document types are involved?
- **Constraints & Risks:** Latency ceilings, privacy/compliance concerns (PII, HIPAA, GDPR), and hallucination risk tolerance.

### Step 2: The Three Iterations

#### Iteration 1: The Baseline
- Simple, high-precision architecture (e.g., structured prompt template + deterministic rules).
- Cost: Low. Latency: Minimal (<2s).
- Why start here? Validates user demand and establishes evaluation benchmarks without complex agent failure modes.

#### Iteration 2: Knowledge Augmentation (Enterprise RAG & Routing)
- Incorporates domain knowledge via hybrid search (Vector + BM25) and reranking.
- Introduces deterministic routing (e.g., query classification into specialized sub-pipelines).
- Evaluation: Measures retrieval context precision and groundedness.

#### Iteration 3: Autonomous Agentic System
- Replaces rigid branches with autonomous planning agents, tool invocation via MCP, and self-correction loops.
- Incorporates multi-agent delegation (e.g., Orchestrator-Worker or Supervisor-Subagent topologies).
- Human-in-the-loop checkpoints for critical actions.

### Step 3: Evaluation & Operational Metrics
- **Quality Metrics:** Faithfulness, Answer Relevance, Hallucination Rate, Tool Execution Accuracy.
- **Operational Metrics:** Cost per 1,000 queries, P50/P95 latency breakdown, token budget management.
