---
title: ページの一括スクレイピング - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/webhook-batch-scrape-page
source: sitemap
fetched_at: 2026-03-23T07:12:45.706761-03:00
rendered_js: false
word_count: 0
summary: This document represents a JSON response structure for a batch web scraping operation, detailing the returned page content, metadata, and execution status.
tags:
    - web-scraping
    - api-response
    - data-extraction
    - json-schema
    - webhook-payload
category: api
---

```
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "b2c3d4e5-0002-0000-0000-000000000000",
  "data": [
    {
      "markdown": "# Example Page\n\nThis is the page content.",
      "metadata": {
        "title": "Example Page",
        "description": "ページの例。",
        "sourceURL": "https://example.com",
        "statusCode": 200
      }
    }
  ],
  "metadata": {}
}
```