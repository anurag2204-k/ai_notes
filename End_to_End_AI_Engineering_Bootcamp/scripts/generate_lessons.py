import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

KB_BASE = r"c:\Users\anurag\Desktop\notes\End_to_End_AI_Engineering_Bootcamp\COURSE_KNOWLEDGE_BASE"
LESSONS_DIR = os.path.join(KB_BASE, "Lessons")
os.makedirs(LESSONS_DIR, exist_ok=True)

lessons_data = [
    {
        "filename": "01-AI-Product-Lifecycle-and-Problem-Framing.md",
        "title": "Understanding the AI Product Lifecycle and Problem Framing",
        "type": "Technical Lecture & Architecture Guide",
        "teaches": "This lesson teaches the systemic engineering lifecycle required to build production AI applications. It contrasts exploratory research prototypes with commercial systems that require deterministic performance, cost bounds, and evaluation gates. It details how to frame business problems into technical AI objectives and establish baseline operational KPIs.",
        "key_concepts": [
            "AI Product Lifecycle: Problem framing, data curation, offline evaluation, prototyping, production hardening, online monitoring",
            "Technical vs. Business Metrics: Linking latency and hallucination rates directly to business churn and compute budgets",
            "Feasibility Assessment: Deciding when an LLM is appropriate versus classical rule-based or machine learning solutions",
            "Iterative Feedback Loops: Using production logs to guide data collection and prompt improvements"
        ],
        "takeaways": [
            "Most AI projects fail at the problem-framing stage, not during prompt engineering.",
            "Always establish clear evaluation benchmarks before writing any application code.",
            "Production AI requires treating models as stochastic components within deterministic software harnesses.",
            "Observability and tracing must be planned during architecture scoping, not patched after deployment."
        ],
        "connection": [
            "Serves as the foundation for the entire course and capstone project.",
            "Dictates how student assignments are framed, built, and evaluated in later sprints."
        ]
    },
    {
        "filename": "02-Naive-vs-Advanced-RAG-Architectures.md",
        "title": "Naive vs. Advanced Retrieval-Augmented Generation (RAG)",
        "type": "Architecture Lecture",
        "teaches": "This lesson deconstructs the architectural progression from naive 'Retrieve-Then-Generate' pipelines to advanced RAG systems. It explains the mechanics of vector lookup, context injection, and parametric vs. non-parametric memory. It systematically catalogs the primary failure modes of naive RAG.",
        "key_concepts": [
            "Parametric vs. Non-Parametric Memory: LLM internal weights versus external knowledge retrieval",
            "Naive RAG Pipeline: Vectorize query → Retrieve top-k nearest neighbors → Stuff context into prompt → Generate response",
            "Core RAG Failure Modes: Retrieval miss, hallucinated context, context overflow, lost-in-the-middle phenomenon",
            "Grounding Mechanics: Enforcing strict instruction boundaries to prevent parametric hallucinations"
        ],
        "takeaways": [
            "Naive RAG fails in production because semantic similarity does not guarantee relevance or factual completeness.",
            "Context stuffing introduces noise that degrades LLM attention, leading to inaccurate answers.",
            "Grounding prompts must explicitly forbid the model from speculating beyond retrieved evidence.",
            "Advanced RAG introduces multi-stage retrieval, re-ranking, and dynamic agent loops to mitigate naive flaws."
        ],
        "connection": [
            "Explains the motivation for Sprint 0's baseline RAG prototype.",
            "Sets the stage for the retrieval optimizations and context engineering implemented in Sprint 1."
        ]
    },
    {
        "filename": "03-Vector-Databases-and-Qdrant-Indexing.md",
        "title": "Vector Databases and Qdrant Collection Indexing",
        "type": "Technical Tutorial & Implementation Guide",
        "teaches": "This lesson teaches vector representation theory, high-dimensional indexing algorithms, and vector database management with Qdrant. It covers distance metrics, HNSW graph structures, and payload filtering. It details the practical engineering required to batch-embed and index large-scale catalog datasets.",
        "key_concepts": [
            "Vector Embeddings: Dense mathematical representations of semantic meaning in high-dimensional vector spaces (e.g. 1536 dims)",
            "Distance Metrics: Cosine similarity vs. Dot product vs. Euclidean distance and their normalization constraints",
            "HNSW (Hierarchical Navigable Small World): Graph-based approximate nearest neighbor (ANN) search algorithm balancing speed and recall",
            "Qdrant Payload Architecture: Storing metadata (ASIN, title, price, category) directly alongside vector points for pre-filtering"
        ],
        "takeaways": [
            "Cosine similarity requires normalized vectors; when using OpenAI embeddings, dot product on normalized vectors is mathematically identical and computationally faster.",
            "Payload design is critical: storing display metadata inside Qdrant eliminates redundant secondary database queries during inference.",
            "HNSW indexing parameters (m and ef_construct) control the speed-accuracy tradeoff during search.",
            "Filtering before retrieval (pre-filtering) prevents searching through irrelevant categories or out-of-stock items."
        ],
        "connection": [
            "Directly underpins the Amazon Electronics catalog search engine in Sprint 0.",
            "Forms the vector storage infrastructure upgraded to hybrid search in Sprint 1."
        ]
    },
    {
        "filename": "04-LLM-Observability-Tracing-and-RAGAS-Evals.md",
        "title": "LLM Observability, Tracing, and Automated RAGAS Evaluations",
        "type": "Implementation Guide & MLOps Standard",
        "teaches": "This lesson teaches how to instrument distributed tracing across LLM pipelines using LangSmith and execute automated quantitative evaluations with RAGAS. It explains the Three Pillars of Observability and demonstrates how LLM-as-a-judge frameworks assess retrieval and generation quality.",
        "key_concepts": [
            "Three Pillars of LLM Observability: Traces (execution graphs), Metrics (latency, cost, token counts), and Logs (metadata, prompts)",
            "Distributed Trace Trees: Hierarchical parent-child spans representing API calls, vector lookups, and model generations",
            "RAGAS Framework: Faithfulness (hallucination detection), Answer Relevance (query alignment), Context Recall, and Context Precision",
            "Synthetic Golden Datasets: Generating Q&A pairs from raw documents to serve as evaluation benchmarks"
        ],
        "takeaways": [
            "Without distributed tracing, diagnosing multi-step stochastic agent pipelines is practically impossible.",
            "RAGAS Faithfulness measures whether every claim in the generated answer is strictly grounded in retrieved context.",
            "Automated evals must be run on representative datasets before pushing prompt or model changes to production.",
            "LangSmith trace IDs enable direct attribution of user feedback to specific pipeline execution runs."
        ],
        "connection": [
            "Implemented in Sprint 0 to benchmark the baseline RAG pipeline.",
            "Used continuously throughout the bootcamp to validate each architectural enhancement."
        ]
    },
    {
        "filename": "05-Pydantic-and-Structured-Outputs-with-Instructor.md",
        "title": "Pydantic and Structured Outputs with Instructor",
        "type": "Code Tutorial & Best Practice",
        "teaches": "This lesson teaches how to force LLMs to generate strictly validated, deterministic JSON structures matching Pydantic models. It explains how Instructor leverages function calling and JSON schema modes to validate outputs and automatically retry when validation rules fail.",
        "key_concepts": [
            "Structured Output Enforcement: Constraining LLM token sampling to valid JSON conforming to an explicit JSON schema",
            "Instructor Library: Python wrapper around LLM APIs providing automatic validation, Pydantic coercion, and retry loops",
            "Self-Correction Retries: Feeding validation error tracebacks back into the model to prompt autonomous schema repair",
            "Typed Schema Engineering: Defining nested models, optional fields, enums, and field descriptions to guide generation"
        ],
        "takeaways": [
            "Unstructured text outputs are unacceptable in production software architectures.",
            "Instructor eliminates regex parsing hacks and JSON decode exceptions by validating responses at the API boundary.",
            "Validation errors provide rich, immediate feedback that enables the LLM to correct its own output in a single retry.",
            "Detailed Field descriptions in Pydantic models act as micro-prompts that significantly improve data extraction accuracy."
        ],
        "connection": [
            "Introduced in Sprint 1 to structure RAG answers and item recommendation cards.",
            "Directly enables agent tool argument generation and intent classification in Sprint 2 and 3."
        ]
    },
    {
        "filename": "06-Contextual-Retrieval-and-Chunking-Strategies.md",
        "title": "Chunking Strategies and Anthropic Contextual Retrieval",
        "type": "Technical Reading & Architecture Guide",
        "teaches": "This lesson explores advanced document chunking strategies and Anthropic's landmark Contextual Retrieval technique. It examines how document fragmentation destroys semantic context and demonstrates how prepending document-level context to chunks dramatically boosts retrieval accuracy.",
        "key_concepts": [
            "Chunking Strategies: Fixed-size chunking, recursive character splitting, document structure-aware splitting, and semantic boundary chunking",
            "Context Loss Problem: Isolated chunks losing their global referents (e.g., 'the company' instead of 'Apple Inc.')",
            "Contextual Retrieval: Using a fast LLM to generate 50-100 tokens of document-level context prepended to every chunk before embedding",
            "Late Chunking: Generating full-document token representations before chunk-pooling to preserve global bidirectional attention"
        ],
        "takeaways": [
            "Poor chunking strategy limits downstream retrieval quality more than vector database choice.",
            "Contextual Retrieval reduces failed retrievals by up to 49% by preserving document context in high-dimensional space.",
            "Document headers, breadcrumbs, and structural hierarchy should always be preserved in chunk metadata.",
            "Semantic chunking balances chunk size by splitting text on natural topic transitions rather than arbitrary character counts."
        ],
        "connection": [
            "Upgrades Sprint 0's naive chunking pipeline into a production-grade ingestion engine in Sprint 1.",
            "Directly enhances retrieval precision for the e-commerce product catalog."
        ]
    },
    {
        "filename": "07-Hybrid-Search-Dense-Sparse-and-Reranking.md",
        "title": "Hybrid Search (Dense + Sparse) and Cross-Encoder Re-Ranking",
        "type": "Architecture & Implementation Guide",
        "teaches": "This lesson teaches how to combine dense semantic embeddings with sparse lexical search (BM25) and apply cross-encoder re-ranking. It explains why dense retrieval fails on exact SKU and keyword queries and demonstrates how two-stage retrieval delivers state-of-the-art search relevance.",
        "key_concepts": [
            "Dense Retrieval: Bi-encoder semantic vector search capturing conceptual meaning and synonyms",
            "Sparse Retrieval: BM25 / TF-IDF lexical frequency search capturing exact keyword, SKU, and acronym matches",
            "Hybrid Fusion: Combining dense and sparse score lists using Reciprocal Rank Fusion (RRF) or relative score fusion in Qdrant",
            "Cross-Encoder Re-Ranking: Applying joint attention across query and document pairs to compute definitive relevance scores"
        ],
        "takeaways": [
            "Dense search alone is insufficient for enterprise search; hybrid search is the mandatory baseline.",
            "Two-stage retrieval balances latency and accuracy: retrieve 25 candidates via fast hybrid search, then re-rank top 5 with cross-encoder.",
            "Bi-encoders compute vector representations independently; cross-encoders compute all-to-all cross-attention between query and passage.",
            "Qdrant natively supports dual dense and sparse vector indexing within the same collection."
        ],
        "connection": [
            "Core technical upgrade implemented in Sprint 1.",
            "Serves as the high-accuracy retrieval tool passed to autonomous agents in Sprint 2."
        ]
    },
    {
        "filename": "08-Prompt-Management-and-Jinja2-Registries.md",
        "title": "Decoupled Prompt Management and Jinja2 Registries",
        "type": "Software Engineering Best Practice",
        "teaches": "This lesson teaches professional prompt engineering and management practices. It demonstrates why hardcoding prompt strings inside application code creates severe maintenance debt and shows how to decouple prompts into version-controlled YAML files rendered via Jinja2 templates.",
        "key_concepts": [
            "Decoupled Prompt Architecture: Separating system prompts, few-shot examples, and task instructions from application logic",
            "Jinja2 Template Engines: Parameterizing prompts with loops, conditionals, and variables for dynamic rendering",
            "YAML Prompt Registries: Version-controlled files specifying model parameters (temperature, max_tokens) alongside prompt text",
            "Prompt Versioning & CI Testing: Treating prompts as executable code subject to unit testing and regression evaluation"
        ],
        "takeaways": [
            "Never scatter raw prompt strings or f-strings across Python business logic modules.",
            "Jinja2 enables clean conditional logic in prompts (e.g., rendering few-shot examples only when available).",
            "YAML configuration registries allow prompt engineers and domain experts to update prompts without modifying backend code.",
            "Standardized prompt loaders ensure that temperature, system instructions, and schemas are applied deterministically."
        ],
        "connection": [
            "Implemented in Sprint 1 for retrieval generation prompts.",
            "Standardizes prompt handling for intent routers, QA agents, and coordinators in Sprints 2, 3, and 4."
        ]
    },
    {
        "filename": "09-Agent-Architectures-and-Anthropic-Design-Patterns.md",
        "title": "Agent Architectures and Anthropic's Agentic Design Patterns",
        "type": "Conceptual Lecture & Architecture Guide",
        "teaches": "This lesson teaches the core design patterns of agentic systems based on Anthropic's 'Building Effective Agents' research. It analyzes the spectrum of autonomy—from deterministic augmented LLMs and prompt chains to autonomous orchestrator-worker systems—guiding engineers on when and when NOT to build agents.",
        "key_concepts": [
            "Spectrum of Autonomy: Augmented LLM → Prompt Chaining → Routing → Parallelization → Orchestrator-Workers → Evaluator-Optimizer",
            "Principle of Simplicity: Prioritizing deterministic code and simple chains before introducing autonomous loops",
            "Orchestrator-Workers Pattern: A central coordinator agent dynamically decomposes tasks and delegates to worker sub-agents",
            "Evaluator-Optimizer Loop: An agent generates a solution, a critic evaluates it against criteria, and feedback refines the output"
        ],
        "takeaways": [
            "The most reliable agentic systems often use the simplest viable architecture rather than maximum autonomy.",
            "Deterministic routing should always be preferred over LLM tool selection when intent boundaries are clear.",
            "Orchestrator-worker patterns are ideal when task complexity cannot be anticipated in advance.",
            "Evaluator-optimizer loops are highly effective for code generation, translation, and structured data extraction."
        ],
        "connection": [
            "Provides the theoretical blueprint for all agent development in Sprints 2, 3, and 4.",
            "Directly informs the Coordinator-Worker multi-agent architecture built in Sprint 4."
        ]
    },
    {
        "filename": "10-LangGraph-StateGraph-and-Cyclical-Workflows.md",
        "title": "LangGraph StateGraph and Cyclical Workflows",
        "type": "Technical Tutorial & Code Guide",
        "teaches": "This lesson teaches the core abstractions of the LangGraph framework. It explains how LangGraph models multi-step agent reasoning as cyclical directed state machines, contrasting it with linear DAG frameworks. It covers StateGraph definitions, node functions, edge routing, and state reducers.",
        "key_concepts": [
            "LangGraph Core Abstractions: StateGraph, Nodes (pure Python functions), Edges, Conditional Edges, START, and END",
            "Typed Graph State: Pydantic schemas or TypedDicts defining shared memory across graph execution",
            "State Reducers: Using operators (e.g., `operator.add`) to append new messages rather than overwriting historical context",
            "Cyclical Execution: Enabling loopback transitions from tool execution nodes back to agent reasoning nodes"
        ],
        "takeaways": [
            "Linear DAGs cannot model real-world agent behavior; cyclical graphs are required for feedback and tool retries.",
            "LangGraph nodes must be pure functions that take the current state and return incremental state updates.",
            "Conditional edges inspect state variables to determine deterministic next-step transitions.",
            "State schemas provide strict type safety and compile-time validation for complex multi-node workflows."
        ],
        "connection": [
            "Introduced in Sprint 2 as the primary agent execution framework.",
            "Used to build the single-turn agent in Sprint 2, the multi-turn agent in Sprint 3, and the multi-agent system in Sprint 4."
        ]
    },
    {
        "filename": "11-Tool-Use-Function-Calling-and-ReAct-Loops.md",
        "title": "Tool Use, Function Calling, and ReAct Agent Loops",
        "type": "Code Tutorial & Implementation Guide",
        "teaches": "This lesson teaches the mechanics of tool binding, function calling, and constructing autonomous ReAct (Reason + Act) loops in LangGraph. It details how tools are converted into JSON schemas, how LLMs emit tool calls, and how tool execution results are injected back into the reasoning loop.",
        "key_concepts": [
            "ReAct Framework: Interleaving thought (reasoning trace), action (tool execution), and observation (tool output)",
            "Tool Specification: Defining tools with explicit type hints, descriptive docstrings, and Pydantic parameter schemas",
            "ToolNode in LangGraph: Prebuilt or custom execution node that receives tool call payloads and invokes underlying Python functions",
            "Loopback Edge: Routing ToolNode output back to the agent node so the LLM can evaluate whether additional tools are required"
        ],
        "takeaways": [
            "LLMs do not execute code directly; they generate structured JSON payloads representing intended function calls.",
            "Tool docstrings are prompt instructions: vague docstrings cause tool hallucination and incorrect arguments.",
            "A ReAct loop allows an agent to recover from empty search results by formulating an alternative query.",
            "Max iteration guards must always be enforced in conditional edges to prevent infinite execution loops."
        ],
        "connection": [
            "Implemented in Sprint 2 to build the single-turn ReAct agent with hybrid retrieval tools.",
            "Extended in Sprint 3 with MCP servers and multiple domain tools."
        ]
    },
    {
        "filename": "12-Agent-Memory-Architectures-and-Reflection.md",
        "title": "Agent Memory Architectures and Reflection Frameworks",
        "type": "Architecture Lecture",
        "teaches": "This lesson analyzes agent memory systems and reflection mechanisms. It categorizes memory into working, short-term, and long-term stores, explaining how agents maintain context over extended workflows. It also presents reflection loops that enable agents to critique and refine their own intermediate work.",
        "key_concepts": [
            "Memory Taxonomy: Working memory (current execution state), Short-term memory (session history), Long-term memory (persistent DB)",
            "Reflection Loops: Self-critique nodes prompting the LLM to verify factual accuracy and constraint compliance before terminating",
            "Context Window Management: Pruning, summarization, and vector retrieval of past conversational history to prevent context overflow",
            "Trajectory Evaluation: Evaluating the validity of the intermediate reasoning steps taken rather than just the final answer"
        ],
        "takeaways": [
            "Working memory lives in the transient graph state; short-term memory requires session checkpointers; long-term memory requires external databases.",
            "Reflection loops significantly reduce hallucination rates in complex synthesis tasks at the cost of additional latency.",
            "Unconstrained memory growth causes context rot: older dialogue turns must be compressed or summarized.",
            "Agent evaluation requires assessing step efficiency: an agent that uses 10 tool calls to find what could be found in 1 is inefficient."
        ],
        "connection": [
            "Completes the theoretical foundations of Sprint 2.",
            "Informs the multi-turn session persistence implemented in Sprint 3."
        ]
    },
    {
        "filename": "13-Multi-Turn-Conversation-Persistence-with-PostgresSaver.md",
        "title": "Multi-Turn Conversation Persistence with PostgresSaver",
        "type": "Implementation Guide & Database Architecture",
        "teaches": "This lesson teaches how to persist conversational agent states across multiple turns using LangGraph checkpointers. It details the transition from in-memory checkpoints (`MemorySaver`) to production database storage (`PostgresSaver`) and explains how `thread_id` manages concurrent user sessions.",
        "key_concepts": [
            "LangGraph Checkpointers: Serializing graph state snapshots at every step to external storage",
            "PostgresSaver: Storing checkpoints in PostgreSQL tables (`checkpoints`, `checkpoint_blobs`, `checkpoint_writes`)",
            "Thread Partitioning: Using `thread_id` in configuration dictionaries to isolate concurrent multi-turn user dialogues",
            "State Inspection & Time-Travel: Querying checkpoint histories to inspect previous states or replay workflows from earlier checkpoints"
        ],
        "takeaways": [
            "Production conversational agents cannot rely on in-memory state; application restarts or container scaling wipe active sessions.",
            "PostgresSaver enables stateless backend API instances: any container can serve any user request given their `thread_id`.",
            "Checkpointing occurs automatically after each node execution, providing out-of-the-box crash recovery.",
            "Time-travel debugging allows developers to rewind a failed agent run to the exact step preceding the error."
        ],
        "connection": [
            "Core architectural advancement implemented in Sprint 3.",
            "Allows the e-commerce chatbot to sustain multi-turn shopping and question-answering dialogues."
        ]
    },
    {
        "filename": "14-Model-Context-Protocol-FastMCP-Microservices.md",
        "title": "Model Context Protocol (MCP) and FastMCP Microservices",
        "type": "Modern Standards & Implementation Guide",
        "teaches": "This lesson teaches Anthropic's Model Context Protocol (MCP) open standard. It demonstrates why bundling tool implementations directly inside agent code creates monolithic bottlenecks and shows how to package tools as independent FastMCP microservices communicating over standard HTTP/SSE transports.",
        "key_concepts": [
            "Model Context Protocol (MCP): Open standard unifying how applications provide tools, prompts, and context to LLMs",
            "MCP Architecture: Host application (LangGraph backend) ↔ Client ↔ Server (FastMCP tool microservice)",
            "FastMCP Framework: High-level Python library for creating MCP servers with decorators and automatic JSON schema generation",
            "Transport Layers: HTTP/SSE for distributed microservices vs. Stdio for local subprocess tools",
            "Security Boundaries: Sandboxing tool execution and file/database access within dedicated microservice containers"
        ],
        "takeaways": [
            "MCP solves the 'M tools × N models' integration problem by establishing a universal protocol standard.",
            "Decoupling tools into FastMCP services allows tools to be updated, scaled, and secured independently of the agent application.",
            "The bootcamp architecture deploys two independent FastMCP servers: `items_mcp_server` and `reviews_mcp_server`.",
            "Custom MCP Tool Nodes in LangGraph dynamically query MCP server tool registries over standard HTTP transports."
        ],
        "connection": [
            "Primary tool integration standard introduced in Sprint 3.",
            "Provides the decoupled microservice architecture orchestrated in Sprint 4 and deployed in Sprint 5."
        ]
    },
    {
        "filename": "15-Human-in-the-Loop-and-LangSmith-Trace-Feedback.md",
        "title": "Human-in-the-Loop (HITL) and LangSmith Trace Feedback",
        "type": "System Reliability & Telemetry Guide",
        "teaches": "This lesson teaches how to implement human oversight checkpoints and capture qualitative user feedback tied to distributed telemetry. It covers LangGraph execution interrupts for high-impact actions and explains how to link frontend user ratings to backend LangSmith trace runs.",
        "key_concepts": [
            "Human-in-the-Loop (HITL): Workflow breakpoints pausing graph execution before sensitive tool calls to await human approval",
            "Graph Interrupts: `interrupt()` functions halting execution while preserving checkpoint state in PostgreSQL",
            "Trace Attribution: Passing backend `trace_id` to the frontend and sending thumbs-up/down ratings back to `/feedback`",
            "Flywheel Dataset Generation: Filtering production traces with negative user feedback to build targeted regression evaluation sets"
        ],
        "takeaways": [
            "Autonomous agents in high-stakes domains must have explicit human sign-off gates before committing irreversible actions.",
            "LangGraph checkpointers make human-in-the-loop seamless by persisting state indefinitely while waiting for user interaction.",
            "Capturing user feedback without trace IDs is useless; feedback must be mathematically attached to the exact LLM run.",
            "Production feedback loops turn user complaints into automated test cases that permanently prevent repeat errors."
        ],
        "connection": [
            "Implemented in Sprint 3 to provide real-time feedback collection and safety controls.",
            "Connected to the Streamlit UI and FastAPI backend feedback endpoints."
        ]
    },
    {
        "filename": "16-Server-Sent-Events-SSE-and-Graph-State-Streaming.md",
        "title": "Server-Sent Events (SSE) and Graph State Streaming",
        "type": "Full-Stack Integration Guide",
        "teaches": "This lesson teaches how to eliminate perceived latency in agentic systems by streaming intermediate node events and tokens over Server-Sent Events (SSE). It explains how LangGraph event streams are transformed into SSE packets in FastAPI and consumed reactively in frontend user interfaces.",
        "key_concepts": [
            "Perceived Latency Problem: Multi-step agent reasoning taking 5-15 seconds, causing poor user UX without real-time feedback",
            "LangGraph Stream Modes: `stream_mode=['debug', 'values']` yielding node start, updates, tool calls, and final outputs",
            "Server-Sent Events (SSE): Unidirectional HTTP streaming protocol transmitting real-time text chunks (`data: ...\\n\\n`)",
            "Frontend Event Parsing: Intercepting node status events ('Analysing...', 'Searching...') to render interactive UI progress bars"
        ],
        "takeaways": [
            "Streaming is not optional for agentic AI: users must see immediate confirmation that the system is actively working.",
            "SSE is significantly lighter and simpler to implement over standard HTTP than bidirectional WebSockets for conversational agents.",
            "Separating intermediate status events from final structured payload events ensures clean frontend rendering.",
            "Yielding tool call previews ('Looking for items: wireless headphones') builds user trust by exposing the agent's reasoning path."
        ],
        "connection": [
            "Implemented in Sprint 3 across FastAPI (`agent_stream_wrapper`) and Streamlit.",
            "Maintained across all subsequent multi-agent and production deployment sprints."
        ]
    },
    {
        "filename": "17-Multi-Agent-Systems-Specialization-and-Topologies.md",
        "title": "Multi-Agent Systems: Specialization and Topologies",
        "type": "Architecture Lecture",
        "teaches": "This lesson teaches the fundamental architectural principles of Multi-Agent Systems (MAS). It analyzes why single agents suffer from tool overload, instruction conflict, and context pollution as scopes expand, and contrasts supervisor, hierarchical, and peer-to-peer collaboration topologies.",
        "key_concepts": [
            "Single-Agent Bottlenecks: Context window bloat, tool selection confusion, conflicting system prompt instructions",
            "Agent Specialization: Decomposing systems into narrow, expert agents with isolated prompts and dedicated toolsets",
            "MAS Topologies: Supervisor / Coordinator pattern (central hub), Network / Peer-to-Peer (direct handoffs), Hierarchical (teams of teams)",
            "Trade-Off Analysis: Balancing task separation benefits against inter-agent communication overhead and token costs"
        ],
        "takeaways": [
            "Do not adopt MAS for simple tasks; multi-agent architectures introduce orchestration latency and debugging complexity.",
            "MAS is essential when tools require incompatible prompt behaviors (e.g., precise SQL execution vs. creative natural language synthesis).",
            "The Supervisor pattern provides the strongest control and error recovery guarantees for commercial enterprise applications.",
            "Isolating tools inside specialized agents drastically reduces tool-calling hallucination and argument errors."
        ],
        "connection": [
            "Foundational theory for Sprint 4.",
            "Directly dictates the multi-agent architecture built for the e-commerce capstone."
        ]
    },
    {
        "filename": "18-Coordinator-Supervisor-Orchestrator-Pattern.md",
        "title": "The Coordinator / Supervisor Orchestrator Pattern",
        "type": "Implementation Guide & State Machine Design",
        "teaches": "This lesson teaches how to build a production Coordinator / Supervisor Agent in LangGraph. It details how the coordinator parses user intent, creates multi-step plans, delegates sub-tasks to specialist worker agents, and regains control after worker execution to synthesize the final user response.",
        "key_concepts": [
            "Supervisor Node Design: High-level planner maintaining overall workflow goals and routing decisions",
            "Worker Delegation: Passing sub-task state to specialized agents (e.g., Product Q&A Agent, Shopping Cart Agent)",
            "Control Handback: Worker nodes routing back to the supervisor node upon completion rather than terminating the graph",
            "Dynamic Re-Planning: Enabling the supervisor to adjust the execution plan if a worker encounters missing data or errors"
        ],
        "takeaways": [
            "The Supervisor acts as the conductor of the multi-agent orchestra, preventing workers from executing in uncoordinated loops.",
            "Workers should be stateless sub-graphs that execute their specific function and report findings back to shared state.",
            "Explicit router conditions ensure deterministic control flow between supervisor and specialist agents.",
            "Supervisor planning prompts must include the capabilities and boundaries of each available worker agent."
        ],
        "connection": [
            "Core architectural centerpiece of Sprint 4.",
            "Orchestrates the Product Q&A Agent and Shopping Cart Agent in the capstone repository."
        ]
    },
    {
        "filename": "19-Agent-to-Agent-A2A-Communication-Protocols.md",
        "title": "Agent-to-Agent (A2A) Communication Protocols",
        "type": "Protocol Standards Guide",
        "teaches": "This lesson teaches standardized communication protocols for inter-agent messaging. It explores message envelope schemas, intent handoffs, state encapsulation, and Google's `a2a-sdk` for building distributed, framework-agnostic agent networks.",
        "key_concepts": [
            "A2A Message Envelopes: Standardized JSON schemas containing sender ID, recipient ID, session token, intent, and payload",
            "Handoff Mechanisms: Transferring conversation context and control between agents across process boundaries",
            "`a2a-sdk`: Google's open protocol library for establishing remote agent-to-agent client/server connections",
            "State Encapsulation: Ensuring private agent scratchpads are not exposed across public inter-agent communication channels"
        ],
        "takeaways": [
            "Ad-hoc dictionary passing does not scale across distributed services; standardized message schemas are mandatory.",
            "A2A protocols enable cross-framework collaboration (e.g., a LangGraph supervisor orchestrating a Google ADK worker).",
            "Handoff tokens ensure that conversational continuity and security permissions persist across agent delegations.",
            "Remote A2A servers allow specialized agent services to scale independently across dedicated compute clusters."
        ],
        "connection": [
            "Introduced in Sprint 4 and implemented practically with remote servers in Sprint 5.",
            "Prepares AI engineers for modern distributed agentic architectures."
        ]
    },
    {
        "filename": "20-Production-Deployment-Docker-Compose-Architecture.md",
        "title": "Production Deployment and Multi-Container Docker Architecture",
        "type": "DevOps & Infrastructure Guide",
        "teaches": "This lesson teaches how to containerize and deploy complex multi-service AI applications. It covers multi-stage Docker builds for Python services, volume management for stateful databases, and Docker Compose orchestration across API, frontend, vector DB, relational DB, and MCP servers.",
        "key_concepts": [
            "Multi-Stage Dockerfiles: Minimizing container image sizes by separating build dependencies from runtime environments",
            "Docker Compose Orchestration: Defining service dependencies, environment variable injection, network bridges, and restart policies",
            "Stateful vs. Stateless Separation: Containerizing stateless application code while mounting persistent volumes for Postgres and Qdrant",
            "Health Checks & Readiness Probes: Ensuring vector and database services are fully initialized before API startup"
        ],
        "takeaways": [
            "AI applications are distributed systems requiring disciplined container orchestration.",
            "The bootcamp architecture coordinates 6 distinct container services in a unified Docker network.",
            "Volume mounts (`./qdrant_data`, `./postgres_data`) ensure vector indices and conversational checkpointers survive container restarts.",
            "Using slim base images and UV in Dockerfiles reduces container build times from minutes to seconds."
        ],
        "connection": [
            "Culmination of system infrastructure covered in Sprint 5.",
            "Powers the reproducible deployment of the entire bootcamp capstone product."
        ]
    },
    {
        "filename": "21-Latency-Cost-Optimization-and-Prompt-Caching.md",
        "title": "Latency, Cost Optimization, and Prompt Caching Mechanics",
        "type": "Cost Engineering & Performance Guide",
        "teaches": "This lesson provides an in-depth financial and latency engineering breakdown for production LLM systems. It covers provider prompt caching mechanics, showing how disciplined prompt structuring unlocks 50-80% cost and latency reductions, alongside speculative decoding and token streaming.",
        "key_concepts": [
            "LLM Cost Economics: Input token pricing, output token pricing, and cost multiplication in iterative agent loops",
            "Prompt Caching Mechanics: Reusing pre-computed KV cache prefixes for identical prompt beginnings (e.g., Anthropic, OpenAI)",
            "Prefix Alignment Rule: Keeping system instructions, tool definitions, and few-shot examples strictly static at the beginning of prompts",
            "Dynamic Tail Rule: Placing dynamic variables (timestamps, user inputs, retrieved context) strictly at the end of prompt schemas"
        ],
        "takeaways": [
            "Prompt caching transforms agentic economics: static system instructions and tool definitions can be cached at up to 80% discount.",
            "A single dynamic character at the beginning of a prompt invalidates the entire downstream KV cache.",
            "Always audit prompt templates to ensure variable parts are positioned at the extreme end of the message payload.",
            "Optimizing token counts directly reduces time-to-first-token (TTFT) and overall API latency."
        ],
        "connection": [
            "Core technical optimization taught in Sprint 5.",
            "Directly applied to reduce operational costs of the capstone e-commerce agent."
        ]
    },
    {
        "filename": "22-LiteLLM-Router-and-Model-Fallback-Cascades.md",
        "title": "LiteLLM Router and Model Fallback Cascades",
        "type": "Reliability Engineering Guide",
        "teaches": "This lesson teaches how to eliminate single-point-of-failure risks in AI applications using LiteLLM Router. It explains how to implement automated fallback cascades across different foundation model providers, ensuring continuous system availability during provider rate limits, outages, or latency spikes.",
        "key_concepts": [
            "Single Provider Risk: Vulnerability to vendor outages, API rate limit exhaustion (HTTP 429), and localized latency degradation",
            "LiteLLM Router: Python proxy routing requests across OpenAI, Anthropic, Google Vertex AI, and local Ollama instances",
            "Fallback Cascades: Automatically routing failed GPT-4o calls to Claude-3-5-Sonnet or Gemini-1.5-Pro without throwing client errors",
            "Load Balancing & Cooldowns: Distributing traffic across multiple API keys and temporarily shelving degraded endpoints"
        ],
        "takeaways": [
            "Commercial enterprise applications cannot rely on a single foundation model API.",
            "LiteLLM Router standardizes API calling syntax across 100+ providers behind a unified OpenAI-compatible interface.",
            "Fallback configurations should match model capabilities: pair primary frontier models with comparable secondary reasoning models.",
            "Automated retries with exponential backoff and provider fallbacks achieve 99.9% application uptime."
        ],
        "connection": [
            "Implemented in Sprint 5 to harden the backend against third-party API disruptions.",
            "Ensures production reliability for the final capstone deployment."
        ]
    },
    {
        "filename": "23-Securing-AI-Systems-Guardrails-and-Injection-Defenses.md",
        "title": "Securing AI Systems: Guardrails and Prompt Injection Defenses",
        "type": "Cybersecurity & Safety Standard",
        "teaches": "This lesson teaches production security practices for agentic AI applications based on the OWASP Top 10 for LLMs. It covers defenses against direct and indirect prompt injection, data exfiltration, unauthorized tool invocation, and input/output guardrails.",
        "key_concepts": [
            "OWASP Top 10 for LLMs: Prompt injection, insecure output handling, training data poisoning, and excessive agency",
            "Direct vs. Indirect Injection: User jailbreaks versus malicious instructions embedded in retrieved external data (e.g. product reviews)",
            "Least-Privilege Tool Scoping: Restricting agent tool capabilities to prevent unintended database writes or data exposure",
            "Input/Output Guardrails: Secondary classifier models (e.g., Llama Guard, NeMo Guardrails) vetting requests and generations"
        ],
        "takeaways": [
            "Treat all retrieved external data (reviews, web pages, PDFs) as untrusted user input susceptible to indirect injection.",
            "Never give agents blanket database credentials; use constrained parameterized query tools with strict input validation.",
            "Model Context Protocol (MCP) servers provide process isolation, preventing tools from compromising host server environments.",
            "Guardrails should be implemented as lightweight deterministic filters before invoking heavy LLM reasoning loops."
        ],
        "connection": [
            "Essential enterprise hardening covered in Sprint 5.",
            "Protects the e-commerce shopping agent from malicious item review payloads and prompt injections."
        ]
    },
    {
        "filename": "24-Automated-Evaluation-Gating-and-CI-Pipelines.md",
        "title": "Automated Evaluation Gating and CI/CD Pipelines for AI",
        "type": "MLOps & CI/CD Guide",
        "teaches": "This lesson teaches how to construct automated Continuous Integration (CI) evaluation gates for AI software repositories. It demonstrates how to run headless regression tests against golden evaluation datasets on GitHub pull requests, blocking deployments if retrieval recall or generation faithfulness falls below established thresholds.",
        "key_concepts": [
            "Continuous Evaluation (CI for AI): Treating evaluation datasets and metrics as automated software test suites",
            "Retriever Precision/Recall Gates: Running automated scripts (`eval_retriever.py`) to verify vector retrieval accuracy on code commits",
            "Evaluation Thresholds: Setting hard pass/fail criteria (e.g., minimum 85% Hit Rate@5, minimum 90% Faithfulness score)",
            "Automated GitHub Actions: Triggering headless Dockerized evaluation runs prior to merging code or deploying images"
        ],
        "takeaways": [
            "Prompt and code changes must never be merged based on manual gut feeling; quantitative CI gates are mandatory.",
            "Headless evaluation scripts should evaluate both retrieval (Hit Rate, MRR) and generation (Faithfulness, Relevance).",
            "Evaluation datasets must be versioned alongside codebase commits in the repository.",
            "Automated CI testing catches regressions caused by subtle prompt tweaks or embedding model upgrades before users are impacted."
        ],
        "connection": [
            "Final engineering discipline taught in Sprint 5.",
            "Validates the completed capstone codebase prior to cohort Demo Day."
        ]
    }
]

for ldata in lessons_data:
    fp = os.path.join(LESSONS_DIR, ldata["filename"])
    lines = []
    lines.append(f"# {ldata['title']}")
    lines.append("")
    lines.append(f"Type: {ldata['type']}")
    lines.append("")
    lines.append("## What it teaches")
    lines.append("")
    lines.append(ldata["teaches"])
    lines.append("")
    lines.append("## Key concepts")
    lines.append("")
    for kc in ldata["key_concepts"]:
        lines.append(f"- {kc}")
    lines.append("")
    lines.append("## Important takeaways")
    lines.append("")
    for it in ldata["takeaways"]:
        lines.append(f"- {it}")
    lines.append("")
    lines.append("## Connection to section")
    lines.append("")
    for cs in ldata["connection"]:
        lines.append(f"- {cs}")
    lines.append("")
    
    with open(fp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Generated {fp}")

print(f"All {len(lessons_data)} individual lesson summaries generated successfully.")
