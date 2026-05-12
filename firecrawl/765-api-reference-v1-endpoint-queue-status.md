---
title: Queue Status - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:18:14.169167-03:00
rendered_js: false
word_count: 72
summary: This document provides the API specification for retrieving status metrics related to a team's web scraping queue, including active, pending, and capacity information.
tags:
    - api-reference
    - scrape-queue
    - metrics
    - job-tracking
    - authentication
    - concurrency
category: api
---

Metrics about your team's scrape queue

> Note: A new [v2 version of this API](https://docs.firecrawl.dev/api-reference/endpoint/queue-status) is now available with improved features and performance.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Response

Number of jobs currently in your queue

Number of jobs currently active

Number of jobs currently waiting

Maximum number of concurrent active jobs based on your plan

Timestamp of the most recent successful job