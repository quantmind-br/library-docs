---
title: Consuming Streaming Events | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/consuming_events
source: sitemap
fetched_at: 2026-04-26T04:13:37.612877225-03:00
rendered_js: false
word_count: 203
summary: This document outlines how to subscribe to real-time workflow events using the Workflows API, covering stream filtering, handling parent-child relationships, and implementing connection resiliency.
tags:
    - workflows-api
    - event-streaming
    - server-sent-events
    - real-time-data
    - api-integration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Subscribe to real-time events from workflows and activities using the Workflows API client.

## Filtering Events

Only receive events from a specific stream:

```python
```

Use SDK event types to detect when a workflow finishes:

```python
```

If your connection drops, resume from where you left off:

```python
```

## Query Parameters

| Parameter | Description |
|-----------|-------------|
| `stream` | Filter by stream name |
| `start_seq` | Resume from sequence number |

## Parent-Child Workflow Events

When a workflow spawns sub-workflows, events maintain parent-child relationships.

To receive events from a parent workflow and all its children in a single stream, subscribe using `root_workflow_exec_id`. Each event includes `workflow_context` so you can tell which workflow in the tree emitted it — if `parent_workflow_exec_id` is set, the event came from a child workflow.

Use the `root_workflow_exec_id` parameter to get all events in a workflow tree:

```python
```

## Event Types

The SDK uses typed event responses discriminated by `event_type`. Each event is a Pydantic model (e.g. `WorkflowExecutionCompletedResponse`, `CustomTaskInProgressResponse`) with fields like `event_id`, `event_timestamp`, `workflow_exec_id`, `workflow_name`, and type-specific `attributes`.

## Connection Resiliency

Streaming connections can drop at any time. Use `start_seq` to resume from the last received event, and implement exponential backoff to avoid hammering the server. The `is_terminal_status()` check is your own helper — check the event type against terminal statuses like `WORKFLOW_EXECUTION_COMPLETED`, `WORKFLOW_EXECUTION_FAILED`, or `WORKFLOW_EXECUTION_CANCELED`.

Filter at the subscription level, not in your code. If you only care about activity events:

```python
```