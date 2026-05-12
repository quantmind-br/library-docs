---
title: Inference Error Codes - Fireworks AI Docs
url: https://docs.fireworks.ai/guides/inference-error-codes
source: sitemap
fetched_at: 2026-04-27T20:18:19.836213331-03:00
rendered_js: false
word_count: 652
summary: This document serves as a reference guide detailing common HTTP error codes returned by the Fireworks API, providing specific reasons for each code and offering actionable steps to resolve the corresponding issues.
tags:
    - api-error-codes
    - fireworks-api
    - troubleshooting
    - http-status
    - inference-errors
    - rate-limiting
category: reference
optimized: true
optimized_at: 2026-04-27T20:20:00Z
---
Understanding error codes helps quickly diagnose and resolve issues when making inference requests to the Fireworks API.

## Common Error Codes

| Code | Error Name | Possible Issue(s) | How to Resolve |
|---|---|---|---|
| `400` | Bad Request | Invalid input or malformed request | Review the request parameters and ensure they match the expected format. |
| `401` | Unauthorized | Invalid API key or insufficient permissions | Verify your API key and ensure it has the correct permissions. |
| `402` | Payment Required | Account is not on a paid plan or has exceeded usage limits | Check your billing status. Upgrade your plan if necessary. |
| `403` | Forbidden | Authentication issues | Verify you have the correct API key. |
| `404` | Not Found | API endpoint path doesn't exist, model doesn't exist, model is not deployed, or no permission | Verify the URL path. Check if the model exists and is available. |
| `405` | Method Not Allowed | Unsupported HTTP method (e.g. using GET instead of POST) | Check the API documentation for the correct HTTP method. |
| `408` | Request Timeout | Request took too long, possibly due to server overload or network issues | Retry the request after a brief wait. Consider increasing the timeout value. |
| `412` | Precondition Failed | Account suspended or LoRA model failed to load | Check your account status. For LoRA models, ensure the model was uploaded correctly. Contact support if the issue persists. |
| `413` | Payload Too Large | Input data exceeds the allowed size limit | Reduce the size of the input payload. |
| `429` | Too Many Requests | Rate limited (serverless) or deployment capacity exceeded (dedicated/on-demand) | See [understanding 429 errors](#understanding-429-errors) below. |
| `500` | Internal Server Error | Server-side code bug | Contact Fireworks support immediately. |
| `502` | Bad Gateway | Invalid response from an upstream server | Wait and retry. If the error persists, it may indicate a server outage. |
| `503` | Service Unavailable | Service is down for maintenance or experiencing issues | Retry the request after some time. Check the [status page](https://status.fireworks.ai) for maintenance announcements. |
| `504` | Gateway Timeout | No response in time from an upstream server | Wait briefly and retry. Consider using a shorter input prompt. |
| `520` | Unknown Error | Unexpected error with no clear explanation | Retry the request. Contact support if the issue persists. |

## Understanding 429 Errors

HTTP 429 (`Too Many Requests`) can be returned on both serverless and dedicated/on-demand deployments, but the cause and recommended action differ.

### Serverless deployments

On serverless, a 429 means your account has exceeded the current rate limit. Serverless rate limits are dynamic and grow with sustained usage. To resolve:

- Wait briefly and retry with exponential backoff
- Monitor `x-ratelimit-remaining-requests` response headers to stay within your limits
- For higher throughput, upgrade to an [on-demand deployment](https://docs.fireworks.ai/guides/ondemand-deployments)

See [[077-guides-quotas-usage-rate-limits|Rate Limits & Quotas]] for full details on serverless rate limiting.

### Dedicated and on-demand deployments

On dedicated and on-demand deployments, **there are no account-level rate limits**. A 429 instead indicates that your deployment's processing capacity is saturated. This is a capacity signal, not quota enforcement. To resolve:

- **Reduce burst concurrency** — lower the number of parallel requests or add client-side rate limiting with backoff
- **Scale up the deployment** — add more replicas or GPUs to increase throughput
- **Optimize request patterns** — use shorter prompts, reduce max output tokens, or batch requests to lower per-request resource consumption

## Troubleshooting Tips

If you encounter an error not listed here:

- Review the API documentation for the correct usage of endpoints and parameters
- Check the [Fireworks status page](https://status.fireworks.ai) for any ongoing service disruptions
- Contact support at [support@fireworks.ai](mailto:support@fireworks.ai) or join our [Discord](https://discord.gg/fireworks-ai)

#api-error-codes #http-status #rate-limiting #troubleshooting
