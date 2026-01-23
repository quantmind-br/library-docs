---
title: Call any LiteLLM model in your custom format | liteLLM
url: https://docs.litellm.ai/docs/extras/creating_adapters
source: sitemap
fetched_at: 2026-01-21T19:45:16.552261767-03:00
rendered_js: false
word_count: 156
summary: This document explains how to create and implement custom adapters in LiteLLM to translate between proprietary API request/response formats and the internal OpenAI-compatible standard.
tags:
    - litellm
    - custom-adapters
    - api-translation
    - python-sdk
    - llm-integration
    - streaming
    - async-support
category: guide
---

Use this to call any LiteLLM supported `.completion()` model, in your custom format. Useful if you have a custom API and want to support any LiteLLM supported model.

## How it works[​](#how-it-works "Direct link to How it works")

Your request → Adapter translates to OpenAI format → LiteLLM processes it → Adapter translates response back → Your response

## Create an Adapter[​](#create-an-adapter "Direct link to Create an Adapter")

Inherit from `CustomLogger` and implement 3 methods:

```
from litellm.integrations.custom_logger import CustomLogger
from litellm.types.llms.openai import ChatCompletionRequest
from litellm.types.utils import ModelResponse

classMyAdapter(CustomLogger):
deftranslate_completion_input_params(self, kwargs)-> ChatCompletionRequest:
"""Convert your format → OpenAI format"""
# Example: Anthropic to OpenAI
return{
"model": kwargs["model"],
"messages": self._convert_messages(kwargs["messages"]),
"max_tokens": kwargs.get("max_tokens"),
}

deftranslate_completion_output_params(self, response: ModelResponse):
"""Convert OpenAI format → your format"""
# Return your provider's response format
return MyProviderResponse(
id=response.id,
            content=response.choices[0].message.content,
            usage=response.usage,
)

deftranslate_completion_output_params_streaming(self, completion_stream):
"""Handle streaming responses"""
return MyStreamWrapper(completion_stream)
```

## Register it[​](#register-it "Direct link to Register it")

```
import litellm

my_adapter = MyAdapter()
litellm.adapters =[{"id":"my_provider","adapter": my_adapter}]
```

## Use it[​](#use-it "Direct link to Use it")

```
from litellm import adapter_completion

# Now you can use your provider's format with any LiteLLM model
response = adapter_completion(
    adapter_id="my_provider",
    model="gpt-4",# or any LiteLLM model
    messages=[{"role":"user","content":"hello"}],
    max_tokens=100
)
```

### Streaming[​](#streaming "Direct link to Streaming")

```
stream = adapter_completion(
    adapter_id="my_provider",
    model="gpt-4",
    messages=[{"role":"user","content":"hello"}],
    stream=True
)

for chunk in stream:
print(chunk)
```

### Async[​](#async "Direct link to Async")

```
from litellm import aadapter_completion

response =await aadapter_completion(
    adapter_id="my_provider",
    model="gpt-4",
    messages=[{"role":"user","content":"hello"}]
)
```

## Example: Anthropic Adapter[​](#example-anthropic-adapter "Direct link to Example: Anthropic Adapter")

Here's how we translate Anthropic's format:

### Input Translation[​](#input-translation "Direct link to Input Translation")

```
deftranslate_completion_input_params(self, kwargs):
    model = kwargs.pop("model")
    messages = kwargs.pop("messages")

# Convert Anthropic messages to OpenAI format
    openai_messages =[]
for msg in messages:
if msg["role"]=="user":
            openai_messages.append({
"role":"user",
"content": msg["content"]
})

# Handle system message
if"system"in kwargs:
        openai_messages.insert(0,{
"role":"system",
"content": kwargs.pop("system")
})

return{
"model": model,
"messages": openai_messages,
**kwargs  # pass through other params
}
```

### Output Translation[​](#output-translation "Direct link to Output Translation")

```
deftranslate_completion_output_params(self, response):
return AnthropicResponse(
id=response.id,
type="message",
        role="assistant",
        content=[{
"type":"text",
"text": response.choices[0].message.content
}],
        usage={
"input_tokens": response.usage.prompt_tokens,
"output_tokens": response.usage.completion_tokens
}
)
```

### Streaming[​](#streaming-1 "Direct link to Streaming")

```
from litellm.types.utils import AdapterCompletionStreamWrapper

classAnthropicStreamWrapper(AdapterCompletionStreamWrapper):
def__init__(self, completion_stream, model):
super().__init__(completion_stream)
        self.model = model
        self.first_chunk =True

asyncdef__anext__(self):
# First chunk
if self.first_chunk:
            self.first_chunk =False
return{"type":"message_start","message":{...}}

# Stream chunks
asyncfor chunk in self.completion_stream:
return{
"type":"content_block_delta",
"delta":{"text": chunk.choices[0].delta.content}
}

# Last chunk
return{"type":"message_stop"}

deftranslate_completion_output_params_streaming(self, stream, model):
return AnthropicStreamWrapper(stream, model)
```

## Use with Proxy[​](#use-with-proxy "Direct link to Use with Proxy")

Add to your proxy config:

```
general_settings:
pass_through_endpoints:
-path:"/v1/messages"
target:"my_module.MyAdapter"
```

Then call it:

```
curl http://localhost:4000/v1/messages \
  -H "Authorization: Bearer sk-1234" \
  -d '{"model": "gpt-4", "messages": [...]}'
```

## Real Example[​](#real-example "Direct link to Real Example")

Check out the full Anthropic adapter:

- [transformation.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/anthropic/experimental_pass_through/adapters/transformation.py)
- [handler.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/anthropic/experimental_pass_through/adapters/handler.py)
- [streaming\_iterator.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/anthropic/experimental_pass_through/adapters/streaming_iterator.py)

## That's it[​](#thats-it "Direct link to That's it")

1. Create a class that inherits `CustomLogger`
2. Implement the 3 translation methods
3. Register with `litellm.adapters = [{"id": "...", "adapter": ...}]`
4. Call with `adapter_completion(adapter_id="...")`

<!--THE END-->

- [How it works](#how-it-works)
- [Create an Adapter](#create-an-adapter)
- [Register it](#register-it)
- [Use it](#use-it)
  
  - [Streaming](#streaming)
  - [Async](#async)
- [Example: Anthropic Adapter](#example-anthropic-adapter)
  
  - [Input Translation](#input-translation)
  - [Output Translation](#output-translation)
  - [Streaming](#streaming-1)
- [Use with Proxy](#use-with-proxy)
- [Real Example](#real-example)
- [That's it](#thats-it)