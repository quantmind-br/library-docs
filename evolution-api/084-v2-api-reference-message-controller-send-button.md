---
title: Send Buttons - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/message-controller/send-button
source: sitemap
fetched_at: 2026-04-12T18:47:41.448581452-03:00
rendered_js: false
word_count: 94
summary: This document details the parameters and potential responses for sending a message, covering required headers, path parameters, body content options like mention counts, and fields returned in the response.
tags:
    - message-sending
    - api-parameters
    - response-data
    - authorization
    - chat-messaging
category: reference
---

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Presence time in milliseconds before sending message

Shows a preview of the target website if there's a link within the message

Mentioned everyone when the message send

Numbers to mention

Available options:

`{{remoteJID}}`

#### Response

The key of the message, which identifies the message in the chat.

The message content, which may include various types of messages like text, images, poll creation, etc.

The timestamp of the message, represented as a string.

The status of the message, such as sent, received, or pending.

[Send List](https://doc.evolution-api.com/v2/api-reference/message-controller/send-list)[Check is WhatsApp](https://doc.evolution-api.com/v2/api-reference/chat-controller/check-is-whatsapp)