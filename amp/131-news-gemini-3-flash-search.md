---
title: Gemini 3 Flash in the Search Subagent
url: https://ampcode.com/news/gemini-3-flash-search
source: crawler
fetched_at: 2026-02-06T02:08:04.423947584-03:00
rendered_js: false
word_count: 77
summary: This document announces the upgrade of Amp's codebase search subagent to Gemini 3 Flash, highlighting a 3x increase in speed and improved parallel tool call capabilities.
tags:
    - amp-codebase
    - gemini-3-flash
    - model-upgrade
    - search-subagent
    - performance-optimization
category: other
---

Amp's codebase search subagent now uses Gemini 3 Flash instead of Haiku 4.5. It's 3x faster for the same quality.

Gemini 3 Flash is better at parallel tool calls, explores with diverse queries, and concludes early. Where Haiku 4.5 averaged ~2.5 parallel calls per iteration, Gemini 3 Flash fires off ~8. It wraps up in ~3 turns instead of ~9.

![Performance vs Latency chart showing Gemini 3 Flash in the optimal zone: high F1 score, low latency](https://static.ampcode.com/news/finder-gemini-3-flash.png)