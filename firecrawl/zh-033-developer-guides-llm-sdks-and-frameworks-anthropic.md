---
title: Anthropic - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/llm-sdks-and-frameworks/anthropic
source: sitemap
fetched_at: 2026-03-23T07:33:55.438175-03:00
rendered_js: false
word_count: 227
summary: 本指南介绍了如何集成 Firecrawl 与 Anthropic Claude 模型，以实现网页内容抓取、自动摘要、工具调用及结构化数据提取等 AI 功能。
tags:
    - firecrawl
    - claude
    - web-scraping
    - ai-automation
    - data-extraction
    - tool-calling
category: guide
---

将 Firecrawl 与 Claude 集成，构建由网页数据驱动的 AI 应用。

## 安装与配置

```
npm install @mendable/firecrawl-js @anthropic-ai/sdk zod zod-to-json-schema
```

创建“.env”文件：

```
FIRECRAWL_API_KEY=your_firecrawl_key
ANTHROPIC_API_KEY=your_anthropic_key
```

> **注意：** 如果使用 Node 版本低于 20，请安装 `dotenv`，并在代码中添加 `import 'dotenv/config'`。

## 抓取 + 摘要

本示例演示了一个简单的工作流：抓取网站，并使用 Claude 对内容进行摘要。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import Anthropic from '@anthropic-ai/sdk';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const message = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    messages: [
        { role: 'user', content: `Summarize in 100 words: ${scrapeResult.markdown}` }
    ]
});

console.log('Response:', message);
```

本示例演示如何使用 Claude 的工具调用功能，让模型根据用户请求自动决定何时抓取网站内容。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { Anthropic } from '@anthropic-ai/sdk';
import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

const firecrawl = new FirecrawlApp({
    apiKey: process.env.FIRECRAWL_API_KEY
});

const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY
});

const ScrapeArgsSchema = z.object({
    url: z.string()
});

console.log("Sending user message to Claude and requesting tool use if necessary...");
const response = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    tools: [{
        name: 'scrape_website',
        description: 'Scrape and extract markdown content from a website URL',
        input_schema: zodToJsonSchema(ScrapeArgsSchema, 'ScrapeArgsSchema') as any
    }],
    messages: [{
        role: 'user',
        content: 'What is Firecrawl? Check firecrawl.dev'
    }]
});

const toolUse = response.content.find(block => block.type === 'tool_use');

if (toolUse && toolUse.type === 'tool_use') {
    const input = toolUse.input as { url: string };
    console.log(`Calling tool: ${toolUse.name} | URL: ${input.url}`);

    const result = await firecrawl.scrape(input.url, {
        formats: ['markdown']
    });

    console.log(`抓取内容预览: ${result.markdown?.substring(0, 300)}...`);
    // Continue with the conversation or process the scraped content as needed
}
```

此示例展示如何使用 Claude 从已抓取的网站内容中提取结构化数据。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import Anthropic from '@anthropic-ai/sdk';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const CompanyInfoSchema = z.object({
    name: z.string(),
    industry: z.string().optional(),
    description: z.string().optional()
});

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown'],
    onlyMainContent: true
});

const prompt = `从此网站内容中提取公司信息。

仅输出此精确格式的有效 JSON(无 markdown,无说明):

{
  "name": "Company Name",
  "industry": "Industry",
  "description": "One sentence description"
}

网站内容:
${scrapeResult.markdown}`;

const message = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    messages: [
        { role: 'user', content: prompt },
        { role: 'assistant', content: '{' }
    ]
});

const textBlock = message.content.find(block => block.type === 'text');

if (textBlock && textBlock.type === 'text') {
    const jsonText = '{' + textBlock.text;
    const companyInfo = CompanyInfoSchema.parse(JSON.parse(jsonText));

    console.log(companyInfo);
}
```

更多示例请参见 [Claude 文档](https://docs.anthropic.com/claude/docs)。