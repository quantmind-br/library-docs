---
title: Models - Zencoder Docs
url: https://docs.zencoder.ai/features/models
source: crawler
fetched_at: 2026-01-23T09:28:13.330646032-03:00
rendered_js: false
word_count: 542
summary: This document explains how to use the Zencoder model selector to switch between various LLMs and manage usage costs through plan-based entitlements and multipliers.
tags:
    - model-selector
    - llm-options
    - zencoder-pricing
    - byok
    - usage-multipliers
    - anthropic
    - openai
    - model-switching
category: guide
---

## Overview

Zencoder now has a model selector in the chat input. Use the dropdown to pick which LLM runs your messages. The options you see depend on your plan and entitlements.

- Currently, the model selector is available to users on the new pricing plans ( not available on legacy plans)
- Model choices may differ by plan; higher plans unlock additional models
- Select the model that fits your task from the selector (Auto, Auto+, Haiku 4.5 Parallel Thinking, Sonnet 4, Sonnet 4.5 Parallel Thinking, Opus 4.1, Opus 4.5 Parallel Thinking, Gemini Pro 3.0, GPT-5.1-Codex, GPT-5.1-Codex-mini, Grok Code Fast 1).

As a truly vendor-agnostic platform, Zencoder supports flagship models from OpenAI, Anthropic, Google, and xAI, allowing you to choose your preferred model while benefiting from our infrastructure, capabilities, and excellent user experience.

## Available models (subject to change)

The Auto model routes across a tuned mix of self-hosted and vendor models for the best balance of speed, quality, and cost. ![Model selector showing available models and multipliers](https://mintcdn.com/forgoodaiinc/PvUw4WPikTeUvWXG/images/model-selector-nov25.png?fit=max&auto=format&n=PvUw4WPikTeUvWXG&q=85&s=72f879b44acb588d6d4e7ac51a11c454)

ModelProviderMultiplierPlan RequirementsAutoZencoder1×All plansAuto+Zencoder2.5×All plansSonnet 4Anthropic2×All plansHaiku 4.5 Parallel ThinkingAnthropic1×Starter, Core, Advanced, MaxSonnet 4.5 Parallel Thinking\*\*\*Anthropic3×Starter, Core, Advanced, MaxOpus 4.1\*\*Anthropic10×Advanced, MaxOpus 4.5 Parallel Thinking\*\*Anthropic5×Advanced, MaxGemini Pro 3.0Google2×All plansGPT-5.1-CodexOpenAI1×Starter, Core, Advanced, MaxGPT-5.1-Codex-miniOpenAI0.5×Starter, Core, Advanced, MaxGrok Code Fast 1xAI0.25×All plans

Grok Code Fast 1 at 0.25× multiplier is our most cost-efficient model offering, followed by GPT-5.1-Codex-mini at 0.5×, and Auto at 1×. All multipliers and model availability are subject to change. Model availability evolves over time. We may add, remove, or upgrade models without notice as providers change capabilities and pricing. Your selector will always reflect the currently supported set for your plan.

## Cost multipliers and Premium LLM calls

Zencoder measures usage in Premium LLM calls. Some models use a multiplier to reflect provider costs or parallel reasoning. See the table above and the screenshot for current multipliers.

## Plan-based availability

Not all plans have access to all models. The selector shows what your current plan can use. If you recently upgraded but don’t see expected options, restart your IDE to refresh entitlements.

- **Starter, Core, Advanced and Max plans**: Model model selector with allocated models, including GPT-5 access
- **Legacy plans**: Model selector is not available

## Bring Your Own Key (BYOK)

You can use your own API key for certain providers. This is useful if you:

- Want to remove daily Premium LLM call limits for those requests
- Prefer billing directly with the provider

Supported providers in the UI today: Anthropic and OpenAI.

### Enable BYOK

## When to switch models

- Use the **Auto** model for most coding tasks - it balances speed, quality, and cost
- Use the **Auto+** for superior performance on complex tasks (2.5× multiplier)
- Use the **Haiku 4.5 Parallel Thinking** if you want speed and cost-efficient option (1× multiplier)
- Use **Grok Code Fast 1** when you need the most cost-efficient option (0.25× multiplier)
- Use **GPT-5.1-Codex-mini** for cost-efficient code generation (0.5× multiplier)
- Use **Gemini Pro 3.0** for high-quality performance with balanced capability (2× multiplier)
- Use **Sonnet 4.5 Parallel Thinking** for spec-driven development tasks requiring persistent state tracking and parallel execution
- Use **GPT-5.1-Codex** for specialized code generation tasks
- Use **Opus 4.1** for challenging tasks requiring high capability (Advanced and Max plans, 10× multiplier)
- Use **Opus 4.5 Parallel Thinking** (Advanced and Max plans) for the most complex reasoning tasks, keeping the 5× multiplier in mind

## Troubleshooting