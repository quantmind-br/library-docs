---
title: Chat · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/core/chat/index.md
source: llms
fetched_at: 2026-01-24T15:36:04.857637421-03:00
rendered_js: false
word_count: 485
summary: This guide explains how to implement and manage chat functionality using Cloudflare RealtimeKit, covering message operations and programmatic data export via the Chat Replay API.
tags:
    - cloudflare-realtimekit
    - chat-messaging
    - real-time-communication
    - message-management
    - data-export
    - api-integration
category: guide
---

This guide explains how to send and receive chat messages in a meeting using Cloudflare RealtimeKit.

## Introduction

### Message Type

## Sending a Chat Message

### Send a Text Message

### Send an Image

### Send a File

### Send Any Message Type

## Receiving Chat Messages

## Editing Chat Messages

### Edit a Text Message

### Edit an Image

### Edit a File

### Edit Any Message Type

## Other Chat Functions

### Get Messages by a User

### Get Messages of a Particular Type

### Pinning a Chat Message

### Deleting a Chat Message

## Export chat messages

You can programmatically retrieve all chat messages of a RealtimeKit session in the following ways:

* Using the Chat Replay API
* Setting up webhook for the `meeting.chatSynced` event

### Get chat download URL

To get the chat download URL, make an HTTP `GET` request to the [Chat Replay API endpoint](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_chat/). The API returns:

```json
{
  "success": true,
  "data": {
    "chat_download_url": "string",
    "chat_download_url_expiry": "string"
  }
}
```

* **`chat_download_url`** - A URL that allows you to download the entire chat dump of a session in CSV format from AWS S3
* **`chat_download_url_expiry`** - The expiry timestamp of the `chat_download_url`. If the URL expires, call this endpoint again to obtain a new download URL

For details on the Chat Replay API endpoint, refer to the [Realtime Kit API documentation](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_chat/).

### Download the chat dump file

You can download the chat dump file in CSV format by making an HTTP `GET` request to the `chat_download_url` obtained in the previous step.

The process of downloading a file from an HTTP URL differs based on whether you are downloading on the client side or server side.

#### Download on the client

To download at client side:

1. Make a `GET` request to the `chat_download_url`
2. Convert the response to a blob
3. Create an invisible `<a>` HTML element with a `download` attribute and add the blob to its `href`
4. Programmatically click on the `<a>` element so that the browser automatically starts downloading, then remove the `<a>` element

#### Download on the server

To download on the server using Node.js streams:

1. Create a writable stream for a local file
2. Make a `GET` request to `chat_download_url`
3. Get a readable stream using `res.body` and pipe to the writable stream created in the first step

### CSV chat dump format

The CSV file contains all chat messages along with participant information and metadata. It includes the following column headings:

* **`id`** - Unique chat message ID
* **`participantId`** - ID of the participant who sent the message
* **`sessionId`** - The session ID from which the chat message was sent
* **`meetingId`** - The ID of the meeting to which this session belongs
* **`displayName`** - Display name of the participant who sent this message
* **`pinned`** - A boolean that indicates if the current message was pinned
* **`isEdited`** - A boolean that indicates if the current message was edited
* **`payloadType`** - An ENUM that indicates the type of payload sent in the chat message. It can be one of `TEXT_MESSAGE`, `IMAGE_MESSAGE`, `FILE_MESSAGE`
* **`payload`** - The actual payload sent in the chat message
* **`createdAt`** - Timestamp when this chat message was sent