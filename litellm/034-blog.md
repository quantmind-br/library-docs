---
title: Blog | liteLLM
url: https://docs.litellm.ai/blog
source: sitemap
fetched_at: 2026-01-21T19:40:44.710623463-03:00
rendered_js: false
word_count: 1469
summary: This document provides instructions and best practices for using Gemini 3 Pro Preview with LiteLLM, specifically addressing thought signatures, multi-turn function calling, and model switching compatibility.
tags:
    - litellm
    - gemini-3
    - google-gemini
    - function-calling
    - thought-signatures
    - python-sdk
    - llm-proxy
category: guide
---

info

This guide covers common questions and best practices for using `gemini-3-pro-preview` with LiteLLM Proxy and SDK.

## Quick Start[​](#quick-start "Direct link to Quick Start")

- Python SDK
- LiteLLM Proxy

```
from litellm import completion
import os

os.environ["GEMINI_API_KEY"]="your-api-key"

response = completion(
    model="gemini/gemini-3-pro-preview",
    messages=[{"role":"user","content":"Hello!"}],
    reasoning_effort="low"
)

print(response.choices[0].message.content)
```

## Supported Endpoints[​](#supported-endpoints "Direct link to Supported Endpoints")

LiteLLM provides **full end-to-end support** for Gemini 3 Pro Preview on:

- ✅ `/v1/chat/completions` - OpenAI-compatible chat completions endpoint
- ✅ `/v1/responses` - OpenAI Responses API endpoint (streaming and non-streaming)
- ✅ [`/v1/messages`](https://docs.litellm.ai/docs/anthropic_unified) - Anthropic-compatible messages endpoint
- ✅ `/v1/generateContent` – [Google Gemini API](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini#rest) compatible endpoint (for code, see: `client.models.generate_content(...)`)

All endpoints support:

- Streaming and non-streaming responses
- Function calling with thought signatures
- Multi-turn conversations
- All Gemini 3-specific features

## Thought Signatures[​](#thought-signatures "Direct link to Thought Signatures")

#### What are Thought Signatures?[​](#what-are-thought-signatures "Direct link to What are Thought Signatures?")

Thought signatures are encrypted representations of the model's internal reasoning process. They're essential for maintaining context across multi-turn conversations, especially with function calling.

#### How Thought Signatures Work[​](#how-thought-signatures-work "Direct link to How Thought Signatures Work")

1. **Automatic Extraction**: When Gemini 3 returns a function call, LiteLLM automatically extracts the `thought_signature` from the response
2. **Storage**: Thought signatures are stored in `provider_specific_fields.thought_signature` of tool calls
3. **Automatic Preservation**: When you include the assistant's message in conversation history, LiteLLM automatically preserves and returns thought signatures to Gemini

## Example: Multi-Turn Function Calling[​](#example-multi-turn-function-calling "Direct link to Example: Multi-Turn Function Calling")

#### Streaming with Thought Signatures[​](#streaming-with-thought-signatures "Direct link to Streaming with Thought Signatures")

When using streaming mode with `stream_chunk_builder()`, thought signatures are now automatically preserved:

- Streaming SDK
- Non-Streaming SDK
- cURL

```
import os
import litellm
from litellm import completion

os.environ["GEMINI_API_KEY"]="your-api-key"

MODEL ="gemini/gemini-3-pro-preview"

messages =[
{"role":"system","content":"You are a helpful assistant. Use the calculate tool."},
{"role":"user","content":"What is 2+2?"},
]

tools =[{
"type":"function",
"function":{
"name":"calculate",
"description":"Calculate a mathematical expression",
"parameters":{
"type":"object",
"properties":{"expression":{"type":"string"}},
"required":["expression"],
},
},
}]

print("Step 1: Sending request with stream=True...")
response = completion(
    model=MODEL,
    messages=messages,
    stream=True,
    tools=tools,
    reasoning_effort="low"
)

# Collect all chunks
chunks =[]
for part in response:
    chunks.append(part)

# Reconstruct message using stream_chunk_builder
# Thought signatures are now preserved automatically!
full_response = litellm.stream_chunk_builder(chunks, messages=messages)
print(f"Full response: {full_response}")

assistant_msg = full_response.choices[0].message

# ✅ Thought signature is now preserved in provider_specific_fields
if assistant_msg.tool_calls and assistant_msg.tool_calls[0].provider_specific_fields:
    thought_sig = assistant_msg.tool_calls[0].provider_specific_fields.get("thought_signature")
print(f"Thought signature preserved: {thought_sig isnotNone}")

# Append assistant message (includes thought signatures automatically)
messages.append(assistant_msg)

# Mock tool execution
messages.append({
"role":"tool",
"content":"4",
"tool_call_id": assistant_msg.tool_calls[0].id
})

print("\nStep 2: Sending tool result back to model...")
response_2 = completion(
    model=MODEL,
    messages=messages,
    stream=True,
    tools=tools,
    reasoning_effort="low"
)

for part in response_2:
if part.choices[0].delta.content:
print(part.choices[0].delta.content, end="")
print()# New line
```

**Key Points:**

- ✅ `stream_chunk_builder()` now preserves `provider_specific_fields` including thought signatures
- ✅ Thought signatures are automatically included when appending `assistant_msg` to conversation history
- ✅ Multi-turn conversations work seamlessly with streaming

#### Important Notes on Thought Signatures[​](#important-notes-on-thought-signatures "Direct link to Important Notes on Thought Signatures")

1. **Automatic Handling**: LiteLLM automatically extracts and preserves thought signatures. You don't need to manually manage them.
2. **Parallel Function Calls**: When the model makes parallel function calls, only the **first function call** has a thought signature.
3. **Sequential Function Calls**: In multi-step function calling, each step's first function call has its own thought signature that must be preserved.
4. **Required for Context**: Thought signatures are essential for maintaining reasoning context. Without them, the model may lose context of its previous reasoning.

## Conversation History: Switching from Non-Gemini-3 Models[​](#conversation-history-switching-from-non-gemini-3-models "Direct link to Conversation History: Switching from Non-Gemini-3 Models")

#### Common Question: Will switching from a non-Gemini-3 model to Gemini-3 break conversation history?[​](#common-question-will-switching-from-a-non-gemini-3-model-to-gemini-3-break-conversation-history "Direct link to Common Question: Will switching from a non-Gemini-3 model to Gemini-3 break conversation history?")

**Answer: No!** LiteLLM automatically handles this by adding dummy thought signatures when needed.

#### How It Works[​](#how-it-works "Direct link to How It Works")

When you switch from a model that doesn't use thought signatures (e.g., `gemini-2.5-flash`) to Gemini 3, LiteLLM:

1. **Detects missing signatures**: Identifies assistant messages with tool calls that lack thought signatures
2. **Adds dummy signature**: Automatically injects a dummy thought signature (`skip_thought_signature_validator`) for compatibility
3. **Maintains conversation flow**: Your conversation history continues to work seamlessly

#### Example: Switching Models Mid-Conversation[​](#example-switching-models-mid-conversation "Direct link to Example: Switching Models Mid-Conversation")

- Python SDK
- cURL

```
from openai import OpenAI

client = OpenAI(api_key="sk-1234", base_url="http://localhost:4000")

# Step 1: Start with gemini-2.5-flash (no thought signatures)
messages =[{"role":"user","content":"What's the weather?"}]

response1 = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=messages,
    tools=[...],
    reasoning_effort="low"
)

# Append assistant message (no tool call thought signature from gemini-2.5-flash)
messages.append(response1.choices[0].message)

# Step 2: Switch to gemini-3-pro-preview
# LiteLLM automatically adds dummy thought signature to the previous assistant message
response2 = client.chat.completions.create(
    model="gemini-3-pro-preview",# 👈 Switched model
    messages=messages,# 👈 Same conversation history
    tools=[...],
    reasoning_effort="low"
)

# ✅ Works seamlessly! No errors, no breaking changes
print(response2.choices[0].message.content)
```

#### Dummy Signature Details[​](#dummy-signature-details "Direct link to Dummy Signature Details")

The dummy signature used is: `base64("skip_thought_signature_validator")`

This is the recommended approach by Google for handling conversation history from models that don't support thought signatures. It allows Gemini 3 to:

- Accept the conversation history without validation errors
- Continue the conversation seamlessly
- Maintain context across model switches

## Thinking Level Parameter[​](#thinking-level-parameter "Direct link to Thinking Level Parameter")

#### How `reasoning_effort` Maps to `thinking_level`[​](#how-reasoning_effort-maps-to-thinking_level "Direct link to how-reasoning_effort-maps-to-thinking_level")

For Gemini 3 Pro Preview, LiteLLM automatically maps `reasoning_effort` to the new `thinking_level` parameter:

`reasoning_effort``thinking_level`Notes`"minimal"``"low"`Maps to low thinking level`"low"``"low"`Default for most use cases`"medium"``"high"`Medium not available yet, maps to high`"high"``"high"`Maximum reasoning depth`"disable"``"low"`Gemini 3 cannot fully disable thinking`"none"``"low"`Gemini 3 cannot fully disable thinking

#### Default Behavior[​](#default-behavior "Direct link to Default Behavior")

If you don't specify `reasoning_effort`, LiteLLM automatically sets `thinking_level="low"` for Gemini 3 models, to avoid high costs.

### Example Usage[​](#example-usage "Direct link to Example Usage")

- Python SDK
- LiteLLM Proxy

```
from litellm import completion

# Low thinking level (faster, lower cost)
response = completion(
    model="gemini/gemini-3-pro-preview",
    messages=[{"role":"user","content":"What's the weather?"}],
    reasoning_effort="low"# Maps to thinking_level="low"
)

# High thinking level (deeper reasoning, higher cost)
response = completion(
    model="gemini/gemini-3-pro-preview",
    messages=[{"role":"user","content":"Solve this complex math problem step by step."}],
    reasoning_effort="high"# Maps to thinking_level="high"
)
```

## Important Notes[​](#important-notes "Direct link to Important Notes")

1. **Gemini 3 Cannot Disable Thinking**: Unlike Gemini 2.5 models, Gemini 3 cannot fully disable thinking. Even when you set `reasoning_effort="none"` or `"disable"`, it maps to `thinking_level="low"`.
2. **Temperature Recommendation**: For Gemini 3 models, LiteLLM defaults `temperature` to `1.0` and strongly recommends keeping it at this default. Setting `temperature < 1.0` can cause:
   
   - Infinite loops
   - Degraded reasoning performance
   - Failure on complex tasks
3. **Automatic Defaults**: If you don't specify `reasoning_effort`, LiteLLM automatically sets `thinking_level="low"` for optimal performance.

## Cost Tracking: Prompt Caching & Context Window[​](#cost-tracking-prompt-caching--context-window "Direct link to Cost Tracking: Prompt Caching & Context Window")

LiteLLM provides comprehensive cost tracking for Gemini 3 Pro Preview, including support for prompt caching and tiered pricing based on context window size.

### Prompt Caching Cost Tracking[​](#prompt-caching-cost-tracking "Direct link to Prompt Caching Cost Tracking")

Gemini 3 supports prompt caching, which allows you to cache frequently used prompt prefixes to reduce costs. LiteLLM automatically tracks and calculates costs for:

- **Cache Hit Tokens**: Tokens that are read from cache (charged at a lower rate)
- **Cache Creation Tokens**: Tokens that are written to cache (one-time cost)
- **Text Tokens**: Regular prompt tokens that are processed normally

#### How It Works[​](#how-it-works-1 "Direct link to How It Works")

LiteLLM extracts caching information from the `prompt_tokens_details` field in the usage object:

```
{
"usage":{
"prompt_tokens":50000,
"completion_tokens":1000,
"total_tokens":51000,
"prompt_tokens_details":{
"cached_tokens":30000,# Cache hit tokens
"cache_creation_tokens":5000,# Tokens written to cache
"text_tokens":15000# Regular processed tokens
}
}
}
```

### Context Window Tiered Pricing[​](#context-window-tiered-pricing "Direct link to Context Window Tiered Pricing")

Gemini 3 Pro Preview supports up to 1M tokens of context, with tiered pricing that automatically applies when your prompt exceeds 200k tokens.

#### Automatic Tier Detection[​](#automatic-tier-detection "Direct link to Automatic Tier Detection")

LiteLLM automatically detects when your prompt exceeds the 200k token threshold and applies the appropriate tiered pricing:

```
from litellm import completion_cost

# Example: Small prompt (< 200k tokens)
response_small = completion(
    model="gemini/gemini-3-pro-preview",
    messages=[{"role":"user","content":"Hello!"}]
)
# Uses base pricing: $0.000002/input token, $0.000012/output token

# Example: Large prompt (> 200k tokens)
response_large = completion(
    model="gemini/gemini-3-pro-preview",
    messages=[{"role":"user","content":"..."*250000}]# 250k tokens
)
# Automatically uses tiered pricing: $0.000004/input token, $0.000018/output token
```

#### Cost Breakdown[​](#cost-breakdown "Direct link to Cost Breakdown")

The cost calculation includes:

1. **Text Processing Cost**: Regular tokens processed at base or tiered rate
2. **Cache Read Cost**: Cached tokens read at discounted rate
3. **Cache Creation Cost**: One-time cost for writing tokens to cache (applies tiered rate if above 200k)
4. **Output Cost**: Generated tokens at base or tiered rate

### Example: Viewing Cost Breakdown[​](#example-viewing-cost-breakdown "Direct link to Example: Viewing Cost Breakdown")

You can view the detailed cost breakdown using LiteLLM's cost tracking:

```
from litellm import completion, completion_cost

response = completion(
    model="gemini/gemini-3-pro-preview",
    messages=[{"role":"user","content":"Explain prompt caching"}],
    caching=True# Enable prompt caching
)

# Get total cost
total_cost = completion_cost(completion_response=response)
print(f"Total cost: ${total_cost:.6f}")

# Access usage details
usage = response.usage
print(f"Prompt tokens: {usage.prompt_tokens}")
print(f"Completion tokens: {usage.completion_tokens}")

# Access caching details
if usage.prompt_tokens_details:
print(f"Cache hit tokens: {usage.prompt_tokens_details.cached_tokens}")
print(f"Cache creation tokens: {usage.prompt_tokens_details.cache_creation_tokens}")
print(f"Text tokens: {usage.prompt_tokens_details.text_tokens}")
```

### Cost Optimization Tips[​](#cost-optimization-tips "Direct link to Cost Optimization Tips")

1. **Use Prompt Caching**: For repeated prompt prefixes, enable caching to reduce costs by up to 90% for cached portions
2. **Monitor Context Size**: Be aware that prompts above 200k tokens use tiered pricing (2x for input, 1.5x for output)
3. **Cache Management**: Cache creation tokens are charged once when writing to cache, then subsequent reads are much cheaper
4. **Track Usage**: Use LiteLLM's built-in cost tracking to monitor spending across different token types

### Integration with LiteLLM Proxy[​](#integration-with-litellm-proxy "Direct link to Integration with LiteLLM Proxy")

When using LiteLLM Proxy, all cost tracking is automatically logged and available through:

- **Usage Logs**: Detailed token and cost breakdowns in proxy logs
- **Budget Management**: Set budgets and alerts based on actual usage
- **Analytics Dashboard**: View cost trends and breakdowns by token type

```
# config.yaml
model_list:
-model_name: gemini-3-pro-preview
litellm_params:
model: gemini/gemini-3-pro-preview
api_key: os.environ/GEMINI_API_KEY

litellm_settings:
# Enable detailed cost tracking
success_callback:["langfuse"]# or your preferred logging service
```

## Using with Claude Code CLI[​](#using-with-claude-code-cli "Direct link to Using with Claude Code CLI")

You can use `gemini-3-pro-preview` with **Claude Code CLI** - Anthropic's command-line interface. This allows you to use Gemini 3 Pro Preview with Claude Code's native syntax and workflows.

### Setup[​](#setup "Direct link to Setup")

**1. Add Gemini 3 Pro Preview to your `config.yaml`:**

```
model_list:
-model_name: gemini-3-pro-preview
litellm_params:
model: gemini/gemini-3-pro-preview
api_key: os.environ/GEMINI_API_KEY

litellm_settings:
master_key: os.environ/LITELLM_MASTER_KEY
```

**2. Set environment variables:**

```
export GEMINI_API_KEY="your-gemini-api-key"
export LITELLM_MASTER_KEY="sk-1234567890"  # Generate a secure key
```

**3. Start LiteLLM Proxy:**

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

**4. Configure Claude Code to use LiteLLM Proxy:**

```
export ANTHROPIC_BASE_URL="http://0.0.0.0:4000"
export ANTHROPIC_AUTH_TOKEN="$LITELLM_MASTER_KEY"
```

**5. Use Gemini 3 Pro Preview with Claude Code:**

```
# Claude Code will use gemini-3-pro-preview from your LiteLLM proxy
claude --model gemini-3-pro-preview

```

### Example Usage[​](#example-usage-1 "Direct link to Example Usage")

Once configured, you can interact with Gemini 3 Pro Preview using Claude Code's native interface:

```
$ claude --model gemini-3-pro-preview
> Explain how thought signatures work in multi-turn conversations.

# Gemini 3 Pro Preview responds through Claude Code interface
```

### Benefits[​](#benefits "Direct link to Benefits")

- ✅ **Native Claude Code Experience**: Use Gemini 3 Pro Preview with Claude Code's familiar CLI interface
- ✅ **Unified Authentication**: Single API key for all models through LiteLLM proxy
- ✅ **Cost Tracking**: All usage tracked through LiteLLM's centralized logging
- ✅ **Seamless Model Switching**: Easily switch between Claude and Gemini models
- ✅ **Full Feature Support**: All Gemini 3 features (thought signatures, function calling, etc.) work through Claude Code

### Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

**Claude Code not finding the model:**

- Ensure the model name in Claude Code matches exactly: `gemini-3-pro-preview`
- Verify your proxy is running: `curl http://0.0.0.0:4000/health`
- Check that `ANTHROPIC_BASE_URL` points to your LiteLLM proxy

**Authentication errors:**

- Verify `ANTHROPIC_AUTH_TOKEN` matches your LiteLLM master key
- Ensure `GEMINI_API_KEY` is set correctly
- Check LiteLLM proxy logs for detailed error messages

## Responses API Support[​](#responses-api-support "Direct link to Responses API Support")

LiteLLM fully supports the OpenAI Responses API for Gemini 3 Pro Preview, including both streaming and non-streaming modes. The Responses API provides a structured way to handle multi-turn conversations with function calling, and LiteLLM automatically preserves thought signatures throughout the conversation.

### Example: Using Responses API with Gemini 3[​](#example-using-responses-api-with-gemini-3 "Direct link to Example: Using Responses API with Gemini 3")

- Non-Streaming
- Streaming

```
from openai import OpenAI
import json

client = OpenAI()

# 1. Define a list of callable tools for the model
tools =[
{
"type":"function",
"name":"get_horoscope",
"description":"Get today's horoscope for an astrological sign.",
"parameters":{
"type":"object",
"properties":{
"sign":{
"type":"string",
"description":"An astrological sign like Taurus or Aquarius",
},
},
"required":["sign"],
},
},
]

defget_horoscope(sign):
returnf"{sign}: Next Tuesday you will befriend a baby otter."

# Create a running input list we will add to over time
input_list =[
{"role":"user","content":"What is my horoscope? I am an Aquarius."}
]

# 2. Prompt the model with tools defined
response = client.responses.create(
    model="gemini-3-pro-preview",
    tools=tools,
input=input_list,
)

# Save function call outputs for subsequent requests
input_list += response.output

for item in response.output:
if item.type=="function_call":
if item.name =="get_horoscope":
# 3. Execute the function logic for get_horoscope
            horoscope = get_horoscope(json.loads(item.arguments))

# 4. Provide function call results to the model
            input_list.append({
"type":"function_call_output",
"call_id": item.call_id,
"output": json.dumps({
"horoscope": horoscope
})
})

print("Final input:")
print(input_list)

response = client.responses.create(
    model="gemini-3-pro-preview",
    instructions="Respond only with a horoscope generated by a tool.",
    tools=tools,
input=input_list,
)

# 5. The model should be able to give a response!
print("Final output:")
print(response.model_dump_json(indent=2))
print("\n"+ response.output_text)
```

**Key Points:**

- ✅ Thought signatures are automatically preserved in function calls
- ✅ Works seamlessly with multi-turn conversations
- ✅ All Gemini 3-specific features are fully supported

### Responses API Benefits[​](#responses-api-benefits "Direct link to Responses API Benefits")

- ✅ **Structured Output**: Responses API provides a clear structure for handling function calls and multi-turn conversations
- ✅ **Thought Signature Preservation**: LiteLLM automatically preserves thought signatures in both streaming and non-streaming modes
- ✅ **Seamless Integration**: Works with existing OpenAI SDK patterns
- ✅ **Full Feature Support**: All Gemini 3 features (thought signatures, function calling, reasoning) are fully supported

## Best Practices[​](#best-practices "Direct link to Best Practices")

#### 1. Always Include Thought Signatures in Conversation History[​](#1-always-include-thought-signatures-in-conversation-history "Direct link to 1. Always Include Thought Signatures in Conversation History")

When building multi-turn conversations with function calling:

✅ **Do:**

```
# Append the full assistant message (includes thought signatures)
messages.append(response.choices[0].message)
```

❌ **Don't:**

```
# Don't manually construct assistant messages without thought signatures
messages.append({
"role":"assistant",
"tool_calls":[...]# Missing thought signatures!
})
```

#### 2. Use Appropriate Thinking Levels[​](#2-use-appropriate-thinking-levels "Direct link to 2. Use Appropriate Thinking Levels")

- **`reasoning_effort="low"`** : For simple queries, quick responses, cost optimization
- **`reasoning_effort="high"`** : For complex problems requiring deep reasoning

#### 3. Keep Temperature at Default[​](#3-keep-temperature-at-default "Direct link to 3. Keep Temperature at Default")

For Gemini 3 models, always use `temperature=1.0` (default). Lower temperatures can cause issues.

#### 4. Handle Model Switches Gracefully[​](#4-handle-model-switches-gracefully "Direct link to 4. Handle Model Switches Gracefully")

When switching from non-Gemini-3 to Gemini-3:

- ✅ LiteLLM automatically handles missing thought signatures
- ✅ No manual intervention needed
- ✅ Conversation history continues seamlessly

## Troubleshooting[​](#troubleshooting-1 "Direct link to Troubleshooting")

#### Issue: Missing Thought Signatures[​](#issue-missing-thought-signatures "Direct link to Issue: Missing Thought Signatures")

**Symptom**: Error when including assistant messages in conversation history

**Solution**: Ensure you're appending the full assistant message from the response:

```
messages.append(response.choices[0].message)# ✅ Includes thought signatures
```

#### Issue: Conversation Breaks When Switching Models[​](#issue-conversation-breaks-when-switching-models "Direct link to Issue: Conversation Breaks When Switching Models")

**Symptom**: Errors when switching from gemini-2.5-flash to gemini-3-pro-preview

**Solution**: This should work automatically! LiteLLM adds dummy signatures. If you see errors, ensure you're using the latest LiteLLM version.

#### Issue: Infinite Loops or Poor Performance[​](#issue-infinite-loops-or-poor-performance "Direct link to Issue: Infinite Loops or Poor Performance")

**Symptom**: Model gets stuck or produces poor results

**Solution**:

- Ensure `temperature=1.0` (default for Gemini 3)
- Check that `reasoning_effort` is set appropriately
- Verify you're using the correct model name: `gemini/gemini-3-pro-preview`

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Gemini Provider Documentation](https://docs.litellm.ai/gemini.md)
- [Thought Signatures Guide](https://docs.litellm.ai/gemini.md#thought-signatures)
- [Reasoning Content Documentation](https://docs.litellm.ai/reasoning_content.md)
- [Function Calling Guide](https://docs.litellm.ai/function_calling.md)