---
title: Scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/scrape
source: sitemap
fetched_at: 2026-03-23T07:18:22.878941-03:00
rendered_js: false
word_count: 578
summary: This document provides the API specifications and request parameters for scraping web pages, including support for LLM data extraction, proxy configuration, and advanced content formatting.
tags:
    - web-scraping
    - api-documentation
    - data-extraction
    - proxy-configuration
    - content-formatting
category: api
---

Scrape a single URL and optionally extract information using an LLM

> Note: A new [v2 version of this API](https://docs.firecrawl.dev/api-reference/endpoint/scrape) is now available with improved features and performance.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

Only return the main content of the page excluding headers, navs, footers, etc.

Tags to include in the output.

Tags to exclude from the output.

Returns a cached version of the page if it is younger than this age in milliseconds. If a cached version of the page is older than this value, the page will be scraped. If you do not need extremely fresh data, enabling this can speed up your scrapes by 500%. Defaults to 0, which disables caching.

Headers to send with the request. Can be used to send cookies, user-agent, etc.

Specify a delay in milliseconds before fetching the content, allowing the page sufficient time to load.

Set to true if you want to emulate scraping from a mobile device. Useful for testing responsive pages and taking mobile screenshots.

Skip TLS certificate verification when making requests

Timeout in milliseconds for the request

Controls how PDF files are processed during scraping. When true, the PDF content is extracted and converted to markdown format, with billing based on the number of pages (1 credit per page). When false, the PDF file is returned in base64 encoding with a flat rate of 1 credit total.

actions

(Wait · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

Actions to perform on the page before grabbing the content

- Wait
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

Location settings for the request. When specified, this will use an appropriate proxy if available and emulate the corresponding language and timezone settings. Defaults to 'US' if not specified.

Removes all base 64 images from the output, which may be overwhelmingly long. The image's alt text remains in the output, but the URL is replaced with a placeholder.

Enables ad-blocking and cookie popup blocking.

Specifies the type of proxy to use.

- basic: Proxies for scraping sites with none to basic anti-bot solutions. Fast and usually works.
- enhanced: Enhanced proxies for scraping sites with advanced anti-bot solutions. Slower, but more reliable on certain sites. Costs up to 5 credits per request.
- auto: Firecrawl will automatically retry scraping with enhanced proxies if the basic proxy fails. If the retry with enhanced is successful, 5 credits will be billed for the scrape. If the first attempt with basic is successful, only the regular cost will be billed.

If you do not specify a proxy, Firecrawl will default to basic.

Available options:

`basic`,

`enhanced`,

`auto`

If true, the page will be stored in the Firecrawl index and cache. Setting this to false is useful if your scraping activity may have data protection concerns. Using some parameters associated with sensitive scraping (actions, headers) will force this parameter to be false.

Formats to include in the output.

Available options:

`markdown`,

`html`,

`rawHtml`,

`links`,

`screenshot`,

`screenshot@fullPage`,

`json`,

`changeTracking`

Options for change tracking (Beta). Only applicable when 'changeTracking' is included in formats. The 'markdown' format must also be specified when using change tracking.

If true, this will enable zero data retention for this scrape. To enable this feature, please contact [help@firecrawl.dev](mailto:help@firecrawl.dev)

#### Response