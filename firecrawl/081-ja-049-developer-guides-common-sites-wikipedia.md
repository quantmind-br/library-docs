---
title: Wikipediaのスクレイピング - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/common-sites/wikipedia
source: sitemap
fetched_at: 2026-03-23T07:35:28.701524-03:00
rendered_js: false
word_count: 34
summary: このドキュメントでは、Firecrawl SDKを使用してWikipediaのデータを効率的にスクレイピング、検索、クロールし、構造化データとして抽出する方法を解説しています。
tags:
    - firecrawl
    - web-scraping
    - wikipedia
    - data-extraction
    - structured-data
    - zod
    - api-integration
category: tutorial
---

研究や知識抽出、AIアプリケーションの構築に向けて、Wikipediaを効果的にスクレイピングする方法を学びます。

## セットアップ

```
npm install @mendable/firecrawl-js zod
```

## ユースケース

- 調査の自動化とファクトチェック
- 知識グラフの構築
- 多言語コンテンツの抽出
- 教育コンテンツの集約
- エンティティ情報抽出

## JSONモードでスクレイピング

Zodスキーマを使用して、Wikipediaの記事から構造化データを抽出します。

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

## 検索

Wikipedia の記事を検索します。

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

## スクレイプ

単一の Wikipedia 記事をスクレイピングします。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://en.wikipedia.org/wiki/Artificial_intelligence', {
    formats: ['markdown'], // 例: html, links など
    onlyMainContent: true
});

console.log(result);
```

## Map

Wikipedia のポータルまたはカテゴリ内に存在するすべての URL を取得します。注: Map は URL のみを返し、コンテンツは含みません。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://en.wikipedia.org/wiki/Portal:Computer_science');

console.log(mapResult.links);
// コンテンツなしでURLの配列を返す
```

## クロール

Wikipedia のドキュメントやカテゴリ内の複数ページをクロールします。

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

## バッチスクレイピング

複数の Wikipedia URL を同時にスクレイピングします。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 完了を待つ
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