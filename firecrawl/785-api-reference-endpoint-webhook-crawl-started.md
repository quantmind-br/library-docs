---
title: Crawl Started - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/webhook-crawl-started
source: sitemap
fetched_at: 2026-03-23T07:18:44.48249-03:00
rendered_js: false
word_count: 99
summary: This document defines the schema and security requirements for webhook event notifications, specifically detailing header signatures and payload fields for crawl job status updates.
tags:
    - webhook-delivery
    - hmac-signature
    - event-schema
    - api-integration
    - data-synchronization
category: reference
---

#### Headers

HMAC-SHA256 signature of the raw request body, formatted as `sha256=<hex>`. Present when an HMAC secret is configured in your [account settings](https://www.firecrawl.dev/app/settings?tab=advanced). See [Webhook Security](https://docs.firecrawl.dev/webhooks/security) for verification details.

Example:

`"sha256=abc123def456789..."`

#### Body

Always `true` for this event.

The event type.

Allowed value: `"crawl.started"`

The crawl job ID, matching the `id` returned by `POST /crawl`.

Unique identifier for this webhook delivery. Use for deduplication — the same value is sent on retries.

Empty array for this event.

The custom metadata object you provided in the webhook configuration. Echoed back in every delivery.

#### Response

Return any `2xx` status code to acknowledge receipt.