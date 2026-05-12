---
title: Map - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:18:23.611601-03:00
rendered_js: false
word_count: 148
summary: This document provides the API specifications for mapping multiple URLs using specific search parameters, authorization headers, and crawl configuration options.
tags:
    - api-reference
    - url-mapping
    - web-crawling
    - http-request
    - proxy-configuration
category: api
---

Map multiple URLs based on options

> Note: A new [v2 version of this API](https://docs.firecrawl.dev/api-reference/endpoint/map) is now available with improved features and performance.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

The base URL to start crawling from

Search query to use for mapping. During the Alpha phase, the 'smart' part of the search functionality is limited to 500 search results. However, if map finds more results, there is no limit applied.

Ignore the website sitemap when crawling.

Only return links found in the website sitemap

Include subdomains of the website

Maximum number of links to return

Required range: `x <= 30000`

Timeout in milliseconds. There is no timeout by default.

Location settings for the request. When specified, this will use an appropriate proxy if available and emulate the corresponding language and timezone settings. Defaults to 'US' if not specified.

#### Response