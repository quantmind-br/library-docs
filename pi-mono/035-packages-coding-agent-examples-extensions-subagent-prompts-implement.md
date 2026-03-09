---
title: Implement
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/subagent/prompts/implement.md
source: git
fetched_at: 2026-03-03T03:42:53.483203-03:00
rendered_js: false
word_count: 91
summary: Explains implementation basics for development or deployment tasks, including process steps and best practices.
tags:
    - development
    - implementation
    - guides
category: guide
---

---
description: Full implementation workflow - scout gathers context, planner creates plan, worker implements
---
Use the subagent tool with the chain parameter to execute this workflow:

1. First, use the "scout" agent to find all code relevant to: $@
2. Then, use the "planner" agent to create an implementation plan for "$@" using the context from the previous step (use {previous} placeholder)
3. Finally, use the "worker" agent to implement the plan from the previous step (use {previous} placeholder)

Execute this as a chain, passing output between steps via {previous}.
