---
title: Update Typebot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/typebot/update-typebot
source: sitemap
fetched_at: 2026-04-12T18:47:43.65126946-03:00
rendered_js: false
word_count: 0
summary: This example demonstrates how to use a cURL command to perform an HTTP POST request for updating a specific typebot instance.
tags:
    - curl-command
    - http-post
    - api-update
    - json-payload
    - endpoint-call
category: reference
---

```
curl --request POST \
  --url https://evolution-example/typebot/update/:typebotId/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "enabled": true,
  "url": "<string>",
  "typebot": "<string>",
  "expire": 123,
  "keywordFinish": "<string>",
  "delayMessage": 123,
  "unknownMessage": "<string>",
  "listeningFromMe": true,
  "stopBotFromMe": true,
  "keepOpen": true,
  "debounceTime": 123,
  "triggerType": "<string>",
  "triggerOperator": "<string>",
  "triggerValue": "<string>"
}
'
```