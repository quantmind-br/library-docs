---
title: Agente - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/agent
source: sitemap
fetched_at: 2026-03-23T07:18:02.589056-03:00
rendered_js: false
word_count: 12
summary: This document provides the API request structure for initiating an automated agent task to perform data extraction from specified URLs.
tags:
    - data-extraction
    - agent-task
    - web-scraping
    - api-request
    - automation
category: api
---

Inicia una tarea de agente para la extracción de datos mediante agentes

```
curl --request POST \
  --url https://api.firecrawl.dev/v2/agent \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "prompt": "<string>",
  "urls": [
    "<string>"
  ],
  "schema": {},
  "maxCredits": 123,
  "strictConstrainToURLs": true,
  "model": "spark-1-mini"
}
'
```