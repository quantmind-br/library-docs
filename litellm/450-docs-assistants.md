---
title: /assistants | liteLLM
url: https://docs.litellm.ai/docs/assistants
source: sitemap
fetched_at: 2026-01-21T19:44:03.799252406-03:00
rendered_js: false
word_count: 160
summary: This document explains how to use the OpenAI Assistants API via LiteLLM, covering thread management, message handling, and assistant execution while detailing its upcoming deprecation.
tags:
    - litellm
    - assistants-api
    - openai
    - azure-openai
    - thread-management
    - streaming
    - python-sdk
category: api
---

Deprecation Notice

OpenAI has deprecated the Assistants API. It will shut down on **August 26, 2026**.

Consider migrating to the [Responses API](https://docs.litellm.ai/docs/response_api) instead. See [OpenAI's migration guide](https://platform.openai.com/docs/guides/responses-vs-assistants) for details.

Covers Threads, Messages, Assistants.

LiteLLM currently covers:

- Create Assistants
- Delete Assistants
- Get Assistants
- Create Thread
- Get Thread
- Add Messages
- Get Messages
- Run Thread

## **Supported Providers**:[​](#supported-providers "Direct link to supported-providers")

- [OpenAI](#quick-start)
- [Azure OpenAI](#azure-openai)
- [OpenAI-Compatible APIs](#openai-compatible-apis)

## Quick Start[​](#quick-start "Direct link to Quick Start")

Call an existing Assistant.

- Get the Assistant
- Create a Thread when a user starts a conversation.
- Add Messages to the Thread as the user asks questions.
- Run the Assistant on the Thread to generate a response by calling the model and the tools.

### SDK + PROXY[​](#sdk--proxy "Direct link to SDK + PROXY")

- SDK
- PROXY

**Create an Assistant**

```
import litellm
import os 

# setup env
os.environ["OPENAI_API_KEY"]="sk-.."

assistant = litellm.create_assistants(
            custom_llm_provider="openai",
            model="gpt-4-turbo",
            instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
            name="Math Tutor",
            tools=[{"type":"code_interpreter"}],
)

### ASYNC USAGE ### 
# assistant = await litellm.acreate_assistants(
#             custom_llm_provider="openai",
#             model="gpt-4-turbo",
#             instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
#             name="Math Tutor",
#             tools=[{"type": "code_interpreter"}],
# )
```

**Get the Assistant**

```
from litellm import get_assistants, aget_assistants
import os 

# setup env
os.environ["OPENAI_API_KEY"]="sk-.."

assistants = get_assistants(custom_llm_provider="openai")

### ASYNC USAGE ### 
# assistants = await aget_assistants(custom_llm_provider="openai")
```

**Create a Thread**

```
from litellm import create_thread, acreate_thread
import os 

os.environ["OPENAI_API_KEY"]="sk-.."

new_thread = create_thread(
            custom_llm_provider="openai",
            messages=[{"role":"user","content":"Hey, how's it going?"}],# type: ignore
)

### ASYNC USAGE ### 
# new_thread = await acreate_thread(custom_llm_provider="openai",messages=[{"role": "user", "content": "Hey, how's it going?"}])
```

**Add Messages to the Thread**

```
from litellm import create_thread, get_thread, aget_thread, add_message, a_add_message
import os 

os.environ["OPENAI_API_KEY"]="sk-.."

## CREATE A THREAD
_new_thread = create_thread(
            custom_llm_provider="openai",
            messages=[{"role":"user","content":"Hey, how's it going?"}],# type: ignore
)

## OR retrieve existing thread
received_thread = get_thread(
            custom_llm_provider="openai",
            thread_id=_new_thread.id,
)

### ASYNC USAGE ### 
# received_thread = await aget_thread(custom_llm_provider="openai", thread_id=_new_thread.id,)

## ADD MESSAGE TO THREAD
message ={"role":"user","content":"Hey, how's it going?"}
added_message = add_message(
            thread_id=_new_thread.id, custom_llm_provider="openai",**message
)

### ASYNC USAGE ### 
# added_message = await a_add_message(thread_id=_new_thread.id, custom_llm_provider="openai", **message)
```

**Run the Assistant on the Thread**

```
from litellm import get_assistants, create_thread, add_message, run_thread, arun_thread
import os 

os.environ["OPENAI_API_KEY"]="sk-.."
assistants = get_assistants(custom_llm_provider="openai")

## get the first assistant ###
assistant_id = assistants.data[0].id

## GET A THREAD
_new_thread = create_thread(
            custom_llm_provider="openai",
            messages=[{"role":"user","content":"Hey, how's it going?"}],# type: ignore
)

## ADD MESSAGE
message ={"role":"user","content":"Hey, how's it going?"}
added_message = add_message(
            thread_id=_new_thread.id, custom_llm_provider="openai",**message
)

## 🚨 RUN THREAD
response = run_thread(
            custom_llm_provider="openai", thread_id=thread_id, assistant_id=assistant_id
)

### ASYNC USAGE ### 
# response = await arun_thread(custom_llm_provider="openai", thread_id=thread_id, assistant_id=assistant_id)

print(f"run_thread: {run_thread}")
```

## Streaming[​](#streaming "Direct link to Streaming")

- SDK
- PROXY

```
from litellm import run_thread_stream 
import os

os.environ["OPENAI_API_KEY"]="sk-.."

message ={"role":"user","content":"Hey, how's it going?"}

data ={"custom_llm_provider":"openai","thread_id": _new_thread.id,"assistant_id": assistant_id,**message}

run = run_thread_stream(**data)
with run as run:
assertisinstance(run, AssistantEventHandler)
for chunk in run:
print(f"chunk: {chunk}")
    run.until_done()
```

## [👉 Proxy API Reference](https://litellm-api.up.railway.app/#/assistants)[​](#-proxy-api-reference "Direct link to -proxy-api-reference")

## Azure OpenAI[​](#azure-openai "Direct link to Azure OpenAI")

**config**

```
assistant_settings:
custom_llm_provider: azure
litellm_params:
api_key: os.environ/AZURE_API_KEY
api_base: os.environ/AZURE_API_BASE
```

**curl**

```
curl -X POST "http://localhost:4000/v1/assistants" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    "name": "Math Tutor",
    "tools": [{"type": "code_interpreter"}],
    "model": "<my-azure-deployment-name>"
  }'
```

## OpenAI-Compatible APIs[​](#openai-compatible-apis "Direct link to OpenAI-Compatible APIs")

To call openai-compatible Assistants API's (eg. Astra Assistants API), just add `openai/` to the model name:

**config**

```
assistant_settings:
custom_llm_provider: openai
litellm_params:
api_key: os.environ/ASTRA_API_KEY
api_base: os.environ/ASTRA_API_BASE
```

**curl**

```
curl -X POST "http://localhost:4000/v1/assistants" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    "name": "Math Tutor",
    "tools": [{"type": "code_interpreter"}],
    "model": "openai/<my-astra-model-name>"
  }'
```