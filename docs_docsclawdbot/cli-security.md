---
title: "null"
url: https://docs.clawd.bot/cli/security.md
source: llms
fetched_at: 2026-01-26T09:50:58.209943249-03:00
rendered_js: false
word_count: 68
summary: This document describes the clawdbot security command, which allows users to audit their configuration for security risks and apply automated fixes.
tags:
    - security-audit
    - cli-commands
    - vulnerability-detection
    - sandboxing
    - session-management
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot security`

Security tools (audit + optional fixes).

Related:

* Security guide: [Security](/gateway/security)

## Audit

```bash  theme={null}
clawdbot security audit
clawdbot security audit --deep
clawdbot security audit --fix
```

The audit warns when multiple DM senders share the main session and recommends `session.dmScope="per-channel-peer"` for shared inboxes.
It also warns when small models (`<=300B`) are used without sandboxing and with web/browser tools enabled.