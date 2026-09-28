import os, sys, json

sys.stdout.reconfigure(encoding='utf-8')

KB_ROOT = r'c:\Users\anurag\Desktop\notes\COURSE_KNOWLEDGE_BASE'
GROUPS_DIR = os.path.join(KB_ROOT, 'Lesson_Groups')
os.makedirs(GROUPS_DIR, exist_ok=True)

modules = [
    {
        "id": "01",
        "folder": "01-Orientation-and-Tooling-Setup",
        "lessons_range": "Lessons 001–009",
        "topic": "Course Orientation, Development Environment & Developer Tooling",
        "big_picture": "Establishes the developer workspace and technological baseline. Before writing agent code, students configure Python/Conda environments, compare visual graph builders (LangFlow) with code orchestration (LangChain), and configure modern AI productivity amplifiers (Cursor AI, NotebookLM, Vercel v0).",
        "flow": "Welcome & Course Roadmap (001) → Hands-on Tracks Intro (002) → Conda & API Setup (003) → LangChain Code Setup (004) → LangFlow Visual Setup (005) → NotebookLM Technical Synthesis (006) → Model/Agent Selection Framework (007) → Cursor AI Coding (008) → Vercel v0 Frontend (009)",
        "flow_explanation": "You start by understanding what the course demands (001-002), establish local dependencies and API keys (003), install the two core execution tracks: LangChain code and LangFlow visual UI (004-005), and equip yourself with an AI-augmented toolkit for analysis and coding (006-009).",
        "key_ideas": [
            "Problem-First mindset: Match tool complexity to actual user requirements.",
            "Dual-track flexibility: Code (LangChain/LangGraph) vs Visual (LangFlow). Both produce equivalent functional architectures.",
            "AI-augmented development: Using Cursor AI and NotebookLM drastically compresses debugging and comprehension cycles.",
            "Environment cleanliness: Isolate API keys, virtual environments, and package versions to avoid dependency hell."
        ],
        "fit_together": "This module provides the operational launchpad. Every future assignment and core lecture builds upon the Python packages, visual environments, and workflow patterns configured here.",
        "should_know": [
            "How to create and manage isolated Conda environments for LangChain and LangGraph.",
            "How to build, test, and export a visual flow in LangFlow.",
            "How to structure an LCEL (LangChain Expression Language) pipeline in Python.",
            "When to choose simple prompt completion versus agentic tool execution."
        ],
        "assignments": [
            "Environment Verification: Successfully run LangFlow locally and test an OpenAI API completion in Python."
        ],
        "resources": [
            "[LangChain Documentation](https://python.langchain.com/docs/introduction/)",
            "[LangFlow Repository](https://github.com/langflow-ai/langflow)",
            "[NotebookLM Setup Guide](https://notebooklm.google.com/notebook/941996fc-c025-4da7-b3f1-854675e742a4)"
        ]
    },
    {
        "id": "02",
        "folder": "02-Generative-AI-Foundations-and-Iterative-Design",
        "lessons_range": "Lessons 010–017",
        "topic": "Generative AI Foundations & Problem-First Iterative Solution Design",
        "big_picture": "Lays the theoretical and strategic foundation of the entire curriculum. Instructors Aishwarya and Kiriti teach students how to systematically dissect business problems, avoid over-engineering with unnecessary agents, and design applications through disciplined evolutionary iterations.",
        "flow": "Core Lecture 1: GenAI & Agentic AI Evolution (010) → Core Lecture 2: Iterative Solution Design (011) → Core AI Terminology & Taxonomy (012) → Enterprise Adoption & ROI Trends (013) → Neural Networks & Transformer Architecture (014) → Reasoning Models: DeepSeek-R1 & o1 (015) → LLM Performance Benchmarks (016) → Cohort Demo Day Retrospective (017)",
        "flow_explanation": "Lecture 1 demystifies how models work and how agents differ from raw LLMs. Lecture 2 introduces the signature 'Problem-First Iterative Solution Design' framework. The accompanying deep dives (012-017) reinforce model mechanics, reasoning paradigms (DeepSeek-R1), and historical student capstone blueprints.",
        "key_ideas": [
            "The Input/Output Framework: Determine whether a task requires deterministic logic, structured extraction, or creative generation.",
            "Iterative Solution Design: Never start at full autonomy. Start at Iteration 1 (deterministic/rule-based), proceed to Iteration 2 (RAG/routing), and graduate to Iteration 3 (autonomous agents).",
            "Reasoning models (o1, DeepSeek-R1) shift compute from pre-training to test-time inference (Chain-of-Thought scaling).",
            "Enterprise ROI: Systems succeed by delivering reliability, explainability, and measurable task compression, not raw novelty."
        ],
        "fit_together": "This module provides the architectural philosophy that governs Assignments 1, 2, and 3 (the evolution of Perplexia AI) and serves as the exact grading rubric for the Capstone Project.",
        "should_know": [
            "The difference between pre-training, instruction fine-tuning, and alignment (RLHF/DPO).",
            "How to structure a problem using the 3-Iteration Solution Design matrix.",
            "How to evaluate models against standard benchmarks (MMLU, HumanEval, BBH).",
            "Why reasoning models behave fundamentally differently under chain-of-thought prompting."
        ],
        "assignments": [
            "Capstone Scoping Preparation: Select a domain problem and draft a preliminary 3-iteration roadmap."
        ],
        "resources": [
            "[Lecture 1 Slides (Canva)](https://www.canva.com/design/DAGoUUTEpbs/NXxopOVFMSm1iZbCuNxj6g/view?utm_content=DAGoUUTEpbs&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he4d79a534f)",
            "[Lecture 2 Slides (Canva)](https://www.canva.com/design/DAGoUc2S-yQ/leXWaQalpwbHf0TYrDSVcA/view?utm_content=DAGoUc2S-yQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h560440b0f0)"
        ]
    },
    {
        "id": "03",
        "folder": "03-Week-1-Office-Hours-and-Troubleshooting",
        "lessons_range": "Lessons 018–022",
        "topic": "Applied Problem Scoping, Architecture Feasibility & Live Troubleshooting",
        "big_picture": "Connects theoretical system design to reality. Through four intensive office hours and community Q&A, students debug early pipeline issues, discuss component selection in LangFlow, and receive direct instructor feedback on scoping their capstone problems.",
        "flow": "Homework Office Hours (July 30): Component Selection (018) → Content Office Hours (July 31): Scoping & Framing (019) → Content Office Hours (Aug 2): Enterprise Feasibility (020) → Homework Office Hours (Aug 2): Pipeline Troubleshooting (021) → Chai & AI Community Networking (022)",
        "flow_explanation": "Students clarify which components belong in basic flows (018), pressure-test their enterprise use cases against hallucination risks (019-020), and resolve environment and LangFlow execution bugs (021) ahead of Week 2 implementation.",
        "key_ideas": [
            "Component selection discipline: Basic conversational flows require only four core nodes (Prompt, Model, Tools, Memory).",
            "Scoping discipline: Narrowing the business problem is 80% of system design; broad, open-ended agents invariably fail.",
            "Handling API limits and local execution crashes: Using local fallbacks and proper environment variable injection."
        ],
        "fit_together": "Eliminates onboarding friction and ensures every student is conceptually prepared to tackle prompt engineering and workflow agents in Week 2.",
        "should_know": [
            "How to structure a clean LangFlow canvas without circular dependencies.",
            "How to critique an AI use case for enterprise feasibility and liability risks.",
            "Where to look when model calls fail or return empty tokens."
        ],
        "assignments": [
            "Finalize environment readiness for Assignment 1."
        ],
        "resources": [
            "[Week 1 Homework Notes (Transcribed Q&A)](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Lessons/018-Week-1-Homework-Office-Hours-July-30/summary.md)",
            "[Environment FAQ NotebookLM](https://notebooklm.google.com/notebook/941996fc-c025-4da7-b3f1-854675e742a4)"
        ]
    },
    {
        "id": "04",
        "folder": "04-Prompt-Engineering-and-Workflow-Agents",
        "lessons_range": "Lessons 023–034",
        "topic": "Modern Prompt Engineering, Structured Outputs & Enterprise Workflow Agents",
        "big_picture": "Transitioning from free-form prompting to deterministic software pipelines. This module covers advanced prompt engineering in 2025, structured JSON/Pydantic outputs, automatic prompt optimization (DSPy), and the architecture of Level 2 Workflow Agents that use deterministic code to route queries and call tools.",
        "flow": "Core Lecture 3: Prompt Engineering in 2025 (023) → Core Lecture 4: Enterprise Workflow Agents (024) → Skill-Based Prompting Deep Dive (025) → Automatic Prompt Optimization / DSPy (026) → Prompting Reasoning Models (027) → Prompt Engineering Papers (028) → Enterprise Workflow Architectures (029) → Workflow Evaluation (030) → LLM-as-a-Judge Masterclass (031) → Production Guardrails (032) → Model Context Protocol Intro (033) → Building Agentic AI in 2025 (034)",
        "flow_explanation": "Lecture 3 teaches precise model steering and structured outputs. Lecture 4 wraps those outputs into directed workflow chains. Deep dives (025-034) cover automated tuning (DSPy), reasoning model behavior, evaluation metrics (LLM-as-a-judge), safety guardrails, and standardize tools via MCP.",
        "key_ideas": [
            "Structured outputs are non-negotiable in production: Always enforce Pydantic/JSON schemas.",
            "Workflow Agents (Level 2) are deterministic: The LLM classifies intent, but hardcoded software routes the execution graph.",
            "Automated Prompt Optimization (DSPy): Compiling prompts algorithmically rather than manual trial-and-error.",
            "Guardrails: Layered defense comprising input validation (regex/PII), prompt guards, and output hallucination verifiers."
        ],
        "fit_together": "Provides the complete architectural blueprint for **Assignment 1** (Perplexia AI Part 1), where students build a routing agent with memory and tool binding.",
        "should_know": [
            "How to force OpenAI models to emit verified JSON adhering to a Pydantic model.",
            "How to construct a query routing chain in LangChain and LangFlow.",
            "How to design an LLM-as-a-judge prompt with clear rubrics to avoid scoring drift.",
            "The architectural role of Model Context Protocol (MCP) in tool discovery."
        ],
        "assignments": [
            "Prepare for Assignment 1: Design the classification prompt and tool interfaces for Perplexia AI."
        ],
        "resources": [
            "[Lecture 3 Slides (Canva)](https://www.canva.com/design/DAGosETX17k/uaZhBToUArMTGDOmJCIx2w/view?utm_content=DAGosETX17k&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h4e96cc3f6b)",
            "[Lecture 4 Slides (Canva)](https://www.canva.com/design/DAGo44zNruc/geNXs6giP4l7HoiAWbTabA/view?utm_content=DAGo44zNruc&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h343ac51335)"
        ]
    },
    {
        "id": "05",
        "folder": "05-Assignment-1-and-Week-2-Execution",
        "lessons_range": "Lessons 035–043",
        "topic": "Assignment 1 Implementation: Building Perplexia AI Part 1 & Enterprise Lifecycle",
        "big_picture": "Hands-on execution of Assignment 1. Students implement the Perplexia AI router, custom tools, and conversational state in either LangChain or LangFlow. Supported by guest lectures from Microsoft enterprise practitioners and rigorous office hours addressing state management.",
        "flow": "Assignment 1 LangChain Specs (035) → Assignment 1 LangFlow Specs (036) → Test Cases Benchmark (037) → Troubleshooting & FAQ (038) → Homework Office Hours (Aug 6): Memory & Routing (039) → Content Office Hours (Aug 7/8): Structured Prompts (040) → Guest Lecture: Agent Development Lifecycle [Sam Julien & Ugo Osuji] (041) → Content Office Hours (Aug 9): Guardrails (042) → Homework Office Hours (Aug 9): Final Submissions (043)",
        "flow_explanation": "Students review assignment specifications and test cases (035-037), resolve execution hurdles using the FAQ (038), receive debugging support in office hours (039-040, 042-043), and gain enterprise perspective on production agent lifecycles from Microsoft leaders (041).",
        "key_ideas": [
            "Router accuracy: Ensuring edge-case math queries route to tools while conversational prompts retain memory.",
            "Stateful memory injection: Injecting conversation history dynamically via `RunnableWithMessageHistory` without exceeding token limits.",
            "Enterprise agent lifecycle: The shift from prototyping to versioning, continuous evaluation, and telemetry.",
            "Graceful degradation: Catching tool errors and allowing the LLM to explain failures cleanly."
        ],
        "fit_together": "Successfully produces the working v1 baseline of Perplexia AI, ready to receive knowledge integration in Week 3.",
        "should_know": [
            "How to pass all 5 benchmark test cases in Assignment 1.",
            "How to manage chat session IDs and persist memory across turns.",
            "How Microsoft approaches enterprise agent lifecycle governance and deployment."
        ],
        "assignments": [
            "Complete and submit **Assignment 1** (Perplexia AI Part 1)."
        ],
        "resources": [
            "[Assignment 1 Workspace](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-LangChain-and-LangFlow-Basics/README.md)",
            "[Starter Drive Folder](https://drive.google.com/drive/folders/1TiWFMDmrta6NKQgSA7Vv3jlM0Y1pflOw?usp=sharing)"
        ]
    },
    {
        "id": "06",
        "folder": "06-Enterprise-RAG-Memory-and-Context-Engineering",
        "lessons_range": "Lessons 044–055",
        "topic": "Enterprise RAG Architecture, Agent Memory Mechanisms & Context Engineering",
        "big_picture": "Mastering the knowledge foundation of enterprise AI. Moving far beyond naive vector search, this module covers production RAG pipelines, semantic chunking, HyDE query expansion, Corrective RAG (CRAG), GraphRAG, and long-term agent memory architectures.",
        "flow": "Core Lecture 5: Enterprise RAG in 2025 (044) → Core Lecture 6: Advanced RAG & Memory (045) → Core Lecture: Context Engineering (046) → Enterprise RAG Guest Lectures (047) → Vector Databases Deep Dive (048) → RAG Evaluation Metrics & Ragas (049) → RAG Optimizations: Semantic Caching & CRAG (050) → Multimodal RAG (051) → GraphRAG Deep Dive (052) → Reading RAG Papers (053) → Agent Memory Frameworks (054) → Landmark Memory Papers: Reflexion & MemGPT (055)",
        "flow_explanation": "Lecture 5 details the end-to-end RAG pipeline and retrieval mathematics. Lecture 6 introduces advanced CRAG and memory structures. Lecture 7 (Context Engineering) optimizes context window attention. The deep dives (047-055) cover vector stores (HNSW), evaluation metrics (Ragas), knowledge graphs (GraphRAG), and episodic memory architectures.",
        "key_ideas": [
            "Garbage In, Garbage Out: Document parsing and chunking quality dictates 80% of RAG accuracy.",
            "Corrective RAG (CRAG): Ingested documents must be evaluated for relevance before generation; if inadequate, fallback to web search.",
            "Hybrid Search: Combining dense semantic embeddings with sparse keyword BM25 to capture both concepts and exact acronyms/IDs.",
            "Agent Memory Hierarchy: Working context (short-term) vs episodic reflection (medium-term) vs vector user profiles (long-term).",
            "Context window budgeting: Attention degrades over large contexts ('lost in the middle'); prune and prioritize high-signal tokens."
        ],
        "fit_together": "Establishes the technical foundation for **Assignment 2** (Perplexia AI Part 2), where students implement CRAG routing and document search in LangGraph.",
        "should_know": [
            "How to calculate and interpret Ragas metrics (Context Precision, Recall, Faithfulness).",
            "How the HyDE algorithm generates hypothetical answers to bridge query-document semantic gaps.",
            "How GraphRAG extracts entities to answer global corpus-wide questions.",
            "How memory reflection works in the Reflexion framework."
        ],
        "assignments": [
            "Prepare for Assignment 2: Ingest the annual performance report PDFs and configure vector embeddings."
        ],
        "resources": [
            "[Lecture 5 Slides (Canva)](https://www.canva.com/design/DAGpcmXbA04/t7rqjR4Gzi19GjA0XUN4_Q/view?utm_content=DAGpcmXbA04&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h9d21093bd3)",
            "[Lecture 6 Slides (Canva)](https://www.canva.com/design/DAGpn4N8zs4/9V9Q_vg5v62jpLnbXks30g/view?utm_content=DAGpn4N8zs4&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h143e1b5d76)",
            "[CRAG Research Paper](https://arxiv.org/abs/2401.15884)"
        ]
    },
    {
        "id": "07",
        "folder": "07-Assignment-2-and-Week-3-Execution",
        "lessons_range": "Lessons 056–068",
        "topic": "Assignment 2 Implementation: Corrective RAG (CRAG), Tavily Search & LangGraph",
        "big_picture": "Implementing Perplexia AI Part 2. Students construct a cyclic LangGraph StateGraph combining internal PDF knowledge retrieval, relevance evaluation, and live web search fallbacks via Tavily. Accompanied by Assignment 1 solution walkthroughs, Comet Opik tracing setup, venture capital AMAs, and intensive office hours.",
        "flow": "Assignment 1 Solutions (056) → Assignment 2 LangGraph Specs (057) → Assignment 2 LangFlow Specs (058) → Tavily Search Setup (059) → Assignment 2 Test Cases (060) → Comet Opik Observability (061) → Troubleshooting Guide (062) → Guest Lecture: AI Future [Pritika Mehta] (063) → Homework Office Hours (Aug 13): CRAG Routing (064) → AMA: VC Landscape [Jaya Gupta] (065) → Content Office Hours (Aug 14/15): Evaluation (066) → Content Office Hours (Aug 16): Multimodal (067) → Homework Office Hours (Aug 16): Finalizing A2 (068)",
        "flow_explanation": "Students review the Assignment 1 solution (056) to ensure solid footing, follow specifications for Assignment 2 (057-060), set up observability with Comet Opik (061), and resolve StateGraph routing challenges during live office hours (064, 066-068).",
        "key_ideas": [
            "Cyclic execution in LangGraph: Managing nodes, state transitions, and conditional edge decisions.",
            "Relevance evaluator node: Grading document chunks and setting boolean flags (`web_search=True`).",
            "Tavily Search API: Fetching clean, LLM-optimized web snippets to answer questions beyond internal documentation.",
            "Observability with Comet Opik: Tracing token expenditure across multi-node LangGraph runs."
        ],
        "fit_together": "Elevates Perplexia AI from a calculator bot to an enterprise research engine, providing the exact state graph patterns needed for Assignment 3.",
        "should_know": [
            "How to define typed dictionaries (`AgentState`) for LangGraph execution.",
            "How to write deterministic conditional routing functions in LangGraph.",
            "How to pass all Assignment 2 test cases across internal documents and live web search.",
            "How venture capital evaluates generative AI startups and defensibility."
        ],
        "assignments": [
            "Complete and submit **Assignment 2** (Perplexia AI Part 2)."
        ],
        "resources": [
            "[Assignment 2 Workspace](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Enterprise-RAG-and-Tavily-Search/README.md)",
            "[PDF Dataset Folder](https://drive.google.com/drive/folders/1h-g9aBIa9FWX6Afe2NCxzVkdusokmJpY?usp=sharing)"
        ]
    },
    {
        "id": "08",
        "folder": "08-Autonomous-Agents-Planning-and-Multi-Agent-Systems",
        "lessons_range": "Lessons 069–082",
        "topic": "Autonomous Agents, Dynamic Planning Protocols, Multi-Agent Systems & Fine-Tuning",
        "big_picture": "Transitioning to true agentic autonomy. Students explore dynamic ReAct planning loops, open protocols (Model Context Protocol and Google A2A), multi-agent orchestration topologies (Supervisor, Router, Swarm), and production AIOps/fine-tuning decision frameworks.",
        "flow": "Core Lecture 7: Types of Agents & Protocols (069) → Core Lecture 8: Planning in Agents (070) → Core Lecture 9: Multi-Agent Systems & Fine-Tuning (071) → Ambient & Sub-Agents (072) → Agent Evaluation Guest Lecture (073) → Multi-Agent Design Patterns (074) → Google AI Co-Scientist Case Study (075) → Enterprise Agent Use Cases (076) → When NOT to Build Level 2 Agents (077) → AI Agent Tech Stack (078) → Agent Monitoring Deep Dive (079) → Open Protocols (MCP & A2A) (080) → Fine-Tuning 101 Guide (081) → Synthetic Data Generation (082)",
        "flow_explanation": "Lecture 7 defines autonomy levels and MCP. Lecture 8 deconstructs ReAct and planning. Lecture 9 explores multi-agent collaboration and fine-tuning. The deep dives (072-082) provide architectural patterns (Supervisor pattern, Google Co-Scientist), evaluation methodologies, and fine-tuning guides (LoRA/QLoRA).",
        "key_ideas": [
            "Level 3 vs Level 4 Autonomy: Single agent with tools vs multiple specialized agents collaborating over structured protocols.",
            "ReAct loop mechanics: Generating thoughts, executing actions, observing tool outputs, and looping until completion.",
            "Model Context Protocol (MCP): The USB-C of AI systems—standardizing tool exposure across agents and platforms.",
            "The Build vs Buy vs Fine-Tune Matrix: Prompt first, augment with RAG second, fine-tune only when task form/style must be permanently encoded.",
            "Multi-Agent Supervisor Pattern: Central coordinator agent delegates sub-tasks to specialized worker agents."
        ],
        "fit_together": "Provides the complete architectural theory for **Assignment 3** (Autonomous Deep Research Agent & MCP integration).",
        "should_know": [
            "The anatomy and message flow of the Model Context Protocol (Host-Client-Server).",
            "How to structure an autonomous ReAct loop without entering infinite execution cycles.",
            "How to build a multi-agent supervisor graph in LangGraph.",
            "When fine-tuning is required versus when in-context RAG is superior."
        ],
        "assignments": [
            "Prepare for Assignment 3: Explore the MCP server examples and review the LangGraph multi-agent architecture."
        ],
        "resources": [
            "[Lecture 7 Slides (Canva)](https://www.canva.com/design/DAGp-2A7DJo/37WmsnH5e5Kya6oFpaItSw/view?utm_content=DAGp-2A7DJo&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h15c38d0fd4)",
            "[Lecture 9 Slides (Canva)](https://www.canva.com/design/DAGp_pzQIlM/vssS92mY1AzvB2T2Hk-C0g/view?utm_content=DAGp_pzQIlM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he4c0fa00a7)",
            "[ReAct Paper (arXiv:2210.03629)](https://arxiv.org/abs/2210.03629)"
        ]
    },
    {
        "id": "09",
        "folder": "09-Assignment-3-MCP-and-Week-4-Execution",
        "lessons_range": "Lessons 083–092",
        "topic": "Assignment 3 Implementation: Autonomous Agents, Deep Research & MCP",
        "big_picture": "Culminating coding milestone. Students build Perplexia AI Part 3—a fully autonomous multi-agent Deep Research platform and custom MCP server. Supported by Assignment 2 solution analysis, bonus MCP workshops, applied AI consulting AMAs, and enterprise strategy masterclasses.",
        "flow": "Assignment 2 Solutions (083) → Assignment 3 LangGraph Specs (084) → Assignment 3 LangFlow Specs (085) → Special Session: Building Agentic AI (086) → Bonus MCP Workshop (087) → Week 4 Troubleshooting (088) → Guest Lecture: AI Strategy [Gabriela de Queiroz] (089) → Homework Office Hours (Aug 20): StateGraph & Deep Research (090) → AMA: Applied AI Consulting [Rachitt Shah] (091) → Content Office Hours (Aug 21/22): Production Pitfalls (092)",
        "flow_explanation": "Students review Assignment 2 solutions (083), dive into Assignment 3 specifications for autonomous agents and deep research (084-085), learn how to write custom MCP servers (087), and resolve complex LangGraph state bugs in office hours (090, 092).",
        "key_ideas": [
            "Autonomous Tool Calling: Transitioning from rigid routers to `bind_tools` with dynamic LLM planning.",
            "Building custom MCP servers: Creating FastMCP services and exposing endpoints to LangGraph agents.",
            "Deep Research Multi-Agent Graph: Orchestrating Planner, Searcher, Fact-Checker, and Report Writer sub-graphs.",
            "Loop guardrails: Implementing recursion limits and cycle detection to safeguard production token budgets."
        ],
        "fit_together": "Completes the technical implementation of Perplexia AI, equipping students with state-of-the-art agent engineering skills.",
        "should_know": [
            "How to implement a custom MCP server in Python and consume it from a LangGraph agent.",
            "How to construct a multi-agent Deep Research workflow that produces comprehensive, cited reports.",
            "How to debug state reconciliation and infinite loops in LangGraph.",
            "How enterprise consultants package and price AI solutions for corporate clients."
        ],
        "assignments": [
            "Complete and submit **Assignment 3** (Perplexia AI Part 3)."
        ],
        "resources": [
            "[Assignment 3 Workspace](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Agentic-Workflows-LangGraph-and-MCP/README.md)",
            "[Starter Drive Folder](https://drive.google.com/drive/folders/1nLPfsGQnqFNpfhocr1JcAU2g183LxDQV?usp=drive_link)",
            "[MCP Servers Repository](https://github.com/modelcontextprotocol/servers)"
        ]
    },
    {
        "id": "10",
        "folder": "10-Capstone-Project-Enterprise-Playbooks-and-Production",
        "lessons_range": "Lessons 093–106",
        "topic": "Final Synthesis, Enterprise Production Playbooks & Capstone Project",
        "big_picture": "The capstone culmination of the program. Students apply the Problem-First Methodology to design and present a production-scoped AI system across three evolutionary iterations. Backed by executive closing lectures, enterprise optimization playbooks (Prompting, RAG, Level 2 Agents), and complete student code archives.",
        "flow": "Final Closing Lecture [Aishwarya & Kiriti] (093) → Homework Office Hours (Aug 23): Course Wrap-Up (094) → Capstone Brainstorming Workshop (095) → Capstone Overview & Rubric (096) → Getting Started Guidelines & Roles (097) → Step 1: Scoping Scratchpad (098) → Step 2: Iterative Solution & Poster Design (099) → Enterprise Prompt Optimizations (100) → Enterprise RAG Optimizations (101) → Level 2 Agent Resources (102) → Evaluation Metrics Playbook (103) → Operational Metrics & Cost Modeling (104) → Assignment 3 Official Solutions (105) → Complete Student Codebase Archive (106)",
        "flow_explanation": "Instructors deliver the closing synthesis and career next steps (093). Students form teams and brainstorm capstone architectures (095-097), fill out the design scratchpad across Iterations 1-3 (098-099), apply enterprise playbooks on optimization, evaluation, and token economics (100-104), and reference final Assignment 3 solutions and full codebase archives (105-106).",
        "key_ideas": [
            "The Complete System Design Story: Connecting business problem to scoping, baseline architecture, knowledge augmentation, and autonomous agent loops.",
            "Quantitative evaluation: Demonstrating measurable improvements across iterations using Ragas and latency benchmarks.",
            "Operational Economics: Calculating token costs per query, P95 latency, and caching ROI before writing code.",
            "Technical Pitch Craft: Presenting complex AI architectures to executive and technical stakeholders using concise visual poster formats."
        ],
        "fit_together": "Transforms students from individual framework users into senior AI architects capable of designing, evaluating, and pitching production-grade enterprise AI systems.",
        "should_know": [
            "How to structure an end-to-end enterprise Agentic AI architecture proposal.",
            "How to estimate operational costs, token budgets, and latency for multi-agent systems.",
            "How to defend architectural decisions during executive Demo Day presentations.",
            "Where to find all reference code in the complete `Cohort 3 - Students.zip` archive."
        ],
        "assignments": [
            "Complete and present the **Capstone Project** on Demo Day."
        ],
        "resources": [
            "[Capstone Workspace](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Projects/Capstone-Iterative-AI-System-Design/README.md)",
            "[Canva Poster Presentation Template](https://www.canva.com/design/DAGiHqwmESM/ZjubxupUOPI1FoXXn_DL2w/edit?utm_content=DAGiHqwmESM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)",
            "[Final Lecture Slides (Canva)](https://www.canva.com/design/DAGw1VQ2JIo/64l5DYo1eevQNJpZG2_obg/view?utm_content=DAGw1VQ2JIo&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h1716795c5d)",
            "[Complete Perplexia Codebase Archive](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Lessons/106-Cohort-3-Students-Code-Archive/summary.md)"
        ]
    }
]

for mod in modules:
    mod_path = os.path.join(GROUPS_DIR, mod["folder"])
    os.makedirs(mod_path, exist_ok=True)
    
    synth_lines = []
    synth_lines.append(f"# Module / Lesson Group {mod['id']}\n")
    synth_lines.append(f"## {mod['lessons_range']}: {mod['topic']}\n\n")
    
    synth_lines.append("### Big Picture\n")
    synth_lines.append(f"{mod['big_picture']}\n\n")
    
    synth_lines.append("### Conceptual Flow\n")
    synth_lines.append(f"```\n{mod['flow']}\n```\n\n")
    synth_lines.append(f"{mod['flow_explanation']}\n\n")
    
    synth_lines.append("### Key Ideas\n")
    for idea in mod["key_ideas"]:
        synth_lines.append(f"- **{idea.split(':')[0]}:**{idea.split(':')[1] if ':' in idea else idea}\n")
    synth_lines.append("\n")
    
    synth_lines.append("### How the Pieces Fit Together\n")
    synth_lines.append(f"{mod['fit_together']}\n\n")
    
    synth_lines.append("### What You Should Know After This Section\n")
    for item in mod["should_know"]:
        synth_lines.append(f"- {item}\n")
    synth_lines.append("\n")
    
    synth_lines.append("### Related Assignments\n")
    for assign in mod["assignments"]:
        synth_lines.append(f"- {assign}\n")
    synth_lines.append("\n")
    
    synth_lines.append("### Important Resources\n")
    for res in mod["resources"]:
        synth_lines.append(f"- {res}\n")
    synth_lines.append("\n")
    
    with open(os.path.join(mod_path, "synthesis.md"), "w", encoding="utf-8") as f:
        f.writelines(synth_lines)

print(f"Generated synthesis for all {len(modules)} lesson groups successfully!")
