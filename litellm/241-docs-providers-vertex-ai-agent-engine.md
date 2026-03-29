---
title: Vertex AI Agent Engine | liteLLM
url: https://docs.litellm.ai/docs/providers/vertex_ai_agent_engine
source: sitemap
fetched_at: 2026-01-21T19:50:38.197680748-03:00
rendered_js: false
word_count: 383
summary: This document provides instructions for integrating Vertex AI Agent Engine with LiteLLM, covering Python SDK usage, proxy configuration, and the visual A2A Gateway setup.
tags:
    - vertex-ai
    - agent-engine
    - litellm
    - reasoning-engines
    - openai-compatibility
    - agentic-workflows
    - python-sdk
category: tutorial
---

Call Vertex AI Agent Engine (Reasoning Engines) in the OpenAI Request/Response format.

PropertyDetailsDescriptionVertex AI Agent Engine provides hosted agent runtimes that can execute agentic workflows with foundation models, tools, and custom logic.Provider Route on LiteLLM`vertex_ai/agent_engine/{RESOURCE_NAME}`Supported Endpoints`/chat/completions`, `/v1/messages`, `/v1/responses`, `/v1/a2a/message/send`Provider Doc[Vertex AI Agent Engine ↗](https://cloud.google.com/vertex-ai/generative-ai/docs/reasoning-engine/overview)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Model Format[​](#model-format "Direct link to Model Format")

Model Format

```
vertex_ai/agent_engine/{RESOURCE_NAME}
```

**Example:**

- `vertex_ai/agent_engine/projects/1060139831167/locations/us-central1/reasoningEngines/8263861224643493888`

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Basic Agent Completion

```
import litellm

response = litellm.completion(
    model="vertex_ai/agent_engine/projects/1060139831167/locations/us-central1/reasoningEngines/8263861224643493888",
    messages=[
{"role":"user","content":"Explain machine learning in simple terms"}
],
)

print(response.choices[0].message.content)
```

Streaming Agent Responses

```
import litellm

response =await litellm.acompletion(
    model="vertex_ai/agent_engine/projects/1060139831167/locations/us-central1/reasoningEngines/8263861224643493888",
    messages=[
{"role":"user","content":"What are the key principles of software architecture?"}
],
    stream=True,
)

asyncfor chunk in response:
if chunk.choices[0].delta.content:
print(chunk.choices[0].delta.content, end="")
```

### LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

#### 1. Configure your model in config.yaml[​](#1-configure-your-model-in-configyaml "Direct link to 1. Configure your model in config.yaml")

- config.yaml

LiteLLM Proxy Configuration

```
model_list:
-model_name: vertex-agent-1
litellm_params:
model: vertex_ai/agent_engine/projects/1060139831167/locations/us-central1/reasoningEngines/8263861224643493888
vertex_project: your-project-id
vertex_location: us-central1
```

#### 2. Start the LiteLLM Proxy[​](#2-start-the-litellm-proxy "Direct link to 2. Start the LiteLLM Proxy")

Start LiteLLM Proxy

```
litellm --config config.yaml
```

#### 3. Make requests to your Vertex AI Agent Engine[​](#3-make-requests-to-your-vertex-ai-agent-engine "Direct link to 3. Make requests to your Vertex AI Agent Engine")

- Curl
- OpenAI Python SDK

Basic Agent Request

```
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "model": "vertex-agent-1",
    "messages": [
      {"role": "user", "content": "Summarize the main benefits of cloud computing"}
    ]
  }'
```

## LiteLLM A2A Gateway[​](#litellm-a2a-gateway "Direct link to LiteLLM A2A Gateway")

You can also connect to Vertex AI Agent Engine through LiteLLM's A2A (Agent-to-Agent) Gateway UI. This provides a visual way to register and test agents without writing code.

### 1. Navigate to Agents[​](#1-navigate-to-agents "Direct link to 1. Navigate to Agents")

From the sidebar, click "Agents" to open the agent management page, then click "+ Add New Agent".

![Click Agents](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/9a979927-ce6b-4168-9fba-e53e28f1c2c4/ascreenshot.jpeg?tl_px=0%2C14&br_px=1376%2C783&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=17%2C277)

![Add New Agent](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/a311750c-2e85-4589-99cb-2ce7e4021e77/ascreenshot.jpeg?tl_px=0%2C0&br_px=1376%2C769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=195%2C257)

### 2. Select Vertex AI Agent Engine Type[​](#2-select-vertex-ai-agent-engine-type "Direct link to 2. Select Vertex AI Agent Engine Type")

Click "A2A Standard" to see available agent types, then select "Vertex AI Agent Engine".

![Select A2A Standard](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/5b1acc4c-dc3f-4639-b4a0-e64b35c228fd/ascreenshot.jpeg?tl_px=52%2C0&br_px=1428%2C769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=524%2C271)

![Select Vertex AI Agent Engine](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/2f3bab61-3e02-4db7-84f0-82200a0f4136/ascreenshot.jpeg?tl_px=0%2C244&br_px=1376%2C1013&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=477%2C277)

### 3. Configure the Agent[​](#3-configure-the-agent "Direct link to 3. Configure the Agent")

Fill in the following fields:

- **Agent Name** - A friendly name for your agent (e.g., `my-vertex-agent`)
- **Reasoning Engine Resource ID** - The full resource path from Google Cloud Console (e.g., `projects/1060139831167/locations/us-central1/reasoningEngines/8263861224643493888`)
- **Vertex Project** - Your Google Cloud project ID
- **Vertex Location** - The region where your agent is deployed (e.g., `us-central1`)

![Enter Agent Name](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/695b84c7-9511-4337-bf19-f4505ab2b72b/ascreenshot.jpeg?tl_px=0%2C90&br_px=1376%2C859&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=480%2C276)

![Enter Resource ID](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/ddce64df-b3a3-4519-ab62-f137887bcea2/ascreenshot.jpeg?tl_px=0%2C294&br_px=1376%2C1063&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=440%2C277)

You can find the Resource ID in Google Cloud Console under Vertex AI &gt; Agent Engine:

![Copy Resource ID from Google Cloud Console](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/185d7f17-cbaa-45de-948d-49d2091805ea/ascreenshot.jpeg?tl_px=0%2C165&br_px=1376%2C934&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=493%2C276)

![Enter Vertex Project](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/a64da441-3e61-4811-a1e3-9f0b12c949ff/ascreenshot.jpeg?tl_px=0%2C233&br_px=1376%2C1002&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=501%2C277)

You can find the Project ID in Google Cloud Console:

![Copy Project ID from Google Cloud Console](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/9ecad3bb-a534-42d6-9604-33906014fad6/user_cropped_screenshot.webp?tl_px=0%2C0&br_px=1728%2C1028&force_format=jpeg&q=100&width=1120.0)

![Enter Vertex Location](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/316d1f38-4fb7-4377-86b6-c0fe7ac24383/ascreenshot.jpeg?tl_px=0%2C330&br_px=1376%2C1099&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=423%2C277)

### 4. Create Agent[​](#4-create-agent "Direct link to 4. Create Agent")

Click "Create Agent" to save your configuration.

![Create Agent](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/fb04b95d-793f-4eed-acf4-d1b3b5fa65e9/ascreenshot.jpeg?tl_px=352%2C347&br_px=1728%2C1117&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=623%2C498)

### 5. Test in Playground[​](#5-test-in-playground "Direct link to 5. Test in Playground")

Go to "Playground" in the sidebar to test your agent.

![Go to Playground](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/9e01369b-6102-4fe3-96a7-90082cadfd6e/ascreenshot.jpeg?tl_px=0%2C0&br_px=1376%2C769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=55%2C226)

### 6. Select A2A Endpoint[​](#6-select-a2a-endpoint "Direct link to 6. Select A2A Endpoint")

Click the endpoint dropdown and select `/v1/a2a/message/send`.

![Select Endpoint](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/d5aeac35-531b-4cf0-af2d-88f0a71fd736/ascreenshot.jpeg?tl_px=0%2C146&br_px=1376%2C915&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=299%2C277)

### 7. Select Your Agent and Send a Message[​](#7-select-your-agent-and-send-a-message "Direct link to 7. Select Your Agent and Send a Message")

Pick your Vertex AI Agent Engine from the dropdown and send a test message.

![Select Agent](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/353431f3-a0ba-4436-865d-ae11595e9cc4/ascreenshot.jpeg?tl_px=0%2C263&br_px=1376%2C1032&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=270%2C277)

![Send Message](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/fbfce72e-f50b-43e1-b6e5-0d41192d8e2d/ascreenshot.jpeg?tl_px=95%2C347&br_px=1471%2C1117&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=524%2C474)

![Agent Response](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-16/892dd826-fbf9-4530-8d82-95270889274a/ascreenshot.jpeg?tl_px=0%2C82&br_px=1376%2C851&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=485%2C277)

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

VariableDescription`GOOGLE_APPLICATION_CREDENTIALS`Path to service account JSON key file`VERTEXAI_PROJECT`Google Cloud project ID`VERTEXAI_LOCATION`Google Cloud region (default: `us-central1`)

```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
export VERTEXAI_PROJECT="your-project-id"
export VERTEXAI_LOCATION="us-central1"
```

## Further Reading[​](#further-reading "Direct link to Further Reading")

- [Vertex AI Agent Engine Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/reasoning-engine/overview)
- [Create a Reasoning Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/reasoning-engine/create)
- [A2A Agent Gateway](https://docs.litellm.ai/docs/a2a)
- [Vertex AI Provider](https://docs.litellm.ai/docs/providers/vertex)