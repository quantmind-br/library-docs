---
title: WebRTC IP | Camoufox
url: https://camoufox.com/fingerprint/webrtc/
source: sitemap
fetched_at: 2026-03-09T16:48:09.346165-03:00
rendered_js: false
word_count: 37
summary: This document details the specific properties used by Camoufox to configure WebRTC IP spoofing by modifying ICE candidates and SDP.
tags:
    - webrtc
    - ip-spoofing
    - ice-candidates
    - sdp
    - configuration
    - properties
category: reference
---

Camoufox implements WebRTC IP spoofing at the protocol level by modifying ICE candidates and SDP before they're sent.

* * *

## [#](#properties)Properties

PropertyTypeDescription`webrtc:ipv4`strIPv4 address to use`webrtc:ipv6`strIPv6 address to use

##### Note

To completely disable WebRTC, set the `media.peerconnection.enabled` preference to `false`.