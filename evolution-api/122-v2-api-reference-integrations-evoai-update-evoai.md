---
title: Update EvoAI Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evoai/update-evoai
source: sitemap
fetched_at: 2026-04-12T18:49:23.429987088-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates using the cURL command to perform a PUT request to update an instance via the evolution-example API endpoint.
tags:
    - curl
    - put-request
    - api-update
    - json-data
    - rest-api
category: reference
---

```
curl --request PUT \
  --url https://evolution-example/evoai/update/:evoaiId/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "enabled": true,
  "agentUrl": "<string>",
  "apiKey": "<string>",
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