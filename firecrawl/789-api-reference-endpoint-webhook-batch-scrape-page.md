---
title: Batch Scrape Page - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/webhook-batch-scrape-page
source: sitemap
fetched_at: 2026-03-23T07:19:23.814466-03:00
rendered_js: false
word_count: 0
summary: This document outlines the JSON schema and data structure for a batch web scraping response, detailing the format of retrieved page content and associated metadata.
tags:
    - web-scraping
    - data-extraction
    - json-schema
    - api-response
    - data-format
category: reference
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
        "description": "An example page.",
        "sourceURL": "https://example.com",
        "statusCode": 200
      }
    }
  ],
  "metadata": {}
}
```