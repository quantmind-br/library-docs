---
title: Parcourir une page - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/webhook-crawl-page
source: sitemap
fetched_at: 2026-03-23T07:14:23.370709-03:00
rendered_js: false
word_count: 0
summary: This document outlines the JSON schema structure used for representing crawled web page data, including internal identifiers and metadata fields.
tags:
    - web-crawling
    - data-extraction
    - json-schema
    - web-metadata
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
        "description": "Exemple de page.",
        "sourceURL": "https://example.com/page",
        "statusCode": 200
      }
    }
  ],
  "metadata": {}
}
```