---
title: "null"
url: https://docs.clawd.bot/cli/logs.md
source: llms
fetched_at: 2026-01-26T10:12:17.059208447-03:00
rendered_js: false
word_count: 39
summary: This document explains how to use the 'clawdbot logs' CLI command to tail Gateway file logs over RPC, including support for remote mode and various output options.
tags:
    - cli-command
    - logging
    - rpc
    - remote-access
    - log-tailing
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot logs`

Tail Gateway file logs over RPC (works in remote mode).

Related:

* Logging overview: [Logging](/logging)

## Examples

```bash  theme={null}
clawdbot logs
clawdbot logs --follow
clawdbot logs --json
clawdbot logs --limit 500
```