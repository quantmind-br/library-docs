---
title: Obter rastreamentos ativos - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/crawl-active
source: sitemap
fetched_at: 2026-03-23T07:11:28.993066-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for a web crawling request, outlining the configuration options available for scraping content, including formatting, filters, and browser emulation settings.
tags:
    - web-scraping
    - api-schema
    - data-extraction
    - json-payload
    - crawl-configuration
category: api
---

```
{
  "success": true,
  "crawls": [
    {
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "teamId": "<string>",
      "url": "<string>",
      "options": {
        "scrapeOptions": {
          "formats": [
            "markdown"
          ],
          "onlyMainContent": true,
          "includeTags": [
            "<string>"
          ],
          "excludeTags": [
            "<string>"
          ],
          "maxAge": 172800000,
          "minAge": 123,
          "headers": {},
          "waitFor": 0,
          "mobile": false,
          "skipTlsVerification": true,
          "timeout": 30000,
          "parsers": [
            "pdf"
          ],
          "actions": [
            {
              "type": "wait",
              "milliseconds": 2
            }
          ],
          "location": {
            "country": "US",
            "languages": [
              "en-US"
            ]
          },
          "removeBase64Images": true,
          "blockAds": true,
          "proxy": "auto",
          "storeInCache": true
        }
      }
    }
  ]
}
```