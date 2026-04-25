---
title: Send Plain Text - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/message-controller/send-text
source: sitemap
fetched_at: 2026-04-12T18:47:26.341858693-03:00
rendered_js: false
word_count: 70
summary: This document demonstrates how to send a text message using the /message/sendText endpoint, detailing required parameters for headers, path, and body data.
tags:
    - sending-messages
    - api-call
    - text-messaging
    - rest-api
    - webhook-data
category: guide
---

```
curl --request POST \
  --url https://evolution-example/message/sendText/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>",
  "text": "<string>",
  "delay": 123,
  "linkPreview": true,
  "mentionsEveryOne": true,
  "mentioned": [
    "{{remoteJID}}"
  ],
  "quoted": {
    "key": {
      "id": "<string>"
    },
    "message": {
      "conversation": "<string>"
    }
  }
}
'

{
  "key": {
    "remoteJid": "553198296801@s.whatsapp.net",
    "fromMe": true,
    "id": "BAE594145F4C59B4"
  },
  "message": {
    "extendedTextMessage": {
      "text": "Olá!"
    }
  },
  "messageTimestamp": "1717689097",
  "status": "PENDING"
}
```

POST

/

message

/

sendText

/

{instance}

```
curl --request POST \
  --url https://evolution-example/message/sendText/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>",
  "text": "<string>",
  "delay": 123,
  "linkPreview": true,
  "mentionsEveryOne": true,
  "mentioned": [
    "{{remoteJID}}"
  ],
  "quoted": {
    "key": {
      "id": "<string>"
    },
    "message": {
      "conversation": "<string>"
    }
  }
}
'

{
  "key": {
    "remoteJid": "553198296801@s.whatsapp.net",
    "fromMe": true,
    "id": "BAE594145F4C59B4"
  },
  "message": {
    "extendedTextMessage": {
      "text": "Olá!"
    }
  },
  "messageTimestamp": "1717689097",
  "status": "PENDING"
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Number to receive the message (with country code)

Presence time in milliseconds before sending message

Shows a preview of the target website if there's a link within the message

Mentioned everyone when the message send

Numbers to mention

Available options:

`{{remoteJID}}`

#### Response

The timestamp of the message.

The status of the message.

[Find Settings](https://doc.evolution-api.com/v2/api-reference/settings/get)[Send Status](https://doc.evolution-api.com/v2/api-reference/message-controller/send-status)