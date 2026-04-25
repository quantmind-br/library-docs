---
title: Mark Message As Unread - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/mark-as-unread
source: sitemap
fetched_at: 2026-04-12T18:50:59.522749361-03:00
rendered_js: false
word_count: 0
summary: This document provides a command-line example using curl to send a POST request to mark a chat as unread within an evolution service instance.
tags:
    - curl
    - post-request
    - chat-api
    - unread-status
    - json-data
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/markChatUnread/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "lastMessage": [
    {
      "remoteJid": "<string>",
      "fromMe": true,
      "id": "<string>"
    }
  ],
  "chat": "<string>"
}
'
```