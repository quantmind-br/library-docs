---
title: Agent - OpenClaw
url: https://docs.openclaw.ai/cli/agent
source: sitemap
fetched_at: 2026-01-30T20:35:54.31555021-03:00
rendered_js: false
word_count: 31
summary: This document explains how to use the openclaw agent command to run agent turns through the Gateway, including options for local execution, agent targeting, and various message delivery settings.
tags:
    - command-line
    - agent-execution
    - gateway-integration
    - message-delivery
    - cli-tool
category: reference
---

## [​](#openclaw-agent) `openclaw agent`

Run an agent turn via the Gateway (use `--local` for embedded). Use `--agent <id>` to target a configured agent directly. Related:

- Agent send tool: [Agent send](https://docs.openclaw.ai/tools/agent-send)

## [​](#examples) Examples

```
openclaw agent --to +15555550123 --message "status update" --deliver
openclaw agent --agent ops --message "Summarize logs"
openclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium
openclaw agent --agent ops --message "Generate report" --deliver --reply-channel slack --reply-to "#reports"
```