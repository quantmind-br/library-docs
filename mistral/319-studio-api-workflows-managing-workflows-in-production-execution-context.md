---
title: Execution Context | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/managing-workflows-in-production/execution_context
source: sitemap
fetched_at: 2026-04-26T04:14:29.97574087-03:00
rendered_js: false
word_count: 45
summary: This document explains how to retrieve the unique execution identifier within a workflow to facilitate logging and system correlation.
tags:
    - workflow-runtime
    - execution-id
    - python-sdk
    - correlation-id
    - tracing
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Access runtime information about the current workflow execution from within workflow code.

## Getting the Execution ID

```python
import mistralai.workflows as workflows
execution_id = workflows.get_execution_id()
```

This returns the unique identifier for the current execution, useful for logging, correlating with external systems, or passing to activities that need to reference the parent execution.

## Example Usage

```python
import mistralai.workflows as workflows

@workflows.workflow.define(name="tracked_workflow")
class TrackedWorkflow:
    @workflows.workflow.entrypoint
    async def run(self, params: MyParams) -> MyResult:
        execution_id = workflows.get_execution_id()
        # Pass execution ID to activities for correlation
        result = await process_with_tracking(params, execution_id)
        return result
```