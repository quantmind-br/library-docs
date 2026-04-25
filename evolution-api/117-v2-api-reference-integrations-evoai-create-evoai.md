---
title: Create EvoAI Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evoai/create-evoai
source: sitemap
fetched_at: 2026-04-12T18:49:29.660233968-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL example demonstrating how to make a POST request to an API endpoint for creating an instance, including various configuration parameters.
tags:
    - curl-command
    - api-call
    - post-request
    - json-data
    - instance-creation
category: reference
---

```
curl --request POST \
  --url https://evolution-example/evoai/create/{instance} \
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