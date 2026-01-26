---
title: "null"
url: https://docs.clawd.bot/cli/status.md
source: llms
fetched_at: 2026-01-26T09:51:03.243571319-03:00
rendered_js: false
word_count: 99
summary: This document describes the clawdbot status command and its various flags used for performing diagnostics on communication channels, session stores, and system health.
tags:
    - diagnostics
    - cli-status
    - system-health
    - session-monitoring
    - channel-verification
    - troubleshooting
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot status`

Diagnostics for channels + sessions.

```bash  theme={null}
clawdbot status
clawdbot status --all
clawdbot status --deep
clawdbot status --usage
```

Notes:

* `--deep` runs live probes (WhatsApp Web + Telegram + Discord + Google Chat + Slack + Signal).
* Output includes per-agent session stores when multiple agents are configured.
* Overview includes Gateway + node host service install/runtime status when available.
* Overview includes update channel + git SHA (for source checkouts).
* Update info surfaces in the Overview; if an update is available, status prints a hint to run `clawdbot update` (see [Updating](/install/updating)).