---
title: Custom API Server (Custom Format) | liteLLM
url: https://docs.litellm.ai/docs/providers/custom_llm_server
source: sitemap
fetched_at: 2026-01-21T19:48:48.733410238-03:00
rendered_js: false
word_count: 236
summary: This document provides instructions on integrating custom LLM providers and internal APIs into LiteLLM by extending the CustomLLM class and configuring the custom provider map. It covers implementation details for chat completions, streaming, and image generation routes within both local Python environments and the LiteLLM proxy.
tags:
    - litellm
    - custom-llm
    - api-integration
    - python
    - llm-proxy
    - custom-provider
category: guide
---

Call your custom torch-serve / internal LLM APIs via LiteLLM

info

- For calling an openai-compatible endpoint, [go here](https://docs.litellm.ai/docs/providers/openai_compatible)
- For modifying incoming/outgoing calls on proxy, [go here](https://docs.litellm.ai/docs/proxy/call_hooks)

Supported Routes:

- `/v1/chat/completions` -&gt; `litellm.acompletion`
- `/v1/completions` -&gt; `litellm.atext_completion`
- `/v1/embeddings` -&gt; `litellm.aembedding`
- `/v1/images/generations` -&gt; `litellm.aimage_generation`
- `/v1/images/edits` -&gt; `litellm.aimage_edit`
- `/v1/messages` -&gt; `litellm.acompletion`

## Quick Start[​](#quick-start "Direct link to Quick Start")

```
import litellm
from litellm import CustomLLM, completion, get_llm_provider


classMyCustomLLM(CustomLLM):
defcompletion(self,*args,**kwargs)-> litellm.ModelResponse:
return litellm.completion(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":"Hello world"}],
            mock_response="Hi!",
)# type: ignore

my_custom_llm = MyCustomLLM()

litellm.custom_provider_map =[# 👈 KEY STEP - REGISTER HANDLER
{"provider":"my-custom-llm","custom_handler": my_custom_llm}
]

resp = completion(
        model="my-custom-llm/my-fake-model",
        messages=[{"role":"user","content":"Hello world!"}],
)

assert resp.choices[0].message.content =="Hi!"
```

## OpenAI Proxy Usage[​](#openai-proxy-usage "Direct link to OpenAI Proxy Usage")

1. Setup your `custom_handler.py` file

```
import litellm
from litellm import CustomLLM, completion, get_llm_provider


classMyCustomLLM(CustomLLM):
defcompletion(self,*args,**kwargs)-> litellm.ModelResponse:
return litellm.completion(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":"Hello world"}],
            mock_response="Hi!",
)# type: ignore

asyncdefacompletion(self,*args,**kwargs)-> litellm.ModelResponse:
return litellm.completion(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":"Hello world"}],
            mock_response="Hi!",
)# type: ignore


my_custom_llm = MyCustomLLM()
```

2. Add to `config.yaml`

In the config below, we pass

python\_filename: `custom_handler.py` custom\_handler\_instance\_name: `my_custom_llm`. This is defined in Step 1

custom\_handler: `custom_handler.my_custom_llm`

```
model_list:
-model_name:"test-model"
litellm_params:
model:"openai/text-embedding-ada-002"
-model_name:"my-custom-model"
litellm_params:
model:"my-custom-llm/my-model"

litellm_settings:
custom_provider_map:
-{"provider":"my-custom-llm","custom_handler": custom_handler.my_custom_llm}
```

```
litellm --config /path/to/config.yaml
```

3. Test it!

```
curl -X POST 'http://0.0.0.0:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
    "model": "my-custom-model",
    "messages": [{"role": "user", "content": "Say \"this is a test\" in JSON!"}],
}'
```

Expected Response

```
{
    "id": "chatcmpl-06f1b9cd-08bc-43f7-9814-a69173921216",
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "Hi!",
                "role": "assistant",
                "tool_calls": null,
                "function_call": null
            }
        }
    ],
    "created": 1721955063,
    "model": "gpt-3.5-turbo",
    "object": "chat.completion",
    "system_fingerprint": null,
    "usage": {
        "prompt_tokens": 10,
        "completion_tokens": 20,
        "total_tokens": 30
    }
}
```

## Add Streaming Support[​](#add-streaming-support "Direct link to Add Streaming Support")

Here's a simple example of returning unix epoch seconds for both completion + streaming use-cases.

s/o [@Eloy Lafuente](https://github.com/stronk7) for this code example.

```
import time
from typing import Iterator, AsyncIterator
from litellm.types.utils import GenericStreamingChunk, ModelResponse
from litellm import CustomLLM, completion, acompletion

classUnixTimeLLM(CustomLLM):
defcompletion(self,*args,**kwargs)-> ModelResponse:
return completion(
            model="test/unixtime",
            mock_response=str(int(time.time())),
)# type: ignore

asyncdefacompletion(self,*args,**kwargs)-> ModelResponse:
returnawait acompletion(
            model="test/unixtime",
            mock_response=str(int(time.time())),
)# type: ignore

defstreaming(self,*args,**kwargs)-> Iterator[GenericStreamingChunk]:
        generic_streaming_chunk: GenericStreamingChunk ={
"finish_reason":"stop",
"index":0,
"is_finished":True,
"text":str(int(time.time())),
"tool_use":None,
"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0},
}
return generic_streaming_chunk # type: ignore

asyncdefastreaming(self,*args,**kwargs)-> AsyncIterator[GenericStreamingChunk]:
        generic_streaming_chunk: GenericStreamingChunk ={
"finish_reason":"stop",
"index":0,
"is_finished":True,
"text":str(int(time.time())),
"tool_use":None,
"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0},
}
yield generic_streaming_chunk # type: ignore

unixtime = UnixTimeLLM()
```

## Image Generation[​](#image-generation "Direct link to Image Generation")

1. Setup your `custom_handler.py` file

```
import litellm
from litellm import CustomLLM
from litellm.types.utils import ImageResponse, ImageObject


classMyCustomLLM(CustomLLM):
asyncdefaimage_generation(self, model:str, prompt:str, model_response: ImageResponse, optional_params:dict, logging_obj: Any, timeout: Optional[Union[float, httpx.Timeout]]=None, client: Optional[AsyncHTTPHandler]=None,)-> ImageResponse:
return ImageResponse(
            created=int(time.time()),
            data=[ImageObject(url="https://example.com/image.png")],
)

my_custom_llm = MyCustomLLM()
```

2. Add to `config.yaml`

In the config below, we pass

python\_filename: `custom_handler.py` custom\_handler\_instance\_name: `my_custom_llm`. This is defined in Step 1

custom\_handler: `custom_handler.my_custom_llm`

```
model_list:
-model_name:"test-model"
litellm_params:
model:"openai/text-embedding-ada-002"
-model_name:"my-custom-model"
litellm_params:
model:"my-custom-llm/my-model"

litellm_settings:
custom_provider_map:
-{"provider":"my-custom-llm","custom_handler": custom_handler.my_custom_llm}
```

```
litellm --config /path/to/config.yaml
```

3. Test it!

```
curl -X POST 'http://0.0.0.0:4000/v1/images/generations' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
    "model": "my-custom-model",
    "prompt": "A cute baby sea otter",
}'
```

Expected Response

```
{
    "created": 1721955063,
    "data": [{"url": "https://example.com/image.png"}],
}
```

## Image Edit[​](#image-edit "Direct link to Image Edit")

1. Setup your `custom_handler.py` file

```
import litellm
from litellm import CustomLLM
from litellm.types.utils import ImageResponse, ImageObject
import time

classMyCustomLLM(CustomLLM):
asyncdefaimage_edit(
        self,
        model:str,
        image: Any,
        prompt:str,
        model_response: ImageResponse,
        api_key: Optional[str],
        api_base: Optional[str],
        optional_params:dict,
        logging_obj: Any,
        timeout: Optional[Union[float, httpx.Timeout]]=None,
        client: Optional[AsyncHTTPHandler]=None,
)-> ImageResponse:
# Your custom image edit logic here
# e.g., call Stability AI, Black Forest Labs, etc.
return ImageResponse(
            created=int(time.time()),
            data=[ImageObject(url="https://example.com/edited-image.png")],
)

my_custom_llm = MyCustomLLM()
```

2. Add to `config.yaml`

In the config below, we pass

python\_filename: `custom_handler.py` custom\_handler\_instance\_name: `my_custom_llm`. This is defined in Step 1

custom\_handler: `custom_handler.my_custom_llm`

```
model_list:
-model_name:"my-custom-image-edit-model"
litellm_params:
model:"my-custom-llm/my-model"

litellm_settings:
custom_provider_map:
-{"provider":"my-custom-llm","custom_handler": custom_handler.my_custom_llm}
```

```
litellm --config /path/to/config.yaml
```

3. Test it!

```
curl -X POST 'http://0.0.0.0:4000/v1/images/edits' \
-H 'Authorization: Bearer sk-1234' \
-F 'model=my-custom-image-edit-model' \
-F 'image=@/path/to/image.png' \
-F 'prompt=Make the sky blue'
```

Expected Response

```
{
    "created": 1721955063,
    "data": [{"url": "https://example.com/edited-image.png"}],
}
```

## Anthropic `/v1/messages`[​](#anthropic-v1messages "Direct link to anthropic-v1messages")

- Write the integration for .acompletion
- litellm will transform it to /v1/messages

<!--THE END-->

1. Setup your `custom_handler.py` file

```
import litellm
from litellm import CustomLLM, completion, get_llm_provider


classMyCustomLLM(CustomLLM):
asyncdefacompletion(self,*args,**kwargs)-> litellm.ModelResponse:
return litellm.completion(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":"Hello world"}],
            mock_response="Hi!",
)# type: ignore


my_custom_llm = MyCustomLLM()
```

2. Add to `config.yaml`

In the config below, we pass

python\_filename: `custom_handler.py` custom\_handler\_instance\_name: `my_custom_llm`. This is defined in Step 1

custom\_handler: `custom_handler.my_custom_llm`

```
model_list:
-model_name:"test-model"
litellm_params:
model:"openai/text-embedding-ada-002"
-model_name:"my-custom-model"
litellm_params:
model:"my-custom-llm/my-model"

litellm_settings:
custom_provider_map:
-{"provider":"my-custom-llm","custom_handler": custom_handler.my_custom_llm}
```

```
litellm --config /path/to/config.yaml
```

3. Test it!

```
curl -L -X POST 'http://0.0.0.0:4000/v1/messages' \
-H 'anthropic-version: 2023-06-01' \
-H 'content-type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
   "model": "my-custom-model",
     "max_tokens": 1024,
     "messages": [{
         "role": "user",
         "content": [
         {
             "type": "text",
             "text": "What are the key findings in this document 12?"
         }]
     }]
}'
```

Expected Response

```
{
"id":"chatcmpl-Bm4qEp4h4vCe7Zi4Gud1MAxTWgibO",
"type":"message",
"role":"assistant",
"model":"gpt-3.5-turbo-0125",
"stop_sequence":null,
"usage":{
"input_tokens":18,
"output_tokens":44
},
"content":[
{
"type":"text",
"text":"Without the specific document being provided, it is not possible to determine the key findings within it. If you can provide the content or a summary of document 12, I would be happy to help identify the key findings."
}
],
"stop_reason":"end_turn"
}
```

## Additional Parameters[​](#additional-parameters "Direct link to Additional Parameters")

Additional parameters are passed inside `optional_params` key in the `completion` or `image_generation` function.

Here's how to set this:

- SDK
- Proxy

```
import litellm
from litellm import CustomLLM, completion, get_llm_provider


classMyCustomLLM(CustomLLM):
defcompletion(self,*args,**kwargs)-> litellm.ModelResponse:
assert kwargs["optional_params"]=={"my_custom_param":"my-custom-param"}# 👈 CHECK HERE
return litellm.completion(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":"Hello world"}],
            mock_response="Hi!",
)# type: ignore

my_custom_llm = MyCustomLLM()

litellm.custom_provider_map =[# 👈 KEY STEP - REGISTER HANDLER
{"provider":"my-custom-llm","custom_handler": my_custom_llm}
]

resp = completion(model="my-custom-llm/my-model", my_custom_param="my-custom-param")
```

## Custom Handler Spec[​](#custom-handler-spec "Direct link to Custom Handler Spec")

```
from litellm.types.utils import GenericStreamingChunk, ModelResponse, ImageResponse
from typing import Iterator, AsyncIterator, Any, Optional, Union
from litellm.llms.base import BaseLLM

classCustomLLMError(Exception):# use this for all your exceptions
def__init__(
        self,
        status_code,
        message,
):
        self.status_code = status_code
        self.message = message
super().__init__(
            self.message
)# Call the base class constructor with the parameters it needs

classCustomLLM(BaseLLM):
def__init__(self)->None:
super().__init__()

defcompletion(self,*args,**kwargs)-> ModelResponse:
raise CustomLLMError(status_code=500, message="Not implemented yet!")

defstreaming(self,*args,**kwargs)-> Iterator[GenericStreamingChunk]:
raise CustomLLMError(status_code=500, message="Not implemented yet!")

asyncdefacompletion(self,*args,**kwargs)-> ModelResponse:
raise CustomLLMError(status_code=500, message="Not implemented yet!")

asyncdefastreaming(self,*args,**kwargs)-> AsyncIterator[GenericStreamingChunk]:
raise CustomLLMError(status_code=500, message="Not implemented yet!")

defimage_generation(
        self,
        model:str,
        prompt:str,
        model_response: ImageResponse,
        optional_params:dict,
        logging_obj: Any,
        timeout: Optional[Union[float, httpx.Timeout]]=None,
        client: Optional[HTTPHandler]=None,
)-> ImageResponse:
raise CustomLLMError(status_code=500, message="Not implemented yet!")

asyncdefaimage_generation(
        self,
        model:str,
        prompt:str,
        model_response: ImageResponse,
        optional_params:dict,
        logging_obj: Any,
        timeout: Optional[Union[float, httpx.Timeout]]=None,
        client: Optional[AsyncHTTPHandler]=None,
)-> ImageResponse:
raise CustomLLMError(status_code=500, message="Not implemented yet!")

defimage_edit(
        self,
        model:str,
        image: Any,
        prompt:str,
        model_response: ImageResponse,
        api_key: Optional[str],
        api_base: Optional[str],
        optional_params:dict,
        logging_obj: Any,
        timeout: Optional[Union[float, httpx.Timeout]]=None,
        client: Optional[HTTPHandler]=None,
)-> ImageResponse:
raise CustomLLMError(status_code=500, message="Not implemented yet!")

asyncdefaimage_edit(
        self,
        model:str,
        image: Any,
        prompt:str,
        model_response: ImageResponse,
        api_key: Optional[str],
        api_base: Optional[str],
        optional_params:dict,
        logging_obj: Any,
        timeout: Optional[Union[float, httpx.Timeout]]=None,
        client: Optional[AsyncHTTPHandler]=None,
)-> ImageResponse:
raise CustomLLMError(status_code=500, message="Not implemented yet!")
```