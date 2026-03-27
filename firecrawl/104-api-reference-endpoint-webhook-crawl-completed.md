---
title: Crawl Completed - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/webhook-crawl-completed
source: sitemap
fetched_at: 2026-03-23T07:19:07.81662-03:00
rendered_js: false
word_count: 79
summary: This document outlines the structure and expected response for webhook event deliveries, including security signature verification and payload fields.
tags:
    - webhook-delivery
    - security-headers
    - event-payload
    - api-integration
    - hmac-verification
category: api
---

#### Headers

HMAC-SHA256 signature of the raw request body, formatted as `sha256=<hex>`. Present when an HMAC secret is configured in your [account settings](https://www.firecrawl.dev/app/settings?tab=advanced). See [Webhook Security](https://docs.firecrawl.dev/webhooks/security) for verification details.

Example:

`"sha256=abc123def456789..."`

#### Body

Always `true` for this event.

The event type.

Allowed value: `"crawl.completed"`

Unique identifier for this webhook delivery.

Empty array. Retrieve results via `GET /crawl/{id}`.

The custom metadata object you provided in the webhook configuration. Echoed back in every delivery.

#### Response

Return any `2xx` status code to acknowledge receipt.