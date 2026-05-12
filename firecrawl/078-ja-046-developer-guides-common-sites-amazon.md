---
title: Amazonのスクレイピング - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/common-sites/amazon
source: sitemap
fetched_at: 2026-03-23T07:35:29.404084-03:00
rendered_js: false
word_count: 35
summary: This document provides a guide on using the Firecrawl SDK to extract, crawl, and search Amazon product data, including structured data extraction using Zod schemas.
tags:
    - firecrawl
    - web-scraping
    - amazon-api
    - data-extraction
    - zod-schema
    - node-js
    - web-crawling
category: guide
---

## セットアップ

```
npm install @mendable/firecrawl-js zod
```

## 概要

Amazon をスクレイピングする場合、主に次のことを行います:

- 商品情報（タイトル、価格、在庫状況）を抽出する
- 顧客レビューと評価を取得する
- 価格変動を監視する
- プログラムで商品検索を行う
- 競合の出品状況を追跡する

## JSONモードでスクレイピング

Zodスキーマを使って構造化された商品データを抽出します。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// Zodスキーマを定義
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

// Zodでパースして検証
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ProductSchema.parse(jsonData);

console.log('✅ 検証済み商品データ:');
console.log(validated);
```

## 検索

Amazonで商品を検索する。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('gaming laptop site:amazon.com', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## スクレイプ

1つの Amazon 商品ページをスクレイプします。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L', {
    formats: ['markdown'], // 例: html、links など
    onlyMainContent: true
});

console.log(result);
```

## Map

Amazon の商品ページやカテゴリーページで利用可能なすべての URL を取得します。注: Map はコンテンツではなく URL のみを返します。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics');

console.log(mapResult.links);
// コンテンツなしでURLの配列を返す
```

## クロール

Amazon のカテゴリや検索結果ページから複数のページをクロールします。

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

## バッチスクレイピング

複数の Amazon 商品 URL を同時にスクレイピングします。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 完了を待つ
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