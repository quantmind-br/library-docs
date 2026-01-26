---
title: "null"
url: https://docs.clawd.bot/providers/openai.md
source: llms
fetched_at: 2026-01-26T09:53:25.007765437-03:00
rendered_js: false
word_count: 166
summary: This document explains how to configure OpenAI authentication for Clawdbot using either an API key or a Codex subscription.
tags:
    - openai
    - authentication
    - clawdbot
    - configuration
    - api-key
    - codex
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# OpenAI

OpenAI provides developer APIs for GPT models. Codex supports **ChatGPT sign-in** for subscription
access or **API key** sign-in for usage-based access. Codex cloud requires ChatGPT sign-in, while
the Codex CLI supports either sign-in method. The Codex CLI caches login details in
`~/.codex/auth.json` (or your OS credential store), which Clawdbot can reuse.

## Option A: OpenAI API key (OpenAI Platform)

**Best for:** direct API access and usage-based billing.
Get your API key from the OpenAI dashboard.

### CLI setup

```bash  theme={null}
clawdbot onboard --auth-choice openai-api-key
# or non-interactive
clawdbot onboard --openai-api-key "$OPENAI_API_KEY"
```

### Config snippet

```json5  theme={null}
{
  env: { OPENAI_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "openai/gpt-5.2" } } }
}
```

## Option B: OpenAI Code (Codex) subscription

**Best for:** using ChatGPT/Codex subscription access instead of an API key.
Codex cloud requires ChatGPT sign-in, while the Codex CLI supports ChatGPT or API key sign-in.

Clawdbot can reuse your **Codex CLI** login (`~/.codex/auth.json`) or run the OAuth flow.

### CLI setup

```bash  theme={null}
# Reuse existing Codex CLI login
clawdbot onboard --auth-choice codex-cli

# Or run Codex OAuth in the wizard
clawdbot onboard --auth-choice openai-codex
```

### Config snippet

```json5  theme={null}
{
  agents: { defaults: { model: { primary: "openai-codex/gpt-5.2" } } }
}
```

## Notes

* Model refs always use `provider/model` (see [/concepts/models](/concepts/models)).
* Auth details + reuse rules are in [/concepts/oauth](/concepts/oauth).