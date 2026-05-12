---
title: MCP Web Search & Scrape in Claude Code - Firecrawl Docs
url: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/claude-code
source: sitemap
fetched_at: 2026-03-23T07:29:28.243346-03:00
rendered_js: false
word_count: 89
summary: This document provides instructions for integrating the Firecrawl MCP server with Claude Code to enable automated web searching and page scraping capabilities.
tags:
    - web-scraping
    - claude-code
    - mcp-server
    - firecrawl
    - tool-integration
    - automation
category: configuration
---

Add web scraping and search capabilities to Claude Code with Firecrawl MCP.

## Quick Setup

### 1. Get Your API Key

Sign up at [firecrawl.dev/app](https://firecrawl.dev/app) and copy your API key.

### 2. Add Firecrawl MCP Server

**Option A: Remote hosted URL (recommended)**

```
claude mcp add firecrawl --url https://mcp.firecrawl.dev/your-api-key/v2/mcp
```

**Option B: Local (npx)**

```
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

Replace `your-api-key` with your actual Firecrawl API key. Done! You can now search and scrape the web from Claude Code.

## Quick Demo

Try these in Claude Code: **Search the web:**

```
Search for the latest Next.js 15 features
```

**Scrape a page:**

```
Scrape firecrawl.dev and tell me what it does
```

**Get documentation:**

```
Find and scrape the Stripe API docs for payment intents
```

Claude will automatically use Firecrawl’s search and scrape tools to get the information.