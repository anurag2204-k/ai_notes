# Course Overview: Building Agentic AI Applications with a Problem-First Approach

> **Instructors:** Aishwarya Naresh Reganti & Kiriti Reddy Badam  
> **Platform:** Maven (Cohort 3, July – August 2025)  
> **Audience:** Senior Engineers, AI Practitioners, Tech Leads, and AI Product Builders  

## 1. What This Course Teaches

This intensive 4-week program bridges the gap between toy AI demos and production-grade Enterprise AI systems. Built around a **Problem-First Design Methodology**, the course teaches engineers how to assess business problems, determine whether generative AI or agentic autonomy is genuinely required, and iteratively evolve an application from deterministic workflows to autonomous multi-agent systems.

Throughout the course, students build **Perplexia AI**—an end-to-end intelligent search and research assistant—advancing it through three progressive milestones:
1. **Week 1-2:** Foundation & Workflow Routing (LangChain, LangFlow, prompt engineering, memory state, and deterministic tool execution).
2. **Week 3:** Enterprise Knowledge Integration (Dense/Sparse RAG, Vector Stores, Tavily live web search, and Corrective RAG routing in LangGraph).
3. **Week 4:** Full Autonomous Agentic AI (Dynamic ReAct planning, multi-tool agents, Model Context Protocol (MCP), and Deep Research multi-agent architectures).
4. **Capstone:** An iterative, production-scoped AI system architecture addressing real enterprise domain problems, backed by rigorous evaluation and ROI metrics.

---

## 2. Course Roadmap & Curriculum Progression

```
WEEK 1: ORIENTATION & FOUNDATIONS
├── Problem-First AI Assessment (Input/Output Utility Framework)
├── Iterative Solution Design (Phase 0 -> Phase 1 -> Phase 2)
└── Environment Setup (LangChain, LangFlow, Conda, OpenAI API)
       ↓
WEEK 2: PROMPT ENGINEERING & WORKFLOW AGENTS
├── Advanced Prompt Engineering (Structured Outputs, In-Context Learning, DSPy)
├── Workflow Agents: Deterministic routing, state management, and guardrails
└── [BUILD] Assignment 1: Perplexia AI Part 1 (Router, Memory, Calculator Tool)
       ↓
WEEK 3: ENTERPRISE RAG & CONTEXT ENGINEERING
├── Production RAG Pipelines (Semantic Chunking, Hybrid Search, HyDE Re-ranking)
├── Corrective RAG (CRAG) & Agent Memory Mechanisms
└── [BUILD] Assignment 2: Perplexia AI Part 2 (LangGraph StateGraph, Tavily Search, Document RAG)
       ↓
WEEK 4: AUTONOMOUS AGENTS, MULTI-AGENT SYSTEMS & MCP
├── Agent Taxonomy (Level 1 to Level 5 Autonomy) & Dynamic ReAct Planning
├── Open Protocols: Model Context Protocol (MCP) & Google Agent-to-Agent (A2A)
├── Multi-Agent Design Patterns (Supervisor, Router, Swarm, Deep Research)
├── AIOps, Production Tracing (Comet Opik), Evaluation (Ragas), & Fine-Tuning Decisions
└── [BUILD] Assignment 3: Perplexia AI Part 3 (Autonomous Tool Agent, Agentic RAG, Deep Research)
       ↓
CAPSTONE & BEYOND
├── Problem Scoping & Constraints Mapping (Scratchpad)
├── 3-Iteration Architectural Evolution & Technical Poster Design
└── Enterprise Operational Playbooks (Latency, Token Economics & Quality Evals)
```

---

## 3. Major Topics & Pillars

1. **Problem-First System Framing:** Avoiding the "agent hammer looking for a nail" trap. Evaluating AI vs rule-based solutions using the Input/Output Framework.
2. **Iterative Solution Design:** Starting with a deterministic baseline (Iteration 1), introducing targeted AI augmentation (Iteration 2), and deploying autonomous agentic workflows only where justified (Iteration 3).
3. **In-Context Engineering & Structured Prompting:** Forcing reliable JSON/Pydantic schemas, minimizing hallucination, and leveraging reasoning models (o1, DeepSeek-R1).
4. **Production RAG & Context Engineering:** Moving beyond naive RAG. Mastering semantic chunking, HyDE (Hypothetical Document Embeddings), re-ranking, and CRAG (Corrective RAG).
5. **Stateful Graph Workflows:** Utilizing **LangGraph** to model cycles, checkpoints, conditional branching, human-in-the-loop approvals, and multi-actor state.
6. **Tool Standardization (MCP):** Using Anthropic's Model Context Protocol to decouple agent logic from tool integration, enabling universal tool connectivity.
7. **Multi-Agent Architectures:** Orchestrating specialized sub-agents via Supervisor and Hierarchical topologies to tackle open-ended research and complex reasoning.
8. **Observability, Evals & Fine-Tuning:** Instrumenting tracing with Comet Opik/Langfuse, measuring retrieval precision with Ragas, and knowing when to fine-tune vs prompt.

---

## 4. Core Mental Models to Remember

1. **The Autonomy Spectrum (Level 1 to Level 5):**
   - *Level 1 (Prompted):* Single prompt in, single response out.
   - *Level 2 (Workflow Chains):* Deterministic sequence of steps with static branching.
   - *Level 3 (Autonomous Tool Callers):* LLM decides which tools to call and evaluates output in a loop.
   - *Level 4 (Multi-Agent Collaborations):* Distinct agents with specific roles communicating over structured protocols.
   - *Level 5 (Self-Evolving/Ambient Agents):* Continuous background execution, self-improving prompt/code loops.
2. **Never Agentize What You Can Automate Deterministically:** High-risk, linear processes should remain deterministic code. Use LLMs strictly for cognitive reasoning, extraction, and ambiguity resolution.
3. **Corrective RAG (CRAG) Fallback:** Always grade retrieved context before generating. If document confidence is low, fall back dynamically to live web search.
4. **State as the Single Source of Truth:** In complex agent loops, state must be an immutable, append-only or carefully merged object passed between functional graph nodes.
5. **Separation of Planning and Execution:** High-performing agents split planning (decomposing goals into task lists) from execution (tool calling) and verification (reflecting on results).

---

## 5. Practical Skills: What You Can Build After This Course

- Production-ready **Hybrid Search & Question-Answering Engines** combining internal PDF vectors and external real-time web search.
- **LangGraph StateGraph applications** with conditional routing, self-correction loops, and stateful memory.
- Custom **Model Context Protocol (MCP) Servers** exposing database connections, APIs, and file systems to Claude Desktop or LangGraph agents.
- Autonomous **Deep Research Agents** that iteratively generate search queries, inspect sources, synthesize cross-document findings, and produce comprehensive reports.
- Comprehensive **LLM Tracing & Quality Evaluation Pipelines** in Comet Opik measuring latency, token consumption, and hallucination rates.

---

## 6. Technology Stack Used

| Layer | Technologies Used |
|:---|:---|
| **Orchestration & Graphs** | `LangGraph`, `LangChain`, `LangFlow` (Visual UI) |
| **Foundation Models** | OpenAI (`gpt-4o`, `gpt-4o-mini`, `o1`), DeepSeek (`DeepSeek-R1`) |
| **Search & Web Retrieval** | `Tavily Search API` |
| **Vector Stores & Embeddings** | `ChromaDB`, `FAISS`, `OpenAI text-embedding-3-small` |
| **Tool Protocols** | `Model Context Protocol (MCP)`, `FastAPI`, `JSON-RPC` |
| **Evaluation & Tracing** | `Comet Opik`, `Ragas`, `Langfuse` |
| **Development & UI** | `Python 3.11+`, `Conda`, `Jupyter Notebooks`, `Cursor AI`, `Vercel v0` |

---

## 7. Master Assignment & Project Map

| Assignment / Project | Core Concepts Practiced | Related Lessons | Key Deliverables & Code |
|:---|:---|:---|:---|
| **Assignment 1:** Perplexia Part 1 | Prompt routing, conversation memory, custom tools (Calculator, DateTime) | 035, 036, 037, 056 | LangChain router script / LangFlow JSON flow |
| **Assignment 2:** Perplexia Part 2 | Vector RAG, PDF ingestion, Tavily web search, CRAG routing logic | 057, 058, 059, 060, 083 | LangGraph StateGraph / LangFlow RAG flow |
| **Assignment 3:** Perplexia Part 3 | ReAct tool agents, Agentic RAG, Deep Research multi-agent system, MCP server | 084, 085, 087, 105 | LangGraph multi-agent graph, custom MCP server |
| **Capstone Project:** Iterative AI System | Enterprise problem scoping, 3 architectural iterations, evaluation rubric, poster | 095, 096, 097, 098, 099 | Project Scratchpad + Canva Architecture Poster |

---

## 8. Recommended Learning Sequence

For maximum retention and hands-on mastery, follow this chronological sequence:
1. **Phase 1 (Orientation & Core Principles):** Start with Lessons `001-011` to internalize the Problem-First design philosophy.
2. **Phase 2 (Prompt Engineering & Chaining):** Study Lessons `023-034`, then immediately complete **Assignment 1** (`035-037`).
3. **Phase 3 (Enterprise RAG & Memory):** Study Lessons `044-055`, then build **Assignment 2** (`057-060`) using LangGraph and Tavily.
4. **Phase 4 (Autonomous Agents & Protocols):** Study Lessons `069-082`, complete **Assignment 3** (`084-087`), and experiment with MCP.
5. **Phase 5 (Capstone Architecture & Productionization):** Study Lessons `093-104` to frame, scope, and present your Capstone project.

---

## 9. What Can Be Safely Skipped / Optional Material

The course is comprehensive. If short on time, the following modules are explicitly designated as optional supplementary material:
- **Chai & AI Informal Session (`022`):** Casual community networking; contains no technical curriculum.
- **Deep-Dive Reading Material (Papers & Specialized Guides):** Lessons `014`, `015`, `028`, `053`, `055`, `081`, `082` are optional theoretical deep dives. You can implement all assignments without reading every research paper.
- **Visual Track vs Code Track:** If you are an experienced Python engineer, you can choose the **LangGraph code track** and skip the parallel **LangFlow visual lessons** (`005`, `036`, `058`, `085`), or vice versa.
