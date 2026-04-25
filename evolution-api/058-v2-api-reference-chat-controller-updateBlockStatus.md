---
title: Update Block Status - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/updateBlockStatus
source: sitemap
fetched_at: 2026-04-12T18:50:55.452420959-03:00
rendered_js: false
word_count: 26
summary: This document provides the cURL command structure for making a POST request to update the status of a specific block within a message endpoint.
tags:
    - rest-api
    - post-request
    - update-status
    - curl-example
    - message-endpoint
category: reference
---

```
curl --request POST \
  --url https://evolution-example/message/updateBlockStatus/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>",
  "status": "<string>"
}
'

This response has no body data.
```

POST

/

message

/

updateBlockStatus

/

{instance}

```
curl --request POST \
  --url https://evolution-example/message/updateBlockStatus/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>",
  "status": "<string>"
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

[Send Presence](https://doc.evolution-api.com/v2/api-reference/chat-controller/send-presence)[Fetch Profile Picture URL](https://doc.evolution-api.com/v2/api-reference/chat-controller/fetch-profilepic-url)