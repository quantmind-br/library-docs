---
title: Session Lifecycle · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/index.md
source: llms
fetched_at: 2026-01-24T15:36:03.175863003-03:00
rendered_js: false
word_count: 290
summary: This document explains the lifecycle of a peer within a session, detailing the transitions between setup, waitlist, meeting, and ended screens.
tags:
    - cloudflare-realtimekit
    - peer-lifecycle
    - session-management
    - ui-kit
    - meeting-states
    - waitlist-logic
category: guide
---

The [Session Guide](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/#session) explains what a session is and how to initialize one. In this guide we will talk about what happens to a peer as they move through a session, when do they go to the setup screen, waitlist screen, ended screen or any other screen, and how you can hook into these events to perform custom actions.

### Lifecycle of a Peer in a Session

![Peer Lifecycle In a Session](https://developers.cloudflare.com/_astro/peer-lifecycle.nMME9i9C_1JnPJw.svg)

Here’s how the peer lifecycle works:

1. **Initialization state**: When the SDK is initialized, the peer first sees a Setup Screen, where they can preview their audio and video before joining.

2. **Join intent**: When the peer decides to join, one of two things happens:

   * If waitlisting is enabled, they are moved to a Waitlist and see a Waitlist screen.
   * If not waitlisted, they join the session and see the main Meeting screen (Stage), where they can interact with others.

3. **During the session**: The peer can see and interact with others in the main Meeting screen (Stage).

4. **Session transitions**:

   * If the peer is rejected from the waitlist, they see a dedicated Rejected screen.
   * If the peer is kicked out, they see an Ended screen and the session ends for them.
   * If the peer leaves voluntarily, or if the meeting ends, they see an Ended screen, and the session ends for them.

Each of these screens is built with UI Kit components, which you can fully customize to match your app’s design and requirements.

The UI Kit SDKs automatically handle which notifications or screens to show at each state, so you don’t have to manage these transitions manually.

In upcoming pages, we will see how to hook into these events to perform custom actions and to build your own custom meeting experience.