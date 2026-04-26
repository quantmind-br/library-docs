---
title: Signals | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/interacting-with-workflows/signals
source: sitemap
fetched_at: 2026-04-26T04:14:19.735088107-03:00
rendered_js: false
word_count: 173
summary: This document explains how to use signals to facilitate asynchronous communication with running workflows, including parameter validation and signal handling patterns.
tags:
    - asynchronous-communication
    - workflow-management
    - signal-handling
    - payload-validation
    - pydantic-models
    - event-driven
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Signals allow external systems to send messages to running workflows asynchronously.

Signals use asynchronous communication and can be sent at any time during workflow execution. Workflows must explicitly handle signals, and signals can carry payload data.

## Signal Handler

The workflow below listens for `add_notification` signals indefinitely. Each time a signal arrives, it appends the message to an internal list and processes it. The `wait_condition` call suspends execution until new notifications are available, avoiding busy-waiting:

```python
```

## Parameter Validation

Signal handlers declare their expected parameters explicitly, and the SDK enforces this contract on every incoming payload. Signals validate incoming payloads against their declared parameters. Incoming data is checked against the expected types, and any extra fields not declared in the handler signature are rejected. Validation failures return HTTP 422 (Unprocessable Entity) with a descriptive error message.

For complex input structures, use Pydantic models. The SDK will automatically deserialize the incoming payload into the model and validate each field:

```python
```

Once your workflow is running and listening for signals, you can send one from the outside using the SDK or the API.