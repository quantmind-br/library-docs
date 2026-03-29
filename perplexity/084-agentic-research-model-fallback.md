---
title: Model Fallback
url: https://docs.perplexity.ai/docs/grounded-llm/responses/model-fallback.md
source: llms
fetched_at: 2026-02-04T07:24:13.964897674-03:00
rendered_js: false
word_count: 335
summary: This document explains how to configure model fallback by specifying multiple models in an array to ensure automatic failover and higher availability. It details the execution order, support for multiple providers, and the billing implications for the utilized model.
tags:
    - model-fallback
    - api-integration
    - failover-mechanisms
    - high-availability
    - provider-redundancy
    - error-handling
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Model Fallback

> Specify multiple models in a fallback chain for higher availability and automatic failover.

## Overview

Model fallback enables specifying multiple models in a `models` array. The API tries each model in order until one succeeds, providing automatic failover when a model is unavailable.

## How It Works

Provide a `models` array containing up to 5 models:

1. The API tries the first model in the array
2. If it fails or is unavailable, the next model is tried
3. This continues until one succeeds or all models are exhausted

The `models` array takes precedence over the single `model` field when both are provided.

<Info>
  **Benefits:**

  * **Higher availability**: Automatic failover when primary model is unavailable
  * **Provider redundancy**: Use models from different providers for maximum reliability
  * **Seamless operation**: No code refactoring needed, fallback is handled automatically by the API
</Info>

## Basic Example

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      models=["openai/gpt-5.2", "openai/gpt-5.1", "openai/gpt-5-mini"],
      input="What are the latest developments in AI?",
      instructions="You have access to a web_search tool. Use it for questions about current events.",
  )

  print(f"Model used: {response.model}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      models: ["openai/gpt-5.2", "openai/gpt-5.1", "openai/gpt-5-mini"],
      input: "What are the latest developments in AI?",
      instructions: "You have access to a web_search tool. Use it for questions about current events.",
  });

  console.log(`Model used: ${response.model}`);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "models": ["openai/gpt-5.2", "openai/gpt-5.1", "openai/gpt-5-mini"],
      "input": "What are the latest developments in AI?",
      "instructions": "You have access to a web_search tool. Use it for questions about current events."
    }'
  ```
</CodeGroup>

## Cross-Provider Fallback

For maximum reliability, use models from different providers:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      models=[
          "openai/gpt-5.2",
          "anthropic/claude-sonnet-4-5",
          "google/gemini-2.5-pro"
      ],
      input="Explain quantum computing in detail",
  )
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      models: [
          "openai/gpt-5.2",
          "anthropic/claude-sonnet-4-5",
          "google/gemini-2.5-pro"
      ],
      input: "Explain quantum computing in detail",
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "models": [
        "openai/gpt-5.2",
        "anthropic/claude-sonnet-4-5",
        "google/gemini-2.5-pro"
      ],
      "input": "Explain quantum computing in detail"
    }'
  ```
</CodeGroup>

## Pricing

<Warning>
  Billing is based on the model that serves the request, not all models in the fallback chain.
</Warning>

The `model` field in the response indicates which model was used, and the `usage` field shows the token counts for that model.

<Accordion title="Example">
  **Request:**

  ```json  theme={null}
  {
    "models": ["openai/gpt-5.2", "openai/gpt-5.1"],
    "input": "..."
  }
  ```

  **Response** (if first model failed):

  ```json  theme={null}
  {
    "model": "openai/gpt-5.1",
    "usage": {
      "input_tokens": 150,
      "output_tokens": 320,
      "total_tokens": 470
    }
  }
  ```

  In this case, billing is based on `gpt-5.1` pricing for 470 tokens.
</Accordion>

<Tip>
  Place preferred models first in the array. Consider pricing differences when ordering the fallback chain.
</Tip>

## Next Steps

<CardGroup cols={2}>
  <Card title="Models" icon="brain" href="/docs/grounded-llm/responses/models">
    Explore available models and their pricing.
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