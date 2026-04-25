---
title: Update n8n Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/n8n/update-n8n
source: sitemap
fetched_at: 2026-04-12T18:48:37.444274975-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL command example demonstrating how to use an HTTP PUT request to update configuration settings for an n8n instance via an API endpoint.
tags:
    - curl
    - http-put
    - api-update
    - webhook-configuration
    - json-data
category: reference
---

```
curl --request PUT \
  --url https://evolution-example/n8n/update/:n8nId/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "enabled": true,
  "webhookUrl": "<string>",
  "basicAuthUser": "<string>",
  "basicAuthPassword": "<string>",
  "triggerType": "all",
  "triggerOperator": "contains",
  "triggerValue": "<string>",
  "expire": 123,
  "keywordFinish": "<string>",
  "delayMessage": 123,
  "unknownMessage": "<string>",
  "listeningFromMe": true,
  "stopBotFromMe": true,
  "keepOpen": true,
  "debounceTime": 123,
  "ignoreJids": [
    "<string>"
  ]
}
'
```