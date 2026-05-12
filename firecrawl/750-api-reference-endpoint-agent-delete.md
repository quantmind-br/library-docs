---
title: Cancel Agent - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/agent-delete
source: sitemap
fetched_at: 2026-03-23T07:19:55.979159-03:00
rendered_js: false
word_count: 39
summary: Provides the API endpoint and authorization requirements for canceling an active agent job within the Firecrawl service.
tags:
    - api-request
    - job-management
    - firecrawl-api
    - delete-request
    - bearer-authentication
category: api
---

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'

curl --request DELETE \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'
```

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

#### Response

Agent job cancelled successfully