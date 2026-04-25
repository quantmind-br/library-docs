---
title: Send Media - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/message-controller/send-media
source: sitemap
fetched_at: 2026-04-12T18:47:13.84257132-03:00
rendered_js: false
word_count: 100
summary: This document details the various parameters and components required for sending a message, covering aspects like recipient identification, timing, content previews, mention functionality, and expected response data.
tags:
    - message-sending
    - api-parameters
    - chat-communication
    - response-fields
    - authorization
category: reference
---

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

The key of the message, which identifies the message in the chat.

The message content, which may include various types of messages like text, images, etc.

The timestamp of the message, represented as a string.

The status of the message, such as sent, received, or pending.

[Send Status](https://doc.evolution-api.com/v2/api-reference/message-controller/send-status)[Send WhatsApp Audio](https://doc.evolution-api.com/v2/api-reference/message-controller/send-audio)