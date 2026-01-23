---
title: Code Interpreter | liteLLM
url: https://docs.litellm.ai/docs/guides/code_interpreter
source: sitemap
fetched_at: 2026-01-21T19:45:22.081348725-03:00
rendered_js: false
word_count: 151
summary: This document provides instructions for using OpenAI's Code Interpreter tool through the LiteLLM Python SDK and AI Gateway, including code execution and file management.
tags:
    - litellm
    - openai
    - code-interpreter
    - python-sdk
    - ai-gateway
    - data-visualization
category: guide
---

Use OpenAI's Code Interpreter tool to execute Python code in a secure, sandboxed environment.

FeatureSupportedLiteLLM Python SDK✅LiteLLM AI Gateway✅Supported Providers`openai`

## LiteLLM AI Gateway[​](#litellm-ai-gateway "Direct link to LiteLLM AI Gateway")

### API (OpenAI SDK)[​](#api-openai-sdk "Direct link to API (OpenAI SDK)")

Use the OpenAI SDK pointed at your LiteLLM Gateway:

code\_interpreter\_gateway.py

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",# Your LiteLLM API key
    base_url="http://localhost:4000"
)

response = client.responses.create(
    model="openai/gpt-4o",
    tools=[{"type":"code_interpreter"}],
input="Calculate the first 20 fibonacci numbers and plot them"
)

print(response)
```

#### Streaming[​](#streaming "Direct link to Streaming")

code\_interpreter\_streaming.py

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",
    base_url="http://localhost:4000"
)

stream = client.responses.create(
    model="openai/gpt-4o",
    tools=[{"type":"code_interpreter"}],
input="Generate sample sales data CSV and create a visualization",
    stream=True
)

for event in stream:
print(event)
```

#### Get Generated File Content[​](#get-generated-file-content "Direct link to Get Generated File Content")

get\_file\_content\_gateway.py

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",
    base_url="http://localhost:4000"
)

# 1. Run code interpreter
response = client.responses.create(
    model="openai/gpt-4o",
    tools=[{"type":"code_interpreter"}],
input="Create a scatter plot and save as PNG"
)

# 2. Get container_id from response
container_id = response.output[0].container_id

# 3. List files
files = client.containers.files.list(container_id=container_id)

# 4. Download file content
forfilein files.data:
    content = client.containers.files.content(
        container_id=container_id,
        file_id=file.id
)

withopen(file.filename,"wb")as f:
        f.write(content.read())
print(f"Downloaded: {file.filename}")
```

### AI Gateway UI[​](#ai-gateway-ui "Direct link to AI Gateway UI")

The LiteLLM Admin UI includes built-in Code Interpreter support.

**Steps:**

1. Go to **Playground** in the LiteLLM UI
2. Select an **OpenAI model** (e.g., `openai/gpt-4o`)
3. Select `/v1/responses` as the endpoint under **Endpoint Type**
4. Toggle **Code Interpreter** in the left panel
5. Send a prompt requesting code execution or file generation

The UI will display:

- Executed Python code (collapsible)
- Generated images inline
- Download links for files (CSVs, etc.)

## LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

### Run Code Interpreter[​](#run-code-interpreter "Direct link to Run Code Interpreter")

code\_interpreter.py

```
import litellm

response = litellm.responses(
    model="openai/gpt-4o",
input="Generate a bar chart of quarterly sales and save as PNG",
    tools=[{"type":"code_interpreter"}]
)

print(response)
```

### Get Generated File Content[​](#get-generated-file-content-1 "Direct link to Get Generated File Content")

After Code Interpreter runs, retrieve the generated files:

get\_file\_content.py

```
import litellm

# 1. Run code interpreter
response = litellm.responses(
    model="openai/gpt-4o",
input="Create a pie chart of market share and save as PNG",
    tools=[{"type":"code_interpreter"}]
)

# 2. Extract container_id from response
container_id = response.output[0].container_id  # e.g. "cntr_abc123..."

# 3. List files in container
files = litellm.list_container_files(
    container_id=container_id,
    custom_llm_provider="openai"
)

# 4. Download each file
forfilein files.data:
    content = litellm.retrieve_container_file_content(
        container_id=container_id,
        file_id=file.id,
        custom_llm_provider="openai"
)

withopen(file.filename,"wb")as f:
        f.write(content)
print(f"Downloaded: {file.filename}")
```

- [Containers API](https://docs.litellm.ai/docs/containers) - Manage containers
- [Container Files API](https://docs.litellm.ai/docs/container_files) - Manage files within containers
- [OpenAI Code Interpreter Docs](https://platform.openai.com/docs/guides/tools-code-interpreter) - Official OpenAI documentation