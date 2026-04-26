---
title: Sticky Worker Sessions | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/activities/sticky_worker_sessions
source: sitemap
fetched_at: 2026-04-26T04:13:35.608033905-03:00
rendered_js: false
word_count: 180
summary: This document explains the concept of sticky worker sessions in task orchestration, outlining their benefits for stateful operations and resource reuse, as well as the risks regarding availability and resource contention.
tags:
    - sticky-sessions
    - worker-affinity
    - stateful-processing
    - resource-optimization
    - workflow-design
    - distributed-systems
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Sticky worker sessions route multiple activities to the same worker instance, enabling resource reuse and stateful operations across activity calls.

## When to Use

**Good for:**
- Sharing expensive resources (ML models, database connections, cached data)
- Stateful data processing across multiple activity calls
- Reducing initialization overhead for related operations

**Avoid for:**
- Activities that must be highly available (session breaks if worker crashes)
- Long-running workflows (ties up specific worker resources)
- When worker-level state isn't needed

## Session Lifecycle

**Session breaks on worker failure:**
- If the worker crashes or scales down, the session ends
- Subsequent activities route to a different worker
- Design activities to handle cold starts gracefully

**In-memory state only:**
- Worker-level state is lost on worker restart or redeployment
- Use databases or external storage for persistent state
- Not a replacement for distributed state management

**Worker resource contention:**
- Long-running sessions tie up specific worker capacity
- Can create hot spots if many workflows target the same worker
- Monitor worker utilization to avoid resource starvation

> [!note] The `sticky_to_worker` parameter doesn't apply to local activities since they already run in the workflow worker process.