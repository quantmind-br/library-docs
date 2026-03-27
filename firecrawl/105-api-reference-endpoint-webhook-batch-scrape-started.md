---
title: Batch Scrape Started - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/webhook-batch-scrape-started
source: sitemap
fetched_at: 2026-03-23T07:19:15.789799-03:00
rendered_js: false
word_count: 76
summary: This document specifies the structure, security requirements, and expected response format for handling webhook notifications from the batch scraping service.
tags:
    - webhook
    - hmac-sha256
    - data-delivery
    - api-integration
    - security-verification
category: reference
---

#### Headers

HMAC-SHA256 signature of the raw request body, formatted as `sha256=<hex>`. Present when an HMAC secret is configured in your [account settings](https://www.firecrawl.dev/app/settings?tab=advanced). See [Webhook Security](https://docs.firecrawl.dev/webhooks/security) for verification details.

Example:

`"sha256=abc123def456789..."`

#### Body

Allowed value: `"batch_scrape.started"`

The batch scrape job ID, matching the `id` returned by `POST /batch/scrape`.

Unique identifier for this webhook delivery.

The custom metadata object you provided in the webhook configuration. Echoed back in every delivery.

#### Response

Return any `2xx` status code to acknowledge receipt.