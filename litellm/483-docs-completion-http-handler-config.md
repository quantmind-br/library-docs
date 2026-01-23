---
title: Custom HTTP Handler | liteLLM
url: https://docs.litellm.ai/docs/completion/http_handler_config
source: sitemap
fetched_at: 2026-01-21T19:44:26.40334982-03:00
rendered_js: false
word_count: 85
summary: This document explains how to configure and inject custom aiohttp sessions into LiteLLM to optimize performance, manage connection pooling, and handle corporate proxy settings.
tags:
    - litellm
    - aiohttp
    - python
    - performance-optimization
    - async-io
    - api-configuration
    - connection-pooling
category: configuration
---

Configure custom aiohttp sessions for better performance and control in LiteLLM completions.

## Overview[​](#overview "Direct link to Overview")

You can now inject custom `aiohttp.ClientSession` instances into LiteLLM for:

- Custom connection pooling and timeouts
- Corporate proxy and SSL configurations
- Performance optimization
- Request monitoring

## Basic Usage[​](#basic-usage "Direct link to Basic Usage")

### Default (No Changes Required)[​](#default-no-changes-required "Direct link to Default (No Changes Required)")

```
import litellm

# Works exactly as before
response =await litellm.acompletion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Hello!"}]
)
```

### Custom Session[​](#custom-session "Direct link to Custom Session")

```
import aiohttp
import litellm
from litellm.llms.custom_httpx.aiohttp_handler import BaseLLMAIOHTTPHandler

# Create optimized session
session = aiohttp.ClientSession(
    timeout=aiohttp.ClientTimeout(total=180),
    connector=aiohttp.TCPConnector(limit=300, limit_per_host=75)
)

# Replace global handler
litellm.base_llm_aiohttp_handler = BaseLLMAIOHTTPHandler(client_session=session)

# All completions now use your session
response =await litellm.acompletion(model="gpt-3.5-turbo", messages=[...])
```

## Common Patterns[​](#common-patterns "Direct link to Common Patterns")

### FastAPI Integration[​](#fastapi-integration "Direct link to FastAPI Integration")

```
from contextlib import asynccontextmanager
from fastapi import FastAPI
import aiohttp
import litellm

@asynccontextmanager
asyncdeflifespan(app: FastAPI):
# Startup
    session = aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=180),
        connector=aiohttp.TCPConnector(limit=300)
)
    litellm.base_llm_aiohttp_handler = BaseLLMAIOHTTPHandler(
        client_session=session
)
yield
# Shutdown
await session.close()

app = FastAPI(lifespan=lifespan)

@app.post("/chat")
asyncdefchat(messages:list[dict]):
returnawait litellm.acompletion(model="gpt-3.5-turbo", messages=messages)
```

### Corporate Proxy[​](#corporate-proxy "Direct link to Corporate Proxy")

```
import ssl

# Custom SSL context
ssl_context = ssl.create_default_context()
ssl_context.load_cert_chain('cert.pem','key.pem')

# Proxy session
session = aiohttp.ClientSession(
    connector=aiohttp.TCPConnector(ssl=ssl_context),
    trust_env=True# Use environment proxy settings
)

litellm.base_llm_aiohttp_handler = BaseLLMAIOHTTPHandler(client_session=session)
```

### High Performance[​](#high-performance "Direct link to High Performance")

```
# Optimized for high throughput
session = aiohttp.ClientSession(
    timeout=aiohttp.ClientTimeout(total=300),
    connector=aiohttp.TCPConnector(
        limit=1000,# High connection limit
        limit_per_host=200,# Per host limit
        ttl_dns_cache=600,# DNS cache
        keepalive_timeout=60,# Keep connections alive
        enable_cleanup_closed=True
)
)

litellm.base_llm_aiohttp_handler = BaseLLMAIOHTTPHandler(client_session=session)
```

## Constructor Options[​](#constructor-options "Direct link to Constructor Options")

```
BaseLLMAIOHTTPHandler(
    client_session=None,# Custom aiohttp.ClientSession
    transport=None,# Advanced transport control
    connector=None,# Custom aiohttp.BaseConnector
)
```

## Resource Management[​](#resource-management "Direct link to Resource Management")

- **User sessions**: You manage the lifecycle (call `await session.close()`)
- **Auto-created sessions**: Automatically cleaned up by the handler
- **100% backward compatible**: Existing code works unchanged

## Configuration Tips[​](#configuration-tips "Direct link to Configuration Tips")

### Development[​](#development "Direct link to Development")

```
session = aiohttp.ClientSession(
    timeout=aiohttp.ClientTimeout(total=60),
    connector=aiohttp.TCPConnector(limit=50)
)
```

### Production[​](#production "Direct link to Production")

```
session = aiohttp.ClientSession(
    timeout=aiohttp.ClientTimeout(total=300),
    connector=aiohttp.TCPConnector(
        limit=1000,
        limit_per_host=200,
        keepalive_timeout=60
)
)
```