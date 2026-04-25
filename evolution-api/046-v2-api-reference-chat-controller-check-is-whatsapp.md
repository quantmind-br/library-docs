---
title: Check is WhatsApp - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/check-is-whatsapp
source: sitemap
fetched_at: 2026-04-12T18:51:11.58352275-03:00
rendered_js: false
word_count: 50
summary: This document details the API endpoint for checking if specified WhatsApp phone numbers exist and provides information regarding required headers, request body structure, and expected JSON response format.
tags:
    - api-endpoint
    - whatsapp-number-check
    - rest-api
    - post-request
    - json-data
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/whatsappNumbers/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "numbers": [
    "<string>"
  ]
}
'

[
  {
    "exists": true,
    "jid": "553198296801@s.whatsapp.net",
    "number": "553198296801"
  }
]
```

POST

/

chat

/

whatsappNumbers

/

{instance}

```
curl --request POST \
  --url https://evolution-example/chat/whatsappNumbers/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "numbers": [
    "<string>"
  ]
}
'

[
  {
    "exists": true,
    "jid": "553198296801@s.whatsapp.net",
    "number": "553198296801"
  }
]
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Phone numbers (with country code) to be checked

#### Response

Indicates whether the WhatsApp account exists.

The JID of the WhatsApp account.

The phone number associated with the WhatsApp account.

Example:

```
[
  {
    "exists": true,
    "jid": "553198296801@s.whatsapp.net",
    "number": "553198296801"
  }
]
```

[Send Buttons](https://doc.evolution-api.com/v2/api-reference/message-controller/send-button)[Mark Message As Read](https://doc.evolution-api.com/v2/api-reference/chat-controller/mark-as-read)