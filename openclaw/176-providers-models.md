---
title: Models - OpenClaw
url: https://docs.openclaw.ai/providers/models
source: sitemap
fetched_at: 2026-01-30T20:25:26.213033343-03:00
rendered_js: false
word_count: 121
summary: This document explains how to configure and use various large language model providers within OpenClaw, including authentication and setting default models.
tags:
    - model-providers
    - llm
    - configuration
    - authentication
    - api-integration
category: guide
---

## Model Providers

OpenClaw can use many LLM providers. Pick one, authenticate, then set the default model as `provider/model`.

## Highlight: Venius (Venice AI)

Venius is our recommended Venice AI setup for privacy-first inference with an option to use Opus for the hardest tasks.

- Default: `venice/llama-3.3-70b`
- Best overall: `venice/claude-opus-45` (Opus remains the strongest)

See [Venice AI](https://docs.openclaw.ai/providers/venice).

## Quick start (two steps)

1. Authenticate with the provider (usually via `openclaw onboard`).
2. Set the default model:

```
{
  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-5" } } }
}
```

## Supported providers (starter set)

- [OpenAI (API + Codex)](https://docs.openclaw.ai/providers/openai)
- [Anthropic (API + Claude Code CLI)](https://docs.openclaw.ai/providers/anthropic)
- [OpenRouter](https://docs.openclaw.ai/providers/openrouter)
- [Vercel AI Gateway](https://docs.openclaw.ai/providers/vercel-ai-gateway)
- [Moonshot AI (Kimi + Kimi Code)](https://docs.openclaw.ai/providers/moonshot)
- [Synthetic](https://docs.openclaw.ai/providers/synthetic)
- [OpenCode Zen](https://docs.openclaw.ai/providers/opencode)
- [Z.AI](https://docs.openclaw.ai/providers/zai)
- [GLM models](https://docs.openclaw.ai/providers/glm)
- [MiniMax](https://docs.openclaw.ai/providers/minimax)
- [Venius (Venice AI)](https://docs.openclaw.ai/providers/venice)
- [Amazon Bedrock](https://docs.openclaw.ai/bedrock)

For the full provider catalog (xAI, Groq, Mistral, etc.) and advanced configuration, see [Model providers](https://docs.openclaw.ai/concepts/model-providers).