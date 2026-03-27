---
title: Webhook Security | Firecrawl
url: https://docs.firecrawl.dev/webhooks/security
source: sitemap
fetched_at: 2026-03-23T07:37:15.352275-03:00
rendered_js: false
word_count: 132
summary: This document explains how to verify the authenticity of webhook requests from Firecrawl using HMAC-SHA256 signature validation.
tags:
    - webhook-security
    - hmac-sha256
    - signature-verification
    - data-integrity
    - security-best-practices
category: guide
---

Firecrawl signs every webhook request using HMAC-SHA256. Verifying signatures ensures requests are authentic and haven’t been tampered with.

## Secret Key

Your webhook secret is available in the [Advanced tab](https://www.firecrawl.dev/app/settings?tab=advanced) of your account settings. Each account has a unique secret used to sign all webhook requests.

## Signature Verification

Each webhook request includes an `X-Firecrawl-Signature` header:

```
X-Firecrawl-Signature: sha256=abc123def456...
```

### How to Verify

1. Extract the signature from the `X-Firecrawl-Signature` header
2. Get the raw request body (before parsing)
3. Compute HMAC-SHA256 using your secret key
4. Compare signatures using a timing-safe function

### Implementation

## Best Practices

### Always Verify Signatures

Never process a webhook without verifying its signature first:

```
app.post('/webhook', (req, res) => {
  if (!verifySignature(req)) {
    return res.status(401).send('Unauthorized');
  }
  processWebhook(req.body);
  res.status(200).send('OK');
});
```

### Use Timing-Safe Comparisons

Standard string comparison can leak timing information. Use `crypto.timingSafeEqual()` in Node.js or `hmac.compare_digest()` in Python.

### Use HTTPS

Always use HTTPS for your webhook endpoint to ensure payloads are encrypted in transit.