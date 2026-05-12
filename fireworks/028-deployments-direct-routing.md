---
title: Direct routing (deprecated) - Fireworks AI Docs
url: https://docs.fireworks.ai/deployments/direct-routing
source: sitemap
fetched_at: 2026-04-27T20:18:58.676027397-03:00
rendered_js: false
word_count: 179
summary: This document explains the benefits of migrating from direct routing to the main API gateway, detailing how the migration can be performed across cURL, Python SDKs (both standard and OpenAI), and noting specialized cloud endpoints like AWS and GCP.
tags:
    - api-migration
    - direct-routing
    - fireworks-gateway
    - latency-reduction
    - cloud-endpoints
    - integration-guide
category: tutorial
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
The API gateway now matches direct routing latency while providing additional benefits. Migrating gives you:

- **Multi-region reliability** — opt in to [[313-deployments-regions|multi-region deployments]] for automatic failover
- **Region flexibility** — move deployments without client code changes
- **Sub-10 ms overhead** — negligible latency for most users
- **Automatic retries** — gateway retries transient errors
- **One URL** — no separate URL per deployment

## Migration Steps

Update the URL and swap your direct-route API key for a standard [Fireworks API key](https://fireworks.ai/api-keys).

### cURL

| Before | After |
|--------|-------|
| `https://my-account-abcd1234.us-arizona-1.direct.fireworks.ai/v1` | `https://api.fireworks.ai/inference/v1` |

Replace the direct-route API key with your Fireworks API key.

### Python (Fireworks SDK)

```python
# Remove base_url (SDK defaults to api.fireworks.ai)
# Remove api_key (SDK reads FIREWORKS_API_KEY env var)
```

### Python (OpenAI SDK)

```python
base_url = "https://api.fireworks.ai/inference/v1"
api_key = os.environ.get("FIREWORKS_API_KEY")
```

## Cloud-Specific Endpoints

| Endpoint | Use Case |
|----------|----------|
| `api.fireworks.ai` | Default, lowest latency for most users |
| `aws.api.fireworks.ai` | AWS traffic stays on AWS |
| `gcp.api.fireworks.ai` | GCP traffic stays on GCP |

## Private Connectivity

| Method | Setup |
|--------|-------|
| **GCP Private Service Connect (PSC)** | Contact Fireworks representative |
| **AWS PrivateLink** | Contact Fireworks representative |
