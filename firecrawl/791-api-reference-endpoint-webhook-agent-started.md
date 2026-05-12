---
title: Agent Started - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/webhook-agent-started
source: sitemap
fetched_at: 2026-03-23T07:19:11.781112-03:00
rendered_js: false
word_count: 75
summary: This document specifies the structure and security verification requirements for receiving and acknowledging webhook event notifications.
tags:
    - webhook-security
    - hmac-signature
    - event-delivery
    - data-payload
    - api-integration
category: reference
---

#### Headers

HMAC-SHA256 signature of the raw request body, formatted as `sha256=<hex>`. Present when an HMAC secret is configured in your [account settings](https://www.firecrawl.dev/app/settings?tab=advanced). See [Webhook Security](https://docs.firecrawl.dev/webhooks/security) for verification details.

Example:

`"sha256=abc123def456789..."`

#### Body

Allowed value: `"agent.started"`

The agent job ID, matching the `id` returned by `POST /agent`.

Unique identifier for this webhook delivery.

The custom metadata object you provided in the webhook configuration. Echoed back in every delivery.

#### Response

Return any `2xx` status code to acknowledge receipt.