---
title: v1 → v2 移行 | Firecrawl
url: https://docs.firecrawl.dev/ja/migrate-to-v2
source: sitemap
fetched_at: 2026-03-23T07:38:02.617608-03:00
rendered_js: false
word_count: 235
summary: This document provides a comprehensive migration guide for upgrading from Firecrawl v1 to v2, detailing API changes, updated method naming conventions, and new features.
tags:
    - migration-guide
    - api-update
    - firecrawl
    - sdk-reference
    - web-scraping
category: guide
---

- [概要](#%E6%A6%82%E8%A6%81)
- [主要な改善点](#%E4%B8%BB%E8%A6%81%E3%81%AA%E6%94%B9%E5%96%84%E7%82%B9)
- [クイック移行チェックリスト](#%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E7%A7%BB%E8%A1%8C%E3%83%81%E3%82%A7%E3%83%83%E3%82%AF%E3%83%AA%E3%82%B9%E3%83%88)
- [SDK サーフェス（v2）](#sdk-%E3%82%B5%E3%83%BC%E3%83%95%E3%82%A7%E3%82%B9%EF%BC%88v2%EF%BC%89)
- [JS/TS](#js%2Fts)
- [メソッド名の変更（v1 → v2）](#%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89%E5%90%8D%E3%81%AE%E5%A4%89%E6%9B%B4%EF%BC%88v1-%E2%86%92-v2%EF%BC%89)
- [Python（同期）](#python%EF%BC%88%E5%90%8C%E6%9C%9F%EF%BC%89)
- [メソッド名の変更（v1 → v2）](#%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89%E5%90%8D%E3%81%AE%E5%A4%89%E6%9B%B4%EF%BC%88v1-%E2%86%92-v2%EF%BC%89-2)
- [Python（非同期）](#python%EF%BC%88%E9%9D%9E%E5%90%8C%E6%9C%9F%EF%BC%89)
- [フォーマットとスクレイプオプション](#%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88%E3%81%A8%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%97%E3%82%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3)
- [JSONフォーマット](#json%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88)
- [スクリーンショットフォーマット](#%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88)
- [クロールオプションの対応表（v1 → v2）](#%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%AB%E3%82%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E5%AF%BE%E5%BF%9C%E8%A1%A8%EF%BC%88v1-%E2%86%92-v2%EF%BC%89)
- [クロール用プロンプトとパラメータのプレビュー](#%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%AB%E7%94%A8%E3%83%97%E3%83%AD%E3%83%B3%E3%83%97%E3%83%88%E3%81%A8%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%81%AE%E3%83%97%E3%83%AC%E3%83%93%E3%83%A5%E3%83%BC)

## 概要

### 主要な改善点

- **デフォルトで高速化**: リクエストは `maxAge` がデフォルトで2日としてキャッシュされ、`blockAds`、`skipTlsVerification`、`removeBase64Images` といった妥当なデフォルト設定が有効です。
- **新しいサマリーフォーマット**: フォーマットに `"summary"` を指定すると、ページ内容の簡潔な要約を直接受け取れます。
- **JSON 抽出の更新**: JSON 抽出と変更トラッキングは、オブジェクト形式 `{ type: "json", prompt, schema }` を使用するようになりました。従来の `"extract"` フォーマットは `"json"` に名称変更されました。
- **スクリーンショットオプションの強化**: オブジェクト形式 `{ type: "screenshot", fullPage, quality, viewport }` を使用します。
- **新しい検索ソース**: `sources` パラメータを設定することで、Web 結果に加えて `"news"` と `"images"` も横断検索できます。
- **プロンプトによるスマートクロール**: 自然言語の `prompt` をクロールに渡すと、システムがパスや制限を自動的に導出します。ジョブ開始前に導出されたオプションを確認するには、新しい /crawl/params-preview エンドポイントを使用してください。

## クイック移行チェックリスト

- v1 クライアントの使用箇所を v2 クライアントに置き換える:
  
  - JS: `const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' })`
  - Python: `firecrawl = Firecrawl(api_key='fc-YOUR-API-KEY')`
  - API: 新しい `https://api.firecrawl.dev/v2/` エンドポイントを使用
- フォーマットを更新:
  
  - 必要に応じて `"summary"` を使用
  - JSONモード: JSON 抽出には `{ type: "json", prompt, schema }` を使用
  - Screenshot および Screenshot@fullPage: オプション指定時は screenshot オブジェクトのフォーマットを使用
- SDK の標準化された非同期フローを採用:
  
  - クロール: `startCrawl` + `getCrawlStatus`（または `crawl` ウェイター）
  - バッチ: `startBatchScrape` + `getBatchScrapeStatus`（または `batchScrape` ウェイター）
  - 抽出: `startExtract` + `getExtractStatus`（または `extract` ウェイター）
- クロールオプションのマッピング（下記参照）
- `/crawl/params-preview` でクロールの `prompt` を確認

## SDK サーフェス（v2）

### JS/TS

#### メソッド名の変更（v1 → v2）

**Scrape、Search、Map**

v1 (FirecrawlApp)v2 (Firecrawl)`scrapeUrl(url, ...)``scrape(url, options?)``search(query, ...)``search(query, options?)``mapUrl(url, ...)``map(url, options?)`

**クロール**

v1v2`crawlUrl(url, ...)``crawl(url, options?)`（waiter）`asyncCrawlUrl(url, ...)``startCrawl(url, options?)``checkCrawlStatus(id, ...)``getCrawlStatus(id)``cancelCrawl(id)``cancelCrawl(id)``checkCrawlErrors(id)``getCrawlErrors(id)`

**バッチスクレイピング**

v1v2`batchScrapeUrls(urls, ...)``batchScrape(urls, opts?)`（waiter）`asyncBatchScrapeUrls(urls, ...)``startBatchScrape(urls, opts?)``checkBatchScrapeStatus(id, ...)``getBatchScrapeStatus(id)``checkBatchScrapeErrors(id)``getBatchScrapeErrors(id)`

**抽出**

v1v2`extract(urls?, params?)``extract(args)``asyncExtract(urls, params?)``startExtract(args)``getExtractStatus(id)``getExtractStatus(id)`

**その他／削除**

v1v2`generateLLMsText(...)`（v2 SDK にはありません）`checkGenerateLLMsTextStatus(id)`（v2 SDK にはありません）`crawlUrlAndWatch(...)``watcher(jobId, ...)``batchScrapeUrlsAndWatch(...)``watcher(jobId, ...)`

* * *

### Python（同期）

#### メソッド名の変更（v1 → v2）

**Scrape、Search、Map**

v1v2`scrape_url(...)``scrape(...)``search(...)``search(...)``map_url(...)``map(...)`

**Crawling**

v1v2`crawl_url(...)``crawl(...)`（waiter）`async_crawl_url(...)``start_crawl(...)``check_crawl_status(...)``get_crawl_status(...)``cancel_crawl(...)``cancel_crawl(...)`

**バッチスクレイピング**

v1v2`batch_scrape_urls(...)``batch_scrape(...)`（waiter）`async_batch_scrape_urls(...)``start_batch_scrape(...)``get_batch_scrape_status(...)``get_batch_scrape_status(...)``get_batch_scrape_errors(...)``get_batch_scrape_errors(...)`

**抽出**

v1v2`extract(...)``extract(...)``start_extract(...)``start_extract(...)``get_extract_status(...)``get_extract_status(...)`

**その他 / 廃止**

v1v2`generate_llms_text(...)`（v2 SDK では未対応）`get_generate_llms_text_status(...)`（v2 SDK では未対応）`watch_crawl(...)``watcher(job_id, ...)`

* * *

### Python（非同期）

- `AsyncFirecrawl` は同じメソッドを備えており（すべて await 可能）、そのまま利用できます。

## フォーマットとスクレイプオプション

- 基本的な場合は文字列フォーマットを使用します: `"markdown"`, `"html"`, `"rawHtml"`, `"links"`, `"summary"`, `"images"`。
- `parsePDF` の代わりに `parsers: [ { "type": "pdf" } | "pdf" ]` を使用します。
- JSON、変更追跡、スクリーンショットにはオブジェクトフォーマットを使用します:

### JSONフォーマット

### スクリーンショットフォーマット

v1v2`allowBackwardCrawling`（削除）`crawlEntireDomain` を使用`maxDepth`（削除）`maxDiscoveryDepth` を使用`ignoreSitemap` (bool)`sitemap`（例：「only」「skip」「include」）（なし）`prompt`

## クロール用プロンプトとパラメータのプレビュー

クロールパラメータのプレビュー例: