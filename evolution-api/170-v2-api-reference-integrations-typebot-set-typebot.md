---
title: Create Typebot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/typebot/set-typebot
source: sitemap
fetched_at: 2026-04-12T18:47:36.190977323-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL command example demonstrating how to send a POST request to an endpoint for creating a typebot instance using necessary headers and a JSON payload.
tags:
    - curl-command
    - post-request
    - api-call
    - json-data
    - typebot-creation
category: reference
---

```
curl --request POST \
  --url https://evolution-example/typebot/create/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "enabled": true,
  "url": "<string>",
  "typebot": "<string>",
  "triggerType": "<string>",
  "triggerOperator": "<string>",
  "triggerValue": "<string>",
  "expire": 123,
  "keywordFinish": "<string>",
  "delayMessage": 123,
  "unknownMessage": "<string>",
  "listeningFromMe": true,
  "stopBotFromMe": true,
  "keepOpen": true,
  "debounceTime": 123
}
'
```