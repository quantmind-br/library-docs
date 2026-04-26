---
title: Workflow Scheduling | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/scheduling
source: sitemap
fetched_at: 2026-04-26T04:13:45.108893943-03:00
rendered_js: false
word_count: 184
summary: This document describes the mechanism for automating workflow execution using cron-based scheduling, including configuration policies for handling missed or overlapping runs.
tags:
    - workflow-automation
    - cron-scheduling
    - worker-configuration
    - execution-policies
    - task-scheduling
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Automatically run workflows at specified times without manual triggering.

Workers automatically register workflow schedules with Workflows during startup. The system handles:
1. Schedule registration with Workflows
2. Periodic refresh of schedule definitions (every 10 seconds)
3. Execution of workflows according to the schedule

## Adding Schedules

Add schedules to workflows using cron expressions:

```python
```

## Overlap Policies

Policies control what happens when schedules are missed or overlap:

- **`catchup_window_seconds`** — If the platform was down or missed scheduled runs, it will retroactively trigger all missed executions within this window. Runs older than the window are skipped.
- **`overlap`** — What to do when a new run is due but the previous one is still running:
  - `SKIP` — drops the new run
  - `BUFFER_ONE` — queues one pending run
  - `ALLOW_ALL` — starts all runs concurrently

## Configuration Notes

> [!important] Worker Configuration:
> - Ensure all workers have identical schedule configurations
> - Mismatched configurations can cause conflicts and unexpected behavior

> [!note] Schedule Definition:
> - Uses standard cron syntax
> - Includes input parameters for scheduled executions
> - Supports multiple cron expressions per workflow

## Additional Notes

- Schedules use UTC time zone by default
- Each schedule can specify different input parameters
- Workers automatically maintain schedule registrations
- Ensure consistent schedule definitions across all workers