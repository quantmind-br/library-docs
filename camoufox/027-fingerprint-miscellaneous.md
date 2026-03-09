---
title: Miscellaneous | Camoufox
url: https://camoufox.com/fingerprint/miscellaneous/
source: sitemap
fetched_at: 2026-03-09T16:48:11.15739-03:00
rendered_js: false
word_count: 51
summary: This document details properties used to spoof or simulate battery status information and the availability of a PDF viewer within a browser environment.
tags:
    - spoofing
    - battery-status
    - pdf-viewer
    - navigator-properties
    - headless-detection
category: reference
---

### [#](#spoof-battery-status-and-pdf-viewer)Spoof battery status and PDF viewer.

PropertyTypeDescription`pdfViewerEnabled`boolSets navigator.pdfViewerEnabled. Please keep this on though, many websites will flag a lack of pdfViewer as a headless browser.`battery:charging`boolBattery charging status`battery:chargingTime`doubleBattery charging time`battery:dischargingTime`doubleBattery discharging time`battery:level`doubleBattery level

##### Note

Please keep pdfViewer on, as many websites will flag a lack of PDF viewer as a headless browser.