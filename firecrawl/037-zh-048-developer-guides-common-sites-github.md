---
title: 抓取 GitHub - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/common-sites/github
source: sitemap
fetched_at: 2026-03-23T07:32:33.189918-03:00
rendered_js: false
word_count: 38
summary: This document provides a technical guide on using the Firecrawl SDK to extract, search, and crawl data from GitHub repositories, issues, and documentation using structured JSON schemas or markdown formats.
tags:
    - firecrawl
    - web-scraping
    - github-data
    - data-extraction
    - sdk-integration
    - structured-data
category: tutorial
---

了解如何使用 Firecrawl 的核心功能抓取 GitHub 的仓库、议题（issues）和文档。

## 设置

```
npm install @mendable/firecrawl-js zod
```

## 使用 JSON 模式抓取

通过 Zod schema 从代码仓库中提取结构化数据。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://github.com/firecrawl/firecrawl', {
    formats: [{
        type: 'json',
        schema: z.object({
            name: z.string(),
            description: z.string(),
            stars: z.number(),
            forks: z.number(),
            language: z.string(),
            topics: z.array(z.string())
        })
    }]
});

console.log(result.json);
```

## 搜索

搜索 GitHub 上的仓库、issue 或文档。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('machine learning site:github.com', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## 抓取

抓取单个 GitHub 页面（仓库、issue 或文件）。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://github.com/firecrawl/firecrawl', {
    formats: ['markdown'] // 例如 html、links 等
});

console.log(result);
```

## 映射

发现仓库或文档站点中所有可用的 URL。请注意：Map 仅返回 URL，不包含页面内容。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://github.com/vercel/next.js/tree/canary/docs');

console.log(mapResult.links);
// 返回不含内容的 URL 数组
```

## Crawl

从仓库或文档中抓取多个页面。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://github.com/facebook/react/wiki', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

## 批量抓取

同时抓取多个 GitHub 链接。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 等待完成
const job = await firecrawl.batchScrape([
    'https://github.com/vercel/next.js',
    'https://github.com/facebook/react',
    'https://github.com/microsoft/typescript'],
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

## 使用 JSON 模式批量爬取

一次性从多个仓库中抽取结构化数据。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 等待完成
const job = await firecrawl.batchScrape([
    'https://github.com/vercel/next.js',
    'https://github.com/facebook/react'],
    {
        options: {
            formats: [{
                type: 'json',
                schema: z.object({
                    name: z.string(),
                    description: z.string(),
                    stars: z.number(),
                    language: z.string()
                })
            }]
        },
        pollInterval: 2,
        timeout: 120
    }
);


console.log(job.status, job.completed, job.total);

console.log(job);
```