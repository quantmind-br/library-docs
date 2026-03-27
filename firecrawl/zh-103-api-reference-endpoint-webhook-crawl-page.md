---
title: 爬取页面 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/webhook-crawl-page
source: sitemap
fetched_at: 2026-03-23T07:08:32.16755-03:00
rendered_js: false
word_count: 0
summary: This document outlines the JSON schema structure used for returning crawled web page data, including specific fields for the crawler output and page metadata.
tags:
    - json-schema
    - web-crawling
    - data-extraction
    - api-response
    - webhook-payload
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
        "description": "页面示例。",
        "sourceURL": "https://example.com/page",
        "statusCode": 200
      }
    }
  ],
  "metadata": {}
}
```