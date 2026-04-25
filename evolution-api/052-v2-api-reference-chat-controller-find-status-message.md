---
title: Find Status Message - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/find-status-message
source: sitemap
fetched_at: 2026-04-12T18:50:51.529689193-03:00
rendered_js: false
word_count: 19
summary: This document demonstrates how to use a cURL command to make a POST request to find status messages via an API endpoint.
tags:
    - api-endpoint
    - post-request
    - curl-example
    - chat-message
    - authorization
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/findStatusMessage/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "where": {
    "_id": "<string>",
    "id": "<string>",
    "remoteJid": "<string>",
    "fromMe": true
  },
  "limit": 123
}
'

This response has no body data.
```

POST

/

chat

/

findStatusMessage

/

{instance}

```
curl --request POST \
  --url https://evolution-example/chat/findStatusMessage/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "where": {
    "_id": "<string>",
    "id": "<string>",
    "remoteJid": "<string>",
    "fromMe": true
  },
  "limit": 123
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

#### Response

[Find Messages](https://doc.evolution-api.com/v2/api-reference/chat-controller/find-messages)[Find Chats](https://doc.evolution-api.com/v2/api-reference/chat-controller/find-chats)