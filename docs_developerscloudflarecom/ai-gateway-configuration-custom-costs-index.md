---
title: Custom costs · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/configuration/custom-costs/index.md
source: llms
fetched_at: 2026-01-24T15:07:14.325959081-03:00
rendered_js: false
word_count: 210
summary: This document explains how to use the cf-aig-custom-cost header to specify custom token pricing for AI Gateway requests to ensure metrics reflect unique or negotiated pricing.
tags:
    - ai-gateway
    - custom-cost
    - token-usage
    - request-headers
    - cost-management
category: guide
---

AI Gateway allows you to set custom costs at the request level. By using this feature, the cost metrics can accurately reflect your unique pricing, overriding the default or public model costs.

Note

Custom costs will only apply to requests that pass tokens in their response. Requests without token information will not have costs calculated.

## Custom cost

To add custom costs to your API requests, use the `cf-aig-custom-cost` header. This header enables you to specify the cost per token for both input (tokens sent) and output (tokens received).

* **per\_token\_in**: The negotiated input token cost (per token).
* **per\_token\_out**: The negotiated output token cost (per token).

There is no limit to the number of decimal places you can include, ensuring precise cost calculations, regardless of how small the values are.

Custom costs will appear in the logs with an underline, making it easy to identify when custom pricing has been applied.

In this example, if you have a negotiated price of $1 per million input tokens and $2 per million output tokens, include the `cf-aig-custom-cost` header as shown below.

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --header 'cf-aig-custom-cost: {"per_token_in":0.000001,"per_token_out":0.000002}' \
  --data ' {
        "model": "gpt-4o-mini",
        "messages": [
          {
            "role": "user",
            "content": "When is Cloudflare’s Birthday Week?"
          }
        ]
      }'
```

Note

If a response is served from cache (cache hit), the cost is always `0`, even if you specified a custom cost. Custom costs only apply when the request reaches the model provider.