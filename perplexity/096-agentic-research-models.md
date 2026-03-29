---
title: Models
url: https://docs.perplexity.ai/docs/grounded-llm/responses/models.md
source: llms
fetched_at: 2026-02-04T07:24:17.604001152-03:00
rendered_js: false
word_count: 635
summary: This document provides a comprehensive list of supported models and their pricing for the Agentic Research API, including configuration methods and high-availability fallback options.
tags:
    - model-pricing
    - agentic-research-api
    - llm-providers
    - token-usage
    - model-fallback
    - api-configuration
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Models

> Explore available presets and third-party models for the Agentic Research API, including Perplexity presets and third-party model support.

### Available Models

The Agentic Research API supports direct access to models from multiple providers. All models are accessed directly from first-party providers with transparent token-based pricing.

Pricing rates are updated monthly and **reflect direct first-party provider pricing with no markup**. All charges are based on actual token consumption, and every API response includes exact token counts so you know your costs per request.

<Warning>
  Not all third-party models support all features (e.g., reasoning, tools). Check model documentation for specific capabilities.
</Warning>

| Model                             | Input Price                                                                | Output Price                                                                 | Cache Read Price     | Provider Documentation                                                                  |
| --------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------- |
| **Perplexity Models**             |                                                                            |                                                                              |                      |                                                                                         |
| `perplexity/sonar`                | \$0.25 / 1M tokens                                                         | \$2.50 / 1M tokens                                                           | \$0.0625 / 1M tokens | [Sonar](https://docs.perplexity.ai/docs/getting-started/models/models/sonar)            |
| **Anthropic Models**              |                                                                            |                                                                              |                      |                                                                                         |
| `anthropic/claude-opus-4-5`       | \$5 / 1M tokens                                                            | \$25 / 1M tokens                                                             | \$0.50 / 1M tokens   | [Claude Opus 4.5](https://www.anthropic.com/claude/opus)                                |
| `anthropic/claude-sonnet-4-5`     | \$3 / 1M tokens                                                            | \$15 / 1M tokens                                                             | \$0.30 / 1M tokens   | [Claude Sonnet 4.5](https://www.anthropic.com/claude/sonnet)                            |
| `anthropic/claude-haiku-4-5`      | \$1 / 1M tokens                                                            | \$5 / 1M tokens                                                              | \$0.10 / 1M tokens   | [Claude Haiku 4.5](https://www.anthropic.com/claude/haiku)                              |
| **OpenAI Models**                 |                                                                            |                                                                              |                      |                                                                                         |
| `openai/gpt-5.2`                  | \$1.75 / 1M tokens                                                         | \$14 / 1M tokens                                                             | \$0.175 / 1M tokens  | [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2)                              |
| `openai/gpt-5.1`                  | \$1.25 / 1M tokens                                                         | \$10 / 1M tokens                                                             | \$0.125 / 1M tokens  | [GPT-5.1](https://platform.openai.com/docs/models/gpt-5.1)                              |
| `openai/gpt-5-mini`               | \$0.25 / 1M tokens                                                         | \$2 / 1M tokens                                                              | \$0.025 / 1M tokens  | [GPT-5 Mini](https://platform.openai.com/docs/models/gpt-5-mini)                        |
| **Google Models**                 |                                                                            |                                                                              |                      |                                                                                         |
| `google/gemini-3-pro-preview`     | \$2.00 / 1M tokens (≤200k context)<br />\$4.00 / 1M tokens (>200k context) | \$12.00 / 1M tokens (≤200k context)<br />\$18.00 / 1M tokens (>200k context) | 90% discount         | [Gemini 3.0 Pro](https://ai.google.dev/gemini-api/docs/models#gemini-3-pro-preview)     |
| `google/gemini-3-flash-preview`   | \$0.50 / 1M tokens                                                         | \$3.00 / 1M tokens                                                           | 90% discount         | [Gemini 3.0 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-3-flash-preview) |
| `google/gemini-2.5-pro`           | \$1.25 / 1M tokens (≤200k context)<br />\$2.50 / 1M tokens (>200k context) | \$10.00 / 1M tokens (≤200k context)<br />\$15.00 / 1M tokens (>200k context) | 90% discount         | [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-pro_1)         |
| `google/gemini-2.5-flash`         | \$0.30 / 1M tokens                                                         | \$2.50 / 1M tokens                                                           | 90% discount         | [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash_1)     |
| **xAI Models**                    |                                                                            |                                                                              |                      |                                                                                         |
| `xai/grok-4-1-fast-non-reasoning` | \$0.20 / 1M tokens                                                         | \$0.50 / 1M tokens                                                           | \$0.05 / 1M tokens   | [Grok 4.1](https://docs.x.ai/docs/models/grok-4-1-fast-non-reasoning)                   |

<Tip>
  **See Your Costs in Real-Time:** Every response includes a `usage` field with exact input tokens, output tokens, and cache read tokens. Calculate your cost instantly using the pricing table above.

  Example response:

  ```json  theme={null}
  {
    "usage": {
      "input_tokens": 150,
      "output_tokens": 320,
      "total_tokens": 470
    }
  }
  ```
</Tip>

## Configuration Options

The Agentic Research API supports two ways to configure models:

1. [**Presets**](/docs/grounded-llm/responses/presets): Pre-configured model setups optimized for specific use cases.
2. [**Models**](/docs/grounded-llm/responses/models): Direct model selection, including third-party models

## Model Fallback

For high-availability applications, you can specify multiple models in a fallback chain. When one model fails or is unavailable, the API automatically tries the next model in the chain.

<Card title="Model Fallback Chain" icon="layer-group" href="/docs/grounded-llm/responses/model-fallback">
  Learn how to use model fallback chains to ensure high availability and reliability by automatically trying multiple models when one fails.
</Card>

<Info>
  **Example:**

  ```python  theme={null}
  response = client.responses.create(
      models=["openai/gpt-5.2", "openai/gpt-5.1", "openai/gpt-5-mini"],
      input="Your question here"
  )
  ```

  For detailed examples, pricing information, and best practices, see the [Model Fallback documentation](/docs/grounded-llm/responses/model-fallback).
</Info>

## Next Steps

<CardGroup cols={2}>
  <Card title="Model Fallback" icon="layer-group" href="/docs/grounded-llm/responses/model-fallback">
    Learn how to use model fallback chains for higher availability.
  </Card>

  <Card title="Presets" icon="gear" href="/docs/grounded-llm/responses/presets">
    Explore available presets and their configurations.
  </Card>

  <Card title="Agentic Research API Quickstart" icon="rocket" href="/docs/grounded-llm/responses/quickstart">
    Get started with your first Agentic Research API call.
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/responses-post">
    View complete endpoint documentation.
  </Card>
</CardGroup>