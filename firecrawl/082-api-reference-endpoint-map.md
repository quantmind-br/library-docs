---
title: Map - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:19:25.337185-03:00
rendered_js: false
word_count: 218
summary: This document describes the parameters and authentication requirements for mapping multiple URLs using the Firecrawl API.
tags:
    - url-mapping
    - web-crawling
    - api-documentation
    - sitemap-configuration
    - request-parameters
category: api
---

Map multiple URLs based on options

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

The base URL to start crawling from

Specify a search query to order the results by relevance. Example: 'blog' will return URLs that contain the word 'blog' in the URL ordered by relevance.

sitemap

enum&lt;string&gt;

default:include

Sitemap mode when mapping. If you set it to `skip`, the sitemap won't be used to find URLs. If you set it to `only`, only URLs that are in the sitemap will be returned. By default (`include`), the sitemap and other methods will be used together to find URLs.

Available options:

`skip`,

`include`,

`only`

Include subdomains of the website

Do not return URLs with query parameters

Bypass the sitemap cache to retrieve fresh URLs. Sitemap data is cached for up to 7 days; use this parameter when your sitemap has been recently updated.

Maximum number of links to return

Required range: `x <= 100000`

Timeout in milliseconds. There is no timeout by default.

Location settings for the request. When specified, this will use an appropriate proxy if available and emulate the corresponding language and timezone settings. Defaults to 'US' if not specified.

#### Response