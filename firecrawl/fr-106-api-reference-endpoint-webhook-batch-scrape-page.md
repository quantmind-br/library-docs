---
title: Page de scraping en lot - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/webhook-batch-scrape-page
source: sitemap
fetched_at: 2026-03-23T07:15:01.380762-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema structure for a batch scraping response, detailing how page content and metadata are organized within the output object.
tags:
    - web-scraping
    - json-schema
    - data-extraction
    - api-response
    - batch-processing
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
        "description": "Exemple de page.",
        "sourceURL": "https://example.com",
        "statusCode": 200
      }
    }
  ],
  "metadata": {}
}
```