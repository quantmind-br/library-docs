---
title: Get Extract Status - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:19:33.256501-03:00
rendered_js: false
word_count: 77
summary: This document provides the API specification for retrieving the current status and token usage of an extract job.
tags:
    - api-reference
    - extract-job
    - status-check
    - token-usage
    - bearer-authentication
category: api
---

Get the status of an extract job

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

The ID of the extract job

#### Response

The current status of the extract job

Available options:

`completed`,

`processing`,

`failed`,

`cancelled`

The number of tokens used by the extract job. Only available if the job is completed.