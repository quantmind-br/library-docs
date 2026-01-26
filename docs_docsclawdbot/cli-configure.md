---
title: "null"
url: https://docs.clawd.bot/cli/configure.md
source: llms
fetched_at: 2026-01-26T09:50:36.076166705-03:00
rendered_js: false
word_count: 127
summary: This document explains how to use the clawdbot configure CLI command to interactively set up credentials, devices, and agent default settings.
tags:
    - cli
    - configuration
    - setup-wizard
    - authentication
    - gateway-config
    - command-line-interface
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot configure`

Interactive prompt to set up credentials, devices, and agent defaults.

Note: The **Model** section now includes a multi-select for the
`agents.defaults.models` allowlist (what shows up in `/model` and the model picker).

Tip: `clawdbot config` without a subcommand opens the same wizard. Use
`clawdbot config get|set|unset` for non-interactive edits.

Related:

* Gateway configuration reference: [Configuration](/gateway/configuration)
* Config CLI: [Config](/cli/config)

Notes:

* Choosing where the Gateway runs always updates `gateway.mode`. You can select "Continue" without other sections if that is all you need.
* Channel-oriented services (Slack/Discord/Matrix/Microsoft Teams) prompt for channel/room allowlists during setup. You can enter names or IDs; the wizard resolves names to IDs when possible.

## Examples

```bash  theme={null}
clawdbot configure
clawdbot configure --section models --section channels
```