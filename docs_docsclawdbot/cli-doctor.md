---
title: "null"
url: https://docs.clawd.bot/cli/doctor.md
source: llms
fetched_at: 2026-01-26T09:50:42.625022012-03:00
rendered_js: false
word_count: 111
summary: This document explains how to use the clawdbot doctor command to perform system health checks and automatically repair configuration issues.
tags:
    - cli-commands
    - health-check
    - troubleshooting
    - configuration-repair
    - clawdbot-gateway
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot doctor`

Health checks + quick fixes for the gateway and channels.

Related:

* Troubleshooting: [Troubleshooting](/gateway/troubleshooting)
* Security audit: [Security](/gateway/security)

## Examples

```bash  theme={null}
clawdbot doctor
clawdbot doctor --repair
clawdbot doctor --deep
```

Notes:

* Interactive prompts (like keychain/OAuth fixes) only run when stdin is a TTY and `--non-interactive` is **not** set. Headless runs (cron, Telegram, no terminal) will skip prompts.
* `--fix` (alias for `--repair`) writes a backup to `~/.clawdbot/clawdbot.json.bak` and drops unknown config keys, listing each removal.

## macOS: `launchctl` env overrides

If you previously ran `launchctl setenv CLAWDBOT_GATEWAY_TOKEN ...` (or `...PASSWORD`), that value overrides your config file and can cause persistent “unauthorized” errors.

```bash  theme={null}
launchctl getenv CLAWDBOT_GATEWAY_TOKEN
launchctl getenv CLAWDBOT_GATEWAY_PASSWORD

launchctl unsetenv CLAWDBOT_GATEWAY_TOKEN
launchctl unsetenv CLAWDBOT_GATEWAY_PASSWORD
```