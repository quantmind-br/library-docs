---
title: Prompt caching - Fireworks AI Docs
url: https://docs.fireworks.ai/guides/prompt-caching
source: sitemap
fetched_at: 2026-04-27T20:12:45.55148478-03:00
rendered_js: false
word_count: 494
summary: This document explains the concept and practical implementation of prompt caching within Fireworks, a performance feature designed to speed up LLM responses by reusing common initial segments (prefixes) of user prompts.
tags:
    - prompt-caching
    - llm-optimization
    - inference-speed
    - fireworks-ai
    - prompt-structure
    - cache-hits
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Prompt Caching

Prompt caching is a performance optimization that allows Fireworks to respond faster to requests with shared prompt prefixes. It can reduce time to first token (TTFT) by up to 80% and is enabled by default for all Fireworks models and [[070-guides-ondemand-deployments|deployments]].

- **Serverless**: Cached prompt tokens receive a default 50% discount (varies by model — check the [Model Library](https://fireworks.ai/models) for model-specific pricing)
- **Dedicated deployments**: Cached tokens are near-free since they affect context length but do not need extra processing

## Common Use Cases

Requests to LLMs often share large portions of prompts:

- Long system prompts with detailed instructions
- Descriptions of available tools for function calling
- Growing previous conversation history
- Shared per-user context (e.g., current file for a coding assistant)

## Structuring Prompts for Caching

Prompt caching requires exact prefix matches. Place static content (instructions, examples) at the beginning and variable content (user-specific information) at the end. For function calling models, tools are considered part of the prompt.

## Optimizing Inference Requests

Prompt caching only works within 1 replica. For serverless or multi-replica deployments, pass a session identifier to maximize cache hit rates:

- `user` field in the request body
- `x-session-affinity` header

- Python
- JavaScript
- curl

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1",
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/<MODEL_ID>",
    messages=[{
        "role": "user",
        "content": "Explain quantum computing in simple terms"
    }],
    extra_headers={
        "x-session-affinity": "session-id-123"
    }
)

print(response.choices[0].message.content)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/<MODEL_ID>",
  messages: [
    {
      role: "user",
      content: "Explain quantum computing in simple terms",
    },
  ],
  extra_headers: {
    "x-session-affinity": "session-id-123"
  }
});

console.log(response.choices[0].message.content);
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "x-session-affinity: session-id-123" \
  -d '{
    "model": "accounts/fireworks/models/",
    "messages": [
      {
        "role": "user",
        "content": "Explain quantum computing in simple terms"
      }
    ]
  }'
```

## Resetting or Isolating Cache State

- **Change session key** in `user` or `x-session-affinity` to move traffic to a different sticky routing key
- **Set `x-prompt-cache-isolation-key`** header or `prompt_cache_isolation_key` field to force cache separation even with identical prompt text
- **For hot-load or weight-sync**: set `reset_prompt_cache` to `all`, `none`, or `new_session` when publishing a new snapshot

## Prompt Optimization for Maximum Cache Hits

> [!tip] Keep your prompt prefix stable
> Any change to the beginning of your prompt invalidates the entire cache chain that follows.

### Structure: Static First, Dynamic Last

```python
# ✅ Good: Static content first
system_prompt = """
You are a helpful AI assistant with expertise in software development.

Your guidelines:
- Provide clear, concise explanations
- Include practical examples when helpful
- Ask clarifying questions when requirements are unclear

Available tools:
- web_search: Search the internet for current information
- code_executor: Run code snippets safely
- file_manager: Read and write files
"""

user_message = ""
if user_context:
    user_message += f"User context: {user_context}\n\n"
if current_time_needed:
    user_message += f"Current time: {datetime.now().isoformat()}\n\n"
user_message += user_query
```

### Smart Timestamp Handling

**Option 1: Rounded timestamps**

```python
# ✅ Round to larger intervals to increase cache hits
current_hour = datetime.now().replace(minute=0, second=0, microsecond=0)
system_prompt = f"""
You are a helpful assistant.
Current hour: {current_hour.strftime('%Y-%m-%d %H:00')}
...
"""
```

**Option 2: Conditional time injection**

```python
# ✅ Only add time when the query actually needs it
def build_prompt(user_query, system_base):
    prompt = system_base
    time_keywords = ['today', 'now', 'current', 'latest', 'recent']
    if any(keyword in user_query.lower() for keyword in time_keywords):
        prompt += f"\nCurrent time: {datetime.now().isoformat()}"
    prompt += f"\nUser: {user_query}"
    return prompt
```

**Option 3: Move time to user message**

```python
# ✅ Keep system prompt static, add time context to user message
system_prompt = """You are a helpful AI assistant..."""  # Stays the same

user_message = f"""
Current time: {datetime.now().isoformat()}
User query: {user_query}
"""
```

## How It Works

Fireworks finds the longest prefix of the request present in the cache and reuses it. The remaining portion is processed normally. The entire prompt is stored for future reuse. Cached prompts typically stay in cache for several minutes up to several hours depending on model, load, and deployment config. Oldest prompts are evicted first.

> [!note] Cached prompts don't change model outputs — responses are identical to non-cached requests. Each generation is sampled independently and not cached.

## Monitoring

For dedicated deployments, response headers include `fireworks-prompt-tokens` (total prompt tokens) and `fireworks-cached-prompt-tokens` (cached portion). Aggregated metrics are in the [usage dashboard](https://fireworks.ai/account/usage?type=deployments).

## Data Privacy

- **Serverless**: Separate caches per Fireworks account prevent data leakage and timing attacks
- **Dedicated deployments**: Shared single cache by default — safe for multi-tenant apps since outputs are unchanged
- **Full isolation**: Pass `x-prompt-cache-isolation-key` header or `prompt_cache_isolation_key` field for complete cache separation

## Migration & Traffic Management

When migrating between deployments, use consistent user/session-based routing (not random) to maintain cache hit rates:

```python
import hashlib

fireworks_traffic_fraction = 0.2
user_id = "session-id-123"

# Deterministic hash for consistent routing
hashed_user_id = int(hashlib.md5(user_id.encode()).hexdigest(), 16)
MAX_HASH = 2**128 - 1
ratio = hashed_user_id / MAX_HASH

if ratio < fireworks_traffic_fraction:
    send_to_new_deployment(user=hashed_user_id)  # Pass user ID for caching
else:
    send_elsewhere()
```

#prompt-caching #llm-optimization #inference-speed #fireworks-ai #prompt-structure #cache-hits
