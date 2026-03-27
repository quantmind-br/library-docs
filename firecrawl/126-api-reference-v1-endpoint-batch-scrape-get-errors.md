---
title: Get Batch Scrape Errors - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:18:45.938457-03:00
rendered_js: false
word_count: 70
summary: This document describes the API endpoint used to retrieve error details and blocked URLs associated with a specific batch scraping job.
tags:
    - api-reference
    - batch-scraping
    - error-reporting
    - job-status
    - web-scraping
category: api
---

Get the errors of a batch scrape job

> Note: A new [v2 version of this API](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get-errors) is now available with improved error reporting and debugging capabilities.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

The ID of the batch scrape job

#### Response

Errored scrape jobs and error details

List of URLs that were attempted in scraping but were blocked by robots.txt