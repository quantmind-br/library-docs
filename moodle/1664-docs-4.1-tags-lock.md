---
title: One doc tagged with "Lock" | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/tags/lock
source: sitemap
fetched_at: 2026-02-17T14:53:11.428472-03:00
rendered_js: false
word_count: 63
summary: This document explains the Moodle Lock API, which provides a mechanism to prevent multiple processes from accessing the same resource simultaneously, primarily to manage concurrent cron jobs.
tags:
    - moodle-api
    - lock-api
    - concurrency-control
    - process-locking
    - cron-management
    - resource-synchronization
category: api
---

## [Lock API](https://moodledev.io/docs/4.1/apis/core/lock)

Locking is required whenever you need to prevent two, or more, processes accessing the same resource at the same time. The prime candidate for locking in Moodle is cron. Locking allows multiple cron processes to work on different parts of cron at the same time with no risk that they will conflict (work on the same job at the same time).