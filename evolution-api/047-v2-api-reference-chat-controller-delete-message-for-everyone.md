---
title: Delete Message for Everyone - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/delete-message-for-everyone
source: sitemap
fetched_at: 2026-04-12T18:51:07.657852489-03:00
rendered_js: false
word_count: 88
summary: This document describes the functionality and required parameters for an API endpoint designed to delete a message visible to all participants in a chat.
tags:
    - message-deletion
    - chat-api
    - authorization
    - group-messages
    - whatsapp-protocol
category: reference
---

Delete Message For Everyone

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Chat contact or group remote JID

If the message was sent by the instance owner or the contact

Participant for group messages only TODO

#### Response

Schema representing a WhatsApp protocol message, including the key, message content, timestamp, and status.

The key that identifies the message in the chat.

The content of the message.

The timestamp of the message, represented as a string.

The status of the message, such as sent, received, or pending.

[Archive Chat](https://doc.evolution-api.com/v2/api-reference/chat-controller/archive-chat)[Update Message](https://doc.evolution-api.com/v2/api-reference/chat-controller/update-message)