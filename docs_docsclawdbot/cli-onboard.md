---
title: "null"
url: https://docs.clawd.bot/cli/onboard.md
source: llms
fetched_at: 2026-01-26T09:50:53.210199797-03:00
rendered_js: false
word_count: 54
summary: This document describes the clawdbot onboard command, an interactive wizard used to configure local or remote Gateway setups. It explains various execution modes including quickstart and manual flows for different setup complexities.
tags:
    - clawdbot-cli
    - onboarding-wizard
    - gateway-setup
    - configuration-tool
    - cli-reference
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot onboard`

Interactive onboarding wizard (local or remote Gateway setup).

Related:

* Wizard guide: [Onboarding](/start/onboarding)

## Examples

```bash  theme={null}
clawdbot onboard
clawdbot onboard --flow quickstart
clawdbot onboard --flow manual
clawdbot onboard --mode remote --remote-url ws://gateway-host:18789
```

Flow notes:

* `quickstart`: minimal prompts, auto-generates a gateway token.
* `manual`: full prompts for port/bind/auth (alias of `advanced`).