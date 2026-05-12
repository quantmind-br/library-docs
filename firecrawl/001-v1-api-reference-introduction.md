---
title: Introduction - Firecrawl Docs
url: https://docs.firecrawl.dev/v1/api-reference/introduction
source: sitemap
fetched_at: 2026-03-23T07:37:23.487661-03:00
rendered_js: false
word_count: 170
summary: This document provides the foundational technical information for interacting with the Firecrawl API, including base URL, authentication procedures, HTTP status code definitions, and rate limiting policies.
tags:
    - api-authentication
    - rate-limiting
    - http-status-codes
    - developer-documentation
    - api-base-url
category: api
---

## Features

## Agentic Features

## Base URL

All requests contain the following base URL:

```
https://api.firecrawl.dev
```

## Authentication

For authentication, it’s required to include an Authorization header. The header should contain `Bearer fc-123456789`, where `fc-123456789` represents your API Key.

```
Authorization: Bearer fc-123456789
```

​

## Response codes

Firecrawl employs conventional HTTP status codes to signify the outcome of your requests. Typically, 2xx HTTP status codes denote success, 4xx codes represent failures related to the user, and 5xx codes signal infrastructure problems.

StatusDescription200Request was successful.400Verify the correctness of the parameters.401The API key was not provided.402Payment required404The requested resource could not be located.429The rate limit has been surpassed.5xxSignifies a server error with Firecrawl.

Refer to the Error Codes section for a detailed explanation of all potential API errors. ​

## Rate limit

The Firecrawl API has a rate limit to ensure the stability and reliability of the service. The rate limit is applied to all endpoints and is based on the number of requests made within a specific time frame. When you exceed the rate limit, you will receive a 429 response code.