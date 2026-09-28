# Model Context Protocol (MCP) and FastMCP Microservices

Type: Modern Standards & Implementation Guide

## What it teaches

This lesson teaches Anthropic's Model Context Protocol (MCP) open standard. It demonstrates why bundling tool implementations directly inside agent code creates monolithic bottlenecks and shows how to package tools as independent FastMCP microservices communicating over standard HTTP/SSE transports.

## Key concepts

- Model Context Protocol (MCP): Open standard unifying how applications provide tools, prompts, and context to LLMs
- MCP Architecture: Host application (LangGraph backend) ↔ Client ↔ Server (FastMCP tool microservice)
- FastMCP Framework: High-level Python library for creating MCP servers with decorators and automatic JSON schema generation
- Transport Layers: HTTP/SSE for distributed microservices vs. Stdio for local subprocess tools
- Security Boundaries: Sandboxing tool execution and file/database access within dedicated microservice containers

## Important takeaways

- MCP solves the 'M tools × N models' integration problem by establishing a universal protocol standard.
- Decoupling tools into FastMCP services allows tools to be updated, scaled, and secured independently of the agent application.
- The bootcamp architecture deploys two independent FastMCP servers: `items_mcp_server` and `reviews_mcp_server`.
- Custom MCP Tool Nodes in LangGraph dynamically query MCP server tool registries over standard HTTP transports.

## Connection to section

- Primary tool integration standard introduced in Sprint 3.
- Provides the decoupled microservice architecture orchestrated in Sprint 4 and deployed in Sprint 5.

