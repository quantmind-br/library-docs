---
title: Workers | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/workers
source: sitemap
fetched_at: 2026-04-26T04:14:05.474803206-03:00
rendered_js: false
word_count: 307
summary: This document explains the function, operational behavior, and fault-tolerance of workers within the Workflows platform, including how they register and execute tasks.
tags:
    - worker-architecture
    - task-execution
    - workflow-management
    - fault-tolerance
    - distributed-computing
    - process-polling
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

A **worker** is the process that actually runs your code. Workers connect to the Workflows platform, register the workflows and activities they know about, and poll for tasks. When the platform schedules a workflow step or activity, an available worker picks it up and executes it.

## Key Properties

**Stateless and interchangeable:** Any worker that has registered a given workflow or activity can execute it — there is no affinity between a specific execution and a specific worker. Run as many workers as you need; the platform distributes tasks automatically.

**Auto-registration:** When you start a worker, your workflows and activities are **automatically registered** with the platform. No separate registration step or deployment manifest.

**Fault-tolerant:** If a worker crashes mid-execution, the platform detects the absence of heartbeats and reassigns the in-progress task to another worker. The workflow resumes without data loss because the event history contains everything needed to reconstruct state.

## Running a Worker

```python
client = workflows.Client()

run_worker(
    client,
    [MyWorkflow],
    task_queue="my-queue"
)
```

The `MISTRAL_API_KEY` environment variable determines which workspace the worker connects to. All workers sharing the same key share the same task queue.

## Task Lifecycle

1. A workflow execution is triggered (via API, schedule, or console)
2. A task is added to the queue
3. An available worker picks up the task and starts executing the workflow
4. When the workflow calls an activity, an activity task is added to the queue
5. Any available worker picks up the activity task and executes it
6. The result is recorded in the execution history
7. The workflow resumes with the activity result and continues

## Verify Connection

To verify a worker is connected and inspect its configuration:

```python
whoami = client.whoami()
print(whoami)
```

#worker-architecture #task-execution #fault-tolerance