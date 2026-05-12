---
title: Search | Firecrawl
url: https://docs.firecrawl.dev/features/search
source: sitemap
fetched_at: 2026-03-23T07:24:29.602202-03:00
rendered_js: false
word_count: 789
summary: This document describes the Firecrawl search API, detailing how to perform web, image, and news searches, filter by category or time, and retrieve scraped content in a single operation.
tags:
    - api
    - web-scraping
    - search-engine
    - data-extraction
    - firecrawl
    - api-documentation
category: api
---

Firecrawl’s search API allows you to perform web searches and optionally scrape the search results in one operation.

- Choose specific output formats (markdown, HTML, links, screenshots)
- Search the web with customizable parameters (location, etc.)
- Optionally retrieve content from search results in various formats
- Control the number of results and set timeouts

For details, see the [Search Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/search).

## Performing a Search with Firecrawl

### /search endpoint

Used to perform web searches and optionally retrieve content from the results.

### Installation

### Basic Usage

### Response

SDKs will return the data object directly. cURL will return the complete payload.

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - The Web Data API for AI",
        "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders.",
        "position": 1
      },
      {
        "url": "https://github.com/firecrawl/firecrawl",
        "title": "mendableai/firecrawl: Turn entire websites into LLM-ready ... - GitHub",
        "description": "Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data.",
        "position": 2
      },
      ...
    ],
    "images": [
      {
        "title": "Quickstart | Firecrawl",
        "imageUrl": "https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png",
        "imageWidth": 5814,
        "imageHeight": 1200,
        "url": "https://docs.firecrawl.dev/",
        "position": 1
      },
      ...
    ],
    "news": [
      {
        "title": "Y Combinator startup Firecrawl is ready to pay $1M to hire three AI agents as employees",
        "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
        "snippet": "It's now placed three new ads on YC's job board for “AI agents only” and has set aside a $1 million budget total to make it happen.",
        "date": "3 months ago",
        "position": 1
      },
      ...
    ]
  }
}
```

## Search result types

In addition to regular web results, Search supports specialized result types via the `sources` parameter:

- `web`: standard web results (default)
- `news`: news-focused results
- `images`: image search results

You can request multiple sources in a single call (e.g., `sources: ["web", "news"]`). When you do, the `limit` parameter applies **per source type** — so `limit: 5` with `sources: ["web", "news"]` returns up to 5 web results and up to 5 news results (10 total). If you need different parameters per source (for example, different `limit` values or different `scrapeOptions`), make separate calls instead.

## Search Categories

Filter search results by specific categories using the `categories` parameter:

- `github`: Search within GitHub repositories, code, issues, and documentation
- `research`: Search academic and research websites (arXiv, Nature, IEEE, PubMed, etc.)
- `pdf`: Search for PDFs

### GitHub Category Search

Search specifically within GitHub repositories:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "web scraping python",
    "categories": ["github"],
    "limit": 10
  }'
```

### Research Category Search

Search academic and research websites:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "machine learning transformers",
    "categories": ["research"],
    "limit": 10
  }'
```

### Mixed Category Search

Combine multiple categories in one search:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "neural networks",
    "categories": ["github", "research"],
    "limit": 15
  }'
```

### Category Response Format

Each search result includes a `category` field indicating its source:

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/neural-network",
        "title": "Neural Network Implementation",
        "description": "A PyTorch implementation of neural networks",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "Advances in Neural Network Architecture",
        "description": "Research paper on neural network improvements",
        "category": "research"
      }
    ]
  }
}
```

Examples:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "openai",
    "sources": ["news"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "jupiter",
    "sources": ["images"],
    "limit": 8
  }'
```

### HD Image Search with Size Filtering

Use images operators to find high-resolution images:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sunset imagesize:1920x1080",
    "sources": ["images"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "mountain wallpaper larger:2560x1440",
    "sources": ["images"],
    "limit": 8
  }'
```

**Common HD resolutions:**

- `imagesize:1920x1080` - Full HD (1080p)
- `imagesize:2560x1440` - QHD (1440p)
- `imagesize:3840x2160` - 4K UHD
- `larger:1920x1080` - HD and above
- `larger:2560x1440` - QHD and above

## Search with Content Scraping

Search and retrieve content from the search results in one operation.

Every option in scrape endpoint is supported by this search endpoint through the `scrapeOptions` parameter.

### Response with Scraped Content

```
{
  "success": true,
  "data": [
    {
      "title": "Firecrawl - The Ultimate Web Scraping API",
      "description": "Firecrawl is a powerful web scraping API that turns any website into clean, structured data for AI and analysis.",
      "url": "https://firecrawl.dev/",
      "markdown": "# Firecrawl\n\nThe Ultimate Web Scraping API\n\n## Turn any website into clean, structured data\n\nFirecrawl makes it easy to extract data from websites for AI applications, market research, content aggregation, and more...",
      "links": [
        "https://firecrawl.dev/pricing",
        "https://firecrawl.dev/docs",
        "https://firecrawl.dev/guides"
      ],
      "metadata": {
        "title": "Firecrawl - The Ultimate Web Scraping API",
        "description": "Firecrawl is a powerful web scraping API that turns any website into clean, structured data for AI and analysis.",
        "sourceURL": "https://firecrawl.dev/",
        "statusCode": 200
      }
    }
  ]
}
```

## Advanced Search Options

Firecrawl’s search API supports various parameters to customize your search:

### Location Customization

### Time-Based Search

Use the `tbs` parameter to filter results by time. Note that `tbs` only applies to `web` source results — it does not filter `news` or `images` results. If you need time-filtered news, consider using a `web` source with the `site:` operator to target specific news domains.

Common `tbs` values:

- `qdr:h` - Past hour
- `qdr:d` - Past 24 hours
- `qdr:w` - Past week
- `qdr:m` - Past month
- `qdr:y` - Past year
- `sbd:1` - Sort by date (newest first)

For more precise time filtering, you can specify exact date ranges using the custom date range format:

You can combine `sbd:1` with time filters to get date-sorted results within a time range. For example, `sbd:1,qdr:w` returns results from the past week sorted newest first, and `sbd:1,cdr:1,cd_min:12/1/2024,cd_max:12/31/2024` returns results from December 2024 sorted by date.

### Custom Timeout

Set a custom timeout for search operations:

## Zero Data Retention (ZDR)

For teams with strict data handling requirements, Firecrawl offers Zero Data Retention (ZDR) options for the `/search` endpoint via the `enterprise` parameter. ZDR search is available on Enterprise plans — visit [firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) to get started.

### End-to-End ZDR

With end-to-end ZDR, both Firecrawl and our upstream search provider enforce zero data retention. No query or result data is stored at any point in the pipeline.

- **Cost:** 10 credits per 10 results
- **Parameter:** `enterprise: ["zdr"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["zdr"]
  }'
```

### Anonymized ZDR

With anonymized ZDR, Firecrawl enforces full zero data retention on our side. Our search provider may cache the query, but it is fully anonymized — no identifying information is attached.

- **Cost:** 2 credits per 10 results
- **Parameter:** `enterprise: ["anon"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["anon"]
  }'
```

### Combining Search ZDR with Scrape ZDR

If you are using search with content scraping (`scrapeOptions`), the `enterprise` parameter covers the search portion while `zeroDataRetention` in `scrapeOptions` covers the scraping portion. To get full ZDR across both, set both:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 5,
    "enterprise": ["zdr"],
    "scrapeOptions": {
      "formats": ["markdown"],
      "zeroDataRetention": true
    }
  }'
```

## Cost Implications

The cost of a search is 2 credits per 10 search results. If scraping options are enabled, the standard scraping costs apply to each search result:

- **Basic scrape**: 1 credit per webpage
- **PDF parsing**: 1 credit per PDF page
- **Enhanced proxy mode**: 4 additional credits per webpage
- **JSON mode**: 4 additional credits per webpage

To help control costs:

- Set `parsers: []` if PDF parsing isn’t required
- Use `proxy: "basic"` instead of `"enhanced"` when possible, or set it to `"auto"`
- Limit the number of search results with the `limit` parameter

## Advanced Scraping Options

For more details about the scraping options, refer to the [Scrape Feature documentation](https://docs.firecrawl.dev/features/scrape). Everything except for the FIRE-1 Agent and Change-Tracking features are supported by this Search endpoint.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.