---
title: Batch Scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:19:59.512015-03:00
rendered_js: false
word_count: 873
summary: This document provides the API specification for performing batch web scraping tasks, including configurable options for output formats, browser actions, caching, and proxy settings.
tags:
    - web-scraping
    - api-documentation
    - data-extraction
    - batch-processing
    - proxy-settings
    - http-requests
category: api
---

Scrape multiple URLs and optionally extract information using an LLM

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

A webhook specification object.

Maximum number of concurrent scrapes. This parameter allows you to set a concurrency limit for this batch scrape. If not specified, the batch scrape adheres to your team's concurrency limit.

If invalid URLs are specified in the urls array, they will be ignored. Instead of them failing the entire request, a batch scrape using the remaining valid URLs will be created, and the invalid URLs will be returned in the invalidURLs field of the response.

formats

(Markdown · object | Summary · object | HTML · object | Raw HTML · object | Links · object | Images · object | Screenshot · object | JSON · object | Change Tracking · object | Branding · object)\[]

Output formats to include in the response. You can specify one or more formats, either as strings (e.g., `'markdown'`) or as objects with additional options (e.g., `{ type: 'json', schema: {...} }`). Some formats require specific options to be set. Example: `['markdown', { type: 'json', schema: {...} }]`.

- Markdown
- Summary
- HTML
- Raw HTML
- Links
- Images
- Screenshot
- JSON
- Change Tracking
- Branding

Only return the main content of the page excluding headers, navs, footers, etc.

Tags to include in the output.

Tags to exclude from the output.

Returns a cached version of the page if it is younger than this age in milliseconds. If a cached version of the page is older than this value, the page will be scraped. If you do not need extremely fresh data, enabling this can speed up your scrapes by 500%. Defaults to 2 days.

When set, the request only checks the cache and never triggers a fresh scrape. The value is in milliseconds and specifies the minimum age the cached data must be. If matching cached data exists, it is returned instantly. If no cached data is found, a 404 with error code SCRAPE\_NO\_CACHED\_DATA is returned. Set to 1 to accept any cached data regardless of age.

Headers to send with the request. Can be used to send cookies, user-agent, etc.

Specify a delay in milliseconds before fetching the content, allowing the page sufficient time to load. This waiting time is in addition to Firecrawl's smart wait feature.

Set to true if you want to emulate scraping from a mobile device. Useful for testing responsive pages and taking mobile screenshots.

Skip TLS certificate verification when making requests.

Timeout in milliseconds for the request. Minimum is 1000 (1 second). Default is 30000 (30 seconds). Maximum is 300000 (300 seconds).

Required range: `1000 <= x <= 300000`

Controls how files are processed during scraping. When "pdf" is included (default), the PDF content is extracted and converted to markdown format, with billing based on the number of pages (1 credit per page). When an empty array is passed, the PDF file is returned in base64 encoding with a flat rate of 1 credit for the entire PDF.

actions

(Wait by Duration · object | Wait for Element · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

Actions to perform on the page before grabbing the content

- Wait by Duration
- Wait for Element
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

Location settings for the request. When specified, this will use an appropriate proxy if available and emulate the corresponding language and timezone settings. Defaults to 'US' if not specified.

Removes all base 64 images from the markdown output, which may be overwhelmingly long. This does not affect html or rawHtml formats. The image's alt text remains in the output, but the URL is replaced with a placeholder.

Enables ad-blocking and cookie popup blocking.

Specifies the type of proxy to use.

- basic: Proxies for scraping sites with none to basic anti-bot solutions. Fast and usually works.
- enhanced: Enhanced proxies for scraping sites with advanced anti-bot solutions. Slower, but more reliable on certain sites. Costs up to 5 credits per request.
- auto: Firecrawl will automatically retry scraping with enhanced proxies if the basic proxy fails. If the retry with enhanced is successful, 5 credits will be billed for the scrape. If the first attempt with basic is successful, only the regular cost will be billed.

Available options:

`basic`,

`enhanced`,

`auto`

If true, the page will be stored in the Firecrawl index and cache. Setting this to false is useful if your scraping activity may have data protection concerns. Using some parameters associated with sensitive scraping (e.g. actions, headers) will force this parameter to be false.

If true, this will enable zero data retention for this batch scrape. To enable this feature, please contact [help@firecrawl.dev](mailto:help@firecrawl.dev)

#### Response

If ignoreInvalidURLs is true, this is an array containing the invalid URLs that were specified in the request. If there were no invalid URLs, this will be an empty array. If ignoreInvalidURLs is false, this field will be undefined.