---
title: MCP Cost Tracking | liteLLM
url: https://docs.litellm.ai/docs/mcp_cost
source: sitemap
fetched_at: 2026-01-21T19:45:41.018844265-03:00
rendered_js: false
word_count: 122
summary: This document explains how to track and manage costs for Model Context Protocol (MCP) tool calls in LiteLLM using either static configuration or custom dynamic hooks.
tags:
    - litellm
    - mcp-protocol
    - cost-tracking
    - tool-calling
    - configuration
    - python-hooks
category: guide
---

LiteLLM provides two ways to track costs for MCP tool calls:

MethodWhen to UseWhat It Does**Config-based Cost Tracking**Simple cost tracking with fixed costs per tool/serverAutomatically tracks costs based on configuration**Custom Post-MCP Hook**Dynamic cost tracking with custom logicAllows custom cost calculations and response modifications

### Config-based Cost Tracking[​](#config-based-cost-tracking "Direct link to Config-based Cost Tracking")

Configure fixed costs for MCP servers directly in your config.yaml:

config.yaml

```
model_list:
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_key: sk-xxxxxxx

mcp_servers:
zapier_server:
url:"https://actions.zapier.com/mcp/sk-xxxxx/sse"
mcp_info:
mcp_server_cost_info:
# Default cost for all tools in this server
default_cost_per_query:0.01
# Custom cost for specific tools
tool_name_to_cost_per_query:
send_email:0.05
create_document:0.03

expensive_api_server:
url:"https://api.expensive-service.com/mcp"
mcp_info:
mcp_server_cost_info:
default_cost_per_query:1.50
```

### Custom Post-MCP Hook[​](#custom-post-mcp-hook "Direct link to Custom Post-MCP Hook")

Use this when you need dynamic cost calculation or want to modify the MCP response before it's returned to the user.

#### 1. Create a custom MCP hook file[​](#1-create-a-custom-mcp-hook-file "Direct link to 1. Create a custom MCP hook file")

custom\_mcp\_hook.py

```
from typing import Optional
from litellm.integrations.custom_logger import CustomLogger
from litellm.types.mcp import MCPPostCallResponseObject


classCustomMCPCostTracker(CustomLogger):
"""
    Custom handler for MCP cost tracking and response modification
    """

asyncdefasync_post_mcp_tool_call_hook(
        self,
        kwargs,
        response_obj: MCPPostCallResponseObject,
        start_time,
        end_time
)-> Optional[MCPPostCallResponseObject]:
"""
        Called after each MCP tool call. 
        Modify costs and response before returning to user.
        """

# Extract tool information from kwargs
        tool_name = kwargs.get("name","")
        server_name = kwargs.get("server_name","")

# Calculate custom cost based on your logic
        custom_cost =42.00

# Set the response cost
        response_obj.hidden_params.response_cost = custom_cost


return response_obj


# Create instance for LiteLLM to use
custom_mcp_cost_tracker = CustomMCPCostTracker()
```

#### 2. Configure in config.yaml[​](#2-configure-in-configyaml "Direct link to 2. Configure in config.yaml")

config.yaml

```
model_list:
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_key: sk-xxxxxxx

# Add your custom MCP hook
callbacks:
- custom_mcp_hook.custom_mcp_cost_tracker

mcp_servers:
zapier_server:
url:"https://actions.zapier.com/mcp/sk-xxxxx/sse"
```

#### 3. Start the proxy[​](#3-start-the-proxy "Direct link to 3. Start the proxy")

```
$ litellm --config /path/to/config.yaml 
```

When MCP tools are called, your custom hook will:

1. Calculate costs based on your custom logic
2. Modify the response if needed
3. Track costs in LiteLLM's logging system