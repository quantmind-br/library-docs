---
title: Meeting Object Explained · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/index.md
source: llms
fetched_at: 2026-01-24T15:36:14.980142461-03:00
rendered_js: false
word_count: 425
summary: This document explains the structure and functionality of the RealtimeKit meeting object, the core interface for managing sessions, participants, and integrated features like chat and polls.
tags:
    - realtimekit
    - meeting-object
    - participant-management
    - sdk-reference
    - session-handling
category: reference
---

The meeting object is the core interface for interacting with a RealtimeKit session. It provides access to participants, local user controls, chat, polls, plugins, and more. This object is returned when you initialize the SDK.

Prerequisites

This page assumes you've already initialized the SDK as described in the [Initialize SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) guide.

This guide covers the core namespaces on the meeting object along with the most commonly used properties, methods, and events. Individual namespace references have been linked for more details.

## Meeting Object Structure

The meeting object contains several properties that organize different aspects of the meeting:

### Self/Local Participant

## Remote participants

### `meeting.participants` - All Remote Participants

## Meeting metadata

### `meeting.meta` - Meeting Metadata

## Chat

### `meeting.chat` - Chat Messages

## Polls

### `meeting.polls` - Polls

## Plugins

### `meeting.plugins` - Plugins

## AI features

### `meeting.ai` - AI Features

## Methods

Join or leave a meeting room:

## Understanding IDs

RealtimeKit uses two types of identifiers for participants:

* **Session ID (`id`)**: Unique identifier for each connection to a meeting. Changes every time a participant joins a new session. On Web platforms, this is called "Peer ID" and stored in `meeting.self.id` or `participant.id`. On mobile platforms, this is called "Participant ID" and stored in `meeting.localUser.id` or `participant.id`.

* **User ID (`userId`)**: Persistent identifier for a participant across multiple sessions. Remains the same when a user reconnects. This is stored in `meeting.self.userId` (Web) or `meeting.localUser.userId` (Mobile), and `participant.userId` for remote participants.

**When to use each:**

* Use `userId` when you need to track the same user across different sessions or reconnections (for example, saving user preferences or permissions)
* Use `id` when working with the current session's connections (for example, managing active video streams or real-time participant states)

## Best Practices

* **Listen to events instead of polling**: The meeting object emits events when state changes occur. Subscribe to these events rather than continuously checking property values.

* **Work with participant collections**: On Web platforms, use `toArray()` to convert participant maps to arrays. On mobile platforms, participant collections are already lists that you can iterate through directly.

* **Check connection state**: Always check `roomJoined` (or `meeting.localUser.roomJoined` on mobile) before accessing properties or calling methods that require an active session.

* **Handle errors gracefully**: Many methods accept error callbacks. Always implement proper error handling to provide a good user experience.

## Next Steps

Now that you understand the meeting object structure, you can use it to build custom meeting experiences. The UI Kit components internally use this same meeting object to provide ready-to-use interfaces. In the next guide, we'll show you how to combine UI Kit components with direct meeting object access to create your own custom UI.