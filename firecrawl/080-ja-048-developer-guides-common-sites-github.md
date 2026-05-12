---
title: GitHubのスクレイピング - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/common-sites/github
source: sitemap
fetched_at: 2026-03-23T07:32:54.096335-03:00
rendered_js: false
word_count: 31
summary: This document provides a technical guide on using the Firecrawl SDK to scrape, crawl, map, and extract structured data from GitHub repositories and documentation sites.
tags:
    - firecrawl
    - web-scraping
    - data-extraction
    - github-api
    - node-js
    - zod-schema
    - web-crawling
category: tutorial
---

Firecrawlのコア機能を使って、GitHubのリポジトリ、Issue、ドキュメントをスクレイピングする方法を解説します。

## セットアップ

```
npm install @mendable/firecrawl-js zod
```

## JSONモードでスクレイプ

Zod スキーマを使ってリポジトリから構造化データを抽出します。

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

## Search

GitHub 上のリポジトリ、Issue、ドキュメントを検索します。

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

## Scrape

リポジトリ、Issue、またはファイルなど、1 つの GitHub ページをスクレイプします。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://github.com/firecrawl/firecrawl', {
    formats: ['markdown'] // 例: html, links など
});

console.log(result);
```

## Map

リポジトリやドキュメントサイト内に存在するすべての利用可能な URL を列挙します。注記: Map はコンテンツを含まない URL のみを返します。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://github.com/vercel/next.js/tree/canary/docs');

console.log(mapResult.links);
// コンテンツなしのURLの配列を返す
```

## Crawl

リポジトリやドキュメント内の複数ページをクロールします。

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

## Batch Scrape

複数の GitHub URL を一括でスクレイプします。

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 完了を待機
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

## JSONモードでのバッチスクレイピング

複数のリポジトリから構造化データを一括で抽出します。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// 完了を待機
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