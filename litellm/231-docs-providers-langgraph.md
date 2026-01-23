---
title: LangGraph | liteLLM
url: https://docs.litellm.ai/docs/providers/langgraph
source: sitemap
fetched_at: 2026-01-21T19:49:31.554487428-03:00
rendered_js: false
word_count: 424
summary: This document explains how to integrate LangGraph agents with LiteLLM, allowing users to call agents through the OpenAI chat completions format using Python, the LiteLLM Proxy, or the A2A Gateway UI.
tags:
    - langgraph
    - litellm
    - openai-format
    - agent-integration
    - python-sdk
    - llm-proxy
    - a2a-gateway
category: guide
---

Call LangGraph agents through LiteLLM using the OpenAI chat completions format.

PropertyDetailsDescriptionLangGraph is a framework for building stateful, multi-actor applications with LLMs. LiteLLM supports calling LangGraph agents via their streaming and non-streaming endpoints.Provider Route on LiteLLM`langgraph/{agent_id}`Provider Doc[LangGraph Platform ↗](https://langchain-ai.github.io/langgraph/cloud/quick_start/)

**Prerequisites:** You need a running LangGraph server. See [Setting Up a Local LangGraph Server](#setting-up-a-local-langgraph-server) below.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Model Format[​](#model-format "Direct link to Model Format")

**Example:**

- `langgraph/agent` - calls the default agent

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Basic LangGraph Completion

```
import litellm

response = litellm.completion(
    model="langgraph/agent",
    messages=[
{"role":"user","content":"What is 25 * 4?"}
],
    api_base="http://localhost:2024",
)

print(response.choices[0].message.content)
```

Streaming LangGraph Response

```
import litellm

response = litellm.completion(
    model="langgraph/agent",
    messages=[
{"role":"user","content":"What is the weather in Tokyo?"}
],
    api_base="http://localhost:2024",
    stream=True,
)

for chunk in response:
if chunk.choices[0].delta.content:
print(chunk.choices[0].delta.content, end="")
```

### LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

#### 1. Configure your model in config.yaml[​](#1-configure-your-model-in-configyaml "Direct link to 1. Configure your model in config.yaml")

- config.yaml

LiteLLM Proxy Configuration

```
model_list:
-model_name: langgraph-agent
litellm_params:
model: langgraph/agent
api_base: http://localhost:2024
```

#### 2. Start the LiteLLM Proxy[​](#2-start-the-litellm-proxy "Direct link to 2. Start the LiteLLM Proxy")

Start LiteLLM Proxy

```
litellm --config config.yaml
```

#### 3. Make requests to your LangGraph agent[​](#3-make-requests-to-your-langgraph-agent "Direct link to 3. Make requests to your LangGraph agent")

- Curl
- OpenAI Python SDK

Basic Request

```
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "model": "langgraph-agent",
    "messages": [
      {"role": "user", "content": "What is 25 * 4?"}
    ]
  }'
```

Streaming Request

```
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "model": "langgraph-agent",
    "messages": [
      {"role": "user", "content": "What is the weather in Tokyo?"}
    ],
    "stream": true
  }'
```

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

VariableDescription`LANGGRAPH_API_BASE`Base URL of your LangGraph server (default: `http://localhost:2024`)`LANGGRAPH_API_KEY`Optional API key for authentication

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

ParameterTypeDescription`model`stringThe agent ID in format `langgraph/{agent_id}``messages`arrayChat messages in OpenAI format`stream`booleanEnable streaming responses`api_base`stringLangGraph server URL`api_key`stringOptional API key

## Setting Up a Local LangGraph Server[​](#setting-up-a-local-langgraph-server "Direct link to Setting Up a Local LangGraph Server")

Before using LiteLLM with LangGraph, you need a running LangGraph server.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- Python 3.11+
- An LLM API key (OpenAI or Google Gemini)

### 1. Install the LangGraph CLI[​](#1-install-the-langgraph-cli "Direct link to 1. Install the LangGraph CLI")

```
pip install "langgraph-cli[inmem]"
```

### 2. Create a new LangGraph project[​](#2-create-a-new-langgraph-project "Direct link to 2. Create a new LangGraph project")

```
langgraph new my-agent --template new-langgraph-project-python
cd my-agent
```

### 3. Install dependencies[​](#3-install-dependencies "Direct link to 3. Install dependencies")

### 4. Set your API key[​](#4-set-your-api-key "Direct link to 4. Set your API key")

```
echo "OPENAI_API_KEY=your_key_here" > .env
```

### 5. Start the server[​](#5-start-the-server "Direct link to 5. Start the server")

The server will start at `http://localhost:2024`.

### Verify the server is running[​](#verify-the-server-is-running "Direct link to Verify the server is running")

```
curl -s --request POST \
  --url "http://localhost:2024/runs/wait" \
  --header 'Content-Type: application/json' \
  --data '{
    "assistant_id": "agent",
    "input": {
      "messages": [{"role": "human", "content": "Hello!"}]
    }
  }'
```

## LiteLLM A2A Gateway[​](#litellm-a2a-gateway "Direct link to LiteLLM A2A Gateway")

You can also connect to LangGraph agents through LiteLLM's A2A (Agent-to-Agent) Gateway UI. This provides a visual way to register and test agents without writing code.

### 1. Navigate to Agents[​](#1-navigate-to-agents "Direct link to 1. Navigate to Agents")

From the sidebar, click "Agents" to open the agent management page, then click "+ Add New Agent".

![Navigate to Agents](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/27429cae-f743-440a-a6aa-29fa7ee013db/ascreenshot.jpeg?tl_px=0%2C0&br_px=2201%2C1230&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=211%2C114)

### 2. Select LangGraph Agent Type[​](#2-select-langgraph-agent-type "Direct link to 2. Select LangGraph Agent Type")

Click "A2A Standard" to see available agent types, then search for "langgraph" and select "Connect to LangGraph agents via the LangGraph Platform API".

![Select A2A Standard](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/4add4088-683d-49ca-9374-23fd65dddf8e/ascreenshot.jpeg?tl_px=0%2C0&br_px=2201%2C1230&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=511%2C139)

![Select LangGraph](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/fd197907-47c7-4e05-959c-c0d42264263c/ascreenshot.jpeg?tl_px=0%2C0&br_px=2201%2C1230&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=431%2C246)

### 3. Configure the Agent[​](#3-configure-the-agent "Direct link to 3. Configure the Agent")

Fill in the following fields:

- **Agent Name** - A unique identifier (e.g., `lan-agent`)
- **LangGraph API Base** - Your LangGraph server URL, typically `http://127.0.0.1:2024/`
- **API Key** - Optional. LangGraph doesn't require an API key by default
- **Assistant ID** - Not used by LangGraph, you can enter any string here

![Enter Agent Name](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/adce3df9-a67c-4d23-b2b5-05120738bc46/ascreenshot.jpeg?tl_px=0%2C0&br_px=2617%2C1463&force_format=jpeg&q=100&width=1120.0)

![Enter API Base](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/6a6a03a7-f235-41db-b4ba-d32ced330f25/ascreenshot.jpeg?tl_px=0%2C251&br_px=2617%2C1714&force_format=jpeg&q=100&width=1120.0)

Click "Create Agent" to save.

![Create Agent](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/ddee4295-9a32-4cda-8e3f-543e5047eb6a/ascreenshot.jpeg?tl_px=416%2C653&br_px=2618%2C1883&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=686%2C316)

### 4. Test in Playground[​](#4-test-in-playground "Direct link to 4. Test in Playground")

Go to "Playground" in the sidebar to test your agent. Change the endpoint type to `/v1/a2a/message/send`.

![Go to Playground](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/c4262189-95ac-4fbc-b5af-8aba8126e4f7/ascreenshot.jpeg?tl_px=0%2C0&br_px=2201%2C1230&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=41%2C104)

![Select A2A Endpoint](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/6cbc8e93-7d0c-47fc-9ad4-562663f759d5/ascreenshot.jpeg?tl_px=0%2C0&br_px=2201%2C1230&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=324%2C265)

### 5. Select Your Agent and Send a Message[​](#5-select-your-agent-and-send-a-message "Direct link to 5. Select Your Agent and Send a Message")

Pick your LangGraph agent from the dropdown and send a test message.

![Select Agent](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/d01da2f1-3b89-47d7-ba95-de2dd8efbc1e/ascreenshot.jpeg?tl_px=0%2C92&br_px=2201%2C1323&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=348%2C277)

![Send Message](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/79db724e-a99e-493a-9747-dc91cb398370/ascreenshot.jpeg?tl_px=51%2C653&br_px=2252%2C1883&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=524%2C444)

The agent responds with its capabilities. You can now interact with your LangGraph agent through the A2A protocol.

![Agent Response](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-13/82aa546a-0eb5-4836-b986-9aefcfe09e10/ascreenshot.jpeg?tl_px=295%2C28&br_px=2496%2C1259&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=524%2C277)

## Further Reading[​](#further-reading "Direct link to Further Reading")

- [LangGraph Platform Documentation](https://langchain-ai.github.io/langgraph/cloud/quick_start/)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)
- [A2A Agent Gateway](https://docs.litellm.ai/docs/a2a)
- [A2A Cost Tracking](https://docs.litellm.ai/docs/a2a_cost_tracking)