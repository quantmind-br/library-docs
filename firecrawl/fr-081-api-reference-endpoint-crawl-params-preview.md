---
title: Aperçu des paramètres de crawling - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/crawl-params-preview
source: sitemap
fetched_at: 2026-03-23T07:15:51.545711-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for a web crawler configuration object used to control parameters such as crawl depth, URL inclusion/exclusion rules, and crawling behavior.
tags:
    - web-crawler
    - configuration-schema
    - json-api
    - crawling-settings
    - data-extraction
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