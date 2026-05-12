---
title: Scout and plan
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/subagent/prompts/scout-and-plan.md
source: git
fetched_at: 2026-05-03T09:31:51.474943713-03:00
rendered_js: false
word_count: 73
summary: Two-step subagent workflow using scout and planner to generate an implementation plan without executing code.
tags:
    - subagent-workflow
    - task-planning
    - code-context
    - automation-pipeline
    - agentic-execution
category: guide
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
---
description: Scout gathers context, planner creates implementation plan (no implementation)
---

Use the subagent tool with the `chain` parameter:

1. Use the **"scout"** agent to find all code relevant to: `$@`
2. Use the **"planner"** agent to create an implementation plan for `"$@"` using context from step 1 (use `{previous}` placeholder)

Execute as a chain, passing output between steps via `{previous}`. Do NOT implement — return the plan only.

#subagent-workflow #task-planning #automation-pipeline
