---
title: Crawl 参数预览 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/crawl-params-preview
source: sitemap
fetched_at: 2026-03-23T07:09:25.722493-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for configuring web crawling parameters, including domain scoping, traversal depth, and data filtering options.
tags:
    - web-crawler
    - configuration-schema
    - data-extraction
    - crawl-settings
    - api-request-body
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