---
title: Completion Function - completion() | liteLLM
url: https://docs.litellm.ai/completion/output
source: sitemap
fetched_at: 2026-01-21T19:41:03.630469643-03:00
rendered_js: false
word_count: 13
summary: This document illustrates the standardized JSON response structure returned by a LiteLLM completion call, including fields for choices, model usage, and metadata.
tags:
    - litellm
    - api-response
    - json-structure
    - completion-api
    - llm-output
category: reference
---

Here's the exact json output you can expect from a litellm `completion` call:

```
{'choices':[{'finish_reason':'stop',
'index':0,
'message':{'role':'assistant',
'content':" I'm doing well, thank you for asking. I am Claude, an AI assistant created by Anthropic."}}],
'created':1691429984.3852863,
'model':'claude-instant-1',
'usage':{'prompt_tokens':18,'completion_tokens':23,'total_tokens':41}}
```