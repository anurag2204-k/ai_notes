# Assignment 1 Resources & Starter Code

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
router_prompt = ChatPromptTemplate.from_template("""
Given the user input below, classify it into one of: 'calculator', 'general'.
Input: {input}
Classification:""")

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
