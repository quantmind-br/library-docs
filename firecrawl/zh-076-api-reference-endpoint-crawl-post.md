---
title: 抓取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/crawl-post
source: sitemap
fetched_at: 2026-03-23T07:09:34.20157-03:00
rendered_js: false
word_count: 0
summary: This document provides the API request structure for initiating a web crawl operation using the Firecrawl v2 endpoint, including configuration options for discovery depth, scraping parameters, and webhook notifications.
tags:
    - web-scraping
    - api-request
    - crawl-configuration
    - data-extraction
    - firecrawl-api
category: api
---

```
curl --request POST \
  --url https://api.firecrawl.dev/v2/crawl \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "url": "<string>",
  "prompt": "<string>",
  "excludePaths": [
    "<string>"
  ],
  "includePaths": [
    "<string>"
  ],
  "maxDiscoveryDepth": 123,
  "sitemap": "include",
  "ignoreQueryParameters": false,
  "regexOnFullURL": false,
  "limit": 10000,
  "crawlEntireDomain": false,
  "allowExternalLinks": false,
  "allowSubdomains": false,
  "delay": 123,
  "maxConcurrency": 123,
  "webhook": {
    "url": "<string>",
    "headers": {},
    "metadata": {},
    "events": [
      "completed"
    ]
  },
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
  },
  "zeroDataRetention": false
}
'
```