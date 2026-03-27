---
title: Vista previa de parámetros de rastreo - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/crawl-params-preview
source: sitemap
fetched_at: 2026-03-23T07:17:53.7394-03:00
rendered_js: false
word_count: 0
summary: This document defines the JSON structure and configuration parameters for a web crawler or scraper tool.
tags:
    - web-crawling
    - data-scraping
    - api-schema
    - configuration-settings
    - url-discovery
category: reference
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