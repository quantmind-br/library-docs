---
title: Sub-workflows | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/sub_workflows
source: sitemap
fetched_at: 2026-04-26T04:13:49.430964072-03:00
rendered_js: false
word_count: 60
summary: This document explains how to orchestrate hierarchical workflows by triggering sub-workflows and managing their execution lifecycle and completion policies.
tags:
    - workflow-orchestration
    - sub-workflow
    - child-workflow
    - execution-control
    - parent-close-policy
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

A workflow can execute other workflows as sub-workflows, enabling hierarchical orchestration patterns.

## Execute and Wait

Execute a sub-workflow and wait for its result:

```python
```

## Fire and Forget

Start a sub-workflow without waiting for its result by passing `wait=False`:

```python
```

By default, `wait=False` sets the parent close policy to `ABANDON`, so the child continues running even if the parent completes.

Override the default close policy with the `parent_close_policy` parameter:

```python
```