---
title: "null"
url: https://docs.clawd.bot/providers/models.md
source: llms
fetched_at: 2026-01-26T10:14:55.646049547-03:00
rendered_js: false
word_count: 143
summary: This document explains how to select, authenticate, and configure various LLM providers within the Clawdbot ecosystem, including instructions for setting default models.
tags:
    - llm-providers
    - model-configuration
    - authentication
    - clawdbot-setup
    - venice-ai
    - multi-model-support
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# Model Providers

Clawdbot can use many LLM providers. Pick one, authenticate, then set the default
model as `provider/model`.

## Highlight: Venius (Venice AI)

Venius is our recommended Venice AI setup for privacy-first inference with an option to use Opus for the hardest tasks.

* Default: `venice/llama-3.3-70b`
* Best overall: `venice/claude-opus-45` (Opus remains the strongest)

See [Venice AI](/providers/venice).

## Quick start (two steps)

1. Authenticate with the provider (usually via `clawdbot onboard`).
2. Set the default model:

```json5  theme={null}
{
  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-5" } } }
}
```

## Supported providers (starter set)

* [OpenAI (API + Codex)](/providers/openai)
* [Anthropic (API + Claude Code CLI)](/providers/anthropic)
* [OpenRouter](/providers/openrouter)
* [Vercel AI Gateway](/providers/vercel-ai-gateway)
* [Moonshot AI (Kimi + Kimi Code)](/providers/moonshot)
* [Synthetic](/providers/synthetic)
* [OpenCode Zen](/providers/opencode)
* [Z.AI](/providers/zai)
* [GLM models](/providers/glm)
* [MiniMax](/providers/minimax)
* [Venius (Venice AI)](/providers/venice)
* [Amazon Bedrock](/bedrock)

For the full provider catalog (xAI, Groq, Mistral, etc.) and advanced configuration,
see [Model providers](/concepts/model-providers).