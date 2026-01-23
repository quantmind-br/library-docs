---
title: Custom Guardrail | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/custom_guardrail
source: sitemap
fetched_at: 2026-01-21T19:52:05.966165673-03:00
rendered_js: false
word_count: 947
summary: This document explains how to implement and integrate custom guardrails in LiteLLM by creating a Python class and configuring it within the gateway. It covers the setup of various event hooks to monitor, modify, or block LLM requests and responses based on custom rules.
tags:
    - litellm
    - custom-guardrails
    - api-gateway
    - python-hooks
    - moderation
    - llm-security
category: tutorial
---

Use this if you want to write code to run a custom guardrail

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Write a `CustomGuardrail` Class[​](#1-write-a-customguardrail-class "Direct link to 1-write-a-customguardrail-class")

The simplest way to create a custom guardrail is by implementing the `apply_guardrail` method. This method is called to check text content and can block requests by raising an exception.

**Example `CustomGuardrail` Class**

Create a new file called `custom_guardrail.py` and add this code to it:

```
import os
from typing import Optional, List
from litellm.integrations.custom_guardrail import CustomGuardrail
from litellm.types.guardrails import PiiEntityType
from litellm._logging import verbose_proxy_logger
from litellm.llms.custom_httpx.http_handler import(
    get_async_httpx_client,
    httpxSpecialProvider,
)

classmyCustomGuardrail(CustomGuardrail):
def__init__(self, api_key: Optional[str]=None, api_base: Optional[str]=None,**kwargs):
        self.api_key = api_key or os.getenv("MY_GUARDRAIL_API_KEY")
        self.api_base = api_base or os.getenv("MY_GUARDRAIL_API_BASE","https://api.myguardrail.com")
super().__init__(**kwargs)

asyncdefapply_guardrail(
        self,
        text:str,# IMPORTANT: This is the text to check against your guardrail rules. It's extracted from the request or response across all LLM call types.
        language: Optional[str]=None,# ignore 
        entities: Optional[List[PiiEntityType]]=None,# ignore
        request_data: Optional[dict]=None,# ignore
)->str:
"""
        Check text content against your guardrail rules.
        Raise an exception to block the request.
        Return the text (optionally modified) to allow it through.
        """
        result =await self._check_with_api(text, request_data)

if result.get("action")=="BLOCK":
raise Exception(f"Content blocked: {result.get('reason','Policy violation')}")

return text

asyncdef_check_with_api(self, text:str, request_data: Optional[dict])->dict:
        async_client = get_async_httpx_client(llm_provider=httpxSpecialProvider.LoggingCallback)

        headers ={
"Content-Type":"application/json",
"Authorization":f"Bearer {self.api_key}",
}

        response =await async_client.post(
f"{self.api_base}/check",
            headers=headers,
            json={"text": text},
            timeout=5,
)

        response.raise_for_status()
return response.json()
```

Advanced: Using Individual Event Hooks

If you need more fine-grained control, you can implement individual event hooks instead of (or in addition to) `apply_guardrail`:

- `async_pre_call_hook` - Modify input or reject request before making LLM API call
- `async_moderation_hook` - Reject request, runs in parallel with LLM API call (helps lower latency)
- `async_post_call_success_hook` - Apply guardrail on input/output, runs after making LLM API call
- `async_post_call_streaming_iterator_hook` - Pass the entire stream to the guardrail

[**See examples of individual event hooks here**](#advanced-individual-event-hooks) | [**See detailed spec of methods here**](#customguardrail-methods)

### 2. Pass your custom guardrail class in LiteLLM `config.yaml`[​](#2-pass-your-custom-guardrail-class-in-litellm-configyaml "Direct link to 2-pass-your-custom-guardrail-class-in-litellm-configyaml")

In the config below, we point the guardrail to our custom guardrail by setting `guardrail: custom_guardrail.myCustomGuardrail`

- Python Filename: `custom_guardrail.py`
- Guardrail class name : `myCustomGuardrail`. This is defined in Step 1

`guardrail: custom_guardrail.myCustomGuardrail`

```
model_list:
-model_name: gpt-4
litellm_params:
model: openai/gpt-4o
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"my-custom-guardrail"
litellm_params:
guardrail: custom_guardrail.myCustomGuardrail  # 👈 Key change
mode:"during_call"# runs apply_guardrail method
api_key: os.environ/MY_GUARDRAIL_API_KEY
api_base: https://api.myguardrail.com
```

Mode Options

- `during_call` - Default mode, runs `apply_guardrail` method (or `async_moderation_hook` if using individual hooks)
- `pre_call` - Runs `async_pre_call_hook` for input modification
- `post_call` - Runs `async_post_call_success_hook` for output validation

Advanced: Multiple modes with individual event hooks

If you're using individual event hooks, you can configure multiple guardrails with different modes:

```
guardrails:
-guardrail_name:"custom-pre-guard"
litellm_params:
guardrail: custom_guardrail.myCustomGuardrail
mode:"pre_call"# runs async_pre_call_hook
-guardrail_name:"custom-during-guard"
litellm_params:
guardrail: custom_guardrail.myCustomGuardrail  
mode:"during_call"# runs async_moderation_hook
-guardrail_name:"custom-post-guard"
litellm_params:
guardrail: custom_guardrail.myCustomGuardrail
mode:"post_call"# runs async_post_call_success_hook
```

### 3. Start LiteLLM Gateway[​](#3-start-litellm-gateway "Direct link to 3. Start LiteLLM Gateway")

- Docker Run
- litellm pip

Mount your `custom_guardrail.py` on the LiteLLM Docker container

This mounts your `custom_guardrail.py` file from your local directory to the `/app` directory in the Docker container, making it accessible to the LiteLLM Gateway.

```
docker run -d \
  -p 4000:4000 \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  --name my-app \
  -v $(pwd)/my_config.yaml:/app/config.yaml \
  -v $(pwd)/custom_guardrail.py:/app/custom_guardrail.py \
  my-app:latest \
  --config /app/config.yaml \
  --port 4000 \
  --detailed_debug \
```

### 4. Test it[​](#4-test-it "Direct link to 4. Test it")

[**Langchain, OpenAI SDK Usage Examples**](https://docs.litellm.ai/docs/proxy/proxy/user_keys#request-format)

- Blocked Request
- Successful Call

This request will be blocked if it violates your guardrail policy:

```
curl -i -X POST http://localhost:4000/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer sk-1234" \
-d '{
    "model": "gpt-4",
    "messages": [
        {
            "role": "user",
            "content": "Content that violates policy"
        }
    ],
   "guardrails": ["my-custom-guardrail"]
}'
```

Expected response when blocked:

```
{
"error":{
"message":"Content blocked: Policy violation",
"type":"None",
"param":"None",
"code":"500"
}
}
```

Advanced: Testing individual event hooks

If you're using individual event hooks, you can test each mode separately:

#### Test `"custom-pre-guard"`[​](#test-custom-pre-guard "Direct link to test-custom-pre-guard")

- Modify input
- Successful Call

Expect this to mask the word `litellm` before sending the request to the LLM API. [This runs the `async_pre_call_hook`](#advanced-individual-event-hooks)

```
curl -i  -X POST http://localhost:4000/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer sk-1234" \
-d '{
    "model": "gpt-4",
    "messages": [
        {
            "role": "user",
            "content": "say the word - `litellm`"
        }
    ],
   "guardrails": ["custom-pre-guard"]
}'
```

#### Test `"custom-during-guard"`[​](#test-custom-during-guard "Direct link to test-custom-during-guard")

- Unsuccessful call
- Successful Call

Expect this to fail since `litellm` is in the message content. [This runs the `async_moderation_hook`](#advanced-individual-event-hooks)

```
curl -i  -X POST http://localhost:4000/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer sk-1234" \
-d '{
    "model": "gpt-4",
    "messages": [
        {
            "role": "user",
            "content": "say the word - `litellm`"
        }
    ],
   "guardrails": ["custom-during-guard"]
}'
```

Expected response:

```
{
"error":{
"message":"Guardrail failed words - `litellm` detected",
"type":"None",
"param":"None",
"code":"500"
}
}
```

#### Test `"custom-post-guard"`[​](#test-custom-post-guard "Direct link to test-custom-post-guard")

- Unsuccessful call
- Successful Call

Expect this to fail since `coffee` will be in the response content. [This runs the `async_post_call_success_hook`](#advanced-individual-event-hooks)

```
curl -i  -X POST http://localhost:4000/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer sk-1234" \
-d '{
    "model": "gpt-4",
    "messages": [
        {
            "role": "user",
            "content": "what is coffee"
        }
    ],
   "guardrails": ["custom-post-guard"]
}'
```

Expected response:

```
{
"error":{
"message":"Guardrail failed Coffee Detected",
"type":"None",
"param":"None",
"code":"500"
}
}
```

## ✨ Pass additional parameters to guardrail[​](#-pass-additional-parameters-to-guardrail "Direct link to ✨ Pass additional parameters to guardrail")

Use this to pass additional parameters to the guardrail API call. e.g. things like success threshold

1. Use `get_guardrail_dynamic_request_body_params`

`get_guardrail_dynamic_request_body_params` is a method of the `litellm.integrations.custom_guardrail.CustomGuardrail` class that fetches the dynamic guardrail params passed in the request body.

```
from typing import Any, Dict, List, Literal, Optional, Union
import litellm
from litellm._logging import verbose_proxy_logger
from litellm.caching.caching import DualCache
from litellm.integrations.custom_guardrail import CustomGuardrail
from litellm.proxy._types import UserAPIKeyAuth

classmyCustomGuardrail(CustomGuardrail):
def__init__(self,**kwargs):
super().__init__(**kwargs)

asyncdefasync_pre_call_hook(
        self,
        user_api_key_dict: UserAPIKeyAuth,
        cache: DualCache,
        data:dict,
        call_type: Literal[
"completion",
"text_completion",
"embeddings",
"image_generation",
"moderation",
"audio_transcription",
"pass_through_endpoint",
"rerank"
],
)-> Optional[Union[Exception,str,dict]]:
# Get dynamic params from request body
        params = self.get_guardrail_dynamic_request_body_params(request_data=data)
# params will contain: {"success_threshold": 0.9}
        verbose_proxy_logger.debug("Guardrail params: %s", params)
return data
```

2. Pass parameters in your API requests:

LiteLLM Proxy allows you to pass `guardrails` in the request body, following the [`guardrails` spec](https://docs.litellm.ai/docs/proxy/guardrails/quick_start#spec-guardrails-parameter).

- OpenAI Python
- Curl

```
import openai
client = openai.OpenAI(
    api_key="anything",
    base_url="http://0.0.0.0:4000"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Write a short poem"}],
    extra_body={
"guardrails":[
"custom-pre-guard":{
"extra_body":{
"success_threshold":0.9
}
}
]
}
)
```

The `get_guardrail_dynamic_request_body_params` method will return:

```
{
"success_threshold":0.9
}
```

## Advanced: Individual Event Hooks[​](#advanced-individual-event-hooks "Direct link to Advanced: Individual Event Hooks")

Pro: More flexibility Con: You need to implement this for each LLM call type (chat completions, text completions, embeddings, image generation, moderation, audio transcription, pass through endpoint, rerank, etc. )

For more fine-grained control over when and how your guardrail runs, you can implement individual event hooks. This gives you flexibility to:

- Modify inputs before the LLM call
- Run checks in parallel with the LLM call (lower latency)
- Validate or modify outputs after the LLM call
- Process streaming responses

### Example with Individual Event Hooks[​](#example-with-individual-event-hooks "Direct link to Example with Individual Event Hooks")

```
from typing import Any, AsyncGenerator, Literal, Optional, Union

import litellm
from litellm._logging import verbose_proxy_logger
from litellm.caching.caching import DualCache
from litellm.integrations.custom_guardrail import CustomGuardrail
from litellm.proxy._types import UserAPIKeyAuth
from litellm.types.utils import ModelResponseStream, CallTypes


classmyCustomGuardrail(CustomGuardrail):
def__init__(
        self,
**kwargs,
):
# store kwargs as optional_params
        self.optional_params = kwargs

super().__init__(**kwargs)

asyncdefasync_pre_call_hook(
        self,
        user_api_key_dict: UserAPIKeyAuth,
        cache: DualCache,
        data:dict,
        call_type: Optional[CallTypes],
)-> Optional[Union[Exception,str,dict]]:
"""
        Runs before the LLM API call
        Runs on only Input
        Use this if you want to MODIFY the input
        """

# In this guardrail, if a user inputs `litellm` we will mask it and then send it to the LLM
        _messages = data.get("messages")
if _messages:
for message in _messages:
                _content = message.get("content")
ifisinstance(_content,str):
if"litellm"in _content.lower():
                        _content = _content.replace("litellm","********")
                        message["content"]= _content

        verbose_proxy_logger.debug(
"async_pre_call_hook: Message after masking %s", _messages
)

return data

asyncdefasync_moderation_hook(
        self,
        data:dict,
        user_api_key_dict: UserAPIKeyAuth,
        call_type: Literal["completion","embeddings","image_generation","moderation","audio_transcription"],
):
"""
        Runs in parallel to LLM API call
        Runs on only Input

        This can NOT modify the input, only used to reject or accept a call before going to LLM API
        """

# this works the same as async_pre_call_hook, but just runs in parallel as the LLM API Call
# In this guardrail, if a user inputs `litellm` we will mask it.
        _messages = data.get("messages")
if _messages:
for message in _messages:
                _content = message.get("content")
ifisinstance(_content,str):
if"litellm"in _content.lower():
raise ValueError("Guardrail failed words - `litellm` detected")

asyncdefasync_post_call_success_hook(
        self,
        data:dict,
        user_api_key_dict: UserAPIKeyAuth,
        response,
):
"""
        Runs on response from LLM API call

        It can be used to reject a response

        If a response contains the word "coffee" -> we will raise an exception
        """
        verbose_proxy_logger.debug("async_pre_call_hook response: %s", response)
ifisinstance(response, litellm.ModelResponse):
for choice in response.choices:
ifisinstance(choice, litellm.Choices):
                    verbose_proxy_logger.debug("async_pre_call_hook choice: %s", choice)
if(
                        choice.message.content
andisinstance(choice.message.content,str)
and"coffee"in choice.message.content
):
raise ValueError("Guardrail failed Coffee Detected")

asyncdefasync_post_call_streaming_iterator_hook(
        self,
        user_api_key_dict: UserAPIKeyAuth,
        response: Any,
        request_data:dict,
)-> AsyncGenerator[ModelResponseStream,None]:
"""
        Passes the entire stream to the guardrail

        This is useful for guardrails that need to see the entire response, such as PII masking.

        See Aim guardrail implementation for an example - https://github.com/BerriAI/litellm/blob/d0e022cfacb8e9ebc5409bb652059b6fd97b45c0/litellm/proxy/guardrails/guardrail_hooks/aim.py#L168

        Triggered by mode: 'post_call'
        """
asyncfor item in response:
yield item

```

## **CustomGuardrail methods**[​](#customguardrail-methods "Direct link to customguardrail-methods")

ComponentDescriptionOptionalChecked DataCan Modify InputCan Modify OutputCan Fail Call`apply_guardrail`Simple method to check and optionally modify text✅INPUT or OUTPUT✅✅✅`async_pre_call_hook`A hook that runs before the LLM API call✅INPUT✅❌✅`async_moderation_hook`A hook that runs during the LLM API call✅INPUT❌❌✅`async_post_call_success_hook`A hook that runs after a successful LLM API call✅INPUT, OUTPUT❌✅✅`async_post_call_streaming_iterator_hook`A hook that processes streaming responses✅OUTPUT❌✅✅

## Frequently Asked Questions[​](#frequently-asked-questions "Direct link to Frequently Asked Questions")

**Q. Is `apply_guardrail` relevant both in the request and in the response (pre\_call, during\_call and post\_call hooks)?**

**A.** Yes, one function works in both - See implementation [here](https://github.com/BerriAI/litellm/blob/0292b84dc47473ddeff29bd5a86f529bc523034b/litellm/proxy/utils.py#L825)

**Q. What do I get in the inputs of `apply_guardrail`? What does each field represent (what is text, language, entities, request\_data)?**

**A.** The main one you should care about is 'text' - this is what you'll want to send to your api for verification - See implementation [here](https://github.com/BerriAI/litellm/blob/0292b84dc47473ddeff29bd5a86f529bc523034b/litellm/llms/anthropic/chat/guardrail_translation/handler.py#L102)

\*\*Q. Is this function agnostic to the LLM provider? Meaning does it pass the same values for OpenAI and Anthropic for example?

**A.** Yes

**Q. How do I know if my guardrail is running?**

**A.** If you implement `apply_guardrail`, you can query the guardrail directly via [the `/apply_guardrail` API](https://docs.litellm.ai/docs/apply_guardrail).