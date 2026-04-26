---
title: Events | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/events
source: sitemap
fetched_at: 2026-04-26T04:14:01.976555813-03:00
rendered_js: false
word_count: 307
summary: This document explains the role of execution history and determinism in enabling reliable, fault-tolerant workflow replay, along with constraints and management techniques like continue-as-new.
tags:
    - workflow-orchestration
    - execution-history
    - determinism
    - fault-tolerance
    - workflow-replay
    - durable-execution
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Every significant action in a workflow's lifetime produces an **event**: the workflow started, an activity was scheduled, an activity completed, a signal was received, the workflow finished. These events are recorded in order, forming an **append-only log** called the **execution history**.

## How Replay Works

The execution history makes **durable execution** possible. It is the source of truth for a workflow's state. When a worker needs to resume a workflow (after a crash, restart, or task reassignment), it replays the execution history from the beginning.

During replay:
- Workflow code runs again from the top
- Completed activities are **not** re-executed — their results are read back from the history
- Because workflow code is **deterministic**, the same sequence of operations is produced every time
- The workflow arrives back at exactly the point where it was interrupted

This is the mechanism that makes workflows resilient to failures **without any recovery code on your part**.

## Determinism Requirement

Determinism is what makes replay reliable: if workflow code produces a different sequence of operations on replay (because it called `datetime.now()` or `random()` and got different values), the replay diverges from the recorded history and the workflow fails.

> [!warning]
> Non-deterministic operations must happen in **activities**, not in workflow code.

## History Limits

Each execution history is bounded: **51,200 events** or **50MB**, whichever comes first.

For workflows that run for a very long time or process very large volumes of work, the platform provides **continue-as-new**: a workflow can carry its essential state forward into a fresh history without interrupting execution.

> [!note]
> The events described here are **execution history events** — the internal record of workflow progress used for durability and replay. The platform also supports **streaming events** that can be consumed in real time by external systems, covered in [Streaming](https://docs.mistral.ai/studio-api/workflows/building-workflows/streaming).

#workflow-orchestration #execution-history #determinism