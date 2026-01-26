---
title: "null"
url: https://docs.clawd.bot/cli/health.md
source: llms
fetched_at: 2026-01-26T10:12:14.281765577-03:00
rendered_js: false
word_count: 54
summary: This document explains how to use the clawdbot health command to monitor the status of the running Gateway, including options for detailed diagnostics and JSON output.
tags:
    - cli
    - clawdbot
    - health-check
    - monitoring
    - diagnostics
    - gateway-status
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot health`

Fetch health from the running Gateway.

```bash  theme={null}
clawdbot health
clawdbot health --json
clawdbot health --verbose
```

Notes:

* `--verbose` runs live probes and prints per-account timings when multiple accounts are configured.
* Output includes per-agent session stores when multiple agents are configured.