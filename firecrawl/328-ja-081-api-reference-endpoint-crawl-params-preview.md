---
title: Crawl パラメータのプレビュー - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/crawl-params-preview
source: sitemap
fetched_at: 2026-03-23T07:13:36.393011-03:00
rendered_js: false
word_count: 0
summary: This document defines the configuration schema for a web crawler service, outlining parameters for path management, traversal depth, and crawl constraints.
tags:
    - web-crawler
    - configuration-schema
    - data-scraping
    - crawl-settings
    - api-payload
category: configuration
---

```
{
  "success": true,
  "data": {
    "url": "<string>",
    "includePaths": [
      "<string>"
    ],
    "excludePaths": [
      "<string>"
    ],
    "maxDepth": 123,
    "maxDiscoveryDepth": 123,
    "crawlEntireDomain": true,
    "allowExternalLinks": true,
    "allowSubdomains": true,
    "sitemap": "skip",
    "ignoreQueryParameters": true,
    "deduplicateSimilarURLs": true,
    "delay": 123,
    "limit": 123
  }
}
```