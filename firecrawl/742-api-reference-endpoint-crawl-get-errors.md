---
title: Get Crawl Errors - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:19:55.267528-03:00
rendered_js: false
word_count: 61
summary: This document describes the API endpoint for retrieving error logs and details regarding failed URLs from a crawl job.
tags:
    - api-reference
    - crawl-job
    - error-handling
    - web-scraping
    - robots-txt
category: api
---

Get the errors of a crawl job

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

#### Response

Errored scrape jobs and error details

List of URLs that were attempted in scraping but were blocked by robots.txt