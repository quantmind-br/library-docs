---
title: Web Search
url: https://docs.perplexity.ai/docs/grounded-llm/responses/tools/web-search.md
source: llms
fetched_at: 2026-02-04T07:24:31.39513479-03:00
rendered_js: false
word_count: 571
summary: This document provides a technical overview of the web_search tool within the Agentic Research API, detailing its pricing, configuration, and advanced filtering capabilities.
tags:
    - web-search
    - agentic-research-api
    - tool-calling
    - search-filters
    - api-pricing
    - perplexity-ai
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Search

> Perform web searches with advanced filtering options using the web_search tool in the Agentic Research API.

## Overview

The `web_search` tool allows models to perform web searches with all the filtering capabilities of the [Search API](/docs/search/quickstart). Use it when you need current information, news, or data beyond the model's training cutoff.

## Pricing

Web search costs **\$5.00 per 1,000 search calls** (\$0.005 per search). You're also charged for tokens consumed when search results are embedded in the model's context.

<Accordion title="Cost Example">
  If a model makes 3 web searches and receives 1,800 tokens of search results, plus your original 100-token query, using `openai/gpt-5.2`:

  | Component     | Calculation              | Cost           |
  | ------------- | ------------------------ | -------------- |
  | Tool calls    | 3 searches × \$0.005     | \$0.015        |
  | Input tokens  | 1,900 tokens × \$1.75/1M | \$0.003325     |
  | Output tokens | 300 tokens × \$14.00/1M  | \$0.0042       |
  | **Total**     |                          | **\$0.022525** |
</Accordion>

## Basic Usage

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest developments in quantum computing?",
      tools=[
          {
              "type": "web_search"
          }
      ],
      instructions="You have access to a web_search tool. Use it for current information."
  )

  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest developments in quantum computing?",
      tools: [
          {
              type: "web_search"
          }
      ],
      instructions: "You have access to a web_search tool. Use it for current information."
  });

  console.log(response.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest developments in quantum computing?",
      "tools": [
        {
          "type": "web_search"
        }
      ],
      "instructions": "You have access to a web_search tool. Use it for current information."
    }' | jq
  ```
</CodeGroup>

## Search Filters

Configure filters in the `filters` object within the tool definition.

| Filter                       | Type             | Description                                                         | Limit            |
| ---------------------------- | ---------------- | ------------------------------------------------------------------- | ---------------- |
| `search_domain_filter`       | Array of strings | Filter by specific domains (allowlist or denylist with `-` prefix)  | Max 20 domains   |
| `search_language_filter`     | Array of strings | Filter by ISO 639-1 language codes                                  | Max 10 languages |
| `search_recency_filter`      | String           | Filter by time period: `"day"`, `"week"`, `"month"`, `"year"`       | -                |
| `search_after_date`          | String           | Filter results published after this date (format: `"M/D/YYYY"`)     | -                |
| `search_before_date`         | String           | Filter results published before this date (format: `"M/D/YYYY"`)    | -                |
| `last_updated_after_filter`  | String           | Filter results last updated after this date (format: `"M/D/YYYY"`)  | -                |
| `last_updated_before_filter` | String           | Filter results last updated before this date (format: `"M/D/YYYY"`) | -                |

### Domain Filtering

Filter search results to specific trusted sources:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest climate change findings?",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_domain_filter": [
                      "nature.com",
                      "science.org",
                      ".gov",
                      ".edu"
                  ]
              }
          }
      ],
      instructions="Use web_search to find recent academic and governmental sources."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest climate change findings?",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_domain_filter: [
                      "nature.com",
                      "science.org",
                      ".gov",
                      ".edu"
                  ]
              }
          }
      ],
      instructions: "Use web_search to find recent academic and governmental sources."
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest climate change findings?",
      "tools": [
        {
          "type": "web_search",
          "filters": {
            "search_domain_filter": ["nature.com", "science.org", ".gov", ".edu"]
          }
        }
      ],
      "instructions": "Use web_search to find recent academic and governmental sources."
    }' | jq
  ```
</CodeGroup>

<Tip>
  Use `-` prefix to exclude domains: `"-reddit.com"` excludes Reddit from results.
</Tip>

### Language Filtering

Search across specific languages:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are European perspectives on AI regulation?",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_language_filter": ["en", "fr", "de", "es"]
              }
          }
      ],
      instructions="Search for content in English, French, German, and Spanish."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are European perspectives on AI regulation?",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_language_filter: ["en", "fr", "de", "es"]
              }
          }
      ],
      instructions: "Search for content in English, French, German, and Spanish."
  });
  ```
</CodeGroup>

### Recency Filtering

Filter by time period for recent information:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest tech industry layoffs?",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_recency_filter": "week"
              }
          }
      ],
      instructions="Search for news from the past week only."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest tech industry layoffs?",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_recency_filter: "week"
              }
          }
      ],
      instructions: "Search for news from the past week only."
  });
  ```
</CodeGroup>

### Date Range Filtering

Filter by specific publication dates:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What happened in AI during Q1 2025?",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_after_date_filter": "1/1/2025",
                  "search_before_date_filter": "3/31/2025"
              }
          }
      ],
      instructions="Search for content published in Q1 2025."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What happened in AI during Q1 2025?",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_after_date_filter: "1/1/2025",
                  search_before_date_filter: "3/31/2025"
              }
          }
      ],
      instructions: "Search for content published in Q1 2025."
  });
  ```
</CodeGroup>

### Combining Filters

Combine multiple filters for precise control:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are recent academic findings on renewable energy?",
      tools=[
          {
              "type": "web_search",
              "filters": {
                  "search_domain_filter": ["nature.com", "science.org", ".edu"],
                  "search_language_filter": ["en"],
                  "search_recency_filter": "month"
              }
          }
      ],
      instructions="Search for recent English-language academic publications."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are recent academic findings on renewable energy?",
      tools: [
          {
              type: "web_search",
              filters: {
                  search_domain_filter: ["nature.com", "science.org", ".edu"],
                  search_language_filter: ["en"],
                  search_recency_filter: "month"
              }
          }
      ],
      instructions: "Search for recent English-language academic publications."
  });
  ```
</CodeGroup>

## User Location

Configure user location for localized search results:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are local news headlines?",
      tools=[
          {
              "type": "web_search",
              "user_location": {
                  "latitude": 37.7749,
                  "longitude": -122.4194,
                  "country": "US",
                  "city": "San Francisco",
                  "region": "CA"
              }
          }
      ],
      instructions="Search for local news in the San Francisco area."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are local news headlines?",
      tools: [
          {
              type: "web_search",
              user_location: {
                  latitude: 37.7749,
                  longitude: -122.4194,
                  country: "US",
                  city: "San Francisco",
                  region: "CA"
              }
          }
      ],
      instructions: "Search for local news in the San Francisco area."
  });
  ```
</CodeGroup>

### Location Properties

| Property    | Type   | Description                     |
| ----------- | ------ | ------------------------------- |
| `latitude`  | number | Latitude coordinate             |
| `longitude` | number | Longitude coordinate            |
| `country`   | string | ISO 3166-1 alpha-2 country code |
| `city`      | string | City name                       |
| `region`    | string | State/province/region code      |

## Token Control

Control the amount of content retrieved per search result using `max_tokens_per_page`:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Summarize recent AI breakthroughs",
      tools=[
          {
              "type": "web_search",
              "max_tokens_per_page": 1024
          }
      ],
      instructions="Search and summarize concisely."
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Summarize recent AI breakthroughs",
      tools: [
          {
              type: "web_search",
              max_tokens_per_page: 1024
          }
      ],
      instructions: "Search and summarize concisely."
  });
  ```
</CodeGroup>

<Tip>
  Lower `max_tokens_per_page` to reduce context token costs, especially when you need brief summaries rather than full content.
</Tip>

## Best Practices

### Effective Instructions

Guide the model on when and how to search:

```python  theme={null}
instructions = """You have access to a web_search tool.

Use web_search when:
- You need current information or recent news
- The query requires multiple sources
- You need to find specific domains or publications

Keep searches focused: use 2-5 word queries for best results."""
```

### Cost Management

* Use specific filters to narrow results and reduce unnecessary searches
* Set `max_tokens_per_page` to control token costs
* Combine filters to get relevant results in fewer calls

## Next Steps

<CardGroup cols={2}>
  <Card title="Fetch URL" icon="globe" href="/docs/grounded-llm/responses/tools/fetch-url">
    Extract full content from specific URLs.
  </Card>

  <Card title="Function Calling" icon="code" href="/docs/grounded-llm/responses/tools/function-calling">
    Define custom functions for external integrations.
  </Card>

  <Card title="Search API" icon="magnifying-glass" href="/docs/search/quickstart">
    Learn more about search capabilities.
  </Card>

  <Card title="Domain Filters Guide" icon="filter" href="/docs/grounded-llm/filters/domain-filters">
    Advanced domain filtering techniques.
  </Card>
</CardGroup>