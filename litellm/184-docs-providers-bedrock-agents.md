---
title: Bedrock Agents | liteLLM
url: https://docs.litellm.ai/docs/providers/bedrock_agents
source: sitemap
fetched_at: 2026-01-21T19:48:26.810873714-03:00
rendered_js: false
word_count: 167
summary: This document provides instructions for calling Amazon Bedrock Agents through LiteLLM using the OpenAI request/response format via the Python SDK and Proxy.
tags:
    - amazon-bedrock
    - bedrock-agents
    - litellm
    - aws
    - openai-compatibility
    - llm-proxy
category: guide
---

Call Bedrock Agents in the OpenAI Request/Response format.

PropertyDetailsDescriptionAmazon Bedrock Agents use the reasoning of foundation models (FMs), APIs, and data to break down user requests, gather relevant information, and efficiently complete tasks.Provider Route on LiteLLM`bedrock/agent/{AGENT_ID}/{ALIAS_ID}`Provider Doc[AWS Bedrock Agents ↗](https://aws.amazon.com/bedrock/agents/)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Model Format to LiteLLM[​](#model-format-to-litellm "Direct link to Model Format to LiteLLM")

To call a bedrock agent through LiteLLM, you need to use the following model format to call the agent.

Here the `model=bedrock/agent/` tells LiteLLM to call the bedrock `InvokeAgent` API.

Model Format to LiteLLM

```
bedrock/agent/{AGENT_ID}/{ALIAS_ID}
```

**Example:**

- `bedrock/agent/L1RT58GYRW/MFPSBCXYTW`
- `bedrock/agent/ABCD1234/LIVE`

You can find these IDs in your AWS Bedrock console under Agents.

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Basic Agent Completion

```
import litellm

# Make a completion request to your Bedrock Agent
response = litellm.completion(
    model="bedrock/agent/L1RT58GYRW/MFPSBCXYTW",# agent/{AGENT_ID}/{ALIAS_ID}
    messages=[
{
"role":"user",
"content":"Hi, I need help with analyzing our Q3 sales data and generating a summary report"
}
],
)

print(response.choices[0].message.content)
print(f"Response cost: ${response._hidden_params['response_cost']}")
```

Streaming Agent Responses

```
import litellm

# Stream responses from your Bedrock Agent
response = litellm.completion(
    model="bedrock/agent/L1RT58GYRW/MFPSBCXYTW",
    messages=[
{
"role":"user",
"content":"Can you help me plan a marketing campaign and provide step-by-step execution details?"
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
-model_name: bedrock-agent-1
litellm_params:
model: bedrock/agent/L1RT58GYRW/MFPSBCXYTW
aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID
aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
aws_region_name: us-west-2

-model_name: bedrock-agent-2
litellm_params:
model: bedrock/agent/AGENT456/ALIAS789
aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID
aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
aws_region_name: us-east-1
```

#### 2. Start the LiteLLM Proxy[​](#2-start-the-litellm-proxy "Direct link to 2. Start the LiteLLM Proxy")

Start LiteLLM Proxy

```
litellm --config config.yaml
```

#### 3. Make requests to your Bedrock Agents[​](#3-make-requests-to-your-bedrock-agents "Direct link to 3. Make requests to your Bedrock Agents")

- Curl
- OpenAI Python SDK

Basic Agent Request

```
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "model": "bedrock-agent-1",
    "messages": [
      {
        "role": "user", 
        "content": "Analyze our customer data and suggest retention strategies"
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
    "model": "bedrock-agent-2",
    "messages": [
      {
        "role": "user",
        "content": "Create a comprehensive social media strategy for our new product"
      }
    ],
    "stream": true
  }'
```

## Provider-specific Parameters[​](#provider-specific-parameters "Direct link to Provider-specific Parameters")

Any non-openai parameters will be passed to the agent as custom parameters.

- SDK
- Proxy

Using custom parameters

```
from litellm import completion

response = litellm.completion(
    model="bedrock/agent/L1RT58GYRW/MFPSBCXYTW",
    messages=[
{
"role":"user",
"content":"Hi who is ishaan cto of litellm, tell me 10 things about him",
}
],
    invocationId="my-test-invocation-id",# PROVIDER-SPECIFIC VALUE
)
```

## Further Reading[​](#further-reading "Direct link to Further Reading")

- [AWS Bedrock Agents Documentation](https://aws.amazon.com/bedrock/agents/)
- [LiteLLM Authentication to Bedrock](https://docs.litellm.ai/docs/providers/bedrock#boto3---authentication)