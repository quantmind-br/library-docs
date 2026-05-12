---
title: Webhook Event Types | Firecrawl
url: https://docs.firecrawl.dev/webhooks/events
source: sitemap
fetched_at: 2026-03-23T07:28:21.236479-03:00
rendered_js: false
word_count: 303
summary: This document provides a comprehensive reference for webhook event types and their JSON payload structures used to monitor crawl, scrape, extraction, and agent job lifecycles.
tags:
    - webhooks
    - api-reference
    - event-notifications
    - data-scraping
    - automation-jobs
category: api
---

## Quick Reference

EventTrigger`crawl.started`Crawl job begins processing`crawl.page`A page is scraped during a crawl`crawl.completed`Crawl job finishes and all pages have been processed`batch_scrape.started`Batch scrape job begins processing`batch_scrape.page`A URL is scraped during a batch scrape`batch_scrape.completed`All URLs in the batch have been processed`extract.started`Extract job begins processing`extract.completed`Extraction finishes successfully`extract.failed`Extraction fails`agent.started`Agent job begins processing`agent.action`Agent executes a tool (scrape, search, etc.)`agent.completed`Agent finishes successfully`agent.failed`Agent encounters an error`agent.cancelled`Agent job is cancelled by the user

## Payload Structure

All webhook events share this structure:

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [...],
  "metadata": {}
}
```

FieldTypeDescription`success`booleanWhether the operation succeeded`type`stringEvent type (e.g. `crawl.page`)`id`stringJob ID`data`arrayEvent-specific data (see examples below)`metadata`objectCustom metadata from your webhook config`error`stringError message (when `success` is `false`)

## Crawl Events

### `crawl.started`

Sent when the crawl job begins processing.

```
{
  "success": true,
  "type": "crawl.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `crawl.page`

Sent for each page scraped. The `data` array contains the page content and metadata.

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Page content...",
      "metadata": {
        "title": "Page Title",
        "description": "Page description",
        "url": "https://example.com/page",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com/page",
        "proxyUsed": "basic",
        "cacheState": "hit",
        "cachedAt": "2025-09-03T21:11:25.636Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

### `crawl.completed`

Sent when the crawl job finishes and all pages have been processed.

```
{
  "success": true,
  "type": "crawl.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

## Batch Scrape Events

### `batch_scrape.started`

Sent when the batch scrape job begins processing.

```
{
  "success": true,
  "type": "batch_scrape.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `batch_scrape.page`

Sent for each URL scraped. The `data` array contains the page content and metadata.

```
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Page content...",
      "metadata": {
        "title": "Page Title",
        "description": "Page description",
        "url": "https://example.com",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com",
        "proxyUsed": "basic",
        "cacheState": "miss",
        "cachedAt": "2025-09-03T23:30:53.434Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

### `batch_scrape.completed`

Sent when all URLs in the batch have been processed.

```
{
  "success": true,
  "type": "batch_scrape.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

Sent when the extract job begins processing.

```
{
  "success": true,
  "type": "extract.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

Sent when extraction finishes successfully. The `data` array contains the extracted data and usage info.

```
{
  "success": true,
  "type": "extract.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "success": true,
      "data": { "siteName": "Example Site", "category": "Technology" },
      "extractId": "550e8400-e29b-41d4-a716-446655440000",
      "llmUsage": 0.0020118,
      "totalUrlsScraped": 1,
      "sources": {
        "siteName": ["https://example.com"],
        "category": ["https://example.com"]
      }
    }
  ],
  "metadata": {}
}
```

Sent when extraction fails. The `error` field contains the failure reason.

```
{
  "success": false,
  "type": "extract.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "error": "Failed to extract data: timeout exceeded",
  "metadata": {}
}
```

## Agent Events

### `agent.started`

Sent when the agent job begins processing.

```
{
  "success": true,
  "type": "agent.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `agent.action`

Sent after each tool execution (scrape, search, etc.).

```
{
  "success": true,
  "type": "agent.action",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 5,
      "action": "mcp__tools__scrape",
      "input": {
        "url": "https://example.com"
      }
    }
  ],
  "metadata": {}
}
```

### `agent.completed`

Sent when the agent finishes successfully. The `data` array contains the extracted data and total credits used.

```
{
  "success": true,
  "type": "agent.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 15,
      "data": {
        "company": "Example Corp",
        "industry": "Technology",
        "founded": 2020
      }
    }
  ],
  "metadata": {}
}
```

### `agent.failed`

Sent when the agent encounters an error. The `error` field contains the failure reason.

```
{
  "success": false,
  "type": "agent.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 8
    }
  ],
  "error": "Max credits exceeded",
  "metadata": {}
}
```

### `agent.cancelled`

Sent when the agent job is cancelled by the user.

```
{
  "success": false,
  "type": "agent.cancelled",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 3
    }
  ],
  "metadata": {}
}
```

## Event Filtering

By default, you receive all events. To subscribe to specific events only, use the `events` array in your webhook config:

```
{
  "url": "https://your-app.com/webhook",
  "events": ["completed", "failed"]
}
```

This is useful if you only care about job completion and don’t need per-page updates.