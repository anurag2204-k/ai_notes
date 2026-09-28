# Assignment 5 — Multi-Agent System Coordination & Transactional Tooling — Requirements & Specification

### Objectives
Decompose complex e-commerce interactions into specialized, collaborative agents governed by a centralized Coordinator.

### Requirements & Constraints
1. **Shopping Cart DB Tools**: PostgreSQL tables must support atomic insert, select, and delete operations by `user_id`.
2. **Shopping Cart Agent**: Specialized sub-agent with prompt focused strictly on cart management. Has zero access to vector retrieval tools.
3. **Coordinator Agent**:
   - Parses composite queries (e.g., 'Find noise-cancelling headphones and add the top rated one to my cart').
   - Formulates multi-step execution plan.
   - Delegates Step 1 to Product Q&A Agent and Step 2 to Shopping Cart Agent.
   - Regains control after each step to update shared state.
4. **UI Synchronization**: Shopping cart sidebar in Streamlit must automatically re-render current cart contents upon tool completion.

### Expected Deliverables
- Database migration script / tool definitions for shopping cart in PostgreSQL.
- Coordinator and Shopping Cart agent definitions in `apps/api/src/api/agents/agents.py`.
- Multi-agent LangGraph workflow in `apps/api/src/api/agents/graph.py`.
- Synchronized frontend cart panel in `apps/chatbot_ui/src/chatbot_ui/app.py`.
