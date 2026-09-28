# Securing AI Systems: Guardrails and Prompt Injection Defenses

Type: Cybersecurity & Safety Standard

## What it teaches

This lesson teaches production security practices for agentic AI applications based on the OWASP Top 10 for LLMs. It covers defenses against direct and indirect prompt injection, data exfiltration, unauthorized tool invocation, and input/output guardrails.

## Key concepts

- OWASP Top 10 for LLMs: Prompt injection, insecure output handling, training data poisoning, and excessive agency
- Direct vs. Indirect Injection: User jailbreaks versus malicious instructions embedded in retrieved external data (e.g. product reviews)
- Least-Privilege Tool Scoping: Restricting agent tool capabilities to prevent unintended database writes or data exposure
- Input/Output Guardrails: Secondary classifier models (e.g., Llama Guard, NeMo Guardrails) vetting requests and generations

## Important takeaways

- Treat all retrieved external data (reviews, web pages, PDFs) as untrusted user input susceptible to indirect injection.
- Never give agents blanket database credentials; use constrained parameterized query tools with strict input validation.
- Model Context Protocol (MCP) servers provide process isolation, preventing tools from compromising host server environments.
- Guardrails should be implemented as lightweight deterministic filters before invoking heavy LLM reasoning loops.

## Connection to section

- Essential enterprise hardening covered in Sprint 5.
- Protects the e-commerce shopping agent from malicious item review payloads and prompt injections.

