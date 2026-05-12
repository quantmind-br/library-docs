---
title: 抓取 Etsy - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/common-sites/etsy
source: sitemap
fetched_at: 2026-03-23T07:34:15.586515-03:00
rendered_js: false
word_count: 40
summary: This document provides a technical guide on using the Firecrawl SDK to scrape, map, and search product data from Etsy, including instructions on structured data extraction with Zod schemas.
tags:
    - web-scraping
    - etsy-api
    - firecrawl
    - data-extraction
    - zod-schema
    - web-crawling
category: guide
---

## 安装与配置

```
npm install @mendable/firecrawl-js zod
```

## 概览

在抓取 Etsy 时，你通常会希望：

- 提取商品列表及其变体信息
- 获取店铺信息和评分
- 监控热门商品和分类
- 跟踪价格和销售数据
- 提取用户评价

## 使用 JSON 模式进行抓取

使用 Zod 架构提取结构化清单数据。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// 定义 Zod schema
const ListingSchema = z.object({
    title: z.string(),
    price: z.string(),
    shopName: z.string(),
    rating: z.number()
});

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set', {
    formats: [{
        type: 'json',
        schema: z.toJSONSchema(ListingSchema)
    }],
});

// 使用 Zod 解析和验证
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ListingSchema.parse(jsonData);

console.log('✅ 已验证的商品数据:');
console.log(validated);
```

## 搜索

在 Etsy 市场上搜索商品。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('handmade jewelry site:etsy.com', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }（新闻）, { type: 'images' }（图片）
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## 抓取

抓取单个 Etsy 商品详情页。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set', {
    formats: ['markdown'], // 例如 html、links 等
    onlyMainContent: true
});

console.log(result);
```

## Map

列出 Etsy 店铺或分类下所有可用的 URL。注意：Map 仅返回 URL，不包含页面内容。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.etsy.com/shop/YourShopName');

console.log(mapResult.links);
// 返回 URL 数组,不包含内容
```

## Crawl

批量抓取 Etsy 店铺或分类下的多个页面。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://www.etsy.com/c/jewelry', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

## 批量抓取

同时抓取多个 Etsy 商品链接 URL。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 等待完成
const job = await firecrawl.batchScrape([
    'https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set',
    'https://www.etsy.com/market/handmade_jewelry',
    'https://www.etsy.com/market/jewelry_handmade'],
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