---
title: Notices · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/release-notes/notice-board/index.md
source: llms
fetched_at: 2026-01-24T15:36:46.070428002-03:00
rendered_js: false
word_count: 108
summary: This document provides release notes and critical updates for Cloudflare RealtimeKit, detailing fixes for Firefox compatibility issues and the deprecation of the legacy media engine.
tags:
    - cloudflare-realtimekit
    - release-notes
    - browser-compatibility
    - sdk-update
    - sfu-media-engine
    - bug-fix
category: other
---

[Subscribe to RSS](https://developers.cloudflare.com/realtime/realtimekit/release-notes/notice-board/index.xml)

## 2025-11-21

**Update on meeting join issues in firefox 144+**

In firefox 144+, users were not able to join the meetings, due to the browser's datachannel behavior change.

Error: `x.data.arrayBuffer is not a function`

Please upgrade to atleast `v1.2.0` to fix this. It is advised to periodically upgrade the SDKs.

## 2025-03-01

**Support for legacy media engine has been removed**

Legacy media engine support has been removed.

If your organization was created before March 1, 2025 and you are upgrading to `1.2.0` or above, you may experience recording issues.

Please contact support to migrate you to the new Cloudflare SFU media engine to ensure continued recording functionality.