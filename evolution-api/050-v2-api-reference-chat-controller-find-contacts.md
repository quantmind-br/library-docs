---
title: Find Contacts - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/find-contacts
source: sitemap
fetched_at: 2026-04-12T18:50:57.455970509-03:00
rendered_js: false
word_count: 19
summary: This document details the endpoint and required parameters for using a POST request to find contacts within a chat context, specifying necessary headers and request body structure.
tags:
    - rest-api
    - post-request
    - chat-endpoint
    - contact-search
    - authorization-key
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/findContacts/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "where": {
    "id": "<string>"
  }
}
'

This response has no body data.
```

POST

/

chat

/

findContacts

/

{instance}

```
curl --request POST \
  --url https://evolution-example/chat/findContacts/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "where": {
    "id": "<string>"
  }
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

#### Response

[Get Base64](https://doc.evolution-api.com/v2/api-reference/chat-controller/get-base64)[Find Messages](https://doc.evolution-api.com/v2/api-reference/chat-controller/find-messages)