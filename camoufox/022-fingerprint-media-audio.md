---
title: Media & Audio | Camoufox
url: https://camoufox.com/fingerprint/media-audio/
source: sitemap
fetched_at: 2026-03-09T16:48:09.598402-03:00
rendered_js: false
word_count: 46
summary: This document details properties used to spoof or fake the available media devices (microphones, webcams, speakers) and parameters of the AudioContext for testing purposes.
tags:
    - media-devices
    - spoofing
    - audiocontext
    - microphone-faking
    - webcam-faking
    - testing
category: reference
---

* * *

## [#](#media-devices)Media Devices

Spoof the amount of microphones, webcams, and speakers avaliable.

PropertyTypeDescriptionDefault`mediaDevices:enabled`boolWhether to enable media device spoofing`false``mediaDevices:micros`uintAmount of microphones`3``mediaDevices:webcams`uintAmount of webcams`1``mediaDevices:speakers`uintAmount of speakers`1`

* * *

## [#](#audiocontext)AudioContext

Spoof the AudioContext sample rate, output latency, and max channel count.

PropertyTypeDescription`AudioContext:sampleRate`uintAudioContext sample rate`AudioContext:outputLatency`doubleAudioContext output latency`AudioContext:maxChannelCount`uintAudioContext max channel count

Testing site

https://audiofingerprint.openwpm.com/