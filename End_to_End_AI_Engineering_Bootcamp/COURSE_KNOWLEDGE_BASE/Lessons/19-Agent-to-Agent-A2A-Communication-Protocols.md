# Agent-to-Agent (A2A) Communication Protocols

Type: Protocol Standards Guide

## What it teaches

This lesson teaches standardized communication protocols for inter-agent messaging. It explores message envelope schemas, intent handoffs, state encapsulation, and Google's `a2a-sdk` for building distributed, framework-agnostic agent networks.

## Key concepts

- A2A Message Envelopes: Standardized JSON schemas containing sender ID, recipient ID, session token, intent, and payload
- Handoff Mechanisms: Transferring conversation context and control between agents across process boundaries
- `a2a-sdk`: Google's open protocol library for establishing remote agent-to-agent client/server connections
- State Encapsulation: Ensuring private agent scratchpads are not exposed across public inter-agent communication channels

## Important takeaways

- Ad-hoc dictionary passing does not scale across distributed services; standardized message schemas are mandatory.
- A2A protocols enable cross-framework collaboration (e.g., a LangGraph supervisor orchestrating a Google ADK worker).
- Handoff tokens ensure that conversational continuity and security permissions persist across agent delegations.
- Remote A2A servers allow specialized agent services to scale independently across dedicated compute clusters.

## Connection to section

- Introduced in Sprint 4 and implemented practically with remote servers in Sprint 5.
- Prepares AI engineers for modern distributed agentic architectures.

