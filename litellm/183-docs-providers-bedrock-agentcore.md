---
title: Bedrock AgentCore | liteLLM
url: https://docs.litellm.ai/docs/providers/bedrock_agentcore
source: sitemap
fetched_at: 2026-01-21T19:48:25.748174586-03:00
rendered_js: false
word_count: 215
summary: This document explains how to integrate and call Amazon Bedrock AgentCore runtimes using the LiteLLM SDK and Proxy with OpenAI-compatible request formats.
tags:
    - amazon-bedrock
    - agentcore
    - litellm
    - aws
    - python-sdk
    - llm-proxy
    - api-integration
category: guide
---

Call Bedrock AgentCore in the OpenAI Request/Response format.

PropertyDetailsDescriptionAmazon Bedrock AgentCore provides direct access to hosted agent runtimes for executing agentic workflows with foundation models.Provider Route on LiteLLM`bedrock/agentcore/{AGENT_RUNTIME_ARN}`Provider Doc[AWS Bedrock AgentCore ↗](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agentcore_InvokeAgentRuntime.html)

info

This documentation is for **AgentCore Agents** (agent runtimes). If you want to use AgentCore MCP servers, add them as you would any other MCP server. See the [MCP documentation](https://docs.litellm.ai/docs/mcp) for details.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Model Format to LiteLLM[​](#model-format-to-litellm "Direct link to Model Format to LiteLLM")

To call a bedrock agent runtime through LiteLLM, use the following model format.

Here the `model=bedrock/agentcore/` tells LiteLLM to call the bedrock `InvokeAgentRuntime` API.

Model Format to LiteLLM

```
bedrock/agentcore/{AGENT_RUNTIME_ARN}
```

**Example:**

- `bedrock/agentcore/arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent-runtime`

You can find the Agent Runtime ARN in your AWS Bedrock console under AgentCore.

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Basic AgentCore Completion

```
import litellm

# Make a completion request to your AgentCore runtime
response = litellm.completion(
    model="bedrock/agentcore/arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent-runtime",
    messages=[
{
"role":"user",
"content":"Explain machine learning in simple terms"
}
],
)

print(response.choices[0].message.content)
print(f"Usage: {response.usage}")
```

Streaming AgentCore Responses

```
import litellm

# Stream responses from your AgentCore runtime
response = litellm.completion(
    model="bedrock/agentcore/arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent-runtime",
    messages=[
{
"role":"user",
"content":"What are the key principles of software architecture?"
}
],
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
-model_name: agentcore-runtime-1
litellm_params:
model: bedrock/agentcore/arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent-runtime
aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID
aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
aws_region_name: us-west-2

-model_name: agentcore-runtime-2
litellm_params:
model: bedrock/agentcore/arn:aws:bedrock-agentcore:us-east-1:987654321098:runtime/production-runtime
aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID
aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
aws_region_name: us-east-1
```

#### 2. Start the LiteLLM Proxy[​](#2-start-the-litellm-proxy "Direct link to 2. Start the LiteLLM Proxy")

Start LiteLLM Proxy

```
litellm --config config.yaml
```

#### 3. Make requests to your AgentCore runtimes[​](#3-make-requests-to-your-agentcore-runtimes "Direct link to 3. Make requests to your AgentCore runtimes")

- Curl
- OpenAI Python SDK

Basic AgentCore Request

```
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "model": "agentcore-runtime-1",
    "messages": [
      {
        "role": "user", 
        "content": "Summarize the main benefits of cloud computing"
      }
    ]
  }'
```

Streaming AgentCore Request

```
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "model": "agentcore-runtime-2",
    "messages": [
      {
        "role": "user",
        "content": "Explain the differences between SQL and NoSQL databases"
      }
    ],
    "stream": true
  }'
```

## Provider-specific Parameters[​](#provider-specific-parameters "Direct link to Provider-specific Parameters")

AgentCore supports additional parameters that can be passed to customize the runtime invocation.

- SDK
- Proxy

Using AgentCore-specific parameters

```
from litellm import completion

response = litellm.completion(
    model="bedrock/agentcore/arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent-runtime",
    messages=[
{
"role":"user",
"content":"Analyze this data and provide insights",
}
],
    qualifier="production",# PROVIDER-SPECIFIC: Runtime qualifier/version
    runtimeSessionId="session-abc-123",# PROVIDER-SPECIFIC: Custom session ID
)
```

### Available Parameters[​](#available-parameters "Direct link to Available Parameters")

ParameterTypeDescription`qualifier`stringOptional runtime qualifier/version to invoke a specific version of the agent runtime`runtimeSessionId`stringOptional custom session ID (must be 33+ characters). If not provided, LiteLLM generates one automatically

## Further Reading[​](#further-reading "Direct link to Further Reading")

- [AWS Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agentcore_InvokeAgentRuntime.html)
- [LiteLLM Authentication to Bedrock](https://docs.litellm.ai/docs/providers/bedrock#boto3---authentication)