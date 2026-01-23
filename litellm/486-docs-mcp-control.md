---
title: MCP Permission Management | liteLLM
url: https://docs.litellm.ai/docs/mcp_control
source: sitemap
fetched_at: 2026-01-21T19:45:40.597649004-03:00
rendered_js: false
word_count: 1562
summary: This document explains how to configure and manage access controls for MCP servers in LiteLLM, covering tool-level filtering, parameter restrictions, and entity-based permission management.
tags:
    - mcp-server
    - access-control
    - permissions
    - security
    - tool-filtering
    - litellm-config
    - parameter-control
category: configuration
---

Control which MCP servers and tools can be accessed by specific keys, teams, or organizations in LiteLLM. When a client attempts to list or call tools, LiteLLM enforces access controls based on configured permissions.

## Overview[​](#overview "Direct link to Overview")

LiteLLM provides fine-grained permission management for MCP servers, allowing you to:

- **Restrict MCP access by entity**: Control which keys, teams, or organizations can access specific MCP servers
- **Tool-level filtering**: Automatically filter available tools based on entity permissions
- **Centralized control**: Manage all MCP permissions from the LiteLLM Admin UI or API
- **One-click public MCPs**: Mark specific servers as available to every LiteLLM API key when you don't need per-key restrictions

This ensures that only authorized entities can discover and use MCP tools, providing an additional security layer for your MCP infrastructure.

## How It Works[​](#how-it-works "Direct link to How It Works")

LiteLLM supports managing permissions for MCP Servers by Keys, Teams, Organizations (entities) on LiteLLM. When a MCP client attempts to list tools, LiteLLM will only return the tools the entity has permissions to access.

When Creating a Key, Team, or Organization, you can select the allowed MCP Servers that the entity has access to.

Control which tools are available from your MCP servers. You can either allow only specific tools or block dangerous ones.

- Only Allow Specific Tools
- Block Specific Tools

Use `allowed_tools` to specify exactly which tools users can access. All other tools will be blocked.

config.yaml

```
mcp_servers:
github_mcp:
url:"https://api.githubcopilot.com/mcp"
auth_type: oauth2
authorization_url: https://github.com/login/oauth/authorize
token_url: https://github.com/login/oauth/access_token
client_id: os.environ/GITHUB_OAUTH_CLIENT_ID
client_secret: os.environ/GITHUB_OAUTH_CLIENT_SECRET
scopes:["public_repo","user:email"]
allowed_tools:["list_tools"]
# only list_tools will be available
```

**Use this when:**

- You want strict control over which tools are available
- You're in a high-security environment
- You're testing a new MCP server with limited tools

### Important Notes[​](#important-notes "Direct link to Important Notes")

- If you specify both `allowed_tools` and `disallowed_tools`, the allowed list takes priority
- Tool names are case-sensitive

## Public MCP Servers (allow\_all\_keys)[​](#public-mcp-servers-allow_all_keys "Direct link to Public MCP Servers (allow_all_keys)")

Some MCP servers are meant to be shared broadly—think internal knowledge bases, calendar integrations, or other low-risk utilities where every team should be able to connect without requesting access. Instead of adding those servers to every key, team, or organization, enable the new `allow_all_keys` toggle.

- UI
- config.yaml

<!--THE END-->

1. Open **MCP Servers → Add / Edit** in the Admin UI.
2. Expand **Permission Management / Access Control**.
3. Toggle **Allow All LiteLLM Keys** on.

The toggle makes the server “public” without touching existing access groups.

### When to use it[​](#when-to-use-it "Direct link to When to use it")

- You have shared MCP utilities where fine-grained ACLs would only add busywork.
- You want a “default enabled” experience for internal users, while still being able to layer tool-level restrictions.
- You’re onboarding new teams and want the safest MCPs available out of the box.

Once enabled, LiteLLM automatically includes the server for every key during tool discovery/calls—no extra virtual-key or team configuration is required.

* * *

Control which parameters are allowed for specific MCP tools using the `allowed_params` configuration. This provides fine-grained control over tool usage by restricting the parameters that can be passed to each tool.

### Configuration[​](#configuration "Direct link to Configuration")

`allowed_params` is a dictionary that maps tool names to lists of allowed parameter names. When configured, only the specified parameters will be accepted for that tool - any other parameters will be rejected with a 403 error.

config.yaml with allowed\_params

```
mcp_servers:
deepwiki_mcp:
url: https://mcp.deepwiki.com/mcp
transport:"http"
auth_type:"none"
allowed_params:
# Tool name: list of allowed parameters
read_wiki_contents:["status"]

my_api_mcp:
url:"https://my-api-server.com"
auth_type:"api_key"
auth_value:"my-key"
allowed_params:
# Using unprefixed tool name
getpetbyid:["status"]
# Using prefixed tool name (both formats work)
my_api_mcp-findpetsbystatus:["status","limit"]
# Another tool with multiple allowed params
create_issue:["title","body","labels"]
```

### How It Works[​](#how-it-works-1 "Direct link to How It Works")

1. **Tool-specific filtering**: Each tool can have its own list of allowed parameters
2. **Flexible naming**: Tool names can be specified with or without the server prefix (e.g., both `"getpetbyid"` and `"my_api_mcp-getpetbyid"` work)
3. **Whitelist approach**: Only parameters in the allowed list are permitted
4. **Unlisted tools**: If `allowed_params` is not set, all parameters are allowed
5. **Error handling**: Requests with disallowed parameters receive a 403 error with details about which parameters are allowed

### Example Request Behavior[​](#example-request-behavior "Direct link to Example Request Behavior")

With the configuration above, here's how requests would be handled:

**✅ Allowed Request:**

```
{
"tool":"read_wiki_contents",
"arguments":{
"status":"active"
}
}
```

**❌ Rejected Request:**

```
{
"tool":"read_wiki_contents",
"arguments":{
"status":"active",
"limit":10// This parameter is not allowed
}
}
```

**Error Response:**

```
{
"error":"Parameters ['limit'] are not allowed for tool read_wiki_contents. Allowed parameters: ['status']. Contact proxy admin to allow these parameters."
}
```

### Use Cases[​](#use-cases "Direct link to Use Cases")

- **Security**: Prevent users from accessing sensitive parameters or dangerous operations
- **Cost control**: Restrict expensive parameters (e.g., limiting result counts)
- **Compliance**: Enforce parameter usage policies for regulatory requirements
- **Staged rollouts**: Gradually enable parameters as tools are tested
- **Multi-tenant isolation**: Different parameter access for different user groups

### Combining with Tool Filtering[​](#combining-with-tool-filtering "Direct link to Combining with Tool Filtering")

`allowed_params` works alongside `allowed_tools` and `disallowed_tools` for complete control:

Combined filtering example

```
mcp_servers:
github_mcp:
url:"https://api.githubcopilot.com/mcp"
auth_type: oauth2
authorization_url: https://github.com/login/oauth/authorize
token_url: https://github.com/login/oauth/access_token
client_id: os.environ/GITHUB_OAUTH_CLIENT_ID
client_secret: os.environ/GITHUB_OAUTH_CLIENT_SECRET
scopes:["public_repo","user:email"]
# Only allow specific tools
allowed_tools:["create_issue","list_issues","search_issues"]
# Block dangerous operations
disallowed_tools:["delete_repo"]
# Restrict parameters per tool
allowed_params:
create_issue:["title","body","labels"]
list_issues:["state","sort","perPage"]
search_issues:["query","sort","order","perPage"]
```

This configuration ensures that:

1. Only the three listed tools are available
2. The `delete_repo` tool is explicitly blocked
3. Each tool can only use its specified parameters

* * *

## MCP Server Access Control[​](#mcp-server-access-control "Direct link to MCP Server Access Control")

LiteLLM Proxy provides two methods for controlling access to specific MCP servers:

1. **URL-based Namespacing** - Use URL paths to directly access specific servers or access groups
2. **Header-based Namespacing** - Use the `x-mcp-servers` header to specify which servers to access

* * *

### Method 1: URL-based Namespacing[​](#method-1-url-based-namespacing "Direct link to Method 1: URL-based Namespacing")

LiteLLM Proxy supports URL-based namespacing for MCP servers using the format `/<servers or access groups>/mcp`. This allows you to:

- **Direct URL Access**: Point MCP clients directly to specific servers or access groups via URL
- **Simplified Configuration**: Use URLs instead of headers for server selection
- **Access Group Support**: Use access group names in URLs for grouped server access

#### URL Format[​](#url-format "Direct link to URL Format")

```
<your-litellm-proxy-base-url>/<server_alias_or_access_group>/mcp
```

**Examples:**

- `/github_mcp/mcp` - Access tools from the "github\_mcp" MCP server
- `/zapier/mcp` - Access tools from the "zapier" MCP server
- `/dev_group/mcp` - Access tools from all servers in the "dev\_group" access group
- `/github_mcp,zapier/mcp` - Access tools from multiple specific servers

#### Usage Examples[​](#usage-examples "Direct link to Usage Examples")

- OpenAI API
- LiteLLM Proxy
- Cursor IDE

cURL Example with URL Namespacing

```
curl --location 'https://api.openai.com/v1/responses' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $OPENAI_API_KEY" \
--data '{
    "model": "gpt-4o",
    "tools": [
        {
            "type": "mcp",
            "server_label": "litellm",
            "server_url": "<your-litellm-proxy-base-url>/github_mcp/mcp",
            "require_approval": "never",
            "headers": {
                "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY"
            }
        }
    ],
    "input": "Run available tools",
    "tool_choice": "required"
}'
```

This example uses URL namespacing to access only the "github" MCP server.

#### Benefits of URL Namespacing[​](#benefits-of-url-namespacing "Direct link to Benefits of URL Namespacing")

- **Direct Access**: No need for additional headers to specify servers
- **Clean URLs**: Self-documenting URLs that clearly indicate which servers are accessible
- **Access Group Support**: Use access group names for grouped server access
- **Multiple Servers**: Specify multiple servers in a single URL with comma separation
- **Simplified Configuration**: Easier setup for MCP clients that prefer URL-based configuration

* * *

You can choose to access specific MCP servers and only list their tools using the `x-mcp-servers` header. This header allows you to:

- Limit tool access to one or more specific MCP servers
- Control which tools are available in different environments or use cases

The header accepts a comma-separated list of server aliases: `"alias_1,Server2,Server3"`

**Notes:**

- If the header is not provided, tools from all available MCP servers will be accessible
- This method works with the standard LiteLLM MCP endpoint

<!--THE END-->

- OpenAI API
- LiteLLM Proxy
- Cursor IDE

cURL Example with Header Namespacing

```
curl --location 'https://api.openai.com/v1/responses' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $OPENAI_API_KEY" \
--data '{
    "model": "gpt-4o",
    "tools": [
        {
            "type": "mcp",
            "server_label": "litellm",
            "server_url": "<your-litellm-proxy-base-url>/mcp/",
            "require_approval": "never",
            "headers": {
                "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY",
                "x-mcp-servers": "alias_1"
            }
        }
    ],
    "input": "Run available tools",
    "tool_choice": "required"
}'
```

In this example, the request will only have access to tools from the "alias\_1" MCP server.

* * *

FeatureHeader NamespacingURL Namespacing**Method**Uses `x-mcp-servers` headerUses URL path `/<servers>/mcp`**Endpoint**Standard `litellm_proxy` endpointCustom `/<servers>/mcp` endpoint**Configuration**Requires additional headerSelf-contained in URL**Multiple Servers**Comma-separated in headerComma-separated in URL path**Access Groups**Supported via headerSupported via URL path**Client Support**Works with all MCP clientsWorks with URL-aware MCP clients**Use Case**Dynamic server selectionFixed server configuration

- OpenAI API
- LiteLLM Proxy
- Cursor IDE

cURL Example with Server Segregation

```
curl --location 'https://api.openai.com/v1/responses' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $OPENAI_API_KEY" \
--data '{
    "model": "gpt-4o",
    "tools": [
        {
            "type": "mcp",
            "server_label": "litellm",
            "server_url": "<your-litellm-proxy-base-url>/mcp/",
            "require_approval": "never",
            "headers": {
                "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY",
                "x-mcp-servers": "alias_1"
            }
        }
    ],
    "input": "Run available tools",
    "tool_choice": "required"
}'
```

In this example, the request will only have access to tools from the "alias\_1" MCP server.

### Grouping MCPs (Access Groups)[​](#grouping-mcps-access-groups "Direct link to Grouping MCPs (Access Groups)")

MCP Access Groups allow you to group multiple MCP servers together for easier management.

#### 1. Create an Access Group[​](#1-create-an-access-group "Direct link to 1. Create an Access Group")

##### A. Creating Access Groups using Config:[​](#a-creating-access-groups-using-config "Direct link to A. Creating Access Groups using Config:")

Creating access groups for MCP using the config

```
mcp_servers:
"deepwiki_mcp":
url: https://mcp.deepwiki.com/mcp
transport:"http"
auth_type:"none"
access_groups:["dev_group"]
```

While adding `mcp_servers` using the config:

- Pass in a list of strings inside `access_groups`
- These groups can then be used for segregating access using keys, teams and MCP clients using headers

##### B. Creating Access Groups using UI[​](#b-creating-access-groups-using-ui "Direct link to B. Creating Access Groups using UI")

To create an access group:

- Go to MCP Servers in the LiteLLM UI
- Click "Add a New MCP Server"
- Under "MCP Access Groups", create a new group (e.g., "dev\_group") by typing it
- Add the same group name to other servers to group them together

#### 2. Use Access Group in Cursor[​](#2-use-access-group-in-cursor "Direct link to 2. Use Access Group in Cursor")

Include the access group name in the `x-mcp-servers` header:

Cursor Configuration with Access Groups

```
{
"mcpServers":{
"LiteLLM":{
"url":"litellm_proxy",
"headers":{
"x-litellm-api-key":"Bearer $LITELLM_API_KEY",
"x-mcp-servers":"dev_group"
}
}
}
}
```

This gives you access to all servers in the "dev\_group" access group.

- Which means that if deepwiki server (and any other servers) which have the access group `dev_group` assigned to them will be available for tool calling

#### Advanced: Connecting Access Groups to API Keys[​](#advanced-connecting-access-groups-to-api-keys "Direct link to Advanced: Connecting Access Groups to API Keys")

When creating API keys, you can assign them to specific access groups for permission management:

- Go to "Keys" in the LiteLLM UI and click "Create Key"
- Select the desired MCP access groups from the dropdown
- The key will have access to all MCP servers in those groups
- This is reflected in the Test Key page

Control which tools different teams can access from the same MCP server. For example, give your Engineering team access to `list_repositories`, `create_issue`, and `search_code`, while Sales only gets `search_code` and `close_issue`.

This video shows how to set allowed tools for a Key, Team, or Organization.

## Dashboard View Modes[​](#dashboard-view-modes "Direct link to Dashboard View Modes")

Proxy admins can also control what non-admins see inside the MCP dashboard via `general_settings.user_mcp_management_mode`:

- `restricted` *(default)* – users only see servers that their team explicitly has access to.
- `view_all` – every dashboard user can see the full MCP server list.

Config example

```
general_settings:
user_mcp_management_mode: view_all
```

This is useful when you want discoverability for MCP offerings without granting additional execution privileges.

## Publish MCP Registry[​](#publish-mcp-registry "Direct link to Publish MCP Registry")

If you want other systems—for example external agent frameworks such as MCP-capable IDEs running outside your network—to automatically discover the MCP servers hosted on LiteLLM, you can expose a Model Context Protocol Registry endpoint. This registry lists the built-in LiteLLM MCP server and every server you have configured, using the [official MCP Registry spec](https://github.com/modelcontextprotocol/registry).

1. Set `enable_mcp_registry: true` under `general_settings` in your proxy config (or DB settings) and restart the proxy.
2. LiteLLM will serve the registry at `GET /v1/mcp/registry.json`.
3. Each entry points to either `/mcp` (built-in server) or `/{mcp_server_name}/mcp` for your custom servers, so clients can connect directly using the advertised Streamable HTTP URL.

Permissions still apply

The registry only advertises server URLs. Actual access control is still enforced by LiteLLM when the client connects to `/mcp` or `/{server}/mcp`, so publishing the registry does not bypass per-key permissions.