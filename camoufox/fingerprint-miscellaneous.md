---
title: Miscellaneous | Camoufox
url: https://camoufox.com/fingerprint/miscellaneous/
source: crawler
fetched_at: 2026-02-14T14:05:45.847098-03:00
rendered_js: true
word_count: 51
summary: This document outlines configuration properties for spoofing a browser's battery status and PDF viewer settings to help prevent headless browser detection.
tags:
    - browser-spoofing
    - bot-detection
    - headless-browsers
    - fingerprinting
    - battery-status
    - browser-configuration
category: configuration
---

### [#](#spoof-battery-status-and-pdf-viewer)Spoof battery status and PDF viewer.

PropertyTypeDescription`pdfViewerEnabled`boolSets navigator.pdfViewerEnabled. Please keep this on though, many websites will flag a lack of pdfViewer as a headless browser.`battery:charging`boolBattery charging status`battery:chargingTime`doubleBattery charging time`battery:dischargingTime`doubleBattery discharging time`battery:level`doubleBattery level

##### Note

Please keep pdfViewer on, as many websites will flag a lack of PDF viewer as a headless browser.