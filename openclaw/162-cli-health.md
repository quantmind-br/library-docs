---
title: Health - OpenClaw
url: https://docs.openclaw.ai/cli/health
source: sitemap
fetched_at: 2026-01-30T20:35:46.009755786-03:00
rendered_js: false
word_count: 37
summary: Provides information about the openclaw health command for checking the status of a running Gateway, including available flags and output formats.
tags:
    - cli-command
    - gateway-status
    - health-check
    - openclaw
category: reference
---

- [openclaw health](#openclaw-health)

## [​](#openclaw-health) `openclaw health`

Fetch health from the running Gateway.

```
openclaw health
openclaw health --json
openclaw health --verbose
```

Notes:

- `--verbose` runs live probes and prints per-account timings when multiple accounts are configured.
- Output includes per-agent session stores when multiple agents are configured.

[Status](https://docs.openclaw.ai/cli/status)[Sessions](https://docs.openclaw.ai/cli/sessions)

Ctrl+I