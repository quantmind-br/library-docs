---
title: /v1/messages | liteLLM
url: https://docs.litellm.ai/docs/anthropic_unified
source: sitemap
fetched_at: 2026-01-21T19:44:02.120047761-03:00
rendered_js: false
word_count: 529
summary: This document explains how to use LiteLLM to call various LLM APIs using the Anthropic messages format, including implementation details for the Python SDK and proxy server.
tags:
    - litellm
    - anthropic-api
    - messages-format
    - llm-proxy
    - python-sdk
    - api-integration
category: api
---

Use LiteLLM to call all your LLM APIs in the Anthropic `v1/messages` format.

## Overview[​](#overview "Direct link to Overview")

FeatureSupportedNotesCost Tracking✅Works with all supported modelsLogging✅Works across all integrationsEnd-user Tracking✅Streaming✅Fallbacks✅Works between supported modelsLoadbalancing✅Works between supported modelsGuardrails✅Applies to input and output text (non-streaming only)Supported Providers**All LiteLLM supported providers**`openai`, `anthropic`, `bedrock`, `vertex_ai`, `gemini`, `azure`, `azure_ai`, etc.

## Usage[​](#usage "Direct link to Usage")

* * *

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

- Anthropic
- OpenAI
- Google AI Studio
- Vertex AI
- AWS Bedrock

#### Non-streaming example[​](#non-streaming-example "Direct link to Non-streaming example")

Anthropic Example using LiteLLM Python SDK

```
import litellm
response =await litellm.anthropic.messages.acreate(
    messages=[{"role":"user","content":"Hello, can you tell me a short joke?"}],
    api_key=api_key,
    model="anthropic/claude-3-haiku-20240307",
    max_tokens=100,
)
```

#### Streaming example[​](#streaming-example "Direct link to Streaming example")

Anthropic Streaming Example using LiteLLM Python SDK

```
import litellm
response =await litellm.anthropic.messages.acreate(
    messages=[{"role":"user","content":"Hello, can you tell me a short joke?"}],
    api_key=api_key,
    model="anthropic/claude-3-haiku-20240307",
    max_tokens=100,
    stream=True,
)
asyncfor chunk in response:
print(chunk)
```

Example response:

```
{
"content":[
{
"text":"Hi! this is a very short joke",
"type":"text"
}
],
"id":"msg_013Zva2CMHLNnXjNJJKqJ2EF",
"model":"claude-3-7-sonnet-20250219",
"role":"assistant",
"stop_reason":"end_turn",
"stop_sequence":null,
"type":"message",
"usage":{
"input_tokens":2095,
"output_tokens":503,
"cache_creation_input_tokens":2095,
"cache_read_input_tokens":0
}
}
```

### LiteLLM Proxy Server[​](#litellm-proxy-server "Direct link to LiteLLM Proxy Server")

- Anthropic
- OpenAI
- Google AI Studio
- Vertex AI
- AWS Bedrock
- curl

<!--THE END-->

1. Setup config.yaml

```
model_list:
-model_name: anthropic-claude
litellm_params:
model: claude-3-7-sonnet-latest
api_key: os.environ/ANTHROPIC_API_KEY
```

2. Start proxy

```
litellm --config /path/to/config.yaml
```

3. Test it!

Anthropic Example using LiteLLM Proxy Server

```
import anthropic

# point anthropic sdk to litellm proxy 
client = anthropic.Anthropic(
    base_url="http://0.0.0.0:4000",
    api_key="sk-1234",
)

response = client.messages.create(
    messages=[{"role":"user","content":"Hello, can you tell me a short joke?"}],
    model="anthropic-claude",
    max_tokens=100,
)
```

## Request Format[​](#request-format "Direct link to Request Format")

* * *

Request body will be in the Anthropic messages API format. **litellm follows the Anthropic messages specification for this endpoint.**

#### Example request body[​](#example-request-body "Direct link to Example request body")

```
{
"model":"claude-3-7-sonnet-20250219",
"max_tokens":1024,
"messages":[
{
"role":"user",
"content":"Hello, world"
}
]
}
```

#### Required Fields[​](#required-fields "Direct link to Required Fields")

- **model** (string):  
  The model identifier (e.g., `"claude-3-7-sonnet-20250219"`).
- **max\_tokens** (integer):  
  The maximum number of tokens to generate before stopping.  
  *Note: The model may stop before reaching this limit; value must be greater than 1.*
- **messages** (array of objects):  
  An ordered list of conversational turns.  
  Each message object must include:
  
  - **role** (enum: `"user"` or `"assistant"`):  
    Specifies the speaker of the message.
  - **content** (string or array of content blocks):  
    The text or content blocks (e.g., an array containing objects with a `type` such as `"text"`) that form the message.  
    *Example equivalence:*
    
    ```
    {"role":"user","content":"Hello, Claude"}
    ```
    
    is equivalent to:
    
    ```
    {"role":"user","content":[{"type":"text","text":"Hello, Claude"}]}
    ```

#### Optional Fields[​](#optional-fields "Direct link to Optional Fields")

- **metadata** (object):  
  Contains additional metadata about the request (e.g., `user_id` as an opaque identifier).
- **stop\_sequences** (array of strings):  
  Custom sequences that, when encountered in the generated text, cause the model to stop.
- **stream** (boolean):  
  Indicates whether to stream the response using server-sent events.
- **system** (string or array):  
  A system prompt providing context or specific instructions to the model.
- **temperature** (number):  
  Controls randomness in the model's responses. Valid range: `0 < temperature < 1`.
- **thinking** (object):  
  Configuration for enabling extended thinking. If enabled, it includes:
  
  - **budget\_tokens** (integer):  
    Minimum of 1024 tokens (and less than `max_tokens`).
  - **type** (enum):  
    E.g., `"enabled"`.
- **tool\_choice** (object):  
  Instructs how the model should utilize any provided tools.
- **tools** (array of objects):  
  Definitions for tools available to the model. Each tool includes:
  
  - **name** (string):  
    The tool's name.
  - **description** (string):  
    A detailed description of the tool.
  - **input\_schema** (object):  
    A JSON schema describing the expected input format for the tool.
- **top\_k** (integer):  
  Limits sampling to the top K options.
- **top\_p** (number):  
  Enables nucleus sampling with a cumulative probability cutoff. Valid range: `0 < top_p < 1`.

## Response Format[​](#response-format "Direct link to Response Format")

* * *

Responses will be in the Anthropic messages API format.

#### Example Response[​](#example-response "Direct link to Example Response")

```
{
"content":[
{
"text":"Hi! My name is Claude.",
"type":"text"
}
],
"id":"msg_013Zva2CMHLNnXjNJJKqJ2EF",
"model":"claude-3-7-sonnet-20250219",
"role":"assistant",
"stop_reason":"end_turn",
"stop_sequence":null,
"type":"message",
"usage":{
"input_tokens":2095,
"output_tokens":503,
"cache_creation_input_tokens":2095,
"cache_read_input_tokens":0
}
}
```

#### Response fields[​](#response-fields "Direct link to Response fields")

- **content** (array of objects):  
  Contains the generated content blocks from the model. Each block includes:
  
  - **type** (string):  
    Indicates the type of content (e.g., `"text"`, `"tool_use"`, `"thinking"`, or `"redacted_thinking"`).
  - **text** (string):  
    The generated text from the model.  
    *Note: Maximum length is 5,000,000 characters.*
  - **citations** (array of objects or `null`):  
    Optional field providing citation details. Each citation includes:
    
    - **cited\_text** (string):  
      The excerpt being cited.
    - **document\_index** (integer):  
      An index referencing the cited document.
    - **document\_title** (string or `null`):  
      The title of the cited document.
    - **start\_char\_index** (integer):  
      The starting character index for the citation.
    - **end\_char\_index** (integer):  
      The ending character index for the citation.
    - **type** (string):  
      Typically `"char_location"`.
- **id** (string):  
  A unique identifier for the response message.  
  *Note: The format and length of IDs may change over time.*
- **model** (string):  
  Specifies the model that generated the response.
- **role** (string):  
  Indicates the role of the generated message. For responses, this is always `"assistant"`.
- **stop\_reason** (string):  
  Explains why the model stopped generating text. Possible values include:
  
  - `"end_turn"`: The model reached a natural stopping point.
  - `"max_tokens"`: The generation stopped because the maximum token limit was reached.
  - `"stop_sequence"`: A custom stop sequence was encountered.
  - `"tool_use"`: The model invoked one or more tools.
- **stop\_sequence** (string or `null`):  
  Contains the specific stop sequence that caused the generation to halt, if applicable; otherwise, it is `null`.
- **type** (string):  
  Denotes the type of response object, which is always `"message"`.
- **usage** (object):  
  Provides details on token usage for billing and rate limiting. This includes:
  
  - **input\_tokens** (integer):  
    Total number of input tokens processed.
  - **output\_tokens** (integer):  
    Total number of output tokens generated.
  - **cache\_creation\_input\_tokens** (integer or `null`):  
    Number of tokens used to create a cache entry.
  - **cache\_read\_input\_tokens** (integer or `null`):  
    Number of tokens read from the cache.