---
title: Crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/crawl-post
source: sitemap
fetched_at: 2026-03-23T07:14:26.068059-03:00
rendered_js: false
word_count: 0
summary: This document provides the API request structure and parameters for initiating a crawl job using the Firecrawl v1 endpoint.
tags:
    - api-request
    - web-crawling
    - data-scraping
    - http-post
    - firecrawl-api
category: api
---

```
curl --request POST \
  --url https://api.firecrawl.dev/v1/crawl \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "url": "<string>",
  "excludePaths": [
    "<string>"
  ],
  "includePaths": [
    "<string>"
  ],
  "regexOnFullURL": false,
  "maxDepth": 10,
  "maxDiscoveryDepth": 123,
  "ignoreSitemap": false,
  "ignoreQueryParameters": false,
  "limit": 10000,
  "allowBackwardLinks": false,
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
  },
  "zeroDataRetention": false
}
'
```