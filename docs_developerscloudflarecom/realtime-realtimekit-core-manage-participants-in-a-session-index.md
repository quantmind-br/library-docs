---
title: Manage Participants in a Session · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/core/manage-participants-in-a-session/index.md
source: llms
fetched_at: 2026-01-24T15:36:13.635284629-03:00
rendered_js: false
word_count: 449
summary: This document explains how to use RealtimeKit host controls to manage session participants through actions such as muting audio, disabling video, pinning users, and removing participants.
tags:
    - realtimekit
    - host-controls
    - participant-management
    - moderation
    - video-conferencing
    - session-management
category: guide
---

Prerequisites

The local participant (for example, a host or moderator) must have the required **Host Controls** permissions enabled in their preset. For details, refer to [Preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/).

Use RealtimeKit host controls to manage other participants in a live session. You can mute audio or video, pin a participant, or remove participants from the session. These actions require specific host control permissions enabled in the local participant's [Preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/). Before you show UI controls or call these methods, verify that the local participant has the necessary permissions. In this guide, the **local participant** refers to the user performing the actions.

### Select a remote participant

## Mute audio

Mute audio of participants when you need to manage background noise, moderate a classroom or webinar, or prevent interruptions during a session. This action requires the **Mute Audio** (`disable_participant_audio`) host control permission enabled in the local participant's preset.

### Mute a participant

To mute a specific participant's audio:

### Mute all participants

This affects all participants, including the local participant. To mute audio for all participants in the session:

## Disable video

Disable video of participants when you need to moderate a session, enforce privacy, or prevent unwanted video during a classroom or webinar. This action requires the **Mute Video** (`disable_participant_video`) host control permission enabled in the local participant's preset.

### Disable video for a participant

To disable a specific participant's video:

### Disable video for all participants

This affects all participants, including the local participant. To disable video for all participants in the session:

## Pin participants

Pin a participant to highlight them, such as a webinar presenter or classroom teacher. This is a session-wide action. All participants will see the pinned participant as the focus. This action requires the **Pin Participant** (`pin_participant`) host control permission enabled in the local participant's preset.

Note

Only one participant can be pinned at a time. Pinning a new participant automatically unpins the previous one.

### Pin a participant

To pin a participant in a session:

### Unpin a participant

Unpin a participant when you need to undo the highlight and return the session to a standard grid or active speaker view. To unpin a pinned participant in a session:

## Remove participants

Remove participants from the session when you need to moderate disruptive behavior or enforce session rules. This action requires the **Kick Participants** (`kick_participant`) host control permission enabled in the local participant's preset.

### Remove a participant

To remove a specific participant from the session:

### Remove all participants

This removes everyone from the session, including the local participant. This ends the session for everyone.

For a complete end-a-session flow, refer to [End a session](https://developers.cloudflare.com/realtime/realtimekit/core/end-a-session/).

To remove all participants from the session:

## Next steps

* Review how presets control permissions in [Preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/).
* Review error handling details in [Error Codes](https://developers.cloudflare.com/realtime/realtimekit/core/error-codes/).