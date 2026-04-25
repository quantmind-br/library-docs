---
title: Set Webhook - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/webhook/set
source: sitemap
fetched_at: 2026-04-12T18:46:55.637296124-03:00
rendered_js: false
word_count: 62
summary: This document details the process and available options for enabling a webhook, specifying which types of events will be sent to the configured endpoint.
tags:
    - webhook-configuration
    - event-types
    - authorization-key
    - api-events
    - webhooks
category: reference
---

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

enable webhook to instance

Enables Webhook by events

Sends files in base64 when available

Events to be sent to the Webhook

Minimum array length: `1`

Available options:

`APPLICATION_STARTUP`,

`QRCODE_UPDATED`,

`MESSAGES_SET`,

`MESSAGES_UPSERT`,

`MESSAGES_UPDATE`,

`MESSAGES_DELETE`,

`SEND_MESSAGE`,

`CONTACTS_SET`,

`CONTACTS_UPSERT`,

`CONTACTS_UPDATE`,

`PRESENCE_UPDATE`,

`CHATS_SET`,

`CHATS_UPSERT`,

`CHATS_UPDATE`,

`CHATS_DELETE`,

`GROUPS_UPSERT`,

`GROUP_UPDATE`,

`GROUP_PARTICIPANTS_UPDATE`,

`CONNECTION_UPDATE`,

`CALL`,

`NEW_JWT_TOKEN`,

`TYPEBOT_START`,

`TYPEBOT_CHANGE_STATUS`

#### Response

[Set Presence](https://doc.evolution-api.com/v2/api-reference/instance-controller/set-presence)[Find Webhook](https://doc.evolution-api.com/v2/api-reference/webhook/get)