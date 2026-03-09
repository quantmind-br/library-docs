---
title: Voices | Camoufox
url: https://camoufox.com/fingerprint/voices/
source: sitemap
fetched_at: 2026-03-09T16:48:10.329521-03:00
rendered_js: false
word_count: 45
summary: This document discusses methods for spoofing voices within the Web Speech API, noting a limitation with the `voices:fakeCompletion` feature.
tags:
    - web-speech-api
    - voice-spoofing
    - tts
    - browser-api
    - bot-detection
category: concept
---

Spoof the voices used in the browser's Web Speech API.

Using `voices:fakeCompletion` is not fully implemented. It can be hypothetically detectable if a website measures the utterance duration and compares it with the elapsed time taken. However, anti-bots will never play TTS to detect you.