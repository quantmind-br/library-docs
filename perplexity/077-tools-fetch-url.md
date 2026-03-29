---
title: Fetch URL
url: https://docs.perplexity.ai/docs/grounded-llm/responses/tools/fetch-url.md
source: llms
fetched_at: 2026-02-04T07:24:25.619434417-03:00
rendered_js: false
word_count: 338
summary: This document explains how to use the fetch_url tool in the Agentic Research API to retrieve and extract full content from specific web addresses. It provides details on pricing, implementation across various programming languages, and strategies for combining it with web search capabilities.
tags:
    - agentic-research-api
    - fetch-url
    - content-extraction
    - web-scraping
    - api-pricing
    - tool-integration
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch URL

> Fetch and extract content from specific URLs using the fetch_url tool in the Agentic Research API.

## Overview

The `fetch_url` tool fetches and extracts content from specific URLs. Use it when you need the full content of a particular web page, article, or document rather than search results.

## Pricing

URL fetch costs **\$0.50 per 1,000 requests** (\$0.0005 per fetch). You're also charged for tokens consumed when fetched content is embedded in the model's context.

<Accordion title="Cost Example">
  If a model fetches 2 URLs with 3,000 tokens of content, plus your original 80-token query, using `anthropic/claude-sonnet-4-5`:

  | Component     | Calculation              | Cost          |
  | ------------- | ------------------------ | ------------- |
  | Tool calls    | 2 fetches × \$0.0005     | \$0.001       |
  | Input tokens  | 3,080 tokens × \$3.00/1M | \$0.00924     |
  | Output tokens | 500 tokens × \$15.00/1M  | \$0.0075      |
  | **Total**     |                          | **\$0.01774** |
</Accordion>

## Basic Usage

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Summarize the content at https://example.com/article",
      tools=[
          {
              "type": "fetch_url"
          }
      ],
      instructions="Use fetch_url to retrieve and summarize the article."
  )

  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Summarize the content at https://example.com/article",
      tools: [
          {
              type: "fetch_url"
          }
      ],
      instructions: "Use fetch_url to retrieve and summarize the article."
  });

  console.log(response.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Summarize the content at https://example.com/article",
      "tools": [
        {
          "type": "fetch_url"
        }
      ],
      "instructions": "Use fetch_url to retrieve and summarize the article."
    }' | jq
  ```
</CodeGroup>

## Use Cases

<CardGroup cols={2}>
  <Card title="Article Summarization" icon="newspaper">
    Fetch and summarize specific articles or blog posts.
  </Card>

  <Card title="Documentation Analysis" icon="book">
    Extract and analyze technical documentation.
  </Card>

  <Card title="Content Comparison" icon="code-compare">
    Compare content from multiple specific URLs.
  </Card>

  <Card title="URL Validation" icon="check">
    Verify content at specific URLs before sharing.
  </Card>
</CardGroup>

## Combining with Web Search

Use `fetch_url` together with `web_search` for comprehensive information gathering—search to find relevant pages, then fetch full content from the most relevant results:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Find recent articles about quantum computing and summarize the top result",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_recency_filter": "week"
              }
          },
          {
              "type": "fetch_url"
          }
      ],
      instructions="First use web_search to find recent articles, then use fetch_url to retrieve the full content of the most relevant article and provide a detailed summary."
  )

  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Find recent articles about quantum computing and summarize the top result",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_recency_filter: "week"
              }
          },
          {
              type: "fetch_url"
          }
      ],
      instructions: "First use web_search to find recent articles, then use fetch_url to retrieve the full content of the most relevant article and provide a detailed summary."
  });

  console.log(response.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Find recent articles about quantum computing and summarize the top result",
      "tools": [
        {
          "type": "web_search",
          "filters": {
            "search_recency_filter": "week"
          }
        },
        {
          "type": "fetch_url"
        }
      ],
      "instructions": "First use web_search to find recent articles, then use fetch_url to retrieve the full content of the most relevant article and provide a detailed summary."
    }' | jq
  ```
</CodeGroup>

## Best Practices

### When to Use fetch\_url vs web\_search

| Use `fetch_url` when...         | Use `web_search` when...                |
| ------------------------------- | --------------------------------------- |
| You have a specific URL         | You need to find relevant pages         |
| You need full page content      | You need snippets from multiple sources |
| Analyzing a particular document | Researching a broad topic               |
| Verifying specific claims       | Finding current news or events          |

### Effective Instructions

Guide the model on when to fetch URLs:

```python  theme={null}
instructions = """You have access to web_search and fetch_url tools.

Use fetch_url when:
- You need detailed content from a specific URL
- You want to analyze a particular article or document
- You need to verify specific claims from a URL

Use web_search first to find URLs, then fetch_url to get full content."""
```

## Next Steps

<CardGroup cols={2}>
  <Card title="Web Search" icon="magnifying-glass" href="/docs/grounded-llm/responses/tools/web-search">
    Search the web with filters and localization.
  </Card>

  <Card title="Function Calling" icon="code" href="/docs/grounded-llm/responses/tools/function-calling">
    Define custom functions for external integrations.
  </Card>

  <Card title="Presets" icon="gear" href="/docs/grounded-llm/responses/presets">
    Use pre-configured presets with built-in tools.
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/responses-post">
    View complete endpoint documentation.
  </Card>
</CardGroup>