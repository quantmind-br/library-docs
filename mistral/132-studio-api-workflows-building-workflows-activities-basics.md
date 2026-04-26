---
title: Basics | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/activities/basics
source: sitemap
fetched_at: 2026-04-26T04:13:31.989795904-03:00
rendered_js: false
word_count: 462
summary: This document outlines the core concepts of configuring activities in a workflow system, covering naming conventions, timeouts, retry policies, heartbeats, and best practices for granularity.
tags:
    - activity-management
    - workflow-design
    - retry-policy
    - timeout-configuration
    - error-handling
    - system-observability
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Activity Basics

Basic activity structure:

```python
@activity.defn
async def my_activity(arg1: str) -> str:
    return f"Processed: {arg1}"
```

### Naming

By default, activity registered using Python function name. Use `name` parameter for custom identifier (used for registration, execution routing, traces, console).

See [observability and naming](https://docs.mistral.ai/studio-api/workflows/observability).

## Timeouts

`start_to_close_timeout`: Maximum time from activity start to result return. If exceeded, activity terminated and treated as failure (may trigger retry). Without timeout, hung activity blocks indefinitely.

## Retry Policy

On failure, activity retries automatically up to `retry_policy_max_attempts` times. `retry_policy_backoff_coefficient` controls exponential backoff — coefficient of `2.0` means delay doubles each attempt (1s, 2s, 4s, 8s). After all retries exhausted, failure propagates to workflow.

## Sticky Worker Sessions

Execute activities on same worker for performance optimization.

See [Sticky Worker Sessions](https://docs.mistral.ai/studio-api/workflows/building-workflows/activities/sticky_worker_sessions).

## Heartbeat

Detect stuck activities by requiring periodic `activity.heartbeat()` calls:

```python
@activity.defn(
    name="my_activity",
    start_to_close_timeout=600,
    heartbeat_timeout=30,
)
async def my_activity(arg1: str) -> str:
    activity.heartbeat()
    # work
```

If no heartbeat within timeout, activity considered failed and retry triggered. Enables fast detection without waiting for full `start_to_close_timeout`.

> [!warning]
> Heartbeat not supported for local activities.

## Granularity Best Practices

Design activities to be as granular as possible — break complex tasks into smaller, manageable units that encapsulate all failure-susceptible logic.

**Benefits:**
- **Failure isolation**: Only affected activity retries
- **Easier debugging**: Identify exact failure point
- **Better retry mechanisms**: Failed part retries independently, saving time and resources

**Example:**
1. Fetch data from API
2. Process the data
3. Store data in database

## Nested Activities

When activities are nested, only parent activity considered for retries/state management. State saved before nested activity, entire parent retried on failure.

> [!example]
> If `nested_activity` fails, entire `parent_activity` retried. #activity-management #workflow-design #retry-policy