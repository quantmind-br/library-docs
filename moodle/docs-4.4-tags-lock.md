---
title: One doc tagged with "Lock" | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/tags/lock
source: sitemap
fetched_at: 2026-02-17T15:00:06.485894-03:00
rendered_js: false
word_count: 63
summary: This document introduces the Moodle Lock API, which prevents concurrent process access to shared resources to ensure task integrity, particularly during cron execution.
tags:
    - moodle
    - lock-api
    - concurrency-control
    - cron-management
    - resource-locking
category: api
---

## [Lock API](https://moodledev.io/docs/4.4/apis/core/lock)

Locking is required whenever you need to prevent two, or more, processes accessing the same resource at the same time. The prime candidate for locking in Moodle is cron. Locking allows multiple cron processes to work on different parts of cron at the same time with no risk that they will conflict (work on the same job at the same time).