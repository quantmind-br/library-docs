---
title: Credit Usage - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/credit-usage
source: sitemap
fetched_at: 2026-03-23T07:19:22.764911-03:00
rendered_js: false
word_count: 47
summary: This document provides the API endpoint details and authentication requirements for retrieving the current credit usage and billing information for an authenticated team.
tags:
    - api-reference
    - credit-usage
    - billing-information
    - team-management
    - authentication
category: api
---

Get remaining credits for the authenticated team

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/credit-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remainingCredits": 1000,
    "planCredits": 500000,
    "billingPeriodStart": "2025-01-01T00:00:00Z",
    "billingPeriodEnd": "2025-01-31T23:59:59Z"
  }
}
```

Get remaining credits for the authenticated team

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/credit-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remainingCredits": 1000,
    "planCredits": 500000,
    "billingPeriodStart": "2025-01-01T00:00:00Z",
    "billingPeriodEnd": "2025-01-31T23:59:59Z"
  }
}
```

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Response