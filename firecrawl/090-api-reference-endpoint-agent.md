---
title: Agent - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/agent
source: sitemap
fetched_at: 2026-03-23T07:20:12.825869-03:00
rendered_js: false
word_count: 136
summary: This document provides the API specifications for initiating an agentic data extraction task, detailing required headers, request parameters, and model configuration options.
tags:
    - api-reference
    - data-extraction
    - agentic-workflow
    - firecrawl-api
    - authentication
    - schema-validation
category: api
---

Start an agent task for agentic data extraction

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

The prompt describing what data to extract

Maximum string length: `10000`

Optional list of URLs to constrain the agent to

Optional JSON schema to structure the extracted data

Maximum credits to spend on this agent task. Defaults to 2500 if not set. Values above 2,500 are always billed as paid requests.

If true, agent will only visit URLs provided in the urls array

model

enum&lt;string&gt;

default:spark-1-mini

The model to use for the agent task. spark-1-mini (default) is 60% cheaper, spark-1-pro offers higher accuracy for complex tasks

Available options:

`spark-1-mini`,

`spark-1-pro`

#### Response

Agent task started successfully