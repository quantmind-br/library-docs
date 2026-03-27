---
title: Batch Scrape Completed - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/webhook-batch-scrape-completed
source: sitemap
fetched_at: 2026-03-23T07:19:06.453381-03:00
rendered_js: false
word_count: 71
summary: This document outlines the structure and signature requirements for receiving and verifying webhook deliveries from the Firecrawl service.
tags:
    - webhooks
    - api-security
    - hmac-sha256
    - data-delivery
    - event-notification
category: reference
---

#### Headers

HMAC-SHA256 signature of the raw request body, formatted as `sha256=<hex>`. Present when an HMAC secret is configured in your [account settings](https://www.firecrawl.dev/app/settings?tab=advanced). See [Webhook Security](https://docs.firecrawl.dev/webhooks/security) for verification details.

Example:

`"sha256=abc123def456789..."`

#### Body

Allowed value: `"batch_scrape.completed"`

Unique identifier for this webhook delivery.

Empty array. Retrieve results via `GET /batch/scrape/{id}`.

The custom metadata object you provided in the webhook configuration. Echoed back in every delivery.

#### Response

Return any `2xx` status code to acknowledge receipt.