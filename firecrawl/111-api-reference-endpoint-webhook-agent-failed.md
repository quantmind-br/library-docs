---
title: Agent Failed - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/webhook-agent-failed
source: sitemap
fetched_at: 2026-03-23T07:19:04.309794-03:00
rendered_js: false
word_count: 75
summary: This document outlines the expected headers, body parameters, and response requirements for webhook deliveries related to failed agent events.
tags:
    - webhooks
    - api-integration
    - security-headers
    - event-notifications
    - error-handling
    - payload-structure
category: api
---

#### Headers

HMAC-SHA256 signature of the raw request body, formatted as `sha256=<hex>`. Present when an HMAC secret is configured in your [account settings](https://www.firecrawl.dev/app/settings?tab=advanced). See [Webhook Security](https://docs.firecrawl.dev/webhooks/security) for verification details.

Example:

`"sha256=abc123def456789..."`

#### Body

Always `false` for this event.

Allowed value: `"agent.failed"`

Unique identifier for this webhook delivery.

Human-readable error message describing the failure.

The custom metadata object you provided in the webhook configuration. Echoed back in every delivery.

#### Response

Return any `2xx` status code to acknowledge receipt.