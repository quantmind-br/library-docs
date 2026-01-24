---
title: Release Notes · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/release-notes/index.md
source: llms
fetched_at: 2026-01-24T15:36:41.173224848-03:00
rendered_js: false
word_count: 586
summary: This document provides a chronological record of releases for the RealtimeKit Web Core SDK, detailing new features, bug fixes, and breaking changes from version 1.0.0 to 1.2.3.
tags:
    - realtimekit
    - sdk-updates
    - release-notes
    - webrtc
    - video-conferencing
    - media-handling
category: other
---

[Subscribe to RSS](https://developers.cloudflare.com/realtime/realtimekit/release-notes/index.xml)

## 2026-01-05

**RealtimeKit Web Core 1.2.3**

**Fixes**

* Fixed an issue where users who joined a meeting with audio and video disabled and then initiated tab screen sharing would experience SDP corruption upon stopping the screen share, preventing subsequent actions such as enabling audio or video.

  Error thrown:

  ```text
  InvalidAccessError: Failed to execute 'setRemoteDescription' on 'RTCPeerConnection': Failed to set remote answer sdp: Failed to set remote audio description send parameters for m-section with mid='<N>'
  ```

* Fixed an issue where awaiting `RealtimeKitClient.initMedia` did not return media tracks

  Example usage:

  ```ts
  const media = await RealtimeKitClient.initMedia({
    video : true,
    audio: true,
  });

  const { videoTrack, audioTrack } = media;
  ```

* Fixed an issue where an undefined variable caused `TypeError: Cannot read properties of undefined (reading 'getValue')` in media retrieval due to a race condition.

## 2025-12-17

**RealtimeKit Web Core 1.2.2**

**Fixes**

* Fixed an issue where camera switching between front and rear cameras was not working on Android devices
* Fixed device selection logic to prioritize media devices more effectively
* Added PIP support for [Reactions](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/addons/#reactions-1)

## 2025-11-18

**RealtimeKit Web Core 1.2.1**

**Fixes**

* Resolved an issue preventing default media device selection.
* Fixed SDK bundle to include `browser.js` instead of incorrectly shipping `index.iife.js` in 1.2.0.

**Enhancements**

* External media devices are now prioritized over internal devices when no preferred device is set.

## 2025-10-30

**RealtimeKit Web Core 1.2.0**

**Features**

* Added support for configuring simulcast via `initMeeting`:

  ```ts
  initMeeting({
    overrides: {
      simulcastConfig: {
        disable: false,
        encodings: [{ scaleResolutionDownBy: 2 }],
      },
    },
  });
  ```

**Fixes**

* Resolved an issue where remote participants' video feeds were not visible during grid pagination in certain edge cases.
* Fixed a bug preventing participants from switching microphones if the first listed microphone was non-functional.

**Breaking changes**

* Legacy media engine support has been removed. If your organization was created before March 1, 2025 and you are upgrading to this SDK version or later, you may experience recording issues. Contact support to migrate to the new Cloudflare SFU media engine to ensure continued recording functionality.

## 2025-08-26

**RealtimeKit Web Core 1.1.7**

**Fixes**

* Prevented speaker change events from being emitted when the active speaker does not change.
* Addressed a behavioral change in microphone switching on recent versions of Google Chrome.
* Added `deviceInfo` logs to improve debugging capabilities for React Native.
* Fixed an issue that queued multiple media consumers for the same peer, optimizing resource usage.

## 2025-08-14

**RealtimeKit Web Core 1.1.6**

**Enhancements**

* Internal changes to make debugging of media consumption issues easier and faster.

## 2025-08-04

**RealtimeKit Web Core 1.1.5**

**Fixes**

* Improved React Native support for `AudioActivityReporter` with proper audio sampling.
* Resolved issue preventing users from creating polls.
* Fixed issue where leaving a meeting took more than 20 seconds.

## 2025-07-17

**RealtimeKit Web Core 1.1.4**

**Fixes**

* Livestream feature is now available to all beta users.
* Fixed Livestream stage functionality where hosts were not consuming peer videos upon participants' stage join.
* Resolved issues with viewer joins and leaves in Livestream stage.

## 2025-07-08

**RealtimeKit Web Core 1.1.3**

**Fixes**

* Fixed issue where users could not enable video mid-meeting if they joined without video initially.

## 2025-07-02

**RealtimeKit Web Core 1.1.2**

**Fixes**

* Fixed edge case in large meetings where existing participants could not hear or see newly joined users.

## 2025-06-30

**RealtimeKit Web Core 1.1.0–1.1.1**

**Features**

* Added methods to toggle self tile visibility.
* Introduced broadcast functionality across connected meetings (breakout rooms).

**New API**

* Broadcast messages across meetings:

  ```ts
  meeting.participants.broadcastMessage("<message_type>", { message: "Hi" }, {
    meetingIds: ["<connected_meeting_id>"],
  });
  ```

**Enhancements**

* Reduced time to display videos of newly joined participants when joining in bulk.
* Added support for multiple meetings on the same page in RealtimeKit Core SDK.

## 2025-06-17

**RealtimeKit Web Core 1.0.2**

**Fixes**

* Enhanced error handling for media operations.
* Fixed issue where active participants with audio or video were not appearing in the active participant list.

## 2025-05-29

**RealtimeKit Web Core 1.0.1**

**Fixes**

* Resolved initial setup issues with Cloudflare RealtimeKit integration.
* Fixed meeting join and media connectivity issues.
* Enhanced media track handling.

## 2025-05-29

**RealtimeKit Web Core 1.0.0**

**Features**

* Initial release of Cloudflare RealtimeKit with support for group calls, webinars, livestreaming, polls, and chat.