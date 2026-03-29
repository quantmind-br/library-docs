---
title: Display active speakers · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/core/display-active-speakers/index.md
source: llms
fetched_at: 2026-01-24T15:36:07.110808301-03:00
rendered_js: false
word_count: 270
summary: This document explains how RealtimeKit tracks and manages active speakers in a meeting, allowing developers to identify and display participants with prominent audio activity.
tags:
    - realtimekit
    - active-speaker
    - audio-activity
    - participant-tracking
    - meeting-ui
    - remote-participants
category: guide
---

RealtimeKit automatically detects and tracks participants who are actively speaking in a meeting. You can display either a single active speaker or multiple active speakers in your application UI, depending on your design requirements.

An active speaker in RealtimeKit is a remote participant with prominent audio activity at any given moment. The SDK maintains two types of data to help you build your UI:

* **Active speaker** — A single remote participant who is currently speaking most prominently.
* **Active participants** — A set of remote participants with the most prominent audio activity.

The SDK automatically updates these properties and subscribes to participant media as speaking activity changes. It prioritizes prominent audio activity, so a participant not currently visible in your UI can replace a visible participant if their audio becomes more active.

Note

The SDK tracks active speakers only when the local participant is viewing or rendering participants in ACTIVE mode (page 0). Refer to the [Remote participants](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#participant-view-modes) page to learn about participant view modes.

Active speaker properties contain only remote participants. The local participant is available separately.

The maximum number of participants in the `active` map is one less than the grid size configured in the local participant's [Preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/). This reserves space for the local participant in your UI. For example, if the grid size is 6, the `active` map contains a maximum of 5 remote participants.

## Display a single active speaker

## Display multiple active speakers

## Visualize audio activity

## Related resources

* [Meeting object explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/) - Understand the meeting object structure and available properties.
* [Remote participant](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/) - Learn more about remote participants in a session and how to display their video.