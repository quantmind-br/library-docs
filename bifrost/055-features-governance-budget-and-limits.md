---
title: Budget and Limits
url: https://docs.getbifrost.ai/features/governance/budget-and-limits.md
source: llms
fetched_at: 2026-01-21T19:43:37.072002032-03:00
rendered_js: false
word_count: 908
summary: This document explains Bifrost's hierarchical budget management and rate-limiting system, detailing how costs and usage are controlled across customers, teams, and virtual keys.
tags:
    - budget-management
    - cost-control
    - rate-limiting
    - virtual-keys
    - governance
    - usage-tracking
category: guide
---

# Budget and Limits

> Enterprise-grade budget management and cost control with hierarchical budget allocation through virtual keys, teams, and customers.

## Overview

Budgeting and rate limiting are a core feature of Bifrost's governance system managed through [Virtual Keys](./virtual-keys).

Bifrost's budget management system provides comprehensive cost control and financial governance for enterprise AI deployments. It operates through a **hierarchical budget structure** that enables granular cost management, usage tracking, and financial oversight across your entire organization.

**Core Hierarchy:**

```
Customer (has independent budget)
    ↓ (one-to-many)
Team (has independent budget) 
    ↓ (one-to-many)
Virtual Key (has independent budget + rate limits)
    ↓ (one-to-many)
Provider Config (has independent budget + rate limits)

OR

Customer (has independent budget)
    ↓ (direct attachment)
Virtual Key (has independent budget + rate limits)
    ↓ (one-to-many)
Provider Config (has independent budget + rate limits)

OR

Virtual Key (standalone - has independent budget + rate limits)
    ↓ (one-to-many)
Provider Config (has independent budget + rate limits)
```

**Key Capabilities:**

* **Virtual Keys** - Primary access control via `x-bf-vk` header (exclusive team OR customer attachment)
* **Budget Management** - Independent budget limits at each hierarchy level with cumulative checking
* **Rate Limiting** - Request and token-based throttling at both VK and provider config levels
* **Provider-Level Governance** - Granular budgets and rate limits per AI provider within a virtual key
* **Model/Provider Filtering** - Granular access control per virtual key
* **Usage Tracking** - Real-time monitoring and audit trails
* **Audit Headers** - Optional team and customer identification

***

## Budget Management

### Cost Calculation

Bifrost automatically calculates costs based on:

* **Provider Pricing** - Real-time model pricing data
* **Token Usage** - Input + output tokens from API responses
* **Request Type** - Different pricing for chat, text, embedding, speech, transcription
* **Cache Status** - Reduced costs for cached responses
* **Batch Operations** - Volume discounts for batch requests

All cost calculation details are covered in [Architecture > Framework > Model Catalog](../../architecture/framework/model-catalog).

### Budget Checking Flow

When a request is made with a virtual key, Bifrost checks **all applicable budgets independently** in the hierarchy. Each budget must have sufficient remaining balance for the request to proceed.

**Checking Sequence:**

**For VK → Team → Customer:**

```
1. ✓ Provider Config Budget (if provider config has budget)
2. ✓ VK Budget (if VK has budget)
3. ✓ Team Budget (if VK's team has budget)  
4. ✓ Customer Budget (if team's customer has budget)
```

**For VK → Customer (direct):**

```
1. ✓ Provider Config Budget (if provider config has budget)
2. ✓ VK Budget (if VK has budget)
3. ✓ Customer Budget (if VK's customer has budget)
```

**For Standalone VK:**

```
1. ✓ Provider Config Budget (if provider config has budget)
2. ✓ VK Budget (if VK has budget)
```

**Important Notes:**

* **All applicable budgets must pass** - any single budget failure blocks the request
* **Budgets are independent** - each tracks its own usage and limits
* **Costs are deducted from all applicable budgets** - same cost applied to each level
* **Rate limits checked at provider config and VK levels** - teams and customers have no rate limits
* **Provider selection** - providers that exceed their budget or rate limits are excluded from [routing](./routing)

**Example:**

```
- Provider config budget: $4/$5 remaining ✓
- VK budget: $9/$10 remaining ✓
- Team budget: $15/$20 remaining ✓  
- Customer budget: $45/$50 remaining ✓
- Result: Allowed (no budget is exceeded)

- After request: 
    - Request cost: $2 
    - Updated Provider=$6/$5, VK=$11/$10, Team=$17/$20, Customer=$47/$50
    - Then the next request will be blocked (both provider and VK budgets exceeded).
```

## Rate Limiting

Rate limits protect your system from abuse and manage traffic by setting thresholds on request frequency and token usage over a specific time window. Rate limits can be configured at **both the Virtual Key level and Provider Config level** for granular control.

Bifrost supports two types of rate limits that work in parallel:

* **Request Limits**: Control the maximum number of API calls that can be made within a set duration (e.g., 100 requests per minute).
* **Token Limits**: Control the maximum number of tokens (prompt + completion) that can be processed within a set duration (e.g., 50,000 tokens per hour).

### Rate Limit Hierarchy

Rate limits are checked in hierarchical order:

```
1. ✓ Provider Config Rate Limits (if provider config has rate limits)
2. ✓ Virtual Key Rate Limits (if VK has rate limits)
```

For a request to be allowed, it must pass both the request limit and token limit checks at **all applicable levels**. If a provider config exceeds its rate limits, that provider is excluded from routing, but other providers within the same virtual key remain available.

### Provider-Level Rate Limiting

Provider configs within a virtual key can have independent rate limits, enabling:

* **Per-Provider Throttling**: Different rate limits for OpenAI vs Anthropic
* **Provider Isolation**: Rate limit violations on one provider don't affect others
* **Granular Control**: Fine-tune limits based on provider capabilities and costs

## Reset Durations

Budgets and rate limits support flexible reset durations:

**Format Examples:**

* `1m` - 1 minute
* `5m` - 5 minutes
* `1h` - 1 hour
* `1d` - 1 day
* `1w` - 1 week
* `1M` - 1 month

**Common Patterns:**

* **Rate Limits**: `1m`, `1h`, `1d` for request throttling
* **Budgets**: `1d`, `1w`, `1M` for cost control

***

## Configuration Guide

Configure provider-level budgets and rate limits using any of these methods:

<Tabs>
  <Tab title="Web UI">
    The Bifrost Web UI provides an intuitive interface for configuring provider-level governance through the Virtual Keys management page.

    ### Creating Virtual Keys with Provider Configs

    1. **Navigate to Virtual Keys**: Go to **Virtual Keys** page in the Bifrost dashboard
    2. **Create New Virtual Key**: Click "Create Virtual Key" button
    3. **Configure Providers**: In the "Provider Configurations" section:
       * Add multiple providers with individual weights
       * Set provider-specific budgets and rate limits
       * Configure allowed models per provider

    ### Provider Configuration Interface

        <img src="https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-config.png?fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=88fe98a283ffe4851305e3f0217a2104" alt="Virtual Key Provider Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-virtual-key-provider-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-config.png?w=280&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=1ffa5eaa330118c040514af1adb01385 280w, https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-config.png?w=560&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=b992743537022224d5d10e357215e0ff 560w, https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-config.png?w=840&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=71bcb1516e62a1aa4023656e610c99f2 840w, https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-config.png?w=1100&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=1886ca46e692e434b5943d2f8f5383a7 1100w, https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-config.png?w=1650&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=95ea9756eac6745685be7bb412ca6916 1650w, https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-config.png?w=2500&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=0434a7805b115bfe294644dd1aff03ec 2500w" />

    **Key Features:**

    * **Visual Provider Cards**: Each provider displays as an expandable card
    * **Budget Controls**: Set spending limits with reset periods per provider
    * **Rate Limit Controls**: Configure token and request limits independently
    * **Model Filtering**: Specify allowed models for each provider
    * **Weight Distribution**: Visual indicators for load balancing weights
    * **Real-time Validation**: Immediate feedback on configuration errors

    ### Monitoring Provider Usage

        <img src="https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-usage-sheet.png?fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=b2dae526ea7371000b67a6a4ee2b9cc3" alt="Provider Usage Sheet" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-virtual-key-provider-usage-sheet.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-usage-sheet.png?w=280&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=38dc6ea0fe8a24e69d839a8130e81a37 280w, https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-usage-sheet.png?w=560&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=a94871f890531f2e24293ed51bfc8ec0 560w, https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-usage-sheet.png?w=840&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=d86849783e8ae07c1ed70a0b03f66b7d 840w, https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-usage-sheet.png?w=1100&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=cb78361fc71ad8068cbbeb7f80714462 1100w, https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-usage-sheet.png?w=1650&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=99a06911d42a284557d024127d5da969 1650w, https://mintcdn.com/bifrost/9GZ8430d0epbuZAi/media/ui-virtual-key-provider-usage-sheet.png?w=2500&fit=max&auto=format&n=9GZ8430d0epbuZAi&q=85&s=a0469a51b79b508772faf730b439d1de 2500w" />

    The info sheet for the virtual key provides real-time monitoring of:

    * Budget consumption per provider
    * Rate limit utilization (tokens and requests)
    * Provider availability status
    * Usage trends and forecasting
  </Tab>

  <Tab title="API">
    Use the Bifrost HTTP API to programmatically manage provider-level governance configurations.

    ### Create Virtual Key with Provider Configs

    ```bash  theme={null}
    curl -X POST "https://your-bifrost-instance.com/api/governance/virtual-keys" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "marketing-team-vk",
        "description": "Marketing team virtual key with provider-specific limits",
        "provider_configs": [
          {
            "provider": "openai",
            "weight": 0.7,
            "allowed_models": ["gpt-4", "gpt-3.5-turbo"],
            "budget": {
              "max_limit": 500.00,
              "reset_duration": "1M"
            },
            "rate_limit": {
              "token_max_limit": 1000000,
              "token_reset_duration": "1h",
              "request_max_limit": 1000,
              "request_reset_duration": "1h"
            }
          },
          {
            "provider": "anthropic",
            "weight": 0.3,
            "allowed_models": ["claude-3-opus", "claude-3-sonnet"],
            "budget": {
              "max_limit": 200.00,
              "reset_duration": "1M"
            },
            "rate_limit": {
              "token_max_limit": 500000,
              "token_reset_duration": "1h",
              "request_max_limit": 500,
              "request_reset_duration": "1h"
            }
          }
        ],
        "budget": {
          "max_limit": 1000.00,
          "reset_duration": "1M"
        },
        "is_active": true
      }'
    ```

    ### Update Provider Configuration

    ```bash  theme={null}
    curl -X PUT "https://your-bifrost-instance.com/api/governance/virtual-keys/{vk_id}" \
      -H "Content-Type: application/json" \
      -d '{
        "provider_configs": [
          {
            "id": 1,
            "provider": "openai",
            "weight": 0.8,
            "budget": {
              "max_limit": 600.00,
              "reset_duration": "1M"
            },
            "rate_limit": {
              "token_max_limit": 1200000,
              "token_reset_duration": "1h"
            }
          }
        ]
      }'
    ```

    ### API Response Structure

    ```json  theme={null}
    {
      "message": "Virtual key created successfully",
      "virtual_key": {
        "id": "vk_123",
        "name": "marketing-team-vk",
        "value": "vk_abc123def456",
        "provider_configs": [
          {
            "id": 1,
            "provider": "openai",
            "weight": 0.7,
            "allowed_models": ["gpt-4", "gpt-3.5-turbo"],
            "budget": {
              "id": "budget_789",
              "max_limit": 500.00,
              "current_usage": 0.00,
              "reset_duration": "1M",
              "last_reset": "2024-01-01T00:00:00Z"
            },
            "rate_limit": {
              "id": "rate_limit_456",
              "token_max_limit": 1000000,
              "token_current_usage": 0,
              "token_reset_duration": "1h",
              "token_last_reset": "2024-01-01T00:00:00Z",
              "request_max_limit": 1000,
              "request_current_usage": 0,
              "request_reset_duration": "1h",
              "request_last_reset": "2024-01-01T00:00:00Z"
            }
          }
        ]
      }
    }
    ```

    ### Field Descriptions

    | Field                          | Type    | Description                                    |
    | ------------------------------ | ------- | ---------------------------------------------- |
    | `provider`                     | string  | AI provider name (e.g., "openai", "anthropic") |
    | `weight`                       | float   | Load balancing weight (0.0-1.0)                |
    | `allowed_models`               | array   | Specific models allowed for this provider      |
    | `budget.max_limit`             | float   | Maximum spend in USD                           |
    | `budget.reset_duration`        | string  | Reset period (e.g., "1h", "1d", "1M")          |
    | `rate_limit.token_max_limit`   | integer | Maximum tokens per period                      |
    | `rate_limit.request_max_limit` | integer | Maximum requests per period                    |
  </Tab>

  <Tab title="config.json">
    Configure provider-level governance through Bifrost's configuration file for declarative management.

    ### Basic Configuration Structure

    ```json  theme={null}
    {
      "governance": {
        "virtual_keys": [
          {
            "name": "development-team-vk",
            "description": "Development team with multi-provider setup",
            "provider_configs": [
              {
                "provider": "openai",
                "weight": 0.6,
                "allowed_models": ["gpt-4", "gpt-3.5-turbo"],
                "budget": {
                  "max_limit": 1000.00,
                  "reset_duration": "1M"
                },
                "rate_limit": {
                  "token_max_limit": 2000000,
                  "token_reset_duration": "1h",
                  "request_max_limit": 2000,
                  "request_reset_duration": "1h"
                }
              },
              {
                "provider": "anthropic",
                "weight": 0.4,
                "allowed_models": ["claude-3-opus", "claude-3-sonnet"],
                "budget": {
                  "max_limit": 500.00,
                  "reset_duration": "1M"
                },
                "rate_limit": {
                  "token_max_limit": 1000000,
                  "token_reset_duration": "1h",
                  "request_max_limit": 1000,
                  "request_reset_duration": "1h"
                }
              }
            ],
            "budget": {
              "max_limit": 2000.00,
              "reset_duration": "1M"
            },
            "rate_limit": {
              "token_max_limit": 5000000,
              "token_reset_duration": "1h",
              "request_max_limit": 3000,
              "request_reset_duration": "1h"
            },
            "is_active": true
          }
        ]
      }
    }
    ```

    ### Advanced Configuration Examples

    #### Cost-Optimized Setup

    ```json  theme={null}
    {
      "governance": {
        "virtual_keys": [
          {
            "name": "cost-optimized-vk",
            "provider_configs": [
              {
                "provider": "openai-gpt-3.5",
                "weight": 0.8,
                "budget": {
                  "max_limit": 50.00,
                  "reset_duration": "1d"
                },
                "rate_limit": {
                  "request_max_limit": 1000,
                  "request_reset_duration": "1h"
                }
              },
              {
                "provider": "openai-gpt-4",
                "weight": 0.2,
                "budget": {
                  "max_limit": 200.00,
                  "reset_duration": "1d"
                },
                "rate_limit": {
                  "request_max_limit": 100,
                  "request_reset_duration": "1h"
                }
              }
            ]
          }
        ]
      }
    }
    ```

    #### High-Volume Production Setup

    ```json  theme={null}
    {
      "governance": {
        "virtual_keys": [
          {
            "name": "production-high-volume-vk",
            "provider_configs": [
              {
                "provider": "openai",
                "weight": 0.5,
                "budget": {
                  "max_limit": 5000.00,
                  "reset_duration": "1M"
                },
                "rate_limit": {
                  "token_max_limit": 10000000,
                  "token_reset_duration": "1h",
                  "request_max_limit": 10000,
                  "request_reset_duration": "1h"
                }
              },
              {
                "provider": "anthropic",
                "weight": 0.3,
                "budget": {
                  "max_limit": 3000.00,
                  "reset_duration": "1M"
                },
                "rate_limit": {
                  "token_max_limit": 6000000,
                  "token_reset_duration": "1h",
                  "request_max_limit": 6000,
                  "request_reset_duration": "1h"
                }
              },
              {
                "provider": "azure-openai",
                "weight": 0.2,
                "budget": {
                  "max_limit": 2000.00,
                  "reset_duration": "1M"
                },
                "rate_limit": {
                  "token_max_limit": 4000000,
                  "token_reset_duration": "1h",
                  "request_max_limit": 4000,
                  "request_reset_duration": "1h"
                }
              }
            ]
          }
        ]
      }
    }
    ```

    **Validation Rules:**

    * Budget limits must be positive numbers
    * Reset durations must be valid time formats
    * Rate limits must be positive integers
    * Provider names must match configured providers
  </Tab>
</Tabs>

## Provider-Level Governance Examples

### Example 1: Mixed Provider Budgets

A virtual key configured with multiple providers and different budget allocations:

```json  theme={null}
{
  "name": "marketing-team-vk",
  "budget": { "max_limit": 100, "reset_duration": "1M" },
  "provider_configs": [
    {
      "provider": "openai",
      "weight": 0.7,
      "budget": { "max_limit": 50, "reset_duration": "1M" }
    },
    {
      "provider": "anthropic", 
      "weight": 0.3,
      "budget": { "max_limit": 30, "reset_duration": "1M" }
    }
  ]
}
```

**Behavior:**

* OpenAI requests limited to 50 dollars/month at provider level + 100 dollars/month at VK level
* Anthropic requests limited to 30 dollars/month at provider level + 100 dollars/month at VK level
* If any provider's budget is exhausted, all requests to that provider will be blocked

### Example 2: Provider-Specific Rate Limits

Different rate limits based on provider capabilities:

```json  theme={null}
{
  "name": "high-volume-vk",
  "provider_configs": [
    {
      "provider": "openai",
      "rate_limit": {
        "request_max_limit": 1000,
        "request_reset_duration": "1h",
        "token_max_limit": 1000000,
        "token_reset_duration": "1h"
      }
    },
    {
      "provider": "anthropic",
      "rate_limit": {
        "request_max_limit": 500,
        "request_reset_duration": "1h",
        "token_max_limit": 500000,
        "token_reset_duration": "1h"
      }
    }
  ]
}
```

**Behavior:**

* OpenAI: 1000 requests/hour, 1M tokens/hour
* Anthropic: 500 requests/hour, 500K tokens/hour
* If any provider's rate limits are exceeded, all requests to that provider will be blocked

### Example 3: Failover Strategy

Provider configurations with budget-based failover:

```json  theme={null}
{
  "name": "cost-optimized-vk",
  "provider_configs": [
    {
      "provider": "openai-cheap",
      "weight": 1.0,
      "budget": { "max_limit": 10, "reset_duration": "1d" }
    },
    {
      "provider": "openai-premium",
      "weight": 0.0,
      "budget": { "max_limit": 50, "reset_duration": "1d" },
      "rate_limit": {
        "request_max_limit": 100,
        "request_reset_duration": "1h",
        "token_max_limit": 50000,
        "token_reset_duration": "1h"
      }
    }
  ]
}
```

**Behavior:**

* Primary: Use cheap provider until \$10 daily budget exhausted
* Fallback: Automatically switch to premium provider when cheap option unavailable. To enable this, you should not send `provider` name in the request body, read [Routing](./routing#automatic-fallbacks) for more details.
* Cost containment: Prevent unexpected overspend on premium resources and limit the number of requests to the premium provider

## Key Benefits of Provider-Level Governance

* **Granular Control**: Set specific spending limits and rate limits per AI provider
* **Automatic Fallback**: Route to alternative providers when budgets or rate limits are exceeded
* **Cost Control**: Track and control spending by provider for better financial oversight
* **Performance Testing**: A/B testing across providers with controlled budgets
* **Multi-Provider Strategies**: Primary/backup provider configurations
* **Cost-Tiered Access**: Cheap providers for basic tasks, premium for complex workloads

***

## Next Steps

* **[Routing](./routing)** - Direct requests to specific AI models, providers, and keys using Virtual Keys.
* **[MCP Tool Filtering](./mcp-tools)** - Manage MCP clients/tools for virtual keys.
* **[Tracing](../observability/default)** - Audit trails and request tracking


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt