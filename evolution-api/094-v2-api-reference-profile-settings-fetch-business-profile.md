---
title: Fetch Business Profile - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/profile-settings/fetch-business-profile
source: sitemap
fetched_at: 2026-04-12T18:47:25.505917346-03:00
rendered_js: false
word_count: 24
summary: This document illustrates the cURL command required to make a POST request to fetch a business profile using a specified instance and phone number.
tags:
    - curl
    - rest-api
    - post-request
    - business-profile
    - api-call
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/fetchBusinessProfile/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>"
}
'

This response has no body data.
```

POST

/

chat

/

fetchBusinessProfile

/

{instance}

```
curl --request POST \
  --url https://evolution-example/chat/fetchBusinessProfile/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>"
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Phone number with country code

#### Response

[Find Chats](https://doc.evolution-api.com/v2/api-reference/chat-controller/find-chats)[Fetch Profile](https://doc.evolution-api.com/v2/api-reference/profile-settings/fetch-profile)