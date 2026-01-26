---
title: "null"
url: https://docs.clawd.bot/cli/health.md
source: llms
fetched_at: 2026-01-26T09:50:45.497496643-03:00
rendered_js: false
word_count: 54
summary: This document describes the clawdbot health command used to retrieve status information, live probes, and performance metrics from a running Gateway instance.
tags:
    - clawdbot-cli
    - health-check
    - monitoring
    - gateway-status
    - command-line
    - system-diagnostics
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