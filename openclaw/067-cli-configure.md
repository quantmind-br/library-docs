---
title: Configure - OpenClaw
url: https://docs.openclaw.ai/cli/configure
source: sitemap
fetched_at: 2026-01-30T20:36:15.052604266-03:00
rendered_js: false
word_count: 103
summary: Provides instructions for configuring OpenClaw gateway settings through an interactive prompt, covering credentials, devices, agent defaults, and model selections.
tags:
    - configuration
    - gateway
    - credentials
    - models
    - interactive
    - setup
category: guide
---

Interactive prompt to set up credentials, devices, and agent defaults. Note: The **Model** section now includes a multi-select for the `agents.defaults.models` allowlist (what shows up in `/model` and the model picker). Tip: `openclaw config` without a subcommand opens the same wizard. Use `openclaw config get|set|unset` for non-interactive edits. Related:

- Gateway configuration reference: [Configuration](https://docs.openclaw.ai/gateway/configuration)
- Config CLI: [Config](https://docs.openclaw.ai/cli/config)

Notes:

- Choosing where the Gateway runs always updates `gateway.mode`. You can select “Continue” without other sections if that is all you need.
- Channel-oriented services (Slack/Discord/Matrix/Microsoft Teams) prompt for channel/room allowlists during setup. You can enter names or IDs; the wizard resolves names to IDs when possible.

## Examples

```
openclaw configure
openclaw configure --section models --section channels
```