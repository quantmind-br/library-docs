---
title: Crawl | Firecrawl
url: https://docs.firecrawl.dev/features/crawl
source: sitemap
fetched_at: 2026-03-23T07:24:42.208337-03:00
rendered_js: false
word_count: 890
summary: This document explains how to use the Firecrawl API to recursively discover and scrape content across websites, including configuration options for webhooks, path filtering, and job management.
tags:
    - web-scraping
    - api-reference
    - crawling
    - data-extraction
    - automation
    - webhook-integration
    - recursive-scraping
category: api
---

Crawl submits a URL to Firecrawl and recursively discovers and scrapes every reachable subpage. It handles sitemaps, JavaScript rendering, and rate limits automatically, returning clean markdown or structured data for each page.

- Discovers pages via sitemap and recursive link traversal
- Supports path filtering, depth limits, and subdomain/external link control
- Returns results via polling, WebSocket, or webhook

## Installation

## Basic usage

Submit a crawl job by calling `POST /v2/crawl` with a starting URL. The endpoint returns a job ID that you use to poll for results.

### Scrape options

All options from the [Scrape endpoint](https://docs.firecrawl.dev/api-reference/endpoint/scrape) are available in crawl via `scrapeOptions` (JS) / `scrape_options` (Python). These apply to every page the crawler scrapes, including formats, proxy, caching, actions, location, and tags.

## Checking crawl status

Use the job ID to poll for the crawl status and retrieve results.

### Response handling

The response varies based on the crawl’s status. For incomplete or large responses exceeding 10MB, a `next` URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the `next` parameter is absent, it indicates the end of the crawl data.

## SDK methods

There are two ways to use crawl with the SDK.

### Crawl and wait

The `crawl` method waits for the crawl to complete and returns the full response. It handles pagination automatically. This is recommended for most use cases.

The response includes the crawl status and all scraped data:

### Start and check later

The `startCrawl` / `start_crawl` method returns immediately with a crawl ID. You then poll for status manually. This is useful for long-running crawls or custom polling logic.

The initial response returns the job ID:

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

## Real-time results with WebSocket

The watcher method provides real-time updates as pages are crawled. Start a crawl, then subscribe to events for immediate data processing.

## Webhooks

You can configure webhooks to receive real-time notifications as your crawl progresses. This allows you to process pages as they are scraped instead of waiting for the entire crawl to complete.

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### Event types

EventDescription`crawl.started`Fires when the crawl begins`crawl.page`Fires for each page successfully scraped`crawl.completed`Fires when the crawl finishes`crawl.failed`Fires if the crawl encounters an error

### Payload

```
{
  "success": true,
  "type": "crawl.page",
  "id": "crawl-job-id",
  "data": [...], // Page data for 'page' events
  "metadata": {}, // Your custom metadata
  "error": null
}
```

### Verifying webhook signatures

Every webhook request from Firecrawl includes an `X-Firecrawl-Signature` header containing an HMAC-SHA256 signature. Always verify this signature to ensure the webhook is authentic and has not been tampered with.

1. Get your webhook secret from the [Advanced tab](https://www.firecrawl.dev/app/settings?tab=advanced) of your account settings
2. Extract the signature from the `X-Firecrawl-Signature` header
3. Compute HMAC-SHA256 of the raw request body using your secret
4. Compare with the signature header using a timing-safe function

For complete implementation examples in JavaScript and Python, see the [Webhook Security documentation](https://docs.firecrawl.dev/webhooks/security). For comprehensive webhook documentation including detailed event payloads, payload structure, advanced configuration, and troubleshooting, see the [Webhooks documentation](https://docs.firecrawl.dev/webhooks/overview).

## Configuration reference

The full set of parameters available when submitting a crawl job:

ParameterTypeDefaultDescription`url``string`(required)The starting URL to crawl from`limit``integer``10000`Maximum number of pages to crawl`maxDiscoveryDepth``integer`(none)Maximum depth from the root URL based on link-discovery hops, not the number of `/` segments in the URL. Each time a new URL is found on a page, it is assigned a depth one higher than the page it was discovered on. The root site and sitemapped pages have a discovery depth of 0. Pages at the max depth are still scraped, but links on them are not followed.`includePaths``string[]`(none)URL pathname regex patterns to include. Only matching paths are crawled.`excludePaths``string[]`(none)URL pathname regex patterns to exclude from the crawl`regexOnFullURL``boolean``false`Match `includePaths`/`excludePaths` against the full URL (including query parameters) instead of just the pathname`crawlEntireDomain``boolean``false`Follow internal links to sibling or parent URLs, not just child paths`allowSubdomains``boolean``false`Follow links to subdomains of the main domain`allowExternalLinks``boolean``false`Follow links to external websites`sitemap``string``"include"`Sitemap handling: `"include"` (default), `"skip"`, or `"only"``ignoreQueryParameters``boolean``false`Avoid re-scraping the same path with different query parameters`delay``number`(none)Delay in seconds between scrapes to respect rate limits`maxConcurrency``integer`(none)Maximum concurrent scrapes. Defaults to your team’s concurrency limit.`scrapeOptions``object`(none)Options applied to every scraped page (formats, proxy, caching, actions, etc.)`webhook``object`(none)Webhook configuration for real-time notifications`prompt``string`(none)Natural language prompt to generate crawl options. Explicitly set parameters override generated equivalents.

## Important details

- **Sitemap discovery**: By default, the crawler includes the website’s sitemap to discover URLs (`sitemap: "include"`). If you set `sitemap: "skip"`, only pages reachable through HTML links from the root URL are found. Assets like PDFs or deeply nested pages listed in the sitemap but not directly linked from HTML will be missed. For maximum coverage, keep the default setting.
- **Credit usage**: Each page crawled costs 1 credit. JSON mode adds 4 credits per page, enhanced proxy adds 4 credits per page, and PDF parsing costs 1 credit per PDF page.
- **Result expiration**: Job results are available via the API for 24 hours after completion. After that, view results in the [activity logs](https://www.firecrawl.dev/app/logs).
- **Crawl errors**: The `data` array contains pages Firecrawl successfully scraped. Use the [Get Crawl Errors](https://docs.firecrawl.dev/api-reference/endpoint/crawl-get-errors) endpoint to retrieve pages that failed due to network errors, timeouts, or robots.txt blocks.
- **Non-deterministic results**: Crawl results may vary between runs of the same configuration. Pages are scraped concurrently, so the order in which links are discovered depends on network timing and which pages finish loading first. This means different branches of a site may be explored to different extents near the depth boundary, especially at higher `maxDiscoveryDepth` values. To get more deterministic results, set `maxConcurrency` to `1` or use `sitemap: "only"` if the site has a comprehensive sitemap.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.