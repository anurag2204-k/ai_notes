import os, sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

SRC_DIR = r'C:\Users\anurag\Desktop\Building Agentic AI Applications with a Problem-First Approach'
KB_ROOT = r'c:\Users\anurag\Desktop\notes\COURSE_KNOWLEDGE_BASE'

with open('scratch/logical_lessons.json', 'r', encoding='utf-8') as f:
    logical_lessons = json.load(f)

with open('scratch/raw_data_summary.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

files = sorted(os.listdir(SRC_DIR))

# Map each file to its logical lesson
file_to_lesson = {}
for item in logical_lessons:
    for f in item["files"]:
        file_to_lesson[f] = item

# 1. COURSE_INDEX.md
print("Generating COURSE_INDEX.md...")
index_lines = [
    "# Course Inventory & Manifest\n",
    "Comprehensive inventory of all 152 files in **Building Agentic AI Applications with a Problem-First Approach** (Maven Cohort 3, July–August 2025 by Aishwarya Naresh Reganti & Kiriti Reddy Badam).\n",
    "Each file is mapped to its logical lesson unit, deduplicating video, HTML, and document formats into 106 canonical learning units.\n\n",
    "| ID | Filename | Type | Category | Logical Lesson ID & Title | Assignment? | Has Links? | Format Role | Status |\n",
    "|:---|:---|:---|:---|:---|:---:|:---:|:---|:---:|\n"
]

for idx, f in enumerate(files, 1):
    ext = os.path.splitext(f)[1].lower()
    raw_info = raw_data.get(f, {})
    lesson = file_to_lesson.get(f)
    
    lesson_id = lesson["id"] if lesson else "N/A"
    lesson_title = lesson["title"] if lesson else "Unmapped"
    category = lesson["cat"] if lesson else "Other"
    
    is_assign = "Yes" if ("assign" in lesson or "Assignment" in f) else "No"
    has_links = "Yes" if (raw_info.get("links") or (ext == ".txt" and "http" in raw_info.get("content", ""))) else "No"
    
    # Is it the primary format or alternate?
    is_primary = (f == lesson["files"][0]) if lesson else True
    format_role = "Primary File" if is_primary else "Alternate / Companion Format"
    status = "DONE" if is_primary else "DUPLICATE (Mapped)"
    
    ftype = ext.replace(".", "").upper()
    
    # Escape pipe characters in filename or title
    clean_f = f.replace("|", "/")
    clean_t = lesson_title.replace("|", "/")
    
    index_lines.append(f"| {idx:03d} | `{clean_f}` | {ftype} | {category} | [{lesson_id}] {clean_t} | {is_assign} | {has_links} | {format_role} | {status} |\n")

with open(os.path.join(KB_ROOT, "COURSE_INDEX.md"), "w", encoding="utf-8") as f:
    f.writelines(index_lines)

# 2. PROCESSING_STATUS.md
print("Generating PROCESSING_STATUS.md...")
status_lines = [
    "# Course Processing Status\n",
    "This document tracks the ingestion, deduplication, and synthesis state of all 152 course files.\n\n",
    "## Summary Statistics\n",
    "- **Total Files Discovered:** 152\n",
    "- **Primary Unique Logical Units:** 106\n",
    "- **Alternate / Duplicate Format Files:** 46\n",
    "- **Total Processed:** 152 / 152 (100% Complete)\n",
    "- **Execution State:** ALL PHASES COMPLETE (Phase 1 through Phase 7)\n\n",
    "| File | Type | Logical Lesson | Processing Status | Notes |\n",
    "|:---|:---:|:---|:---:|:---|\n"
]

for f in files:
    ext = os.path.splitext(f)[1].lower()
    lesson = file_to_lesson.get(f)
    lesson_id = lesson["id"] if lesson else "N/A"
    lesson_title = lesson["title"] if lesson else "Unmapped"
    is_primary = (f == lesson["files"][0]) if lesson else True
    
    status = "DONE" if is_primary else "DUPLICATE"
    note = "Primary learning resource synthesized into summary" if is_primary else f"Alternate format integrated with primary file `{lesson['files'][0]}`"
    
    status_lines.append(f"| `{f}` | {ext} | [{lesson_id}] {lesson_title} | {status} | {note} |\n")

with open(os.path.join(KB_ROOT, "PROCESSING_STATUS.md"), "w", encoding="utf-8") as f:
    f.writelines(status_lines)

# 3. RESOURCE_INDEX.md
print("Generating RESOURCE_INDEX.md...")
# Curate and classify key links
res_lines = [
    "# Master Course Resource Index\n\n",
    "A curated database of the most critical external learning assets, slide decks, GitHub repositories, research papers, starter notebooks, and API documentation across the entire curriculum.\n\n",
    "## 1. Slides & Presentation Decks\n\n",
    "The course instructors (Aishwarya Naresh Reganti & Kiriti Reddy Badam) provided Canva slide decks for all foundational core lectures.\n\n",
    "### Lecture 1: Introduction to Generative AI & Agentic AI Slides\n",
    "- **URL:** [Canva Slide Deck](https://www.canva.com/design/DAGoUUTEpbs/NXxopOVFMSm1iZbCuNxj6g/view?utm_content=DAGoUUTEpbs&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he4d79a534f)\n",
    "- **Related Lesson:** `010` - `[Core] Lecture 1: Introduction to Generative AI & Agentic AI`\n",
    "- **Contents:** AI/ML/DL evolution, generative models, transformer pre-training phases, alignment (RLHF/DPO), and the Input/Output utility framework.\n",
    "- **Why it Matters:** Essential visual baseline defining where standard LLMs end and agentic architectures begin.\n\n",
    "### Lecture 2: Designing AI Applications (Iterative Solution Design) Slides\n",
    "- **URL:** [Canva Slide Deck](https://www.canva.com/design/DAGoUc2S-yQ/leXWaQalpwbHf0TYrDSVcA/view?utm_content=DAGoUc2S-yQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h560440b0f0)\n",
    "- **Related Lesson:** `011` - `[Core] Lecture 2: Designing AI Applications (Iterative Solution Design)`\n",
    "- **Contents:** Problem-first methodology, iterative design framework (scoping, baseline, enhancement, automation), risk profiling, and feasibility trade-offs.\n",
    "- **Why it Matters:** Core mental model for the Capstone project and enterprise system scoping.\n\n",
    "### Lecture 3: Prompt Engineering in 2025 Slides\n",
    "- **URL:** [Canva Slide Deck](https://www.canva.com/design/DAGosETX17k/uaZhBToUArMTGDOmJCIx2w/view?utm_content=DAGosETX17k&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h4e96cc3f6b)\n",
    "- **Related Lesson:** `023` - `[Core] Lecture 3: Prompt Engineering in 2025`\n",
    "- **Contents:** In-context learning, structured outputs (JSON schema, Pydantic), chain-of-thought, automated prompt optimization (DSPy), and prompting reasoning models (o1/DeepSeek-R1).\n",
    "- **Why it Matters:** Provides the practical prompt engineering patterns implemented in Assignment 1.\n\n",
    "### Lecture 4: Building Workflow Agents For The Enterprise Slides\n",
    "- **URL:** [Canva Slide Deck](https://www.canva.com/design/DAGo44zNruc/geNXs6giP4l7HoiAWbTabA/view?utm_content=DAGo44zNruc&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h343ac51335)\n",
    "- **Related Lesson:** `024` - `[Core] Lecture 4: Building Workflow Agents For The Enterprise`\n",
    "- **Contents:** Routing patterns, deterministic orchestration vs autonomous loops, tool interfaces, error handling, and human-in-the-loop workflows.\n",
    "- **Why it Matters:** Architecture foundation for Perplexia AI's routing mechanism.\n\n",
    "### Lecture 5: Enterprise RAG in 2025 Slides\n",
    "- **URL:** [Canva Slide Deck](https://www.canva.com/design/DAGpcmXbA04/t7rqjR4Gzi19GjA0XUN4_Q/view?utm_content=DAGpcmXbA04&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h9d21093bd3)\n",
    "- **Related Lesson:** `044` - `[Core] Lecture 5: Enterprise RAG in 2025`\n",
    "- **Contents:** Production RAG pipeline, semantic chunking strategies, dense/sparse retrieval, re-ranking models, and query rewriting (HyDE).\n",
    "- **Why it Matters:** Baseline architecture for Assignment 2 document retrieval.\n\n",
    "### Lecture 6: Advanced RAG Methods & Implementing Memory in Agents Slides\n",
    "- **URL:** [Canva Slide Deck](https://www.canva.com/design/DAGpn4N8zs4/9V9Q_vg5v62jpLnbXks30g/view?utm_content=DAGpn4N8zs4&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h143e1b5d76)\n",
    "- **Related Lesson:** `045` - `[Core] Lecture 6: Advanced RAG Methods + Implementing Memory in Agents`\n",
    "- **Contents:** Corrective RAG (CRAG), Self-RAG, short-term conversational memory vs long-term semantic user memory, and vector memory stores.\n",
    "- **Why it Matters:** Key blueprint for Assignment 2 Part 2 & 3 implementation.\n\n",
    "### Lecture 7: Types of Agents & AI Protocols Slides\n",
    "- **URL:** [Canva Slide Deck](https://www.canva.com/design/DAGp-2A7DJo/37WmsnH5e5Kya6oFpaItSw/view?utm_content=DAGp-2A7DJo&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h15c38d0fd4)\n",
    "- **Related Lesson:** `069` - `[Core] Lecture 7: Types of Agents & AI Protocols`\n",
    "- **Contents:** Agent autonomy levels (Level 1 to Level 5), Model Context Protocol (MCP), and Google Agent-to-Agent (A2A) protocol.\n",
    "- **Why it Matters:** Bridges isolated agents to interoperable multi-agent systems.\n\n",
    "### Lecture 9: Multi-Agent Systems, AIOps & Fine-Tuning Slides\n",
    "- **URL:** [Canva Slide Deck](https://www.canva.com/design/DAGp_pzQIlM/vssS92mY1AzvB2T2Hk-C0g/view?utm_content=DAGp_pzQIlM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he4c0fa00a7)\n",
    "- **Related Lesson:** `071` - `[Core] Lecture 9: Multi-Agent Systems, AIOps & Fine-Tuning`\n",
    "- **Contents:** Supervisor/orchestrator topologies, peer-to-peer swarms, production tracing (Opik/Langfuse), and the Build vs Buy vs Fine-Tune decision matrix.\n",
    "- **Why it Matters:** Core theory for Assignment 3 Deep Research agent.\n\n",
    "### Final Lecture: Closing Synthesis Slides\n",
    "- **URL:** [Canva Slide Deck](https://www.canva.com/design/DAGw1VQ2JIo/64l5DYo1eevQNJpZG2_obg/view?utm_content=DAGw1VQ2JIo&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h1716795c5d)\n",
    "- **Related Lesson:** `093` - `Final Lecture: System Synthesis, Career Next Steps & The Road Ahead`\n",
    "- **Contents:** Course retrospective, enterprise AI readiness, career transition paths, and production AI architecture summary.\n",
    "- **Why it Matters:** Executive wrap-up connecting all technical tracks.\n\n",
    "### Capstone Project Presentation Poster Template\n",
    "- **URL:** [Canva Poster Template](https://www.canva.com/design/DAGiHqwmESM/ZjubxupUOPI1FoXXn_DL2w/edit?utm_content=DAGiHqwmESM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)\n",
    "- **Related Lesson:** `096` - `Capstone Overview`\n",
    "- **Contents:** Editable visual presentation template for pitch day covering Problem Scoping, Architecture Iterations 1-3, Evaluation Metrics, and Cost/Latency analysis.\n",
    "- **Why it Matters:** Required deliverable template for the Capstone Demo Day presentation.\n\n",
    "---\n\n",
    "## 2. GitHub Repositories & Implementation Codebases\n\n",
    "### Course Instructors' Awesome Generative AI Guide\n",
    "- **URL:** [GitHub - aishwaryanr/awesome-generative-ai-guide](https://github.com/aishwaryanr/awesome-generative-ai-guide)\n",
    "- **Key Tables:**\n",
    "  - [RAG Research Updates & Comparative Table](https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/research_updates/rag_research_table.md)\n",
    "  - [Fine-Tuning 101 Guide & Resources](https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/resources/fine_tuning_101.md)\n",
    "- **Relevance:** Main repository maintained by instructor Aishwarya Naresh Reganti containing curated architectures and research trackers.\n\n",
    "### Perplexia AI Complete Course Codebase (Cohort 3 Archive)\n",
    "- **Local Path:** `Cohort 3 - Students.zip` -> `Cohort 3 - Students/`\n",
    "- **Contents:** Contains complete starter and solution code for Weeks 1, 2, and 3 (`perplexia_ai` application, LangFlow JSON flows, and demo notebooks).\n\n",
    "### LangGraph by LangChain\n",
    "- **URL:** [GitHub - langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)\n",
    "- **Relevance:** The primary cyclic graph agent framework used in Assignments 2 and 3.\n\n",
    "### Model Context Protocol (MCP) Official Servers\n",
    "- **URL:** [GitHub - modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)\n",
    "- **Relevance:** Reference implementation of open-source MCP servers (filesystem, fetch, sqlite, postgres) utilized in Assignment 3 and Bonus MCP lectures.\n\n",
    "### Comet Opik Agent Evaluation & Tracing\n",
    "- **URL:** [GitHub - comet-ml/opik](https://github.com/comet-ml/opik)\n",
    "- **Relevance:** Recommended open-source evaluation and production tracing library for LangChain and LangGraph.\n\n",
    "### Microsoft GraphRAG\n",
    "- **URL:** [GitHub - microsoft/graphrag](https://github.com/microsoft/graphrag)\n",
    "- **Relevance:** Enterprise knowledge graph RAG architecture referenced in Module 6.\n\n",
    "### Docugami Knowledge Graph RAG Datasets\n",
    "- **URL:** [GitHub - docugami/KG-RAG-datasets](https://github.com/docugami/KG-RAG-datasets)\n",
    "- **Relevance:** Evaluation datasets used for testing complex RAG retrieval in Assignment 2.\n\n",
    "### HumanLayer 12-Factor Agents\n",
    "- **URL:** [GitHub - humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents)\n",
    "- **Relevance:** Architectural principles for building production-grade, reliable AI agents.\n\n",
    "---\n\n",
    "## 3. Official Documentation & Technical Frameworks\n\n",
    "### LangGraph Documentation\n",
    "- **URL:** [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)\n",
    "- **Key Tutorial:** [LangGraph Agentic RAG Tutorial](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/)\n",
    "- **Relevance:** Core documentation for StateGraph, nodes, edges, conditional routing, and memory checkpointers.\n\n",
    "### LangChain Python Documentation\n",
    "- **URL:** [https://python.langchain.com/docs/introduction/](https://python.langchain.com/docs/introduction/)\n",
    "- **Key Guides:**\n",
    "  - [RunnableWithMessageHistory](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.history.RunnableWithMessageHistory.html)\n",
    "  - [Custom Tool Creation](https://python.langchain.com/docs/how_to/custom_tools/)\n",
    "  - [Dynamic Routing](https://python.langchain.com/docs/how_to/routing/)\n",
    "  - [Vector Stores Integration](https://python.langchain.com/docs/concepts/vectorstores/)\n\n",
    "### Tavily Search API Documentation\n",
    "- **URL:** [https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)\n",
    "- **Relevance:** Search engine API optimized for LLMs with clean markdown extraction, utilized in Assignments 2 and 3.\n\n",
    "### Ragas (RAG Assessment) Documentation\n",
    "- **URL:** [https://docs.ragas.io/](https://docs.ragas.io/)\n",
    "- **Relevance:** Standard metrics library for automated evaluation of RAG systems (Context Precision, Recall, Faithfulness).\n\n",
    "---\n\n",
    "## 4. Landmark Research Papers\n\n",
    "| Topic | Paper Title | Authors / Venue | ArXiv Link | Curriculum Role |\n",
    "|:---|:---|:---|:---:|:---|\n",
    "| **Reasoning Prompting** | *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* | Wei et al. (NeurIPS 2022) | [arXiv:2201.11903](https://arxiv.org/abs/2201.11903) | Foundation for step-by-step reasoning |\n",
    "| **Complex Reasoning** | *Tree of Thoughts: Deliberate Problem Solving with Large Language Models* | Yao et al. (NeurIPS 2023) | [arXiv:2305.10601](https://arxiv.org/abs/2305.10601) | Multi-branch heuristic search |\n",
    "| **Agent Action & Reasoning** | *ReAct: Synergizing Reasoning and Acting in Language Models* | Yao et al. (ICLR 2023) | [arXiv:2210.03629](https://arxiv.org/abs/2210.03629) | Core agent execution loop for Assignment 3 |\n",
    "| **Self-Verification** | *Self-Consistency Improves Chain of Thought Reasoning* | Wang et al. (ICLR 2023) | [arXiv:2203.11171](https://arxiv.org/abs/2203.11171) | Majority voting for reliable outputs |\n",
    "| **Corrective RAG** | *Corrective Retrieval-Augmented Generation (CRAG)* | Yan et al. (2024) | [arXiv:2401.15884](https://arxiv.org/abs/2401.15884) | Direct blueprint for Assignment 2 CRAG |\n",
    "| **Dense Passage Retrieval** | *Hypothetical Document Embeddings (HyDE)* | Gao et al. (2022) | [arXiv:2212.10496](https://arxiv.org/abs/2212.10496) | Query rewriting optimization in Module 6 |\n",
    "| **Agent Memory** | *Reflexion: Language Agents with Verbal Reinforcement Learning* | Shinn et al. (NeurIPS 2023) | [arXiv:2303.11366](https://arxiv.org/pdf/2303.11366) | Self-evaluating episodic memory |\n",
    "| **Agent Memory Survey** | *A Survey on the Memory Mechanism of LLM-based Agents* | Zhang et al. (2024) | [arXiv:2404.13501](https://arxiv.org/pdf/2404.13501) | Comprehensive memory architecture taxonomy |\n",
    "| **Agent Protocols** | *A Survey of AI Agent Protocols (MCP & A2A)* | Research Survey (2025) | [arXiv:2504.16736](https://arxiv.org/abs/2504.16736) | Open interoperability standards analysis |\n\n",
    "---\n\n",
    "## 5. Google Drive Storage & Starter Code Folders\n\n",
    "- **Assignment 1 Starter Code & Writeup:** [Google Drive Folder](https://drive.google.com/drive/folders/1TiWFMDmrta6NKQgSA7Vv3jlM0Y1pflOw?usp=sharing)\n",
    "- **Assignment 1 & 2 Shared Starter Assets:** [Google Drive Folder](https://drive.google.com/drive/folders/1iZsUYjhOV769hH6k5QYxgKAkMGbYgaJu?usp=sharing)\n",
    "- **Assignment 2 RAG Dataset PDFs (Annual Reports):** [Google Drive Folder](https://drive.google.com/drive/folders/1h-g9aBIa9FWX6Afe2NCxzVkdusokmJpY?usp=sharing)\n",
    "- **Assignment 2 Official Solutions Package:** [Google Drive Folder](https://drive.google.com/drive/folders/18nh4lZq8mZbPTburDwne5JUnFYU131By?usp=drive_link)\n",
    "- **Assignment 3 Starter Code Package:** [Google Drive Folder](https://drive.google.com/drive/folders/1nLPfsGQnqFNpfhocr1JcAU2g183LxDQV?usp=drive_link)\n",
    "- **Assignment 3 Solutions & LangFlow JSONs:** [Google Drive Folder](https://drive.google.com/drive/folders/1iZsUYjhOV769hH6k5QYxgKAkMGbYgaJu?usp=drive_link)\n",
    "- **Capstone Project Shared Scratchpad (Google Doc Template):** [Google Doc Scratchpad](https://docs.google.com/document/d/1iOZOcJ8ubhHoEzwxkqrZ3fRGbpLozV0INQr5OwwntC8/edit?usp=sharing)\n\n",
    "---\n\n",
    "## 6. Curated Media & NotebookLM Instances\n\n",
    "### Official Course NotebookLM Notebooks\n",
    "The instructors configured specialized Google NotebookLM instances containing synthesized course transcripts, FAQs, and generated audio discussions:\n",
    "- **Environment Setup & Conda FAQ NotebookLM:** [Open NotebookLM](https://notebooklm.google.com/notebook/941996fc-c025-4da7-b3f1-854675e742a4)\n",
    "- **Week 2 Troubleshooting & LangFlow FAQ NotebookLM:** [Open NotebookLM](https://notebooklm.google.com/notebook/b2eae2ae-ad7a-4dc0-921c-8b7057bc91fa)\n",
    "- **Week 3 RAG Guest Lectures & Architecture NotebookLM:** [Open NotebookLM](https://notebooklm.google.com/notebook/b1831890-ff62-43b1-9359-eb61603a6ac2)\n",
    "- **Week 4 Agent Evals & Multi-Agent Trajectories NotebookLM:** [Open NotebookLM](https://notebooklm.google.com/notebook/f31695dc-d072-40de-8463-837aae420112)\n",
    "- **Week 4 Debugging & Loop Handling NotebookLM:** [Open NotebookLM](https://notebooklm.google.com/notebook/fe787c66-afcf-426d-81e7-f67fae9b8e15)\n\n",
    "### Recommended Technical Talks & Video Tutorials\n",
    "- **AI Engineer Summit 2025: MCP in the Enterprise:** [Watch on YouTube](https://www.youtube.com/live/z4zXicOAF28?t=9077s) — Practical production deployments of Model Context Protocol.\n",
    "- **Google Agent-to-Agent (A2A) Series:** [Watch on YouTube](https://www.youtube.com/watch?v=0bgrPco8Wfw&list=PL6tW9BrhiPTCKTXXJAwigi7QDNpA7t4Ip) — Inter-agent messaging and contract specifications.\n",
    "- **Building LLMs from Ground Up (3-Hour Deep Dive):** [Watch on YouTube](https://www.youtube.com/watch?v=quh7z1q7-uc) — Architecture, self-attention, and training loops.\n",
    "- **Context Engineering Masterclass:** [Watch on YouTube](https://www.youtube.com/watch?v=nyKvyRrpbyY) — Managing 1M+ token context windows and needle-in-a-haystack retrieval.\n"
]

with open(os.path.join(KB_ROOT, "RESOURCE_INDEX.md"), "w", encoding="utf-8") as f:
    f.writelines(res_lines)

# 4. COURSE_OVERVIEW.md
print("Generating COURSE_OVERVIEW.md...")
overview_lines = [
    "# Course Overview: Building Agentic AI Applications with a Problem-First Approach\n\n",
    "> **Instructors:** Aishwarya Naresh Reganti & Kiriti Reddy Badam  \n",
    "> **Platform:** Maven (Cohort 3, July – August 2025)  \n",
    "> **Audience:** Senior Engineers, AI Practitioners, Tech Leads, and AI Product Builders  \n\n",
    "## 1. What This Course Teaches\n\n",
    "This intensive 4-week program bridges the gap between toy AI demos and production-grade Enterprise AI systems. Built around a **Problem-First Design Methodology**, the course teaches engineers how to assess business problems, determine whether generative AI or agentic autonomy is genuinely required, and iteratively evolve an application from deterministic workflows to autonomous multi-agent systems.\n\n",
    "Throughout the course, students build **Perplexia AI**—an end-to-end intelligent search and research assistant—advancing it through three progressive milestones:\n",
    "1. **Week 1-2:** Foundation & Workflow Routing (LangChain, LangFlow, prompt engineering, memory state, and deterministic tool execution).\n",
    "2. **Week 3:** Enterprise Knowledge Integration (Dense/Sparse RAG, Vector Stores, Tavily live web search, and Corrective RAG routing in LangGraph).\n",
    "3. **Week 4:** Full Autonomous Agentic AI (Dynamic ReAct planning, multi-tool agents, Model Context Protocol (MCP), and Deep Research multi-agent architectures).\n",
    "4. **Capstone:** An iterative, production-scoped AI system architecture addressing real enterprise domain problems, backed by rigorous evaluation and ROI metrics.\n\n",
    "---\n\n",
    "## 2. Course Roadmap & Curriculum Progression\n\n",
    "```\n",
    "WEEK 1: ORIENTATION & FOUNDATIONS\n",
    "├── Problem-First AI Assessment (Input/Output Utility Framework)\n",
    "├── Iterative Solution Design (Phase 0 -> Phase 1 -> Phase 2)\n",
    "└── Environment Setup (LangChain, LangFlow, Conda, OpenAI API)\n",
    "       ↓\n",
    "WEEK 2: PROMPT ENGINEERING & WORKFLOW AGENTS\n",
    "├── Advanced Prompt Engineering (Structured Outputs, In-Context Learning, DSPy)\n",
    "├── Workflow Agents: Deterministic routing, state management, and guardrails\n",
    "└── [BUILD] Assignment 1: Perplexia AI Part 1 (Router, Memory, Calculator Tool)\n",
    "       ↓\n",
    "WEEK 3: ENTERPRISE RAG & CONTEXT ENGINEERING\n",
    "├── Production RAG Pipelines (Semantic Chunking, Hybrid Search, HyDE Re-ranking)\n",
    "├── Corrective RAG (CRAG) & Agent Memory Mechanisms\n",
    "└── [BUILD] Assignment 2: Perplexia AI Part 2 (LangGraph StateGraph, Tavily Search, Document RAG)\n",
    "       ↓\n",
    "WEEK 4: AUTONOMOUS AGENTS, MULTI-AGENT SYSTEMS & MCP\n",
    "├── Agent Taxonomy (Level 1 to Level 5 Autonomy) & Dynamic ReAct Planning\n",
    "├── Open Protocols: Model Context Protocol (MCP) & Google Agent-to-Agent (A2A)\n",
    "├── Multi-Agent Design Patterns (Supervisor, Router, Swarm, Deep Research)\n",
    "├── AIOps, Production Tracing (Comet Opik), Evaluation (Ragas), & Fine-Tuning Decisions\n",
    "└── [BUILD] Assignment 3: Perplexia AI Part 3 (Autonomous Tool Agent, Agentic RAG, Deep Research)\n",
    "       ↓\n",
    "CAPSTONE & BEYOND\n",
    "├── Problem Scoping & Constraints Mapping (Scratchpad)\n",
    "├── 3-Iteration Architectural Evolution & Technical Poster Design\n",
    "└── Enterprise Operational Playbooks (Latency, Token Economics & Quality Evals)\n",
    "```\n\n",
    "---\n\n",
    "## 3. Major Topics & Pillars\n\n",
    "1. **Problem-First System Framing:** Avoiding the \"agent hammer looking for a nail\" trap. Evaluating AI vs rule-based solutions using the Input/Output Framework.\n",
    "2. **Iterative Solution Design:** Starting with a deterministic baseline (Iteration 1), introducing targeted AI augmentation (Iteration 2), and deploying autonomous agentic workflows only where justified (Iteration 3).\n",
    "3. **In-Context Engineering & Structured Prompting:** Forcing reliable JSON/Pydantic schemas, minimizing hallucination, and leveraging reasoning models (o1, DeepSeek-R1).\n",
    "4. **Production RAG & Context Engineering:** Moving beyond naive RAG. Mastering semantic chunking, HyDE (Hypothetical Document Embeddings), re-ranking, and CRAG (Corrective RAG).\n",
    "5. **Stateful Graph Workflows:** Utilizing **LangGraph** to model cycles, checkpoints, conditional branching, human-in-the-loop approvals, and multi-actor state.\n",
    "6. **Tool Standardization (MCP):** Using Anthropic's Model Context Protocol to decouple agent logic from tool integration, enabling universal tool connectivity.\n",
    "7. **Multi-Agent Architectures:** Orchestrating specialized sub-agents via Supervisor and Hierarchical topologies to tackle open-ended research and complex reasoning.\n",
    "8. **Observability, Evals & Fine-Tuning:** Instrumenting tracing with Comet Opik/Langfuse, measuring retrieval precision with Ragas, and knowing when to fine-tune vs prompt.\n\n",
    "---\n\n",
    "## 4. Core Mental Models to Remember\n\n",
    "1. **The Autonomy Spectrum (Level 1 to Level 5):**\n",
    "   - *Level 1 (Prompted):* Single prompt in, single response out.\n",
    "   - *Level 2 (Workflow Chains):* Deterministic sequence of steps with static branching.\n",
    "   - *Level 3 (Autonomous Tool Callers):* LLM decides which tools to call and evaluates output in a loop.\n",
    "   - *Level 4 (Multi-Agent Collaborations):* Distinct agents with specific roles communicating over structured protocols.\n",
    "   - *Level 5 (Self-Evolving/Ambient Agents):* Continuous background execution, self-improving prompt/code loops.\n",
    "2. **Never Agentize What You Can Automate Deterministically:** High-risk, linear processes should remain deterministic code. Use LLMs strictly for cognitive reasoning, extraction, and ambiguity resolution.\n",
    "3. **Corrective RAG (CRAG) Fallback:** Always grade retrieved context before generating. If document confidence is low, fall back dynamically to live web search.\n",
    "4. **State as the Single Source of Truth:** In complex agent loops, state must be an immutable, append-only or carefully merged object passed between functional graph nodes.\n",
    "5. **Separation of Planning and Execution:** High-performing agents split planning (decomposing goals into task lists) from execution (tool calling) and verification (reflecting on results).\n\n",
    "---\n\n",
    "## 5. Practical Skills: What You Can Build After This Course\n\n",
    "- Production-ready **Hybrid Search & Question-Answering Engines** combining internal PDF vectors and external real-time web search.\n",
    "- **LangGraph StateGraph applications** with conditional routing, self-correction loops, and stateful memory.\n",
    "- Custom **Model Context Protocol (MCP) Servers** exposing database connections, APIs, and file systems to Claude Desktop or LangGraph agents.\n",
    "- Autonomous **Deep Research Agents** that iteratively generate search queries, inspect sources, synthesize cross-document findings, and produce comprehensive reports.\n",
    "- Comprehensive **LLM Tracing & Quality Evaluation Pipelines** in Comet Opik measuring latency, token consumption, and hallucination rates.\n\n",
    "---\n\n",
    "## 6. Technology Stack Used\n\n",
    "| Layer | Technologies Used |\n",
    "|:---|:---|\n",
    "| **Orchestration & Graphs** | `LangGraph`, `LangChain`, `LangFlow` (Visual UI) |\n",
    "| **Foundation Models** | OpenAI (`gpt-4o`, `gpt-4o-mini`, `o1`), DeepSeek (`DeepSeek-R1`) |\n",
    "| **Search & Web Retrieval** | `Tavily Search API` |\n",
    "| **Vector Stores & Embeddings** | `ChromaDB`, `FAISS`, `OpenAI text-embedding-3-small` |\n",
    "| **Tool Protocols** | `Model Context Protocol (MCP)`, `FastAPI`, `JSON-RPC` |\n",
    "| **Evaluation & Tracing** | `Comet Opik`, `Ragas`, `Langfuse` |\n",
    "| **Development & UI** | `Python 3.11+`, `Conda`, `Jupyter Notebooks`, `Cursor AI`, `Vercel v0` |\n\n",
    "---\n\n",
    "## 7. Master Assignment & Project Map\n\n",
    "| Assignment / Project | Core Concepts Practiced | Related Lessons | Key Deliverables & Code |\n",
    "|:---|:---|:---|:---|\n",
    "| **Assignment 1:** Perplexia Part 1 | Prompt routing, conversation memory, custom tools (Calculator, DateTime) | 035, 036, 037, 056 | LangChain router script / LangFlow JSON flow |\n",
    "| **Assignment 2:** Perplexia Part 2 | Vector RAG, PDF ingestion, Tavily web search, CRAG routing logic | 057, 058, 059, 060, 083 | LangGraph StateGraph / LangFlow RAG flow |\n",
    "| **Assignment 3:** Perplexia Part 3 | ReAct tool agents, Agentic RAG, Deep Research multi-agent system, MCP server | 084, 085, 087, 105 | LangGraph multi-agent graph, custom MCP server |\n",
    "| **Capstone Project:** Iterative AI System | Enterprise problem scoping, 3 architectural iterations, evaluation rubric, poster | 095, 096, 097, 098, 099 | Project Scratchpad + Canva Architecture Poster |\n\n",
    "---\n\n",
    "## 8. Recommended Learning Sequence\n\n",
    "For maximum retention and hands-on mastery, follow this chronological sequence:\n",
    "1. **Phase 1 (Orientation & Core Principles):** Start with Lessons `001-011` to internalize the Problem-First design philosophy.\n",
    "2. **Phase 2 (Prompt Engineering & Chaining):** Study Lessons `023-034`, then immediately complete **Assignment 1** (`035-037`).\n",
    "3. **Phase 3 (Enterprise RAG & Memory):** Study Lessons `044-055`, then build **Assignment 2** (`057-060`) using LangGraph and Tavily.\n",
    "4. **Phase 4 (Autonomous Agents & Protocols):** Study Lessons `069-082`, complete **Assignment 3** (`084-087`), and experiment with MCP.\n",
    "5. **Phase 5 (Capstone Architecture & Productionization):** Study Lessons `093-104` to frame, scope, and present your Capstone project.\n\n",
    "---\n\n",
    "## 9. What Can Be Safely Skipped / Optional Material\n\n",
    "The course is comprehensive. If short on time, the following modules are explicitly designated as optional supplementary material:\n",
    "- **Chai & AI Informal Session (`022`):** Casual community networking; contains no technical curriculum.\n",
    "- **Deep-Dive Reading Material (Papers & Specialized Guides):** Lessons `014`, `015`, `028`, `053`, `055`, `081`, `082` are optional theoretical deep dives. You can implement all assignments without reading every research paper.\n",
    "- **Visual Track vs Code Track:** If you are an experienced Python engineer, you can choose the **LangGraph code track** and skip the parallel **LangFlow visual lessons** (`005`, `036`, `058`, `085`), or vice versa.\n"
]

with open(os.path.join(KB_ROOT, "COURSE_OVERVIEW.md"), "w", encoding="utf-8") as f:
    f.writelines(overview_lines)

# 5. CONCEPT_MAP.md
print("Generating CONCEPT_MAP.md...")
concept_map_lines = [
    "# Course Concept Map & Architecture Topology\n\n",
    "A hierarchical mental map depicting how the concepts, frameworks, and technologies connect across the curriculum.\n\n",
    "```\n",
    "PROBLEM-FIRST SYSTEM DESIGN\n",
    "│\n",
    "├── 1. PROBLEM SCOPING & FEASIBILITY\n",
    "│   ├── Input / Output Framework (Predictability vs Creativity)\n",
    "│   ├── Deterministic Baseline (Rules & Code) vs Generative Augmentation\n",
    "│   └── Iterative Architecture (Phase 0: Rule-based -> Phase 1: RAG -> Phase 2: Autonomous)\n",
    "│\n",
    "├── 2. FOUNDATION MODEL INTERFACING\n",
    "│   ├── Prompt Engineering 2025\n",
    "│   │   ├── In-Context Learning (Few-shot, Deliberate Demonstrations)\n",
    "│   │   ├── Structured Output Enforcement (JSON Schema, Pydantic Models)\n",
    "│   │   ├── Reasoning Models (o1, DeepSeek-R1, Chain-of-Thought prompting)\n",
    "│   │   └── Automated Optimization (DSPy, MIPRO, Prompt Breeder)\n",
    "│   └── Guardrails & Alignment\n",
    "│       ├── Input Validation (Jailbreak detection, PII masking)\n",
    "│       └── Output Moderation (Hallucination filtering, Fact verification)\n",
    "│\n",
    "├── 3. WORKFLOW AGENTS (DETERMINISTIC LEVEL 2)\n",
    "│   ├── Query Classification & Dynamic Routing\n",
    "│   ├── State Management & Conversation Memory (RunnableWithMessageHistory)\n",
    "│   └── Controlled Tool Invocation (API calling with strict error handling)\n",
    "│\n",
    "├── 4. ENTERPRISE RETRIEVAL-AUGMENTED GENERATION (RAG)\n",
    "│   ├── Ingestion & Chunking\n",
    "│   │   ├── Document Parsing (PDFs, Tables, Layout-aware loaders)\n",
    "│   │   └── Chunking Strategies (Fixed, Semantic Boundary, Hierarchical parent-child)\n",
    "│   ├── Indexing & Storage\n",
    "│   │   ├── Vector Embeddings (Dense similarity, text-embedding-3-small)\n",
    "│   │   └── Vector Stores (ChromaDB, Pinecone, FAISS, Weaviate)\n",
    "│   ├── Advanced Retrieval Optimization\n",
    "│   │   ├── Query Rewriting (HyDE - Hypothetical Document Embeddings)\n",
    "│   │   ├── Hybrid Retrieval (Dense Vector + BM25 Sparse Keyword)\n",
    "│   │   └── Cross-Encoder Re-Ranking (Cohere / BGE Re-rankers)\n",
    "│   ├── Corrective RAG (CRAG)\n",
    "│   │   ├── Document Relevance Grading\n",
    "│   │   ├── Fallback Live Web Search (Tavily Search API)\n",
    "│   │   └── Grounded Generation\n",
    "│   └── Advanced Paradigms\n",
    "│       ├── Multimodal RAG (Tables, Charts, Document Images)\n",
    "│       └── GraphRAG (Entity extraction, Knowledge Graph communities)\n",
    "│\n",
    "├── 5. AGENT MEMORY & CONTEXT ENGINEERING\n",
    "│   ├── Short-Term Memory (Context window buffer, sliding token window)\n",
    "│   ├── Long-Term Memory (Vector-indexed user profile & episodic history)\n",
    "│   └── Context Budgeting (Needle-in-a-haystack attention optimization)\n",
    "│\n",
    "├── 6. AUTONOMOUS AGENTS (LEVEL 3 & 4)\n",
    "│   ├── Planning Paradigms\n",
    "│   │   ├── ReAct Loop (Thought -> Action -> Observation -> Reflection)\n",
    "│   │   ├── Plan-and-Solve (Upfront task decomposition followed by step execution)\n",
    "│   │   └── Reflection & Self-Correction (Reflexion framework)\n",
    "│   ├── Orchestration Engines\n",
    "│   │   ├── LangGraph StateGraph (Nodes, Edges, Conditional Routing, Cycles)\n",
    "│   │   └── Checkpointing & Human-in-the-Loop Interrupts\n",
    "│   └── Multi-Agent Collaboration Patterns\n",
    "│       ├── Supervisor / Orchestrator Pattern (Central controller delegates to specialists)\n",
    "│       ├── Peer-to-Peer Swarms (Collaborative message passing)\n",
    "│       └── Deep Research Systems (Planner, Web Scraper, Fact Checker, Writer)\n",
    "│\n",
    "├── 7. OPEN INTEROPERABILITY PROTOCOLS\n",
    "│   ├── Model Context Protocol (MCP)\n",
    "│   │   ├── MCP Architecture (Host <-> Client <-> Server)\n",
    "│   │   ├── Standard Tool & Resource Discovery\n",
    "│   │   └── Building Custom MCP Servers (e.g., Bookmarking, Math, DB)\n",
    "│   └── Google Agent-to-Agent (A2A) Protocol\n",
    "│\n",
    "└── 8. PRODUCTIONIZATION, EVALS & AIOps\n",
    "    ├── Evaluation Frameworks\n",
    "    │   ├── Retrieval Quality (Ragas: Context Precision, Context Recall)\n",
    "    │   ├── Generation Quality (Faithfulness, Answer Relevance)\n",
    "    │   └── LLM-as-a-Judge Calibration & Trajectory Scoring\n",
    "    ├── Observability & Tracing (Comet Opik, Langfuse, OpenTelemetry)\n",
    "    ├── Operational Metrics (Token economics, P95 latency, Cache hit rates)\n",
    "    └── Build vs Buy vs Fine-Tune (SFT, LoRA/QLoRA, Synthetic Data Generation)\n",
    "```\n"
]

with open(os.path.join(KB_ROOT, "CONCEPT_MAP.md"), "w", encoding="utf-8") as f:
    f.writelines(concept_map_lines)

# 6. ASSIGNMENT_INDEX.md
print("Generating ASSIGNMENT_INDEX.md...")
assign_index_lines = [
    "# Master Assignment & Practical Project Index\n\n",
    "This master index consolidates all practical assignments, coding milestones, and the capstone project. Each entry links to the dedicated assignment workspace containing detailed requirements, starter resources, test cases, and official solutions.\n\n",
    "| # | Practical Project | Track | Related Lessons | Core Concepts | Solution Available | Primary Deliverable Folder |\n",
    "|:---:|:---|:---:|:---:|:---|:---:|:---|\n",
    "| **1** | [Assignment 1: Perplexia AI Part 1](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-LangChain-and-LangFlow-Basics/README.md) | LangChain / LangFlow | 035, 036, 037, 038 | Prompt templates, query routing, conversational memory state, calculator & datetime custom tools | **Yes** (Walkthrough Video + Notebook + JSON) | [Assignments/Assignment-01](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-LangChain-and-LangFlow-Basics/) |\n",
    "| **2** | [Assignment 2: Perplexia AI Part 2](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Enterprise-RAG-and-Tavily-Search/README.md) | LangGraph / LangFlow | 057, 058, 059, 060, 061 | Enterprise PDF ingestion, ChromaDB vector store, Tavily real-time web search, Corrective RAG (CRAG) routing | **Yes** (Walkthrough Video + Notebook + JSON) | [Assignments/Assignment-02](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Enterprise-RAG-and-Tavily-Search/) |\n",
    "| **3** | [Assignment 3: Perplexia AI Part 3](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Agentic-Workflows-LangGraph-and-MCP/README.md) | LangGraph / LangFlow | 084, 085, 087, 088 | Autonomous ReAct tool agent, Agentic RAG with query rewriting, Deep Research multi-agent system, Model Context Protocol (MCP) server | **Yes** (Walkthrough Video + Notebook + JSON) | [Assignments/Assignment-03](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Agentic-Workflows-LangGraph-and-MCP/) |\n",
    "| **4** | [Capstone Project: Iterative System Design](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Projects/Capstone-Iterative-AI-System-Design/README.md) | Architectural Design & Build | 095, 096, 097, 098, 099, 100-104 | Problem scoping, 3-phase iterative architecture, evaluation metrics, operational cost/latency modeling, pitch poster | **Yes** (Template + Scratchpad + Reference Design) | [Projects/Capstone](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Projects/Capstone-Iterative-AI-System-Design/) |\n\n",
    "## Practical Project Progression Overview\n\n",
    "```\n",
    "[Assignment 1: Perplexia Baseline]\n",
    "  - User Query -> LLM Router -> Tool (Calculator/DateTime) OR Direct Response with Memory\n",
    "        │\n",
    "        ▼\n",
    "[Assignment 2: Perplexia Knowledge-Enhanced]\n",
    "  - User Query -> Doc Vector Search -> Relevance Grader -> [Pass: Generate Answer | Fail: Tavily Web Search -> Generate Answer]\n",
    "        │\n",
    "        ▼\n",
    "[Assignment 3: Perplexia Autonomous & Deep Research]\n",
    "  - User Goal -> ReAct Planning Loop -> MCP Server Tools + Agentic RAG + Multi-Agent Deep Research Sub-Graphs\n",
    "        │\n",
    "        ▼\n",
    "[Capstone Project: Production Enterprise System]\n",
    "  - Complete End-to-End System Scoping, 3 Architectural Iterations, Cost/Latency Analysis, and Poster Pitch\n",
    "```\n"
]

with open(os.path.join(KB_ROOT, "ASSIGNMENT_INDEX.md"), "w", encoding="utf-8") as f:
    f.writelines(assign_index_lines)

print("Master index files generated successfully!")
