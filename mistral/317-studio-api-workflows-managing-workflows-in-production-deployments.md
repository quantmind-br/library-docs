---
title: Deployments | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/managing-workflows-in-production/deployments
source: sitemap
fetched_at: 2026-04-26T04:14:26.036441416-03:00
rendered_js: false
word_count: 344
summary: This document explains the concept of deployments as a mechanism for organizing workers, managing workflow execution routing, and handling concurrency in shared workspaces.
tags:
    - deployment-management
    - workflow-execution
    - worker-isolation
    - horizontal-scaling
    - load-balancing
    - task-routing
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

A deployment is a named group of workers that owns a set of workflow definitions and receives all executions for those definitions. It enables worker isolation in shared workspaces and automatic execution routing.

## Required Configuration

`DEPLOYMENT_NAME` is **required** at worker startup. The worker fails immediately at boot if it is not set.

Valid characters: alphanumeric, hyphens, underscores (max 128 characters).

`WORKER_NAME` identifies the individual worker process and is visible in the console and API. It defaults to `socket.gethostname()`.

## Shared Workspaces

In a shared workspace, multiple developers can run workers simultaneously without interfering. Each deployment only receives executions for the workflow definitions it registered.

Alice's runs land on Alice's workers. Bob's runs land on Bob's workers.

## Execution Routing

When only one active deployment owns a workflow, executions route automatically — no extra configuration needed:

```python
```

When two active deployments register the same workflow name, the platform cannot route automatically and returns `409 Conflict`:

```python
```

Resolve by passing `deployment_name` explicitly:

```python
```

When a worker registers a workflow name already owned by a different active deployment, the platform warns immediately. Registration is not blocked — the warning is returned in the registration response and appears in worker logs:

```python
```

The conflict resolves automatically when one of the deployments becomes inactive (its workers stop).

Multiple workers in the **same** deployment registering the same definitions is horizontal scaling — no warning is produced.

## Active/Inactive State

A deployment is **active** while at least one of its workers has heartbeated within the liveness window. Workers heartbeat every ~10 seconds automatically. When all workers stop, the deployment becomes **inactive** after the liveness window lapses (50 seconds in production, configurable).

Inactive deployments do not receive executions and are not counted as conflicting when checking for ambiguity.

## Horizontal Scaling

Run multiple workers under the same `DEPLOYMENT_NAME` to increase throughput. Executions are distributed across all active workers in the deployment.

For production, deploy workers as a Kubernetes `Deployment` or `StatefulSet` with replicas pointing at the same `DEPLOYMENT_NAME`. The platform load-balances tasks automatically.

## Managing Deployments

List all active deployments in your workspace:

```python
```

Pass `workflow_name` to filter by workflow, or `active_only=false` to include inactive deployments.

Inspect a specific deployment and its individual workers:

```python
```