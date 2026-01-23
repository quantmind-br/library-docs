---
title: Control Plane for Multi-region Architecture (Enterprise) | liteLLM
url: https://docs.litellm.ai/docs/proxy/control_plane_and_data_plane
source: sitemap
fetched_at: 2026-01-21T19:51:28.329938359-03:00
rendered_js: false
word_count: 422
summary: This guide explains how to implement a distributed LiteLLM architecture by separating regional worker instances from a centralized administrative instance to optimize performance and management.
tags:
    - litellm
    - multi-region
    - deployment-architecture
    - configuration
    - scalability
    - distributed-systems
category: guide
---

Learn how to deploy LiteLLM across multiple regions while maintaining centralized administration and avoiding duplication of management overhead.

## Overview[​](#overview "Direct link to Overview")

When scaling LiteLLM for production use, you may want to deploy multiple instances across different regions or availability zones while maintaining a single point of administration. This guide covers how to set up a distributed LiteLLM deployment with:

- **Regional Worker Instances**: Handle LLM requests for users in specific regions
- **Centralized Admin Instance**: Manages configuration, users, keys, and monitoring

## Architecture Pattern: Regional + Admin Instances[​](#architecture-pattern-regional--admin-instances "Direct link to Architecture Pattern: Regional + Admin Instances")

### Typical Deployment Scenario[​](#typical-deployment-scenario "Direct link to Typical Deployment Scenario")

### Benefits of This Architecture[​](#benefits-of-this-architecture "Direct link to Benefits of This Architecture")

1. **Reduced Management Overhead**: Only one instance needs admin capabilities
2. **Regional Performance**: Users get low-latency access from their region
3. **Centralized Control**: All administration happens from a single interface
4. **Security**: Limit admin access to designated instances only
5. **Cost Efficiency**: Avoid duplicating admin infrastructure

## Configuration[​](#configuration "Direct link to Configuration")

### Admin Instance Configuration[​](#admin-instance-configuration "Direct link to Admin Instance Configuration")

The admin instance handles all management operations and provides the UI.

**Environment Variables for Admin Instance:**

```
# Keep admin capabilities enabled (default behavior)
# DISABLE_ADMIN_UI=false          # Admin UI available
# DISABLE_ADMIN_ENDPOINTS=false   # Management APIs available
DISABLE_LLM_API_ENDPOINTS=true      # LLM APIs disabled
DATABASE_URL=postgresql://user:pass@global-db:5432/litellm
LITELLM_MASTER_KEY=your-master-key
```

### Worker Instance Configuration[​](#worker-instance-configuration "Direct link to Worker Instance Configuration")

Worker instances handle LLM requests but have admin capabilities disabled.

**Environment Variables for Worker Instances:**

```
# Disable admin capabilities
DISABLE_ADMIN_UI=true           # No admin UI
DISABLE_ADMIN_ENDPOINTS=true    # No management endpoints

DATABASE_URL=postgresql://user:pass@global-db:5432/litellm
LITELLM_MASTER_KEY=your-master-key
```

## Environment Variables Reference[​](#environment-variables-reference "Direct link to Environment Variables Reference")

### `DISABLE_ADMIN_UI`[​](#disable_admin_ui "Direct link to disable_admin_ui")

Disables the LiteLLM Admin UI interface.

- **Default**: `false`
- **Worker Instances**: Set to `true`
- **Admin Instance**: Leave as `false` (or don't set)

```
# Worker instances
DISABLE_ADMIN_UI=true
```

**Effect**: When enabled, the web UI at `/ui` becomes unavailable.

### `DISABLE_ADMIN_ENDPOINTS`[​](#disable_admin_endpoints "Direct link to disable_admin_endpoints")

Disables all management/admin API endpoints.

- **Default**: `false`
- **Worker Instances**: Set to `true`
- **Admin Instance**: Leave as `false` (or don't set)

```
# Worker instances  
DISABLE_ADMIN_ENDPOINTS=true
```

**Disabled Endpoints Include**:

- `/key/*` - Key management
- `/user/*` - User management
- `/team/*` - Team management
- `/config/*` - Configuration updates
- All other administrative endpoints

**Available Endpoints** (when disabled):

- `/chat/completions` - LLM requests
- `/v1/*` - OpenAI-compatible APIs
- `/vertex_ai/*` - Vertex AI pass-through APIs
- `/bedrock/*` - Bedrock pass-through APIs
- `/health` - Basic health check
- `/metrics` - Prometheus metrics
- All other LLM API endpoints

### `DISABLE_LLM_API_ENDPOINTS`[​](#disable_llm_api_endpoints "Direct link to disable_llm_api_endpoints")

Disables all LLM API endpoints.

- **Default**: `false`
- **Worker Instances**: Leave as `false` (or don't set)
- **Admin Instance**: Set to `true`

```
# Admin instance
DISABLE_LLM_API_ENDPOINTS=true
```

**Disabled Endpoints Include**:

- `/chat/completions` - LLM requests
- `/v1/*` - OpenAI-compatible APIs
- `/vertex_ai/*` - Vertex AI pass-through APIs
- `/bedrock/*` - Bedrock pass-through APIs
- All other LLM API endpoints

**Available Endpoints** (when disabled):

- `/key/*` - Key management
- `/user/*` - User management
- `/team/*` - Team management
- `/config/*` - Configuration updates
- All other administrative endpoints

### `LITELLM_UI_API_DOC_BASE_URL`[​](#litellm_ui_api_doc_base_url "Direct link to litellm_ui_api_doc_base_url")

Optional override for the API Reference base URL (used in sample code/docs) when the admin UI runs on a different host than the proxy.

## Usage Patterns[​](#usage-patterns "Direct link to Usage Patterns")

### Client Usage[​](#client-usage "Direct link to Client Usage")

**For LLM Requests** (use regional endpoints):

```
import openai

# US users
client_us = openai.OpenAI(
    base_url="https://us.company.com/v1",
    api_key="your-litellm-key"
)

# EU users  
client_eu = openai.OpenAI(
    base_url="https://eu.company.com/v1",
    api_key="your-litellm-key"
)

response = client_us.chat.completions.create(
    model="gpt-4",
    messages=[{"role":"user","content":"Hello!"}]
)
```

**For Administration** (use admin endpoint):

```
import requests

# Create a new API key
response = requests.post(
"https://admin.company.com/key/generate",
    headers={"Authorization":"Bearer sk-1234"},
    json={"duration":"30d"}
)
```

- [Virtual Keys](https://docs.litellm.ai/docs/proxy/virtual_keys) - Managing API keys and users
- [Health Checks](https://docs.litellm.ai/docs/proxy/health) - Monitoring instance health
- [Prometheus Metrics](https://docs.litellm.ai/docs/proxy/logging#prometheus-metrics) - Collecting metrics
- [Production Deployment](https://docs.litellm.ai/docs/proxy/prod) - Production best practices