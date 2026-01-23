---
title: Post-Call Rules | liteLLM
url: https://docs.litellm.ai/docs/proxy/rules
source: sitemap
fetched_at: 2026-01-21T19:53:35.131897637-03:00
rendered_js: false
word_count: 77
summary: This document explains how to implement custom post-call validation rules in LiteLLM Proxy to evaluate and potentially reject LLM responses based on user-defined criteria.
tags:
    - litellm
    - proxy-rules
    - post-call-validation
    - response-filtering
    - custom-logic
    - error-handling
category: guide
---

Use this to fail a request based on the output of an llm api call.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Step 1: Create a file (e.g. post\_call\_rules.py)[​](#step-1-create-a-file-eg-post_call_rulespy "Direct link to Step 1: Create a file (e.g. post_call_rules.py)")

```
defmy_custom_rule(input):# receives the model response 
iflen(input)<5:
return{
"decision":False,
"message":"This violates LiteLLM Proxy Rules. Response too short"
}
return{"decision":True}# message not required since, request will pass
```

### Step 2. Point it to your proxy[​](#step-2-point-it-to-your-proxy "Direct link to Step 2. Point it to your proxy")

```
litellm_settings:
  post_call_rules: post_call_rules.my_custom_rule
```

### Step 3. Start + test your proxy[​](#step-3-start--test-your-proxy "Direct link to Step 3. Start + test your proxy")

```
$ litellm /path/to/config.yaml
```

```
curl --location 'http://0.0.0.0:4000/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-1234' \
--data '{
  "model": "gpt-3.5-turbo",
  "messages": [{"role":"user","content":"What llm are you?"}],
  "temperature": 0.7,
  "max_tokens": 10,
}'
```

* * *

This will now check if a response is &gt; len 5, and if it fails, it'll retry a call 3 times before failing.

### Response that fail the rule[​](#response-that-fail-the-rule "Direct link to Response that fail the rule")

This is the response from LiteLLM Proxy on failing a rule

```
{
"error":
{
"message":"This violates LiteLLM Proxy Rules. Response too short",
"type":null,
"param":null,
"code":500
}
}
```