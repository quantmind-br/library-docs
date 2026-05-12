---
title: Agent Completed - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/webhook-agent-completed
source: sitemap
fetched_at: 2026-03-23T07:19:05.358427-03:00
rendered_js: false
word_count: 64
summary: This document specifies the structure and security requirements for webhook events, including header authentication via HMAC-SHA256 and expected response codes.
tags:
    - webhook-security
    - hmac-sha256
    - data-delivery
    - api-integration
    - event-notifications
category: reference
---

#### Headers

HMAC-SHA256 signature of the raw request body, formatted as `sha256=<hex>`. Present when an HMAC secret is configured in your [account settings](https://www.firecrawl.dev/app/settings?tab=advanced). See [Webhook Security](https://docs.firecrawl.dev/webhooks/security) for verification details.

Example:

`"sha256=abc123def456789..."`

#### Body

Allowed value: `"agent.completed"`

Unique identifier for this webhook delivery.

The custom metadata object you provided in the webhook configuration. Echoed back in every delivery.

#### Response

Return any `2xx` status code to acknowledge receipt.