---
title: Streaming Events | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/streaming
source: sitemap
fetched_at: 2026-04-26T04:13:46.71883695-03:00
rendered_js: false
word_count: 169
summary: This document explains how to publish real-time streaming events from within workflows and activities using a task-based approach to power interactive features like UI updates or LLM token streaming.
tags:
    - real-time-streaming
    - event-driven
    - workflow-automation
    - state-updates
    - event-publishing
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Stream events in real-time from your workflows and activities to power live UIs, progress indicators, and token-by-token LLM responses.

## Publishing Events

Inside an activity, use the `Task` context manager to publish events. A `Task` represents a named stream of state updates that external consumers can subscribe to. The `type` parameter is a topic name you choose (e.g., `"token-stream"`), and `state` is the initial payload. Each call to `update_state()` publishes the new state as an event to all subscribers in real time.

When the `async with` block exits, the task is marked as complete and a terminal event is published.

See [Consuming Streaming Events](https://docs.mistral.ai/studio-api/workflows/building-workflows/consuming_events) for details on subscribing to events.

## Common Patterns

The most common pattern — stream tokens as they're generated:

```python
```

Report progress during long operations:

```python
```

## Best Practices

The `type` parameter is a topic name you define. Best practices:
- Use lowercase with underscores
- Keep names short and descriptive
- Use consistent naming across your app

> [!warning] Events have a **1MB message limit**. For large data, split into multiple events.

Each published event is wrapped with context: