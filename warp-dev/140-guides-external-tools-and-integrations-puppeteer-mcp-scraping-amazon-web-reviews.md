---
title: 'Puppeteer MCP: Scraping Web Reviews | Guides | Warp'
url: https://docs.warp.dev/guides/external-tools-and-integrations/puppeteer-mcp-scraping-amazon-web-reviews
source: sitemap
fetched_at: 2026-04-29T15:06:50.99499012-03:00
rendered_js: false
word_count: 328
summary: This tutorial explains how to integrate and configure the Puppeteer MCP server within the Warp terminal to automate browser tasks, web scraping, and data analysis using AI-driven prompts.
tags:
    - warp-terminal
    - puppeteer
    - mcp-server
    - browser-automation
    - web-scraping
    - ai-agents
category: tutorial
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
> [!info]
> This tutorial demonstrates how to configure and use the **Puppeteer MCP server** inside Warp to scrape Amazon web reviews.

## Overview

**Puppeteer MCP** integrates Warp's agents with the browser, enabling navigation, form filling, screenshotting, and scraping content. Once configured, Warp issues Puppeteer commands directly from prompts for full browser automation without manual scripting.

You'll learn how to:
- Set up the Puppeteer MCP server.
- Use Warp's voice input and AI to describe automation tasks.
- Execute browser workflows hands-free.
- Capture, scrape, and analyze web data programmatically.

## Configure the Puppeteer MCP Server

1. Open the **MCP Panel**: press **Cmd+Shift+P** (Mac) or **Ctrl+Shift+P** (Windows/Linux), then search for `MCP`.
2. Click **Add** and paste the JSON configuration:

```json
{
  "puppeteer": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-puppeteer"
    ],
    "env": {},
    "working_directory": null
  }
}
```

3. Save. Available endpoints include:

| Endpoint | Action |
|---|---|
| `puppeteer.navigate` | Open a URL |
| `puppeteer.fill` | Fill form fields |
| `puppeteer.screenshot` | Capture a page |
| `puppeteer.evaluate` | Run JavaScript |

## Use Voice Input to Trigger Automation

Enable voice input via the microphone icon, then speak naturally:

```
Can you go to Amazon search for "white t-shirt women?"
Scrape the results so the titles, prices, and links are extracted.
Then open each product link and summarize the product reviews.
Finally, give me a recommendation for which shirt to buy based on pricing and review quality.
```

## How It Works

Puppeteer performs these steps autonomously:

- Navigates to Amazon and fills the search bar.
- Scrapes product results — titles, prices, and links.
- Clicks into each product and extracts review data via JavaScript selectors.
- Takes screenshots for reference.

Puppeteer runs headless or in visible browser mode — no mouse or keyboard interaction required.

## Results Example

| Product | Price | Rating | Summary |
|---|---|---|---|
| Cozy T-Shirt | $8 | 4.5 stars | Good fit, soft fabric |

> [!tip]
> Puppeteer MCP lets Warp act like your hands in the browser — navigating, scraping, and summarizing while you focus on analysis.

## Other Use Cases

- **Product research** — Compare reviews or specs across sites.
- **Competitive analysis** — Scrape pricing or product data.
- **Web testing** — Automate login, checkout, or other user flows.
- **Periodic scraping** — Scheduled data or screenshot capture.
