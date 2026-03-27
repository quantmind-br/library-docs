---
title: Gemini - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/llm-sdks-and-frameworks/gemini
source: sitemap
fetched_at: 2026-03-23T07:34:09.337204-03:00
rendered_js: false
word_count: 198
summary: This document provides a guide on integrating Firecrawl with Google Gemini to scrape web data and process it using AI for summarization, conversational analysis, and structured data extraction.
tags:
    - web-scraping
    - ai-integration
    - firecrawl
    - google-gemini
    - data-extraction
    - llm-workflows
category: tutorial
---

将 Firecrawl 与 Google 的 Gemini 集成，以构建由网页数据驱动的 AI 应用。

## 安装与配置

```
npm install @mendable/firecrawl-js @google/genai
```

创建“.env”文件：

```
FIRECRAWL_API_KEY=your_firecrawl_key
GEMINI_API_KEY=your_gemini_key
```

> **注意：** 如果使用 Node 版本低于 20，请安装 `dotenv`，并在代码中添加 `import 'dotenv/config'`。

## 抓取 + 摘要

此示例演示了一个简单的工作流：抓取网站并使用 Gemini 对内容生成摘要。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: `Summarize: ${scrapeResult.markdown}`,
});

console.log('Summary:', response.text);
```

## 内容分析

此示例展示了如何使用 Gemini 的多轮对话功能来分析网页内容。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://news.ycombinator.com/', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const chat = ai.chats.create({
    model: 'gemini-2.5-flash'
});

// 获取 Hacker News 上的前 3 条热门内容
const result1 = await chat.sendMessage({
    message: `Based on this website content from Hacker News, what are the top 3 stories right now?\n\n${scrapeResult.markdown}`
});
console.log('Top 3 Stories:', result1.text);

// 获取 Hacker News 上的第 4 和第 5 条热门内容
const result2 = await chat.sendMessage({
    message: `Now, what are the 4th and 5th top stories on Hacker News from the same content?`
});
console.log('4th and 5th Stories:', result2.text);
```

此示例演示了如何使用 Gemini 的 JSON 模式，从已抓取的网站内容中提取结构化数据。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI, Type } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('抓取的内容长度:', scrapeResult.markdown?.length);

const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: `提取公司信息: ${scrapeResult.markdown}`,
    config: {
        responseMimeType: 'application/json',
        responseSchema: {
            type: Type.OBJECT,
            properties: {
                name: { type: Type.STRING },
                industry: { type: Type.STRING },
                description: { type: Type.STRING },
                products: {
                    type: Type.ARRAY,
                    items: { type: Type.STRING }
                }
            },
            propertyOrdering: ['name', 'industry', 'description', 'products']
        }
    }
});

console.log('已提取的公司信息:', response?.text);
```

更多示例请参阅 [Gemini 文档](https://ai.google.dev/docs)。