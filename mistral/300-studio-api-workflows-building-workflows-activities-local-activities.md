---
title: Local Activities | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/activities/local_activities
source: sitemap
fetched_at: 2026-04-26T04:13:34.493571829-03:00
rendered_js: false
word_count: 206
summary: This document explains the use of local activities to optimize performance for short-lived tasks by executing them directly within the workflow worker process.
tags:
    - performance-optimization
    - workflow-management
    - task-scheduling
    - latency-reduction
    - local-activities
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Local activities run directly in the workflow worker process, bypassing the task queue for low-latency execution of short operations (< 1 second).

## When to Use

**Good for:**
- Quick computations, validations, data transformations
- High-volume scenarios where latency matters
- Operations completing in under 1 second

**Avoid for:**
- Long-running operations (> a few seconds)
- External API calls or I/O-heavy tasks
- Operations needing separate retry isolation or scaling

## Trade-offs

Bypasses standard scheduling:
- No task queue isolation — activities share resources with workflows
- Worker process blocking — slow local activities block the workflow worker
- No independent scaling — cannot scale local activities separately
- Limited failure isolation — worker crashes affect both workflows and local activities

> [!warning] Local activities can cause worker crashes if they fail unexpectedly. Unlike regular activities, local activity failures can bring down the entire worker process, potentially causing data loss and requiring manual intervention to restart the workflow.

## Supported Features

Activity settings (partial support):
- Timeouts — supported
- Retry policies — supported
- Dependency injection — supported
- Rate limiting — NOT supported

> [!note] The `sticky_to_worker`, `rate_limit`, and `heartbeat_timeout` parameters don't apply to local activities since they already run in the workflow worker process.