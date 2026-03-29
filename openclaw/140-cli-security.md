---
title: Security - OpenClaw
url: https://docs.openclaw.ai/cli/security
source: sitemap
fetched_at: 2026-01-30T20:34:03.372140671-03:00
rendered_js: false
word_count: 53
summary: Provides information about security auditing tools and best practices for OpenCLAW applications, including recommendations for session scoping and model sandboxing.
tags:
    - security-audit
    - session-management
    - model-sandboxing
    - openclaw-cli
    - security-tools
category: guide
---

## [​](#openclaw-security) `openclaw security`

Security tools (audit + optional fixes). Related:

- Security guide: [Security](https://docs.openclaw.ai/gateway/security)

## [​](#audit) Audit

```
openclaw security audit
openclaw security audit --deep
openclaw security audit --fix
```

The audit warns when multiple DM senders share the main session and recommends `session.dmScope="per-channel-peer"` (or `per-account-channel-peer` for multi-account channels) for shared inboxes. It also warns when small models (`<=300B`) are used without sandboxing and with web/browser tools enabled.