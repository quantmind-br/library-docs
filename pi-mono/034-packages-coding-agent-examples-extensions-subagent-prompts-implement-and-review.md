---
title: Implement and review
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/subagent/prompts/implement-and-review.md
source: git
fetched_at: 2026-05-03T09:31:49.396825823-03:00
rendered_js: false
word_count: 68
summary: Multi-step workflow using subagent chain — worker implements, reviewer reviews, worker applies feedback.
tags:
    - agent-workflow
    - subagent-tool
    - automated-code-review
    - chaining-logic
    - task-execution
category: guide
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
---
description: Worker implements, reviewer reviews, worker applies feedback
---

Use the subagent tool with the `chain` parameter:

1. Use the **"worker"** agent to implement: `$@`
2. Use the **"reviewer"** agent to review the implementation from step 1 (use `{previous}` placeholder)
3. Use the **"worker"** agent to apply feedback from step 2 (use `{previous}` placeholder)

Execute as a chain, passing output between steps via `{previous}`.

#agent-workflow #subagent-tool #chaining-logic
