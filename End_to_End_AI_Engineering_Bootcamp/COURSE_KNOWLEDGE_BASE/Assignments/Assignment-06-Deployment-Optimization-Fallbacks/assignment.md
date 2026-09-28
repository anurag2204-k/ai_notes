# Assignment 6 — Cloud Deployment, Optimization & Reliability Engineering — Requirements & Specification

### Objectives
Package the complete system into a resilient, cost-optimized, containerized product protected by automated evaluation gates.

### Requirements & Constraints
1. **Fallback Routing**: Backend must use LiteLLM Router to automatically recover from primary model API rate limits (HTTP 429) or timeouts.
2. **Prompt Caching**: All system prompts must place static instructions first and dynamic user variables at the very end.
3. **Remote A2A**: Implement a remote server with `a2a-sdk` and connect from LangGraph.
4. **Automated CI Evals**: Script `apps/api/evals/eval_retriever.py` must run headless against Qdrant, computing Hit Rate@5 and MRR, exiting with code 1 if Hit Rate < 85%.
5. **Docker Compose**: Entire stack must launch cleanly with a single command: `docker compose up -d`.

### Expected Deliverables
- Multi-stage Dockerfiles (`apps/api/Dockerfile`, `apps/chatbot_ui/Dockerfile`).
- Master `docker-compose.yml` coordinating 6 services.
- Headless retriever evaluation script: `apps/api/evals/eval_retriever.py`.
