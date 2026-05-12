---
title: Get Agent Status - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/agent-get
source: sitemap
fetched_at: 2026-03-23T07:20:02.973342-03:00
rendered_js: false
word_count: 78
summary: This document describes the API endpoint for retrieving the current status, model configuration, and error details of a specific agent job.
tags:
    - api-reference
    - agent-job
    - status-check
    - job-monitoring
    - bearer-authentication
category: api
---

Get the status of an agent job

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

#### Response

Available options:

`processing`,

`completed`,

`failed`

The extracted data (only present when status is completed)

model

enum&lt;string&gt;

default:spark-1-pro

Model preset used for the agent run

Available options:

`spark-1-pro`,

`spark-1-mini`

Error message (only present when status is failed)