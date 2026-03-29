---
title: Status - OpenClaw
url: https://docs.openclaw.ai/cli/status
source: sitemap
fetched_at: 2026-01-30T20:34:20.012565271-03:00
rendered_js: false
word_count: 75
summary: Provides information about the openclaw status command and its various options for diagnosing channels and sessions.
tags:
    - diagnostics
    - status-command
    - channels
    - sessions
    - troubleshooting
category: reference
---

Diagnostics for channels + sessions.

```
openclaw status
openclaw status --all
openclaw status --deep
openclaw status --usage
```

Notes:

- `--deep` runs live probes (WhatsApp Web + Telegram + Discord + Google Chat + Slack + Signal).
- Output includes per-agent session stores when multiple agents are configured.
- Overview includes Gateway + node host service install/runtime status when available.
- Overview includes update channel + git SHA (for source checkouts).
- Update info surfaces in the Overview; if an update is available, status prints a hint to run `openclaw update` (see [Updating](https://docs.openclaw.ai/install/updating)).