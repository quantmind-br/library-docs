---
title: Send List - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/message-controller/send-list
source: sitemap
fetched_at: 2026-04-12T18:47:35.80144619-03:00
rendered_js: false
word_count: 93
summary: This document details the various parameters and response elements for sending messages, covering aspects like message content structure, time precision, and available mention options.
tags:
    - messaging
    - message-sending
    - api-parameters
    - response-fields
    - user-interaction
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

[Send Poll](https://doc.evolution-api.com/v2/api-reference/message-controller/send-poll)[Send Buttons](https://doc.evolution-api.com/v2/api-reference/message-controller/send-button)