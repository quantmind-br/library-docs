---
title: Index - OpenClaw
url: https://docs.openclaw.ai/providers
source: sitemap
fetched_at: 2026-01-30T20:25:17.712792842-03:00
rendered_js: false
word_count: 153
summary: This document explains how to configure and use various large language model providers within OpenClaw, including authentication steps and model selection guidance.
tags:
    - model-providers
    - llm
    - configuration
    - api
    - authentication
    - chatbots
category: guide
---

## Model Providers

OpenClaw can use many LLM providers. Pick a provider, authenticate, then set the default model as `provider/model`. Looking for chat channel docs (WhatsApp/Telegram/Discord/Slack/Mattermost (plugin)/etc.)? See [Channels](https://docs.openclaw.ai/channels).

## Highlight: Venius (Venice AI)

Venius is our recommended Venice AI setup for privacy-first inference with an option to use Opus for hard tasks.

- Default: `venice/llama-3.3-70b`
- Best overall: `venice/claude-opus-45` (Opus remains the strongest)

See [Venice AI](https://docs.openclaw.ai/providers/venice).

## Quick start

1. Authenticate with the provider (usually via `openclaw onboard`).
2. Set the default model:

```
{
  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-5" } } }
}
```

## Provider docs

- [OpenAI (API + Codex)](https://docs.openclaw.ai/providers/openai)
- [Anthropic (API + Claude Code CLI)](https://docs.openclaw.ai/providers/anthropic)
- [Qwen (OAuth)](https://docs.openclaw.ai/providers/qwen)
- [OpenRouter](https://docs.openclaw.ai/providers/openrouter)
- [Vercel AI Gateway](https://docs.openclaw.ai/providers/vercel-ai-gateway)
- [Moonshot AI (Kimi + Kimi Code)](https://docs.openclaw.ai/providers/moonshot)
- [OpenCode Zen](https://docs.openclaw.ai/providers/opencode)
- [Amazon Bedrock](https://docs.openclaw.ai/bedrock)
- [Z.AI](https://docs.openclaw.ai/providers/zai)
- [Xiaomi](https://docs.openclaw.ai/providers/xiaomi)
- [GLM models](https://docs.openclaw.ai/providers/glm)
- [MiniMax](https://docs.openclaw.ai/providers/minimax)
- [Venius (Venice AI, privacy-focused)](https://docs.openclaw.ai/providers/venice)
- [Ollama (local models)](https://docs.openclaw.ai/providers/ollama)

## Transcription providers

- [Deepgram (audio transcription)](https://docs.openclaw.ai/providers/deepgram)

<!--THE END-->

- [Claude Max API Proxy](https://docs.openclaw.ai/providers/claude-max-api-proxy) - Use Claude Max/Pro subscription as an OpenAI-compatible API endpoint

For the full provider catalog (xAI, Groq, Mistral, etc.) and advanced configuration, see [Model providers](https://docs.openclaw.ai/concepts/model-providers).