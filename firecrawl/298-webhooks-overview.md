---
title: Webhooks | Firecrawl
url: https://docs.firecrawl.dev/webhooks/overview
source: sitemap
fetched_at: 2026-03-23T07:37:19.565498-03:00
rendered_js: false
word_count: 108
summary: This document describes how to configure and utilize webhooks to receive real-time notifications for operations like crawling and scraping.
tags:
    - webhooks
    - api-integration
    - real-time-notifications
    - data-scraping
    - event-driven
    - web-services
category: configuration
---

Webhooks let you receive real-time notifications as your operations progress, instead of polling for status.

## Supported Operations

OperationEventsCrawl`started`, `page`, `completed`Batch Scrape`started`, `page`, `completed`Extract`started`, `completed`, `failed`Agent`started`, `action`, `completed`, `failed`, `cancelled`

## Configuration

Add a `webhook` object to your request:

```
{
  "webhook": {
    "url": "https://your-domain.com/webhook",
    "metadata": {
      "any_key": "any_value"
    },
    "events": ["started", "page", "completed", "failed"]
  }
} 
```

FieldTypeRequiredDescription`url`stringYesYour endpoint URL (HTTPS)`headers`objectNoCustom headers to include`metadata`objectNoCustom data included in payloads`events`arrayNoEvent types to receive (default: all)

## Usage

### Crawl with Webhook

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

### Batch Scrape with Webhook

```
curl -X POST https://api.firecrawl.dev/v2/batch/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
      ],
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

## Timeouts & Retries

Your endpoint must respond with a `2xx` status within **10 seconds**. If delivery fails (timeout, non-2xx, or network error), Firecrawl retries automatically:

RetryDelay after failure1st1 minute2nd5 minutes3rd15 minutes

After 3 failed retries, the webhook is marked as failed and no further attempts are made.