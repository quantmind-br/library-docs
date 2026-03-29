---
title: Snowflake | liteLLM
url: https://docs.litellm.ai/docs/providers/snowflake
source: sitemap
fetched_at: 2026-01-21T19:50:25.126334288-03:00
rendered_js: false
word_count: 63
summary: This document provides instructions on how to authenticate and execute completion and embedding calls to Snowflake models using the LiteLLM library.
tags:
    - snowflake
    - litellm
    - authentication
    - jwt-token
    - python-sdk
    - llm-integration
category: guide
---

```
    "temperature",
    "max_tokens",
    "top_p",
    "response_format"
```

Snowflake does have API keys. Instead, you access the Snowflake API with your JWT token and account identifier.

```
from litellm import completion, embedding

## set ENV variables
os.environ["SNOWFLAKE_JWT"]="JWT_TOKEN"
os.environ["SNOWFLAKE_ACCOUNT_ID"]="YOUR ACCOUNT IDENTIFIER"

# Snowflake completion call
response = completion(
    model="snowflake/mistral-7b",
    messages =[{"content":"Hello, how are you?","role":"user"}]
)

# Snowflake embedding call
response = embedding(
    model="snowflake/mistral-7b",
input=["My text"]
)

# Pass`api_key` and `account_id` as parameters
response = completion(
    model="snowflake/mistral-7b",
    messages =[{"content":"Hello, how are you?","role":"user"}],
    account_id="AAAA-BBBB",
    api_key="JWT_TOKEN"
)

# using PAT
response = completion(
    model="snowflake/mistral-7b",
    messages =[{"content":"Hello, how are you?","role":"user"}],
    api_key="pat/PAT_TOKEN"
)
```