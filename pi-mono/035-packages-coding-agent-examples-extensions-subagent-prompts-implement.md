---
title: Implement
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/subagent/prompts/implement.md
source: git
fetched_at: 2026-05-03T09:31:51.171398026-03:00
rendered_js: false
word_count: 83
summary: Full implementation workflow — scout gathers context, planner creates plan, worker implements.
tags:
    - agentic-workflow
    - subagent-tool
    - code-implementation
    - automation-pipeline
    - agent-orchestration
category: guide
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
---
description: Full implementation workflow — scout gathers context, planner creates plan, worker implements
---

Use the subagent tool with the `chain` parameter:

1. Use the **"scout"** agent to find all code relevant to: `$@`
2. Use the **"planner"** agent to create an implementation plan for `"$@"` using context from step 1 (use `{previous}` placeholder)
3. Use the **"worker"** agent to implement the plan from step 2 (use `{previous}` placeholder)

Execute as a chain, passing output between steps via `{previous}`.

#agentic-workflow #subagent-tool #automation-pipeline
