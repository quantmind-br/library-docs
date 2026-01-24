---
title: Events · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/events/index.md
source: llms
fetched_at: 2026-01-24T15:36:57.539390602-03:00
rendered_js: false
word_count: 221
summary: This document explains the various events emitted by the meeting participants object, enabling developers to synchronize their UI with participant status changes, grid updates, and media stream activities.
tags:
    - realtimekit
    - event-listeners
    - participant-management
    - grid-events
    - meeting-sdk
    - video-conferencing
category: reference
---

This page provides an overview of the events emitted by `meeting.participants` and related participant maps, which you can use to keep your UI in sync with changes such as participants joining or leaving, pinning updates, active speaker changes, and grid view mode or page changes.

Prerequisites

This page assumes you have already initialized the SDK and understand the meeting object structure. Refer to [Initialize SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) and [Meeting Object Explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/) if needed.

## Grid events

These events allow you to monitor changes to the grid.

### View mode change

### Page change

### Active speaker

Triggered when a participant starts speaking.

## Participant map events

These events allow you to monitor changes to remote participant maps. Use them to get notified when a participant joins or leaves the meeting, is pinned, or moves out of the grid.

### Participant joined

Triggered when any participant joins the meeting.

### Participant left

Triggered when any participant leaves the meeting.

### Active participants changed

### Participant pinned

Triggered when a participant is pinned.

### Participant unpinned

Triggered when a participant is unpinned.

## Participant events

You can monitor changes to a specific participant using the following events.

### Video update

Triggered when any participant starts or stops video.

### Audio update

Triggered when any participant starts or stops audio.

### Screen share update

Triggered when any participant starts or stops screen share.

### Network quality score

## Listen to participant events