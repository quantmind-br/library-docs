---
title: Advanced Scraping Guide | Firecrawl
url: https://docs.firecrawl.dev/advanced-scraping-guide
source: sitemap
fetched_at: 2026-03-23T07:27:58.409231-03:00
rendered_js: false
word_count: 1278
summary: This document provides a comprehensive reference for configuring Firecrawl's scrape endpoints, including options for content formatting, PDF parsing, content filtering, timing, and browser automation actions.
tags:
    - firecrawl
    - web-scraping
    - api-reference
    - pdf-parsing
    - browser-automation
    - data-extraction
category: reference
---

Reference for every option across Firecrawl’s scrape, crawl, map, and agent endpoints.

## Basic scraping

To scrape a single page and get clean markdown content, use the `/scrape` endpoint.

## Scraping PDFs

Firecrawl supports PDFs. Use the `parsers` option (e.g., `parsers: ["pdf"]`) when you want to ensure PDF parsing. You can control the parsing strategy with the `mode` option:

- **`auto`** (default) — attempts fast text-based extraction first, then falls back to OCR if needed.
- **`fast`** — text-based parsing only (embedded text). Fastest, but skips scanned/image-heavy pages.
- **`ocr`** — forces OCR parsing on every page. Use for scanned documents or when `auto` misclassifies a page.

`{ type: "pdf" }` and `"pdf"` both default to `mode: "auto"`.

```
"parsers": [{ "type": "pdf", "mode": "fast", "maxPages": 50 }]
```

## Scrape options

When using the `/scrape` endpoint, you can customize the request with the following options.

### Formats (`formats`)

The `formats` array controls which output types the scraper returns. Default: `["markdown"]`. **String formats**: pass the name directly (e.g. `"markdown"`).

FormatDescription`markdown`Page content converted to clean Markdown.`html`Processed HTML with unnecessary elements removed.`rawHtml`Original HTML exactly as returned by the server.`links`All links found on the page.`images`All images found on the page.`summary`An LLM-generated summary of the page content.`branding`Extracts brand identity (colors, fonts, typography, spacing, UI components).

**Object formats**: pass an object with `type` and additional options.

FormatOptionsDescription`json``prompt?: string`, `schema?: object`Extract structured data using an LLM. Provide a JSON schema and/or a natural-language prompt (max 10,000 characters).`screenshot``fullPage?: boolean`, `quality?: number`, `viewport?: { width, height }`Capture a screenshot. Max one per request. Viewport max resolution is 7680×4320. Screenshot URLs expire after 24 hours.`changeTracking``modes?: ("json" | "git-diff")[]`, `tag?: string`, `schema?: object`, `prompt?: string`Track changes between scrapes. Requires `"markdown"` to also be in the formats array.`attributes``selectors: [{ selector: string, attribute: string }]`Extract specific HTML attributes from elements matching CSS selectors.

### Content filtering

These parameters control which parts of the page appear in the output. `onlyMainContent` runs first to strip boilerplate (nav, footer, etc.), then `includeTags` and `excludeTags` further narrow the result. If you set `onlyMainContent: false`, the full page HTML is used as the starting point for tag filtering.

ParameterTypeDefaultDescription`onlyMainContent``boolean``true`Return only the main content. Set `false` for the full page.`includeTags``array`—HTML tags, classes, or IDs to include (e.g. `["h1", "p", ".main-content"]`).`excludeTags``array`—HTML tags, classes, or IDs to exclude (e.g. `["#ad", "#footer"]`).

### Timing and cache

ParameterTypeDefaultDescription`waitFor``integer` (ms)`0`Extra wait time before scraping, on top of smart-wait. Use sparingly.`maxAge``integer` (ms)`172800000`Return a cached version if fresher than this value (default is 2 days). Set `0` to always fetch fresh.`timeout``integer` (ms)`30000`Max request duration before aborting (default is 30 seconds). Minimum is 1000 (1 second).

### PDF parsing

ParameterTypeDefaultDescription`parsers``array``["pdf"]`Controls PDF processing. `[]` to skip parsing and return base64 (1 credit flat).

```
{ "type": "pdf", "mode": "fast" | "auto" | "ocr", "maxPages": 10 }
```

PropertyTypeDefaultDescription`type``"pdf"`*(required)*Parser type.`mode``"fast" | "auto" | "ocr"``"auto"``fast`: text-based extraction only. `auto`: fast with OCR fallback. `ocr`: force OCR.`maxPages``integer`—Cap the number of pages to parse.

### Actions

Run browser actions before scraping. This is useful for dynamic content, navigation, or user-gated pages. You can include up to 50 actions per request, and the combined wait time across all `wait` actions and `waitFor` must not exceed 60 seconds.

ActionParametersDescription`wait``milliseconds?: number`, `selector?: string`Wait for a fixed duration **or** until an element is visible (provide one, not both). When using `selector`, times out after 30 seconds.`click``selector: string`, `all?: boolean`Click an element matching the CSS selector. Set `all: true` to click every match.`write``text: string`Type text into the currently focused field. You must focus the element with a `click` action first.`press``key: string`Press a keyboard key (e.g. `"Enter"`, `"Tab"`, `"Escape"`).`scroll``direction?: "up" | "down"`, `selector?: string`Scroll the page or a specific element. Direction defaults to `"down"`.`screenshot``fullPage?: boolean`, `quality?: number`, `viewport?: { width, height }`Capture a screenshot. Max viewport resolution is 7680×4320.`scrape`*(none)*Capture the current page HTML at this point in the action sequence.`executeJavascript``script: string`Run JavaScript code in the page. Returns `{ type, value }`.`pdf``format?: string`, `landscape?: boolean`, `scale?: number`Generate a PDF. Supported formats: `"A0"` through `"A6"`, `"Letter"`, `"Legal"`, `"Tabloid"`, `"Ledger"`. Defaults to `"Letter"`.

#### Action execution notes

- **Write** requires a preceding `click` to focus the target element.
- **Scroll** accepts an optional `selector` to scroll a specific element instead of the page.
- **Wait** accepts either `milliseconds` (fixed delay) or `selector` (wait until visible).
- Actions run **sequentially**: each step completes before the next begins.
- Actions are **not supported for PDFs**. If the URL resolves to a PDF the request will fail.

#### Advanced action examples

**Taking a screenshot:**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "click", "selector": "#load-more" },
      { "type": "wait", "milliseconds": 1000 },
      { "type": "screenshot", "fullPage": true, "quality": 80 }
    ]
  }'
```

**Clicking multiple elements:**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "click", "selector": ".expand-button", "all": true },
      { "type": "wait", "milliseconds": 500 }
    ],
    "formats": ["markdown"]
  }'
```

**Generating a PDF:**

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://example.com",
    "actions": [
      { "type": "pdf", "format": "A4", "landscape": false }
    ]
  }'
```

### Full scrape example

The following request combines multiple scrape options:

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "formats": [
        "markdown",
        "links",
        "html",
        "rawHtml",
        { "type": "screenshot", "fullPage": true, "quality": 80 }
      ],
      "includeTags": ["h1", "p", "a", ".main-content"],
      "excludeTags": ["#ad", "#footer"],
      "onlyMainContent": false,
      "waitFor": 1000,
      "timeout": 15000,
      "parsers": ["pdf"]
    }'
```

This request returns markdown, HTML, raw HTML, links, and a full-page screenshot. It scopes content to `<h1>`, `<p>`, `<a>`, and `.main-content` while excluding `#ad` and `#footer`, waits 1 second before scraping, sets a 15 second timeout, and enables PDF parsing. See the full [Scrape API reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape) for details.

Use the JSON format object in `formats` to extract structured data in one pass:

## Agent endpoint

Use the `/v2/agent` endpoint for autonomous, multi-page data extraction. The agent runs asynchronously: you start a job, then poll for results.

### Agent options

ParameterTypeDefaultDescription`prompt``string`*(required)*Natural-language instructions describing what data to extract (max 10,000 characters).`urls``array`—URLs to constrain the agent to.`schema``object`—JSON schema to structure the extracted data.`maxCredits``number``2500`Maximum credits the agent can spend. The dashboard supports up to 2,500; for higher limits, set this via the API (values above 2,500 are always billed as paid requests).`strictConstrainToURLs``boolean``false`When `true`, the agent only visits the provided URLs.`model``string``"spark-1-mini"`AI model to use. `"spark-1-mini"` (default, 60% cheaper) or `"spark-1-pro"` (higher accuracy).

### Check agent status

Poll `GET /v2/agent/{jobId}` to check progress. The response `status` field will be `"processing"`, `"completed"`, or `"failed"`.

```
curl -X GET https://api.firecrawl.dev/v2/agent/YOUR-JOB-ID \
  -H 'Authorization: Bearer fc-YOUR-API-KEY'
```

The Python and Node SDKs also provide a convenience method (`firecrawl.agent()`) that starts the job and polls automatically until completion.

## Crawling multiple pages

To crawl multiple pages, use the `/v2/crawl` endpoint. The crawl runs asynchronously and returns a job ID. Use the `limit` parameter to control how many pages are crawled. If omitted, the crawl will process up to 10,000 pages.

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 10
    }'
```

### Response

```
{ "id": "1234-5678-9101" }
```

### Check crawl job

Use the job ID to check the status of a crawl and retrieve its results.

```
curl -X GET https://api.firecrawl.dev/v2/crawl/1234-5678-9101 \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY'
```

If the content is larger than 10MB or the crawl job is still running, the response may include a `next` parameter, a URL to the next page of results.

### Crawl prompt and params preview

You can provide a natural-language `prompt` to let Firecrawl derive crawl settings. Preview them first:

```
curl -X POST https://api.firecrawl.dev/v2/crawl/params-preview \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://docs.firecrawl.dev",
    "prompt": "Extract docs and blog"
  }'
```

### Crawler options

When using the `/v2/crawl` endpoint, you can customize crawling behavior with the following options.

#### Path filtering

ParameterTypeDefaultDescription`includePaths``array`—Regex patterns for URLs to include (pathname only by default).`excludePaths``array`—Regex patterns for URLs to exclude (pathname only by default).`regexOnFullURL``boolean``false`Match patterns against the full URL instead of just the pathname.

#### Crawl scope

ParameterTypeDefaultDescription`maxDiscoveryDepth``integer`—Max link-depth for discovering new URLs.`limit``integer``10000`Max pages to crawl.`crawlEntireDomain``boolean``false`Explore siblings and parents to cover the entire domain.`allowExternalLinks``boolean``false`Follow links to external domains.`allowSubdomains``boolean``false`Follow subdomains of the main domain.`delay``number` (s)—Delay between scrapes.

#### Sitemap and deduplication

ParameterTypeDefaultDescription`sitemap``string``"include"``"include"`: use sitemap + link discovery. `"skip"`: ignore sitemap. `"only"`: crawl only sitemap URLs.`deduplicateSimilarURLs``boolean``true`Normalize URL variants (`www.`, `https`, trailing slashes, `index.html`) as duplicates.`ignoreQueryParameters``boolean``false`Strip query strings before deduplication (e.g. `/page?a=1` and `/page?a=2` become one URL).

#### Scrape options for crawl

ParameterTypeDefaultDescription`scrapeOptions``object``{ formats: ["markdown"] }`Per-page scrape config. Accepts all [scrape options](#scrape-options) above.

### Crawl example

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "includePaths": ["^/blog/.*$", "^/docs/.*$"],
      "excludePaths": ["^/admin/.*$", "^/private/.*$"],
      "maxDiscoveryDepth": 2,
      "limit": 1000
    }'
```

## Mapping website links

The `/v2/map` endpoint identifies URLs related to a given website.

```
curl -X POST https://api.firecrawl.dev/v2/map \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'
```

### Map options

ParameterTypeDefaultDescription`search``string`—Filter links by text match.`limit``integer``100`Max links to return.`sitemap``string``"include"``"include"`, `"skip"`, or `"only"`.`includeSubdomains``boolean``true`Include subdomains.

Here is the API Reference for it: [Map Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/map)

## Whitelisting Firecrawl

### Allowing Firecrawl to scrape your website

- **User Agent**: Allow `FirecrawlAgent` in your firewall or security rules.
- **IP addresses**: Firecrawl does not use a fixed set of outbound IPs.

### Allowing your application to call the Firecrawl API

If your firewall blocks outbound requests from your application to external services, you need to whitelist Firecrawl’s API server IP address so your application can reach the Firecrawl API (`api.firecrawl.dev`):

- **IP Address**: `35.245.250.27`

Add this IP to your firewall’s outbound allowlist so your backend can send scrape, crawl, map, and agent requests to Firecrawl.