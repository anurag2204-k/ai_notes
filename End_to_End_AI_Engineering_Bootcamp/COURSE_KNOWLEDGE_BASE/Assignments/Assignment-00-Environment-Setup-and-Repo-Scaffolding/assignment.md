# Assignment 0 — Development Environment Setup & Project Scaffolding — Requirements & Specification

### Objectives
Establish a reproducible local development environment supporting fast dependency resolution, multi-service container orchestration, and isolated API credentials.

### Requirements & Constraints
1. **Python Version**: Must use Python >= 3.11 managed via `uv`.
2. **Container Infrastructure**: Docker Engine with Docker Compose v2 support.
3. **Environment Secrets**: Create `.env` from `env.example` containing:
   - `OPENAI_API_KEY`: Valid key for embedding and LLM inference.
   - `LANGSMITH_API_KEY`: Valid key for tracing.
   - `LANGSMITH_TRACING=true`: Enabled for automatic run capture.
   - `LANGSMITH_PROJECT=ai-engineering-bootcamp`.
4. **Workspace Scaffolding**: Verify the directory layout containing:
   - `apps/api/`: FastAPI backend service.
   - `apps/chatbot_ui/`: Streamlit frontend service.
   - `notebooks/`: Sprint experimentation notebooks.

### Deliverables
- Fully resolved `uv.lock` file.
- Functional Docker container runtime.
- Verified test script checking LLM API connectivity via `notebooks/prerequisites/01-llm-apis.ipynb`.
