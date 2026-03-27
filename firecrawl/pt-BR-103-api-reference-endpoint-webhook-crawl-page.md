---
title: Rastrear página - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/webhook-crawl-page
source: sitemap
fetched_at: 2026-03-23T07:10:58.612855-03:00
rendered_js: false
word_count: 0
summary: This document outlines the JSON schema structure for a crawl result, containing status information, page content, and metadata for a specific URL.
tags:
    - web-crawling
    - data-extraction
    - json-schema
    - web-scraping
    - api-response
category: reference
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
        "description": "Uma página de exemplo.",
        "sourceURL": "https://example.com/page",
        "statusCode": 200
      }
    }
  ],
  "metadata": {}
}
```