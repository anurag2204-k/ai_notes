import os, sys, json

sys.stdout.reconfigure(encoding='utf-8')

KB_ROOT = r'c:\Users\anurag\Desktop\notes\COURSE_KNOWLEDGE_BASE'
ASSIGN_DIR = os.path.join(KB_ROOT, 'Assignments')
PROJ_DIR = os.path.join(KB_ROOT, 'Projects')

# -------------------------------------------------------------------------
# ASSIGNMENT 1
# -------------------------------------------------------------------------
a1_path = os.path.join(ASSIGN_DIR, 'Assignment-01-LangChain-and-LangFlow-Basics')
os.makedirs(a1_path, exist_ok=True)

# A1 README
a1_readme = """# Assignment 1 — Perplexia AI Part 1: Workflow Agents & Tool Integration

## What is this assignment?
Assignment 1 kicks off the development of **Perplexia AI**—your custom AI search and research assistant. In this initial phase, you build the foundational workflow agent capable of understanding user queries, dynamically routing them to specialized execution paths, executing deterministic external tools (such as a calculator or datetime tool), and maintaining multi-turn conversational memory.

## What you need to do
- **Part 1 (Query Routing):** Construct a query classification prompt that analyzes user input and routes between direct conversational responses and tool execution.
- **Part 2 (Tool Integration):** Implement custom tools (a Calculator tool for arithmetic expressions and optionally a DateTime tool for current timestamp awareness).
- **Part 3 (Conversational Memory):** Integrate stateful conversational memory using `RunnableWithMessageHistory` in LangChain (or Memory components in LangFlow) to maintain chat context across multiple user turns.
- **Part 4 (System Evaluation):** Run the provided test cases to verify that calculation questions trigger tool calls while general knowledge questions produce direct responses with correct historical continuity.

## Concepts being practiced
- In-Context Prompt Engineering & Few-Shot Routing
- Custom Tool Binding and Schema Definition
- Deterministic Routing Chains (LCEL / Runnable Branch)
- Conversational Memory State Management
- Visual vs Code-based Agent Pipeline Construction

## Related Course Lessons
- Lesson `004` & `005`: [Build] LangChain Setup and Interactive Demo
- Lesson `006` & `007`: [Build] LangFlow Setup and Visual Pipeline Demo
- Lesson `023`: [Core] Lecture 3: Prompt Engineering in 2025
- Lesson `024`: [Core] Lecture 4: Building Workflow Agents For The Enterprise
- Lessons `035`, `036`, `037`: Assignment 1 Specifications & Test Benchmarks

## Difficulty / Scope
- **Difficulty:** Introductory to Intermediate
- **Estimated Completion Time:** 4–6 hours
- **Prerequisites:** Python 3.10+, basic familiarity with LCEL or visual node connections in LangFlow, OpenAI API key.

## Important Links
- [Assignment Instructions Page](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-LangChain-and-LangFlow-Basics/assignment.md)
- [Assignment Starter Code & Resources](https://drive.google.com/drive/folders/1TiWFMDmrta6NKQgSA7Vv3jlM0Y1pflOw?usp=sharing)
- [Official Solution Guide](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-LangChain-and-LangFlow-Basics/solution.md)
- [LangChain Custom Tools Documentation](https://python.langchain.com/docs/how_to/custom_tools/)
- [LangChain RunnableWithMessageHistory Guide](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.history.RunnableWithMessageHistory.html)

## Solution
Official walkthrough videos and completed code are available. See [solution.md](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-01-LangChain-and-LangFlow-Basics/solution.md) for full walkthrough links and repository paths.
"""

# A1 assignment.md
a1_assignment = """# Assignment 1: Detailed Specifications & Requirements

## Scenario & System Objective
You are building the v1 baseline of **Perplexia AI**. Users need an assistant that doesn't hallucinate mathematical results and remembers what they said two messages ago. Your goal is to build a deterministic workflow agent that intelligently routes queries.

---

## Architectural Requirements

### 1. Query Router Node
- The system must analyze incoming user text.
- If the query requires mathematical calculation (e.g., *"What is 45 * 892 + 12?"*), route to the **Calculator Tool**.
- If the query asks for current temporal context (e.g., *"What day is today?"*), route to the **DateTime Tool**.
- If the query is conversational or factual, route to the **General Conversation Node**.
- Output should be strictly formatted (e.g., JSON schema or discrete string tags: `calculator`, `datetime`, `general`).

### 2. Custom Tools Implementation
- **Calculator Tool:** Must evaluate arithmetic safely without exposing security vulnerabilities (use AST evaluation or strict math regex; avoid unconstrained `eval()`).
- **DateTime Tool (Bonus):** Returns the current system date and UTC/local time in ISO format.

### 3. State & Memory Component
- Maintain conversation history keyed by `session_id`.
- The history must be injected into the LLM prompt template as `ChatPromptTemplate.from_messages([("system", ...), MessagesPlaceholder(variable_name="history"), ("human", "{input}")])`.
- Ensure memory persists across at least 5 consecutive user interactions.

---

## Evaluation Benchmark & Test Cases

| Test Case | User Input | Expected Route | Expected Behavior |
|:---:|:---|:---:|:---|
| **TC-1** | *"Hi! My name is Alex and I'm a software engineer."* | `general` | Remembers Alex's name and role; responds cordially. |
| **TC-2** | *"What was my name and what do I do?"* | `general` | Successfully recalls Alex and software engineering from memory. |
| **TC-3** | *"Can you calculate 1450 divided by 25 plus 38?"* | `calculator` | Routes to calculator tool; evaluates to `96.0`. |
| **TC-4** | *"Tell me a fun fact about honeybees."* | `general` | Routes to general knowledge generation; no tool invoked. |
| **TC-5** | *"Multiply the result of the previous math problem by 2."* | `calculator` | Contextual memory + calculator tool: retrieves `96.0`, computes `192.0`. |

---

## Deliverables
1. **Code Track:** Python script (`perplexia_ai/week1/`) implementing the router, tool bindings, and memory runnable.
2. **Visual Track:** LangFlow JSON file (`Assignment 1 - Solutions.json`) with connected LLM, Prompt, Memory, and Tool components.
3. Test output log proving successful execution of the 5 benchmark test cases.
"""

# A1 resources.md
a1_resources = """# Assignment 1 Resources & Starter Code

## 1. Starter Assets & Google Drive
- **Starter Package (Google Drive):** [Assignment 1 Folder](https://drive.google.com/drive/folders/1TiWFMDmrta6NKQgSA7Vv3jlM0Y1pflOw?usp=sharing)
- **Local Course Archive:** Located in `Cohort 3 - Students.zip` under `Cohort 3 - Students/Assignment 1/`
  - Starter templates for LangChain
  - LangFlow baseline canvas

## 2. Recommended Dependencies
```bash
pip install langchain langchain-openai langchain-core langflow python-dotenv
```

## 3. Reference Implementation Architecture
```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_openai import ChatOpenAI

# 1. Router prompt
router_prompt = ChatPromptTemplate.from_template(\"\"\"
Given the user input below, classify it into one of: 'calculator', 'general'.
Input: {input}
Classification:\"\"\")

# 2. Main conversational chain with memory
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are Perplexia, an accurate research assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])
```

## 4. Documentation References
- [LangChain LCEL Documentation](https://python.langchain.com/docs/concepts/lcel/)
- [LangChain Custom Tools](https://python.langchain.com/docs/how_to/custom_tools/)
"""

# A1 solution.md
a1_solution = """# Assignment 1 Official Solutions

## Solution Availability
- **Official Solution Walkthrough Videos:** Available in course archive (`077 [Build] Assignment 1 Solutions 1.mp4` and `078 [Build] Assignment 1 Solutions 2.mp4`).
- **Official Solution Code:** Located in `Cohort 3 - Students.zip` -> `Cohort 3 - Students/Assignment 1 - Solutions/`.
- **Google Drive Solution Folder:** [Assignment 1 Solutions Drive](https://drive.google.com/drive/folders/1iZsUYjhOV769hH6k5QYxgKAkMGbYgaJu?usp=sharing)

## What the Solution Covers
1. **LangFlow Solution (`Assignment 1 - Solutions (revised).json`):**
   - The instructor demonstrates connecting an OpenAI Model node to a Chat Memory node (`ChatMessageHistory`).
   - Uses a Conditional Router component to inspect query intent.
   - Attaches a Python Code Tool executing sanitized arithmetic calculations.
2. **LangChain Code Solution (`perplexia_ai/week1/`):**
   - Implements `part1.py` (basic routing), `part2.py` (tool integration), and `part3.py` (memory persistence).
   - Demonstrates factory pattern in `factory.py` to instantiate the chain dynamically based on environment configuration.
"""

with open(os.path.join(a1_path, "README.md"), "w", encoding="utf-8") as f:
    f.write(a1_readme)
with open(os.path.join(a1_path, "assignment.md"), "w", encoding="utf-8") as f:
    f.write(a1_assignment)
with open(os.path.join(a1_path, "resources.md"), "w", encoding="utf-8") as f:
    f.write(a1_resources)
with open(os.path.join(a1_path, "solution.md"), "w", encoding="utf-8") as f:
    f.write(a1_solution)

# -------------------------------------------------------------------------
# ASSIGNMENT 2
# -------------------------------------------------------------------------
a2_path = os.path.join(ASSIGN_DIR, 'Assignment-02-Enterprise-RAG-and-Tavily-Search')
os.makedirs(a2_path, exist_ok=True)

a2_readme = """# Assignment 2 — Perplexia AI Part 2: Enterprise RAG, Web Search & Corrective Routing

## What is this assignment?
In Assignment 2, you advance **Perplexia AI** from a simple calculator/memory assistant into a knowledge-grounded enterprise research tool. You integrate two critical data sources: an internal document collection (multi-year enterprise annual performance report PDFs) and real-time external knowledge via the Tavily Search API. Crucially, you implement **Corrective RAG (CRAG)** in **LangGraph**, enabling the system to evaluate retrieved internal documents and fallback gracefully to live web search when internal data is insufficient.

## What you need to do
- **Part 1 (Document Ingestion & Vector RAG):** Ingest annual performance reports (PDFs), chunk them using semantic strategies, index them into ChromaDB/InMemoryVectorStore with OpenAI embeddings, and build an internal retrieval tool.
- **Part 2 (Live Web Search):** Integrate the Tavily Search API to execute real-time web queries with snippet summarization.
- **Part 3 (Corrective RAG - CRAG Routing):** Build a LangGraph cyclic StateGraph with:
  - Document retrieval node.
  - Document relevance evaluator / grading node (LLM as judge assessing whether retrieved chunks answer the query).
  - Conditional edge: If relevant, proceed to generation; if irrelevant or ambiguous, route to Tavily web search.
  - Final answer generation grounded in verified sources with citations.
- **Part 4 (Observability):** Instrument your pipeline with Comet Opik to trace execution steps, latency, and token consumption.

## Concepts being practiced
- Document Chunking, Embedding Models & Vector Stores
- Hybrid Internal vs External Knowledge Routing
- Corrective Retrieval-Augmented Generation (CRAG)
- LangGraph StateGraph, Nodes, Edges, and Conditional Branching
- Observability and Pipeline Tracing (Comet Opik)

## Related Course Lessons
- Lessons `044` & `045`: [Core] Enterprise RAG in 2025 & Advanced RAG / Memory
- Lesson `046`: [Core] Context Engineering in Agents
- Lessons `057`, `058`, `059`, `060`: Assignment 2 Specifications & Tavily Setup
- Lesson `061`: [Build] Comet Opik Setup for LangGraph Tracing

## Difficulty / Scope
- **Difficulty:** Intermediate to Advanced
- **Estimated Completion Time:** 6–8 hours
- **Prerequisites:** Completion of Assignment 1, Tavily API Key, OpenAI API Key, LangGraph installed.

## Important Links
- [Assignment Specifications](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Enterprise-RAG-and-Tavily-Search/assignment.md)
- [Official Solution Guide](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Enterprise-RAG-and-Tavily-Search/solution.md)
- [CRAG Research Paper (arXiv:2401.15884)](https://arxiv.org/abs/2401.15884)
- [Tavily Search API Documentation](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)
- [Comet Opik GitHub](https://github.com/comet-ml/opik)

## Solution
Official solutions and video walkthroughs are available. See [solution.md](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-02-Enterprise-RAG-and-Tavily-Search/solution.md).
"""

a2_assignment = """# Assignment 2: Detailed Specifications & Requirements

## Architecture: Corrective RAG (CRAG) in LangGraph

```
                 [User Query]
                      │
                      ▼
               [Retrieve Docs]
                      │
                      ▼
             [Grade Relevance]
             /               \\
   (Relevant)                 (Not Relevant / Incomplete)
         │                               │
         ▼                               ▼
 [Generate Answer]              [Rewrite / Web Search]
         │                               │
         │                               ▼
         │                       [Generate Answer]
         ▼                               ▼
   [Final Answer Grounded with Citations & Sources]
```

---

## Detailed Task Requirements

### 1. Ingestion Pipeline
- Download the annual performance report PDFs (2019-2022) from the course assets folder.
- Use `PyPDFLoader` or `PDFPlumber` to parse raw text and preserve tabular structures.
- Chunk text using `RecursiveCharacterTextSplitter` with `chunk_size=1000` and `chunk_overlap=200`.
- Generate embeddings using OpenAI `text-embedding-3-small` and index into `Chroma` or `InMemoryVectorStore`.

### 2. Tavily Search Tool
- Configure `TavilySearchResults(max_results=3)`.
- Extract raw content and URL references for attribution.

### 3. LangGraph StateGraph Construction
Define a typed state dictionary:
```python
from typing import TypedDict, List

class AgentState(TypedDict):
    question: str
    generation: str
    web_search: bool
    documents: List[str]
```
- **Node 1 (`retrieve`):** Fetches top-k relevant document chunks from the vector store.
- **Node 2 (`grade_documents`):** Prompts an LLM evaluator to score each document chunk as `yes` or `no` for semantic relevance to the question.
- **Conditional Edge (`decide_to_generate`):**
  - If any document is evaluated as relevant, continue to generation.
  - If all documents are irrelevant, set `web_search=True` and route to `web_search` node.
- **Node 3 (`web_search`):** Rewrites query for web search and queries Tavily.
- **Node 4 (`generate`):** Generates concise final answer strictly referencing the retrieved context.

---

## Evaluation Benchmark & Test Cases

1. **Internal Knowledge Test:**
   - *Query:* *"What were the primary strategic achievements reported in the 2021 annual performance report?"*
   - *Expected Behavior:* Grades documents as relevant; answers purely from PDF vector store; skips Tavily web search.
2. **External Knowledge Test:**
   - *Query:* *"What were the major tech stock market movements yesterday?"*
   - *Expected Behavior:* Grades internal PDFs as irrelevant; triggers Tavily search; generates up-to-date response with live citations.
3. **Ambiguous / Multi-Hop Test:**
   - *Query:* *"How did our 2020 revenue compare to Microsoft's 2024 earnings?"*
   - *Expected Behavior:* Retrieves internal 2020 PDF data, flags missing 2024 Microsoft data, invokes Tavily web search, and synthesizes a comparative table.
"""

a2_resources = """# Assignment 2 Resources & Datasets

## 1. Datasets & Files
- **Annual Reports PDF Dataset:** Located in `Cohort 3 - Students.zip` -> `Cohort 3 - Students/Assignment 2/RAG Dataset/`:
  - `2019-annual-performance-report.pdf`
  - `2020-annual-performance-report.pdf`
  - `2021-annual-performance-report.pdf`
  - `2022-annual-performance-report.pdf`
- **Google Drive Dataset Mirror:** [PDFs Folder](https://drive.google.com/drive/folders/1h-g9aBIa9FWX6Afe2NCxzVkdusokmJpY?usp=sharing)
- **LangFlow Demo Flows:**
  - `Tavily Web Search Example.json`
  - `Vector Store RAG Example.json`

## 2. Starter Notebooks
- `LangGraph And Tavily Demo.ipynb`
- `Using Comet Opik with LangGraph.ipynb`
- `custom_tracking_opik.ipynb`

## 3. Recommended Packages
```bash
pip install langgraph langchain-community langchain-openai chromadb tavily-python opik pypdf
```
"""

a2_solution = """# Assignment 2 Official Solutions

## Official Solution Assets
- **Video Walkthroughs:** `117 [Build] Assignment 2 Solutions 1.mp4` & `118 [Build] Assignment 2 Solutions 2.mp4`
- **Official Solution Code:** Located in `Cohort 3 - Students.zip` -> `Cohort 3 - Students/Assignment 2 - Solutions/`:
  - `LangGraph/code/perplexia_ai/week2/`
    - `part1.py` (Vector store RAG)
    - `part2.py` (Tavily search integration)
    - `part3.py` (Complete LangGraph CRAG StateGraph)
    - `prompts.py` (Document grader and query rewriter prompts)
  - `LangFlow/`
    - `Assignment 2 - Part 1 Solution.json`
    - `Assignment 2 - Part 3 Solutions.json`
- **Google Drive Solutions Link:** [Assignment 2 Solutions Drive](https://drive.google.com/drive/folders/18nh4lZq8mZbPTburDwne5JUnFYU131By?usp=drive_link)

## What the Solution Demonstrates
- Strict document grading using Pydantic output parsers (`score: Literal['yes', 'no']`).
- Building the StateGraph with `StateGraph(AgentState)` and adding conditional edges via `graph.add_conditional_edges()`.
- Instrumenting Opik callbacks: passing `opik_tracer` to monitor LLM token costs across the grading and generation stages.
"""

with open(os.path.join(a2_path, "README.md"), "w", encoding="utf-8") as f:
    f.write(a2_readme)
with open(os.path.join(a2_path, "assignment.md"), "w", encoding="utf-8") as f:
    f.write(a2_assignment)
with open(os.path.join(a2_path, "resources.md"), "w", encoding="utf-8") as f:
    f.write(a2_resources)
with open(os.path.join(a2_path, "solution.md"), "w", encoding="utf-8") as f:
    f.write(a2_solution)

# -------------------------------------------------------------------------
# ASSIGNMENT 3
# -------------------------------------------------------------------------
a3_path = os.path.join(ASSIGN_DIR, 'Assignment-03-Agentic-Workflows-LangGraph-and-MCP')
os.makedirs(a3_path, exist_ok=True)

a3_readme = """# Assignment 3 — Perplexia AI Part 3: Autonomous Agents, Deep Research & Model Context Protocol (MCP)

## What is this assignment?
Assignment 3 represents the apex of the hands-on curriculum. You transform Perplexia AI from a predefined workflow into an **autonomous agentic system** where planning, tool selection, task decomposition, and loop termination are dynamically handled by the AI. You build a dynamic **Tool-Using Agent**, an **Agentic RAG pipeline**, and a multi-agent **Deep Research System**. Furthermore, you implement and connect a custom **Model Context Protocol (MCP)** server, making Perplexia fully extensible using open industry protocols.

## What you need to do
- **Part 1 (Tool-Using Agent & MCP Integration):** Replace hardcoded routers with an autonomous ReAct agent using `bind_tools`. Create a custom MCP server (e.g., Bookmarking or Math server) exposing tools over JSON-RPC.
- **Part 2 (Agentic RAG):** Implement autonomous document research where the agent inspects retrieved documents, realizes what information is missing, reformulates queries, and searches iteratively until the research goal is satisfied.
- **Part 3 (Deep Research Multi-Agent System):** Build a multi-agent collaborative system:
  - *Lead Researcher / Planner Agent:* Decomposes research questions into sub-topics.
  - *Web & Document Search Agent:* Executes multi-source retrieval.
  - *Fact Checker / Critic Agent:* Validates consistency and flags discrepancies.
  - *Report Writer Agent:* Compiles findings into an executive briefing with citations.
- **Part 4 (Testing & Self-Evaluation):** Develop a domain-specific evaluation benchmark with multi-step reasoning queries.

## Concepts being practiced
- ReAct Agent Execution Loops (`create_react_agent` / StateGraph)
- Model Context Protocol (MCP) Client & Server Architecture
- Agentic RAG (Self-directed iterative query expansion)
- Multi-Agent Orchestration (Supervisor Pattern)
- Context Management & Infinite Loop Prevention

## Related Course Lessons
- Lesson `069`: [Core] Lecture 7: Types of Agents & AI Protocols
- Lesson `070`: [Core] Lecture 8: Planning in Agents (ReAct Prompting)
- Lesson `071`: [Core] Lecture 9: Multi-Agent Systems, AIOps & Fine-Tuning
- Lessons `084`, `085`: Assignment 3 Specifications (LangGraph & LangFlow)
- Lesson `087`: [Build][Bonus] Using and Building MCP Servers

## Difficulty / Scope
- **Difficulty:** Advanced
- **Estimated Completion Time:** 8–12 hours
- **Model Recommendation:** Use `gpt-4o` (not mini) for reliable tool-calling and planning precision.

## Important Links
- [Assignment Specifications](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Agentic-Workflows-LangGraph-and-MCP/assignment.md)
- [Official Solution Guide](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Agentic-Workflows-LangGraph-and-MCP/solution.md)
- [Starter Code Package (Google Drive)](https://drive.google.com/drive/folders/1nLPfsGQnqFNpfhocr1JcAU2g183LxDQV?usp=drive_link)
- [Model Context Protocol GitHub](https://github.com/modelcontextprotocol/servers)
- [LangGraph Agentic RAG Documentation](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/)

## Solution
Official walkthrough videos and full source code are provided. See [solution.md](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Assignments/Assignment-03-Agentic-Workflows-LangGraph-and-MCP/solution.md).
"""

a3_assignment = """# Assignment 3: Detailed Specifications & Requirements

## Architecture: Autonomous Deep Research Multi-Agent System

```
                      [User Research Topic]
                                │
                                ▼
                     [Research Planner Agent]
                    (Decompose into 3 Sub-Tasks)
                                │
                                ▼
                    [Supervisor / Coordinator]
                   /            |             \\
                  ▼             ▼              ▼
           [Search Sub-Agent] [Doc Sub-Agent] [MCP Tool Server]
                  \\             |              /
                   \\            |             /
                    ▼           ▼            ▼
                   [Fact-Checking / Critic Agent]
                    (Checks consistency & gaps)
                                │
                                ▼
                     [Executive Report Writer]
                    (Structured Markdown Output)
```

---

## Technical Specifications

### Part 1: Autonomous Tool-Using Agent & Custom MCP Server
1. **Dynamic Tool Calling:** Use `ChatOpenAI(model="gpt-4o").bind_tools([calculator_tool, tavily_tool, document_retriever])`.
2. **Custom MCP Server:**
   - Create a custom MCP server script (`bookmarking_mcp_server.py` or `math_server.py`).
   - Implement tools: `add_bookmark(title, url, notes)` and `search_bookmarks(query)`.
   - Connect your LangGraph agent to the MCP client to dynamically discover and invoke MCP server endpoints.

### Part 2: Agentic RAG
1. Implement a self-directed retrieval loop. If the model receives retrieved text that does not answer the core question, it must formulate a refined sub-query rather than producing a fallback hallucination.
2. Cap the loop at a maximum of `max_iterations = 4` to prevent infinite execution cycles.

### Part 3: Deep Research System
1. Build a multi-agent StateGraph with at least three distinct roles:
   - **Planner:** Generates a structured research agenda.
   - **Researcher:** Iteratively queries web and local document vectors.
   - **Writer:** Synthesizes facts, resolves conflicting claims, and structures the final output with footnotes and links.

---

## Evaluation Benchmark & Requirements
- **Complex Query 1:** *"Perform a comprehensive competitive analysis of OpenAI vs Anthropic's enterprise strategies in 2024-2025, detailing model pricing, tool protocols (MCP), and enterprise security guarantees."*
- **Complex Query 2:** *"Analyze our company's annual reports from 2019-2022 to track operating margin trends, and cross-reference with current industry benchmarks found on the web."*
- **Deliverable:** Full Python package (`perplexia_ai/week3/`) and demonstration notebook or LangFlow JSON exports.
"""

a3_resources = """# Assignment 3 Resources & Starter Assets

## 1. Starter Code & Files
- **Starter Package (Google Drive):** [Assignment 3 Drive Folder](https://drive.google.com/drive/folders/1nLPfsGQnqFNpfhocr1JcAU2g183LxDQV?usp=drive_link)
- **Local Course Archive:** Located in `Cohort 3 - Students.zip` -> `Cohort 3 - Students/Assignment 3/`:
  - `LangGraph Agents and Comet Opik.ipynb`
  - `MCP with LangGraph Demo.ipynb`
  - `math_server.py`
  - `code/perplexia_ai/week3/`
  - `LangFlow Demo Flows/`:
    - `Agent with Tools Example.json`
    - `Agents Calling Agents.json`
    - `Agents with Vector Store Tool.json`
    - `MCP server example.json`

## 2. MCP Installation & Configuration
```bash
pip install mcp langchain-mcp-adapters
```
"""

a3_solution = """# Assignment 3 Official Solutions

## Official Solution Assets
- **Video Walkthroughs:** `149 [Build] Assignment 3 Solutions 1.mp4` & `150 [Build] Assignment 3 Solutions 2.mp4`
- **Solution Code in Archive:** `Cohort 3 - Students.zip` -> `Cohort 3 - Students/Assignment 3 - Solutions/`:
  - `LangGraph/code/perplexia_ai/week3/`
    - `part1.py` (ReAct Tool Agent)
    - `part1_mcp.py` (MCP Client Integration)
    - `bookmarking_mcp_server.py` (FastMCP Server Implementation)
    - `part2.py` (Agentic RAG with query rewriting)
    - `part3.py` (Deep Research Multi-Agent System)
    - `prompts.py` (Planner, Critic, and Writer prompts)
  - `LangFlow/`
    - `Assignment 3 Part 1 - Tool Using Agent.json`
    - `Assignment 3 Part 2 - Agentic RAG.json`
    - `Assignment 3 Part 3 - Deep Research Agent.json`
- **Google Drive Solutions Link:** [Assignment 3 Solutions Drive](https://drive.google.com/drive/folders/1iZsUYjhOV769hH6k5QYxgKAkMGbYgaJu?usp=drive_link)
"""

with open(os.path.join(a3_path, "README.md"), "w", encoding="utf-8") as f:
    f.write(a3_readme)
with open(os.path.join(a3_path, "assignment.md"), "w", encoding="utf-8") as f:
    f.write(a3_assignment)
with open(os.path.join(a3_path, "resources.md"), "w", encoding="utf-8") as f:
    f.write(a3_resources)
with open(os.path.join(a3_path, "solution.md"), "w", encoding="utf-8") as f:
    f.write(a3_solution)

# -------------------------------------------------------------------------
# CAPSTONE PROJECT
# -------------------------------------------------------------------------
cap_path = os.path.join(PROJ_DIR, 'Capstone-Iterative-AI-System-Design')
os.makedirs(cap_path, exist_ok=True)

cap_readme = """# Capstone Project: Problem-First Iterative AI System Design

## What is this project?
The Capstone Project is the culminating exercise of the program. Applying the **Problem-First Methodology** taught by Aishwarya and Kiriti, student teams select a real-world enterprise domain problem (e.g., automated legal contract auditing, clinical trial protocol matching, or automated financial risk reporting) and architect an end-to-end Agentic AI system through **three iterative evolutionary stages**.

## Project Deliverables
1. **Scoping & Scratched Document:** Structured design document detailing problem framing, stakeholders, constraints, and baseline feasibility.
2. **Architectural Evolution (Iterations 1, 2, and 3):**
   - *Iteration 1 (Deterministic / Rule-Augmented Baseline):* Low risk, fast time-to-market.
   - *Iteration 2 (Knowledge-Enhanced RAG & Directed Workflows):* Incorporating domain data with semantic retrieval and verification.
   - *Iteration 3 (Autonomous Multi-Agent Architecture):* Autonomous planning, tool-calling, reflection, and human-in-the-loop escalation.
3. **Evaluation & Operational Playbook:** Complete quality rubric (Ragas metrics, LLM-as-a-judge) and operational economic analysis (P95 latency, token cost modeling).
4. **Demo Day Pitch Poster:** Visual technical poster formatted according to the official Canva template.
5. **Working Prototype (Optional Bonus):** Working LangGraph or LangFlow proof-of-concept demonstrating key workflow nodes.

## Related Course Lessons
- Lessons `011`: [Core] Lecture 2: Designing AI Applications (Iterative Solution Design)
- Lessons `095` - `099`: Capstone Brainstorming, Overview, Guidelines, Step 1 & Step 2
- Lessons `100` - `104`: Enterprise Playbooks (Prompt/RAG Optimizations, Operational & Evaluation Metrics)
"""

cap_reqs = """# Capstone Project: Detailed Requirements & Rubric

## Project Structure & 3-Iteration Framework

### Step 1: Problem Scoping (The \"Problem-First\" Foundation)
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
"""

cap_resources = """# Capstone Project Resources & Templates

## Official Course Templates
- **Capstone Presentation Canva Poster Template:** [Canva Poster Template](https://www.canva.com/design/DAGiHqwmESM/ZjubxupUOPI1FoXXn_DL2w/edit?utm_content=DAGiHqwmESM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
- **Official Scoping Scratchpad (Google Doc):** [Google Doc Scratchpad](https://docs.google.com/document/d/1iOZOcJ8ubhHoEzwxkqrZ3fRGbpLozV0INQr5OwwntC8/edit?usp=sharing)
- **Demo Day Showcase Video:** Lesson `017` / `021` showcases winning Capstone projects from Cohorts 1 & 2.

## Technical Playbooks for Implementation
- [Enterprise Prompt Optimizations](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Lessons/100-Prompt-Optimizations-For-The-Enterprise/summary.md)
- [Enterprise RAG Optimizations](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Lessons/101-RAG-Optimizations-For-The-Enterprise/summary.md)
- [Level 2 Agent Patterns & Tool Sandboxing](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Lessons/102-Level-2-Agents-Resources-For-The-Enterprise/summary.md)
- [Evaluation & Quality Metrics Guide](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Lessons/103-Evaluation-Metrics/summary.md)
- [Operational & Economics Metrics Guide](file:///c:/Users/anurag/Desktop/notes/COURSE_KNOWLEDGE_BASE/Lessons/104-Operational-Metrics/summary.md)
"""

cap_guide = """# Capstone Scoping & Architectural Design Guide

## Blueprint for a Winning Capstone Architecture

```
[Phase 1: Problem Scoping]
  - Identify non-linear cognitive tasks where rules fail.
  - Define user persona, input modalities, and required SLA.

[Phase 2: Architectural Iterations]
  ┌────────────────────────────────────────────────────────┐
  │ Iteration 1: Deterministic Prompt & Rule Pipeline      │
  │ • Fast baseline, low cost, 0 agentic loops             │
  └──────────────────────────┬─────────────────────────────┘
                             │ (Identify knowledge gaps)
                             ▼
  ┌────────────────────────────────────────────────────────┐
  │ Iteration 2: Enterprise Hybrid RAG + Router            │
  │ • Vector DB + Tavily fallback + HyDE query expansion   │
  └──────────────────────────┬─────────────────────────────┘
                             │ (Identify reasoning bottlenecks)
                             ▼
  ┌────────────────────────────────────────────────────────┐
  │ Iteration 3: Supervisor-Worker Multi-Agent System       │
  │ • LangGraph StateGraph, MCP Tool Servers, Evals        │
  └────────────────────────────────────────────────────────┘

[Phase 3: Operational & Economic Feasibility]
  - Token cost per run = (Input_Tokens * Input_Price) + (Output_Tokens * Output_Price)
  - Latency budget = Σ(LLM time) + Σ(Tool time) + Network overhead
  - Error mitigation: Fallbacks, timeouts, and human intervention gateways.
```
"""

with open(os.path.join(cap_path, "README.md"), "w", encoding="utf-8") as f:
    f.write(cap_readme)
with open(os.path.join(cap_path, "requirements.md"), "w", encoding="utf-8") as f:
    f.write(cap_reqs)
with open(os.path.join(cap_path, "resources.md"), "w", encoding="utf-8") as f:
    f.write(cap_resources)
with open(os.path.join(cap_path, "scoping_and_architecture_guide.md"), "w", encoding="utf-8") as f:
    f.write(cap_guide)

print("Assignments and Capstone directories generated successfully!")
