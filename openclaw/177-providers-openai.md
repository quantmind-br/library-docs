---
title: Openai - OpenClaw
url: https://docs.openclaw.ai/providers/openai
source: sitemap
fetched_at: 2026-01-30T20:25:21.642889262-03:00
rendered_js: false
word_count: 105
summary: This document explains how to authenticate and configure access to OpenAI's GPT models using either API keys or ChatGPT/Codex subscriptions through the OpenCLAW platform.
tags:
    - api-authentication
    - openai-api
    - codex-integration
    - cli-setup
    - model-configuration
    - oauth
category: guide
---

OpenAI provides developer APIs for GPT models. Codex supports **ChatGPT sign-in** for subscription access or **API key** sign-in for usage-based access. Codex cloud requires ChatGPT sign-in.

## Option A: OpenAI API key (OpenAI Platform)

**Best for:** direct API access and usage-based billing. Get your API key from the OpenAI dashboard.

### CLI setup

```
openclaw onboard --auth-choice openai-api-key
# or non-interactive
openclaw onboard --openai-api-key "$OPENAI_API_KEY"
```

### Config snippet

```
{
  env: { OPENAI_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "openai/gpt-5.2" } } }
}
```

## Option B: OpenAI Code (Codex) subscription

**Best for:** using ChatGPT/Codex subscription access instead of an API key. Codex cloud requires ChatGPT sign-in, while the Codex CLI supports ChatGPT or API key sign-in.

### CLI setup

```
# Run Codex OAuth in the wizard
openclaw onboard --auth-choice openai-codex

# Or run OAuth directly
openclaw models auth login --provider openai-codex
```

### Config snippet

```
{
  agents: { defaults: { model: { primary: "openai-codex/gpt-5.2" } } }
}
```

## Notes

- Model refs always use `provider/model` (see [/concepts/models](https://docs.openclaw.ai/concepts/models)).
- Auth details + reuse rules are in [/concepts/oauth](https://docs.openclaw.ai/concepts/oauth).