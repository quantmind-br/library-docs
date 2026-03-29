---
title: Opencode - OpenClaw
url: https://docs.openclaw.ai/providers/opencode
source: sitemap
fetched_at: 2026-01-30T20:25:00.58988279-03:00
rendered_js: false
word_count: 73
summary: This document explains how to set up and use OpenCode Zen, a curated list of models for coding agents that requires an API key and the 'opencode' provider. It provides CLI setup instructions and configuration examples.
tags:
    - opencode
    - zen
    - api-key
    - cli-setup
    - configuration
    - coding-agents
category: guide
---

## OpenCode Zen

OpenCode Zen is a **curated list of models** recommended by the OpenCode team for coding agents. It is an optional, hosted model access path that uses an API key and the `opencode` provider. Zen is currently in beta.

## CLI setup

```
openclaw onboard --auth-choice opencode-zen
# or non-interactive
openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
```

## Config snippet

```
{
  env: { OPENCODE_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "opencode/claude-opus-4-5" } } }
}
```

## Notes

- `OPENCODE_ZEN_API_KEY` is also supported.
- You sign in to Zen, add billing details, and copy your API key.
- OpenCode Zen bills per request; check the OpenCode dashboard for details.