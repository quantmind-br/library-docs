---
title: 获取爬取状态 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/crawl-get
source: sitemap
fetched_at: 2026-03-23T07:08:07.41693-03:00
rendered_js: false
word_count: 0
summary: This document defines the JSON structure for an API response containing web page content, extracted metadata, and usage statistics.
tags:
    - api-response
    - data-schema
    - web-scraping
    - metadata-extraction
    - json-format
category: api
---

```
{
  "status": "<string>",
  "total": 123,
  "completed": 123,
  "creditsUsed": 123,
  "expiresAt": "2023-11-07T05:31:56Z",
  "next": "<string>",
  "data": [
    {
      "markdown": "<string>",
      "html": "<string>",
      "rawHtml": "<string>",
      "links": [
        "<string>"
      ],
      "screenshot": "<string>",
      "metadata": {
        "title": "<string>",
        "description": "<string>",
        "language": "<string>",
        "sourceURL": "<string>",
        "keywords": "<string>",
        "ogLocaleAlternate": [
          "<string>"
        ],
        "<any other metadata> ": "<string>",
        "statusCode": 123,
        "error": "<string>"
      }
    }
  ]
}
```