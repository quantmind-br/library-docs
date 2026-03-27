---
title: Página de scraping por lotes - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/webhook-batch-scrape-page
source: sitemap
fetched_at: 2026-03-23T07:16:58.743816-03:00
rendered_js: false
word_count: 0
summary: This document outlines the JSON schema structure for batch web scraping results, including data extraction, status codes, and source metadata.
tags:
    - web-scraping
    - json-schema
    - data-extraction
    - api-response
    - metadata-parsing
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
        "description": "Una página de ejemplo.",
        "sourceURL": "https://example.com",
        "statusCode": 200
      }
    }
  ],
  "metadata": {}
}
```