---
title: One doc tagged with "Lock" | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/tags/lock
source: sitemap
fetched_at: 2026-02-17T15:08:38.948582-03:00
rendered_js: false
word_count: 63
summary: This document explains the purpose of the Moodle Lock API, which prevents multiple processes from accessing the same resource simultaneously to avoid conflicts, particularly during cron execution.
tags:
    - lock-api
    - moodle-development
    - concurrency
    - cron-management
    - resource-locking
category: api
---

## [Lock API](https://moodledev.io/docs/4.5/apis/core/lock)

Locking is required whenever you need to prevent two, or more, processes accessing the same resource at the same time. The prime candidate for locking in Moodle is cron. Locking allows multiple cron processes to work on different parts of cron at the same time with no risk that they will conflict (work on the same job at the same time).