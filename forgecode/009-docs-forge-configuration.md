---
title: ForgeCode
url: https://forgecode.dev/docs/forge-configuration/
source: sitemap
fetched_at: 2026-03-29T16:30:40.071783-03:00
rendered_js: false
word_count: 270
summary: This document describes the root-level configuration options available in the forge.yaml file for managing ForgeCode system behavior, request limits, and model parameters.
tags:
    - forgecode
    - yaml-configuration
    - model-parameters
    - resource-management
    - system-settings
    - request-handling
category: configuration
---

ForgeCode provides comprehensive configuration options through your `forge.yaml` file. These root-level settings control behavior and apply globally to your entire ForgeCode instance.

Root-level configuration options are placed at the top of your `forge.yaml` file.

### Request and Turn Management[​](#request-and-turn-management "Direct link to Request and Turn Management")

#### `max_requests_per_turn`[​](#max_requests_per_turn "Direct link to max_requests_per_turn")

- **Type**: `number`
- **Default**: `50`
- **Description**: Sets the maximum number of requests that can be made in a single conversation turn. This prevents runaway operations and controls resource usage.

#### `max_tool_failure_per_turn`[​](#max_tool_failure_per_turn "Direct link to max_tool_failure_per_turn")

- **Type**: `number`
- **Default**: `3`
- **Description**: Defines the maximum number of consecutive tool failures allowed before the agent stops attempting to use tools. This prevents infinite retry loops when tools are consistently failing.

### Model Parameters[​](#model-parameters "Direct link to Model Parameters")

#### `top_p`[​](#top_p "Direct link to top_p")

- **Type**: `number`
- **Range**: `0.0` to `1.0`
- **Default**: `0.8`
- **Description**: Controls the diversity of the model's responses. Lower values make responses more focused and deterministic, while higher values increase creativity and randomness.

#### `top_k`[​](#top_k "Direct link to top_k")

- **Type**: `number`
- **Default**: `30`
- **Description**: Limits the model to consider only the top K most likely tokens at each step. Lower values make responses more predictable, while higher values allow for more diverse outputs.

#### `max_tokens`[​](#max_tokens "Direct link to max_tokens")

- **Type**: `number`
- **Default**: `20480`
- **Description**: Sets the maximum number of tokens the model can generate in a single response. This controls the length of responses and helps manage costs.

### System Behavior[​](#system-behavior "Direct link to System Behavior")

#### `max_walker_depth`[​](#max_walker_depth "Direct link to max_walker_depth")

- **Type**: `number`
- **Default**: `1`
- **Description**: Sets the maximum depth for file system traversal operations. Controls how deep ForgeCode will recursively explore directory structures to prevent excessive resource usage.

### Updates[​](#updates "Direct link to Updates")

#### `updates`[​](#updates-1 "Direct link to updates-1")

- **Type**: `object`
- **Description**: Configures automatic update behavior for ForgeCode.

Here's a complete example of a well-configured `forge.yaml` file:

- [Environment Configuration](https://forgecode.dev/docs/environment-configuration/) - Environment-specific settings
- [Context Compaction](https://forgecode.dev/docs/context-compaction/) - Memory management and conversation history
- [MCP Integration](https://forgecode.dev/docs/mcp-integration/) - Model Context Protocol setup