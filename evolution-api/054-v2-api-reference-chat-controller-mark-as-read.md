---
title: Mark Message As Read - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/mark-as-read
source: sitemap
fetched_at: 2026-04-12T18:50:49.560820476-03:00
rendered_js: false
word_count: 41
summary: This document provides instructions and an example using cURL for making a POST request to mark specific chat messages as read via the API.
tags:
    - api-call
    - http-request
    - post-method
    - chat-messaging
    - read-status
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/markMessageAsRead/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "readMessages": [
    {
      "remoteJid": "<string>",
      "fromMe": true,
      "id": "<string>"
    }
  ]
}
'

{
  "message": "Read messages",
  "read": "success"
}
```

POST

/

chat

/

markMessageAsRead

/

{instance}

```
curl --request POST \
  --url https://evolution-example/chat/markMessageAsRead/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "readMessages": [
    {
      "remoteJid": "<string>",
      "fromMe": true,
      "id": "<string>"
    }
  ]
}
'

{
  "message": "Read messages",
  "read": "success"
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Messages to be mark as read

#### Response

A brief message describing the action performed.

The status of the read action.

[Check is WhatsApp](https://doc.evolution-api.com/v2/api-reference/chat-controller/check-is-whatsapp)[Mark Message As Unread](https://doc.evolution-api.com/v2/api-reference/chat-controller/mark-as-unread)