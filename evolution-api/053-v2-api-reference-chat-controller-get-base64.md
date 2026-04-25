---
title: Get Base64 - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/get-base64
source: sitemap
fetched_at: 2026-04-12T18:50:47.522856214-03:00
rendered_js: false
word_count: 38
summary: This document details how to use a POST request to retrieve the Base64 representation of media from a chat message endpoint, including required parameters and request structure.
tags:
    - base64
    - media-message
    - api-call
    - video-conversion
category: reference
---

Get Base64 From Media Message

```
curl --request POST \
  --url https://evolution-example/chat/getBase64FromMediaMessage/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "message": {
    "key": {
      "id": "<string>"
    }
  },
  "convertToMp4": true
}
'

This response has no body data.
```

POST

/

chat

/

getBase64FromMediaMessage

/

{instance}

Get Base64 From Media Message

```
curl --request POST \
  --url https://evolution-example/chat/getBase64FromMediaMessage/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "message": {
    "key": {
      "id": "<string>"
    }
  },
  "convertToMp4": true
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Convert video to MP4, for video only

#### Response

[Fetch Profile Picture URL](https://doc.evolution-api.com/v2/api-reference/chat-controller/fetch-profilepic-url)[Find Contacts](https://doc.evolution-api.com/v2/api-reference/chat-controller/find-contacts)