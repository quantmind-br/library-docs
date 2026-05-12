---
title: Model choice | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/model-choice
source: sitemap
fetched_at: 2026-04-29T15:03:49.153915763-03:00
rendered_js: false
word_count: 324
summary: This document provides an overview of the Large Language Models supported by Warp, explains how to configure and switch between them, and details the platform's model fallback and zero data retention policies.
tags:
    - llm-support
    - model-configuration
    - data-privacy
    - agent-profiles
    - model-fallback
    - ai-integration
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp offers a curated set of LLMs to power your Agentic Development Environment. Use the `model_id` values below when configuring via the [Oz Platform](https://docs.warp.dev/agent-platform/cloud-agents/platform) or [CLI](https://docs.warp.dev/reference/cli).

## Available models

### Auto models

Auto models perform well across all workflows and let Warp manage selection dynamically.

| Provider | Model | `model_id` |
|----------|-------|-----------|
| OpenAI | GPT-4.1 | `openai/gpt-4.1` |
| OpenAI | o4-mini | `openai/o4-mini` |
| Anthropic | Claude Sonnet 4.5 | `anthropic/claude-sonnet-4-5-20250514` |
| Anthropic | Claude Opus 4 | `anthropic/claude-opus-4-5-20251120` |
| Anthropic | Claude 3.7 Sonnet | `anthropic/claude-3-7-sonnet-20250620` |
| Anthropic | Claude 3.5 Sonnet | `anthropic/claude-3-5-sonnet-20241022` |
| Google | Gemini 2.5 Pro | `google/gemini-2.5-pro-preview-06-05` |
| Google | Gemini 2.0 Flash | `google/gemini-2.0-flash` |
| Google | Gemini 2.5 Flash | `google/gemini-2.5-flash` |

### Hosted models via Fireworks AI

Warp also supports open source models hosted via Fireworks AI without requiring your own inference infrastructure.

## How to change models

Click the model name in the prompt input to open a dropdown. Your selection persists automatically for future prompts.

## Model fallback

Warp automatically uses a fallback model if your selected model is unavailable due to provider outages or capacity issues. When the original model becomes available again, Warp switches back automatically.

## Configuring models per Agent Profile

Set the base model for each [Agent Profile](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/agent-profiles-permissions) in **Settings** > **Agents** > **Profiles**, alongside autonomy, tool access, and other permissions. The base model also applies to [Planning](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/planning).

## Zero data retention policies

Warp has executed **Zero Data Retention (ZDR)** agreements with these LLM providers:

- OpenAI
- Anthropic
- Google
- xAI
- Fireworks AI
- Baseten

Under ZDR, by default across all plans:
- Providers commit **not** to train models on any customer data processed through Warp.
- Providers commit to delete inputs and outputs within a fixed time period after generating output.

Warp enforces these commitments through technical measures and contractual safeguards.

#llm-support #model-configuration #data-privacy #agent-profiles
