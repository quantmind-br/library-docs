---
title: Letta Integration | liteLLM
url: https://docs.litellm.ai/docs/integrations/letta
source: sitemap
fetched_at: 2026-01-21T19:45:32.527182797-03:00
rendered_js: false
word_count: 380
summary: This guide explains how to integrate the Letta framework with LiteLLM Proxy and SDK to build memory-enabled, stateful AI agents. It covers model configuration, agent creation, and advanced features like load balancing and tool use across different LLM providers.
tags:
    - letta
    - litellm
    - ai-agents
    - persistent-memory
    - llm-proxy
    - model-integration
category: guide
---

[Letta](https://github.com/letta-ai/letta) (formerly MemGPT) is a framework for building stateful LLM agents with persistent memory. This guide shows how to integrate both LiteLLM SDK and LiteLLM Proxy with Letta to leverage multiple LLM providers while building memory-enabled agents.

## What is Letta?[​](#what-is-letta "Direct link to What is Letta?")

Letta allows you to build LLM agents that can:

- Maintain long-term memory across conversations
- Use function calling for tool interactions
- Handle large context windows efficiently
- Persist agent state and memory

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

```
pip install letta litellm
```

## Quick Start[​](#quick-start "Direct link to Quick Start")

- LiteLLM Proxy
- LiteLLM SDK

### 1. Start LiteLLM Proxy[​](#1-start-litellm-proxy "Direct link to 1. Start LiteLLM Proxy")

First, create a configuration file for your LiteLLM proxy:

```
# config.yaml
model_list:
-model_name: gpt-4
litellm_params:
model: openai/gpt-4
api_key: os.environ/OPENAI_API_KEY

-model_name: claude-3-sonnet
litellm_params:
model: anthropic/claude-3-sonnet-20240229
api_key: os.environ/ANTHROPIC_API_KEY

-model_name: gpt-3.5-turbo
litellm_params:
model: azure/gpt-35-turbo
api_key: os.environ/AZURE_API_KEY
api_base: os.environ/AZURE_API_BASE
api_version:"2023-07-01-preview"
```

Start the proxy:

```
litellm --config config.yaml --port 4000
```

### 2. Configure Letta with LiteLLM Proxy[​](#2-configure-letta-with-litellm-proxy "Direct link to 2. Configure Letta with LiteLLM Proxy")

Configure Letta to use your LiteLLM proxy endpoint:

```
import letta
from letta import create_client

# Configure Letta to use LiteLLM proxy
client = create_client()

# Configure the LLM endpoint
client.set_default_llm_config(
    model="gpt-4",# This should match a model from your LiteLLM config
    model_endpoint_type="openai",
    model_endpoint="http://localhost:4000",# Your LiteLLM proxy URL
    context_window=8192
)

# Configure embedding endpoint (optional)
client.set_default_embedding_config(
    embedding_endpoint_type="openai",
    embedding_endpoint="http://localhost:4000",
    embedding_model="text-embedding-ada-002"
)
```

### 3. Create and Use a Letta Agent[​](#3-create-and-use-a-letta-agent "Direct link to 3. Create and Use a Letta Agent")

- Using LiteLLM Proxy
- Using LiteLLM SDK

```
import letta
from letta import create_client

# Create Letta client
client = create_client()

# Create a new agent
agent_state = client.create_agent(
    name="my-assistant",
    system="You are a helpful assistant with persistent memory.",
    llm_config=client.get_default_llm_config(),
    embedding_config=client.get_default_embedding_config()
)

# Send a message to the agent
response = client.user_message(
    agent_id=agent_state.id,
    message="Hi! My name is Alice and I love reading science fiction books."
)

print(f"Agent response: {response.messages[-1].text}")

# Send another message - the agent will remember previous context
response = client.user_message(
    agent_id=agent_state.id,
    message="What did I tell you about my interests?"
)

print(f"Agent response: {response.messages[-1].text}")
```

## Advanced Configuration[​](#advanced-configuration "Direct link to Advanced Configuration")

### Using Different Models for Different Agents[​](#using-different-models-for-different-agents "Direct link to Using Different Models for Different Agents")

- LiteLLM Proxy
- LiteLLM SDK

```
from letta import LLMConfig, EmbeddingConfig

# Create different LLM configurations pointing to your proxy
gpt4_config = LLMConfig(
    model="gpt-4",
    model_endpoint_type="openai",
    model_endpoint="http://localhost:4000",
    context_window=8192
)

claude_config = LLMConfig(
    model="claude-3-sonnet",
    model_endpoint_type="openai",# Using OpenAI-compatible endpoint
    model_endpoint="http://localhost:4000",
    context_window=200000
)

# Create agents with different configurations
research_agent = client.create_agent(
    name="research-agent",
    system="You are a research assistant specialized in analysis.",
    llm_config=claude_config  # Use Claude for research tasks
)

creative_agent = client.create_agent(
    name="creative-agent",
    system="You are a creative writing assistant.",
    llm_config=gpt4_config  # Use GPT-4 for creative tasks
)
```

### Function Calling with Tools[​](#function-calling-with-tools "Direct link to Function Calling with Tools")

- LiteLLM Proxy
- LiteLLM SDK

```
# Define custom tools for your agent
defsearch_web(query:str)->str:
"""Search the web for information"""
# Your web search implementation
returnf"Search results for: {query}"

defsave_note(content:str)->str:
"""Save a note to persistent storage"""
# Your note saving implementation
returnf"Note saved: {content}"

# Create agent with tools (using proxy endpoint)
agent_state = client.create_agent(
    name="research-assistant",
    system="You are a research assistant that can search the web and save notes.",
    llm_config=client.get_default_llm_config(),
    embedding_config=client.get_default_embedding_config(),
    tools=[search_web, save_note]
)

# The agent can now use these tools
response = client.user_message(
    agent_id=agent_state.id,
    message="Search for recent developments in AI and save important findings."
)
```

## Authentication[​](#authentication "Direct link to Authentication")

- LiteLLM Proxy Authentication
- LiteLLM SDK Authentication

If your LiteLLM proxy requires authentication:

```
import os
from letta import LLMConfig

# Set up authenticated configuration
llm_config = LLMConfig(
    model="gpt-4",
    model_endpoint_type="openai",
    model_endpoint="http://localhost:4000",
    model_wrapper="openai",
    context_window=8192
)

# If using API keys with your proxy
os.environ["OPENAI_API_KEY"]="your-litellm-proxy-api-key"

client = create_client()
client.set_default_llm_config(llm_config)
```

For proxy with authentication enabled:

```
# config.yaml with auth
general_settings:
master_key:"your-master-key"

model_list:
-model_name: gpt-4
litellm_params:
model: openai/gpt-4
api_key: os.environ/OPENAI_API_KEY
```

```
# Configure Letta with authenticated proxy
llm_config = LLMConfig(
    model="gpt-4",
    model_endpoint_type="openai",
    model_endpoint="http://localhost:4000",
    context_window=8192,
    api_key="your-master-key"# Proxy master key
)
```

## Load Balancing and Fallbacks[​](#load-balancing-and-fallbacks "Direct link to Load Balancing and Fallbacks")

- LiteLLM Proxy Features
- LiteLLM SDK Router

LiteLLM proxy's load balancing and fallback features work seamlessly with Letta:

```
# config.yaml with fallbacks
model_list:
-model_name: gpt-4
litellm_params:
model: openai/gpt-4
api_key: os.environ/OPENAI_API_KEY
tpm:40000
rpm:500

-model_name: gpt-4# Same model name for fallback
litellm_params:
model: azure/gpt-4
api_key: os.environ/AZURE_API_KEY
api_base: os.environ/AZURE_API_BASE
api_version:"2023-07-01-preview"
tpm:80000
rpm:800

router_settings:
routing_strategy:"usage-based-routing"
fallbacks:[{"gpt-4":["azure/gpt-4"]}]
```

The proxy handles all routing, load balancing, and fallbacks transparently for Letta.

## Monitoring and Observability[​](#monitoring-and-observability "Direct link to Monitoring and Observability")

- LiteLLM Proxy Monitoring
- LiteLLM SDK Monitoring

Enable logging to track your Letta agents' LLM usage through the proxy:

```
# config.yaml with logging
model_list:
# ... your models

litellm_settings:
success_callback:["langfuse"]# or other observability tools

environment_variables:
LANGFUSE_PUBLIC_KEY:"your-key"
LANGFUSE_SECRET_KEY:"your-secret"
```

View metrics in the proxy dashboard:

```
# Start proxy with UI
litellm --config config.yaml --port 4000 --detailed_debug
```

## Example: Multi-Agent System[​](#example-multi-agent-system "Direct link to Example: Multi-Agent System")

- Using LiteLLM Proxy
- Using LiteLLM SDK

```
import letta
from letta import create_client, LLMConfig

client = create_client()

# Create specialized agents using proxy endpoints
agents ={}

# Research agent using Claude for analysis
agents['researcher']= client.create_agent(
    name="researcher",
    system="You are a research specialist. Analyze information thoroughly.",
    llm_config=LLMConfig(
        model="claude-3-sonnet",
        model_endpoint="http://localhost:4000",
        model_endpoint_type="openai"
)
)

# Writer agent using GPT-4 for content creation
agents['writer']= client.create_agent(
    name="writer",
    system="You are a content writer. Create engaging, well-structured content.",
    llm_config=LLMConfig(
        model="gpt-4",
        model_endpoint="http://localhost:4000",
        model_endpoint_type="openai"
)
)

# Coordinator workflow
defresearch_and_write_workflow(topic:str):
# Research phase
    research_response = client.user_message(
        agent_id=agents['researcher'].id,
        message=f"Research the topic: {topic}. Provide key insights and data."
)

    research_results = research_response.messages[-1].text

# Writing phase
    write_response = client.user_message(
        agent_id=agents['writer'].id,
        message=f"Based on this research: {research_results}\n\nWrite an article about {topic}."
)

return write_response.messages[-1].text

# Execute workflow
article = research_and_write_workflow("The future of AI in healthcare")
print(article)
```

## Best Practices[​](#best-practices "Direct link to Best Practices")

- LiteLLM Proxy Best Practices
- LiteLLM SDK Best Practices

<!--THE END-->

1. **Model Selection**: Use appropriate models for different tasks:
   
   - Claude for analysis and reasoning
   - GPT-4 for creative tasks
   - GPT-3.5-turbo for simple interactions
2. **Proxy Configuration**:
   
   - Set appropriate rate limits and timeouts
   - Use fallbacks for reliability
   - Enable authentication for production
3. **Memory Management**: Letta handles memory automatically, but monitor usage with large contexts
4. **Cost Optimization**:
   
   - Use the proxy's budgeting features to control costs
   - Set up rate limiting per user/team
   - Monitor token usage through proxy dashboard
5. **Monitoring**: Enable observability to track agent performance and token usage

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

- LiteLLM Proxy Issues
- LiteLLM SDK Issues

### Connection Issues[​](#connection-issues "Direct link to Connection Issues")

```
# Test your LiteLLM proxy
curl -X POST http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

### Configuration Debugging[​](#configuration-debugging "Direct link to Configuration Debugging")

```
# Enable verbose logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Test Letta configuration
client = create_client()
print(client.get_default_llm_config())
```

### Common Proxy Issues[​](#common-proxy-issues "Direct link to Common Proxy Issues")

- **Port conflicts**: Make sure port 4000 isn't in use
- **Model not found**: Verify model names match your config.yaml
- **Authentication errors**: Check master key configuration
- **Rate limiting**: Monitor proxy logs for rate limit hits

## Resources[​](#resources "Direct link to Resources")

- [Letta Documentation](https://docs.letta.ai/)
- [LiteLLM Proxy Documentation](https://docs.litellm.ai/docs/proxy/quick_start)
- [LiteLLM SDK Documentation](https://docs.litellm.ai/docs/completion/input)
- [Function Calling Guide](https://docs.litellm.ai/docs/completion/function_call)
- [Observability Setup](https://docs.litellm.ai/docs/observability/langfuse_integration)
- [Router Configuration](https://docs.litellm.ai/docs/routing)