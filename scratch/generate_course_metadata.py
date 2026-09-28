import os, sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

SRC_DIR = r'C:\Users\anurag\Desktop\Building Agentic AI Applications with a Problem-First Approach'
files = sorted(os.listdir(SRC_DIR))

with open('scratch/raw_data_summary.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# Define mapping rules for logical lessons
# We group pairs/triplets:
# (004, 005), (006, 007), (012, 013), (014, 015), (022, 023), (024, 025), (026, 027), (028, 029),
# (031, 032), (033, 034), (045, 046), (047, 048), (051, 052), (053, 054), (055, 056), (057, 058),
# (059, 060), (061, 062), (063, 064), (066, 067, 068), (077, 078, 079), (080, 081), (082, 083),
# (086, 087), (089, 090), (091, 092), (094, 095), (096, 097), (098, 099), (100, 101), (103, 104),
# (106, 107), (117, 118, 119), (120, 121), (124, 125), (127, 128, 129), (130, 131), (132, 133),
# (134, 135), (136, 137), (149, 150, 151)

groups_def = [
    # Module 1: Course Orientation, Setup & Foundations (001 - 011)
    {"id": "001", "files": ["001 Welcome Lecture.mp4"], "title": "Welcome Lecture", "cat": "Core", "type": "Lecture", "mod": 1, "week": 1},
    {"id": "002", "files": ["002 [Build] Introduction.html"], "title": "[Build] Introduction to Course Hands-On Tracks", "cat": "Build", "type": "Tutorial", "mod": 1, "week": 1},
    {"id": "003", "files": ["003 [Build] Environment Setup for Assignments.html"], "title": "[Build] Environment Setup for Assignments (Conda, API Keys, Dependencies)", "cat": "Build", "type": "Tutorial", "mod": 1, "week": 1},
    {"id": "004", "files": ["004 [Build] LangChain Setup and Demo.html", "005 Longchain Setup and Demo.mp4"], "title": "[Build] LangChain Setup and Interactive Demo", "cat": "Build", "type": "Demo / Tutorial", "mod": 1, "week": 1},
    {"id": "005", "files": ["006 [Build]LangFlow Setup and Demo.html", "007 LangFlow Setup and Demo.mp4"], "title": "[Build] LangFlow Setup and Visual Pipeline Demo", "cat": "Build", "type": "Demo / Tutorial", "mod": 1, "week": 1},
    {"id": "006", "files": ["008 [Grow] NotebookLM For Analysis.html"], "title": "[Grow] NotebookLM For Deep Technical Analysis & Audio Summaries", "cat": "Grow", "type": "Deep Dive", "mod": 1, "week": 1},
    {"id": "007", "files": ["009 [Grow] AI Models & Agents When to Choose What.html"], "title": "[Grow] AI Models & Agents: When to Choose What (Selection Framework)", "cat": "Grow", "type": "Deep Dive", "mod": 1, "week": 1},
    {"id": "008", "files": ["010 [Build] Cursor AI For Coding Assistance.html"], "title": "[Build] Cursor AI For Accelerated AI Development & Pair Programming", "cat": "Build", "type": "Tutorial", "mod": 1, "week": 1},
    {"id": "009", "files": ["011 [Grow] Vercel v0 for Building Web Apps.html"], "title": "[Grow] Vercel v0 for Rapid Generative UI & Full-Stack Prototyping", "cat": "Grow", "type": "Deep Dive", "mod": 1, "week": 1},

    # Module 2: Generative AI Foundations & Iterative System Design (012 - 021)
    {"id": "010", "files": ["012 [Core] Lecture 1 Introduction to Generative AI & Agentic AI.mp4", "013 [Core] Lecture 1 Introduction to Generative AI & Agentic AI.html"], "title": "[Core] Lecture 1: Introduction to Generative AI & Agentic AI", "cat": "Core", "type": "Core Lecture", "mod": 2, "week": 1},
    {"id": "011", "files": ["014 [Core] Lecture 2 Designing AI Applications (Iterative Solution Design).mp4", "015 [Core] Lecture 2 Designing AI Applications (Iterative Solution Design).html"], "title": "[Core] Lecture 2: Designing AI Applications (Iterative Solution Design)", "cat": "Core", "type": "Core Lecture", "mod": 2, "week": 1},
    {"id": "012", "files": ["016 [Grow] Generative AI & Agentic AI Terms You Must Know.html"], "title": "[Grow] Generative AI & Agentic AI Glossary: Core Terms & Taxonomy", "cat": "Grow", "type": "Reference Material", "mod": 2, "week": 1},
    {"id": "013", "files": ["017 [Grow] Enterprise AI Adoption Trends, ROI, and the Road Ahead.html"], "title": "[Grow] Enterprise AI Adoption Trends, ROI Calculation & Executive Roadmap", "cat": "Grow", "type": "Deep Dive", "mod": 2, "week": 1},
    {"id": "014", "files": ["018 [Grow] Understanding Deep Learning, Neural Networks & LLM Architecture.html"], "title": "[Grow] Foundations: Deep Learning, Neural Networks & Transformer LLM Architecture", "cat": "Grow", "type": "Deep Dive", "mod": 2, "week": 1},
    {"id": "015", "files": ["019 [Grow] DeepSeek-R1 and Large Reasoning Models.html"], "title": "[Grow] Large Reasoning Models: DeepSeek-R1, Chain-of-Thought & RL Scaling", "cat": "Grow", "type": "Deep Dive", "mod": 2, "week": 1},
    {"id": "016", "files": ["020 [Grow] LLM Performance Benchmarks.html"], "title": "[Grow] LLM Performance Benchmarks (MMLU, HumanEval, TruthfulQA, BBH)", "cat": "Grow", "type": "Reference Material", "mod": 2, "week": 1},
    {"id": "017", "files": ["021 [Grow] Demo Day Video From Cohort 1 & Cohort 2.html"], "title": "[Grow] Demo Day Retrospective: Real-World Systems From Cohorts 1 & 2", "cat": "Grow", "type": "Supplementary Resource", "mod": 2, "week": 1},

    # Module 3: Week 1 Applied Discussions & Office Hours (022 - 030)
    {"id": "018", "files": ["022 Week 1 Homework Office Hours - July 30.docx", "023 Week 1 Homework Office Hours.mp4"], "title": "Week 1 Homework Office Hours (July 30): Component Selection & Setup", "cat": "Office Hours", "type": "Office Hours", "mod": 3, "week": 1},
    {"id": "019", "files": ["024 Week 1 Content Office Hours.mp4", "025 Week 1 Content Office Hours - July 31.docx"], "title": "Week 1 Content Office Hours (July 31): System Design & Scope Framing", "cat": "Office Hours", "type": "Office Hours", "mod": 3, "week": 1},
    {"id": "020", "files": ["026 Week 1 Content Office Hours - Aug 2.mp4", "027 Week 1 Content Office Hours - August 2.docx"], "title": "Week 1 Content Office Hours (Aug 2): Enterprise Feasibility & Risk", "cat": "Office Hours", "type": "Office Hours", "mod": 3, "week": 1},
    {"id": "021", "files": ["028 Week 1 Homework Office Hours - Aug 2.mp4", "029 Week 1 Homework Office Hours - August 2.docx"], "title": "Week 1 Homework Office Hours (Aug 2): Pipeline Troubleshooting & Flows", "cat": "Office Hours", "type": "Office Hours", "mod": 3, "week": 1},
    {"id": "022", "files": ["030 Chai & AI Session (Not Recorded).mp4"], "title": "Chai & AI Community Session: Open Q&A and Career Discussions", "cat": "Other", "type": "Workshop", "mod": 3, "week": 1},

    # Module 4: Advanced Prompt Engineering & Enterprise Workflow Agents (031 - 044)
    {"id": "023", "files": ["031 [Core] Lecture 3 Prompt Engineering in 2025.html", "032 [Core] Lecture 3 Prompt Engineering in 2025.mp4"], "title": "[Core] Lecture 3: Prompt Engineering in 2025 (Techniques, DSPy & Reasoning)", "cat": "Core", "type": "Core Lecture", "mod": 4, "week": 2},
    {"id": "024", "files": ["033 [Core] Lecture 4 Building Workflow Agents For The Enterprise.html", "034 [Core] Lecture 4 Building Workflow Agents For The Enterprise.mp4"], "title": "[Core] Lecture 4: Building Workflow Agents For The Enterprise (Chains to Graphs)", "cat": "Core", "type": "Core Lecture", "mod": 4, "week": 2},
    {"id": "025", "files": ["035 [Grow] Skill Based Prompting  A Deep Dive.html"], "title": "[Grow] Skill-Based Prompting: CoT, ToT, ReAct, Least-to-Most & Decomposition", "cat": "Grow", "type": "Deep Dive", "mod": 4, "week": 2},
    {"id": "026", "files": ["036 [Grow] Automatic Prompt Optimization A Deep Dive.html"], "title": "[Grow] Automatic Prompt Optimization (APO, DSPy, Prompt Breeder & MIPRO)", "cat": "Grow", "type": "Deep Dive", "mod": 4, "week": 2},
    {"id": "027", "files": ["037 [Grow] Prompting For Reasoning Models.html"], "title": "[Grow] Prompting Strategies for Reasoning Models (o1, o3, DeepSeek-R1)", "cat": "Grow", "type": "Deep Dive", "mod": 4, "week": 2},
    {"id": "028", "files": ["038 [Grow] Reading Prompt Engineering Research.html"], "title": "[Grow] Key Research Papers in Prompt Engineering and In-Context Learning", "cat": "Grow", "type": "Deep Dive", "mod": 4, "week": 2},
    {"id": "029", "files": ["039 [Grow] Workflow Agents in the Enterprise (Popular Architectures & Examples).html"], "title": "[Grow] Workflow Agent Architectures in Enterprise (Deterministic vs Autonomous)", "cat": "Grow", "type": "Deep Dive", "mod": 4, "week": 2},
    {"id": "030", "files": ["040 [Grow] Evaluating Workflow Agents & Challenges.html"], "title": "[Grow] Evaluating Workflow Agents: Deterministic Checks & LLM-as-a-Judge", "cat": "Grow", "type": "Deep Dive", "mod": 4, "week": 2},
    {"id": "031", "files": ["041 [Grow] Evaluating LLM Judge Evaluations Best Practices (Aishwarya's talk).mp4"], "title": "[Grow] Best Practices for LLM-as-a-Judge Evaluations (Instructor Masterclass)", "cat": "Grow", "type": "Workshop", "mod": 4, "week": 2},
    {"id": "032", "files": ["042 [Grow] Guardrails in AI Systems A Deep Dive.html"], "title": "[Grow] Guardrails in Production AI Systems: Input, Output & Execution Safety", "cat": "Grow", "type": "Deep Dive", "mod": 4, "week": 2},
    {"id": "033", "files": ["043 [Grow] MCP Introduction & What it Enables.html"], "title": "[Grow] Model Context Protocol (MCP) Introduction: Universal Tool Standardization", "cat": "Grow", "type": "Deep Dive", "mod": 4, "week": 2},
    {"id": "034", "files": ["044 Building Agentic AI Applications in 2025.mp4"], "title": "Building Agentic AI Applications in 2025: Paradigm Shifts & Tooling", "cat": "Core", "type": "Lecture", "mod": 4, "week": 2},

    # Module 5: Assignment 1 & Week 2 Implementation / Office Hours (045 - 060)
    {"id": "035", "files": ["045 [Build] Assignment 1 - Using LangChain.html", "046 [Build] Assignment 1 - Using LangChain.mp4"], "title": "[Build] Assignment 1: Building Perplexia AI Part 1 with LangChain", "cat": "Build", "type": "Assignment", "mod": 5, "week": 2, "assign": 1},
    {"id": "036", "files": ["047 [Build] Assignment 1 - Using LangFlow.mp4", "048 [Build] Assignment 1 - Using LangFlow.html"], "title": "[Build] Assignment 1: Building Perplexia AI Part 1 with LangFlow", "cat": "Build", "type": "Assignment", "mod": 5, "week": 2, "assign": 1},
    {"id": "037", "files": ["049 [Build] Assignment 1 - Test Cases Sample.html"], "title": "[Build] Assignment 1 Test Cases & Evaluation Benchmark", "cat": "Build", "type": "Assignment", "mod": 5, "week": 2, "assign": 1},
    {"id": "038", "files": ["050 [Build] Running Into Issues Start Here FAQs, Common Issues etc..html"], "title": "[Build] Week 2 Troubleshooting Guide & Assignment 1 FAQ", "cat": "Build", "type": "Tutorial", "mod": 5, "week": 2},
    {"id": "039", "files": ["051 Week 2 Homework Office Hours - Aug 6.mp4", "052 Week 2 Homework Office Hours - August 6.docx"], "title": "Week 2 Homework Office Hours (Aug 6): Memory State & Routing", "cat": "Office Hours", "type": "Office Hours", "mod": 5, "week": 2},
    {"id": "040", "files": ["053 Week 2 Content Office Hours - Aug 8.mp4", "054 Week 2 Content Office Hours - August 7.docx"], "title": "Week 2 Content Office Hours (Aug 7/8): Structured Prompts & Tools", "cat": "Office Hours", "type": "Office Hours", "mod": 5, "week": 2},
    {"id": "041", "files": ["055 Understanding the Agent Development Lifecycle in the Enterprise [Sam Julien & Ugo Osuji].mp4", "056 Understanding the Agent Development Lifecycle in the Enterprise [Sam Julien & Ugo Osuji].html"], "title": "Guest Lecture: Enterprise Agent Lifecycle [Sam Julien & Ugo Osuji, Microsoft]", "cat": "Grow", "type": "Guest Lecture", "mod": 5, "week": 2},
    {"id": "042", "files": ["057 Week 2 Content Office Hours - Aug 9.mp4", "058 _Week 2 Content Office Hours - August 9.docx"], "title": "Week 2 Content Office Hours (Aug 9): Evaluation & Guardrails", "cat": "Office Hours", "type": "Office Hours", "mod": 5, "week": 2},
    {"id": "043", "files": ["059 Week 2 Homework Office Hours - Aug 9.mp4", "060 Week 2 Homework Office Hours - August 9.docx"], "title": "Week 2 Homework Office Hours (Aug 9): Assignment 1 Final Submissions", "cat": "Office Hours", "type": "Office Hours", "mod": 5, "week": 2},

    # Module 6: Enterprise RAG Architecture, Memory & Context Engineering (061 - 076)
    {"id": "044", "files": ["061 [Core] Enterprise RAG in 2025.html", "062 [Core] Enterprise RAG in 2025.mp4"], "title": "[Core] Lecture 5: Enterprise RAG in 2025 (Pipeline, Chunking & HyDE)", "cat": "Core", "type": "Core Lecture", "mod": 6, "week": 3},
    {"id": "045", "files": ["063 [Core] Advanced RAG Methods + Implementing Memory in Agents.html", "064 [Core] Advanced RAG Methods + Implementing Memory in Agents.mp4"], "title": "[Core] Lecture 6: Advanced RAG Methods & Long-Term Agent Memory", "cat": "Core", "type": "Core Lecture", "mod": 6, "week": 3},
    {"id": "046", "files": ["065 [Core] Context Engineering in Agents.html"], "title": "[Core] Context Engineering in Agents: Managing Attention & Token Budgets", "cat": "Core", "type": "Core Lecture", "mod": 6, "week": 3},
    {"id": "047", "files": ["066 [Grow] Recorded Guest Lectures on RAG in the Enterprise.html", "067 [Grow] Recorded Guest Lectures on RAG in the Enterprise 1.mp4", "068 [Grow] Recorded Guest Lectures on RAG in the Enterprise 2.mp4"], "title": "[Grow] Enterprise RAG Case Studies: Production Scaling & Architecture", "cat": "Grow", "type": "Guest Lecture", "mod": 6, "week": 3},
    {"id": "048", "files": ["069 [Grow] Vector Databases Deep Dive.html"], "title": "[Grow] Vector Databases Deep Dive: HNSW, IVF, Pinecone, Chroma & Weaviate", "cat": "Grow", "type": "Deep Dive", "mod": 6, "week": 3},
    {"id": "049", "files": ["070 [Grow] Frequently Used RAG Evaluation Metrics.html"], "title": "[Grow] RAG Evaluation Metrics: Faithfulness, Answer Relevance, Context Precision", "cat": "Grow", "type": "Deep Dive", "mod": 6, "week": 3},
    {"id": "050", "files": ["071 [Grow] RAG Optimizations Deep Dive (Caching & Agentic RAG).html"], "title": "[Grow] RAG Optimizations: Semantic Caching, Corrective RAG & Query Routing", "cat": "Grow", "type": "Deep Dive", "mod": 6, "week": 3},
    {"id": "051", "files": ["072 [Grow] Multimodal RAG Deep-Dive.html"], "title": "[Grow] Multimodal RAG: Processing Tables, Images, Charts & Document Layouts", "cat": "Grow", "type": "Deep Dive", "mod": 6, "week": 3},
    {"id": "052", "files": ["073 [Grow] GraphRAG Deep-Dive.html"], "title": "[Grow] GraphRAG Deep Dive: Knowledge Graphs, Entity Extraction & Global Summaries", "cat": "Grow", "type": "Deep Dive", "mod": 6, "week": 3},
    {"id": "053", "files": ["074 [Grow] Reading RAG Papers.html"], "title": "[Grow] Essential Reading: Landmark RAG Research Papers", "cat": "Grow", "type": "Deep Dive", "mod": 6, "week": 3},
    {"id": "054", "files": ["075 [Grow] Additional Resources on Agent Memory.html"], "title": "[Grow] Agent Memory Frameworks: Short-Term, Long-Term & Episodic Storage", "cat": "Grow", "type": "Deep Dive", "mod": 6, "week": 3},
    {"id": "055", "files": ["076 [Grow] Reading Agent Memory Papers.html"], "title": "[Grow] Landmark Papers on Agent Memory: Generative Agents, MemGPT & Reflexion", "cat": "Grow", "type": "Deep Dive", "mod": 6, "week": 3},

    # Module 7: Assignment 2 & Week 3 Implementation / Office Hours (077 - 099)
    {"id": "056", "files": ["077 [Build] Assignment 1 Solutions 1.mp4", "078 [Build] Assignment 1 Solutions 2.mp4", "079 [Build] Assignment 1 Solutions.html"], "title": "[Build] Assignment 1 Official Solutions Walkthrough (LangChain & LangFlow)", "cat": "Build", "type": "Solution", "mod": 7, "week": 3, "sol": 1},
    {"id": "057", "files": ["080 [Build] Assignment 2 - Using LangGraph.mp4", "081 [Build] Assignment 2 - Using LangGraph.html"], "title": "[Build] Assignment 2: Perplexia AI Part 2 - LangGraph RAG & Web Search", "cat": "Build", "type": "Assignment", "mod": 7, "week": 3, "assign": 2},
    {"id": "058", "files": ["082 [Build] Assignment 2 - Using LangFlow.html", "083 [Build] Assignment 2 - Using LangFlow.mp4"], "title": "[Build] Assignment 2: Perplexia AI Part 2 - LangFlow Visual RAG", "cat": "Build", "type": "Assignment", "mod": 7, "week": 3, "assign": 2},
    {"id": "059", "files": ["084 [Build] Tavily Setup.html"], "title": "[Build] Tavily Web Search API Setup & Configuration Guide", "cat": "Build", "type": "Tutorial", "mod": 7, "week": 3},
    {"id": "060", "files": ["085 [Build] Assignment 2 - Test Cases.html"], "title": "[Build] Assignment 2 Benchmark Test Cases (Doc Retrieval & Live Search)", "cat": "Build", "type": "Assignment", "mod": 7, "week": 3, "assign": 2},
    {"id": "061", "files": ["086 [Build] Comet Opik Setup (ONLY for LangChainLangGraph users).mp4", "087 [Build] Comet Opik Setup (ONLY for LangChainLangGraph users).html"], "title": "[Build] Comet Opik Observability Setup & Tracing for LangGraph", "cat": "Build", "type": "Tutorial", "mod": 7, "week": 3},
    {"id": "062", "files": ["088 [Build] Running Into Issues Start Here.html"], "title": "[Build] Week 3 Troubleshooting Guide: RAG Ingestion & API Limits", "cat": "Build", "type": "Tutorial", "mod": 7, "week": 3},
    {"id": "063", "files": ["089 AI and the Future of Software Development A Sneak Peek [Pritika Mehta].mp4", "090 Notes for_ AI and the Future of Software Development_ A Sneak Peek [Pritika Mehta].docx"], "title": "Guest Lecture: AI & Future of Software Development [Pritika Mehta]", "cat": "Grow", "type": "Guest Lecture", "mod": 7, "week": 3},
    {"id": "064", "files": ["091 Week 3 Homework Office Hours - Aug 13.mp4", "092 Week 3 Homework Office Hours - August 13.docx"], "title": "Week 3 Homework Office Hours (Aug 13): CRAG Routing & Chunking", "cat": "Office Hours", "type": "Office Hours", "mod": 7, "week": 3},
    {"id": "065", "files": ["093 AMA w Jaya Gupta (Partner, Foundation Capital).mp4"], "title": "AMA Session: Venture Capital & AI Startup Landscape [Jaya Gupta, Foundation Capital]", "cat": "AMA", "type": "AMA", "mod": 7, "week": 3},
    {"id": "066", "files": ["094 Week 3 Content Office Hours - Aug 15.mp4", "095 Week 3 Content Office Hours - August 14.docx"], "title": "Week 3 Content Office Hours (Aug 14/15): Evaluation Datasets & Vector Stores", "cat": "Office Hours", "type": "Office Hours", "mod": 7, "week": 3},
    {"id": "067", "files": ["096 Week 3 Content Office Hours - Aug 16.mp4", "097 Week 3 Content Office Hours - August 16.docx"], "title": "Week 3 Content Office Hours (Aug 16): Multimodal Embeddings & Context Windows", "cat": "Office Hours", "type": "Office Hours", "mod": 7, "week": 3},
    {"id": "068", "files": ["098 Week 3 Homework Office Hours - Aug 16.mp4", "099 Week 3 Homework Office Hours - August 16.docx"], "title": "Week 3 Homework Office Hours (Aug 16): Assignment 2 Debugging & Submission", "cat": "Office Hours", "type": "Office Hours", "mod": 7, "week": 3},

    # Module 8: Autonomous Agents, Planning Protocols & Multi-Agent Systems (100 - 116)
    {"id": "069", "files": ["100 [Core] Types of Agents & AI Protocols.html", "101 [Core] Types of Agents & AI Protocols.mp4"], "title": "[Core] Lecture 7: Types of Agents & AI Protocols (Level 1 to Level 5, MCP, A2A)", "cat": "Core", "type": "Core Lecture", "mod": 8, "week": 4},
    {"id": "070", "files": ["102 [Core] Planning in Agents (ReAct Prompting).html"], "title": "[Core] Lecture 8: Planning in Agents (ReAct, Plan-and-Solve & Reflection)", "cat": "Core", "type": "Core Lecture", "mod": 8, "week": 4},
    {"id": "071", "files": ["103 [Core] Multi-Agent Systems, AIOps & Fine-Tuning.html", "104 [Core] Multi-Agent Systems, AIOps & Fine-Tuning.mp4"], "title": "[Core] Lecture 9: Multi-Agent Systems, AIOps & Fine-Tuning Decisions", "cat": "Core", "type": "Core Lecture", "mod": 8, "week": 4},
    {"id": "072", "files": ["105 [Grow] Ambient Agents, Background Agents, Sub-Agents and More!.html"], "title": "[Grow] Advanced Agent Topologies: Ambient, Background & Asynchronous Sub-Agents", "cat": "Grow", "type": "Deep Dive", "mod": 8, "week": 4},
    {"id": "073", "files": ["106 [Grow] Recorded Guest Lecture on Agent Evaluation.html", "107 [Grow] Recorded Guest Lecture on Agent Evaluation.mp4"], "title": "[Grow] Guest Lecture: Rigorous Agent Evaluation & Trajectory Benchmarking", "cat": "Grow", "type": "Guest Lecture", "mod": 8, "week": 4},
    {"id": "074", "files": ["108 [Grow] Deep Dive on Multi-Agent Design Patterns.html"], "title": "[Grow] Multi-Agent Design Patterns: Router, Supervisor, Hierarchical & Swarm", "cat": "Grow", "type": "Deep Dive", "mod": 8, "week": 4},
    {"id": "075", "files": ["109 [Grow] A Real-World Multi-Agent System Google's AI Co-Scientist.html"], "title": "[Grow] Case Study: Google AI Co-Scientist Multi-Agent Architecture", "cat": "Grow", "type": "Deep Dive", "mod": 8, "week": 4},
    {"id": "076", "files": ["110 [Grow] Enterprise Use Cases For Agents (Level 1 & Level 2).html"], "title": "[Grow] Enterprise Use Cases for Level 1 & Level 2 Agents", "cat": "Grow", "type": "Deep Dive", "mod": 8, "week": 4},
    {"id": "077", "files": ["111 [Grow] How, When & When Not to Build Level 2 Agents in Enterprise (A Deep Dive).html"], "title": "[Grow] Strategic Decision Framework: When and When NOT to Build Level 2 Agents", "cat": "Grow", "type": "Deep Dive", "mod": 8, "week": 4},
    {"id": "078", "files": ["112 [Grow] The AI Agent Stack + Players!.html"], "title": "[Grow] The 2025 AI Agent Technology Stack: Frameworks, Compute & Observability", "cat": "Grow", "type": "Reference Material", "mod": 8, "week": 4},
    {"id": "079", "files": ["113 [Grow] A Deep Dive on Agent EvalsMonitoring.html"], "title": "[Grow] Production Monitoring & Evals for Agents: Opik, Langfuse & Tracing", "cat": "Grow", "type": "Deep Dive", "mod": 8, "week": 4},
    {"id": "080", "files": ["114 [Grow] A Deep Dive on Agent Protocols & Best Resources.html"], "title": "[Grow] Deep Dive on Open Agent Protocols (Model Context Protocol & Google A2A)", "cat": "Grow", "type": "Deep Dive", "mod": 8, "week": 4},
    {"id": "081", "files": ["115 [Grow] A 101 Fine-Tuning Guide.html"], "title": "[Grow] Fine-Tuning 101: SFT, LoRA, QLoRA & DPO for Specialized Models", "cat": "Grow", "type": "Deep Dive", "mod": 8, "week": 4},
    {"id": "082", "files": ["116 [Grow] Data Generation for Fine-Tuning & Synthetic Data.html"], "title": "[Grow] Synthetic Data Generation & Distillation Pipelines for Model Training", "cat": "Grow", "type": "Deep Dive", "mod": 8, "week": 4},

    # Module 9: Assignment 3, MCP Protocols & Week 4 Execution (117 - 135)
    {"id": "083", "files": ["117 [Build] Assignment 2 Solutions 1.mp4", "118 [Build] Assignment 2 Solutions 2.mp4", "119 [Build] Assignment 2 Solutions.html"], "title": "[Build] Assignment 2 Official Solutions Walkthrough (LangGraph & LangFlow)", "cat": "Build", "type": "Solution", "mod": 9, "week": 4, "sol": 2},
    {"id": "084", "files": ["120 [Build] Assignment 3 - Using LangGraph.html", "121 [Build] Assignment 3 - Using LangGraph.mp4"], "title": "[Build] Assignment 3: Perplexia AI Part 3 - Autonomous Agents & Deep Research (LangGraph)", "cat": "Build", "type": "Assignment", "mod": 9, "week": 4, "assign": 3},
    {"id": "085", "files": ["122 [Build] Assignment 3 - Using LangFlow.html"], "title": "[Build] Assignment 3: Perplexia AI Part 3 - LangFlow Multi-Agent Workflows", "cat": "Build", "type": "Assignment", "mod": 9, "week": 4, "assign": 3},
    {"id": "086", "files": ["123 Building Agentic AI Applications with a Problem-First Approach.mp4"], "title": "Building Agentic AI Applications with a Problem-First Approach (Special Session)", "cat": "Core", "type": "Lecture", "mod": 9, "week": 4},
    {"id": "087", "files": ["124 [Build][Bonus] Using and building MCP.html", "125 [Build][Bonus] Using and building MCP.mp4"], "title": "[Build][Bonus] Building and Integrating Model Context Protocol (MCP) Servers", "cat": "Build", "type": "Workshop", "mod": 9, "week": 4},
    {"id": "088", "files": ["126 Stuck Start Here.html"], "title": "[Build] Week 4 Troubleshooting Guide: Agent Loops & State Management", "cat": "Build", "type": "Tutorial", "mod": 9, "week": 4},
    {"id": "089", "files": ["127 AI Strategy in Action A Leader’s Playbook for Real-World Results [Gabriela de Queiroz].mp4", "128 AI Strategy in Action A Leader’s Playbook for Real-World Results [Gabriela de Queiroz].html", "129 Notes from_ AI Strategy in Action_ A Leader’s Playbook for Real-World Results [Gabriela De Queiroz].docx"], "title": "Guest Lecture: AI Strategy in Action - A Leader's Playbook [Gabriela de Queiroz, Microsoft]", "cat": "Grow", "type": "Guest Lecture", "mod": 9, "week": 4},
    {"id": "090", "files": ["130 Week 4 Homework Office Hours -  Aug 20.mp4", "131 Week 4 Homework Office Hours - August 20.docx"], "title": "Week 4 Homework Office Hours (Aug 20): Deep Research & StateGraph", "cat": "Office Hours", "type": "Office Hours", "mod": 9, "week": 4},
    {"id": "091", "files": ["132 AMA w Rachitt Shah (Applied AI Consultant).mp4", "133 AMA w_ Rachitt Shah (Applied AI Consultant) - August 21.docx"], "title": "AMA Session: Production AI Consulting & Client Engagements [Rachitt Shah]", "cat": "AMA", "type": "AMA", "mod": 9, "week": 4},
    {"id": "092", "files": ["134 Week 4 Content Office Hours - Aug 22.mp4", "135 Week 4 Content Office Hours - August 21.docx"], "title": "Week 4 Content Office Hours (Aug 21/22): Agent Protocols & Production Pitfalls", "cat": "Office Hours", "type": "Office Hours", "mod": 9, "week": 4},

    # Module 10: Capstone Project, Enterprise Playbooks & Production (136 - 151 + Students Archive)
    {"id": "093", "files": ["136 Final Lecture (Aish + Kiriti).mp4", "137 Final Lecture (Aish + Kiriti) Slides.txt"], "title": "Final Lecture: System Synthesis, Career Next Steps & The Road Ahead [Aishwarya & Kiriti]", "cat": "Core", "type": "Core Lecture", "mod": 10, "week": 4},
    {"id": "094", "files": ["138 Week 4 Homework Office Hours - Aug 23.mp4"], "title": "Week 4 Homework Office Hours (Aug 23): Assignment 3 Final Wrap-Up", "cat": "Office Hours", "type": "Office Hours", "mod": 10, "week": 4},
    {"id": "095", "files": ["139 Capstone Brainstorming Workshop - Aug 24.mp4"], "title": "Capstone Brainstorming Workshop (Aug 24): Scoping & Team Breakouts", "cat": "Capstone / Project", "type": "Workshop", "mod": 10, "week": 4},
    {"id": "096", "files": ["140 Capstone Overview.html"], "title": "Capstone Overview: Iterative AI System Design Challenge", "cat": "Capstone / Project", "type": "Project", "mod": 10, "week": 4},
    {"id": "097", "files": ["141 Getting Started Capstone Guidelines.html"], "title": "Getting Started: Capstone Guidelines, Team Roles & Rubric", "cat": "Capstone / Project", "type": "Project", "mod": 10, "week": 4},
    {"id": "098", "files": ["142 Step 1 Scoping Your Project (ScratchPad).html"], "title": "Capstone Step 1: Problem Scoping, Target Audience & Constraints", "cat": "Capstone / Project", "type": "Project", "mod": 10, "week": 4},
    {"id": "099", "files": ["143 Step 2 Iterative Solution Design (ScratchPad) & Poster Design.html"], "title": "Capstone Step 2: Iterative Solution Design, Architecture & Poster Presentation", "cat": "Capstone / Project", "type": "Project", "mod": 10, "week": 4},
    {"id": "100", "files": ["144 Prompt Optimizations For The Enterprise.html"], "title": "Enterprise Playbook: Advanced Prompt Optimizations & Caching", "cat": "Grow", "type": "Reference Material", "mod": 10, "week": 4},
    {"id": "101", "files": ["145 RAG Optimizations For The Enterprise.html"], "title": "Enterprise Playbook: Production RAG Optimizations (HyDE, Re-Ranking, Self-RAG)", "cat": "Grow", "type": "Reference Material", "mod": 10, "week": 4},
    {"id": "102", "files": ["146 Level 2 Agents Resources For The Enterprise.html"], "title": "Enterprise Playbook: Level 2 Agent Deployment Patterns & Tool Sandboxing", "cat": "Grow", "type": "Reference Material", "mod": 10, "week": 4},
    {"id": "103", "files": ["147 Evaluation Metrics.html"], "title": "Enterprise Metrics: Quality & Evaluation Metrics Framework (RAGAS, Tracing)", "cat": "Grow", "type": "Reference Material", "mod": 10, "week": 4},
    {"id": "104", "files": ["148 Operational Metrics.html"], "title": "Enterprise Metrics: Operational Metrics (Latency, Token Economics, Error Rates)", "cat": "Grow", "type": "Reference Material", "mod": 10, "week": 4},
    {"id": "105", "files": ["149 [Build] Assignment 3 Solutions 1.mp4", "150 [Build] Assignment 3 Solutions 2.mp4", "151 [Build] Assignment 3 Solutions.html"], "title": "[Build] Assignment 3 Official Solutions Walkthrough (LangGraph Deep Research & MCP)", "cat": "Build", "type": "Solution", "mod": 10, "week": 4, "sol": 3},
    {"id": "106", "files": ["Cohort 3 - Students.zip"], "title": "Student Code & Starter Artifacts Archive: Complete Perplexia AI Codebase", "cat": "Build", "type": "Code Archive", "mod": 10, "week": 4}
]

# Verify all 152 files are accounted for
accounted_files = set()
for item in groups_def:
    for f in item["files"]:
        if f in accounted_files:
            print(f"ERROR: Duplicate assignment of file: {f}")
        accounted_files.add(f)

all_files_set = set(files)
missing = all_files_set - accounted_files
extra = accounted_files - all_files_set

print(f"Total files in directory: {len(all_files_set)}")
print(f"Total files accounted for: {len(accounted_files)}")
print(f"Missing files: {missing}")
print(f"Extra files: {extra}")

if not missing and not extra:
    print("PERFECT 100% ACCOUNTABILITY: All 152 files mapped to exactly 106 logical lessons!")

with open('scratch/logical_lessons.json', 'w', encoding='utf-8') as f:
    json.dump(groups_def, f, indent=2, ensure_ascii=False)

print("Saved scratch/logical_lessons.json successfully.")
