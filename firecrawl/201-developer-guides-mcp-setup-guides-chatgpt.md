---
title: MCP Web Search & Scrape in ChatGPT - Firecrawl Docs
url: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/chatgpt
source: sitemap
fetched_at: 2026-03-23T07:39:37.590263-03:00
rendered_js: false
word_count: 285
summary: This document provides step-by-step instructions for integrating the Firecrawl MCP server with ChatGPT to enable web scraping, crawling, and search capabilities.
tags:
    - firecrawl
    - mcp-server
    - web-scraping
    - chatgpt-integration
    - api-setup
    - developer-mode
category: guide
---

Add web scraping and search capabilities to ChatGPT with Firecrawl MCP.

## Quick Setup

### 1. Get Your API Key

Sign up at [firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys) and copy your API key.

### 2. Enable Developer Mode

Open ChatGPT settings by clicking your username in the bottom left corner, or navigate directly to [chatgpt.com/#settings](https://chatgpt.com/#settings). In the settings modal, scroll to the bottom and select **Advanced Settings**. Toggle **Developer mode** to ON.

### 3. Create the Connector

With Developer mode enabled, go to the **Apps & Connectors** tab in the same settings modal. Click the **Create** button in the top right corner.

Fill in the connector details:

- **Name:** `Firecrawl MCP`
- **Description:** `Web scraping, crawling, search, and content extraction` (optional)
- **MCP Server URL:** `https://mcp.firecrawl.dev/YOUR_API_KEY_HERE/v2/mcp`
- **Authentication:** `None`

Replace `YOUR_API_KEY_HERE` in the URL with your actual [Firecrawl API key](https://www.firecrawl.dev/app/api-keys).

Check the **“I understand and want to continue”** checkbox, then click **Create**.

### 4. Verify Setup

Go back to the main ChatGPT interface. You should see **Developer mode** displayed, indicating that MCP connectors are active. If you do not see Developer mode, reload the page. If it still does not appear, open settings again and verify that Developer mode is toggled ON under Advanced Settings.

### 5. Access Firecrawl Tools

To use Firecrawl in a conversation, click the **+** button in the chat input, then select **More** and choose **Firecrawl MCP**.

## Quick Demo

With Firecrawl MCP selected, try these prompts: **Search:**

```
Search for the latest React Server Components updates
```

**Scrape:**

```
Scrape firecrawl.dev and tell me what it does
```

**Get docs:**

```
Scrape the Vercel documentation for edge functions and summarize it
```

When ChatGPT uses the Firecrawl MCP tools, you will see a confirmation prompt asking for your approval.

You can check **“Remember for this conversation”** to avoid repeated confirmations during the same chat session. This security measure is implemented by OpenAI to ensure MCP tools do not perform unintended actions. Once confirmed, ChatGPT will execute the request and return the results.