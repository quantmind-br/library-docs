---
title: Send Presence - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/send-presence
source: sitemap
fetched_at: 2026-04-12T18:51:01.63032393-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL command example demonstrating how to send a presence status update via a POST request.
tags:
    - curl-command
    - presence-api
    - http-request
    - json-data
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/sendPresence/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>",
  "options": {
    "delay": 123,
    "presence": "composing",
    "number": "<string>"
  }
}
'
```