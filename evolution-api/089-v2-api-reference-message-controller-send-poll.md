---
title: Send Poll - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/message-controller/send-poll
source: sitemap
fetched_at: 2026-04-12T18:47:16.383832716-03:00
rendered_js: false
word_count: 104
summary: This document outlines the various components and data points available when interacting with a messaging or communication API, covering required fields like parameters, body values, and response elements.
tags:
    - api-payload
    - message-sending
    - data-fields
    - response-structure
    - authorization
category: reference
---

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Values for question

Available options:

`Question 1`,

`Question 2`,

`Question 3`

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

[Send Reaction](https://doc.evolution-api.com/v2/api-reference/message-controller/send-reaction)[Send List](https://doc.evolution-api.com/v2/api-reference/message-controller/send-list)