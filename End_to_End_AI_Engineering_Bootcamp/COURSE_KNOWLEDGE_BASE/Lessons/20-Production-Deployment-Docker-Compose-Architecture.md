# Production Deployment and Multi-Container Docker Architecture

Type: DevOps & Infrastructure Guide

## What it teaches

This lesson teaches how to containerize and deploy complex multi-service AI applications. It covers multi-stage Docker builds for Python services, volume management for stateful databases, and Docker Compose orchestration across API, frontend, vector DB, relational DB, and MCP servers.

## Key concepts

- Multi-Stage Dockerfiles: Minimizing container image sizes by separating build dependencies from runtime environments
- Docker Compose Orchestration: Defining service dependencies, environment variable injection, network bridges, and restart policies
- Stateful vs. Stateless Separation: Containerizing stateless application code while mounting persistent volumes for Postgres and Qdrant
- Health Checks & Readiness Probes: Ensuring vector and database services are fully initialized before API startup

## Important takeaways

- AI applications are distributed systems requiring disciplined container orchestration.
- The bootcamp architecture coordinates 6 distinct container services in a unified Docker network.
- Volume mounts (`./qdrant_data`, `./postgres_data`) ensure vector indices and conversational checkpointers survive container restarts.
- Using slim base images and UV in Dockerfiles reduces container build times from minutes to seconds.

## Connection to section

- Culmination of system infrastructure covered in Sprint 5.
- Powers the reproducible deployment of the entire bootcamp capstone product.

