---
title: Archive Chat - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/archive-chat
source: sitemap
fetched_at: 2026-04-12T18:51:09.499822674-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL command example demonstrating how to make a POST request to archive a chat within an instance.
tags:
    - curl
    - post-request
    - api-endpoint
    - chat-management
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/archiveChat/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "lastMessage": {
    "key": {
      "remoteJid": "<string>",
      "fromMe": true,
      "id": "<string>"
    }
  },
  "archive": true,
  "chat": "<string>"
}
'
```