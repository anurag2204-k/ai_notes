# Multi-Turn Conversation Persistence with PostgresSaver

Type: Implementation Guide & Database Architecture

## What it teaches

This lesson teaches how to persist conversational agent states across multiple turns using LangGraph checkpointers. It details the transition from in-memory checkpoints (`MemorySaver`) to production database storage (`PostgresSaver`) and explains how `thread_id` manages concurrent user sessions.

## Key concepts

- LangGraph Checkpointers: Serializing graph state snapshots at every step to external storage
- PostgresSaver: Storing checkpoints in PostgreSQL tables (`checkpoints`, `checkpoint_blobs`, `checkpoint_writes`)
- Thread Partitioning: Using `thread_id` in configuration dictionaries to isolate concurrent multi-turn user dialogues
- State Inspection & Time-Travel: Querying checkpoint histories to inspect previous states or replay workflows from earlier checkpoints

## Important takeaways

- Production conversational agents cannot rely on in-memory state; application restarts or container scaling wipe active sessions.
- PostgresSaver enables stateless backend API instances: any container can serve any user request given their `thread_id`.
- Checkpointing occurs automatically after each node execution, providing out-of-the-box crash recovery.
- Time-travel debugging allows developers to rewind a failed agent run to the exact step preceding the error.

## Connection to section

- Core architectural advancement implemented in Sprint 3.
- Allows the e-commerce chatbot to sustain multi-turn shopping and question-answering dialogues.

