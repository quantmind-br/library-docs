---
title: Send Status - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/message-controller/send-status
source: sitemap
fetched_at: 2026-04-12T18:47:15.533500937-03:00
rendered_js: false
word_count: 117
summary: This document outlines the structure and available parameters for sending messages via an API, detailing requirements for authorization keys, message content types, and response data.
tags:
    - message-sending
    - api-parameters
    - authorization
    - content-types
    - status-updates
category: reference
---

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

status type

Available options:

`text`,

`image`,

`audio`

Optional for image or video

1 = SERIF 2 = NORICAN\_REGULAR 3 = BRYNDAN\_WRITE 4 = BEBASNEUE\_REGULAR 5 = OSWALD\_HEAVY

true to send to all contacts or false to send to statusJidList below

Numbers to send status

Available options:

`{{remoteJID}}`

#### Response

The key of the message, which identifies the message in the chat.

The message content, which may include various types of messages like text, images, etc.

The timestamp of the message, represented as a string.

The status of the message, such as sent, received, or pending.

The participant in the chat to whom the message was sent.

[Send Plain Text](https://doc.evolution-api.com/v2/api-reference/message-controller/send-text)[Send Media](https://doc.evolution-api.com/v2/api-reference/message-controller/send-media)