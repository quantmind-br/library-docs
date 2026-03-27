---
title: Get Crawl Errors - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:18:51.80729-03:00
rendered_js: false
word_count: 60
summary: This document describes the API endpoint used to retrieve a list of failed URLs and specific error details from a web crawl job.
tags:
    - api-endpoint
    - crawl-job
    - error-reporting
    - web-scraping
    - robots-txt
category: api
---

Get the errors of a crawl job

> Note: A new [v2 version of this API](https://docs.firecrawl.dev/api-reference/endpoint/crawl-get-errors) is now available with improved features and performance.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

#### Response

Errored scrape jobs and error details

List of URLs that were attempted in scraping but were blocked by robots.txt