---
title: 从 v1 迁移到 v2 | Firecrawl
url: https://docs.firecrawl.dev/zh/migrate-to-v2
source: sitemap
fetched_at: 2026-03-23T07:36:59.489396-03:00
rendered_js: false
word_count: 230
summary: This document provides a comprehensive migration guide for transitioning from Firecrawl v1 to v2, outlining key functional improvements, API endpoint updates, and method name changes across JS/TS and Python SDKs.
tags:
    - firecrawl
    - api-migration
    - sdk-update
    - data-scraping
    - web-crawling
    - v2-migration
category: guide
---

- [概述](#%E6%A6%82%E8%BF%B0)
- [关键改进](#%E5%85%B3%E9%94%AE%E6%94%B9%E8%BF%9B)
- [快速迁移清单](#%E5%BF%AB%E9%80%9F%E8%BF%81%E7%A7%BB%E6%B8%85%E5%8D%95)
- [SDK 外观（v2）](#sdk-%E5%A4%96%E8%A7%82%EF%BC%88v2%EF%BC%89)
- [JS/TS](#js%2Fts)
- [方法名变更（v1 → v2）](#%E6%96%B9%E6%B3%95%E5%90%8D%E5%8F%98%E6%9B%B4%EF%BC%88v1-%E2%86%92-v2%EF%BC%89)
- [Python（同步）](#python%EF%BC%88%E5%90%8C%E6%AD%A5%EF%BC%89)
- [方法名变更（v1 → v2）](#%E6%96%B9%E6%B3%95%E5%90%8D%E5%8F%98%E6%9B%B4%EF%BC%88v1-%E2%86%92-v2%EF%BC%89-2)
- [Python（异步）](#python%EF%BC%88%E5%BC%82%E6%AD%A5%EF%BC%89)
- [formats 与抓取选项](#formats-%E4%B8%8E%E6%8A%93%E5%8F%96%E9%80%89%E9%A1%B9)
- [JSON 格式](#json-%E6%A0%BC%E5%BC%8F)
- [截图格式](#%E6%88%AA%E5%9B%BE%E6%A0%BC%E5%BC%8F)
- [爬取选项映射（v1 → v2）](#%E7%88%AC%E5%8F%96%E9%80%89%E9%A1%B9%E6%98%A0%E5%B0%84%EF%BC%88v1-%E2%86%92-v2%EF%BC%89)
- [爬取提示 + 参数预览](#%E7%88%AC%E5%8F%96%E6%8F%90%E7%A4%BA-%2B-%E5%8F%82%E6%95%B0%E9%A2%84%E8%A7%88)

## 概述

### 关键改进

- **默认更快**：请求会使用 `maxAge`（默认 2 天）进行缓存，并启用合理的默认设置，如 `blockAds`、`skipTlsVerification` 和 `removeBase64Images`。
- **新的摘要格式**：现在可以将 `"summary"` 指定为格式，直接获取页面内容的精炼摘要。
- **更新的 JSON 提取**：JSON 提取和变更追踪现在使用对象格式：`{ type: "json", prompt, schema }`。旧的 `"extract"` 格式已重命名为 `"json"`。
- **更强大的截图选项**：使用对象形式：`{ type: "screenshot", fullPage, quality, viewport }`。
- **新的搜索来源**：通过设置 `sources` 参数，除网页结果外，还可在 `"news"` 和 `"images"` 中进行搜索。
- **基于提示的智能爬取**：传入自然语言 `prompt` 进行爬取，系统会自动推导路径/限制。开始任务前，可使用新的 /crawl/params-preview 端点检查推导出的选项。

## 快速迁移清单

- 将 v1 客户端用法替换为 v2 客户端：
  
  - JS：`const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' })`
  - Python：`firecrawl = Firecrawl(api_key='fc-YOUR-API-KEY')`
  - API：改用新的 `https://api.firecrawl.dev/v2/` 端点。
- 更新格式：
  
  - 需要时使用 “summary”
  - JSON 模式：进行 JSON 抽取时使用 `{ type: "json", prompt, schema }`
  - Screenshot 和 Screenshot@fullPage：指定选项时使用 screenshot 对象格式
- 在 SDK 中采用标准化的异步流程：
  
  - Crawls：`startCrawl` + `getCrawlStatus`（或 `crawl` 等待器）
  - Batch：`startBatchScrape` + `getBatchScrapeStatus`（或 `batchScrape` 等待器）
  - Extract：`startExtract` + `getExtractStatus`（或 `extract` 等待器）
- 爬取选项映射（见下文）
- 使用 `/crawl/params-preview` 检查爬取的 `prompt`

## SDK 外观（v2）

### JS/TS

#### 方法名变更（v1 → v2）

**Scrape、Search 和 Map**

v1（FirecrawlApp）v2（Firecrawl）`scrapeUrl(url, ...)``scrape(url, options?)``search(query, ...)``search(query, options?)``mapUrl(url, ...)``map(url, options?)`

**爬取**

v1v2`crawlUrl(url, ...)``crawl(url, options?)`（waiter）`asyncCrawlUrl(url, ...)``startCrawl(url, options?)``checkCrawlStatus(id, ...)``getCrawlStatus(id)``cancelCrawl(id)``cancelCrawl(id)``checkCrawlErrors(id)``getCrawlErrors(id)`

**批量抓取**

v1v2`batchScrapeUrls(urls, ...)``batchScrape(urls, opts?)`（waiter）`asyncBatchScrapeUrls(urls, ...)``startBatchScrape(urls, opts?)``checkBatchScrapeStatus(id, ...)``getBatchScrapeStatus(id)``checkBatchScrapeErrors(id)``getBatchScrapeErrors(id)`

**提取**

v1v2`extract(urls?, params?)``extract(args)``asyncExtract(urls, params?)``startExtract(args)``getExtractStatus(id)``getExtractStatus(id)`

**其他 / 已移除**

v1v2`generateLLMsText(...)`（v2 SDK 中无）`checkGenerateLLMsTextStatus(id)`（v2 SDK 中无）`crawlUrlAndWatch(...)``watcher(jobId, ...)``batchScrapeUrlsAndWatch(...)``watcher(jobId, ...)`

* * *

### Python（同步）

#### 方法名变更（v1 → v2）

**Scrape、Search 和 Map**

v1v2`scrape_url(...)``scrape(...)``search(...)``search(...)``map_url(...)``map(...)`

**Crawling**

v1v2`crawl_url(...)``crawl(...)`（waiter）`async_crawl_url(...)``start_crawl(...)``check_crawl_status(...)``get_crawl_status(...)``cancel_crawl(...)``cancel_crawl(...)`

**Batch Scraping**

v1v2`batch_scrape_urls(...)``batch_scrape(...)`（waiter）`async_batch_scrape_urls(...)``start_batch_scrape(...)``get_batch_scrape_status(...)``get_batch_scrape_status(...)``get_batch_scrape_errors(...)``get_batch_scrape_errors(...)`

**Extraction**

v1v2`extract(...)``extract(...)``start_extract(...)``start_extract(...)``get_extract_status(...)``get_extract_status(...)`

**其他 / 已移除**

v1v2`generate_llms_text(...)`（v2 SDK 中无）`get_generate_llms_text_status(...)`（v2 SDK 中无）`watch_crawl(...)``watcher(job_id, ...)`

* * *

### Python（异步）

- `AsyncFirecrawl` 提供相同的方法（均可 await）。

## formats 与抓取选项

- 基础场景请使用字符串 formats：“markdown”、“html”、“rawHtml”、“links”、“summary”、“images”。
- 请使用 `parsers: [ { "type": "pdf" } | "pdf" ]`，而非 `parsePDF`。
- 对于 JSON、变更跟踪和截图，请使用对象 formats：

### JSON 格式

### 截图格式

v1v2`allowBackwardCrawling`（已移除）请使用 `crawlEntireDomain``maxDepth`（已移除）请使用 `maxDiscoveryDepth``ignoreSitemap` (bool)`sitemap`（例如：“only”、“skip”或“include”）(none)`prompt`

## 爬取提示 + 参数预览

查看爬取参数预览示例：