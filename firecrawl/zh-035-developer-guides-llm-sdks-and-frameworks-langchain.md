---
title: LangChain - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/llm-sdks-and-frameworks/langchain
source: sitemap
fetched_at: 2026-03-23T07:34:07.297582-03:00
rendered_js: false
word_count: 257
summary: 本指南介绍了如何将 Firecrawl 集成到 LangChain 工作流中，以实现网页内容的自动抓取、数据处理及结构化信息提取。
tags:
    - firecrawl
    - langchain
    - web-scraping
    - llm-integration
    - data-extraction
    - ai-application
category: tutorial
---

将 Firecrawl 与 LangChain 集成，构建由网页数据驱动的 AI 应用。

## 安装与设置

```
npm install @langchain/openai @mendable/firecrawl-js
```

创建 `.env` 文件：

```
FIRECRAWL_API_KEY=your_firecrawl_key
OPENAI_API_KEY=your_openai_key
```

> **注意：** 如果使用 Node 版本低于 20，请安装 `dotenv`，并在代码中添加 `import 'dotenv/config'`。

## 抓取 + 对话

本示例展示一个简单的工作流：抓取网站，并使用 LangChain 处理抓取到的内容。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { HumanMessage } from '@langchain/core/messages';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const chat = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
});

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const response = await chat.invoke([
    new HumanMessage(`Summarize: ${scrapeResult.markdown}`)
]);

console.log('Summary:', response.content);
```

## Chains

本示例演示如何构建一个 LangChain 链，用于处理和分析抓取到的内容。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { ChatPromptTemplate } from '@langchain/core/prompts';
import { StringOutputParser } from '@langchain/core/output_parsers';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const model = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
});

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

// 创建处理链
const prompt = ChatPromptTemplate.fromMessages([
    ['system', '你是分析公司网站的专家。'],
    ['user', '从以下内容中提取公司名称和主要产品:{content}']
]);

const chain = prompt.pipe(model).pipe(new StringOutputParser());

// 执行链
const result = await chain.invoke({
    content: scrapeResult.markdown
});

console.log('Chain result:', result);
```

此示例演示如何使用 LangChain 的工具调用功能，让模型自动决定何时抓取网站。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { DynamicStructuredTool } from '@langchain/core/tools';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 创建抓取工具
const scrapeWebsiteTool = new DynamicStructuredTool({
    name: 'scrape_website',
    description: '从任何网站 URL 抓取内容',
    schema: z.object({
        url: z.string().url().describe('要抓取的 URL')
    }),
    func: async ({ url }) => {
        console.log('正在抓取:', url);
        const result = await firecrawl.scrape(url, {
            formats: ['markdown']
        });
        console.log('抓取内容预览:', result.markdown?.substring(0, 200) + '...');
        return result.markdown || '未抓取到内容';
    }
});

const model = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
}).bindTools([scrapeWebsiteTool]);

const response = await model.invoke('什么是 Firecrawl?访问 firecrawl.dev 并告诉我相关信息。');

console.log('响应:', response.content);
console.log('工具调用:', response.tool_calls);
```

此示例演示如何使用 LangChain 的结构化输出功能来提取结构化数据。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('抓取的内容长度:', scrapeResult.markdown?.length);

const CompanyInfoSchema = z.object({
    name: z.string(),
    industry: z.string(),
    description: z.string(),
    products: z.array(z.string())
});

const model = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
}).withStructuredOutput(CompanyInfoSchema);

const companyInfo = await model.invoke([
    {
        role: 'system',
        content: '从网站内容中提取公司信息。'
    },
    {
        role: 'user',
        content: `提取数据: ${scrapeResult.markdown}`
    }
]);

console.log('已提取的公司信息:', companyInfo);
```

更多示例，请参阅 [LangChain 文档](https://js.langchain.com/docs)。