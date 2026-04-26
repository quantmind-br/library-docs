---
title: Resetting Workflows | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/managing-workflows-in-production/reset_workflow
source: sitemap
fetched_at: 2026-04-26T04:14:33.791562043-03:00
rendered_js: false
word_count: 226
summary: This document explains how to reset a workflow execution to restart it from a previous point in its event history, typically to resolve stuck processes or code-related errors.
tags:
    - workflow-management
    - event-history
    - error-recovery
    - debugging
    - workflow-reset
    - distributed-systems
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Reset a workflow execution to restart it from a specific point in its event history.

Resetting is useful when a workflow gets stuck — for example, because of a non-determinism error after a code change — or when it cannot complete due to a bug that has since been fixed.

> [!warning] Resetting should only be used **after fixing the underlying problem**. All progress made after the reset point will be lost.

## Behavior

When you reset a workflow:
1. The current run is terminated
2. A new run is created under the same execution ID
3. All events up to the reset point are copied to the new run
4. The workflow replays from the reset point using the **latest version of your code**

This means any bug fix you deployed will take effect when the workflow resumes.

## Finding Valid Reset Points

Use the trace events API to find valid reset points:

```python
```

If you provide an invalid event ID, the API returns a `WF_1001` error with a `valid_reset_events` field listing valid alternatives.

## Best Practices

1. **Fix the root cause first** — resetting without fixing the bug will reproduce the same failure
2. **Always provide a reason** — it is recorded in the event history for auditing
3. **Use `exclude_signals` carefully** — skipping signals means any external input received after the reset point won't be replayed
4. **Test your fix** — deploy and test the fix on a development workspace before resetting production workflows