---
title: Web UI Kit · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/release-notes/web-ui-kit/index.md
source: llms
fetched_at: 2026-01-24T15:36:47.282203253-03:00
rendered_js: false
word_count: 293
summary: This document provides a chronological record of updates, feature enhancements, and bug fixes for the Cloudflare RealtimeKit Web UI Kit.
tags:
    - release-notes
    - realtimekit
    - web-ui-kit
    - cloudflare
    - video-conferencing
    - bug-fixes
category: reference
---

[Subscribe to RSS](https://developers.cloudflare.com/realtime/realtimekit/release-notes/web-ui-kit/index.xml)

## 2025-11-18

**RealtimeKit Web UI Kit 1.0.7**

**Fixes**

* Fixed alignment issues with unread chat message count, unread polls count, and pending participant stage request count.
* Resolved issue where action toggles were incorrectly displayed in participant video preview in the settings component.

## 2025-10-30

**RealtimeKit Web UI Kit 1.0.6**

**Fixes**

* Fixed an issue where `rtk-debugger` displayed audio and video bitrate as `0`.
* Resolved menu visibility for the last participant when the participants list is long.
* Fixed `rtk-polls` not rendering when props were provided after initial mount.
* Improved `rtk-participant-tile` audio visualizer appearance when muted (no longer shows as a single dot).
* Prevented large notifications from overflowing their container.
* Fixed a memory leak in the `mediaConnectionUpdate` event listener.
* Corrected `rtk-ui-provider` prop passing to children during consecutive meetings on the same page.

## 2025-08-14

**RealtimeKit Web UI Kit 1.0.5**

**Fixes**

* Fixed Safari CSS issues where the `rtk-settings` component was not visible and the Audio Playback modal was not taking the proper height.

**Enhancements**

* Livestream viewer now has a seeker and DVR functionality.

## 2025-07-17

**RealtimeKit Web UI Kit 1.0.4**

**Fixes**

* Fixed Angular integration issues.

**Enhancements**

* Added support for multiple meetings on the same page in RealtimeKit.
* Enhanced the `rtk-ui-provider` component to serve as a parent component for sharing common props (`meeting`, `config`, `iconPack`) with all child components.

## 2025-07-08

**RealtimeKit Web UI Kit 1.0.3**

**Fixes**

* Resolved `TypeError` that occurred for meetings without titles.
* Implemented minor UI improvements for chat components.

**Features**

* Made Livestream feature available to all beta users.

## 2025-07-02

**RealtimeKit Web UI Kit 1.0.2**

**Performance**

* Fixed dependency issues to enhance performance and Angular integration.

## 2025-06-30

**RealtimeKit Web UI Kit 1.0.1**

**Deprecated API**

* Discontinued Vue UI support.

## 2025-05-29

**RealtimeKit Web UI Kit 1.0.0**

**Features**

* Initial release of Cloudflare RealtimeKit with support for group calls, webinars, livestreaming, polls, and chat.