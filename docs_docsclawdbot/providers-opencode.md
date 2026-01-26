---
title: "null"
url: https://docs.clawd.bot/providers/opencode.md
source: llms
fetched_at: 2026-01-26T09:53:29.089875173-03:00
rendered_js: false
word_count: 95
summary: This document explains how to set up and configure OpenCode Zen, a curated model access path for coding agents that uses the opencode provider.
tags:
    - opencode-zen
    - cli-setup
    - model-configuration
    - api-integration
    - coding-agents
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# OpenCode Zen

OpenCode Zen is a **curated list of models** recommended by the OpenCode team for coding agents.
It is an optional, hosted model access path that uses an API key and the `opencode` provider.
Zen is currently in beta.

## CLI setup

```bash  theme={null}
clawdbot onboard --auth-choice opencode-zen
# or non-interactive
clawdbot onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
```

## Config snippet

```json5  theme={null}
{
  env: { OPENCODE_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "opencode/claude-opus-4-5" } } }
}
```

## Notes

* `OPENCODE_ZEN_API_KEY` is also supported.
* You sign in to Zen, add billing details, and copy your API key.
* OpenCode Zen bills per request; check the OpenCode dashboard for details.