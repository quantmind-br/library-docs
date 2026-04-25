---
title: Webhooks - Evolution API Documentation
url: https://doc.evolution-api.com/v2/en/configuration/webhooks
source: sitemap
fetched_at: 2026-04-12T18:46:45.597521737-03:00
rendered_js: false
word_count: 439
summary: This document details how to use webhooks for real-time integration with the Evolution API and WhatsApp, explaining both instance-based and global webhook activation methods along with supported events.
tags:
    - webhook-integration
    - real-time-updates
    - api-events
    - whatsapp-automation
    - environment-variables
category: guide
---

Webhooks allow real-time integration between the Evolution API and WhatsApp™, enabling automated data synchronization and sharing. This feature is exactly what makes it possible to create self-service bots and multi-service systems.

## Enabling Webhooks

There are two ways to enable the webhook:

- In the `.env` file with global events
- By calling the `/webhook/instance` endpoint

### Instance Webhook Events

Most users will prefer instance-based activation, as it makes it easier to control the received events. However, in some cases, a global webhook is necessary. This can be done using the global webhook variable. Here is an example with some common events being listened to:

```
{
  "url": "{{webhookUrl}}",
  "webhook_by_events": false,
  "webhook_base64": false,
  "events": [
      "QRCODE_UPDATED",
      "MESSAGES_UPSERT",
      "MESSAGES_UPDATE",
      "MESSAGES_DELETE",
      "SEND_MESSAGE",
      "CONNECTION_UPDATE",
      "TYPEBOT_START",
      "TYPEBOT_CHANGE_STATUS"
  ]    
}
```

### Parameters

ParameterTypeRequiredDescriptionenabledbooleanYesEnter “true” to create or change Webhook data, or “false” if you want to stop using it.urlstringYesWebhook URL to receive event data.webhook\_by\_eventsbooleanNoWhether to generate a specific Webhook URL for each of your events.eventsarrayNoList of events to be processed. If you don’t want to use some of these events, simply remove them from the list.

### Global Webhook Events

Each instance’s Webhook URL and events will be requested when they are created. Set up a global webhook that will listen to enabled events from all instances.

```
WEBHOOK_GLOBAL_URL=''
WEBHOOK_GLOBAL_ENABLED=false

# With this option enabled, you work with one URL per webhook event, respecting the global URL and each event's name
WEBHOOK_GLOBAL_WEBHOOK_BY_EVENTS=false

## Set the events you want to listen to; all events listed below are supported
WEBHOOK_EVENTS_APPLICATION_STARTUP=false
WEBHOOK_EVENTS_QRCODE_UPDATED=true

# Some extra events for errors
WEBHOOK_EVENTS_ERRORS=false
WEBHOOK_EVENTS_ERRORS_WEBHOOK=
```

## Supported Events

These are the available and supported webhook events:

**Environment Variable****URL****Description**APPLICATION\_STARTUP/application-startupNotifies when an application startup occursQRCODE\_UPDATED/qrcode-updatedSends the QR code in base64 format for scanningCONNECTION\_UPDATE/connection-updateInforms the status of the WhatsApp connectionMESSAGES\_SET/messages-setSends a list of all messages loaded in WhatsApp. This event occurs only onceMESSAGES\_UPSERT/messages-upsertNotifies when a message is receivedMESSAGES\_UPDATE/messages-updateInforms when a message is updatedMESSAGES\_DELETE/messages-deleteInforms when a message is deletedSEND\_MESSAGE/send-messageNotifies when a message is sentCONTACTS\_SET/contacts-setPerforms the initial loading of all contacts. This event occurs only onceCONTACTS\_UPSERT/contacts-upsertReloads all contacts with additional information. This event occurs only onceCONTACTS\_UPDATE/contacts-updateInforms when a contact is updatedPRESENCE\_UPDATE/presence-updateInforms if the user is online, performing an action such as typing or recording, and their last seen status: ‘unavailable’, ‘available’, ‘typing’, ‘recording’, ‘paused’CHATS\_SET/chats-setSends a list of all loaded chatsCHATS\_UPDATE/chats-updateInforms when a chat is updatedCHATS\_UPSERT/chats-upsertSends any new chat informationCHATS\_DELETE/chats-deleteNotifies when a chat is deletedGROUPS\_UPSERT/groups-upsertNotifies when a group is createdGROUPS\_UPDATE/groups-updateNotifies when a group has its information updatedGROUP\_PARTICIPANTS\_UPDATE/group-participants-updateNotifies when an action occurs involving a participant: ‘add’, ‘remove’, ‘promote’, ‘demote’NEW\_TOKEN/new-jwtNotifies when the token (jwt) is updated

## Webhook by Events

When enabling the WEBHOOK\_BY\_EVENTS options in both global and local webhooks, the following paths will be appended to the end of the webhook URL.

### Example

Suppose your webhook URL is `https://sub.domain.com/webhook/`. Evolution will automatically add the event name to the end of the URL when `webhook_by_events` is set to true.

## Locating Webhook

If necessary, there is an option to locate any active webhook on the specific instance.

MethodEndpointGET\[baseUrl]/webhook/find/\[instance]

### Data returned from the request:

Calling the endpoint will return all information about the webhook being used by the instance.

```
{
  "enabled": true,
  "url": "[url]",
  "webhookByEvents": false,
  "events": [
    [events]
  ]
}
```