---
title: Workflows | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/workflows
source: sitemap
fetched_at: 2026-04-26T04:14:07.213520135-03:00
rendered_js: false
word_count: 442
summary: This document explains the core principles of designing deterministic workflows, focusing on state management, orchestration constraints, and the separation of logic from side-effect-heavy activities.
tags:
    - workflow-orchestration
    - determinism
    - sdk-development
    - event-replay
    - distributed-systems
    - fault-tolerance
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

A **workflow** is the orchestration layer of your application. It defines what needs to happen, in what order, under what conditions — but it does not do the work itself. A workflow coordinates activities, waits for external events, manages timers, and decides how to proceed based on results.

Workflows can run for seconds or months. They survive process restarts, infrastructure failures, and transient errors without losing their place because the platform records every significant event in the lifecycle and uses that record to reconstruct state.

## Fundamental Constraint: Determinism

Workflow code **must be deterministic**. Given the same starting conditions, a workflow must always produce the same sequence of operations.

**Why?** Replay. When a worker restarts or recovers a workflow, it re-executes workflow code from the beginning, matching each operation against the recorded event history. If the code produces a different sequence (because it called `datetime.now()` and got a different timestamp, or `random()` and got a different number), the replay diverges and the workflow fails with a non-determinism error.

Use SDK-provided replacements for non-deterministic operations:

```python
from datetime import datetime
from sdk import random

# Instead of calling datetime.now() directly in a workflow:
now = sdk.now()  # Use SDK-provided time
rand_val = sdk.random()  # Use SDK-provided random
```

Any operation that touches the outside world (API call, database query, file read) belongs in an **activity**, not in the workflow itself.

> [!warning]
> The SDK enforces determinism by default: a sandbox intercepts calls to known non-deterministic APIs and raises an error immediately. You can disable enforcement per-workflow with `enforce_determinism=False`, but keeping it on is strongly recommended.

## Input Validation

The `run` method accepts any JSON-serializable types. When the entrypoint takes a single Pydantic `BaseModel`, its fields become the top-level input keys:

```python
class MyInput(BaseModel):
    name: str
    age: int

@workflow
def my_workflow(input: MyInput):
    ...
```

For different input shapes, use a union of models:

```python
class InputA(BaseModel):
    type: Literal["a"]
    value_a: str

class InputB(BaseModel):
    type: Literal["b"]
    value_b: int

@workflow
def my_workflow(input: InputA | InputB):
    ...
```

SDK validates input against each member in order and passes the first match. Use `extra="forbid"` on each model for precise discrimination.

## Execution Timeout

Every workflow has an `execution_timeout` — the hard cap on its total lifetime including all retries and continue-as-new iterations. The default is **1 hour**. Workflows that need to run longer must opt in:

```python
@workflow.define(execution_timeout=timedelta(hours=24))
def my_long_running_workflow():
    ...
```

## Constraints

| Constraint | Value |
|------------|-------|
| **Timeout between activities** | 2 seconds — workflow code must complete within this time |
| **I/O** | Not allowed in workflows — all network calls, DB queries, file ops go in activities |
| **Input/output limit** | 2MB in and 2MB out per workflow invocation |
| **Execution history limit** | 51,200 events or 50MB — see [Events](https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/events) |

#workflow-orchestration #determinism #sdk-development