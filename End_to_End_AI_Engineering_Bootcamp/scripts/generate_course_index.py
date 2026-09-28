import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

KB_BASE = r"c:\Users\anurag\Desktop\notes\End_to_End_AI_Engineering_Bootcamp\COURSE_KNOWLEDGE_BASE"
ROOT_DIR = r"C:\Users\anurag\Desktop\End-to-End AI Engineering Bootcamp"
CODE_DIR = os.path.join(ROOT_DIR, "code")

with open(r"c:\Users\anurag\Desktop\notes\End_to_End_AI_Engineering_Bootcamp\scripts\course_inventory.json", "r", encoding="utf-8") as f:
    inventory = json.load(f)

lines = []
lines.append("# Master Course Inventory & Index")
lines.append("")
lines.append("> **Course**: End-to-End AI Engineering Bootcamp  ")
lines.append("> **Instructor**: Aurimas Griciunas  ")
lines.append("> **Curriculum Unit**: Sprints 0 through 5 + Capstone System  ")
lines.append("> **Source Directory**: `C:\\Users\\anurag\\Desktop\\End-to-End AI Engineering Bootcamp`  ")
lines.append("")
lines.append("This index inventories every physical and digital artifact across the bootcamp repository, establishing authoritative relationships between HTML course modules, slide decks, video walkthroughs, Jupyter notebooks, and backend production code.")
lines.append("")
lines.append("---")
lines.append("")

# Table header
lines.append("## Course Files & Artifacts Inventory")
lines.append("")
lines.append("| Section | File Name | Type | Identified Lesson / Title | Purpose / Role | Assignment/Project? | Duplicate / Alternate Format | Processed Status |")
lines.append("|---|---|---|---|---|---|---|---|")

# 1. Orientation / Prep files
lines.append("| Prep | `End-to-end AI Engineering bootcamp Prep.pdf` | PDF Slide Deck | Bootcamp Orientation & Roadmap | Architecture overview, schedule, expectations, communication | No | Alternate format to 001 Video | DONE |")
lines.append("| Prep | `Setting up your development environment..html` | HTML Guide | Setting Up Development Environment | Instructions for Docker, UV, Python 3.11+, Git, Ollama/APIs | Assignment Prep | Alternate format to Videos 1-4 | DONE |")
lines.append("| Prep | `Setting up your development environment 1.mp4` | MP4 Video | Dev Env Setup Part 1: UV & Python | Video walkthrough of UV package manager installation | No | Alternate format of Setup HTML | DUPLICATE |")
lines.append("| Prep | `Setting up your development environment 2.mp4` | MP4 Video | Dev Env Setup Part 2: Docker Engine | Video walkthrough of Docker & Docker Compose setup | No | Alternate format of Setup HTML | DUPLICATE |")
lines.append("| Prep | `Setting up your development environment 3.mp4` | MP4 Video | Dev Env Setup Part 3: Git & SSH | Video walkthrough of GitHub repository cloning & SSH keys | No | Alternate format of Setup HTML | DUPLICATE |")
lines.append("| Prep | `Setting up your development environment 4.mp4` | MP4 Video | Dev Env Setup Part 4: API Keys & Env | Video walkthrough of setting .env and OpenAI/Google API keys | No | Alternate format of Setup HTML | DUPLICATE |")
lines.append("| Prep | `001 12 JAN End-to-end AI Engineering bootcamp Prep.mp4` | MP4 Video | Cohort Kickoff & Logistics | Live recording of opening orientation and cohort overview | No | Alternate format to Prep.pdf | DUPLICATE |")

for i in range(1, 9):
    lines.append(f"| Prep | `00{i+1} Hands-On Section {i}.mp4` | MP4 Video | Hands-On Foundations Part {i} | Early setup & environment verification recording | Yes | Walkthrough of baseline setup | DONE |")

# Sprints mapping
sprint_meta = {
    "Sprint 0 – Problem Framing, Infrastructure Setup & RAG Foundations": {
        "sec": "Sprint 0",
        "slides": "Sprint-0-info-review.pdf",
        "review_video": "010 Sprint Review Project framing, tooling overview, and repo setup.mp4",
        "lab_video": "011 Sprint Build Lab Set up development environment and scaffold project repo.mp4",
        "oh_video": "012 Jan 16 Office Hours.mp4",
        "hands_on_videos": [
            ("013 Video 1 (Notebook).mp4", "Dataset Exploration (Amazon Items)"),
            ("014 Video 2 (Notebook).mp4", "Preprocessing & Cleaning Amazon Catalog Data"),
            ("015 Video 3 (Backend).mp4", "Baseline RAG Pipeline Implementation"),
            ("016 Video 4 (Frontend).mp4", "FastAPI Backend & Streamlit Frontend Connection"),
            ("017 Video 5 (Notebook + Backend).mp4", "Observability Setup (LangSmith / OpenTelemetry)"),
            ("018 Video 6 (Notebook).mp4", "Synthetic Evaluation Dataset Generation"),
            ("019 Video 7 (Notebook + Backend).mp4", "RAGAS Evaluation Framework Integration")
        ]
    },
    "Sprint 1 – Retrieval Quality & Context Engineering": {
        "sec": "Sprint 1",
        "slides": "Sprint-1-info-review.pdf",
        "review_video": "020 JAN 20 Sprint Review Retrieval Quality & Context Engineering.mp4",
        "lab_video": "021 Sprint Build Lab Improve context retrieval, prompts, and system robustness.mp4",
        "oh_video": None,
        "hands_on_videos": [
            ("022 Video 1 (Notebook).mp4", "Structured Outputs Intro with Instructor & Pydantic"),
            ("023 Video 2 (Notebook).mp4", "Structured Outputs in RAG Pipeline"),
            ("024 Video 3 (Notebook).mp4", "Backend Migration of Structured Outputs"),
            ("025 Video 4 (Notebook).mp4", "UI Grounding Context & Product Metadata Cards"),
            ("026 Video 5 (Notebook).mp4", "Hybrid Search (Dense + Sparse Qdrant)"),
            ("027 Video 6 (Backend).mp4", "Cohere / Cross-Encoder Re-Ranking & Prompt Configs")
        ]
    },
    "Sprint 2 – Agents & Agentic Systems": {
        "sec": "Sprint 2",
        "slides": "Sprint-2-info-review.pdf",
        "review_video": "028 JAN 27 Sprint Review Autonomous Agents.mp4",
        "lab_video": "029 Jan 29 Sprint Build Lab Agentic Systems.mp4",
        "oh_video": "030 JAN 30 Office Hours.mp4",
        "hands_on_videos": [
            ("031 Video 1 (Notebook).mp4", "LangGraph Building Blocks & StateGraph"),
            ("032 Video 2 (Backend).mp4", "Tool Definition & ReAct Agent Loop"),
            ("033 Video 3 (NotebookBackend).mp4", "Query Expansion & Multi-Query Rewriting Node"),
            ("034 Video 4 (NotebookBackend).mp4", "Intent Router Node for Query Filtering"),
            ("035 Video 5 (NotebookBackend).mp4", "Single-Turn ReAct Agent with Retrieval Tool"),
            ("036 Video 6 (NotebookBackend).mp4", "Backend Migration of LangGraph ReAct Agent")
        ]
    },
    "Sprint 3 – Moving From Basic To Agentic RAG": {
        "sec": "Sprint 3",
        "slides": "Sprint-3-info-review.pdf",
        "review_video": "037 FEB 03 Sprint Review Moving from basic to agentic RAG.mp4",
        "lab_video": "038 FEB 05 Sprint Build Lab Build a tool-using agent integrated with your RAG backend.mp4",
        "oh_video": "039 FEB 10 Office Hours.mp4 / 040 FEB 12 Office Hours.mp4",
        "hands_on_videos": [
            ("041 Video 1 (Notebook).mp4", "LangGraph State Persistence (MemorySaver / Postgres)"),
            ("042 Video 2 (Notebook).mp4", "Multi-Turn Conversation Persistence in FastAPI Backend"),
            ("043 Video 3 (Backend).mp4", "Secondary Qdrant Collection (Amazon Reviews) & Tool"),
            ("044 Video 4 (Backend).mp4", "Human Feedback Collection in UI & LangSmith Trace Link"),
            ("045 Video 5 (Notebook).mp4", "Model Context Protocol (MCP) FastMCP Server Setup"),
            ("046 Video 6 (Notebook).mp4", "Custom MCP Tool Node in LangGraph Graph"),
            ("047 Video 7 (Notebook).mp4", "Graph State Streaming & Server-Sent Events (SSE)"),
            ("048 Video 8 (Backend).mp4", "SSE Backend Streaming to Streamlit Frontend")
        ]
    },
    "Sprint 4 – Multi-Agent Systems": {
        "sec": "Sprint 4",
        "slides": "Sprint-4-info-review.pdf",
        "review_video": "049 FEB 17 Sprint Review Designing and orchestrating multi-agent systems.mp4",
        "lab_video": "050 FEB 19 Sprint Build Lab Implement a multi-agent task flow and run coordination scenarios.mp4",
        "oh_video": None,
        "hands_on_videos": [
            ("051 Video 1 (Notebook).mp4", "PostgreSQL Shopping Cart Schema & Tool Functions"),
            ("052 Video 2 (Backend).mp4", "Shopping Cart Specialized Agent in LangGraph"),
            ("053 Video 3 (Notebook).mp4", "Coordinator Agent Architecture & Plan Execution"),
            ("054 Video 4 (Backend).mp4", "Multi-Agent Graph Integration (Coordinator + Cart + Q&A)"),
            ("055 Video 5 (Notebook + Backend).mp4", "Frontend Live Cart Synchronization via SSE"),
            ("056 Video 6 (Notebook).mp4", "Agent-to-Agent Handoff & Memory State Passing"),
            ("057 Video 7 (Notebook).mp4", "Multi-Agent Error Recovery & Backoff"),
            ("058 Video 8 (Notebook + Backend).mp4", "End-to-End Multi-Agent System Verification")
        ]
    },
    "Sprint 5 – Deployment, Optimization and Reliability": {
        "sec": "Sprint 5",
        "slides": "Sprint-4-info-review.pdf (Part 2) / Architecture Docs",
        "review_video": "059 FEB 24 Sprint Review Best practices for cloud deployment, monitoring and performance tuning.mp4",
        "lab_video": "060 FEB 26 Sprint Build Lab Containerise your capstone and implement CI Pipeline.mp4",
        "oh_video": "061 FEB 27 Office Hours.mp4",
        "hands_on_videos": [
            ("062 Video 1 (Notebook).mp4", "LiteLLM Router & Model Fallback Mechanics"),
            ("063 Video 2 (Backend).mp4", "FastAPI Backend LiteLLM Fallback Integration"),
            ("064 Video 3 (Backend + Frontend).mp4", "Google Agent Development Kit (ADK) SDK Migration"),
            ("065 Video 4 (Notebook).mp4", "ADK Web Server for Agent Debugging"),
            ("066 Video 5 (Notebook + Backend).mp4", "Remote A2A Server & Client with a2a-sdk"),
            ("067 Video 6 (Backend + CI).mp4", "LangGraph Graph Connection to Remote A2A Server"),
            ("068 Video 6 (Notebooks + Cloud).mp4", "OpenAI Prompt Caching Caveats & Cost Optimization")
        ]
    }
}

for sprint_name, sdata in inventory["sprints"].items():
    smeta = sprint_meta.get(sprint_name, {})
    sec_tag = smeta.get("sec", sprint_name[:8])
    
    # 1. Slide Deck
    slide_file = smeta.get("slides")
    if slide_file and os.path.exists(os.path.join(CODE_DIR, slide_file)):
        lines.append(f"| {sec_tag} | `{slide_file}` | PDF Slide Deck | {sec_tag} Comprehensive Info Review | Deep technical slide deck covering architectures, diagrams, formulas | No | Reference Slides | DONE |")
    
    # 2. Sprint Review Video
    rv = smeta.get("review_video")
    if rv:
        lines.append(f"| {sec_tag} | `{rv}` | MP4 Video | {sec_tag} Review Lecture | Live conceptual deep-dive by Aurimas Griciunas | No | Lecture Recording | DONE |")
        
    # 3. Sprint Build Lab Video
    lv = smeta.get("lab_video")
    if lv:
        lines.append(f"| {sec_tag} | `{lv}` | MP4 Video | {sec_tag} Build Lab | Live coding demonstration & capstone scaffolding | Yes | Lab Walkthrough | DONE |")
        
    # 4. Office Hours Video
    ov = smeta.get("oh_video")
    if ov and "/" not in ov:
        lines.append(f"| {sec_tag} | `{ov}` | MP4 Video | {sec_tag} Office Hours | Q&A, student debugging, architecture clarifications | No | Q&A Session | DONE |")
    elif ov and "/" in ov:
        for single_ov in ov.split(" / "):
            lines.append(f"| {sec_tag} | `{single_ov.strip()}` | MP4 Video | {sec_tag} Office Hours | Q&A and architecture debugging | No | Q&A Session | DONE |")
            
    # 5. HTML Files
    for file_info in sdata:
        fn = file_info["filename"]
        title = file_info.get("title", fn.replace(".html", ""))
        # Clean title
        if title == "End-to-End AI Engineering Bootcamp":
            clean_t = fn.replace(".html", "")
            if clean_t[:3].isdigit():
                clean_t = clean_t[4:]
            title = clean_t
        is_assign = "Yes" if "hands-on" in fn.lower() else "No"
        purpose = "Practical Hands-on Guide" if is_assign == "Yes" else "Core Technical Lesson"
        lines.append(f"| {sec_tag} | `{fn}` | HTML Lesson | {title} | {purpose} | {is_assign} | Primary Text Lesson | DONE |")

    # 6. Hands-on videos
    for hv_file, hv_topic in smeta.get("hands_on_videos", []):
        lines.append(f"| {sec_tag} | `{hv_file}` | MP4 Video | {hv_topic} | Step-by-step code walkthrough matching notebook/backend | Yes | Video companion to notebook | DUPLICATE |")

# Capstone Closing Videos
lines.append("| Capstone | `069 MAR 3 Sprint Review Best practices for cloud deployment, monitoring, and performance tuning (Part 2).mp4` | MP4 Video | Cloud Deployment & Tuning Part 2 | Advanced infrastructure, reliability, and cost tuning | No | Lecture Recording | DONE |")
lines.append("| Capstone | `070 MAR 5 Case studies of real world Agentic AI Systems.mp4` | MP4 Video | Real-World Agentic AI Case Studies | Industry production architectures and post-mortems | No | Guest / Case Study | DONE |")
lines.append("| Capstone | `071 MAR 10 Demo Day Present your working AI product to cohort.mp4` | MP4 Video | Capstone Demo Day | Student capstone project showcases and evaluations | Project | Project Showcase | DONE |")
lines.append("| Capstone | `072 MAR 12 Closing Celebration & Feedback.mp4` | MP4 Video | Closing Celebration & Retrospective | Graduation, career transitions, and next steps | No | Event Recording | DONE |")

# Code Repository Packages
lines.append("| Repo | `ai-engineering-bootcamp-cohort-4-main.zip` | ZIP Archive | Master Project Repository | Full production codebase: FastAPI, LangGraph, Streamlit, MCP servers, Docker | Project | Complete Master Source | DONE |")
lines.append("| Repo | `ai-engineering-bootcamp-cohort-4-sprint-0.zip` | ZIP Archive | Sprint 0 Snapshot | Code snapshot at completion of Sprint 0 | Project | Milestone Snapshot | DUPLICATE |")
lines.append("| Repo | `ai-engineering-bootcamp-cohort-4-sprint-1.zip` | ZIP Archive | Sprint 1 Snapshot | Code snapshot at completion of Sprint 1 | Project | Milestone Snapshot | DUPLICATE |")
lines.append("| Repo | `ai-engineering-bootcamp-cohort-4-sprint-2.zip` | ZIP Archive | Sprint 2 Snapshot | Code snapshot at completion of Sprint 2 | Project | Milestone Snapshot | DUPLICATE |")
lines.append("| Repo | `ai-engineering-bootcamp-cohort-4-sprint-3.zip` | ZIP Archive | Sprint 3 Snapshot | Code snapshot at completion of Sprint 3 | Project | Milestone Snapshot | DUPLICATE |")

out_file = os.path.join(KB_BASE, "01_COURSE_INDEX.md")
with open(out_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print(f"Generated {out_file} with {len(lines)} lines.")
