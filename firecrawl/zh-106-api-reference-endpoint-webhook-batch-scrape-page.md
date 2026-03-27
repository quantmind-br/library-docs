---
title: 批量抓取页面 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/webhook-batch-scrape-page
source: sitemap
fetched_at: 2026-03-23T07:09:09.351326-03:00
rendered_js: false
word_count: 0
summary: This document represents a JSON response structure returned by a batch web scraping service, containing page content and associated metadata for processed URLs.
tags:
    - batch-scraping
    - web-scraping
    - json-response
    - data-extraction
    - api-output
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
        "description": "页面示例。",
        "sourceURL": "https://example.com",
        "statusCode": 200
      }
    }
  ],
  "metadata": {}
}
```