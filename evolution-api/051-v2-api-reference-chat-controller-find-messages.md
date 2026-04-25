---
title: Find Messages - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/find-messages
source: sitemap
fetched_at: 2026-04-12T18:50:45.617634071-03:00
rendered_js: false
word_count: 20
summary: This document provides the technical specification for using a POST request to the findMessages endpoint, detailing required headers like API key and content type, along with the expected JSON body structure.
tags:
    - api-endpoint
    - rest-api
    - http-request
    - json-body
    - authorization
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/findMessages/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "where": {
    "key": {
      "remoteJid": "<string>"
    }
  }
}
'

This response has no body data.
```

POST

/

chat

/

findMessages

/

{instance}

```
curl --request POST \
  --url https://evolution-example/chat/findMessages/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "where": {
    "key": {
      "remoteJid": "<string>"
    }
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

[Find Contacts](https://doc.evolution-api.com/v2/api-reference/chat-controller/find-contacts)[Find Status Message](https://doc.evolution-api.com/v2/api-reference/chat-controller/find-status-message)