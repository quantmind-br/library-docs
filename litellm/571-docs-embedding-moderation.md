---
title: litellm.moderation() | liteLLM
url: https://docs.litellm.ai/docs/embedding/moderation
source: sitemap
fetched_at: 2026-01-21T19:45:07.311869689-03:00
rendered_js: false
word_count: 8
summary: This document explains how to use LiteLLM to interact with the OpenAI moderation endpoint to check content for violations.
tags:
    - litellm
    - openai
    - moderation-api
    - content-filtering
    - python
category: reference
---

LiteLLM supports the moderation endpoint for OpenAI

## Usage[​](#usage "Direct link to Usage")

```
import os
from litellm import moderation
os.environ['OPENAI_API_KEY']=""
response = moderation(input="i'm ishaan cto of litellm")
```