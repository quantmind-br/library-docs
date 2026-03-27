---
title: ページをクロール - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/webhook-crawl-page
source: sitemap
fetched_at: 2026-03-23T07:12:40.564195-03:00
rendered_js: false
word_count: 0
summary: This document represents a JSON-formatted data structure returned by a web crawling service, containing crawled page content and associated metadata.
tags:
    - web-crawling
    - data-extraction
    - json-schema
    - web-scraping
    - api-response
category: api
---

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "a1b2c3d4-0002-0000-0000-000000000000",
  "data": [
    {
      "markdown": "# Example Page\n\nThis is the page content.",
      "metadata": {
        "title": "Example Page",
        "description": "ページの例。",
        "sourceURL": "https://example.com/page",
        "statusCode": 200
      }
    }
  ],
  "metadata": {}
}
```