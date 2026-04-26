---
title: Executions | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/executions
source: sitemap
fetched_at: 2026-04-26T04:14:03.582013555-03:00
rendered_js: false
word_count: 226
summary: This document describes the lifecycle, status states, and invocation process for workflow executions within the Mistral platform.
tags:
    - workflow-execution
    - execution-id
    - workflow-management
    - mistral-sdk
    - execution-states
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

An **execution** is a single invocation of a workflow. Each execution has a unique `execution_id` (auto-generated or specified by the caller) and progresses through a sequence of statuses as it runs.

## Starting an Execution

Start a workflow execution from client code using the Mistral SDK:

```python
execution = client.workflows.runs.launch(
    workflow_identifier="my-workflow",
    input={"key": "value"},
    execution_id="optional-custom-id"
)
```

The `workflow_identifier` must match the `name` you passed to `@workflows.workflow.define()`. The returned `execution` object contains the `execution_id` and initial `status` (typically `RUNNING`).

You can also trigger executions from the [Mistral Console](https://console.mistral.ai/) or via a schedule.

## Execution States

An execution starts as `RUNNING` and ends in one of several terminal states:

| State | Description |
|-------|-------------|
| `COMPLETED` | Finished successfully |
| `FAILED` | Terminated with an unhandled error |
| `CANCELED` | Gracefully stopped |
| `TERMINATED` | Forcefully stopped |
| `TIMED_OUT` | Exceeded `execution_timeout` |
| `CONTINUED_AS_NEW` | History reset via continue-as-new |
| `RETRYING_AFTER_ERROR` | Failed and scheduled for retry |

## Execution vs. Run

An **execution** is a workflow invocation with a stable `execution_id` that persists across its entire lifetime. A **run** is a single attempt within that execution.

Most of the time, an execution has exactly one run. But if a workflow is reset to a previous point in its history, a **new run begins under the same `execution_id`**.

> [!warning]
> Only one run can be active at a time. API action endpoints (`/cancel`, `/terminate`, `/signals`, `/queries`, `/updates`) always target the **latest run** of an execution.

#workflow-execution #execution-states #mistral-sdk