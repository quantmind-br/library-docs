---
title: Azure AI Foundry Agents | liteLLM
url: https://docs.litellm.ai/docs/providers/azure_ai_agents
source: sitemap
fetched_at: 2026-01-21T19:48:03.657961835-03:00
rendered_js: false
word_count: 656
summary: This document provides instructions for integrating Azure AI Foundry Agents with LiteLLM, covering authentication methods, Python SDK usage, and thread management for stateful conversations.
tags:
    - azure-ai-foundry
    - litellm
    - agents
    - authentication
    - python-sdk
    - azure-ad
    - thread-management
category: guide
---

Call Azure AI Foundry Agents in the OpenAI Request/Response format.

PropertyDetailsDescriptionAzure AI Foundry Agents provides hosted agent runtimes that can execute agentic workflows with foundation models, tools, and code interpreters.Provider Route on LiteLLM`azure_ai/agents/{AGENT_ID}`Provider Doc[Azure AI Foundry Agents ↗](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/quickstart)

## Authentication[​](#authentication "Direct link to Authentication")

Azure AI Foundry Agents require **Azure AD authentication** (not API keys). You can authenticate using:

### Option 1: Service Principal (Recommended for Production)[​](#option-1-service-principal-recommended-for-production "Direct link to Option 1: Service Principal (Recommended for Production)")

Set these environment variables:

```
export AZURE_TENANT_ID="your-tenant-id"
export AZURE_CLIENT_ID="your-client-id"
export AZURE_CLIENT_SECRET="your-client-secret"
```

LiteLLM will automatically obtain an Azure AD token using these credentials.

Pass a token directly via `api_key`:

```
# Get token via Azure CLI
az account get-access-token --resource "https://ai.azure.com" --query accessToken -o tsv
```

### Required Azure Role[​](#required-azure-role "Direct link to Required Azure Role")

Your Service Principal or user must have the **Azure AI Developer** or **Azure AI User** role on your Azure AI Foundry project.

To assign via Azure CLI:

```
az role assignment create \
  --assignee-object-id "<service-principal-object-id>" \
  --assignee-principal-type "ServicePrincipal" \
  --role "Azure AI Developer" \
  --scope "/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<resource>"
```

Or add via **Azure AI Foundry Portal** → Your Project → **Project users** → **+ New user**.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Model Format to LiteLLM[​](#model-format-to-litellm "Direct link to Model Format to LiteLLM")

To call an Azure AI Foundry Agent through LiteLLM, use the following model format.

Here the `model=azure_ai/agents/` tells LiteLLM to call the Azure AI Foundry Agent Service API.

Model Format to LiteLLM

```
azure_ai/agents/{AGENT_ID}
```

**Example:**

- `azure_ai/agents/asst_abc123`

You can find the Agent ID in your Azure AI Foundry portal under Agents.

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Basic Agent Completion

```
import litellm

# Make a completion request to your Azure AI Foundry Agent
# Uses AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET env vars for auth
response = litellm.completion(
    model="azure_ai/agents/asst_abc123",
    messages=[
{
"role":"user",
"content":"Explain machine learning in simple terms"
}
],
    api_base="https://your-resource.services.ai.azure.com/api/projects/your-project",
)

print(response.choices[0].message.content)
print(f"Usage: {response.usage}")
```

Streaming Agent Responses

```
import litellm

# Stream responses from your Azure AI Foundry Agent
response =await litellm.acompletion(
    model="azure_ai/agents/asst_abc123",
    messages=[
{
"role":"user",
"content":"What are the key principles of software architecture?"
}
],
    api_base="https://your-resource.services.ai.azure.com/api/projects/your-project",
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
-model_name: azure-agent-1
litellm_params:
model: azure_ai/agents/asst_abc123
api_base: https://your-resource.services.ai.azure.com/api/projects/your-project
# Service Principal auth (recommended)
tenant_id: os.environ/AZURE_TENANT_ID
client_id: os.environ/AZURE_CLIENT_ID
client_secret: os.environ/AZURE_CLIENT_SECRET

-model_name: azure-agent-math-tutor
litellm_params:
model: azure_ai/agents/asst_def456
api_base: https://your-resource.services.ai.azure.com/api/projects/your-project
# Or pass Azure AD token directly
api_key: os.environ/AZURE_AD_TOKEN
```

#### 2. Start the LiteLLM Proxy[​](#2-start-the-litellm-proxy "Direct link to 2. Start the LiteLLM Proxy")

Start LiteLLM Proxy

```
litellm --config config.yaml
```

#### 3. Make requests to your Azure AI Foundry Agents[​](#3-make-requests-to-your-azure-ai-foundry-agents "Direct link to 3. Make requests to your Azure AI Foundry Agents")

- Curl
- OpenAI Python SDK

Basic Agent Request

```
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "model": "azure-agent-1",
    "messages": [
      {
        "role": "user", 
        "content": "Summarize the main benefits of cloud computing"
      }
    ]
  }'
```

Streaming Agent Request

```
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "model": "azure-agent-math-tutor",
    "messages": [
      {
        "role": "user",
        "content": "What is 25 * 4?"
      }
    ],
    "stream": true
  }'
```

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

VariableDescription`AZURE_TENANT_ID`Azure AD tenant ID for Service Principal auth`AZURE_CLIENT_ID`Application (client) ID of your Service Principal`AZURE_CLIENT_SECRET`Client secret for your Service Principal

```
export AZURE_TENANT_ID="your-tenant-id"
export AZURE_CLIENT_ID="your-client-id"
export AZURE_CLIENT_SECRET="your-client-secret"
```

## Conversation Continuity (Thread Management)[​](#conversation-continuity-thread-management "Direct link to Conversation Continuity (Thread Management)")

Azure AI Foundry Agents use threads to maintain conversation context. LiteLLM automatically manages threads for you, but you can also pass an existing thread ID to continue a conversation.

Continuing a Conversation

```
import litellm

# First message creates a new thread
response1 =await litellm.acompletion(
    model="azure_ai/agents/asst_abc123",
    messages=[{"role":"user","content":"My name is Alice"}],
    api_base="https://your-resource.services.ai.azure.com/api/projects/your-project",
)

# Get the thread_id from the response
thread_id = response1._hidden_params.get("thread_id")

# Continue the conversation using the same thread
response2 =await litellm.acompletion(
    model="azure_ai/agents/asst_abc123",
    messages=[{"role":"user","content":"What's my name?"}],
    api_base="https://your-resource.services.ai.azure.com/api/projects/your-project",
    thread_id=thread_id,# Pass the thread_id to continue conversation
)

print(response2.choices[0].message.content)# Should mention "Alice"
```

## Provider-specific Parameters[​](#provider-specific-parameters "Direct link to Provider-specific Parameters")

Azure AI Foundry Agents support additional parameters that can be passed to customize the agent invocation.

- SDK
- Proxy

Using Agent-specific parameters

```
from litellm import completion

response = litellm.completion(
    model="azure_ai/agents/asst_abc123",
    messages=[
{
"role":"user",
"content":"Analyze this data and provide insights",
}
],
    api_base="https://your-resource.services.ai.azure.com/api/projects/your-project",
    thread_id="thread_abc123",# Optional: Continue existing conversation
    instructions="Be concise and focus on key insights",# Optional: Override agent instructions
)
```

### Available Parameters[​](#available-parameters "Direct link to Available Parameters")

ParameterTypeDescription`thread_id`stringOptional thread ID to continue an existing conversation`instructions`stringOptional instructions to override the agent's default instructions for this run

## LiteLLM A2A Gateway[​](#litellm-a2a-gateway "Direct link to LiteLLM A2A Gateway")

You can also connect to Azure AI Foundry Agents through LiteLLM's A2A (Agent-to-Agent) Gateway UI. This provides a visual way to register and test agents without writing code.

### 1. Navigate to Agents[​](#1-navigate-to-agents "Direct link to 1. Navigate to Agents")

From the sidebar, click "Agents" to open the agent management page, then click "+ Add New Agent".

![Add New Agent](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/f8efe335-a08a-4f2b-9f7f-de28e4d58b05/ascreenshot.jpeg?tl_px=0%2C0&br_px=2201%2C1230&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=217%2C118)

### 2. Select Azure AI Foundry Agent Type[​](#2-select-azure-ai-foundry-agent-type "Direct link to 2. Select Azure AI Foundry Agent Type")

Click "A2A Standard" to see available agent types, then select "Azure AI Foundry".

![Select A2A Standard](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/ede38044-3e18-43b9-afe3-b7513bf9963e/ascreenshot.jpeg?tl_px=0%2C0&br_px=2201%2C1230&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=409%2C143)

![Select Azure AI Foundry](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/33c396fc-a927-4b03-8ee2-ea04950b12c1/ascreenshot.jpeg?tl_px=0%2C86&br_px=2201%2C1317&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=433%2C277)

### 3. Configure the Agent[​](#3-configure-the-agent "Direct link to 3. Configure the Agent")

Fill in the following fields:

#### Agent Name[​](#agent-name "Direct link to Agent Name")

Enter a friendly agent name - callers will see this name as the agent available.

![Enter Agent Name](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/18c02804-7612-40c4-9ba4-3f1a4c0725d5/ascreenshot.jpeg?tl_px=0%2C0&br_px=2617%2C1463&force_format=jpeg&q=100&width=1120.0)

#### Agent ID[​](#agent-id "Direct link to Agent ID")

Get the Agent ID from your Azure AI Foundry portal:

1. Go to [https://ai.azure.com/](https://ai.azure.com/) and click "Agents"

<!--THE END-->

![Azure Agents](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/5e29fc48-c0f7-4b6d-8313-2063d1240d15/ascreenshot.jpeg?tl_px=0%2C0&br_px=2618%2C1463&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=39%2C187)

2. Copy the "ID" of the agent you want to add (e.g., `asst_hbnoK9BOCcHhC3lC4MDroVGG`)

<!--THE END-->

![Copy Agent ID](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/bf17dfec-a627-41c6-9121-3935e86d3700/ascreenshot.jpeg?tl_px=0%2C0&br_px=2618%2C1463&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=504%2C241)

3. Paste the Agent ID in LiteLLM - this tells LiteLLM which agent to invoke on Azure Foundry

![Paste Agent ID](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/45230c28-54f6-441c-9a20-4ef8b74076e2/ascreenshot.jpeg?tl_px=0%2C97&br_px=2617%2C1560&force_format=jpeg&q=100&width=1120.0)

#### Azure AI API Base[​](#azure-ai-api-base "Direct link to Azure AI API Base")

Get your API base URL from Azure AI Foundry:

1. Go to [https://ai.azure.com/](https://ai.azure.com/) and click "Overview"
2. Under libraries, select Microsoft Foundry
3. Get your endpoint - it should look like `https://<domain>.services.ai.azure.com/api/projects/<project-name>`

<!--THE END-->

![Get API Base](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/60e2c735-4480-44b7-ab12-d69f4200b12c/ascreenshot.jpeg?tl_px=0%2C40&br_px=2618%2C1503&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=278%2C277)

4. Paste the URL in LiteLLM

![Paste API Base](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/e9c6f48e-7602-449a-9261-0df4a0a66876/ascreenshot.jpeg?tl_px=267%2C456&br_px=2468%2C1687&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=524%2C277)

#### Authentication[​](#authentication-1 "Direct link to Authentication")

Add your Azure AD credentials for authentication:

- **Azure Tenant ID**
- **Azure Client ID**
- **Azure Client Secret**

![Add Auth](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/e5e2b636-cf2e-4283-a1cc-8d497d349243/ascreenshot.jpeg?tl_px=0%2C653&br_px=2201%2C1883&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=339%2C405)

Click "Create Agent" to save.

![Create Agent](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/799a720a-639e-4217-a6f5-51687fc07611/ascreenshot.jpeg?tl_px=416%2C653&br_px=2618%2C1883&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=693%2C519)

### 4. Test in Playground[​](#4-test-in-playground "Direct link to 4. Test in Playground")

Go to "Playground" in the sidebar to test your agent.

![Go to Playground](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/7da84247-db1c-4d55-9015-6e3d60ea63ce/ascreenshot.jpeg?tl_px=0%2C0&br_px=2201%2C1230&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=63%2C106)

Change the endpoint type to `/v1/a2a/message/send`.

![Select A2A Endpoint](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/733265a8-412d-4eac-bc19-03436d7846c4/ascreenshot.jpeg?tl_px=0%2C0&br_px=2201%2C1230&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=286%2C234)

### 5. Select Your Agent and Send a Message[​](#5-select-your-agent-and-send-a-message "Direct link to 5. Select Your Agent and Send a Message")

Pick your Azure AI Foundry agent from the dropdown and send a test message.

![Select Agent](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/59a8e66e-6f82-42e3-ab48-78355464e6be/ascreenshot.jpeg?tl_px=0%2C28&br_px=2201%2C1259&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=269%2C277)

The agent responds with its capabilities. You can now interact with your Azure AI Foundry agent through the A2A protocol.

![Agent Response](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-12-14/a0aafb69-6c28-4977-8210-96f9de750cdf/ascreenshot.jpeg?tl_px=0%2C0&br_px=2201%2C1230&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https%3A%2F%2Fcolony-recorder.s3.us-west-1.amazonaws.com%2Fimages%2Fwatermarks%2FFB923C_standard.png&wat_pad=487%2C272)

## Further Reading[​](#further-reading "Direct link to Further Reading")

- [Azure AI Foundry Agents Documentation](https://learn.microsoft.com/en-us/azure/ai-services/agents/)
- [Create Thread and Run API Reference](https://learn.microsoft.com/en-us/rest/api/aifoundry/aiagents/create-thread-and-run/create-thread-and-run)
- [A2A Agent Gateway](https://docs.litellm.ai/docs/a2a)
- [A2A Cost Tracking](https://docs.litellm.ai/docs/a2a_cost_tracking)