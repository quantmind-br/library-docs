---
title: Gather context and clarify
url: https://github.com/nicobailon/pi-subagents/blob/main/prompts/gather-context-and-clarify.md
source: git
fetched_at: 2026-04-27T21:18:06.320659763-03:00
rendered_js: false
word_count: 107
summary: This document describes a workflow methodology where context-gathering subagents are launched prior to planning or implementation to gather necessary information.
tags:
    - subagent-workflow
    - context-gathering
    - scout-researcher
    - meta-prompting
    - clarification-questions
    - interview-tool
category: guide
---

---
description: Use subagents to gather context, then ask clarifying questions
---

Based on our discussion and my intent, launch focused context-gathering subagents before planning or implementing.

Use `scout` to inspect the relevant local files, existing patterns, constraints, tests, and likely integration points. Use `researcher` when external docs, recent sources, ecosystem context, or primary evidence would improve the answer.

Give each subagent a specific meta prompt. Ask them to return concise findings plus the remaining clarification questions that matter for implementation confidence.

After they return, synthesize what we know and use the `interview` tool to ask me the unresolved questions needed to reach a shared understanding.

$@
