---
title: Window | Camoufox
url: https://camoufox.com/fingerprint/window/
source: sitemap
fetched_at: 2026-03-09T16:48:06.112966-03:00
rendered_js: false
word_count: 103
summary: This document details a set of properties that allow for the spoofing or modification of various window metrics, including dimensions, scroll positions, and history length.
tags:
    - window-properties
    - spoofing
    - browser-metrics
    - scroll-offsets
    - viewport
    - history
category: reference
---

#### [#](#spoof-the-innerouter-window-size-scroll-offsets-window-position-history-length-and-more)Spoof the inner/outer window size, scroll offsets, window position, history length, and more.

* * *

## [#](#properties)Properties

PropertyTypeDescription`window.scrollMinX`intMinimum horizontal scroll offset`window.scrollMinY`intMinimum vertical scroll offset`window.scrollMaxX`intMaximum horizontal scroll offset`window.scrollMaxY`intMaximum vertical scroll offset`window.outerHeight`uintTotal height of the browser window`window.outerWidth`uintTotal width of the browser window`window.innerHeight`uintHeight of the browser viewport`window.innerWidth`uintWidth of the browser viewport`window.screenX`intHorizontal distance from the left border`window.screenY`intVertical distance from the top border`window.history.length`uintNumber of entries in the session history`window.devicePixelRatio`doubleRatio of physical pixels to CSS pixels

* * *

##### Note

Setting the outer window viewport will cause some cosmetic defects to the Camoufox window if the user attempts to manually resize it. Under no circumstances will Camoufox allow the outer window viewport to be resized.