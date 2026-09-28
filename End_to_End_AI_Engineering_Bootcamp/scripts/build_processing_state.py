import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

KB_BASE = r"c:\Users\anurag\Desktop\notes\End_to_End_AI_Engineering_Bootcamp\COURSE_KNOWLEDGE_BASE"
AGENT_DIR = os.path.join(KB_BASE, ".agent")
os.makedirs(AGENT_DIR, exist_ok=True)

# Build processing_state.json
processing_state = {
    "course_title": "End-to-End AI Engineering Bootcamp",
    "instructor": "Aurimas Griciunas",
    "cohort": "Cohort 4 (Jan - Mar 2026)",
    "architecture_focus": "Production Agentic AI, RAG Systems, Multi-Agent Orchestration, MCP, Observability, Deployment",
    "sections": {
        "Section-00": {
            "name": "Sprint 0 - Problem Framing, Infrastructure Setup & RAG Foundations",
            "source_dir": "code/Sprint 0 – Problem Framing, Infrastructure Setup & RAG Foundations",
            "status": "DONE",
            "summary_path": "Sections/Section-00-Problem-Framing-Infrastructure-Setup-RAG-Foundations/SUMMARY.md",
            "resources_path": "Sections/Section-00-Problem-Framing-Infrastructure-Setup-RAG-Foundations/resources.md",
            "slides": "code/Sprint-0-info-review.pdf",
            "notebooks": [
                "ai-engineering-bootcamp-cohort-4-main/notebooks/prerequisites/01-llm-apis.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_1/01-explore-amazon-dataset.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_1/02-RAG-preprocessing-items.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_1/03-RAG-pipeline.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_1/04-RAG-Eval-dataset.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_1/05-RAG-Evals.ipynb"
            ],
            "videos": [
                "010 Sprint Review Project framing, tooling overview, and repo setup.mp4",
                "011 Sprint Build Lab Set up development environment and scaffold project repo.mp4",
                "012 Jan 16 Office Hours.mp4",
                "013 Video 1 (Notebook).mp4",
                "014 Video 2 (Notebook).mp4",
                "015 Video 3 (Backend).mp4",
                "016 Video 4 (Frontend).mp4",
                "017 Video 5 (Notebook + Backend).mp4",
                "018 Video 6 (Notebook).mp4",
                "019 Video 7 (Notebook + Backend).mp4"
            ],
            "assignments": [
                "Assignments/Assignment-00-Environment-Setup-and-Repo-Scaffolding",
                "Assignments/Assignment-01-End-to-End-Baseline-RAG-Pipeline"
            ]
        },
        "Section-01": {
            "name": "Sprint 1 - Retrieval Quality & Context Engineering",
            "source_dir": "code/Sprint 1 – Retrieval Quality & Context Engineering",
            "status": "DONE",
            "summary_path": "Sections/Section-01-Retrieval-Quality-Context-Engineering/SUMMARY.md",
            "resources_path": "Sections/Section-01-Retrieval-Quality-Context-Engineering/resources.md",
            "slides": "code/Sprint-1-info-review.pdf",
            "notebooks": [
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_2/01-Structured-Outputs-Intro.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_2/02-Structured-Outputs-RAG-Pipeline.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_2/03-Hybrid-Search.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_2/04-Reranking.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_2/05-Prompt-Management.ipynb"
            ],
            "videos": [
                "020 JAN 20 Sprint Review Retrieval Quality & Context Engineering.mp4",
                "021 Sprint Build Lab Improve context retrieval, prompts, and system robustness.mp4",
                "022 Video 1 (Notebook).mp4",
                "023 Video 2 (Notebook).mp4",
                "024 Video 3 (Notebook).mp4",
                "025 Video 4 (Notebook).mp4",
                "026 Video 5 (Notebook).mp4",
                "027 Video 6 (Backend).mp4"
            ],
            "assignments": [
                "Assignments/Assignment-02-Context-Engineering-Hybrid-Search-Reranking"
            ]
        },
        "Section-02": {
            "name": "Sprint 2 - Agents & Agentic Systems",
            "source_dir": "code/Sprint 2 – Agents & Agentic Systems",
            "status": "DONE",
            "summary_path": "Sections/Section-02-Agents-and-Agentic-Systems/SUMMARY.md",
            "resources_path": "Sections/Section-02-Agents-and-Agentic-Systems/resources.md",
            "slides": "code/Sprint-2-info-review.pdf",
            "notebooks": [
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/01-LangGraph-Intro.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/02-Query-Rewriting.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/03-Router.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/04-Agent-Single-Turn.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/05-LangGraph-LangChain.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_3/06-Tool-Calling.ipynb"
            ],
            "videos": [
                "028 JAN 27 Sprint Review Autonomous Agents.mp4",
                "029 Jan 29 Sprint Build Lab Agentic Systems.mp4",
                "030 JAN 30 Office Hours.mp4",
                "031 Video 1 (Notebook).mp4",
                "032 Video 2 (Backend).mp4",
                "033 Video 3 (NotebookBackend).mp4",
                "034 Video 4 (NotebookBackend).mp4",
                "035 Video 5 (NotebookBackend).mp4",
                "036 Video 6 (NotebookBackend).mp4"
            ],
            "assignments": [
                "Assignments/Assignment-03-Autonomous-Agent-LangGraph-Tool-Calling"
            ]
        },
        "Section-03": {
            "name": "Sprint 3 - Moving From Basic To Agentic RAG",
            "source_dir": "code/Sprint 3 – Moving From Basic To Agentic RAG",
            "status": "DONE",
            "summary_path": "Sections/Section-03-Moving-From-Basic-To-Agentic-RAG/SUMMARY.md",
            "resources_path": "Sections/Section-03-Moving-From-Basic-To-Agentic-RAG/resources.md",
            "slides": "code/Sprint-3-info-review.pdf",
            "notebooks": [
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_4/01-Multi-Turn-Agent.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_4/02-Multiple-Tools.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_4/03-Human-Feedback.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_4/04-MCP.ipynb",
                "ai-engineering-bootcamp-cohort-4-main/notebooks/week_4/05-State-Streaming.ipynb"
            ],
            "videos": [
                "037 FEB 03 Sprint Review Moving from basic to agentic RAG.mp4",
                "038 FEB 05 Sprint Build Lab Build a tool-using agent integrated with your RAG backend.mp4",
                "039 FEB 10 Office Hours.mp4",
                "040 FEB 12 Office Hours.mp4",
                "041 Video 1 (Notebook).mp4",
                "042 Video 2 (Notebook).mp4",
                "043 Video 3 (Backend).mp4",
                "044 Video 4 (Backend).mp4",
                "045 Video 5 (Notebook).mp4",
                "046 Video 6 (Notebook).mp4",
                "047 Video 7 (Notebook).mp4",
                "048 Video 8 (Backend).mp4"
            ],
            "assignments": [
                "Assignments/Assignment-04-Agentic-RAG-MCP-Human-in-the-Loop"
            ]
        },
        "Section-04": {
            "name": "Sprint 4 - Multi-Agent Systems",
            "source_dir": "code/Sprint 4 – Multi-Agent Systems",
            "status": "DONE",
            "summary_path": "Sections/Section-04-Multi-Agent-Systems/SUMMARY.md",
            "resources_path": "Sections/Section-04-Multi-Agent-Systems/resources.md",
            "slides": "code/Sprint-4-info-review.pdf",
            "notebooks": [
                "ai-engineering-bootcamp-cohort-4-main/apps/api/src/api/agents/graph.py",
                "ai-engineering-bootcamp-cohort-4-main/apps/api/src/api/agents/agents.py"
            ],
            "videos": [
                "049 FEB 17 Sprint Review Designing and orchestrating multi-agent systems.mp4",
                "050 FEB 19 Sprint Build Lab Implement a multi-agent task flow and run coordination scenarios.mp4",
                "051 Video 1 (Notebook).mp4",
                "052 Video 2 (Backend).mp4",
                "053 Video 3 (Notebook).mp4",
                "054 Video 4 (Backend).mp4",
                "055 Video 5 (Notebook + Backend).mp4",
                "056 Video 6 (Notebook).mp4",
                "057 Video 7 (Notebook).mp4",
                "058 Video 8 (Notebook + Backend).mp4"
            ],
            "assignments": [
                "Assignments/Assignment-05-Multi-Agent-System-Coordination"
            ]
        },
        "Section-05": {
            "name": "Sprint 5 - Deployment, Optimization and Reliability",
            "source_dir": "code/Sprint 5 – Deployment, Optimization and Reliability",
            "status": "DONE",
            "summary_path": "Sections/Section-05-Deployment-Optimization-Reliability/SUMMARY.md",
            "resources_path": "Sections/Section-05-Deployment-Optimization-Reliability/resources.md",
            "slides": "code/Sprint-4-info-review.pdf & Course Architecture Docs",
            "notebooks": [
                "ai-engineering-bootcamp-cohort-4-main/docker-compose.yml",
                "ai-engineering-bootcamp-cohort-4-main/apps/api/Dockerfile",
                "ai-engineering-bootcamp-cohort-4-main/apps/chatbot_ui/Dockerfile"
            ],
            "videos": [
                "059 FEB 24 Sprint Review Best practices for cloud deployment, monitoring and performance tuning.mp4",
                "060 FEB 26 Sprint Build Lab Containerise your capstone and implement CI Pipeline.mp4",
                "061 FEB 27 Office Hours.mp4",
                "062 Video 1 (Notebook).mp4",
                "063 Video 2 (Backend).mp4",
                "064 Video 3 (Backend + Frontend).mp4",
                "065 Video 4 (Notebook).mp4",
                "066 Video 5 (Notebook + Backend).mp4",
                "067 Video 6 (Backend + CI).mp4",
                "068 Video 6 (Notebooks + Cloud).mp4",
                "069 MAR 3 Sprint Review Best practices for cloud deployment, monitoring, and performance tuning (Part 2).mp4",
                "070 MAR 5 Case studies of real world Agentic AI Systems.mp4",
                "071 MAR 10 Demo Day Present your working AI product to cohort.mp4",
                "072 MAR 12 Closing Celebration & Feedback.mp4"
            ],
            "assignments": [
                "Assignments/Assignment-06-Deployment-Optimization-Fallbacks"
            ],
            "capstone_project": "Projects/Capstone-Production-Agentic-AI-Product"
        }
    }
}

with open(os.path.join(AGENT_DIR, "processing_state.json"), "w", encoding="utf-8") as f:
    json.dump(processing_state, f, indent=2)

print("Saved .agent/processing_state.json")
