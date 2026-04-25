---
title: Fetch Profile Picture URL - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/fetch-profilepic-url
source: sitemap
fetched_at: 2026-04-12T18:51:05.567309349-03:00
rendered_js: false
word_count: 46
summary: This document describes how to fetch a user's profile picture URL using a POST request to the chat/fetchProfilePictureUrl endpoint.
tags:
    - profile-picture
    - api-call
    - whatsapp
    - rest-api
    - http-request
category: reference
---

Fetch Profile Picture URL

```
curl --request POST \
  --url https://evolution-example/chat/fetchProfilePictureUrl/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>"
}
'

{
  "wuid": "553198296801@s.whatsapp.net",
  "profilePictureUrl": "https://pps.whatsapp.net/v/t61.2..."
}
```

POST

/

chat

/

fetchProfilePictureUrl

/

{instance}

Fetch Profile Picture URL

```
curl --request POST \
  --url https://evolution-example/chat/fetchProfilePictureUrl/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>"
}
'

{
  "wuid": "553198296801@s.whatsapp.net",
  "profilePictureUrl": "https://pps.whatsapp.net/v/t61.2..."
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Number to fetch profile picture URL: {{remoteJid}}

#### Response

The WhatsApp User ID (WUID).

URL of the user's profile picture.

[Update Block Status](https://doc.evolution-api.com/v2/api-reference/chat-controller/updateBlockStatus)[Get Base64](https://doc.evolution-api.com/v2/api-reference/chat-controller/get-base64)