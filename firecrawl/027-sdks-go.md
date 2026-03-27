---
title: Go SDK | Firecrawl
url: https://docs.firecrawl.dev/sdks/go
source: sitemap
fetched_at: 2026-03-23T07:21:12.946872-03:00
rendered_js: false
word_count: 268
summary: This document provides instructions for installing and using the Firecrawl Go SDK to scrape, crawl, and map websites. It covers client initialization, method usage for data extraction, and handling API responses.
tags:
    - go-sdk
    - web-scraping
    - web-crawling
    - firecrawl
    - api-integration
    - data-extraction
category: guide
---

## Installation

To install the Firecrawl Go SDK, you can use go get:

```
go get github.com/mendableai/firecrawl-go
```

## Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the `API key` as a parameter to the `FirecrawlApp` struct.
3. Set the `API URL` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `https://api.firecrawl.dev`.
4. Set the `version` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `v1`.

Here’s an example of how to use the SDK with error handling:

```
import (
	"fmt"
	"log"
	"github.com/google/uuid"
	"github.com/mendableai/firecrawl-go"
)

func ptr[T any](v T) *T {
	return &v
}

func main() {
	// Initialize the FirecrawlApp with your API key
	apiKey := "fc-YOUR_API_KEY"
	apiUrl := "https://api.firecrawl.dev"
	version := "v1"

	app, err := firecrawl.NewFirecrawlApp(apiKey, apiUrl, version)
	if err != nil {
		log.Fatalf("Failed to initialize FirecrawlApp: %v", err)
	}

  // Scrape a website
  scrapeStatus, err := app.ScrapeUrl("https://firecrawl.dev", firecrawl.ScrapeParams{
    Formats: []string{"markdown", "html"},
  })
  if err != nil {
    log.Fatalf("Failed to send scrape request: %v", err)
  }

  fmt.Println(scrapeStatus)

	// Crawl a website
  idempotencyKey := uuid.New().String() // optional idempotency key
  crawlParams := &firecrawl.CrawlParams{
		ExcludePaths: []string{"blog/*"},
		MaxDepth:     ptr(2),
	}

	crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", crawlParams, &idempotencyKey)
	if err != nil {
		log.Fatalf("Failed to send crawl request: %v", err)
	}

	fmt.Println(crawlStatus) 
}
```

### Scraping a URL

To scrape a single URL with error handling, use the `ScrapeURL` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```
// Scrape a website
scrapeResult, err := app.ScrapeUrl("https://firecrawl.dev", map[string]any{
  "formats": []string{"markdown", "html"},
})
if err != nil {
  log.Fatalf("Failed to scrape URL: %v", err)
}

fmt.Println(scrapeResult)
```

### Crawling a Website

To crawl a website, use the `CrawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

```
crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", map[string]any{
  "limit": 100,
  "scrapeOptions": map[string]any{
    "formats": []string{"markdown", "html"},
  },
})
if err != nil {
  log.Fatalf("Failed to send crawl request: %v", err)
}

fmt.Println(crawlStatus) 
```

### Checking Crawl Status

To check the status of a crawl job, use the `CheckCrawlStatus` method. It takes the job ID as a parameter and returns the current status of the crawl job.

```
// Get crawl status
crawlStatus, err := app.CheckCrawlStatus("<crawl_id>")

if err != nil {
  log.Fatalf("Failed to get crawl status: %v", err)
}

fmt.Println(crawlStatus)
```

### Map a Website

Use `MapUrl` to generate a list of URLs from a website. The `params` argument let you customize the mapping process, including options to exclude subdomains or to utilize the sitemap.

```
// Map a website
mapResult, err := app.MapUrl("https://firecrawl.dev", nil)
if err != nil {
  log.Fatalf("Failed to map URL: %v", err)
}

fmt.Println(mapResult)
```

## Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.