---
title: Python Interface | Camoufox
url: https://camoufox.com/python/
source: sitemap
fetched_at: 2026-03-09T16:47:52.100411-03:00
rendered_js: false
word_count: 80
summary: This document introduces Camoufox, a Python library that provides a lightweight wrapper around the Playwright API to automate the injection of unique device characteristics for browser fingerprint spoofing.
tags:
    - playwright-api
    - browser-fingerprinting
    - camoufox
    - device-emulation
    - python-library
category: reference
---

#### [#](#lightweight-wrapper-around-the-playwright-api-to-help-launch-camoufox-rocket)Lightweight wrapper around the Playwright API to help launch Camoufox. 🚀

* * *

Camoufox's Python library wraps around Playwright's API to help automatically generate & inject unique device characteristics into Camoufox such as the OS, device info, navigator, fonts, headers, screen/viewport size, addons, etc.

It uses [BrowserForge](https://github.com/daijro/browserforge) under the hood to generate fingerprints that mimic the statistical distribution of device characteristics in real-world traffic.

In addition, it will also calculate your target geolocation, timezone, and locale to avoid proxy detection.

Installation

installation/