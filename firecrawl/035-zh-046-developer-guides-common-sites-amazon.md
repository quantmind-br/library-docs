---
title: 抓取 Amazon - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/common-sites/amazon
source: sitemap
fetched_at: 2026-03-23T07:34:21.223274-03:00
rendered_js: false
word_count: 40
summary: This document provides a technical guide on using the Firecrawl SDK to extract, search, and crawl data from Amazon product pages efficiently. It demonstrates how to implement structured data extraction using Zod schemas alongside various scraping and mapping methods.
tags:
    - firecrawl
    - web-scraping
    - amazon-data
    - zod-schema
    - data-extraction
    - structured-data
category: tutorial
---

## 配置

```
npm install @mendable/firecrawl-js zod
```

## 概览

在抓取 Amazon 时，你通常会：

- 提取商品信息（标题、价格、库存情况）
- 获取客户评价和评分
- 监控价格变动
- 以编程方式搜索商品
- 跟踪竞争对手的商品列表

## 使用 JSON 模式进行抓取

使用 Zod 架构提取结构化的产品数据。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// 定义 Zod schema
const ProductSchema = z.object({
    title: z.string(),
    price: z.string(),
    rating: z.number(),
    availability: z.string(),
    features: z.array(z.string())
});

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.amazon.com/dp/B0DZZWMB2L', {
    formats: [{
        type: 'json',
        schema: z.toJSONSchema(ProductSchema)
    }],
});

// 使用 Zod 解析和验证
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ProductSchema.parse(jsonData);

console.log('✅ 已验证的产品数据:');
console.log(validated);
```

## 搜索

在 Amazon 上搜索产品。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('gaming laptop site:amazon.com', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }（新闻）, { type: 'images' }（图片）
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## 抓取

抓取单个 Amazon 商品详情页。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L', {
    formats: ['markdown'], // 即 html、links 等
    onlyMainContent: true
});

console.log(result);
```

## Map

在 Amazon 商品或类目页面上发现所有可用的 URL。注意：Map 仅返回 URL，不包含页面内容。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics');

console.log(mapResult.links);
// 返回 URL 数组,不包含页面内容
```

## 爬取

从 Amazon 商品分类或搜索结果中爬取多个页面。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://www.amazon.com/s?k=mechanical+keyboards', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

## 批量抓取

同时抓取多个 Amazon 商品页面的 URL。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 等待完成
const job = await firecrawl.batchScrape([
    'https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L',
    'https://www.amazon.com/Razer-Blade-Gaming-Laptop-Lightweight/dp/B0FP47DNFQ',
    'https://www.amazon.com/HP-2025-Omen-Gaming-Laptop/dp/B0FL4RMGSH'],
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