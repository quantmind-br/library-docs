---
title: Scrub Logged Data | liteLLM
url: https://docs.litellm.ai/docs/observability/scrub_data
source: sitemap
fetched_at: 2026-01-21T19:46:32.177618122-03:00
rendered_js: false
word_count: 98
summary: This document explains how to redact sensitive information or mask PII in message logs using custom logging hooks in LiteLLM before data is sent to external integrations.
tags:
    - litellm
    - data-masking
    - pii-redaction
    - logging
    - custom-logger
    - langfuse
    - python
category: guide
---

Redact messages / mask PII before sending data to logging integrations (langfuse/etc.).

```
from litellm.integrations.custom_logger import CustomLogger

classMyCustomHandler(CustomLogger):
asyncdefasync_logging_hook(
        self, kwargs:dict, result: Any, call_type:str
)-> Tuple[dict, Any]:
"""
        For masking logged request/response. Return a modified version of the request/result. 

        Called before `async_log_success_event`.
        """
if(
            call_type =="completion"or call_type =="acompletion"
):# /chat/completions requests
            messages: Optional[List]= kwargs.get("messages",None)

            kwargs["messages"]=[{"role":"user","content":"MASK_THIS_ASYNC_VALUE"}]

return kwargs, responses

deflogging_hook(
        self, kwargs:dict, result: Any, call_type:str
)-> Tuple[dict, Any]:
"""
        For masking logged request/response. Return a modified version of the request/result.

        Called before `log_success_event`.
        """
if(
            call_type =="completion"or call_type =="acompletion"
):# /chat/completions requests
            messages: Optional[List]= kwargs.get("messages",None)

            kwargs["messages"]=[{"role":"user","content":"MASK_THIS_SYNC_VALUE"}]

return kwargs, responses


customHandler = MyCustomHandler()
```

```
# pip install langfuse 

import os
import litellm
from litellm import completion 

os.environ["LANGFUSE_PUBLIC_KEY"]=""
os.environ["LANGFUSE_SECRET_KEY"]=""
# Optional, defaults to https://cloud.langfuse.com
os.environ["LANGFUSE_HOST"]# optional
# LLM API Keys
os.environ['OPENAI_API_KEY']=""

litellm.callbacks =[customHandler]
litellm.success_callback =["langfuse"]


## sync 
response = completion(model="gpt-3.5-turbo", messages=[{"role":"user","content":"Hi 👋 - i'm openai"}],
                              stream=True)
for chunk in response:
continue


## async
import asyncio 

defasync completion():
    response =await acompletion(model="gpt-3.5-turbo", messages=[{"role":"user","content":"Hi 👋 - i'm openai"}],
                              stream=True)
asyncfor chunk in response:
continue
asyncio.run(completion())
```