---
title: Flowise
url: https://coolify.io/docs/services/flowise.md
source: llms
fetched_at: 2026-02-17T14:44:02.315866-03:00
rendered_js: false
word_count: 97
summary: This document introduces Flowise as an open-source low-code tool for LLM orchestration and details its available deployment configurations, including SQLite and PostgreSQL with Redis variants.
tags:
    - flowise
    - llm-orchestration
    - ai-agents
    - deployment-variants
    - database-configuration
    - coolify
category: reference
---

# Flowise

## What is Flowise

Flowise is an open source low-code tool for developers to build customized LLM orchestration flows & AI agents.

## Deployment Variants

Flowise is available in two deployment configurations in Coolify:

### Flowise (Default)

* **Database:** SQLite (embedded)
* **Use case:** Simple deployments, testing, or personal AI workflow development
* **Components:** Single Flowise container with built-in SQLite database

### Flowise with Databases

* **Database:** PostgreSQL + Redis
* **Use case:** Production deployments requiring better performance, caching, and scalability
* **Components:**
  * Flowise container
  * PostgreSQL container for data persistence
  * Redis container for caching and session management
  * Automatic database configuration and health checks

## Links

* [Official Documentation](https://docs.flowiseai.com/?utm_source=coolify.io)