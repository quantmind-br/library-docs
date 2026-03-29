---
title: Onboard - OpenClaw
url: https://docs.openclaw.ai/cli/onboard
source: sitemap
fetched_at: 2026-01-30T20:34:56.754191634-03:00
rendered_js: false
word_count: 46
summary: Provides instructions for using the openclaw onboard command to set up local or remote Gateway connections through an interactive wizard interface.
tags:
    - cli-command
    - onboarding
    - gateway-setup
    - wizard
    - configuration
category: reference
---

- [openclaw onboard](#openclaw-onboard)
- [Examples](#examples)

## `openclaw onboard`

Interactive onboarding wizard (local or remote Gateway setup). Related:

- Wizard guide: [Onboarding](https://docs.openclaw.ai/start/onboarding)

## Examples

```
openclaw onboard
openclaw onboard --flow quickstart
openclaw onboard --flow manual
openclaw onboard --mode remote --remote-url ws://gateway-host:18789
```

Flow notes:

- `quickstart`: minimal prompts, auto-generates a gateway token.
- `manual`: full prompts for port/bind/auth (alias of `advanced`).
- Fastest first chat: `openclaw dashboard` (Control UI, no channel setup).

[Setup](https://docs.openclaw.ai/cli/setup)[Configure](https://docs.openclaw.ai/cli/configure)