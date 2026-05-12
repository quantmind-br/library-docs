---
title: 队列状态 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:07:57.99799-03:00
rendered_js: false
word_count: 0
summary: This document provides a JSON response schema representing the current status and metrics of a job queue system.
tags:
    - job-queue
    - system-status
    - concurrency-metrics
    - json-schema
    - api-response
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