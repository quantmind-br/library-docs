---
title: キューのステータス - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:12:13.674952-03:00
rendered_js: false
word_count: 0
summary: This document provides a JSON response format representing the real-time status and concurrency metrics of a job processing queue.
tags:
    - job-queue
    - api-response
    - concurrency-metrics
    - queue-status
    - system-monitoring
category: api
---

```
{
  "success": true,
  "jobsInQueue": 123,
  "activeJobsInQueue": 123,
  "waitingJobsInQueue": 123,
  "maxConcurrency": 123,
  "mostRecentSuccess": "2023-11-07T05:31:56Z"
}
```