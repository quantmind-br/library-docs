---
title: Agent Action - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/webhook-agent-action
source: sitemap
fetched_at: 2026-03-23T07:19:14.496001-03:00
rendered_js: false
word_count: 73
summary: This document specifies the structure and security requirements for handling incoming webhook events, including header signatures and payload schema.
tags:
    - webhook-delivery
    - hmac-security
    - api-integration
    - request-payload
    - event-notification
category: reference
---

#### Headers

HMAC-SHA256 signature of the raw request body, formatted as `sha256=<hex>`. Present when an HMAC secret is configured in your [account settings](https://www.firecrawl.dev/app/settings?tab=advanced). See [Webhook Security](https://docs.firecrawl.dev/webhooks/security) for verification details.

Example:

`"sha256=abc123def456789..."`

#### Body

Allowed value: `"agent.action"`

Unique identifier for this webhook delivery.

Array with a single object describing the action taken.

The custom metadata object you provided in the webhook configuration. Echoed back in every delivery.

#### Response

Return any `2xx` status code to acknowledge receipt.