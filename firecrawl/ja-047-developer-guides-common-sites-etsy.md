---
title: Etsyのスクレイピング - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/common-sites/etsy
source: sitemap
fetched_at: 2026-03-23T07:35:32.663483-03:00
rendered_js: false
word_count: 32
summary: This document provides a guide on using the Firecrawl SDK to scrape, map, search, and crawl data from Etsy, including instructions on extracting structured data using Zod schemas.
tags:
    - web-scraping
    - etsy-api
    - firecrawl
    - data-extraction
    - structured-data
    - zod
    - web-crawling
category: guide
---

## セットアップ

```
npm install @mendable/firecrawl-js zod
```

## 概要

Etsy をスクレイピングする場合は、通常次のようなデータを取得します:

- 商品一覧とバリエーションを抽出する
- ショップ情報と評価を取得する
- トレンドの商品やカテゴリを監視する
- 価格と売上データを追跡する
- 顧客レビューを抽出する

## JSONモードでスクレイピング

Zodスキーマを使って、構造化されたリスティングデータを抽出します。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// Zodスキーマを定義
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

// Zodでパースして検証
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ListingSchema.parse(jsonData);

console.log('✅ 検証済みリスティングデータ:');
console.log(validated);
```

## Search

Etsy マーケットプレイスで商品を検索する。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('handmade jewelry site:etsy.com', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## スクレイプ

Etsy の商品ページを 1 件スクレイピングします。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set', {
    formats: ['markdown'], // 例: html, links など
    onlyMainContent: true
});

console.log(result);
```

## Map

Etsy のショップまたはカテゴリ内で利用可能なすべての URL を取得します。注意: Map はコンテンツではなく URL のみを返します。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.etsy.com/shop/YourShopName');

console.log(mapResult.links);
// コンテンツなしでURLの配列を返します
```

## クロール

Etsyのショップまたはカテゴリ配下の複数ページをクロールします。

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

## バッチスクレイピング

複数のEtsy出品URLを同時にスクレイピングします。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 完了を待つ
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