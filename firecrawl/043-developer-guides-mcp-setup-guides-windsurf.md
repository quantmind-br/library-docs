---
title: MCP Web Search & Scrape in Windsurf - Firecrawl Docs
url: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/windsurf
source: sitemap
fetched_at: 2026-03-23T07:39:40.234202-03:00
rendered_js: false
word_count: 71
summary: This document provides instructions on integrating the Firecrawl Model Context Protocol (MCP) server into the Windsurf environment to enable web scraping and search capabilities.
tags:
    - windsurf
    - firecrawl
    - mcp-server
    - web-scraping
    - ai-agents
    - configuration
category: configuration
---

Add web scraping and search capabilities to Windsurf with Firecrawl MCP.

## Quick Setup

### 1. Get Your API Key

Sign up at [firecrawl.dev/app](https://firecrawl.dev/app) and copy your API key.

### 2. Add to Windsurf

Add this to your `./codeium/windsurf/model_config.json`:

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

Replace `YOUR_API_KEY` with your actual Firecrawl API key.

### 3. Restart Windsurf

Done! Windsurf can now search and scrape the web.

## Quick Demo

Try these in Windsurf: **Search:**

```
Search for the latest Tailwind CSS features
```

**Scrape:**

```
Scrape firecrawl.dev and explain what it does
```

**Get docs:**

```
Find and scrape the Supabase authentication documentation
```

Windsurf’s AI agents will automatically use Firecrawl tools.