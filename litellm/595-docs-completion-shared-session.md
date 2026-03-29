---
title: Shared Session Support | liteLLM
url: https://docs.litellm.ai/docs/completion/shared_session
source: sitemap
fetched_at: 2026-01-21T19:44:44.566255837-03:00
rendered_js: false
word_count: 266
summary: This document explains how to share aiohttp.ClientSession instances in LiteLLM to optimize performance and resource utilization by reusing HTTP connections across multiple API calls.
tags:
    - litellm
    - aiohttp
    - client-session
    - performance-optimization
    - async-io
    - connection-pooling
category: guide
---

## Overview[​](#overview "Direct link to Overview")

LiteLLM now supports sharing `aiohttp.ClientSession` instances across multiple API calls to avoid creating unnecessary new sessions. This improves performance and resource utilization.

## Usage[​](#usage "Direct link to Usage")

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

```
import asyncio
from aiohttp import ClientSession
from litellm import acompletion

asyncdefmain():
# Create a shared session
asyncwith ClientSession()as shared_session:
# Use the same session for multiple calls
        response1 =await acompletion(
            model="gpt-4o",
            messages=[{"role":"user","content":"Hello"}],
            shared_session=shared_session
)

        response2 =await acompletion(
            model="gpt-4o",
            messages=[{"role":"user","content":"How are you?"}],
            shared_session=shared_session
)

# Both calls reuse the same session!

asyncio.run(main())
```

### Without Shared Session (Default)[​](#without-shared-session-default "Direct link to Without Shared Session (Default)")

```
import asyncio
from litellm import acompletion

asyncdefmain():
# Each call creates a new session
    response1 =await acompletion(
        model="gpt-4o",
        messages=[{"role":"user","content":"Hello"}]
)

    response2 =await acompletion(
        model="gpt-4o",
        messages=[{"role":"user","content":"How are you?"}]
)
# Two separate sessions created

asyncio.run(main())
```

## Benefits[​](#benefits "Direct link to Benefits")

- **Performance**: Reuse HTTP connections across multiple calls
- **Resource Efficiency**: Reduce memory and connection overhead
- **Better Control**: Manage session lifecycle explicitly
- **Debugging**: Easy to trace which calls use which sessions

## Debug Logging[​](#debug-logging "Direct link to Debug Logging")

Enable debug logging to see session reuse in action:

```
import os
import litellm

# Enable debug logging
os.environ['LITELLM_LOG']='DEBUG'

# You'll see logs like:
# 🔄 SHARED SESSION: acompletion called with shared_session (ID: 12345)
# ✅ SHARED SESSION: Reusing existing ClientSession (ID: 12345)
```

## Common Patterns[​](#common-patterns "Direct link to Common Patterns")

### FastAPI Integration[​](#fastapi-integration "Direct link to FastAPI Integration")

```
from fastapi import FastAPI
import aiohttp
import litellm

app = FastAPI()

@app.post("/chat")
asyncdefchat(messages:list[dict]):
# Create session per request
asyncwith aiohttp.ClientSession()as session:
returnawait litellm.acompletion(
            model="gpt-4o",
            messages=messages,
            shared_session=session
)
```

### Batch Processing[​](#batch-processing "Direct link to Batch Processing")

```
import asyncio
from aiohttp import ClientSession
from litellm import acompletion

asyncdefprocess_batch(messages_list):
asyncwith ClientSession()as shared_session:
        tasks =[]
for messages in messages_list:
            task = acompletion(
                model="gpt-4o",
                messages=messages,
                shared_session=shared_session
)
            tasks.append(task)

# All tasks use the same session
        results =await asyncio.gather(*tasks)
return results
```

### Custom Session Configuration[​](#custom-session-configuration "Direct link to Custom Session Configuration")

```
import aiohttp
import litellm

# Create optimized session
asyncwith aiohttp.ClientSession(
    timeout=aiohttp.ClientTimeout(total=180),
    connector=aiohttp.TCPConnector(limit=300, limit_per_host=75)
)as shared_session:

    response =await litellm.acompletion(
        model="gpt-4o",
        messages=[{"role":"user","content":"Hello"}],
        shared_session=shared_session
)
```

## Implementation Details[​](#implementation-details "Direct link to Implementation Details")

The `shared_session` parameter is threaded through the entire LiteLLM call chain:

1. **`acompletion()`** - Accepts `shared_session` parameter
2. **`BaseLLMHTTPHandler`** - Passes session to HTTP client creation
3. **`AsyncHTTPHandler`** - Uses existing session if provided
4. **`LiteLLMAiohttpTransport`** - Reuses the session for HTTP requests

## Backward Compatibility[​](#backward-compatibility "Direct link to Backward Compatibility")

- **100% backward compatible** - Existing code works unchanged
- **Optional parameter** - `shared_session=None` by default
- **No breaking changes** - All existing functionality preserved

## Testing[​](#testing "Direct link to Testing")

Test the shared session functionality:

```
import asyncio
from aiohttp import ClientSession
from litellm import acompletion

asyncdeftest_shared_session():
asyncwith ClientSession()as session:
print(f"✅ Created session: {id(session)}")

try:
            response =await acompletion(
                model="gpt-4o",
                messages=[{"role":"user","content":"Hello"}],
                shared_session=session,
                api_key="your-api-key"
)
print(f"Response: {response.choices[0].message.content}")
except Exception as e:
print(f"✅ Expected error: {type(e).__name__}")

print("✅ Session control working!")

asyncio.run(test_shared_session())
```

## Files Modified[​](#files-modified "Direct link to Files Modified")

The shared session functionality was added to these files:

- `litellm/main.py` - Added `shared_session` parameter to `acompletion()` and `completion()`
- `litellm/llms/custom_httpx/http_handler.py` - Core session reuse logic
- `litellm/llms/custom_httpx/llm_http_handler.py` - HTTP handler integration
- `litellm/llms/openai/openai.py` - OpenAI provider integration
- `litellm/llms/openai/common_utils.py` - OpenAI client creation
- `litellm/llms/azure/chat/o_series_handler.py` - Azure O Series handler

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Session Not Being Reused[​](#session-not-being-reused "Direct link to Session Not Being Reused")

1. **Check debug logs**: Enable `LITELLM_LOG=DEBUG` to see session reuse messages
2. **Verify session is not closed**: Ensure the session is still active when making calls
3. **Check parameter passing**: Make sure `shared_session` is passed to all `acompletion()` calls

### Performance Issues[​](#performance-issues "Direct link to Performance Issues")

1. **Session configuration**: Tune `aiohttp.ClientSession` parameters for your use case
2. **Connection limits**: Adjust `limit` and `limit_per_host` in `TCPConnector`
3. **Timeout settings**: Configure appropriate timeouts for your environment