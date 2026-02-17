---
title: One doc tagged with "Lock" | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/tags/lock
source: sitemap
fetched_at: 2026-02-17T15:20:03.412114-03:00
rendered_js: false
word_count: 63
summary: The Moodle Lock API provides a mechanism to prevent multiple processes from accessing the same resource simultaneously, ensuring safe concurrent execution for tasks like cron.
tags:
    - moodle
    - lock-api
    - concurrency-control
    - process-management
    - resource-locking
category: api
---

## [Lock API](https://moodledev.io/docs/5.0/apis/core/lock)

Locking is required whenever you need to prevent two, or more, processes accessing the same resource at the same time. The prime candidate for locking in Moodle is cron. Locking allows multiple cron processes to work on different parts of cron at the same time with no risk that they will conflict (work on the same job at the same time).