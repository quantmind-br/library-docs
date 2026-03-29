---
title: Local Debugging | liteLLM
url: https://docs.litellm.ai/docs/debugging/local_debugging
source: sitemap
fetched_at: 2026-01-21T19:45:02.058809606-03:00
rendered_js: false
word_count: 149
summary: This document explains how to perform local debugging and logging for LLM calls using LiteLLM's built-in debug mode and custom logging functions.
tags:
    - litellm
    - debugging
    - logging
    - python-sdk
    - api-monitoring
    - error-handling
category: guide
---

There's 2 ways to do local debugging - `litellm._turn_on_debug()` and by passing in a custom function `completion(...logger_fn=<your_local_function>)`. Warning: Make sure to not use `_turn_on_debug()` in production. It logs API keys, which might end up in log files.

This is good for getting print statements for everything litellm is doing.

```
import litellm
from litellm import completion

litellm._turn_on_debug()# 👈 this is the 1-line change you need to make

## set ENV variables
os.environ["OPENAI_API_KEY"]="openai key"
os.environ["COHERE_API_KEY"]="cohere key"

messages =[{"content":"Hello, how are you?","role":"user"}]

# openai call
response = completion(model="gpt-3.5-turbo", messages=messages)

# cohere call
response = completion("command-nightly", messages)
```

If you need to store the logs as JSON, just set the `litellm.json_logs = True`.

We currently just log the raw POST request from litellm as a JSON - \[**See Code**].

But sometimes all you care about is seeing exactly what's getting sent to your api call and what's being returned - e.g. if the api call is failing, why is that happening? what are the exact params being set?

In that case, LiteLLM allows you to pass in a custom logging function to see / modify the model call Input/Outputs.

**Note**: We expect you to accept a dict object.

```
from litellm import completion

defmy_custom_logging_fn(model_call_dict):
print(f"model call details: {model_call_dict}")

## set ENV variables
os.environ["OPENAI_API_KEY"]="openai key"
os.environ["COHERE_API_KEY"]="cohere key"

messages =[{"content":"Hello, how are you?","role":"user"}]

# openai call
response = completion(model="gpt-3.5-turbo", messages=messages, logger_fn=my_custom_logging_fn)

# cohere call
response = completion("command-nightly", messages, logger_fn=my_custom_logging_fn)
```