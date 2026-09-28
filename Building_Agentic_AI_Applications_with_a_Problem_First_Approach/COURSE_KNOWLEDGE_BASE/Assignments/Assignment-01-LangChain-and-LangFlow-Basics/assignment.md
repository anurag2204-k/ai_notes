# Assignment 1: Detailed Specifications & Requirements

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
