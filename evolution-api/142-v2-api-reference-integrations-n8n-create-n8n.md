---
title: Create n8n Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/n8n/create-n8n
source: sitemap
fetched_at: 2026-04-12T18:48:39.582249894-03:00
rendered_js: false
word_count: 0
summary: This document provides a command-line example demonstrating how to use cURL to send a POST request to an endpoint for creating or configuring a resource.
tags:
    - curl
    - post-request
    - api-call
    - json-data
    - webhooks
category: reference
---

```
curl --request POST \
  --url https://evolution-example/n8n/create/{instance} \
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