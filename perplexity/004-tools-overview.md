---
title: Tools Overview
url: https://docs.perplexity.ai/docs/grounded-llm/responses/tools/overview.md
source: llms
fetched_at: 2026-02-04T07:24:31.172577931-03:00
rendered_js: false
word_count: 241
summary: This document provides an overview of the built-in and custom tools available in the Agentic Research API, explaining how to configure them to extend model capabilities with web search and function calling.
tags:
    - agentic-research-api
    - web-search
    - fetch-url
    - function-calling
    - tool-configuration
    - api-tools
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Tools Overview

> Extend model capabilities with built-in tools and custom functions in the Agentic Research API.

## Overview

The Agentic Research API provides tools that extend model capabilities beyond their training data. Tools must be explicitly configured in your API request—once enabled, models autonomously decide when to use them based on your instructions.

<CardGroup cols={3}>
  <Card title="web_search" icon="magnifying-glass" href="/docs/grounded-llm/responses/tools/web-search">
    Perform web searches with filtering by domain, language, recency, and date range.
  </Card>

  <Card title="fetch_url" icon="globe" href="/docs/grounded-llm/responses/tools/fetch-url">
    Fetch and extract content from specific URLs.
  </Card>

  <Card title="Function Calling" icon="code" href="/docs/grounded-llm/responses/tools/function-calling">
    Define custom functions to connect models to your own systems and APIs.
  </Card>
</CardGroup>

## Built-in vs Custom Tools

| Type         | Tools                     | Use Case                                   |
| ------------ | ------------------------- | ------------------------------------------ |
| **Built-in** | `web_search`, `fetch_url` | Real-time web information retrieval        |
| **Custom**   | Your functions            | Connect to databases, APIs, business logic |

## Quick Example

Enable tools by adding them to the `tools` array in your request:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest AI developments?",
      tools=[
          {"type": "web_search"},
          {"type": "fetch_url"}
      ],
      instructions="Use web_search for current information. Use fetch_url when you need full article content."
  )

  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest AI developments?",
      tools: [
          { type: "web_search" },
          { type: "fetch_url" }
      ],
      instructions: "Use web_search for current information. Use fetch_url when you need full article content."
  });

  console.log(response.output_text);
  ```
</CodeGroup>

## Pricing

| Tool             | Cost                                        |
| ---------------- | ------------------------------------------- |
| `web_search`     | \$5.00 per 1,000 calls                      |
| `fetch_url`      | \$0.50 per 1,000 calls                      |
| Function Calling | No additional cost (standard token pricing) |

<Info>
  You're also charged for tokens consumed when tool results are embedded in the model's context. See the [Pricing page](/docs/getting-started/pricing) for full details.
</Info>

## Next Steps

<CardGroup cols={2}>
  <Card title="Web Search" icon="magnifying-glass" href="/docs/grounded-llm/responses/tools/web-search">
    Learn about search filters and localization options.
  </Card>

  <Card title="Fetch URL" icon="globe" href="/docs/grounded-llm/responses/tools/fetch-url">
    Extract content from specific web pages.
  </Card>

  <Card title="Function Calling" icon="code" href="/docs/grounded-llm/responses/tools/function-calling">
    Define custom functions for external integrations.
  </Card>

  <Card title="Presets" icon="gear" href="/docs/grounded-llm/responses/presets">
    Use pre-configured presets with built-in tools.
  </Card>
</CardGroup>