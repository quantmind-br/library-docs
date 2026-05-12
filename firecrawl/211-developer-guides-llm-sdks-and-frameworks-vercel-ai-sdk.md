---
title: Vercel AI SDK - Firecrawl Docs
url: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk
source: sitemap
fetched_at: 2026-03-23T07:31:29.373489-03:00
rendered_js: false
word_count: 164
summary: This document provides integration instructions and usage examples for using Firecrawl tools within Vercel AI SDK applications to perform web scraping, searching, crawling, and autonomous browsing.
tags:
    - firecrawl
    - vercel-ai-sdk
    - web-scraping
    - ai-agents
    - headless-browser
    - data-extraction
category: guide
---

Firecrawl tools for the Vercel AI SDK. Scrape, search, browse, and extract web data in your AI applications.

## Install

```
npm install firecrawl-aisdk ai
```

Set environment variables:

```
FIRECRAWL_API_KEY=fc-your-key       # https://firecrawl.dev
AI_GATEWAY_API_KEY=your-key         # https://vercel.com/ai-gateway
```

## Quick Start

The easiest way to get started. `FirecrawlTools()` gives you search, scrape, and browser tools with an auto-generated system prompt that guides the model on tool selection.

```
import { generateText, stepCountIs } from 'ai';
import { FirecrawlTools } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Search for Firecrawl, scrape the top result, and summarize what it does',
  tools: FirecrawlTools(),
  stopWhen: stepCountIs(5),
});
```

With custom options:

```
const tools = FirecrawlTools({
  apiKey: 'fc-custom-key',                // optional, defaults to env var
  search: { limit: 3, country: 'US' },    // default search options
  scrape: { onlyMainContent: true },       // default scrape options
  browser: {},                             // enable browser tool
});
```

Disable any tool by passing `false`:

```
const tools = FirecrawlTools({
  browser: false,   // search + scrape only
});
```

Every tool is **dual-purpose** - use it directly as a tool (reads `FIRECRAWL_API_KEY` from env) or call it as a factory for custom config:

```
import { scrape, search } from 'firecrawl-aisdk';

// Use directly - reads FIRECRAWL_API_KEY from env
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape, search },
  prompt: '...',
});

// Or call as factory for custom config
const customScrape = scrape({ apiKey: 'fc-custom-key' });
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape: customScrape },
  prompt: '...',
});
```

### Scrape

```
import { generateText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Scrape https://firecrawl.dev and summarize what it does',
  tools: { scrape },
});
```

### Search

```
import { generateText } from 'ai';
import { search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Search for Firecrawl and summarize what you find',
  tools: { search },
});
```

### Search + Scrape

```
import { generateText } from 'ai';
import { search, scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Search for Firecrawl, scrape the top result, and explain what it does',
  tools: { search, scrape },
});
```

### Map

```
import { generateText } from 'ai';
import { map } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Map https://docs.firecrawl.dev and list the main sections',
  tools: { map },
});
```

### Stream

```
import { streamText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const result = streamText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Scrape https://firecrawl.dev and explain what it does',
  tools: { scrape },
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

## Browser

The browser tool auto-creates a cloud session on first use and cleans up on process exit:

```
import { generateText, stepCountIs } from 'ai';
import { browser } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browser: browser() },
  stopWhen: stepCountIs(25),
  prompt: 'Go to https://news.ycombinator.com and get the top 3 stories.',
});
```

To get a live view URL (for watching the browser in real-time) or manually control the session lifecycle:

```
const browserTool = browser();
console.log('Live view:', await browserTool.start());

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browserTool },
  stopWhen: stepCountIs(25),
  prompt: 'Go to https://news.ycombinator.com and get the top 3 stories.',
});

await browserTool.close();
```

### Browser + Search

```
import { generateText, stepCountIs } from 'ai';
import { browser, search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browser: browser(), search },
  stopWhen: stepCountIs(25),
  prompt: 'Search for the top AI paper this week, browse it, and summarize the key findings.',
});
```

Crawl, batch scrape, extract, and agent return a job ID. Pair them with `poll` to get results:

### Crawl

```
import { generateText } from 'ai';
import { crawl, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Crawl https://docs.firecrawl.dev (limit 3 pages) and summarize',
  tools: { crawl, poll },
});
```

### Batch Scrape

```
import { generateText } from 'ai';
import { batchScrape, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Scrape https://firecrawl.dev and https://docs.firecrawl.dev, then compare',
  tools: { batchScrape, poll },
});
```

### Agent

Autonomous web data gathering - searches, navigates, and extracts data on its own.

```
import { generateText, stepCountIs } from 'ai';
import { agent, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Find the founders of Firecrawl, their roles, and their backgrounds',
  tools: { agent, poll },
  stopWhen: stepCountIs(10),
});
```

## All Exports

```
import {
  // Dual-purpose tools (use directly or call as factory)
  scrape,             // Scrape a single URL
  search,             // Search the web
  map,                // Discover URLs on a site
  crawl,              // Crawl multiple pages (async)
  batchScrape,        // Scrape multiple URLs (async)
  agent,              // Autonomous web agent (async)
  extract,            // Extract structured data (async)

  // Job management
  poll,               // Poll async jobs for results
  status,             // Check job status
  cancel,             // Cancel running jobs

  // Browser (factory-only)
  browser,            // browser({ firecrawlApiKey: '...' })

  // All-in-one bundle
  FirecrawlTools,     // FirecrawlTools({ apiKey, search, scrape, browser })

  // Helpers
  stepLogger,         // Token stats per tool call
  logStep,            // Simple one-liner logging
} from 'firecrawl-aisdk';
```