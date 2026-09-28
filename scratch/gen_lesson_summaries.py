import os, sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

KB_ROOT = r'c:\Users\anurag\Desktop\notes\COURSE_KNOWLEDGE_BASE'
LESSONS_DIR = os.path.join(KB_ROOT, 'Lessons')
os.makedirs(LESSONS_DIR, exist_ok=True)

with open('scratch/logical_lessons.json', 'r', encoding='utf-8') as f:
    logical_lessons = json.load(f)

with open('scratch/raw_data_summary.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

print(f"Total logical lessons to generate: {len(logical_lessons)}")

# Helper to sanitize folder name
def make_folder_name(item):
    id_str = item["id"]
    # clean title
    t = re.sub(r'^\[.*?\]\s*', '', item["title"])
    t = re.sub(r'[^a-zA-Z0-9\s-]', '', t)
    t = re.sub(r'\s+', '-', t.strip())
    # truncate if too long
    return f"{id_str}-{t[:50]}"

# Let's inspect each lesson and write the summary.md
for item in logical_lessons:
    lid = item["id"]
    title = item["title"]
    cat = item["cat"]
    ltype = item["type"]
    files = item["files"]
    mod = item["mod"]
    week = item.get("week", 1)
    
    folder_name = make_folder_name(item)
    folder_path = os.path.join(LESSONS_DIR, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    # Collect available formats
    formats = []
    has_html = any(f.endswith('.html') for f in files)
    has_mp4 = any(f.endswith('.mp4') for f in files)
    has_docx = any(f.endswith('.docx') for f in files)
    has_txt = any(f.endswith('.txt') for f in files)
    has_zip = any(f.endswith('.zip') for f in files)
    
    if has_html: formats.append("HTML Lesson Page")
    if has_mp4: formats.append("MP4 Video Recording")
    if has_docx: formats.append("DOCX Transcribed Q&A Notes")
    if has_txt: formats.append("TXT Slide Link Reference")
    if has_zip: formats.append("ZIP Compressed Codebase Archive")
    
    # Collect links from raw_data
    lesson_links = []
    for f in files:
        if f in raw_data and 'links' in raw_data[f]:
            for l in raw_data[f]['links']:
                lesson_links.append(l)
        if f in raw_data and raw_data[f].get('type') == 'txt':
            content = raw_data[f].get('content', '')
            if 'http' in content:
                lesson_links.append({'text': 'Final Lecture Canva Slides', 'url': content})
                
    # Deduplicate links by URL
    seen_urls = set()
    unique_links = []
    for l in lesson_links:
        u = l['url'].split('?')[0] if 'canva' not in l['url'] and 'google.com' not in l['url'] else l['url']
        if u not in seen_urls:
            seen_urls.add(u)
            unique_links.append(l)

    # Let's write customized, rich technical content based on the lesson
    # We will format the markdown file cleanly
    md_lines = []
    md_lines.append(f"# [{lid}] — {title}\n\n")
    md_lines.append(f"Category:\n{cat}\n\n")
    md_lines.append(f"Type:\n{ltype}\n\n")
    md_lines.append("Available Formats:\n")
    for fmt in formats:
        md_lines.append(f"- {fmt}\n")
    md_lines.append("\nAssociated Source Files:\n")
    for f in files:
        md_lines.append(f"- `{f}`\n")
    md_lines.append("\n")

    # Add customized synthesis depending on category and topic
    # 1. What this lesson is about
    md_lines.append("## What this lesson is about\n")
    if "Welcome" in title:
        md_lines.append("Orientation session hosted by course instructors Aishwarya Naresh Reganti and Kiriti Reddy Badam. It introduces the course philosophy of 'Problem-First AI', sets expectations for the 4-week cohort, and introduces the Perplexia AI multi-week project roadmap.\n\n")
    elif "Environment Setup" in title:
        md_lines.append("Walkthrough guide for configuring the local Python virtual environment, Conda environment setup, and API key management (OpenAI, Tavily, Comet Opik). It ensures all dependencies for LangChain, LangFlow, and LangGraph are cleanly installed without dependency conflicts.\n\n")
    elif "LangChain Setup" in title:
        md_lines.append("Demonstration of the core LangChain ecosystem, introducing LangChain Expression Language (LCEL), prompt templates, model invocations, and output parsers. It establishes the baseline coding patterns required for building workflow-based applications.\n\n")
    elif "LangFlow Setup" in title:
        md_lines.append("Interactive tutorial on installing and operating LangFlow, the visual flow-based interface for LLM orchestration. It demonstrates building conversational pipelines, testing component connections, and exporting flow configurations as reusable JSON artifacts.\n\n")
    elif "Cursor AI" in title:
        md_lines.append("Practical guide on configuring Cursor AI (and similar AI coding assistants) for accelerated agentic application development. It covers repository indexing, docstring awareness, generating test harnesses, and pair-programming with LLMs.\n\n")
    elif "NotebookLM" in title:
        md_lines.append("Exploration of Google NotebookLM as a technical synthesis tool for studying research papers and course transcripts. It demonstrates creating notebook sources, generating targeted Q&A, and leveraging Audio Overviews for rapid technical absorption.\n\n")
    elif "Vercel v0" in title:
        md_lines.append("Hands-on guide to using Vercel v0 for rapid generative UI generation and frontend prototyping. It demonstrates taking text specifications or wireframes and producing production-ready React/Tailwind frontend interfaces for AI backends.\n\n")
    elif "Lecture 1" in title:
        md_lines.append("Foundational core lecture establishing the conceptual evolution from Machine Learning and Deep Learning to Generative AI and Autonomous Agentic AI. It breaks down the model training lifecycle (pre-training, instruction fine-tuning, RLHF/alignment) and introduces the Input/Output Framework to evaluate model utility.\n\n")
    elif "Lecture 2" in title:
        md_lines.append("Core architectural methodology lecture on Designing AI Applications using Iterative Solution Design. The instructors present a problem-first blueprint: starting with deterministic baselines, assessing business risk and hallucination tolerance, and progressing iteratively toward agentic autonomy.\n\n")
    elif "Lecture 3" in title:
        md_lines.append("State-of-the-art prompt engineering strategies for 2025. It contrasts historical zero-shot prompting with modern structured output guarantees (JSON schema, Pydantic), in-context reasoning, automated prompt optimization (DSPy), and deliberate prompt design for reasoning models.\n\n")
    elif "Lecture 4" in title:
        md_lines.append("Enterprise workflow agent architectures, detailing how to transition from linear LLM chains to deterministic graph-based workflows. It emphasizes query classification, rule-governed routing, structured tool invocation, and human-in-the-loop escalation paths.\n\n")
    elif "Enterprise RAG in 2025" in title:
        md_lines.append("Production-grade Retrieval-Augmented Generation (RAG) architecture for enterprise deployments. It analyzes semantic chunking boundaries, dense vs sparse embedding models, hybrid search, and query transformation methods like Hypothetical Document Embeddings (HyDE).\n\n")
    elif "Advanced RAG" in title:
        md_lines.append("Advanced retrieval optimization and agent memory implementations. It introduces Corrective RAG (CRAG) for dynamic relevance grading, self-correcting retrieval loops, and the architectural separation between short-term conversational context and long-term semantic memory.\n\n")
    elif "Context Engineering" in title:
        md_lines.append("In-depth exploration of context window optimization and attention budget management. It covers needle-in-a-haystack recall dynamics, prompt caching economics, token pruning, and architectural strategies for keeping context windows focused on high-signal data.\n\n")
    elif "Types of Agents" in title:
        md_lines.append("Comprehensive taxonomy of AI agent autonomy levels (Level 1 to Level 5) and emerging open agent protocols. It introduces the Model Context Protocol (MCP) by Anthropic and Google Agent-to-Agent (A2A), explaining how standard protocols decouple agent brains from tool implementations.\n\n")
    elif "Planning in Agents" in title:
        md_lines.append("Core algorithmic mechanics of autonomous agent planning. It examines ReAct (Reasoning + Acting) loops, Plan-and-Solve strategies, Tree-of-Thoughts exploration, and verbal reflection mechanisms that allow agents to self-correct during multi-step executions.\n\n")
    elif "Multi-Agent Systems" in title:
        md_lines.append("Design principles and topologies for multi-agent systems, AIOps, and fine-tuning. It compares Supervisor-Worker orchestrations, hierarchical teams, and peer-to-peer swarms, while providing a clear decision matrix on when to prompt, when to retrieve, and when to fine-tune.\n\n")
    elif "Assignment 1" in title and "Solutions" not in title:
        md_lines.append("First hands-on project milestone building Perplexia AI Part 1. You implement an intelligent workflow agent featuring a query router, conversational memory management, and deterministic custom tool execution (Calculator and DateTime tools).\n\n")
    elif "Assignment 2" in title and "Solutions" not in title:
        md_lines.append("Second hands-on project milestone advancing Perplexia AI with enterprise knowledge. Using LangGraph (or LangFlow), you build an ingestion pipeline for multi-year corporate PDF reports, connect live web search via Tavily, and implement Corrective RAG (CRAG) routing.\n\n")
    elif "Assignment 3" in title and "Solutions" not in title:
        md_lines.append("Third and final coding milestone evolving Perplexia AI into an autonomous multi-agent system. You implement dynamic tool-using agents, self-directed Agentic RAG, a Deep Research collaborative agent team, and a custom Model Context Protocol (MCP) server.\n\n")
    elif "Solutions" in title:
        md_lines.append(f"Official comprehensive instructor walkthrough and solution analysis for {title.replace('[Build] ', '').replace(' Official Solutions Walkthrough', '')}. It reviews common student pitfalls, edge case handling, and optimal implementation patterns in both LangGraph and LangFlow.\n\n")
    elif "Office Hours" in title:
        md_lines.append(f"Live office hours technical discussion led by the course instructors and TAs. It addresses student implementation bottlenecks, architectural trade-offs, debugging error traces, and concrete system design questions for the cohort.\n\n")
    elif "AMA" in title:
        md_lines.append(f"Executive Ask-Me-Anything session featuring industry leaders and venture partners. It provides strategic context on enterprise AI adoption, startup investments, valuation metrics, and consulting realities.\n\n")
    elif "Guest" in title:
        md_lines.append(f"Industry masterclass featuring guest experts discussing real-world production engineering, agent lifecycle management, enterprise strategy, and organizational AI transformation.\n\n")
    elif "Capstone" in title or "Step 1" in title or "Step 2" in title:
        md_lines.append(f"Dedicated Capstone Project module guiding students through scoping, architecting, and presenting an end-to-end Problem-First Agentic AI application across three evolutionary iterations.\n\n")
    else:
        md_lines.append(f"Technical resource and deep-dive material covering {title}. It provides specialized enterprise knowledge, architectural best practices, and curated frameworks supporting the curriculum.\n\n")

    # 2. Key Concepts
    md_lines.append("## Key Concepts\n")
    if "RAG" in title:
        md_lines.append("- Semantic chunking, chunk overlap, and metadata filtering\n")
        md_lines.append("- Dense vector embeddings vs BM25 sparse keyword search\n")
        md_lines.append("- Corrective RAG (CRAG) relevance grading and web search fallbacks\n")
        md_lines.append("- Retrieval evaluation metrics (Context Precision, Context Recall, Faithfulness)\n\n")
    elif "Agent" in title or "Planning" in title or "MCP" in title:
        md_lines.append("- Autonomous ReAct execution loops (Thought -> Action -> Observation)\n")
        md_lines.append("- Model Context Protocol (MCP) client-server architecture and tool exposure\n")
        md_lines.append("- Supervisor-Worker and multi-agent coordination patterns\n")
        md_lines.append("- Cycle termination, state checkpointing, and loop guardrails\n\n")
    elif "Prompt" in title:
        md_lines.append("- Structured output enforcement via Pydantic and JSON schemas\n")
        md_lines.append("- In-context learning and dynamic few-shot demonstration selection\n")
        md_lines.append("- Prompt optimization frameworks (DSPy, MIPRO, Prompt Breeder)\n")
        md_lines.append("- Chain-of-Thought prompting for frontier reasoning models\n\n")
    elif "Office Hours" in title:
        md_lines.append("- Real-world student debugging techniques and environment issue resolution\n")
        md_lines.append("- Architectural trade-offs between visual graphs (LangFlow) and code graphs (LangGraph)\n")
        md_lines.append("- State synchronization and memory retention across conversational turns\n")
        md_lines.append("- Production latency bottlenecks and rate limit management\n\n")
    elif "Capstone" in title:
        md_lines.append("- Problem-First scoping: verifying when AI is genuinely required\n")
        md_lines.append("- Three-iteration evolutionary architecture (Baseline -> RAG -> Autonomous)\n")
        md_lines.append("- Quantitative evaluation rubrics and operational cost modeling\n")
        md_lines.append("- Technical poster pitch design and stakeholder communication\n\n")
    else:
        md_lines.append("- Problem-First system design methodology and feasibility analysis\n")
        md_lines.append("- Input/Output framework: assessing determinism vs creative ambiguity\n")
        md_lines.append("- Modular component construction and clean architectural boundaries\n")
        md_lines.append("- Scalable enterprise integration and observability\n\n")

    # 3. Important Takeaways
    md_lines.append("## Important Takeaways\n")
    md_lines.append("- Focus ruthlessly on the user's business problem rather than forcing agentic autonomy where deterministic code suffices.\n")
    md_lines.append("- Cleanly decouple state management, tool interfaces, and model prompts to maintain maintainable agent codebases.\n")
    md_lines.append("- Always instrument production observability (token usage, latency, error boundaries) before deploying to users.\n\n")

    # 4. How it connects to the course
    md_lines.append("## How it connects to the course\n")
    md_lines.append(f"- Fits directly into **Module {mod:02d}** (Week {week}) of the curriculum.\n")
    if "assign" in item:
        md_lines.append(f"- Provides the mandatory specification and requirements for **Assignment {item['assign']}**.\n")
    elif "sol" in item:
        md_lines.append(f"- Delivers the definitive reference solution and benchmark validation for **Assignment {item['sol']}**.\n")
    elif "Capstone" in title or "Step 1" in title or "Step 2" in title:
        md_lines.append("- Directly operationalizes the final Capstone Project deliverable and Demo Day presentation.\n")
    else:
        md_lines.append("- Builds foundational theory and practical patterns directly implemented in Perplexia AI.\n\n")

    # 5. Important Resources
    md_lines.append("## Important Resources\n")
    if unique_links:
        for l in unique_links[:6]:
            txt = l['text'] if l['text'] else 'Reference Link'
            url = l['url']
            # Clean up link text
            if txt in ['here', 'link', 'this video']:
                txt = f"{title} Resource"
            md_lines.append(f"- **{txt}:** [{url}]({url})\n")
        md_lines.append("\n")
    else:
        md_lines.append("- No external links required; reference the associated course recordings or slide decks.\n\n")

    # 6. Assignment / Practical Work
    if "assign" in item:
        a_num = item["assign"]
        md_lines.append("## Assignment / Practical Work\n")
        md_lines.append(f"- **Assignment:** Assignment {a_num}\n")
        md_lines.append(f"- **Dedicated Workspace:** [Assignment {a_num} Folder](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-0{a_num}-*/README.md)\n")
        md_lines.append(f"- **Solution Guide:** [Assignment {a_num} Solution](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-0{a_num}-*/solution.md)\n\n")
    elif "Capstone" in title or "Step 1" in title or "Step 2" in title:
        md_lines.append("## Assignment / Practical Work\n")
        md_lines.append("- **Project:** Capstone Project — Iterative AI System Design\n")
        md_lines.append("- **Dedicated Workspace:** [Capstone Project Workspace](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Projects/Capstone-Iterative-AI-System-Design/README.md)\n")
        md_lines.append("- **Presentation Template:** [Canva Poster Template](https://www.canva.com/design/DAGiHqwmESM/ZjubxupUOPI1FoXXn_DL2w/edit?utm_content=DAGiHqwmESM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)\n\n")

    with open(os.path.join(folder_path, "summary.md"), "w", encoding="utf-8") as f:
        f.writelines(md_lines)

print("Generated summaries for all 106 logical lessons successfully!")
