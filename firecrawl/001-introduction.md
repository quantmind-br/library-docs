---
title: Quickstart | Firecrawl
url: https://docs.firecrawl.dev/introduction
source: sitemap
fetched_at: 2026-03-23T07:30:24.896172-03:00
rendered_js: false
word_count: 339
summary: This document provides an introduction to Firecrawl, a web scraping and crawling service designed to convert website content into structured, LLM-ready data for AI agents and applications.
tags:
    - web-scraping
    - ai-agents
    - data-extraction
    - markdown-conversion
    - browser-sandbox
    - api-integration
category: guide
---

## Scrape your first website

Turn any website into clean, LLM-ready data with a single API call.

### Use Firecrawl with AI agents (recommended)

The Firecrawl skill is the fastest way for agents to discover and use Firecrawl. Without it, your agent will not know Firecrawl is available.

```
npx -y firecrawl-cli@latest init --all --browser
```

Or use the [MCP Server](https://docs.firecrawl.dev/mcp-server) to connect Firecrawl directly to Claude, Cursor, Windsurf, VS Code, and other AI tools.

### Make your first request

Copy the code below, replace `fc-YOUR-API-KEY` with your API key, and run it:

Example response

```
{
  "success": true,
  "data": {
    "markdown": "# Example Domain\n\nThis domain is for use in illustrative examples...",
    "metadata": {
      "title": "Example Domain",
      "sourceURL": "https://example.com"
    }
  }
}
```

* * *

## What can Firecrawl do?

### Why Firecrawl?

- **LLM-ready output**: Get clean markdown, structured JSON, screenshots, and more
- **Handles the hard stuff**: Proxies, anti-bot, JavaScript rendering, and dynamic content
- **Reliable**: Built for production with high uptime and consistent results
- **Fast**: Get results in seconds, optimized for high-throughput
- **Browser Sandbox**: Fully managed browser environments for agents, zero config, scales to any size
- **MCP Server**: Connect Firecrawl to any AI tool via the [Model Context Protocol](https://docs.firecrawl.dev/mcp-server)

* * *

## Scraping

Scrape any URL and get its content in markdown, HTML, or other formats. See the [Scrape feature docs](https://docs.firecrawl.dev/features/scrape) for all options.

Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

## Search

Firecrawl’s search API allows you to perform web searches and optionally scrape the search results in one operation.

- Choose specific output formats (markdown, HTML, links, screenshots)
- Choose specific sources (web, news, images)
- Search the web with customizable parameters (location, etc.)

For details, see the [Search Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/search).

Response

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

## Agent

Firecrawl’s Agent is an autonomous web data gathering tool. Just describe what data you need, and it will search, navigate, and extract it from anywhere on the web. See the [Agent feature docs](https://docs.firecrawl.dev/features/agent) for all options.

Example response

```
{
  "success": true,
  "data": {
    "result": "Notion offers the following pricing plans:\n\n1. **Free** - $0/month - For individuals...\n2. **Plus** - $10/seat/month - For small teams...\n3. **Business** - $18/seat/month - For companies...\n4. **Enterprise** - Custom pricing - For large organizations...",
    "sources": [
      "https://www.notion.so/pricing"
    ]
  }
}
```

## Browser

Firecrawl Browser Sandbox gives your agents a secure browser environment to interact with the web. Fill out forms, click buttons, authenticate, and more. No local setup or Chromium installs needed. See the [Browser feature docs](https://docs.firecrawl.dev/features/browser) for complete documentation.

Example response

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-...",
  "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-...?interactive=true"
}
```

* * *

## Resources