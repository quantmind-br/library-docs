---
title: Remote Participants · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/index.md
source: llms
fetched_at: 2026-01-24T15:36:58.658089652-03:00
rendered_js: false
word_count: 267
summary: This guide explains how to manage meeting participants, including data access, video display, view modes, and administrative host controls within the RealtimeKit SDK.
tags:
    - realtime-kit
    - participant-management
    - host-controls
    - video-conferencing
    - meeting-permissions
    - waiting-room
category: guide
---

This guide explains how to access participant data, display videos, handle events, and manage participant permissions in your RealtimeKit meetings.

Prerequisites

This page assumes you've already initialized the SDK and understand the meeting object structure. Refer to [Initialize SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) and [Meeting Object Explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/) if needed.

The participant object contains all information related to a particular participants, including information about the grid and each participants media streams, name, and state variables. It is accessible via `meeting.participants`.

### Properties

### Access participant properties

### Access participant object

You can fetch a participant from the [participant maps](#participant-maps).

## Participant Maps

## View Modes

The view mode indicates whether participants are populated in `ACTIVE_GRID` mode or `PAGINATED` mode.

* **`ACTIVE_GRID` mode** - Participants are automatically replaced in `meeting.participants.active` based on who is speaking or who has their video turned on
* **`PAGINATED` mode** - Participants in `meeting.participants.active` are fixed. Use `setPage()` to change the active participants

### Set view mode

### Set page in paginated mode

### Monitor view mode

## Host Controls

The participant object allows the host several controls. These can be selected while creating the host [preset](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/create/).

### Media controls

With the correct permissions, the host can disable media for remote participants.

### Waiting room controls

The waiting room allows the host to control which users can join your meeting and when. They can either choose to accept or reject the request.

You can also automate this flow so that users join the meeting automatically when the host joins the meeting, using [presets](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/create/).

#### Accept waiting room request

#### Reject waiting room request

### Pin participants

The host can choose to pin or unpin participants to the grid.

### Update participant permissions

## Display participant videos