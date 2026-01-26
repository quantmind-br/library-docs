---
title: "null"
url: https://docs.clawd.bot/cli/agent.md
source: llms
fetched_at: 2026-01-26T10:12:00.214939266-03:00
rendered_js: false
word_count: 51
summary: This document explains how to use the clawdbot agent command to execute agent interactions via the Gateway or locally, including message delivery and session management.
tags:
    - cli
    - agent-turn
    - command-line
    - messaging
    - automation
    - gateway
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot agent`

Run an agent turn via the Gateway (use `--local` for embedded).
Use `--agent <id>` to target a configured agent directly.

Related:

* Agent send tool: [Agent send](/tools/agent-send)

## Examples

```bash  theme={null}
clawdbot agent --to +15555550123 --message "status update" --deliver
clawdbot agent --agent ops --message "Summarize logs"
clawdbot agent --session-id 1234 --message "Summarize inbox" --thinking medium
clawdbot agent --agent ops --message "Generate report" --deliver --reply-channel slack --reply-to "#reports"
```