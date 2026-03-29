---
title: Structured Outputs (JSON Mode) | liteLLM
url: https://docs.litellm.ai/docs/completion/json_mode
source: sitemap
fetched_at: 2026-01-21T19:44:28.980247293-03:00
rendered_js: false
word_count: 228
summary: This document provides a technical guide on implementing structured outputs and JSON schemas using LiteLLM across various model providers. It details how to check for model compatibility, utilize Pydantic models for response formatting, and enable client-side schema validation.
tags:
    - litellm
    - structured-outputs
    - json-schema
    - pydantic
    - model-compatibility
    - llm-api
    - response-format
category: guide
---

## Quick Start[​](#quick-start "Direct link to Quick Start")

- SDK
- PROXY

```
from litellm import completion
import os 

os.environ["OPENAI_API_KEY"]=""

response = completion(
  model="gpt-4o-mini",
  response_format={"type":"json_object"},
  messages=[
{"role":"system","content":"You are a helpful assistant designed to output JSON."},
{"role":"user","content":"Who won the world series in 2020?"}
]
)
print(response.choices[0].message.content)
```

## Check Model Support[​](#check-model-support "Direct link to Check Model Support")

### 1. Check if model supports `response_format`[​](#1-check-if-model-supports-response_format "Direct link to 1-check-if-model-supports-response_format")

Call `litellm.get_supported_openai_params` to check if a model/provider supports `response_format`.

```
from litellm import get_supported_openai_params

params = get_supported_openai_params(model="anthropic.claude-3", custom_llm_provider="bedrock")

assert"response_format"in params
```

### 2. Check if model supports `json_schema`[​](#2-check-if-model-supports-json_schema "Direct link to 2-check-if-model-supports-json_schema")

This is used to check if you can pass

- `response_format={ "type": "json_schema", "json_schema": … , "strict": true }`
- `response_format=<Pydantic Model>`

```
from litellm import supports_response_schema

assert supports_response_schema(model="gemini-1.5-pro-preview-0215", custom_llm_provider="bedrock")
```

Check out [model\_prices\_and\_context\_window.json](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json) for a full list of models and their support for `response_schema`.

## Pass in 'json\_schema'[​](#pass-in-json_schema "Direct link to Pass in 'json_schema'")

To use Structured Outputs, simply specify

```
response_format: { "type": "json_schema", "json_schema": … , "strict": true }
```

Works for:

- OpenAI models
- Azure OpenAI models
- xAI models (Grok-2 or later)
- Google AI Studio - Gemini models
- Vertex AI models (Gemini + Anthropic)
- Bedrock Models
- Anthropic API Models
- Groq Models
- Ollama Models
- Databricks Models

<!--THE END-->

- SDK
- PROXY

```
import os
from litellm import completion 
from pydantic import BaseModel

# add to env var 
os.environ["OPENAI_API_KEY"]=""

messages =[{"role":"user","content":"List 5 important events in the XIX century"}]

classCalendarEvent(BaseModel):
  name:str
  date:str
  participants:list[str]

classEventsList(BaseModel):
    events:list[CalendarEvent]

resp = completion(
    model="gpt-4o-2024-08-06",
    messages=messages,
    response_format=EventsList
)

print("Received={}".format(resp))

events_list = EventsList.model_validate_json(resp.choices[0].message.content)
```

## Validate JSON Schema[​](#validate-json-schema "Direct link to Validate JSON Schema")

Not all vertex models support passing the json\_schema to them (e.g. `gemini-1.5-flash`). To solve this, LiteLLM supports client-side validation of the json schema.

```
litellm.enable_json_schema_validation=True
```

If `litellm.enable_json_schema_validation=True` is set, LiteLLM will validate the json response using `jsonvalidator`.

[**See Code**](https://github.com/BerriAI/litellm/blob/671d8ac496b6229970c7f2a3bdedd6cb84f0746b/litellm/litellm_core_utils/json_validation_rule.py#L4)

- SDK
- PROXY

```
# !gcloud auth application-default login - run this to add vertex credentials to your env
import litellm, os
from litellm import completion 
from pydantic import BaseModel 


messages=[
{"role":"system","content":"Extract the event information."},
{"role":"user","content":"Alice and Bob are going to a science fair on Friday."},
]

litellm.enable_json_schema_validation =True
litellm.set_verbose =True# see the raw request made by litellm

classCalendarEvent(BaseModel):
  name:str
  date:str
  participants:list[str]

resp = completion(
    model="gemini/gemini-1.5-pro",
    messages=messages,
    response_format=CalendarEvent,
)

print("Received={}".format(resp))
```

## Gemini - Native JSON Schema Format (Gemini 2.0+)[​](#gemini---native-json-schema-format-gemini-20 "Direct link to Gemini - Native JSON Schema Format (Gemini 2.0+)")

Gemini 2.0+ models automatically use the native `responseJsonSchema` parameter, which provides better compatibility with standard JSON Schema format.

### Benefits (Gemini 2.0+):[​](#benefits-gemini-20 "Direct link to Benefits (Gemini 2.0+):")

- Standard JSON Schema format (lowercase types like `string`, `object`)
- Supports `additionalProperties: false` for stricter validation
- Better compatibility with Pydantic's `model_json_schema()`
- No `propertyOrdering` required

### Usage[​](#usage "Direct link to Usage")

- SDK
- PROXY

```
from litellm import completion
from pydantic import BaseModel

classUserInfo(BaseModel):
    name:str
    age:int

response = completion(
    model="gemini/gemini-2.0-flash",
    messages=[{"role":"user","content":"Extract: John is 25 years old"}],
    response_format={
"type":"json_schema",
"json_schema":{
"name":"user_info",
"schema":{
"type":"object",
"properties":{
"name":{"type":"string"},
"age":{"type":"integer"}
},
"required":["name","age"],
"additionalProperties":False# Supported on Gemini 2.0+
}
}
}
)
```

### Model Behavior[​](#model-behavior "Direct link to Model Behavior")

ModelFormat Used`additionalProperties` SupportGemini 2.0+`responseJsonSchema` (JSON Schema)✅ YesGemini 1.5`responseSchema` (OpenAPI)❌ No

LiteLLM automatically selects the appropriate format based on the model version.