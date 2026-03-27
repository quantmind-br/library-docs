---
title: Token Usage - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/token-usage
source: sitemap
fetched_at: 2026-03-23T07:19:29.718414-03:00
rendered_js: false
word_count: 73
summary: This document describes the API endpoint for retrieving the remaining credit and token usage for an authenticated team.
tags:
    - api-endpoint
    - token-usage
    - billing-management
    - firecrawl-api
    - authentication
    - credit-system
category: api
---

Get remaining tokens for the authenticated team (Extract only)

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/token-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remainingTokens": 1000,
    "planTokens": 500000,
    "billingPeriodStart": "2025-01-01T00:00:00Z",
    "billingPeriodEnd": "2025-01-31T23:59:59Z"
  }
}
```

We’ve simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens. Reported token usage now includes usage from all endpoints.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Response