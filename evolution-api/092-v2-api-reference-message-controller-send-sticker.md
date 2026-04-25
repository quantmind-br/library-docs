---
title: Send Sticker - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/message-controller/send-sticker
source: sitemap
fetched_at: 2026-04-12T18:47:11.901197364-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL example demonstrating how to use an HTTP POST request to send a sticker message through an API endpoint.
tags:
    - curl-example
    - http-post
    - message-sending
    - api-request
    - json-data
category: reference
---

```
curl --request POST \
  --url https://evolution-example/message/sendSticker/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>",
  "sticker": "<string>",
  "delay": 123,
  "linkPreview": true,
  "mentionsEveryOne": true,
  "mentioned": [
    "{{remoteJID}}"
  ],
  "quoted": {
    "key": {
      "id": "<string>"
    },
    "message": {
      "conversation": "<string>"
    }
  }
}
'
```