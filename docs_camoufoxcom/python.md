---
title: Python Interface | Camoufox
url: https://camoufox.com/python/
source: crawler
fetched_at: 2026-02-14T14:05:37.416612-03:00
rendered_js: true
word_count: 80
summary: This document introduces the Camoufox Python library, a lightweight Playwright wrapper designed to automate device fingerprinting and geolocation configuration to avoid detection.
tags:
    - camoufox
    - playwright-wrapper
    - browser-fingerprinting
    - anti-bot-detection
    - python-library
    - web-automation
category: reference
---

#### [#](#lightweight-wrapper-around-the-playwright-api-to-help-launch-camoufox-rocket)Lightweight wrapper around the Playwright API to help launch Camoufox. 🚀

* * *

Camoufox's Python library wraps around Playwright's API to help automatically generate & inject unique device characteristics into Camoufox such as the OS, device info, navigator, fonts, headers, screen/viewport size, addons, etc.

It uses [BrowserForge](https://github.com/daijro/browserforge) under the hood to generate fingerprints that mimic the statistical distribution of device characteristics in real-world traffic.

In addition, it will also calculate your target geolocation, timezone, and locale to avoid proxy detection.

Installation

installation/