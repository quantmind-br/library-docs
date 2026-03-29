---
title: Doctor - OpenClaw
url: https://docs.openclaw.ai/cli/doctor
source: sitemap
fetched_at: 2026-01-30T20:35:33.0380166-03:00
rendered_js: false
word_count: 87
summary: Provides guidance on diagnosing and resolving common issues with the OpenClaw gateway and channels through command-line health checks and repair options.
tags:
    - health-checks
    - troubleshooting
    - gateway
    - channels
    - cli-tools
    - macos
    - configuration
category: guide
---

Health checks + quick fixes for the gateway and channels. Related:

- Troubleshooting: [Troubleshooting](https://docs.openclaw.ai/gateway/troubleshooting)
- Security audit: [Security](https://docs.openclaw.ai/gateway/security)

## Examples

```
openclaw doctor
openclaw doctor --repair
openclaw doctor --deep
```

Notes:

- Interactive prompts (like keychain/OAuth fixes) only run when stdin is a TTY and `--non-interactive` is **not** set. Headless runs (cron, Telegram, no terminal) will skip prompts.
- `--fix` (alias for `--repair`) writes a backup to `~/.openclaw/openclaw.json.bak` and drops unknown config keys, listing each removal.

## macOS: `launchctl` env overrides

If you previously ran `launchctl setenv OPENCLAW_GATEWAY_TOKEN ...` (or `...PASSWORD`), that value overrides your config file and can cause persistent “unauthorized” errors.

```
launchctl getenv OPENCLAW_GATEWAY_TOKEN
launchctl getenv OPENCLAW_GATEWAY_PASSWORD

launchctl unsetenv OPENCLAW_GATEWAY_TOKEN
launchctl unsetenv OPENCLAW_GATEWAY_PASSWORD
```