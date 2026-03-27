---
title: Get Active Crawls - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/crawl-active
source: sitemap
fetched_at: 2026-03-23T07:18:56.868436-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema structure for a web crawling and scraping request, detailing configurable options such as content parsing, proxy settings, and browser interactions.
tags:
    - web-scraping
    - api-schema
    - data-extraction
    - json-config
    - web-crawling
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