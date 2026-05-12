---
title: Prévia de Parâmetros de Crawler - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/crawl-params-preview
source: sitemap
fetched_at: 2026-03-23T07:11:25.273621-03:00
rendered_js: false
word_count: 0
summary: This document defines the JSON structure for configuring web crawler behavior, including path filtering, depth limits, and crawl scope settings.
tags:
    - web-crawler
    - configuration-schema
    - crawl-settings
    - data-extraction
    - api-definition
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