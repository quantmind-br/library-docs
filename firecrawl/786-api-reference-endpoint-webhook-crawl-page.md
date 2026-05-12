---
title: Crawl Page - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/webhook-crawl-page
source: sitemap
fetched_at: 2026-03-23T07:19:15.54261-03:00
rendered_js: false
word_count: 0
summary: This document represents a JSON-formatted response structure from a web crawling service, providing page metadata and content retrieved from a specific source URL.
tags:
    - web-scraping
    - json-schema
    - data-extraction
    - crawl-service
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
        "description": "An example page.",
        "sourceURL": "https://example.com/page",
        "statusCode": 200
      }
    }
  ],
  "metadata": {}
}
```