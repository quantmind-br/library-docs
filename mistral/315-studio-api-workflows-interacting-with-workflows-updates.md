---
title: Updates | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/interacting-with-workflows/updates
source: sitemap
fetched_at: 2026-04-26T04:14:22.459369045-03:00
rendered_js: false
word_count: 190
summary: This document explains the mechanism of synchronous workflow updates, detailing how they handle state modifications, return values, and input validation within an external communication context.
tags:
    - workflow-updates
    - synchronous-communication
    - data-validation
    - state-management
    - pydantic-models
    - api-design
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Updates allow external systems to modify workflow state and receive a response. Unlike signals, updates are synchronous and can return values.

Updates use synchronous communication and return a response to the caller. Unlike signals, they can modify workflow state, return values, and execute activities as part of handling the request.

## Update Handler

The workflow below exposes an `update_data` handler that runs an activity, updates internal state, and returns a result to the caller — all in a single synchronous call. This makes updates the right choice when the caller needs confirmation that the operation completed.

```python
```

## Parameter Validation

Update handlers declare their expected parameters, and the SDK validates the payload before the handler runs. Updates validate incoming payloads against their declared parameters. Incoming data is checked against the expected types, and any extra fields not declared in the handler signature are rejected. Validation failures return HTTP 422 (Unprocessable Entity) with a descriptive error message.

For complex input structures, use Pydantic models. This is especially useful when an update carries several related fields that belong together:

```python
```

Once your workflow is running, you can send an update from the outside and receive the handler's return value synchronously.