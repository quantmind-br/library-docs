---
title: Queue Status - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:19:33.611892-03:00
rendered_js: false
word_count: 79
summary: This document provides an overview of the scrape queue metrics available for team accounts, including job statuses and account concurrency limits.
tags:
    - scrape-queue
    - metrics-api
    - job-monitoring
    - concurrency-limits
    - api-documentation
category: reference
---

Metrics about your team's scrape queue

Metrics about your team’s scrape queue.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Response

Number of jobs currently in your queue

Number of jobs currently active

Number of jobs currently waiting

Maximum number of concurrent active jobs based on your plan

Timestamp of the most recent successful job