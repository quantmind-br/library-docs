---
title: Agent Development Kit (ADK) - Firecrawl Docs
url: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/google-adk
source: sitemap
fetched_at: 2026-03-23T07:39:55.788806-03:00
rendered_js: false
word_count: 344
summary: This document explains how to integrate Firecrawl with Google's Agent Development Kit using the Model Context Protocol to provide AI agents with web crawling and scraping capabilities.
tags:
    - firecrawl
    - google-adk
    - web-scraping
    - mcp
    - ai-agents
    - data-extraction
category: guide
---

Integrate Firecrawl with Google’s Agent Development Kit (ADK) to build powerful AI agents with web scraping capabilities through the Model Context Protocol (MCP).

## Overview

Firecrawl provides an MCP server that seamlessly integrates with Google’s ADK, enabling your agents to efficiently scrape, crawl, and extract structured data from any website. The integration supports both cloud-based and self-hosted Firecrawl instances with streamable HTTP for optimal performance.

## Features

- Efficient web scraping, crawling, and content discovery from any website
- Advanced search capabilities and intelligent content extraction
- Deep research and high-volume batch scraping
- Flexible deployment (cloud-based or self-hosted)
- Optimized for modern web environments with streamable HTTP support

## Prerequisites

- Obtain an API key for Firecrawl from [firecrawl.dev](https://firecrawl.dev)
- Install Google ADK

## Setup

ToolNameDescriptionScrape Tool`firecrawl_scrape`Scrape content from a single URL with advanced optionsBatch Scrape Tool`firecrawl_batch_scrape`Scrape multiple URLs efficiently with built-in rate limiting and parallel processingCheck Batch Status`firecrawl_check_batch_status`Check the status of a batch operationMap Tool`firecrawl_map`Map a website to discover all indexed URLs on the siteSearch Tool`firecrawl_search`Search the web and optionally extract content from search resultsCrawl Tool`firecrawl_crawl`Start an asynchronous crawl with advanced optionsCheck Crawl Status`firecrawl_check_crawl_status`Check the status of a crawl jobExtract Tool`firecrawl_extract`Extract structured information from web pages using LLM capabilities

## Configuration

### Required Configuration

**FIRECRAWL\_API\_KEY**: Your Firecrawl API key

- Required when using cloud API (default)
- Optional when using self-hosted instance with FIRECRAWL\_API\_URL

### Optional Configuration

**Firecrawl API URL (for self-hosted instances)**:

- `FIRECRAWL_API_URL`: Custom API endpoint
- Example: `https://firecrawl.your-domain.com`
- If not provided, the cloud API will be used

**Retry configuration**:

- `FIRECRAWL_RETRY_MAX_ATTEMPTS`: Maximum retry attempts (default: 3)
- `FIRECRAWL_RETRY_INITIAL_DELAY`: Initial delay in milliseconds (default: 1000)
- `FIRECRAWL_RETRY_MAX_DELAY`: Maximum delay in milliseconds (default: 10000)
- `FIRECRAWL_RETRY_BACKOFF_FACTOR`: Exponential backoff multiplier (default: 2)

**Credit usage monitoring**:

- `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: Warning threshold (default: 1000)
- `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: Critical threshold (default: 100)

## Example: Web Research Agent

```
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

FIRECRAWL_API_KEY = "YOUR-API-KEY"

# Create a research agent
research_agent = Agent(
    model="gemini-2.5-pro",
    name="research_agent",
    description='An AI agent that researches topics by scraping and analyzing web content',
    instruction='''You are a research assistant. When given a topic or question:
    1. Use the search tool to find relevant websites
    2. Scrape the most relevant pages for detailed information
    3. Extract structured data when needed
    4. Provide comprehensive, well-sourced answers''',
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=f"https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp",
            ),
        )
    ],
)

# Use the agent
response = research_agent.run("What are the latest features in Python 3.13?")
print(response)
```

## Best Practices

1. **Use the right tool for the job**:
   
   - `firecrawl_search` when you need to find relevant pages first
   - `firecrawl_scrape` for single pages
   - `firecrawl_batch_scrape` for multiple known URLs
   - `firecrawl_crawl` for discovering and scraping entire sites
2. **Monitor your usage**: Configure credit thresholds to avoid unexpected usage
3. **Handle errors gracefully**: Configure retry settings based on your use case
4. **Optimize performance**: Use batch operations when scraping multiple URLs

* * *