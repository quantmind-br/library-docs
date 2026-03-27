---
title: Get Batch Scrape Errors - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:20:04.946591-03:00
rendered_js: false
word_count: 69
summary: This document provides the API specification for retrieving error information and blocked URL details from a specific batch scrape job.
tags:
    - batch-scrape
    - error-handling
    - api-documentation
    - scrape-job
    - robots-txt
category: api
---

Get the errors of a batch scrape job

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

The ID of the batch scrape job

#### Response

Errored scrape jobs and error details

List of URLs that were attempted in scraping but were blocked by robots.txt