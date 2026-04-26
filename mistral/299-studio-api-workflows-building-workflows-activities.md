---
title: Activities | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/activities
source: sitemap
fetched_at: 2026-04-26T04:13:29.757051419-03:00
rendered_js: false
word_count: 97
summary: This document defines the role and characteristics of activities as fundamental units of work within a workflow-based application architecture.
tags:
    - workflow-orchestration
    - distributed-systems
    - task-execution
    - idempotency
    - data-serialization
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Activities perform the actual work in your application while workflows coordinate them.

An activity is a unit of work that performs actual computations, API calls, or other operations. Key characteristics:

- Must be idempotent (safe to retry)
- Execute in isolated processes
- Have automatic retry mechanisms
- Accept any JSON-serializable types as inputs/outputs (str, int, dict, list, etc.)
- Input/output limited to 2MB

## Related

- [Basics](https://docs.mistral.ai/studio-api/workflows/building-workflows/activities/basics) — defining activities, core features, granularity, and nesting
- [Local Activities](https://docs.mistral.ai/studio-api/workflows/building-workflows/activities/local_activities) — run activities directly in the worker process for low-latency operations
- [Sticky Worker Sessions](https://docs.mistral.ai/studio-api/workflows/building-workflows/activities/sticky_worker_sessions) — route related activities to the same worker for resource sharing