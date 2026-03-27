---
title: 抓取 Wikipedia - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/common-sites/wikipedia
source: sitemap
fetched_at: 2026-03-23T07:34:16.72263-03:00
rendered_js: false
word_count: 36
summary: 本指南介绍了如何使用 Firecrawl SDK 从 Wikipedia 获取和结构化提取数据，包括单页抓取、批量爬取、搜索以及内容映射功能。
tags:
    - web-scraping
    - wikipedia-data
    - firecrawl-sdk
    - data-extraction
    - structured-data
    - ai-applications
category: guide
---

了解如何高效抓取 Wikipedia，用于研究、知识抽取与构建 AI 应用。

## 安装与配置

```
npm install @mendable/firecrawl-js zod
```

## 使用场景

- 研究流程自动化与事实核查
- 构建知识图谱
- 多语言内容提取
- 教育内容聚合
- 实体信息抽取

## 使用 JSON 模式进行抓取

使用 Zod 模式从 Wikipedia 条目中提取结构化数据。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://en.wikipedia.org/wiki/JavaScript', {
    formats: [{
        type: 'json',
        schema: z.object({
            name: z.string(),
            creator: z.string(),
            firstAppeared: z.string(),
            typingDiscipline: z.string(),
            website: z.string()
        })
    }]
});

console.log(result.json);
```

## 搜索

在维基百科上搜索文章。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('quantum computing site:en.wikipedia.org', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## 抓取

抓取单个维基百科页面。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://en.wikipedia.org/wiki/Artificial_intelligence', {
    formats: ['markdown'], // 例如 html、links 等
    onlyMainContent: true
});

console.log(result);
```

## Map

在 Wikipedia 门户或分类下发现所有可用的 URL。注意：Map 只返回 URL，不包含页面内容。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://en.wikipedia.org/wiki/Portal:Computer_science');

console.log(mapResult.links);
// 返回 URL 数组,不包含内容
```

## Crawl

从维基百科的文档或分类中爬取多个页面。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://en.wikipedia.org/wiki/Portal:Artificial_intelligence', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

## 批量抓取

一次性抓取多个 Wikipedia 链接。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 等待完成
const job = await firecrawl.batchScrape([
    'https://en.wikipedia.org/wiki/Machine_learning',
    'https://en.wikipedia.org/wiki/Artificial_intelligence',
    'https://en.wikipedia.org/wiki/Deep_learning'],
    {
        options: {
            formats: ['markdown']
        },
        pollInterval: 2,
        timeout: 120
    }
);


console.log(job.status, job.completed, job.total);

console.log(job);
```