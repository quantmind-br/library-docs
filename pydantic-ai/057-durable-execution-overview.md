---
title: Overview - Pydantic AI
url: https://ai.pydantic.dev/durable_execution/overview/
source: sitemap
fetched_at: 2026-01-22T22:25:12.68373077-03:00
rendered_js: false
word_count: 82
summary: This document explains how Pydantic AI supports durable execution to create fault-tolerant, long-running agents that persist progress across failures and restarts.
tags:
    - durable-execution
    - pydantic-ai
    - fault-tolerance
    - temporal
    - dbos
    - prefect
category: concept
---

## Durable Execution

Pydantic AI allows you to build durable agents that can preserve their progress across transient API failures and application errors or restarts, and handle long-running, asynchronous, and human-in-the-loop workflows with production-grade reliability. Durable agents have full support for [streaming](https://ai.pydantic.dev/agents/#streaming-all-events) and [MCP](https://ai.pydantic.dev/mcp/client/), with the added benefit of fault tolerance.

Pydantic AI natively supports three durable execution solutions:

- [Temporal](https://ai.pydantic.dev/durable_execution/temporal/)
- [DBOS](https://ai.pydantic.dev/durable_execution/dbos/)
- [Prefect](https://ai.pydantic.dev/durable_execution/prefect/)

These integrations only use Pydantic AI's public interface, so they also serve as a reference for integrating with other durable systems.