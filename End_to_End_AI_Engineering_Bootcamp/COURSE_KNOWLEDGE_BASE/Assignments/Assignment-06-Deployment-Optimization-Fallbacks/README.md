# Assignment 6 — Cloud Deployment, Optimization & Reliability Engineering

## What is this assignment?

Harden, optimize, and containerize the entire multi-agent application for enterprise production. Implement LiteLLM Router model fallback cascades, optimize prompt templates for provider KV prompt caching, refactor warehouse agents into Google ADK services, connect remote A2A servers, and implement automated CI evaluation regression gates.

## What you need to do

- Implement LiteLLM Router in FastAPI backend to establish automated fallback cascades (e.g. GPT-4o → Claude-3-5-Sonnet → Gemini-1.5-Pro).
- Audit prompt templates to ensure static system instructions and tool schemas maximize provider prompt cache hit rates.
- Reimplement warehouse management agent using Google Agent Development Kit (ADK) and verify via ADK Web Server.
- Implement a remote A2A server using `a2a-sdk` and connect LangGraph graph over network sockets.
- Configure multi-stage Dockerfiles and `docker-compose.yml` to orchestrate 6 services with persistent storage volumes.
- Build an automated evaluation CI gate script (`eval_retriever.py`) that tests retrieval recall and blocks failing builds.

## Concepts practiced

- Model Fallback Routing (LiteLLM Router)
- Prompt Caching Economics & Prefix Alignment
- Google Agent Development Kit (ADK) & ADK Web Server
- Remote Agent-to-Agent (A2A) Client/Server (`a2a-sdk`)
- Production Multi-Container Docker Orchestration
- Automated CI Evaluation Regression Gates

## Related Section

Section 5 — Deployment, Optimization and Reliability

## Related Lessons

- 01 Deployment architecture patterns for AI Systems
- 02 Managing latency and cost for AI applications
- 03 Securing AI systems
- 04 CI CD for AI applications

## Important Resources

- [05 Hands-on Section.html](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/code/Sprint%205%20–%20Deployment,%20Optimization%20and%20Reliability/05%20Hands-on%20Section.html)
- [docker-compose.yml](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/docker-compose.yml)
- [eval_retriever.py](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/scratch/repo/ai-engineering-bootcamp-cohort-4-main/apps/api/evals/eval_retriever.py)
- [059 Sprint Review Video](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/059%20FEB%2024%20Sprint%20Review%20Best%20practices%20for%20cloud%20deployment,%20monitoring%20and%20performance%20tuning.mp4)
- [062-068 Hands-on Videos 1-6](file:///C:/Users/anurag/Desktop/End-to-End%20AI%20Engineering%20Bootcamp/)

## Solution

Official solution walkthroughs, reference notebooks, and production code files are detailed in [solution.md](file:///c:/Users/anurag/Desktop/notes/End_to_End_AI_Engineering_Bootcamp/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-06-Deployment-Optimization-Fallbacks/solution.md).

