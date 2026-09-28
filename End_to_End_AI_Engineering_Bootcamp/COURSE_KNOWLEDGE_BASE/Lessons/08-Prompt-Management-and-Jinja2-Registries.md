# Decoupled Prompt Management and Jinja2 Registries

Type: Software Engineering Best Practice

## What it teaches

This lesson teaches professional prompt engineering and management practices. It demonstrates why hardcoding prompt strings inside application code creates severe maintenance debt and shows how to decouple prompts into version-controlled YAML files rendered via Jinja2 templates.

## Key concepts

- Decoupled Prompt Architecture: Separating system prompts, few-shot examples, and task instructions from application logic
- Jinja2 Template Engines: Parameterizing prompts with loops, conditionals, and variables for dynamic rendering
- YAML Prompt Registries: Version-controlled files specifying model parameters (temperature, max_tokens) alongside prompt text
- Prompt Versioning & CI Testing: Treating prompts as executable code subject to unit testing and regression evaluation

## Important takeaways

- Never scatter raw prompt strings or f-strings across Python business logic modules.
- Jinja2 enables clean conditional logic in prompts (e.g., rendering few-shot examples only when available).
- YAML configuration registries allow prompt engineers and domain experts to update prompts without modifying backend code.
- Standardized prompt loaders ensure that temperature, system instructions, and schemas are applied deterministically.

## Connection to section

- Implemented in Sprint 1 for retrieval generation prompts.
- Standardizes prompt handling for intent routers, QA agents, and coordinators in Sprints 2, 3, and 4.

