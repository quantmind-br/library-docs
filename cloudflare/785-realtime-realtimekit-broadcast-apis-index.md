---
title: Message Broadcast APIs · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/broadcast-apis/index.md
source: llms
fetched_at: 2026-01-24T15:35:58.537582183-03:00
rendered_js: false
word_count: 185
summary: This document explains how to use broadcast APIs to send and receive custom messages among meeting participants, including details on rate limiting and audience targeting.
tags:
    - broadcast-api
    - real-time-messaging
    - signaling-channel
    - event-handling
    - rate-limiting
    - participant-management
category: api
---

The broadcast APIs allow a user to send custom messages to all other users in a meeting.

### Broadcasting a Message

The Participants module on the meeting object allows you to broadcast messages to all other users in a meeting (or to other meetings in case of connected meetings) over the signaling channel.

### Subscribe to Messages

Use the `broadcastedMessage` event to listen for messages sent via `broadcastMessage` and handle them in your application.

### Rate Limiting & Constraints

* The method is rate‑limited (server‑side + client‑side) to prevent abuse.
* Default client‑side config in the deprecated module: maxInvocations = 5 per period = 1s.
* The Participants module exposes a `rateLimitConfig` and `updateRateLimits(maxInvocations, period)` for tuning on the client, but server‑side limits may still apply.
* The event type cannot be `spotlight`. This is reserved for internal use by the SDK.

### Examples

#### Broadcast to everyone in the meeting

#### Broadcast to a specific set of participants.

Only the participants with those participantIds receive the message.

#### Broadcast to a preset

All participants whose preset name is `speaker` receive the message.

#### Broadcast across multiple meetings

All participants in the specified meetings receive the message.