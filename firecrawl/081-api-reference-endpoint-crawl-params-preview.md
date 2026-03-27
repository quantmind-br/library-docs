---
title: Crawl Params Preview - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/crawl-params-preview
source: sitemap
fetched_at: 2026-03-23T07:19:45.777746-03:00
rendered_js: false
word_count: 0
summary: This document defines the JSON structure and available configuration parameters for specifying crawler behavior and scope settings.
tags:
    - crawler-configuration
    - web-scraping
    - api-schema
    - data-extraction-settings
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