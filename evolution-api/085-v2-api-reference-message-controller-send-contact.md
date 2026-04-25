---
title: Send Contact - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/message-controller/send-contact
source: sitemap
fetched_at: 2026-04-12T18:47:49.838143718-03:00
rendered_js: false
word_count: 74
summary: This document illustrates the usage of a cURL request to send a contact message via an API endpoint, detailing the required parameters for headers and the body structure.
tags:
    - api-call
    - message-sending
    - contact-message
    - curl-example
    - rest-api
category: reference
---

```
curl --request POST \
  --url https://evolution-example/message/sendContact/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>",
  "contact": [
    {
      "wuid": "<string>",
      "phoneNumber": "<string>",
      "organization": "<string>",
      "email": "<string>",
      "url": "<string>",
      "fullName": "<string>"
    }
  ]
}
'

{
  "key": {
    "remoteJid": "553198296801@s.whatsapp.net",
    "fromMe": true,
    "id": "BAE58DA6CBC941BC"
  },
  "message": {
    "contactMessage": {
      "displayName": "Guilherme Gomes",
      "vcard": "BEGIN:VCARD\nVERSION:3.0\nN:Guilherme Gomes\nFN:Guilherme Gomes\nORG:AtendAI;\nEMAIL:...",
      "contextInfo": {}
    }
  },
  "messageTimestamp": "1717780437",
  "status": "PENDING"
}
```

POST

/

message

/

sendContact

/

{instance}

```
curl --request POST \
  --url https://evolution-example/message/sendContact/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>",
  "contact": [
    {
      "wuid": "<string>",
      "phoneNumber": "<string>",
      "organization": "<string>",
      "email": "<string>",
      "url": "<string>",
      "fullName": "<string>"
    }
  ]
}
'

{
  "key": {
    "remoteJid": "553198296801@s.whatsapp.net",
    "fromMe": true,
    "id": "BAE58DA6CBC941BC"
  },
  "message": {
    "contactMessage": {
      "displayName": "Guilherme Gomes",
      "vcard": "BEGIN:VCARD\nVERSION:3.0\nN:Guilherme Gomes\nFN:Guilherme Gomes\nORG:AtendAI;\nEMAIL:...",
      "contextInfo": {}
    }
  },
  "messageTimestamp": "1717780437",
  "status": "PENDING"
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Number to receive the message (with country code)

#### Response

The key of the message, which identifies the message in the chat.

The message content, which may include various types of messages like text, images, contact, etc.

The timestamp of the message, represented as a string.

The status of the message, such as sent, received, or pending.

[Send Location](https://doc.evolution-api.com/v2/api-reference/message-controller/send-location)[Send Reaction](https://doc.evolution-api.com/v2/api-reference/message-controller/send-reaction)