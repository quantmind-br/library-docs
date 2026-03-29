---
title: OpenAI - Response API | liteLLM
url: https://docs.litellm.ai/docs/providers/openai/responses_api
source: sitemap
fetched_at: 2026-01-21T19:50:00.921768183-03:00
rendered_js: false
word_count: 231
summary: This document provides instructions and code examples for using the LiteLLM Python SDK and Proxy server to manage AI model responses, covering streaming, image generation, and response lifecycle operations.
tags:
    - litellm-python-sdk
    - litellm-proxy
    - openai-sdk
    - streaming
    - image-generation
    - api-integration
    - computer-use
category: tutorial
---

## Usage[​](#usage "Direct link to Usage")

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

#### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

OpenAI Non-streaming Response

```
import litellm

# Non-streaming response
response = litellm.responses(
    model="openai/o1-pro",
input="Tell me a three sentence bedtime story about a unicorn.",
    max_output_tokens=100
)

print(response)
```

#### Streaming[​](#streaming "Direct link to Streaming")

OpenAI Streaming Response

```
import litellm

# Streaming response
response = litellm.responses(
    model="openai/o1-pro",
input="Tell me a three sentence bedtime story about a unicorn.",
    stream=True
)

for event in response:
print(event)
```

#### Image Generation with Streaming[​](#image-generation-with-streaming "Direct link to Image Generation with Streaming")

OpenAI Streaming Image Generation

```
import litellm
import base64

# Streaming image generation with partial images
stream = litellm.responses(
    model="gpt-4.1",# Use an actual image generation model
input="Generate a gorgeous image of a river made of white owl feathers",
    stream=True,
    tools=[{"type":"image_generation","partial_images":2}],

)

for event in stream:
if event.type=="response.image_generation_call.partial_image":
        idx = event.partial_image_index
        image_base64 = event.partial_image_b64
        image_bytes = base64.b64decode(image_base64)
withopen(f"river{idx}.png","wb")as f:
            f.write(image_bytes)
```

#### GET a Response[​](#get-a-response "Direct link to GET a Response")

Get Response by ID

```
import litellm

# First, create a response
response = litellm.responses(
    model="openai/o1-pro",
input="Tell me a three sentence bedtime story about a unicorn.",
    max_output_tokens=100
)

# Get the response ID
response_id = response.id

# Retrieve the response by ID
retrieved_response = litellm.get_responses(
    response_id=response_id
)

print(retrieved_response)

# For async usage
# retrieved_response = await litellm.aget_responses(response_id=response_id)
```

#### DELETE a Response[​](#delete-a-response "Direct link to DELETE a Response")

Delete Response by ID

```
import litellm

# First, create a response
response = litellm.responses(
    model="openai/o1-pro",
input="Tell me a three sentence bedtime story about a unicorn.",
    max_output_tokens=100
)

# Get the response ID
response_id = response.id

# Delete the response by ID
delete_response = litellm.delete_responses(
    response_id=response_id
)

print(delete_response)

# For async usage
# delete_response = await litellm.adelete_responses(response_id=response_id)
```

### LiteLLM Proxy with OpenAI SDK[​](#litellm-proxy-with-openai-sdk "Direct link to LiteLLM Proxy with OpenAI SDK")

1. Set up config.yaml

OpenAI Proxy Configuration

```
model_list:
-model_name: openai/o1-pro
litellm_params:
model: openai/o1-pro
api_key: os.environ/OPENAI_API_KEY
```

2. Start LiteLLM Proxy Server

Start LiteLLM Proxy Server

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

3. Use OpenAI SDK with LiteLLM Proxy

#### Non-streaming[​](#non-streaming-1 "Direct link to Non-streaming")

OpenAI Proxy Non-streaming Response

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-api-key"# Your proxy API key
)

# Non-streaming response
response = client.responses.create(
    model="openai/o1-pro",
input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
```

#### Streaming[​](#streaming-1 "Direct link to Streaming")

OpenAI Proxy Streaming Response

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-api-key"# Your proxy API key
)

# Streaming response
response = client.responses.create(
    model="openai/o1-pro",
input="Tell me a three sentence bedtime story about a unicorn.",
    stream=True
)

for event in response:
print(event)
```

#### Image Generation with Streaming[​](#image-generation-with-streaming-1 "Direct link to Image Generation with Streaming")

OpenAI Proxy Streaming Image Generation

```
from openai import OpenAI
import base64

# Initialize client with your proxy URL
client = OpenAI(api_key="sk-1234", base_url="http://localhost:4000")

stream = client.responses.create(
    model="gpt-4.1",
input="Draw a gorgeous image of a river made of white owl feathers, snaking its way through a serene winter landscape",
    stream=True,
    tools=[{"type":"image_generation","partial_images":2}],
)


for event in stream:
print(f"event: {event}")
if event.type=="response.image_generation_call.partial_image":
        idx = event.partial_image_index
        image_base64 = event.partial_image_b64
        image_bytes = base64.b64decode(image_base64)
withopen(f"river{idx}.png","wb")as f:
            f.write(image_bytes)

```

#### GET a Response[​](#get-a-response-1 "Direct link to GET a Response")

Get Response by ID with OpenAI SDK

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-api-key"# Your proxy API key
)

# First, create a response
response = client.responses.create(
    model="openai/o1-pro",
input="Tell me a three sentence bedtime story about a unicorn."
)

# Get the response ID
response_id = response.id

# Retrieve the response by ID
retrieved_response = client.responses.retrieve(response_id)

print(retrieved_response)
```

#### DELETE a Response[​](#delete-a-response-1 "Direct link to DELETE a Response")

Delete Response by ID with OpenAI SDK

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-api-key"# Your proxy API key
)

# First, create a response
response = client.responses.create(
    model="openai/o1-pro",
input="Tell me a three sentence bedtime story about a unicorn."
)

# Get the response ID
response_id = response.id

# Delete the response by ID
delete_response = client.responses.delete(response_id)

print(delete_response)
```

## Supported Responses API Parameters[​](#supported-responses-api-parameters "Direct link to Supported Responses API Parameters")

ProviderSupported Parameters`openai`[All Responses API parameters are supported](https://github.com/BerriAI/litellm/blob/7c3df984da8e4dff9201e4c5353fdc7a2b441831/litellm/llms/openai/responses/transformation.py#L23)

## Reusable Prompts[​](#reusable-prompts "Direct link to Reusable Prompts")

Use the `prompt` parameter to reference a stored prompt template and optionally supply variables.

Stored Prompt

```
import litellm

response = litellm.responses(
    model="openai/o1-pro",
    prompt={
"id":"pmpt_abc123",
"version":"2",
"variables":{
"customer_name":"Jane Doe",
"product":"40oz juice box",
},
},
)

print(response)
```

The same parameter is supported when calling the LiteLLM proxy with the OpenAI SDK:

Stored Prompt via Proxy

```
from openai import OpenAI

client = OpenAI(base_url="http://localhost:4000", api_key="your-api-key")

response = client.responses.create(
    model="openai/o1-pro",
    prompt={
"id":"pmpt_abc123",
"version":"2",
"variables":{
"customer_name":"Jane Doe",
"product":"40oz juice box",
},
},
)

print(response)
```

## Computer Use[​](#computer-use "Direct link to Computer Use")

- LiteLLM Python SDK
- LiteLLM Proxy

```
import litellm

# Non-streaming response
response = litellm.responses(
    model="computer-use-preview",
    tools=[{
"type":"computer_use_preview",
"display_width":1024,
"display_height":768,
"environment":"browser"# other possible values: "mac", "windows", "ubuntu"
}],
input=[
{
"role":"user",
"content":[
{
"type":"text",
"text":"Check the latest OpenAI news on bing.com."
}
# Optional: include a screenshot of the initial state of the environment
# {
#     type: "input_image",
#     image_url: f"data:image/png;base64,{screenshot_base64}"
# }
]
}
],
    reasoning={
"summary":"concise",
},
    truncation="auto"
)

print(response.output)
```

- LiteLLM Python SDK
- LiteLLM Proxy

MCP Tools with LiteLLM SDK

```
import litellm
from typing import Optional

# Configure MCP Tools
MCP_TOOLS =[
{
"type":"mcp",
"server_label":"deepwiki",
"server_url":"https://mcp.deepwiki.com/mcp",
"allowed_tools":["ask_question"]
}
]

# Step 1: Make initial request - OpenAI will use MCP LIST and return MCP calls for approval
response = litellm.responses(
    model="openai/gpt-4.1",
    tools=MCP_TOOLS,
input="What transport protocols does the 2025-03-26 version of the MCP spec support?"
)

# Get the MCP approval ID
mcp_approval_id =None
for output in response.output:
if output.type=="mcp_approval_request":
        mcp_approval_id = output.id
break

# Step 2: Send followup with approval for the MCP call
response_with_mcp_call = litellm.responses(
    model="openai/gpt-4.1",
    tools=MCP_TOOLS,
input=[
{
"type":"mcp_approval_response",
"approve":True,
"approval_request_id": mcp_approval_id
}
],
    previous_response_id=response.id,
)

print(response_with_mcp_call)
```

## Verbosity Parameter[​](#verbosity-parameter "Direct link to Verbosity Parameter")

The `verbosity` parameter is supported for the `responses` API.

- LiteLLM Python SDK
- LiteLLM Proxy

Verbosity Parameter

```
from litellm import responses

question ="Write a poem about a boy and his first pet dog."

for verbosity in["low","medium","high"]:
    response = responses(
        model="gpt-5-mini",
input=question,
        text={"verbosity": verbosity}
)

print(response)
```

## Function Calling[​](#function-calling "Direct link to Function Calling")

Function Calling with Parallel Tool Calls

```
import litellm
import json

tools =[
{
"type":"function",
"name":"get_weather",
"description":"Get current weather for a location",
"parameters":{
"type":"object",
"properties":{
"location":{"type":"string"}
},
"required":["location"]
}
}
]

# Step 1: Request with tools (parallel_tool_calls=True allows multiple calls)
response = litellm.responses(
    model="openai/gpt-4o",
input=[{"role":"user","content":"What's the weather in Paris and Tokyo?"}],
    tools=tools,
    parallel_tool_calls=True,# Defaults = True
)

# Step 2: Execute tool calls and collect results
tool_results =[]
for output in response.output:
if output.type=="function_call":
        result ={"temperature":15,"condition":"sunny"}# Your function logic here
        tool_results.append({
"type":"function_call_output",
"call_id": output.call_id,
"output": json.dumps(result)
})

# Step 3: Send results back
final_response = litellm.responses(
    model="openai/gpt-4o",
input=tool_results,
    tools=tools,
)

print(final_response.output)
```

Set `parallel_tool_calls=False` to ensure zero or one tool is called per turn. [More details](https://platform.openai.com/docs/guides/function-calling#parallel-function-calling).

## Free-form Function Calling[​](#free-form-function-calling "Direct link to Free-form Function Calling")

- LiteLLM Python SDK
- LiteLLM Proxy

Free-form Function Calling

```
import litellm

response = litellm.responses(
    model="gpt-5-mini",
input="Please use the code_exec tool to calculate the area of a circle with radius equal to the number of 'r's in strawberry",
    text={"format":{"type":"text"}},
    tools=[
{
"type":"custom",
"name":"code_exec",
"description":"Executes arbitrary python code",
}
]
)
print(response.output)
```

## Context-Free Grammar[​](#context-free-grammar "Direct link to Context-Free Grammar")

- LiteLLM Python SDK
- LiteLLM Proxy

Context-Free Grammar

```
import litellm

import textwrap

# ----------------- grammars for MS SQL dialect -----------------
mssql_grammar = textwrap.dedent(r"""
            // ---------- Punctuation & operators ----------
            SP: " "
            COMMA: ","
            GT: ">"
            EQ: "="
            SEMI: ";"

            // ---------- Start ----------
            start: "SELECT" SP "TOP" SP NUMBER SP select_list SP "FROM" SP table SP "WHERE" SP amount_filter SP "AND" SP date_filter SP "ORDER" SP "BY" SP sort_cols SEMI

            // ---------- Projections ----------
            select_list: column (COMMA SP column)*
            column: IDENTIFIER

            // ---------- Tables ----------
            table: IDENTIFIER

            // ---------- Filters ----------
            amount_filter: "total_amount" SP GT SP NUMBER
            date_filter: "order_date" SP GT SP DATE

            // ---------- Sorting ----------
            sort_cols: "order_date" SP "DESC"

            // ---------- Terminals ----------
            IDENTIFIER: /[A-Za-z_][A-Za-z0-9_]*/
            NUMBER: /[0-9]+/
            DATE: /'[0-9]{4}-[0-9]{2}-[0-9]{2}'/
    """)

sql_prompt_mssql =(
"Call the mssql_grammar to generate a query for Microsoft SQL Server that retrieve the "
"five most recent orders per customer, showing customer_id, order_id, order_date, and total_amount, "
"where total_amount > 500 and order_date is after '2025-01-01'. "
)


response = litellm.responses(
    model="gpt-5",
input=sql_prompt_mssql,
    text={"format":{"type":"text"}},
    tools=[
{
"type":"custom",
"name":"mssql_grammar",
"description":"Executes read-only Microsoft SQL Server queries limited to SELECT statements with TOP and basic WHERE/ORDER BY. YOU MUST REASON HEAVILY ABOUT THE QUERY AND MAKE SURE IT OBEYS THE GRAMMAR.",
"format":{
"type":"grammar",
"syntax":"lark",
"definition": mssql_grammar
}
},
],
    parallel_tool_calls=False
)

print("--- MS SQL Query ---")
print(response_mssql.output[1].input)
```

## Minimal Reasoning[​](#minimal-reasoning "Direct link to Minimal Reasoning")

- LiteLLM Python SDK
- LiteLLM Proxy

Minimal Reasoning

```
import litellm

response = litellm.responses(
    model="gpt-5",
input=[{'role':'developer','content': prompt },
{'role':'user','content':'The food that the restaurant was great! I recommend it to everyone.'}],
    reasoning ={
"effort":"minimal"
},
)

print(response)
```