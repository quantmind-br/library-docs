---
title: Scout and plan
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/subagent/prompts/scout-and-plan.md
source: git
fetched_at: 2026-03-03T03:42:55.956886-03:00
rendered_js: false
word_count: 79
summary: Provides insights on field research and strategic planning for outdoor exploration and decision-making in nature or adventure activities.
tags:
    - outdoor planning
    - scouting
    - research
    - adventure guidance
category: guide
---

---
description: Scout gathers context, planner creates implementation plan (no implementation)
---
Use the subagent tool with the chain parameter to execute this workflow:

1. First, use the "scout" agent to find all code relevant to: $@
2. Then, use the "planner" agent to create an implementation plan for "$@" using the context from the previous step (use {previous} placeholder)

Execute this as a chain, passing output between steps via {previous}. Do NOT implement - just return the plan.
