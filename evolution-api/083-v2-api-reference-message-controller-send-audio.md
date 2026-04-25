---
title: Send WhatsApp Audio - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/message-controller/send-audio
source: sitemap
fetched_at: 2026-04-12T18:47:45.648162953-03:00
rendered_js: false
word_count: 106
summary: This document details the parameters and response structure for a messaging function, including requirements for authorization, path identifiers, message body content, and the data received upon successful transmission.
tags:
    - messaging-api
    - authorization
    - message-sending
    - request-parameters
    - response-data
category: reference
---

#### Authorizations

Your authorization key header

#### Path Parameters

ID of the instance to connect

#### Body

Number to receive the message (with country code)

Presence time in milliseconds before sending message

Shows a preview of the target website if there's a link within the message

Mentioned everyone when the message send

Numbers to mention

Available options:

`{{remoteJID}}`

#### Response

The key of the message, which identifies the message in the chat.

The message content, which may include various types of messages like text, images, audio, etc.

The timestamp of the message, represented as a string.

The status of the message, such as sent, received, or pending.

[Send Media](https://doc.evolution-api.com/v2/api-reference/message-controller/send-media)[Send Sticker](https://doc.evolution-api.com/v2/api-reference/message-controller/send-sticker)