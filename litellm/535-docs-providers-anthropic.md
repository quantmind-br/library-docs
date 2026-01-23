---
title: Anthropic | liteLLM
url: https://docs.litellm.ai/docs/providers/anthropic
source: sitemap
fetched_at: 2026-01-21T19:47:51.375666059-03:00
rendered_js: false
word_count: 1138
summary: This document provides technical details and instructions for integrating Anthropic's Claude models with LiteLLM, covering model versions, parameter mapping, and structured output support.
tags:
    - litellm
    - anthropic
    - claude
    - api-integration
    - structured-outputs
    - azure-foundry
category: reference
---

LiteLLM supports all anthropic models.

- `claude-sonnet-4-5-20250929`
- `claude-opus-4-5-20251101`
- `claude-opus-4-1-20250805`
- `claude-4` (`claude-opus-4-20250514`, `claude-sonnet-4-20250514`)
- `claude-3.7` (`claude-3-7-sonnet-20250219`)
- `claude-3.5` (`claude-3-5-sonnet-20240620`)
- `claude-3` (`claude-3-haiku-20240307`, `claude-3-opus-20240229`, `claude-3-sonnet-20240229`)
- `claude-2`
- `claude-2.1`
- `claude-instant-1.2`

PropertyDetailsDescriptionClaude is a highly performant, trustworthy, and intelligent AI platform built by Anthropic. Claude excels at tasks involving language, reasoning, analysis, coding, and more. Also available via Azure Foundry.Provider Route on LiteLLM`anthropic/` (add this prefix to the model name, to route any requests to Anthropic - e.g. `anthropic/claude-3-5-sonnet-20240620`). For Azure Foundry deployments, use `azure/claude-*` (see [Azure Anthropic documentation](https://docs.litellm.ai/docs/providers/azure/azure_anthropic))Provider Doc[Anthropic ↗](https://docs.anthropic.com/en/docs/build-with-claude/overview), [Azure Foundry Claude ↗](https://learn.microsoft.com/en-us/azure/ai-services/foundry-models/claude)API Endpoint for Provider[https://api.anthropic.com](https://api.anthropic.com) (or Azure Foundry endpoint: `https://<resource-name>.services.ai.azure.com/anthropic`)Supported Endpoints`/chat/completions`, `/v1/messages` (passthrough)

## Supported OpenAI Parameters[​](#supported-openai-parameters "Direct link to Supported OpenAI Parameters")

Check this in code, [here](https://docs.litellm.ai/docs/completion/input#translated-openai-params)

```
"stream",
"stop",
"temperature",
"top_p",
"max_tokens",
"max_completion_tokens",
"tools",
"tool_choice",
"extra_headers",
"parallel_tool_calls",
"response_format",
"user",
"reasoning_effort",
```

info

**Notes:**

- Anthropic API fails requests when `max_tokens` are not passed. Due to this litellm passes `max_tokens=4096` when no `max_tokens` are passed.
- `response_format` is fully supported for Claude Sonnet 4.5 and Opus 4.1 models (see [Structured Outputs](#structured-outputs) section)
- `reasoning_effort` is automatically mapped to `output_config={"effort": ...}` for Claude Opus 4.5 models (see [Effort Parameter](https://docs.litellm.ai/docs/providers/anthropic_effort))

## **Structured Outputs**[​](#structured-outputs "Direct link to structured-outputs")

LiteLLM supports Anthropic's [structured outputs feature](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) for Claude Sonnet 4.5 and Opus 4.1 models. When you use `response_format` with these models, LiteLLM automatically:

- Adds the required `structured-outputs-2025-11-13` beta header
- Transforms OpenAI's `response_format` to Anthropic's `output_format` format

### Supported Models[​](#supported-models "Direct link to Supported Models")

- `sonnet-4-5` or `sonnet-4.5` (all Sonnet 4.5 variants)
- `opus-4-1` or `opus-4.1` (all Opus 4.1 variants)
  
  - `opus-4-5` or `opus-4.5` (all Opus 4.5 variants)

### Example Usage[​](#example-usage "Direct link to Example Usage")

- LiteLLM SDK
- LiteLLM Proxy

```
from litellm import completion

response = completion(
    model="claude-sonnet-4-5-20250929",
    messages=[{"role":"user","content":"What is the capital of France?"}],
    response_format={
"type":"json_schema",
"json_schema":{
"name":"capital_response",
"strict":True,
"schema":{
"type":"object",
"properties":{
"country":{"type":"string"},
"capital":{"type":"string"}
},
"required":["country","capital"],
"additionalProperties":False
}
}
}
)

print(response.choices[0].message.content)
# Output: {"country": "France", "capital": "Paris"}
```

info

When using structured outputs with supported models, LiteLLM automatically:

- Converts OpenAI's `response_format` to Anthropic's `output_schema`
- Adds the `anthropic-beta: structured-outputs-2025-11-13` header
- Creates a tool with the schema and forces the model to use it

## API Keys[​](#api-keys "Direct link to API Keys")

```
import os

os.environ["ANTHROPIC_API_KEY"]="your-api-key"
# os.environ["ANTHROPIC_API_BASE"] = "" # [OPTIONAL] or 'ANTHROPIC_BASE_URL'
# os.environ["LITELLM_ANTHROPIC_DISABLE_URL_SUFFIX"] = "true" # [OPTIONAL] Disable automatic URL suffix appending
```

Azure Foundry Support

Claude models are also available via Microsoft Azure Foundry. Use the `azure/` prefix instead of `anthropic/` and configure Azure authentication. See the [Azure Anthropic documentation](https://docs.litellm.ai/docs/providers/azure/azure_anthropic) for details.

Example:

```
response = completion(
    model="azure/claude-sonnet-4-5",
    api_base="https://<resource-name>.services.ai.azure.com/anthropic",
    api_key="your-azure-api-key",
    messages=[{"role":"user","content":"Hello!"}]
)
```

### Custom API Base[​](#custom-api-base "Direct link to Custom API Base")

When using a custom API base for Anthropic (e.g., a proxy or custom endpoint), LiteLLM automatically appends the appropriate suffix (`/v1/messages` or `/v1/complete`) to your base URL.

If your custom endpoint already includes the full path or doesn't follow Anthropic's standard URL structure, you can disable this automatic suffix appending:

```
import os

os.environ["ANTHROPIC_API_BASE"]="https://my-custom-endpoint.com/custom/path"
os.environ["LITELLM_ANTHROPIC_DISABLE_URL_SUFFIX"]="true"# Prevents automatic suffix
```

Without `LITELLM_ANTHROPIC_DISABLE_URL_SUFFIX`:

- Base URL `https://my-proxy.com` → `https://my-proxy.com/v1/messages`
- Base URL `https://my-proxy.com/api` → `https://my-proxy.com/api/v1/messages`

With `LITELLM_ANTHROPIC_DISABLE_URL_SUFFIX=true`:

- Base URL `https://my-proxy.com/custom/path` → `https://my-proxy.com/custom/path` (unchanged)

### Azure AI Foundry (Alternative Method)[​](#azure-ai-foundry-alternative-method "Direct link to Azure AI Foundry (Alternative Method)")

Recommended Method

For full Azure support including Azure AD authentication, use the dedicated [Azure Anthropic provider](https://docs.litellm.ai/docs/providers/azure/azure_anthropic) with `azure_ai/` prefix.

As an alternative, you can use the `anthropic/` provider directly with your Azure endpoint since Azure exposes Claude using Anthropic's native API.

```
from litellm import completion

response = completion(
    model="anthropic/claude-sonnet-4-5",
    api_base="https://<your-resource>.services.ai.azure.com/anthropic",
    api_key="<your-azure-api-key>",
    messages=[{"role":"user","content":"Hello!"}],
)
print(response)
```

info

**Finding your Azure endpoint:** Go to Azure AI Foundry → Your deployment → Overview. Your base URL will be `https://<resource-name>.services.ai.azure.com/anthropic`

## Usage[​](#usage "Direct link to Usage")

```
import os
from litellm import completion

# set env - [OPTIONAL] replace with your anthropic key
os.environ["ANTHROPIC_API_KEY"]="your-api-key"

messages =[{"role":"user","content":"Hey! how's it going?"}]
response = completion(model="claude-opus-4-20250514", messages=messages)
print(response)
```

## Usage - Streaming[​](#usage---streaming "Direct link to Usage - Streaming")

Just set `stream=True` when calling completion.

```
import os
from litellm import completion

# set env
os.environ["ANTHROPIC_API_KEY"]="your-api-key"

messages =[{"role":"user","content":"Hey! how's it going?"}]
response = completion(model="claude-opus-4-20250514", messages=messages, stream=True)
for chunk in response:
print(chunk["choices"][0]["delta"]["content"])# same as openai format
```

## Usage with LiteLLM Proxy[​](#usage-with-litellm-proxy "Direct link to Usage with LiteLLM Proxy")

Here's how to call Anthropic with the LiteLLM Proxy Server

### 1. Save key in your environment[​](#1-save-key-in-your-environment "Direct link to 1. Save key in your environment")

```
export ANTHROPIC_API_KEY="your-api-key"
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

- config.yaml
- config - default all Anthropic Model
- cli

```
model_list:
-model_name: claude-4### RECEIVED MODEL NAME ###
litellm_params:# all params accepted by litellm.completion() - https://docs.litellm.ai/docs/completion/input
model: claude-opus-4-20250514### MODEL NAME sent to `litellm.completion()` ###
api_key:"os.environ/ANTHROPIC_API_KEY"# does os.getenv("ANTHROPIC_API_KEY")
```

```
litellm --config /path/to/config.yaml
```

### 3. Test it[​](#3-test-it "Direct link to 3. Test it")

- Curl Request
- OpenAI v1.0.0+
- Langchain

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "claude-3",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ]
    }
'
```

## Supported Models[​](#supported-models-1 "Direct link to Supported Models")

`Model Name` 👉 Human-friendly name.  
`Function Call` 👉 How to call the model in LiteLLM.

Model NameFunction Callclaude-sonnet-4-5`completion('claude-sonnet-4-5-20250929', messages)`claude-opus-4`completion('claude-opus-4-20250514', messages)`claude-sonnet-4`completion('claude-sonnet-4-20250514', messages)`claude-3.7`completion('claude-3-7-sonnet-20250219', messages)`claude-3-5-sonnet`completion('claude-3-5-sonnet-20240620', messages)`claude-3-haiku`completion('claude-3-haiku-20240307', messages)`claude-3-opus`completion('claude-3-opus-20240229', messages)`claude-3-5-sonnet-20240620`completion('claude-3-5-sonnet-20240620', messages)`claude-3-sonnet`completion('claude-3-sonnet-20240229', messages)`claude-2.1`completion('claude-2.1', messages)`claude-2`completion('claude-2', messages)`claude-instant-1.2`completion('claude-instant-1.2', messages)`claude-instant-1`completion('claude-instant-1', messages)`

## **Prompt Caching**[​](#prompt-caching "Direct link to prompt-caching")

Use Anthropic Prompt Caching

[Relevant Anthropic API Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)

note

Here's what a sample Raw Request from LiteLLM for Anthropic Context Caching looks like:

```
POST Request Sent from LiteLLM:
curl -X POST \
https://api.anthropic.com/v1/messages \
-H 'accept: application/json' -H 'anthropic-version: 2023-06-01' -H 'content-type: application/json' -H 'x-api-key: sk-...' \
-d '{'model': 'claude-3-5-sonnet-20240620', [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What are the key terms and conditions in this agreement?",
          "cache_control": {
            "type": "ephemeral"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "Certainly! The key terms and conditions are the following: the contract is 1 year long for $10/mo"
        }
      ]
    }
  ],
  "temperature": 0.2,
  "max_tokens": 10
}'
```

**Note:** Anthropic no longer requires the `anthropic-beta: prompt-caching-2024-07-31` header. Prompt caching now works automatically when you use `cache_control` in your messages.

### Caching - Large Context Caching[​](#caching---large-context-caching "Direct link to Caching - Large Context Caching")

This example demonstrates basic Prompt Caching usage, caching the full text of the legal agreement as a prefix while keeping the user instruction uncached.

- LiteLLM SDK
- LiteLLM Proxy

```
response =await litellm.acompletion(
    model="anthropic/claude-3-5-sonnet-20240620",
    messages=[
{
"role":"system",
"content":[
{
"type":"text",
"text":"You are an AI assistant tasked with analyzing legal documents.",
},
{
"type":"text",
"text":"Here is the full text of a complex legal agreement",
"cache_control":{"type":"ephemeral"},
},
],
},
{
"role":"user",
"content":"what are the key terms and conditions in this agreement?",
},
]
)

```

### Caching - Tools definitions[​](#caching---tools-definitions "Direct link to Caching - Tools definitions")

In this example, we demonstrate caching tool definitions.

The cache\_control parameter is placed on the final tool

- LiteLLM SDK
- LiteLLM Proxy

```
import litellm

response =await litellm.acompletion(
    model="anthropic/claude-3-5-sonnet-20240620",
    messages =[{"role":"user","content":"What's the weather like in Boston today?"}]
    tools =[
{
"type":"function",
"function":{
"name":"get_current_weather",
"description":"Get the current weather in a given location",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"The city and state, e.g. San Francisco, CA",
},
"unit":{"type":"string","enum":["celsius","fahrenheit"]},
},
"required":["location"],
},
"cache_control":{"type":"ephemeral"}
},
}
]
)
```

### Caching - Continuing Multi-Turn Convo[​](#caching---continuing-multi-turn-convo "Direct link to Caching - Continuing Multi-Turn Convo")

In this example, we demonstrate how to use Prompt Caching in a multi-turn conversation.

The cache\_control parameter is placed on the system message to designate it as part of the static prefix.

The conversation history (previous messages) is included in the messages array. The final turn is marked with cache-control, for continuing in followups. The second-to-last user message is marked for caching with the cache\_control parameter, so that this checkpoint can read from the previous cache.

- LiteLLM SDK
- LiteLLM Proxy

```
import litellm

response =await litellm.acompletion(
    model="anthropic/claude-3-5-sonnet-20240620",
    messages=[
# System Message
{
"role":"system",
"content":[
{
"type":"text",
"text":"Here is the full text of a complex legal agreement"
*400,
"cache_control":{"type":"ephemeral"},
}
],
},
# marked for caching with the cache_control parameter, so that this checkpoint can read from the previous cache.
{
"role":"user",
"content":[
{
"type":"text",
"text":"What are the key terms and conditions in this agreement?",
"cache_control":{"type":"ephemeral"},
}
],
},
{
"role":"assistant",
"content":"Certainly! the key terms and conditions are the following: the contract is 1 year long for $10/mo",
},
# The final turn is marked with cache-control, for continuing in followups.
{
"role":"user",
"content":[
{
"type":"text",
"text":"What are the key terms and conditions in this agreement?",
"cache_control":{"type":"ephemeral"},
}
],
},
]
)
```

```
from litellm import completion

# set env
os.environ["ANTHROPIC_API_KEY"]="your-api-key"

tools =[
{
"type":"function",
"function":{
"name":"get_current_weather",
"description":"Get the current weather in a given location",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"The city and state, e.g. San Francisco, CA",
},
"unit":{"type":"string","enum":["celsius","fahrenheit"]},
},
"required":["location"],
},
},
}
]
messages =[{"role":"user","content":"What's the weather like in Boston today?"}]

response = completion(
    model="anthropic/claude-3-opus-20240229",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)
# Add any assertions, here to check response args
print(response)
assertisinstance(response.choices[0].message.tool_calls[0].function.name,str)
assertisinstance(
    response.choices[0].message.tool_calls[0].function.arguments,str
)

```

### Forcing Anthropic Tool Use[​](#forcing-anthropic-tool-use "Direct link to Forcing Anthropic Tool Use")

If you want Claude to use a specific tool to answer the user’s question

You can do this by specifying the tool in the `tool_choice` field like so:

```
response = completion(
    model="anthropic/claude-3-opus-20240229",
    messages=messages,
    tools=tools,
    tool_choice={"type":"tool","name":"get_weather"},
)
```

### Disable Tool Calling[​](#disable-tool-calling "Direct link to Disable Tool Calling")

You can disable tool calling by setting the `tool_choice` to `"none"`.

- SDK
- Proxy

```
from litellm import completion

response = completion(
    model="anthropic/claude-3-opus-20240229",
    messages=messages,
    tools=tools,
    tool_choice="none",
)

```

### MCP Tool Calling[​](#mcp-tool-calling "Direct link to MCP Tool Calling")

Here's how to use MCP tool calling with Anthropic:

- LiteLLM SDK
- LiteLLM Proxy

LiteLLM supports MCP tool calling with Anthropic in the OpenAI Responses API format.

- OpenAI Format
- Anthropic Format

```
import os 
from litellm import completion

os.environ["ANTHROPIC_API_KEY"]="sk-ant-..."

tools=[
{
"type":"mcp",
"server_label":"deepwiki",
"server_url":"https://mcp.deepwiki.com/mcp",
"require_approval":"never",
},
]

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=[{"role":"user","content":"Who won the World Cup in 2022?"}],
    tools=tools
)
```

### Parallel Function Calling[​](#parallel-function-calling "Direct link to Parallel Function Calling")

Here's how to pass the result of a function call back to an anthropic model:

```
from litellm import completion
import os 

os.environ["ANTHROPIC_API_KEY"]="sk-ant.."


litellm.set_verbose =True

### 1ST FUNCTION CALL ###
tools =[
{
"type":"function",
"function":{
"name":"get_current_weather",
"description":"Get the current weather in a given location",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"The city and state, e.g. San Francisco, CA",
},
"unit":{"type":"string","enum":["celsius","fahrenheit"]},
},
"required":["location"],
},
},
}
]
messages =[
{
"role":"user",
"content":"What's the weather like in Boston today in Fahrenheit?",
}
]
try:
# test without max tokens
    response = completion(
        model="anthropic/claude-3-opus-20240229",
        messages=messages,
        tools=tools,
        tool_choice="auto",
)
# Add any assertions, here to check response args
print(response)
assertisinstance(response.choices[0].message.tool_calls[0].function.name,str)
assertisinstance(
        response.choices[0].message.tool_calls[0].function.arguments,str
)

    messages.append(
        response.choices[0].message.model_dump()
)# Add assistant tool invokes
    tool_result =(
'{"location": "Boston", "temperature": "72", "unit": "fahrenheit"}'
)
# Add user submitted tool results in the OpenAI format
    messages.append(
{
"tool_call_id": response.choices[0].message.tool_calls[0].id,
"role":"tool",
"name": response.choices[0].message.tool_calls[0].function.name,
"content": tool_result,
}
)
### 2ND FUNCTION CALL ###
# In the second response, Claude should deduce answer from tool results
    second_response = completion(
        model="anthropic/claude-3-opus-20240229",
        messages=messages,
        tools=tools,
        tool_choice="auto",
)
print(second_response)
except Exception as e:
print(f"An error occurred - {str(e)}")
```

s/o @[Shekhar Patnaik](https://www.linkedin.com/in/patnaikshekhar) for requesting this!

### Context Management (Beta)[​](#context-management-beta "Direct link to Context Management (Beta)")

Anthropic’s [context editing](https://docs.claude.com/en/docs/build-with-claude/context-editing) API lets you automatically clear older tool results or thinking blocks. LiteLLM now forwards the native `context_management` payload when you call Anthropic models, and automatically attaches the required `context-management-2025-06-27` beta header.

```
from litellm import completion

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=[{"role":"user","content":"Summarize the latest tool results"}],
    context_management={
"edits":[
{
"type":"clear_tool_uses_20250919",
"trigger":{"type":"input_tokens","value":30000},
"keep":{"type":"tool_uses","value":3},
"clear_at_least":{"type":"input_tokens","value":5000},
"exclude_tools":["web_search"],
}
]
},
)
```

### Anthropic Hosted Tools (Computer, Text Editor, Web Search, Memory)[​](#anthropic-hosted-tools-computer-text-editor-web-search-memory "Direct link to Anthropic Hosted Tools (Computer, Text Editor, Web Search, Memory)")

- Computer
- Text Editor
- Web Search
- Memory

```
from litellm import completion

tools =[
{
"type":"computer_20241022",
"function":{
"name":"computer",
"parameters":{
"display_height_px":100,
"display_width_px":100,
"display_number":1,
},
},
}
]
model ="claude-3-5-sonnet-20241022"
messages =[{"role":"user","content":"Save a picture of a cat to my desktop."}]

resp = completion(
    model=model,
    messages=messages,
    tools=tools,
# headers={"anthropic-beta": "computer-use-2024-10-22"},
)

print(resp)
```

## Usage - Vision[​](#usage---vision "Direct link to Usage - Vision")

```
from litellm import completion

# set env
os.environ["ANTHROPIC_API_KEY"]="your-api-key"

defencode_image(image_path):
import base64

withopen(image_path,"rb")as image_file:
return base64.b64encode(image_file.read()).decode("utf-8")


image_path ="../proxy/cached_logo.jpg"
# Getting the base64 string
base64_image = encode_image(image_path)
resp = litellm.completion(
    model="anthropic/claude-3-opus-20240229",
    messages=[
{
"role":"user",
"content":[
{"type":"text","text":"Whats in this image?"},
{
"type":"image_url",
"image_url":{
"url":"data:image/jpeg;base64,"+ base64_image
},
},
],
}
],
)
print(f"\nResponse: {resp}")
```

## Usage - Thinking / `reasoning_content`[​](#usage---thinking--reasoning_content "Direct link to usage---thinking--reasoning_content")

LiteLLM translates OpenAI's `reasoning_effort` to Anthropic's `thinking` parameter. [Code](https://github.com/BerriAI/litellm/blob/23051d89dd3611a81617d84277059cd88b2df511/litellm/llms/anthropic/chat/transformation.py#L298)

reasoning\_effortthinking"low""budget\_tokens": 1024"medium""budget\_tokens": 2048"high""budget\_tokens": 4096

- SDK
- PROXY

```
from litellm import completion

resp = completion(
    model="anthropic/claude-3-7-sonnet-20250219",
    messages=[{"role":"user","content":"What is the capital of France?"}],
    reasoning_effort="low",
)

```

**Expected Response**

```
ModelResponse(
id='chatcmpl-c542d76d-f675-4e87-8e5f-05855f5d0f5e',
    created=1740470510,
    model='claude-3-7-sonnet-20250219',
object='chat.completion',
    system_fingerprint=None,
    choices=[
        Choices(
            finish_reason='stop',
            index=0,
            message=Message(
                content="The capital of France is Paris.",
                role='assistant',
                tool_calls=None,
                function_call=None,
                provider_specific_fields={
'citations':None,
'thinking_blocks':[
{
'type':'thinking',
'thinking':'The capital of France is Paris. This is a very straightforward factual question.',
'signature':'EuYBCkQYAiJAy6...'
}
]
}
),
            thinking_blocks=[
{
'type':'thinking',
'thinking':'The capital of France is Paris. This is a very straightforward factual question.',
'signature':'EuYBCkQYAiJAy6AGB...'
}
],
            reasoning_content='The capital of France is Paris. This is a very straightforward factual question.'
)
],
    usage=Usage(
        completion_tokens=68,
        prompt_tokens=42,
        total_tokens=110,
        completion_tokens_details=None,
        prompt_tokens_details=PromptTokensDetailsWrapper(
            audio_tokens=None,
            cached_tokens=0,
            text_tokens=None,
            image_tokens=None
),
        cache_creation_input_tokens=0,
        cache_read_input_tokens=0
)
)
```

### Pass `thinking` to Anthropic models[​](#pass-thinking-to-anthropic-models "Direct link to pass-thinking-to-anthropic-models")

You can also pass the `thinking` parameter to Anthropic models.

You can also pass the `thinking` parameter to Anthropic models.

- SDK
- PROXY

```
response = litellm.completion(
  model="anthropic/claude-3-7-sonnet-20250219",
  messages=[{"role":"user","content":"What is the capital of France?"}],
  thinking={"type":"enabled","budget_tokens":1024},
)
```

Pass `extra_headers: dict` to `litellm.completion`

```
from litellm import completion
messages =[{"role":"user","content":"What is Anthropic?"}]
response = completion(
    model="claude-3-5-sonnet-20240620",
    messages=messages,
    extra_headers={"anthropic-beta":"max-tokens-3-5-sonnet-2024-07-15"}
)
```

## Usage - "Assistant Pre-fill"[​](#usage---assistant-pre-fill 'Direct link to Usage - "Assistant Pre-fill"')

You can "put words in Claude's mouth" by including an `assistant` role message as the last item in the `messages` array.

> \[!IMPORTANT] The returned completion will *not* include your "pre-fill" text, since it is part of the prompt itself. Make sure to prefix Claude's completion with your pre-fill.

```
import os
from litellm import completion

# set env - [OPTIONAL] replace with your anthropic key
os.environ["ANTHROPIC_API_KEY"]="your-api-key"

messages =[
{"role":"user","content":"How do you say 'Hello' in German? Return your answer as a JSON object, like this:\n\n{ \"Hello\": \"Hallo\" }"},
{"role":"assistant","content":"{"},
]
response = completion(model="claude-2.1", messages=messages)
print(response)
```

#### Example prompt sent to Claude[​](#example-prompt-sent-to-claude "Direct link to Example prompt sent to Claude")

```

Human: How do you say 'Hello' in German? Return your answer as a JSON object, like this:

{ "Hello": "Hallo" }

Assistant: {
```

## Usage - "System" messages[​](#usage---system-messages 'Direct link to Usage - "System" messages')

If you're using Anthropic's Claude 2.1, `system` role messages are properly formatted for you.

```
import os
from litellm import completion

# set env - [OPTIONAL] replace with your anthropic key
os.environ["ANTHROPIC_API_KEY"]="your-api-key"

messages =[
{"role":"system","content":"You are a snarky assistant."},
{"role":"user","content":"How do I boil water?"},
]
response = completion(model="claude-2.1", messages=messages)
```

#### Example prompt sent to Claude[​](#example-prompt-sent-to-claude-1 "Direct link to Example prompt sent to Claude")

```
You are a snarky assistant.

Human: How do I boil water?

Assistant:
```

## Usage - PDF[​](#usage---pdf "Direct link to Usage - PDF")

Pass base64 encoded PDF files to Anthropic models using the `file` content type with a `file_data` field.

- SDK
- PROXY

### **using base64**[​](#using-base64 "Direct link to using-base64")

```
from litellm import completion, supports_pdf_input
import base64
import requests

# URL of the file
url ="https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf"

# Download the file
response = requests.get(url)
file_data = response.content

encoded_file = base64.b64encode(file_data).decode("utf-8")

## check if model supports pdf input - (2024/11/11) only claude-3-5-haiku-20241022 supports it
supports_pdf_input("anthropic/claude-3-5-haiku-20241022")# True

response = completion(
    model="anthropic/claude-3-5-haiku-20241022",
    messages=[
{
"role":"user",
"content":[
{"type":"text","text":"You are a very professional document summarization specialist. Please summarize the given document."},
{
"type":"file",
"file":{
"file_data":f"data:application/pdf;base64,{encoded_file}",# 👈 PDF
}
},
],
}
],
    max_tokens=300,
)

print(response.choices[0])
```

## \[BETA] Citations API[​](#beta-citations-api "Direct link to [BETA] Citations API")

Pass `citations: {"enabled": true}` to Anthropic, to get citations on your document responses.

Note: This interface is in BETA. If you have feedback on how citations should be returned, please [tell us here](https://github.com/BerriAI/litellm/issues/7970#issuecomment-2644437943)

- SDK
- PROXY

```
from litellm import completion

resp = completion(
    model="claude-3-5-sonnet-20241022",
    messages=[
{
"role":"user",
"content":[
{
"type":"document",
"source":{
"type":"text",
"media_type":"text/plain",
"data":"The grass is green. The sky is blue.",
},
"title":"My Document",
"context":"This is a trustworthy document.",
"citations":{"enabled":True},
},
{
"type":"text",
"text":"What color is the grass and sky?",
},
],
}
],
)

citations = resp.choices[0].message.provider_specific_fields["citations"]

assert citations isnotNone
```

## Usage - passing 'user\_id' to Anthropic[​](#usage---passing-user_id-to-anthropic "Direct link to Usage - passing 'user_id' to Anthropic")

LiteLLM translates the OpenAI `user` param to Anthropic's `metadata[user_id]` param.

- SDK
- PROXY

```
response = completion(
    model="claude-3-5-sonnet-20240620",
    messages=messages,
    user="user_123",
)
```

## Usage - Agent Skills[​](#usage---agent-skills "Direct link to Usage - Agent Skills")

LiteLLM supports using Agent Skills with the API

- SDK
- PROXY

```
response = completion(
    model="claude-sonnet-4-5-20250929",
    messages=messages,
    tools=[
{
"type":"code_execution_20250825",
"name":"code_execution"
}
],
    container={
"skills":[
{
"type":"anthropic",
"skill_id":"pptx",
"version":"latest"
}
]
}
)
```

The container and its "id" will be present in "provider\_specific\_fields" in streaming/non-streaming response