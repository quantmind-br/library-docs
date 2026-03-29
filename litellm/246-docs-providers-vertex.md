---
title: VertexAI [Gemini] | liteLLM
url: https://docs.litellm.ai/docs/providers/vertex
source: sitemap
fetched_at: 2026-01-21T19:50:36.710773669-03:00
rendered_js: false
word_count: 2190
summary: This document provides technical instructions for integrating Google Vertex AI with LiteLLM, covering authentication methods, supported model operations, and advanced features like function calling and JSON schema validation.
tags:
    - vertex-ai
    - litellm
    - google-cloud
    - gemini-api
    - function-calling
    - json-schema
    - api-integration
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionVertex AI is a fully-managed AI development platform for building and using generative AI.Provider Route on LiteLLM`vertex_ai/`Link to Provider Doc[Vertex AI ↗](https://cloud.google.com/vertex-ai)Base URL1. Regional endpoints  
`https://{vertex_location}-aiplatform.googleapis.com/`  
2\. Global endpoints (limited availability)  
`https://aiplatform.googleapis.com/`Supported Operations[`/chat/completions`](#sample-usage), `/completions`, [`/embeddings`](#embedding-models), [`/audio/speech`](#text-to-speech-apis), [`/fine_tuning`](#fine-tuning-apis), [`/batches`](#batch-apis), [`/files`](#batch-apis), [`/images`](#image-generation-models), [`/rerank`](#rerank-api)

Vertex AI vs Gemini API

Model FormatProviderAuth Required`vertex_ai/gemini-2.0-flash`Vertex AIGCP credentials + project`gemini-2.0-flash` (no prefix)Vertex AIGCP credentials + project`gemini/gemini-2.0-flash`Gemini API`GEMINI_API_KEY` (simple API key)

**If you just want to use an API key** (like OpenAI), use the `gemini/` prefix instead. See [Gemini - Google AI Studio](https://docs.litellm.ai/docs/providers/gemini).

Models without a prefix default to Vertex AI which requires GCP authentication.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/liteLLM_VertextAI_Example.ipynb)

## `vertex_ai/` route[​](#vertex_ai-route "Direct link to vertex_ai-route")

The `vertex_ai/` route uses uses [VertexAI's REST API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#syntax).

```
from litellm import completion
import json 

## GET CREDENTIALS 
## RUN ## 
# !gcloud auth application-default login - run this to add vertex credentials to your env
## OR ## 
file_path ='path/to/vertex_ai_service_account.json'

# Load the JSON file
withopen(file_path,'r')asfile:
    vertex_credentials = json.load(file)

# Convert to JSON string
vertex_credentials_json = json.dumps(vertex_credentials)

## COMPLETION CALL 
response = completion(
  model="vertex_ai/gemini-2.5-pro",
  messages=[{"content":"Hello, how are you?","role":"user"}],
  vertex_credentials=vertex_credentials_json
)
```

### **System Message**[​](#system-message "Direct link to system-message")

```
from litellm import completion
import json 

## GET CREDENTIALS 
file_path ='path/to/vertex_ai_service_account.json'

# Load the JSON file
withopen(file_path,'r')asfile:
    vertex_credentials = json.load(file)

# Convert to JSON string
vertex_credentials_json = json.dumps(vertex_credentials)


response = completion(
  model="vertex_ai/gemini-2.5-pro",
  messages=[{"content":"You are a good bot.","role":"system"},{"content":"Hello, how are you?","role":"user"}],
  vertex_credentials=vertex_credentials_json
)
```

### **Function Calling**[​](#function-calling "Direct link to function-calling")

Force Gemini to make tool calls with `tool_choice="required"`.

```
from litellm import completion
import json 

## GET CREDENTIALS 
file_path ='path/to/vertex_ai_service_account.json'

# Load the JSON file
withopen(file_path,'r')asfile:
    vertex_credentials = json.load(file)

# Convert to JSON string
vertex_credentials_json = json.dumps(vertex_credentials)


messages =[
{
"role":"system",
"content":"Your name is Litellm Bot, you are a helpful assistant",
},
# User asks for their name and weather in San Francisco
{
"role":"user",
"content":"Hello, what is your name and can you tell me the weather?",
},
]

tools =[
{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get the current weather in a given location",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"The city and state, e.g. San Francisco, CA",
}
},
"required":["location"],
},
},
}
]

data ={
"model":"vertex_ai/gemini-1.5-pro-preview-0514"),
"messages": messages,
"tools": tools,
"tool_choice":"required",
"vertex_credentials": vertex_credentials_json
}

## COMPLETION CALL 
print(completion(**data))
```

### **JSON Schema**[​](#json-schema "Direct link to json-schema")

From v`1.40.1+` LiteLLM supports sending `response_schema` as a param for Gemini-1.5-Pro on Vertex AI. For other models (e.g. `gemini-1.5-flash` or `claude-3-5-sonnet`), LiteLLM adds the schema to the message list with a user-controlled prompt.

**Response Schema**

- SDK
- PROXY

```
from litellm import completion 
import json 

## SETUP ENVIRONMENT
# !gcloud auth application-default login - run this to add vertex credentials to your env

messages =[
{
"role":"user",
"content":"List 5 popular cookie recipes."
}
]

response_schema ={
"type":"array",
"items":{
"type":"object",
"properties":{
"recipe_name":{
"type":"string",
},
},
"required":["recipe_name"],
},
}


completion(
    model="vertex_ai/gemini-1.5-pro",
    messages=messages,
    response_format={"type":"json_object","response_schema": response_schema}# 👈 KEY CHANGE
)

print(json.loads(completion.choices[0].message.content))
```

**Validate Schema**

To validate the response\_schema, set `enforce_validation: true`.

- SDK
- PROXY

```
from litellm import completion, JSONSchemaValidationError
try:
	completion(
    model="vertex_ai/gemini-1.5-pro",
    messages=messages,
    response_format={
"type":"json_object",
"response_schema": response_schema,
"enforce_validation": true # 👈 KEY CHANGE
}
)
except JSONSchemaValidationError as e:
print("Raw Response: {}".format(e.raw_response))
raise e
```

LiteLLM will validate the response against the schema, and raise a `JSONSchemaValidationError` if the response does not match the schema.

JSONSchemaValidationError inherits from `openai.APIError`

Access the raw response with `e.raw_response`

**Add to prompt yourself**

```
from litellm import completion 

## GET CREDENTIALS 
file_path ='path/to/vertex_ai_service_account.json'

# Load the JSON file
withopen(file_path,'r')asfile:
    vertex_credentials = json.load(file)

# Convert to JSON string
vertex_credentials_json = json.dumps(vertex_credentials)

messages =[
{
"role":"user",
"content":"""
List 5 popular cookie recipes.

Using this JSON schema:

    Recipe = {"recipe_name": str}

Return a `list[Recipe]`
        """
}
]

completion(model="vertex_ai/gemini-1.5-flash-preview-0514", messages=messages, response_format={"type":"json_object"})
```

### **Google Hosted Tools (Web Search, Code Execution, etc.)**[​](#google-hosted-tools-web-search-code-execution-etc "Direct link to google-hosted-tools-web-search-code-execution-etc")

#### **Web Search**[​](#web-search "Direct link to web-search")

Add Google Search Result grounding to vertex ai calls.

[**Relevant VertexAI Docs**](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/grounding#examples)

See the grounding metadata with `response_obj._hidden_params["vertex_ai_grounding_metadata"]`

- SDK
- PROXY

```
from litellm import completion 

## SETUP ENVIRONMENT
# !gcloud auth application-default login - run this to add vertex credentials to your env

tools =[{"googleSearch":{}}]# 👈 ADD GOOGLE SEARCH

resp = litellm.completion(
                    model="vertex_ai/gemini-1.0-pro-001",
                    messages=[{"role":"user","content":"Who won the world cup?"}],
                    tools=tools,
)

print(resp)
```

#### **Url Context**[​](#url-context "Direct link to url-context")

Using the URL context tool, you can provide Gemini with URLs as additional context for your prompt. The model can then retrieve content from the URLs and use that content to inform and shape its response.

[**Relevant Docs**](https://ai.google.dev/gemini-api/docs/url-context)

See the grounding metadata with `response_obj._hidden_params["vertex_ai_url_context_metadata"]`

- SDK
- PROXY

```
from litellm import completion
import os

os.environ["GEMINI_API_KEY"]=".."

# 👇 ADD URL CONTEXT
tools =[{"urlContext":{}}]

response = completion(
    model="gemini/gemini-2.0-flash",
    messages=[{"role":"user","content":"Summarize this document: https://ai.google.dev/gemini-api/docs/models"}],
    tools=tools,
)

print(response)

# Access URL context metadata
url_context_metadata = response.model_extra['vertex_ai_url_context_metadata']
urlMetadata = url_context_metadata[0]['urlMetadata'][0]
print(f"Retrieved URL: {urlMetadata['retrievedUrl']}")
print(f"Retrieval Status: {urlMetadata['urlRetrievalStatus']}")
```

#### **Enterprise Web Search**[​](#enterprise-web-search "Direct link to enterprise-web-search")

You can also use the `enterpriseWebSearch` tool for an [enterprise compliant search](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/web-grounding-enterprise).

- SDK
- PROXY

```
from litellm import completion 

## SETUP ENVIRONMENT
# !gcloud auth application-default login - run this to add vertex credentials to your env

tools =[{"enterpriseWebSearch":{}}]# 👈 ADD GOOGLE ENTERPRISE SEARCH

resp = litellm.completion(
                    model="vertex_ai/gemini-1.0-pro-001",
                    messages=[{"role":"user","content":"Who won the world cup?"}],
                    tools=tools,
)

print(resp)
```

#### **Code Execution**[​](#code-execution "Direct link to code-execution")

- SDK
- PROXY

```
from litellm import completion
import os

## SETUP ENVIRONMENT
# !gcloud auth application-default login - run this to add vertex credentials to your env


tools =[{"codeExecution":{}}]# 👈 ADD CODE EXECUTION

response = completion(
    model="vertex_ai/gemini-2.0-flash",
    messages=[{"role":"user","content":"What is the weather in San Francisco?"}],
    tools=tools,
)

print(response)
```

#### **Google Maps**[​](#google-maps "Direct link to google-maps")

Use Google Maps to provide location-based context to your Gemini models.

[**Relevant Vertex AI Docs**](https://ai.google.dev/gemini-api/docs/grounding#google-maps)

- SDK
- PROXY

**Basic Usage - Enable Widget Only**

```
from litellm import completion

## SETUP ENVIRONMENT
# !gcloud auth application-default login - run this to add vertex credentials to your env

tools =[{"googleMaps":{"enableWidget":"ENABLE_WIDGET"}}]# 👈 ADD GOOGLE MAPS

resp = litellm.completion(
    model="vertex_ai/gemini-2.0-flash",
    messages=[{"role":"user","content":"What restaurants are nearby?"}],
    tools=tools,
)

print(resp)
```

**With Location Data**

You can specify a location to ground the model's responses with location-specific information:

```
from litellm import completion

## SETUP ENVIRONMENT
# !gcloud auth application-default login - run this to add vertex credentials to your env

tools =[{
"googleMaps":{
"enableWidget":"ENABLE_WIDGET",
"latitude":37.7749,# San Francisco latitude
"longitude":-122.4194,# San Francisco longitude
"languageCode":"en_US"# Optional: language for results
}
}]# 👈 ADD GOOGLE MAPS WITH LOCATION

resp = litellm.completion(
    model="vertex_ai/gemini-2.0-flash",
    messages=[{"role":"user","content":"What restaurants are nearby?"}],
    tools=tools,
)

print(resp)
```

#### **Moving from Vertex AI SDK to LiteLLM (GROUNDING)**[​](#moving-from-vertex-ai-sdk-to-litellm-grounding "Direct link to moving-from-vertex-ai-sdk-to-litellm-grounding")

If this was your initial VertexAI Grounding code,

```
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig, Tool, grounding


vertexai.init(project=project_id, location="us-central1")

model = GenerativeModel("gemini-1.5-flash-001")

# Use Google Search for grounding
tool = Tool.from_google_search_retrieval(grounding.GoogleSearchRetrieval())

prompt ="When is the next total solar eclipse in US?"
response = model.generate_content(
    prompt,
    tools=[tool],
    generation_config=GenerationConfig(
        temperature=0.0,
),
)

print(response)
```

then, this is what it looks like now

```
from litellm import completion


# !gcloud auth application-default login - run this to add vertex credentials to your env

tools =[{"googleSearch":{"disable_attributon":False}}]# 👈 ADD GOOGLE SEARCH

resp = litellm.completion(
                    model="vertex_ai/gemini-1.0-pro-001",
                    messages=[{"role":"user","content":"Who won the world cup?"}],
                    tools=tools,
                    vertex_project="project-id"
)

print(resp)
```

### **Thinking / `reasoning_content`**[​](#thinking--reasoning_content "Direct link to thinking--reasoning_content")

LiteLLM translates OpenAI's `reasoning_effort` to Gemini's `thinking` parameter. [Code](https://github.com/BerriAI/litellm/blob/620664921902d7a9bfb29897a7b27c1a7ef4ddfb/litellm/llms/vertex_ai/gemini/vertex_and_google_ai_studio_gemini.py#L362)

Added an additional non-OpenAI standard "disable" value for non-reasoning Gemini requests.

**Mapping**

reasoning\_effortthinking"disable""budget\_tokens": 0"low""budget\_tokens": 1024"medium""budget\_tokens": 2048"high""budget\_tokens": 4096

- SDK
- PROXY

```
from litellm import completion

# !gcloud auth application-default login - run this to add vertex credentials to your env

resp = completion(
    model="vertex_ai/gemini-2.5-flash-preview-04-17",
    messages=[{"role":"user","content":"What is the capital of France?"}],
    reasoning_effort="low",
    vertex_project="project-id",
    vertex_location="us-central1"
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
                reasoning_content='The capital of France is Paris. This is a very straightforward factual question.'
),
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

#### Pass `thinking` to Gemini models[​](#pass-thinking-to-gemini-models "Direct link to pass-thinking-to-gemini-models")

You can also pass the `thinking` parameter to Gemini models.

This is translated to Gemini's [`thinkingConfig` parameter](https://ai.google.dev/gemini-api/docs/thinking#set-budget).

- SDK
- PROXY

```
from litellm import completion

# !gcloud auth application-default login - run this to add vertex credentials to your env

response = litellm.completion(
  model="vertex_ai/gemini-2.5-flash-preview-04-17",
  messages=[{"role":"user","content":"What is the capital of France?"}],
  thinking={"type":"enabled","budget_tokens":1024},
  vertex_project="project-id",
  vertex_location="us-central1"
)
```

### **Context Caching**[​](#context-caching "Direct link to context-caching")

#### Unified Endpoint[​](#unified-endpoint "Direct link to Unified Endpoint")

Use Vertex AI context caching in the same way as [**Google AI Studio - Context Caching**](https://docs.litellm.ai/docs/providers/gemini#context-caching)

##### Example usage[​](#example-usage "Direct link to Example usage")

- SDK
- SDK with Custom TTL
- PROXY

```
from litellm import completion 

for _ inrange(2):
    resp = completion(
        model="vertex_ai/gemini-2.5-pro",
        messages=[
# System Message
{
"role":"system",
"content":[
{
"type":"text",
"text":"Here is the full text of a complex legal agreement"*4000,
"cache_control":{"type":"ephemeral"},# 👈 KEY CHANGE
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
}]
)

print(resp.usage)# 👈 2nd usage block will be less, since cached tokens used
```

#### Calling provider api directly[​](#calling-provider-api-directly "Direct link to Calling provider api directly")

[**Go straight to provider**](https://docs.litellm.ai/docs/pass_through/vertex_ai#context-caching)

##### 1. Create the Cache[​](#1-create-the-cache "Direct link to 1. Create the Cache")

First, create the cache by sending a `POST` request to the `cachedContents` endpoint via the LiteLLM proxy.

- PROXY

```
curl http://0.0.0.0:4000/vertex_ai/v1/projects/{project_id}/locations/{location}/cachedContents \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_KEY" \
  -d '{
    "model": "projects/{project_id}/locations/{location}/publishers/google/models/gemini-2.5-flash",
    "displayName": "example_cache",
    "contents": [{
      "role": "user",
      "parts": [{
        "text": ".... a long book to be cached"
      }]
    }]
  }'
```

##### 2. Get the Cache Name from the Response[​](#2-get-the-cache-name-from-the-response "Direct link to 2. Get the Cache Name from the Response")

Vertex AI will return a response containing the `name` of the cached content. This name is the identifier for your cached data.

```
{
"name":"projects/12341234/locations/{location}/cachedContents/123123123123123",
"model":"projects/{project_id}/locations/{location}/publishers/google/models/gemini-2.5-flash",
"createTime":"2025-09-23T19:13:50.674976Z",
"updateTime":"2025-09-23T19:13:50.674976Z",
"expireTime":"2025-09-23T20:13:50.655988Z",
"displayName":"example_cache",
"usageMetadata":{
"totalTokenCount":1246,
"textCount":5132
}
}
```

##### 3. Use the Cached Content[​](#3-use-the-cached-content "Direct link to 3. Use the Cached Content")

Use the `name` from the response as `cachedContent` or `cached_content` in subsequent API calls to reuse the cached information. This is passed in the body of your request to `/chat/completions`.

- PROXY

```

curl http://0.0.0.0:4000/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_KEY" \
  -d '{
    "cachedContent": "projects/545201925769/locations/us-central1/cachedContents/4511135542628319232",
    "model": "gemini-2.5-flash",
    "messages": [
        {
            "role": "user",
            "content": "what is the book about?"
        }
    ]
  }'
```

## Pre-requisites[​](#pre-requisites "Direct link to Pre-requisites")

- `pip install google-cloud-aiplatform` (pre-installed on proxy docker image)
- Authentication:
  
  - run `gcloud auth application-default login` See [Google Cloud Docs](https://cloud.google.com/docs/authentication/external/set-up-adc)
  - Alternatively you can set `GOOGLE_APPLICATION_CREDENTIALS`
  
  Here's how: [**Jump to Code**](#extra)
  
  - Create a service account on GCP
  - Export the credentials as a json
  - load the json and json.dump the json as a string
  - store the json string in your environment as `GOOGLE_APPLICATION_CREDENTIALS`

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
import litellm
litellm.vertex_project ="hardy-device-38811"# Your Project ID
litellm.vertex_location ="us-central1"# proj location

response = litellm.completion(model="gemini-2.5-pro", messages=[{"role":"user","content":"write code for saying hi from LiteLLM"}])
```

## Usage with LiteLLM Proxy Server[​](#usage-with-litellm-proxy-server "Direct link to Usage with LiteLLM Proxy Server")

Here's how to use Vertex AI with the LiteLLM Proxy Server

1. Modify the config.yaml

<!--THE END-->

- Different location per model
- One location all vertex models

Use this when you need to set a different location for each vertex model

```
model_list:
-model_name: gemini-vision
litellm_params:
model: vertex_ai/gemini-1.0-pro-vision-001
vertex_project:"project-id"
vertex_location:"us-central1"
-model_name: gemini-vision
litellm_params:
model: vertex_ai/gemini-1.0-pro-vision-001
vertex_project:"project-id2"
vertex_location:"us-east"
```

2. Start the proxy

```
$ litellm --config /path/to/config.yaml
```

3. Send Request to LiteLLM Proxy Server

<!--THE END-->

- OpenAI Python v1.0.0+
- curl

```
import openai
client = openai.OpenAI(
    api_key="sk-1234",# pass litellm proxy key, if you're using virtual keys
    base_url="http://0.0.0.0:4000"# litellm-proxy-base url
)

response = client.chat.completions.create(
    model="team1-gemini-2.5-pro",
    messages =[
{
"role":"user",
"content":"what llm are you"
}
],
)

print(response)
```

## Authentication - vertex\_project, vertex\_location, etc.[​](#authentication---vertex_project-vertex_location-etc "Direct link to Authentication - vertex_project, vertex_location, etc.")

Set your vertex credentials via:

- dynamic params OR
- env vars

### **Dynamic Params**[​](#dynamic-params "Direct link to dynamic-params")

You can set:

- `vertex_credentials` (str) - can be a json string or filepath to your vertex ai service account.json
- `vertex_location` (str) - place where vertex model is deployed (us-central1, asia-southeast1, etc.). Some models support the global location, please see [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#supported_models)
- `vertex_project` Optional\[str] - use if vertex project different from the one in vertex\_credentials

as dynamic params for a `litellm.completion` call.

- SDK
- PROXY

```
from litellm import completion
import json 

## GET CREDENTIALS 
file_path ='path/to/vertex_ai_service_account.json'

# Load the JSON file
withopen(file_path,'r')asfile:
    vertex_credentials = json.load(file)

# Convert to JSON string
vertex_credentials_json = json.dumps(vertex_credentials)


response = completion(
  model="vertex_ai/gemini-2.5-pro",
  messages=[{"content":"You are a good bot.","role":"system"},{"content":"Hello, how are you?","role":"user"}],
  vertex_credentials=vertex_credentials_json,
  vertex_project="my-special-project",
  vertex_location="my-special-location"
)
```

### **Workload Identity Federation**[​](#workload-identity-federation "Direct link to workload-identity-federation")

LiteLLM supports [Google Cloud Workload Identity Federation (WIF)](https://cloud.google.com/iam/docs/workload-identity-federation), which allows you to grant on-premises or multi-cloud workloads access to Google Cloud resources without using a service account key. This is the recommended approach for workloads running in other cloud environments (AWS, Azure, etc.) or on-premises.

To use Workload Identity Federation, pass the path to your WIF credentials configuration file via `vertex_credentials`:

- SDK
- PROXY

```
from litellm import completion

response = completion(
    model="vertex_ai/gemini-1.5-pro",
    messages=[{"role":"user","content":"Hello!"}],
    vertex_credentials="/path/to/wif-credentials.json",# 👈 WIF credentials file
    vertex_project="your-gcp-project-id",
    vertex_location="us-central1"
)
```

**WIF Credentials File Format**

Your WIF credentials JSON file typically looks like this (for AWS federation):

```
{
"type":"external_account",
"audience":"//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID",
"subject_token_type":"urn:ietf:params:aws:token-type:aws4_request",
"service_account_impersonation_url":"https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT_EMAIL:generateAccessToken",
"token_url":"https://sts.googleapis.com/v1/token",
"credential_source":{
"environment_id":"aws1",
"region_url":"http://169.254.169.254/latest/meta-data/placement/availability-zone",
"url":"http://169.254.169.254/latest/meta-data/iam/security-credentials",
"regional_cred_verification_url":"https://sts.{region}.amazonaws.com?Action=GetCallerIdentity&Version=2011-06-15"
}
}
```

For more details on setting up Workload Identity Federation, see [Google Cloud WIF documentation](https://cloud.google.com/iam/docs/workload-identity-federation).

### **Environment Variables**[​](#environment-variables "Direct link to environment-variables")

You can set:

- `GOOGLE_APPLICATION_CREDENTIALS` - store the filepath for your service\_account.json in here (used by vertex sdk directly).
- VERTEXAI\_LOCATION - place where vertex model is deployed (us-central1, asia-southeast1, etc.)
- VERTEXAI\_PROJECT - Optional\[str] - use if vertex project different from the one in vertex\_credentials

<!--THE END-->

1. GOOGLE\_APPLICATION\_CREDENTIALS

```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service_account.json"
```

2. VERTEXAI\_LOCATION

```
export VERTEXAI_LOCATION="us-central1" # can be any vertex location
```

3. VERTEXAI\_PROJECT

```
export VERTEXAI_PROJECT="my-test-project" # ONLY use if model project is different from service account project
```

## Specifying Safety Settings[​](#specifying-safety-settings "Direct link to Specifying Safety Settings")

In certain use-cases you may need to make calls to the models and pass [safety settings](https://ai.google.dev/docs/safety_setting_gemini) different from the defaults. To do so, simple pass the `safety_settings` argument to `completion` or `acompletion`. For example:

### Set per model/request[​](#set-per-modelrequest "Direct link to Set per model/request")

- SDK
- Proxy

```
response = completion(
    model="vertex_ai/gemini-2.5-pro",
    messages=[{"role":"user","content":"write code for saying hi from LiteLLM"}]
    safety_settings=[
{
"category":"HARM_CATEGORY_HARASSMENT",
"threshold":"BLOCK_NONE",
},
{
"category":"HARM_CATEGORY_HATE_SPEECH",
"threshold":"BLOCK_NONE",
},
{
"category":"HARM_CATEGORY_SEXUALLY_EXPLICIT",
"threshold":"BLOCK_NONE",
},
{
"category":"HARM_CATEGORY_DANGEROUS_CONTENT",
"threshold":"BLOCK_NONE",
},
]
)
```

### Set Globally[​](#set-globally "Direct link to Set Globally")

- SDK
- Proxy

```
import litellm 

litellm.set_verbose =True 👈 See RAW REQUEST/RESPONSE 

litellm.vertex_ai_safety_settings =[
{
"category":"HARM_CATEGORY_HARASSMENT",
"threshold":"BLOCK_NONE",
},
{
"category":"HARM_CATEGORY_HATE_SPEECH",
"threshold":"BLOCK_NONE",
},
{
"category":"HARM_CATEGORY_SEXUALLY_EXPLICIT",
"threshold":"BLOCK_NONE",
},
{
"category":"HARM_CATEGORY_DANGEROUS_CONTENT",
"threshold":"BLOCK_NONE",
},
]
response = completion(
    model="vertex_ai/gemini-2.5-pro",
    messages=[{"role":"user","content":"write code for saying hi from LiteLLM"}]
)
```

## Set Vertex Project & Vertex Location[​](#set-vertex-project--vertex-location "Direct link to Set Vertex Project & Vertex Location")

All calls using Vertex AI require the following parameters:

- Your Project ID

```
import os, litellm 

# set via env var
os.environ["VERTEXAI_PROJECT"]="hardy-device-38811"# Your Project ID`

### OR ###

# set directly on module 
litellm.vertex_project ="hardy-device-38811"# Your Project ID`
```

- Your Project Location

```
import os, litellm 

# set via env var
os.environ["VERTEXAI_LOCATION"]= "us-central1 # Your Location

### OR ###

# set directly on module 
litellm.vertex_location = "us-central1 # Your Location
```

## Gemini Pro[​](#gemini-pro "Direct link to Gemini Pro")

Model NameFunction Callgemini-2.5-pro`completion('gemini-2.5-pro', messages)`, `completion('vertex_ai/gemini-2.5-pro', messages)`gemini-2.5-flash-preview-09-2025`completion('gemini-2.5-flash-preview-09-2025', messages)`, `completion('vertex_ai/gemini-2.5-flash-preview-09-2025', messages)`gemini-2.5-flash-lite-preview-09-2025`completion('gemini-2.5-flash-lite-preview-09-2025', messages)`, `completion('vertex_ai/gemini-2.5-flash-lite-preview-09-2025', messages)`

## Private Service Connect (PSC) Endpoints[​](#private-service-connect-psc-endpoints "Direct link to Private Service Connect (PSC) Endpoints")

LiteLLM supports Vertex AI models deployed to Private Service Connect (PSC) endpoints, allowing you to use custom `api_base` URLs for private deployments.

### Usage[​](#usage "Direct link to Usage")

```
from litellm import completion

# Use PSC endpoint with custom api_base
response = completion(
    model="vertex_ai/1234567890",# Numeric endpoint ID
    messages=[{"role":"user","content":"Hello!"}],
    api_base="http://10.96.32.8",# Your PSC endpoint
    vertex_project="my-project-id",
    vertex_location="us-central1",
    use_psc_endpoint_format=True
)
```

**Key Features:**

- Supports both numeric endpoint IDs and custom model names
- Works with both completion and embedding endpoints
- Automatically constructs full PSC URL: `{api_base}/v1/projects/{project}/locations/{location}/endpoints/{model}:{endpoint}`
- Compatible with streaming requests

### Configuration[​](#configuration "Direct link to Configuration")

Add PSC endpoints to your `config.yaml`:

```
model_list:
-model_name: psc-gemini
litellm_params:
model: vertex_ai/1234567890  # Numeric endpoint ID
api_base:"http://10.96.32.8"# Your PSC endpoint
vertex_project:"my-project-id"
vertex_location:"us-central1"
vertex_credentials:"/path/to/service_account.json"
use_psc_endpoint_format:True
-model_name: psc-embedding
litellm_params:
model: vertex_ai/text-embedding-004
api_base:"http://10.96.32.8"# Your PSC endpoint
vertex_project:"my-project-id"
vertex_location:"us-central1"
vertex_credentials:"/path/to/service_account.json"
use_psc_endpoint_format:True
```

## Fine-tuned Models[​](#fine-tuned-models "Direct link to Fine-tuned Models")

You can call fine-tuned Vertex AI Gemini models through LiteLLM

PropertyDetailsProvider Route`vertex_ai/gemini/{MODEL_ID}`Vertex Documentation[Vertex AI - Fine-tuned Gemini Models](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-use-supervised-tuning#test_the_tuned_model_with_a_prompt)Supported Operations`/chat/completions`, `/completions`, `/embeddings`, `/images`

To use a model that follows the `/gemini` request/response format, simply set the model parameter as

Model parameter for calling fine-tuned gemini models

```
model="vertex_ai/gemini/<your-finetuned-model>"
```

- LiteLLM Python SDK
- LiteLLM Proxy

Example

```
import litellm
import os

## set ENV variables
os.environ["VERTEXAI_PROJECT"]="hardy-device-38811"
os.environ["VERTEXAI_LOCATION"]="us-central1"

response = litellm.completion(
  model="vertex_ai/gemini/<your-finetuned-model>",# e.g. vertex_ai/gemini/4965075652664360960
  messages=[{"content":"Hello, how are you?","role":"user"}],
)
```

## Gemini Pro Vision[​](#gemini-pro-vision "Direct link to Gemini Pro Vision")

Model NameFunction Callgemini-2.5-pro-vision`completion('gemini-2.5-pro-vision', messages)`, `completion('vertex_ai/gemini-2.5-pro-vision', messages)`

## Gemini 1.5 Pro (and Vision)[​](#gemini-15-pro-and-vision "Direct link to Gemini 1.5 Pro (and Vision)")

Model NameFunction Callgemini-1.5-pro`completion('gemini-1.5-pro', messages)`, `completion('vertex_ai/gemini-1.5-pro', messages)`gemini-1.5-flash-preview-0514`completion('gemini-1.5-flash-preview-0514', messages)`, `completion('vertex_ai/gemini-1.5-flash-preview-0514', messages)`gemini-1.5-pro-preview-0514`completion('gemini-1.5-pro-preview-0514', messages)`, `completion('vertex_ai/gemini-1.5-pro-preview-0514', messages)`

#### Using Gemini Pro Vision[​](#using-gemini-pro-vision "Direct link to Using Gemini Pro Vision")

Call `gemini-2.5-pro-vision` in the same input/output format as OpenAI [`gpt-4-vision`](https://docs.litellm.ai/docs/providers/openai#openai-vision-models)

LiteLLM Supports the following image types passed in `url`

- Images with Cloud Storage URIs - gs://cloud-samples-data/generative-ai/image/boats.jpeg
- Images with direct links - [https://storage.googleapis.com/github-repo/img/gemini/intro/landmark3.jpg](https://storage.googleapis.com/github-repo/img/gemini/intro/landmark3.jpg)
- Videos with Cloud Storage URIs - [https://storage.googleapis.com/github-repo/img/gemini/multimodality\_usecases\_overview/pixel8.mp4](https://storage.googleapis.com/github-repo/img/gemini/multimodality_usecases_overview/pixel8.mp4)
- Base64 Encoded Local Images

**Example Request - image url**

- Images with direct links
- Local Base64 Images

```
import litellm

response = litellm.completion(
  model ="vertex_ai/gemini-2.5-pro-vision",
  messages=[
{
"role":"user",
"content":[
{
"type":"text",
"text":"Whats in this image?"
},
{
"type":"image_url",
"image_url":{
"url":"https://awsmp-logos.s3.amazonaws.com/seller-xw5kijmvmzasy/c233c9ade2ccb5491072ae232c814942.png"
}
}
]
}
],
)
print(response)
```

## Usage - Function Calling[​](#usage---function-calling "Direct link to Usage - Function Calling")

LiteLLM supports Function Calling for Vertex AI gemini models.

```
from litellm import completion
import os
# set env
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=".."
os.environ["VERTEX_AI_PROJECT"]=".."
os.environ["VERTEX_AI_LOCATION"]=".."

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
    model="vertex_ai/gemini-2.5-pro-vision",
    messages=messages,
    tools=tools,
)
# Add any assertions, here to check response args
print(response)
assertisinstance(response.choices[0].message.tool_calls[0].function.name,str)
assertisinstance(
    response.choices[0].message.tool_calls[0].function.arguments,str
)

```

For Gemini 3+ models, LiteLLM supports per-part media resolution control using OpenAI's `detail` parameter. This allows you to specify different resolution levels for individual images and videos in your request, whether using `image_url` or `file` content types.

**Supported `detail` values:**

- `"low"` - Maps to `media_resolution: "low"` (280 tokens for images, 70 tokens per frame for videos)
- `"medium"` - Maps to `media_resolution: "medium"`
- `"high"` - Maps to `media_resolution: "high"` (1120 tokens for images)
- `"ultra_high"` - Maps to `media_resolution: "ultra_high"`
- `"auto"` or `None` - Model decides optimal resolution (no `media_resolution` set)

**Usage Examples:**

- Images
- Videos with Files

```
from litellm import completion

messages =[
{
"role":"user",
"content":[
{
"type":"image_url",
"image_url":{
"url":"https://example.com/chart.png",
"detail":"high"# High resolution for detailed chart analysis
}
},
{
"type":"text",
"text":"Analyze this chart"
},
{
"type":"image_url",
"image_url":{
"url":"https://example.com/icon.png",
"detail":"low"# Low resolution for simple icon
}
}
]
}
]

response = completion(
    model="vertex_ai/gemini-3-pro-preview",
    messages=messages,
)
```

info

**Per-Part Resolution:** Each image or video in your request can have its own `detail` setting, allowing mixed-resolution requests (e.g., a high-res chart alongside a low-res icon). This feature works with both `image_url` and `file` content types, and is only available for Gemini 3+ models.

For Gemini 3+ models, LiteLLM supports fine-grained video processing control through the `video_metadata` field. This allows you to specify frame extraction rates and time ranges for video analysis.

**Supported `video_metadata` parameters:**

ParameterTypeDescriptionExample`fps`NumberFrame extraction rate (frames per second)`5``start_offset`StringStart time for video clip processing`"10s"``end_offset`StringEnd time for video clip processing`"60s"`

note

**Field Name Conversion:** LiteLLM automatically converts snake\_case field names to camelCase for the Gemini API:

- `start_offset` → `startOffset`
- `end_offset` → `endOffset`
- `fps` remains unchanged

warning

- **Gemini 3+ Only:** This feature is only available for Gemini 3.0 and newer models
- **Video Files Recommended:** While `video_metadata` is designed for video files, error handling for other media types is delegated to the Vertex AI API
- **File Formats Supported:** Works with `gs://`, `https://`, and base64-encoded video files

**Usage Examples:**

- Basic Video Metadata
- Combined with Detail
- PROXY

```
from litellm import completion

response = completion(
    model="vertex_ai/gemini-3-pro-preview",
    messages=[
{
"role":"user",
"content":[
{"type":"text","text":"Analyze this video clip"},
{
"type":"file",
"file":{
"file_id":"gs://my-bucket/video.mp4",
"format":"video/mp4",
"video_metadata":{
"fps":5,# Extract 5 frames per second
"start_offset":"10s",# Start from 10 seconds
"end_offset":"60s"# End at 60 seconds
}
}
}
]
}
]
)

print(response.choices[0].message.content)
```

## Usage - PDF / Videos / Audio etc. Files[​](#usage---pdf--videos--audio-etc-files "Direct link to Usage - PDF / Videos / Audio etc. Files")

Pass any file supported by Vertex AI, through LiteLLM.

LiteLLM Supports the following file types passed in url.

Using `file` message type for VertexAI is live from v1.65.1+

```
Files with Cloud Storage URIs - gs://cloud-samples-data/generative-ai/image/boats.jpeg
Files with direct links - https://storage.googleapis.com/github-repo/img/gemini/intro/landmark3.jpg
Videos with Cloud Storage URIs - https://storage.googleapis.com/github-repo/img/gemini/multimodality_usecases_overview/pixel8.mp4
Base64 Encoded Local Files
```

- SDK
- PROXY

### **Using `gs://` or any URL**[​](#using-gs-or-any-url "Direct link to using-gs-or-any-url")

```
from litellm import completion

response = completion(
    model="vertex_ai/gemini-1.5-flash",
    messages=[
{
"role":"user",
"content":[
{"type":"text","text":"You are a very professional document summarization specialist. Please summarize the given document."},
{
"type":"file",
"file":{
"file_id":"gs://cloud-samples-data/generative-ai/pdf/2403.05530.pdf",
"format":"application/pdf"# OPTIONAL - specify mime-type
}
},
],
}
],
    max_tokens=300,
)

print(response.choices[0])
```

### **using base64**[​](#using-base64 "Direct link to using-base64")

```
from litellm import completion
import base64
import requests

# URL of the file
url ="https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf"

# Download the file
response = requests.get(url)
file_data = response.content

encoded_file = base64.b64encode(file_data).decode("utf-8")

response = completion(
    model="vertex_ai/gemini-1.5-flash",
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
{
"type":"audio_input",
                    "audio_input {
"audio_input":f"data:audio/mp3;base64,{encoded_file}",# 👈 AUDIO File ('file' message works as too)
}
},
],
}
],
    max_tokens=300,
)

print(response.choices[0])
```

## Chat Models[​](#chat-models "Direct link to Chat Models")

Model NameFunction Callchat-bison-32k`completion('chat-bison-32k', messages)`chat-bison`completion('chat-bison', messages)`chat-bison@001`completion('chat-bison@001', messages)`

## Code Chat Models[​](#code-chat-models "Direct link to Code Chat Models")

Model NameFunction Callcodechat-bison`completion('codechat-bison', messages)`codechat-bison-32k`completion('codechat-bison-32k', messages)`codechat-bison@001`completion('codechat-bison@001', messages)`

## Text Models[​](#text-models "Direct link to Text Models")

Model NameFunction Calltext-bison`completion('text-bison', messages)`text-bison@001`completion('text-bison@001', messages)`

## Code Text Models[​](#code-text-models "Direct link to Code Text Models")

Model NameFunction Callcode-bison`completion('code-bison', messages)`code-bison@001`completion('code-bison@001', messages)`code-gecko@001`completion('code-gecko@001', messages)`code-gecko@latest`completion('code-gecko@latest', messages)`

## **Embedding Models**[​](#embedding-models "Direct link to embedding-models")

#### Usage - Embedding[​](#usage---embedding "Direct link to Usage - Embedding")

- SDK
- LiteLLM PROXY

```
import litellm
from litellm import embedding
litellm.vertex_project ="hardy-device-38811"# Your Project ID
litellm.vertex_location ="us-central1"# proj location

response = embedding(
    model="vertex_ai/textembedding-gecko",
input=["good morning from litellm"],
)
print(response)
```

#### Supported Embedding Models[​](#supported-embedding-models "Direct link to Supported Embedding Models")

All models listed [here](https://github.com/BerriAI/litellm/blob/57f37f743886a0249f630a6792d49dffc2c5d9b7/model_prices_and_context_window.json#L835) are supported

Model NameFunction Calltext-embedding-004`embedding(model="vertex_ai/text-embedding-004", input)`text-multilingual-embedding-002`embedding(model="vertex_ai/text-multilingual-embedding-002", input)`textembedding-gecko`embedding(model="vertex_ai/textembedding-gecko", input)`textembedding-gecko-multilingual`embedding(model="vertex_ai/textembedding-gecko-multilingual", input)`textembedding-gecko-multilingual@001`embedding(model="vertex_ai/textembedding-gecko-multilingual@001", input)`textembedding-gecko@001`embedding(model="vertex_ai/textembedding-gecko@001", input)`textembedding-gecko@003`embedding(model="vertex_ai/textembedding-gecko@003", input)`text-embedding-preview-0409`embedding(model="vertex_ai/text-embedding-preview-0409", input)`text-multilingual-embedding-preview-0409`embedding(model="vertex_ai/text-multilingual-embedding-preview-0409", input)`Fine-tuned OR Custom Embedding models`embedding(model="vertex_ai/<your-model-id>", input)`

### Supported OpenAI (Unified) Params[​](#supported-openai-unified-params "Direct link to Supported OpenAI (Unified) Params")

[param](https://docs.litellm.ai/docs/embedding/supported_embedding#input-params-for-litellmembedding)type[vertex equivalent](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api)`input`**string or List\[string]**`instances``dimensions`**int**`output_dimensionality``input_type`**Literal\["RETRIEVAL\_QUERY","RETRIEVAL\_DOCUMENT", "SEMANTIC\_SIMILARITY", "CLASSIFICATION", "CLUSTERING", "QUESTION\_ANSWERING", "FACT\_VERIFICATION"]**`task_type`

#### Usage with OpenAI (Unified) Params[​](#usage-with-openai-unified-params "Direct link to Usage with OpenAI (Unified) Params")

- SDK
- LiteLLM PROXY

```
response = litellm.embedding(
    model="vertex_ai/text-embedding-004",
input=["good morning from litellm","gm"]
    input_type ="RETRIEVAL_DOCUMENT",
    dimensions=1,
)
```

### Supported Vertex Specific Params[​](#supported-vertex-specific-params "Direct link to Supported Vertex Specific Params")

paramtype`auto_truncate`**bool**`task_type`**Literal\["RETRIEVAL\_QUERY","RETRIEVAL\_DOCUMENT", "SEMANTIC\_SIMILARITY", "CLASSIFICATION", "CLUSTERING", "QUESTION\_ANSWERING", "FACT\_VERIFICATION"]**`title`**str**

#### Usage with Vertex Specific Params (Use `task_type` and `title`)[​](#usage-with-vertex-specific-params--use-task_type-and-title "Direct link to usage-with-vertex-specific-params--use-task_type-and-title")

You can pass any vertex specific params to the embedding model. Just pass them to the embedding function like this:

[Relevant Vertex AI doc with all embedding params](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api#request_body)

- SDK
- LiteLLM PROXY

```
response = litellm.embedding(
    model="vertex_ai/text-embedding-004",
input=["good morning from litellm","gm"]
    task_type ="RETRIEVAL_DOCUMENT",
    title ="test",
    dimensions=1,
    auto_truncate=True,
)
```

## **Multi-Modal Embeddings**[​](#multi-modal-embeddings "Direct link to multi-modal-embeddings")

Known Limitations:

- Only supports 1 image / video / image per request
- Only supports GCS or base64 encoded images / videos

### Usage[​](#usage-1 "Direct link to Usage")

- SDK
- LiteLLM PROXY (Unified Endpoint)
- LiteLLM PROXY (Vertex SDK)

Using GCS Images

```
response =await litellm.aembedding(
    model="vertex_ai/multimodalembedding@001",
input="gs://cloud-samples-data/vertex-ai/llm/prompts/landmark1.png"# will be sent as a gcs image
)
```

Using base 64 encoded images

```
response =await litellm.aembedding(
    model="vertex_ai/multimodalembedding@001",
input="data:image/jpeg;base64,..."# will be sent as a base64 encoded image
)
```

### Text + Image + Video Embeddings[​](#text--image--video-embeddings "Direct link to Text + Image + Video Embeddings")

- SDK
- LiteLLM PROXY (Unified Endpoint)

Text + Image

```
response =await litellm.aembedding(
    model="vertex_ai/multimodalembedding@001",
input=["hey","gs://cloud-samples-data/vertex-ai/llm/prompts/landmark1.png"]# will be sent as a gcs image
)
```

Text + Video

```
response =await litellm.aembedding(
    model="vertex_ai/multimodalembedding@001",
input=["hey","gs://my-bucket/embeddings/supermarket-video.mp4"]# will be sent as a gcs image
)
```

Image + Video

```
response =await litellm.aembedding(
    model="vertex_ai/multimodalembedding@001",
input=["gs://cloud-samples-data/vertex-ai/llm/prompts/landmark1.png","gs://my-bucket/embeddings/supermarket-video.mp4"]# will be sent as a gcs image
)
```

## **Fine Tuning APIs**[​](#fine-tuning-apis "Direct link to fine-tuning-apis")

PropertyDetailsDescriptionCreate Fine Tuning Jobs in Vertex AI (`/tuningJobs`) using OpenAI Python SDKVertex Fine Tuning Documentation[Vertex Fine Tuning](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/tuning#create-tuning)

### Usage[​](#usage-2 "Direct link to Usage")

#### 1. Add `finetune_settings` to your config.yaml[​](#1-add-finetune_settings-to-your-configyaml "Direct link to 1-add-finetune_settings-to-your-configyaml")

```
model_list:
-model_name: gpt-4
litellm_params:
model: openai/fake
api_key: fake-key
api_base: https://exampleopenaiendpoint-production.up.railway.app/

# 👇 Key change: For /fine_tuning/jobs endpoints
finetune_settings:
-custom_llm_provider:"vertex_ai"
vertex_project:"adroit-crow-413218"
vertex_location:"us-central1"
vertex_credentials:"/Users/ishaanjaffer/Downloads/adroit-crow-413218-a956eef1a2a8.json"
```

#### 2. Create a Fine Tuning Job[​](#2-create-a-fine-tuning-job "Direct link to 2. Create a Fine Tuning Job")

- OpenAI Python SDK
- curl

```
ft_job =await client.fine_tuning.jobs.create(
    model="gemini-1.0-pro-002",# Vertex model you want to fine-tune
    training_file="gs://cloud-samples-data/ai-platform/generative_ai/sft_train_data.jsonl",# file_id from create file response
    extra_headers={"custom-llm-provider":"vertex_ai"},# tell litellm proxy which provider to use
)
```

**Advanced use case - Passing `adapter_size` to the Vertex AI API**

Set hyper\_parameters, such as `n_epochs`, `learning_rate_multiplier` and `adapter_size`. [See Vertex Advanced Hyperparameters](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/tuning#advanced_use_case)

- OpenAI Python SDK
- curl

```

ft_job = client.fine_tuning.jobs.create(
    model="gemini-1.0-pro-002",# Vertex model you want to fine-tune
    training_file="gs://cloud-samples-data/ai-platform/generative_ai/sft_train_data.jsonl",# file_id from create file response
    hyperparameters={
"n_epochs":3,# epoch_count on Vertex
"learning_rate_multiplier":0.1,# learning_rate_multiplier on Vertex
"adapter_size":"ADAPTER_SIZE_ONE"# type: ignore, vertex specific hyperparameter
},
    extra_headers={"custom-llm-provider":"vertex_ai"},
)
```

## Labels[​](#labels "Direct link to Labels")

Google enables you to add custom metadata to its `generateContent` and `streamGenerateContent` calls. This mechanism is useful in Vertex AI because it allows costs and usage tracking over multiple different applications or users.

### Usage[​](#usage-3 "Direct link to Usage")

You can use that feature through LiteLLM by sending `labels` or `metadata` field in your requests.

If the client sets the `labels` field in the request to the LiteLLM, the LiteLLM will pass the `labels` field to the Vertex AI backend.

If the client sets the `metadata` field in the request to the LiteLLM and the `labels` field is not set, the LiteLLM will create the `labels` field filled with `metadata` key/value pairs for all string values and pass it to the Vertex AI backend.

Here is an example JSON request demonstrating the labels usage:

```
{
"model":"gemini-2.0-flash-lite",
"messages":[
{"role":"user","content":"respond in 20 words. who are you?"}
],
"labels":{
"client_app":"acme_comp_financial_app",
"department":"finance",
"project":"acme_ai"
}
}
```

### Using `GOOGLE_APPLICATION_CREDENTIALS`[​](#using-google_application_credentials "Direct link to using-google_application_credentials")

Here's the code for storing your service account credentials as `GOOGLE_APPLICATION_CREDENTIALS` environment variable:

```
import os 
import tempfile

defload_vertex_ai_credentials():
# Define the path to the vertex_key.json file
print("loading vertex ai credentials")
  filepath = os.path.dirname(os.path.abspath(__file__))
  vertex_key_path = filepath +"/vertex_key.json"

# Read the existing content of the file or create an empty dictionary
try:
withopen(vertex_key_path,"r")asfile:
# Read the file content
print("Read vertexai file path")
          content =file.read()

# If the file is empty or not valid JSON, create an empty dictionary
ifnot content ornot content.strip():
              service_account_key_data ={}
else:
# Attempt to load the existing JSON content
file.seek(0)
              service_account_key_data = json.load(file)
except FileNotFoundError:
# If the file doesn't exist, create an empty dictionary
      service_account_key_data ={}

# Create a temporary file
with tempfile.NamedTemporaryFile(mode="w+", delete=False)as temp_file:
# Write the updated content to the temporary file
      json.dump(service_account_key_data, temp_file, indent=2)

# Export the temporary file as GOOGLE_APPLICATION_CREDENTIALS
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= os.path.abspath(temp_file.name)
```

### Using GCP Service Account[​](#using-gcp-service-account "Direct link to Using GCP Service Account")

info

Trying to deploy LiteLLM on Google Cloud Run? Tutorial [here](https://docs.litellm.ai/docs/proxy/deploy#deploy-on-google-cloud-run)

1. Figure out the Service Account bound to the Google Cloud Run service

<!--THE END-->

2. Get the FULL EMAIL address of the corresponding Service Account
3. Next, go to IAM & Admin &gt; Manage Resources , select your top-level project that houses your Google Cloud Run Service

Click `Add Principal`

4. Specify the Service Account as the principal and Vertex AI User as the role

Once that's done, when you deploy the new container in the Google Cloud Run service, LiteLLM will have automatic access to all Vertex AI endpoints.

s/o @[Darien Kindlund](https://www.linkedin.com/in/kindlund/) for this tutorial

## **Rerank API**[​](#rerank-api "Direct link to rerank-api")

Vertex AI supports reranking through the Discovery Engine API, providing semantic ranking capabilities for document retrieval.

### Setup[​](#setup "Direct link to Setup")

Set your Google Cloud project ID:

```
export VERTEXAI_PROJECT="your-project-id"
```

### Usage[​](#usage-4 "Direct link to Usage")

```
from litellm import rerank

# Using the latest model (recommended)
response = rerank(
    model="vertex_ai/semantic-ranker-default@latest",
    query="What is Google Gemini?",
    documents=[
"Gemini is a cutting edge large language model created by Google.",
"The Gemini zodiac symbol often depicts two figures standing side-by-side.",
"Gemini is a constellation that can be seen in the night sky."
],
    top_n=2,
    return_documents=True# Set to False for ID-only responses
)

# Using specific model versions
response_v003 = rerank(
    model="vertex_ai/semantic-ranker-default-003",
    query="What is Google Gemini?",
    documents=documents,
    top_n=2
)

print(response.results)
```

### Parameters[​](#parameters "Direct link to Parameters")

ParameterTypeDescription`model`stringModel name (e.g., `vertex_ai/semantic-ranker-default@latest`)`query`stringSearch query`documents`listDocuments to rank`top_n`intNumber of top results to return`return_documents`boolReturn full content (True) or IDs only (False)

### Supported Models[​](#supported-models "Direct link to Supported Models")

- `semantic-ranker-default@latest`
- `semantic-ranker-fast@latest`
- `semantic-ranker-default-003`
- `semantic-ranker-default-002`

For detailed model specifications, see the [Google Cloud ranking API documentation](https://cloud.google.com/generative-ai-app-builder/docs/ranking#rank_or_rerank_a_set_of_records_according_to_a_query).

### Proxy Usage[​](#proxy-usage "Direct link to Proxy Usage")

Add to your `config.yaml`:

```
model_list:
-model_name: semantic-ranker-default@latest
litellm_params:
model: vertex_ai/semantic-ranker-default@latest
vertex_ai_project:"your-project-id"
vertex_ai_location:"us-central1"
vertex_ai_credentials:"path/to/service-account.json"
```

Start the proxy:

```
litellm --config /path/to/config.yaml
```

Test with curl:

```
curl http://0.0.0.0:4000/rerank \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "semantic-ranker-default@latest",
    "query": "What is Google Gemini?",
    "documents": [
      "Gemini is a cutting edge large language model created by Google.",
      "The Gemini zodiac symbol often depicts two figures standing side-by-side.",
      "Gemini is a constellation that can be seen in the night sky."
    ],
    "top_n": 2
  }'
```