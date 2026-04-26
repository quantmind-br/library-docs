---
title: Deployments | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/deployments
source: sitemap
fetched_at: 2026-04-26T04:13:59.610598017-03:00
rendered_js: false
word_count: 188
summary: This document explains the concept of deployments, which are groups of workers that share workflow definitions and handle task executions through isolation, routing, and scaling.
tags:
    - deployment
    - worker-isolation
    - workflow-management
    - horizontal-scaling
    - task-routing
    - infrastructure
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

A **deployment** is a named group of workers that owns a set of workflow definitions and receives all executions for those definitions.

Workers join a deployment by setting the `DEPLOYMENT_NAME` environment variable at startup:

```bash
DEPLOYMENT_NAME=my-deployment mistral-workflows run
```

All workers running under the same `DEPLOYMENT_NAME` form a single deployment. They share identical workflow definitions and collectively receive all executions routed to that deployment.

## Capabilities

| Capability | Description |
|------------|-------------|
| **Worker isolation** | Each deployment exclusively receives executions for its registered workflows; multiple teams can run workers simultaneously without interfering |
| **Automatic routing** | When a single active deployment owns a workflow, executions route automatically — no manual configuration |
| **Horizontal scaling** | Run multiple workers under the same `DEPLOYMENT_NAME` to increase throughput; the platform distributes tasks across all of them |
| **Lifecycle tracking** | A deployment is active as long as at least one worker has heartbeated within the liveness window; inactive deployments are excluded from routing |

For a complete guide covering execution routing, conflict detection, and the Deployments API, see [Managing Deployments](https://docs.mistral.ai/studio-api/workflows/managing-workflows-in-production/deployments).

#deployment #worker-isolation #horizontal-scaling