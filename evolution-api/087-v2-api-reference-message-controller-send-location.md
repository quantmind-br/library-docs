---
title: Send Location - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/message-controller/send-location
source: sitemap
fetched_at: 2026-04-12T18:47:23.642361769-03:00
rendered_js: false
word_count: 100
summary: This document outlines the structure and required parameters for sending messages, detailing inputs such as message content, timing information, and mention targeting, alongside describing the expected response data.
tags:
    - messaging
    - api-parameters
    - message-sending
    - response-structure
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

The message content, which may include various types of messages like text, images, location, etc.

The timestamp of the message, represented as a string.

The status of the message, such as sent, received, or pending.

[Send Sticker](https://doc.evolution-api.com/v2/api-reference/message-controller/send-sticker)[Send Contact](https://doc.evolution-api.com/v2/api-reference/message-controller/send-contact)