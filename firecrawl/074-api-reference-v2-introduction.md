---
title: Introduction - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v2-introduction
source: sitemap
fetched_at: 2026-03-23T07:32:12.239284-03:00
rendered_js: false
word_count: 192
summary: This document provides the foundational technical information for integrating with the Firecrawl API, covering authentication, base URL conventions, HTTP status codes, and rate limiting policies.
tags:
    - web-scraping
    - api-documentation
    - authentication
    - rate-limiting
    - http-status-codes
category: reference
---

The Firecrawl API gives you programmatic access to web data. All endpoints share a common base URL, authentication scheme, and response format described on this page.

## Features

## Agentic Features

## Base URL

All requests use the following base URL:

```
https://api.firecrawl.dev
```

## Authentication

Every request requires an `Authorization` header with your API key:

```
Authorization: Bearer fc-YOUR-API-KEY
```

Include this header in all API calls. You can find your API key in the [Firecrawl dashboard](https://www.firecrawl.dev/app/api-keys).

## Response codes

Firecrawl uses conventional HTTP status codes to indicate the outcome of your requests. Codes in the `2xx` range indicate success, `4xx` codes indicate client errors, and `5xx` codes indicate server errors.

StatusDescription`200`Request was successful.`400`Invalid request parameters.`401`API key is missing or invalid.`402`Payment required.`404`The requested resource was not found.`429`Rate limit exceeded.`5xx`Server error on Firecrawl’s side.

When a `5xx` error occurs, the response body includes a specific error code to help you diagnose the issue.

## Rate limit

The Firecrawl API enforces rate limits on all endpoints to ensure service stability. Rate limits are based on the number of requests within a specific time window. When you exceed the rate limit, the API returns a `429` status code. Back off and retry the request after a short delay.