---
title: One doc tagged with "Lock" | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/tags/lock
source: sitemap
fetched_at: 2026-02-17T15:40:48.205532-03:00
rendered_js: false
word_count: 63
summary: This document explains the Lock API in Moodle, which is used to prevent concurrent access to resources by multiple processes, particularly within cron jobs.
tags:
    - lock-api
    - moodle-development
    - concurrency-control
    - cron-management
    - resource-locking
category: api
---

## [Lock API](https://moodledev.io/docs/5.2/apis/core/lock)

Locking is required whenever you need to prevent two, or more, processes accessing the same resource at the same time. The prime candidate for locking in Moodle is cron. Locking allows multiple cron processes to work on different parts of cron at the same time with no risk that they will conflict (work on the same job at the same time).