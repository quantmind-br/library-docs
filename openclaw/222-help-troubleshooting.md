---
title: Troubleshooting - OpenClaw
url: https://docs.openclaw.ai/help/troubleshooting
source: sitemap
fetched_at: 2026-01-30T20:29:03.331598588-03:00
rendered_js: false
word_count: 224
summary: Provides troubleshooting instructions and commands for resolving common issues with the openclaw CLI tool and gateway connectivity.
tags:
    - troubleshooting
    - cli-tool
    - gateway
    - installation
    - logs
    - configuration
    - error-handling
category: guide
---

## First 60 seconds

Run these in order:

```
openclaw status
openclaw status --all
openclaw gateway probe
openclaw logs --follow
openclaw doctor
```

If the gateway is reachable, deep probes:

## Common “it broke” cases

### `openclaw: command not found`

Almost always a Node/npm PATH issue. Start here:

- [Install (Node/npm PATH sanity)](https://docs.openclaw.ai/install#nodejs--npm-path-sanity)

### Installer fails (or you need full logs)

Re-run the installer in verbose mode to see the full trace and npm output:

```
curl -fsSL https://openclaw.bot/install.sh | bash -s -- --verbose
```

For beta installs:

```
curl -fsSL https://openclaw.bot/install.sh | bash -s -- --beta --verbose
```

You can also set `OPENCLAW_VERBOSE=1` instead of the flag.

- [Gateway troubleshooting](https://docs.openclaw.ai/gateway/troubleshooting)
- [Gateway authentication](https://docs.openclaw.ai/gateway/authentication)

### Control UI fails on HTTP (device identity required)

- [Gateway troubleshooting](https://docs.openclaw.ai/gateway/troubleshooting)
- [Control UI](https://docs.openclaw.ai/web/control-ui#insecure-http)

### `docs.openclaw.ai` shows an SSL error (Comcast/Xfinity)

Some Comcast/Xfinity connections block `docs.openclaw.ai` via Xfinity Advanced Security. Disable Advanced Security or add `docs.openclaw.ai` to the allowlist, then retry.

- Xfinity Advanced Security help: [https://www.xfinity.com/support/articles/using-xfinity-xfi-advanced-security](https://www.xfinity.com/support/articles/using-xfinity-xfi-advanced-security)
- Quick sanity checks: try a mobile hotspot or VPN to confirm it’s ISP-level filtering

### Service says running, but RPC probe fails

- [Gateway troubleshooting](https://docs.openclaw.ai/gateway/troubleshooting)
- [Background process / service](https://docs.openclaw.ai/gateway/background-process)

### Model/auth failures (rate limit, billing, “all models failed”)

- [Models](https://docs.openclaw.ai/cli/models)
- [OAuth / auth concepts](https://docs.openclaw.ai/concepts/oauth)

### `/model` says `model not allowed`

This usually means `agents.defaults.models` is configured as an allowlist. When it’s non-empty, only those provider/model keys can be selected.

- Check the allowlist: `openclaw config get agents.defaults.models`
- Add the model you want (or clear the allowlist) and retry `/model`
- Use `/models` to browse the allowed providers/models

### When filing an issue

Paste a safe report:

If you can, include the relevant log tail from `openclaw logs --follow`.