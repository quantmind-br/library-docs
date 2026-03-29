---
title: Rules | liteLLM
url: https://docs.litellm.ai/docs/rules
source: sitemap
fetched_at: 2026-01-21T19:54:20.439730734-03:00
rendered_js: false
word_count: 123
summary: This document explains how to implement custom pre-call and post-call validation rules in LiteLLM to filter inputs and responses or trigger model fallbacks.
tags:
    - litellm
    - validation-rules
    - error-handling
    - llm-api
    - python-library
    - fallback-mechanisms
category: guide
---

Use this to fail a request based on the input or output of an llm api call.

```
import litellm 
import os 

# set env vars 
os.environ["OPENAI_API_KEY"]="your-api-key"
os.environ["OPENROUTER_API_KEY"]="your-api-key"

defmy_custom_rule(input):# receives the model response 
if"i don't think i can answer"ininput:# trigger fallback if the model refuses to answer 
returnFalse
returnTrue

litellm.post_call_rules =[my_custom_rule]# have these be functions that can be called to fail a call

response = litellm.completion(model="gpt-3.5-turbo", messages=[{"role":"user",
"content":"Hey, how's it going?"}], fallbacks=["openrouter/gryphe/mythomax-l2-13b"])
```

## Available Endpoints[​](#available-endpoints "Direct link to Available Endpoints")

- `litellm.pre_call_rules = []` - A list of functions to iterate over before making the api call. Each function is expected to return either True (allow call) or False (fail call).
- `litellm.post_call_rules = []` - List of functions to iterate over before making the api call. Each function is expected to return either True (allow call) or False (fail call).

## Expected format of rule[​](#expected-format-of-rule "Direct link to Expected format of rule")

```
defmy_custom_rule(input:str)->bool:# receives the model response 
if"i don't think i can answer"ininput:# trigger fallback if the model refuses to answer 
returnFalse
returnTrue
```

#### Inputs[​](#inputs "Direct link to Inputs")

- `input`: *str*: The user input or llm response.

#### Outputs[​](#outputs "Direct link to Outputs")

- `bool`: Return True (allow call) or False (fail call)

## Example Rules[​](#example-rules "Direct link to Example Rules")

### Example 1: Fail if user input is too long[​](#example-1-fail-if-user-input-is-too-long "Direct link to Example 1: Fail if user input is too long")

```
import litellm 
import os 

# set env vars 
os.environ["OPENAI_API_KEY"]="your-api-key"

defmy_custom_rule(input):# receives the model response 
iflen(input)>10:# fail call if too long
returnFalse
returnTrue

litellm.pre_call_rules =[my_custom_rule]# have these be functions that can be called to fail a call

response = litellm.completion(model="gpt-3.5-turbo", messages=[{"role":"user","content":"Hey, how's it going?"}])
```

### Example 2: Fallback to uncensored model if llm refuses to answer[​](#example-2-fallback-to-uncensored-model-if-llm-refuses-to-answer "Direct link to Example 2: Fallback to uncensored model if llm refuses to answer")

```
import litellm 
import os 

# set env vars 
os.environ["OPENAI_API_KEY"]="your-api-key"
os.environ["OPENROUTER_API_KEY"]="your-api-key"

defmy_custom_rule(input):# receives the model response 
if"i don't think i can answer"ininput:# trigger fallback if the model refuses to answer 
returnFalse
returnTrue

litellm.post_call_rules =[my_custom_rule]# have these be functions that can be called to fail a call

response = litellm.completion(model="gpt-3.5-turbo", messages=[{"role":"user",
"content":"Hey, how's it going?"}], fallbacks=["openrouter/gryphe/mythomax-l2-13b"])
```