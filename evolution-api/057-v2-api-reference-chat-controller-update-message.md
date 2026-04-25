---
title: Update Message - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/update-message
source: sitemap
fetched_at: 2026-04-12T18:50:52.30438046-03:00
rendered_js: false
word_count: 0
summary: This example demonstrates how to send a POST request using curl to update a specific message within an instance via a provided API endpoint.
tags:
    - curl-command
    - post-request
    - message-update
    - api-call
    - json-data
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/updateMessage/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": 123,
  "text": "<string>",
  "key": {
    "remoteJid": "<string>",
    "fromMe": true,
    "id": "<string>"
  }
}
'
```