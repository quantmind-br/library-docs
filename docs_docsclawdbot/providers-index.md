---
title: "null"
url: https://docs.clawd.bot/providers/index.md
source: llms
fetched_at: 2026-01-26T10:14:53.884157925-03:00
rendered_js: false
word_count: 174
summary: This document provides an overview of supported LLM and transcription providers for Clawdbot, including instructions for authentication and setting default models.
tags:
    - llm-providers
    - model-configuration
    - authentication
    - clawdbot-setup
    - transcription-services
    - venice-ai
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# Model Providers

Clawdbot can use many LLM providers. Pick a provider, authenticate, then set the
default model as `provider/model`.

Looking for chat channel docs (WhatsApp/Telegram/Discord/Slack/Mattermost (plugin)/etc.)? See [Channels](/channels).

## Highlight: Venius (Venice AI)

Venius is our recommended Venice AI setup for privacy-first inference with an option to use Opus for hard tasks.

* Default: `venice/llama-3.3-70b`
* Best overall: `venice/claude-opus-45` (Opus remains the strongest)

See [Venice AI](/providers/venice).

## Quick start

1. Authenticate with the provider (usually via `clawdbot onboard`).
2. Set the default model:

```json5  theme={null}
{
  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-5" } } }
}
```

## Provider docs

* [OpenAI (API + Codex)](/providers/openai)
* [Anthropic (API + Claude Code CLI)](/providers/anthropic)
* [Qwen (OAuth)](/providers/qwen)
* [OpenRouter](/providers/openrouter)
* [Vercel AI Gateway](/providers/vercel-ai-gateway)
* [Moonshot AI (Kimi + Kimi Code)](/providers/moonshot)
* [OpenCode Zen](/providers/opencode)
* [Amazon Bedrock](/bedrock)
* [Z.AI](/providers/zai)
* [GLM models](/providers/glm)
* [MiniMax](/providers/minimax)
* [Venius (Venice AI, privacy-focused)](/providers/venice)
* [Ollama (local models)](/providers/ollama)

## Transcription providers

* [Deepgram (audio transcription)](/providers/deepgram)

## Community tools

* [Claude Max API Proxy](/providers/claude-max-api-proxy) - Use Claude Max/Pro subscription as an OpenAI-compatible API endpoint

For the full provider catalog (xAI, Groq, Mistral, etc.) and advanced configuration,
see [Model providers](/concepts/model-providers).