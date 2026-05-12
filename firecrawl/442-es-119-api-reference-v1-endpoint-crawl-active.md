---
title: Obtener rastreos activos - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/crawl-active
source: sitemap
fetched_at: 2026-03-23T07:16:38.136264-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for a web crawling configuration, detailing the parameters for request settings, content scraping, and data extraction options.
tags:
    - web-scraping
    - api-schema
    - data-extraction
    - json-configuration
    - crawl-options
category: reference
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
          "onlyMainContent": true,
          "includeTags": [
            "<string>"
          ],
          "excludeTags": [
            "<string>"
          ],
          "maxAge": 0,
          "headers": {},
          "waitFor": 0,
          "mobile": false,
          "skipTlsVerification": false,
          "timeout": 30000,
          "parsePDF": true,
          "jsonOptions": {
            "schema": {},
            "systemPrompt": "<string>",
            "prompt": "<string>"
          },
          "actions": [
            {
              "type": "wait",
              "milliseconds": 2,
              "selector": "#my-element"
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
          "proxy": "basic",
          "storeInCache": true,
          "formats": [
            "markdown"
          ],
          "changeTrackingOptions": {
            "modes": [
              "git-diff"
            ],
            "schema": {},
            "prompt": "<string>",
            "tag": null
          }
        }
      }
    }
  ]
}
```