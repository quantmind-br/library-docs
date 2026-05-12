---
title: 队列状态 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:09:18.504651-03:00
rendered_js: false
word_count: 0
summary: This document provides a JSON response format for checking the status, concurrency limits, and job metrics of a background processing queue.
tags:
    - queue-management
    - job-processing
    - api-response
    - concurrency-monitoring
    - system-status
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