---
title: Implement and review
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/subagent/prompts/implement-and-review.md
source: git
fetched_at: 2026-03-03T03:42:51.872094-03:00
rendered_js: false
word_count: 75
summary: describes a multi-step workflow for implementing, reviewing, and applying feedback using subagents in an automated system
tags:
    - workflow-design
    - agent-chaining
    - feedback-loops
    - multi-agent-system
category: concept
---

---
description: Worker implements, reviewer reviews, worker applies feedback
---
Use the subagent tool with the chain parameter to execute this workflow:

1. First, use the "worker" agent to implement: $@
2. Then, use the "reviewer" agent to review the implementation from the previous step (use {previous} placeholder)
3. Finally, use the "worker" agent to apply the feedback from the review (use {previous} placeholder)

Execute this as a chain, passing output between steps via {previous}.
