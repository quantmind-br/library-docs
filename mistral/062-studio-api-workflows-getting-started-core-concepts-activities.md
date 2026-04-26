---
title: Activities | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/activities
source: sitemap
fetched_at: 2026-04-26T04:13:56.684801795-03:00
rendered_js: false
word_count: 219
summary: This document explains the role of activities in workflow execution, detailing their purpose for handling side effects, I/O operations, and the requirements for idempotency and configuration.
tags:
    - workflow-orchestration
    - distributed-systems
    - idempotency
    - async-functions
    - activity-execution
    - fault-tolerance
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## What are Activities?

Activities are where the **actual work happens** in a workflow. Sending emails, calling external APIs, running database queries, processing files, generating AI model responses — anything that interacts with the outside world or has side effects belongs here, not in the workflow itself.

Activities are ordinary async functions. They have no constraints around determinism: they can call anything, use any library, read from disk, write to a database.

The platform treats each activity call as **atomic** — if an activity fails, it is retried automatically according to a configurable policy. Once it succeeds, its result is recorded in the execution history and the workflow moves on.

## Idempotency

Because results are persisted, a successful activity is **never re-executed on replay** — only its recorded result is used. This means activities should be **idempotent**: running them twice with the same input should produce the same observable outcome, in case a retry happens after a partial execution.

## Configuration

Activities are called with `await` directly inside workflow code:

```python
@workflow
def my_workflow():
    result = await my_activity("input")
```

Configure retries and timeouts on the decorator:

```python
@activity.defn
async def my_activity(input: str) -> str:
    ...
```

> [!warning]
> Always set `start_to_close_timeout` — without it, a hung activity blocks indefinitely.

## Constraints

| Constraint | Value |
|------------|-------|
| **Input/output limit** | 2MB in and 2MB out |
| **Async only** | Use async libraries for I/O; blocking calls stall the worker for all concurrent activities |

#workflow-orchestration #idempotency #async-functions