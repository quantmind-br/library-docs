---
title: MCP Web Search & Scrape in Factory AI - Firecrawl Docs
url: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/factory-ai
source: sitemap
fetched_at: 2026-03-23T07:39:43.387021-03:00
rendered_js: false
word_count: 106
summary: This document provides instructions on integrating the Firecrawl Model Context Protocol (MCP) server into Factory AI to enable web scraping and search functionality.
tags:
    - factory-ai
    - firecrawl
    - web-scraping
    - mcp-server
    - ai-integration
    - automation
category: guide
---

Add web scraping and search capabilities to Factory AI with Firecrawl MCP.

## Quick Setup

### 1. Get Your API Key

Sign up at [firecrawl.dev/app](https://firecrawl.dev/app) and copy your API key.

### 2. Install Factory AI CLI

Install the [Factory AI CLI](https://docs.factory.ai/cli/getting-started/quickstart) if you haven’t already: **macOS/Linux:**

```
curl -fsSL https://app.factory.ai/cli | sh
```

**Windows:**

```
iwr https://app.factory.ai/cli/install.ps1 -useb | iex
```

### 3. Add Firecrawl MCP Server

In the Factory droid CLI, add Firecrawl using the `/mcp add` command:

```
/mcp add firecrawl "npx -y firecrawl-mcp" -e FIRECRAWL_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual Firecrawl API key.

### 4. Done!

The Firecrawl tools are now available in your Factory AI session!

## Quick Demo

Try these in Factory AI: **Search the web:**

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

Factory will automatically use Firecrawl’s search and scrape tools to get the information.