---
title: Vercel AI SDK - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk
source: sitemap
fetched_at: 2026-03-23T07:31:13.882519-03:00
rendered_js: false
word_count: 48
summary: This document provides a technical guide for integrating Firecrawl with the Vercel AI SDK, enabling AI models to perform web scraping, searching, crawling, and data extraction.
tags:
    - vercel-ai-sdk
    - firecrawl
    - web-scraping
    - ai-agents
    - javascript
    - typescript
    - data-extraction
category: guide
---

适用于 Vercel AI SDK 的 Firecrawl 工具，为 AI 应用提供网页抓取、搜索、浏览和数据提取能力。

## 安装

```
npm install firecrawl-aisdk ai
```

设置环境变量：

```
FIRECRAWL_API_KEY=fc-your-key       # https://firecrawl.dev
AI_GATEWAY_API_KEY=your-key         # https://vercel.com/ai-gateway
```

## 快速开始

最简单的上手方式。`FirecrawlTools()` 提供搜索、抓取和浏览工具，并自动生成系统提示词，引导模型选择合适的工具。

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

使用自定义配置：

```
const tools = FirecrawlTools({
  apiKey: 'fc-custom-key',                // 可选，默认使用环境变量
  search: { limit: 3, country: 'US' },    // 默认搜索选项
  scrape: { onlyMainContent: true },       // 默认抓取选项
  browser: {},                             // 启用浏览器工具
});
```

将其设置为 `false` 即可禁用某个工具：

```
const tools = FirecrawlTools({
  browser: false,   // 仅启用搜索 + 抓取
});
```

每个工具都**兼具两种用法**——既可以直接作为工具使用（从环境变量中读取 `FIRECRAWL_API_KEY`），也可以作为工厂函数调用，用于自定义配置：

```
import { scrape, search } from 'firecrawl-aisdk';

// 直接使用 - 从环境变量读取 FIRECRAWL_API_KEY
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape, search },
  prompt: '...',
});

// 或作为工厂函数调用以自定义配置
const customScrape = scrape({ apiKey: 'fc-custom-key' });
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape: customScrape },
  prompt: '...',
});
```

### 爬取

```
import { generateText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: '抓取 https://firecrawl.dev 并总结它的作用',
  tools: { scrape },
});
```

### 搜索

```
import { generateText } from 'ai';
import { search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: '搜索 Firecrawl 并总结你的发现',
  tools: { search },
});
```

### 搜索 + 抓取

```
import { generateText } from 'ai';
import { search, scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: '搜索 Firecrawl,抓取首个结果,并说明其功能',
  tools: { search, scrape },
});
```

### 映射

```
import { generateText } from 'ai';
import { map } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Map https://docs.firecrawl.dev and list the main sections',
  tools: { map },
});
```

### 流式

```
import { streamText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const result = streamText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: '抓取 https://firecrawl.dev 并解释它的功能',
  tools: { scrape },
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

## Browser

`browser` 工具在首次使用时会自动创建一个云端会话，并在进程退出时自动清理：

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

要获取用于实时查看浏览器的实时预览 URL，或手动控制会话生命周期：

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

### 浏览器 + 搜索

```
import { generateText, stepCountIs } from 'ai';
import { browser, search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browser: browser(), search },
  stopWhen: stepCountIs(25),
  prompt: '搜索本周顶级 AI 论文,浏览并总结其核心发现。',
});
```

Crawl、batch scrape、extract 和 agent 会返回一个任务 ID。配合 `poll` 获取结果：

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

### 批量抓取

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

自动化网页数据采集——可自行搜索、浏览并提取数据。

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

## 全部导出

```
import {
  // 双用途工具（可直接使用或作为工厂调用）
  scrape,             // 抓取单个 URL
  search,             // 搜索网络
  map,                // 发现站点上的 URL
  crawl,              // 爬取多个页面（异步）
  batchScrape,        // 批量抓取多个 URL（异步）
  agent,              // 自主网络代理（异步）
  extract,            // 提取结构化数据（异步）

  // 任务管理
  poll,               // 轮询异步任务以获取结果
  status,             // 检查任务状态
  cancel,             // 取消正在运行的任务

  // 浏览器（仅工厂模式）
  browser,            // browser({ firecrawlApiKey: '...' })

  // 一体化套件
  FirecrawlTools,     // FirecrawlTools({ apiKey, search, scrape, browser })

  // 辅助工具
  stepLogger,         // 每次工具调用的 Token 统计
  logStep,            // 简单的单行日志记录
} from 'firecrawl-aisdk';
```