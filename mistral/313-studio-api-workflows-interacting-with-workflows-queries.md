---
title: Queries | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/interacting-with-workflows/queries
source: sitemap
fetched_at: 2026-04-26T04:14:16.997346727-03:00
rendered_js: false
word_count: 183
summary: This document explains the purpose and implementation of workflow queries, which allow for synchronous, read-only access to a workflow's current state.
tags:
    - workflow-queries
    - synchronous-communication
    - read-only-access
    - data-validation
    - pydantic-models
    - state-management
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Queries allow external systems to read the current state of a running workflow synchronously.

Queries use synchronous communication and are read-only — they should not modify workflow state. They can be called at any time during execution but must return quickly, making them unsuitable for long-running operations.

## Query Handler

The workflow below tracks its own progress as it runs. The `get_status` query handler reads that state and returns it immediately to the caller — without interrupting or modifying the running workflow:

```python
```

## Parameter Validation

Query handlers can accept parameters just like any other handler, and the SDK validates the payload before invoking the handler. Queries validate incoming payloads against their declared parameters. Incoming data is checked against the expected types, and any extra fields not declared in the handler signature are rejected. Validation failures return HTTP 422 (Unprocessable Entity) with a descriptive error message.

For complex input structures, use Pydantic models. This lets you pass structured parameters to a query handler while keeping full type safety:

```python
```

Once your workflow is running, you can query its state at any time from the outside using the SDK or the API.