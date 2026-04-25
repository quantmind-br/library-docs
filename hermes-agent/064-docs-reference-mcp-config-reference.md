---
title: MCP Config Reference | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference
source: crawler
fetched_at: 2026-04-24T17:00:20.57714142-03:00
rendered_js: false
word_count: 423
summary: This document serves as a reference guide detailing the structure and configuration options for Model Context Protocol (MCP) servers within Hermes, explaining how to define connections, filter tools using include/exclude semantics, and handle various connection behaviors like OAuth authentication.
tags:
    - mcp-reference
    - config-guide
    - server-keys
    - tool-filtering
    - oauth-2.1
    - protocol-definition
category: reference
---

This page is the compact reference companion to the main MCP docs.

For conceptual guidance, see:

- [MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- [Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)

## Root config shape[​](#root-config-shape "Direct link to Root config shape")

```yaml
mcp_servers:
<server_name>:
command:"..."# stdio servers
args:[]
env:{}

# OR
url:"..."# HTTP servers
headers:{}

enabled:true
timeout:120
connect_timeout:60
tools:
include:[]
exclude:[]
resources:true
prompts:true
```

## Server keys[​](#server-keys "Direct link to Server keys")

KeyTypeApplies toMeaning`command`stringstdioExecutable to launch`args`liststdioArguments for the subprocess`env`mappingstdioEnvironment passed to the subprocess`url`stringHTTPRemote MCP endpoint`headers`mappingHTTPHeaders for remote server requests`enabled`boolbothSkip the server entirely when false`timeout`numberbothTool call timeout`connect_timeout`numberbothInitial connection timeout`tools`mappingbothFiltering and utility-tool policy`auth`stringHTTPAuthentication method. Set to `oauth` to enable OAuth 2.1 with PKCE`sampling`mappingbothServer-initiated LLM request policy (see MCP guide)

KeyTypeMeaning`include`string or listWhitelist server-native MCP tools`exclude`string or listBlacklist server-native MCP tools`resources`bool-likeEnable/disable `list_resources` + `read_resource``prompts`bool-likeEnable/disable `list_prompts` + `get_prompt`

## Filtering semantics[​](#filtering-semantics "Direct link to Filtering semantics")

### `include`[​](#include "Direct link to include")

If `include` is set, only those server-native MCP tools are registered.

```yaml
tools:
include:[create_issue, list_issues]
```

### `exclude`[​](#exclude "Direct link to exclude")

If `exclude` is set and `include` is not, every server-native MCP tool except those names is registered.

```yaml
tools:
exclude:[delete_customer]
```

### Precedence[​](#precedence "Direct link to Precedence")

If both are set, `include` wins.

```yaml
tools:
include:[create_issue]
exclude:[create_issue, delete_issue]
```

Result:

- `create_issue` is still allowed
- `delete_issue` is ignored because `include` takes precedence

Hermes may register these utility wrappers per MCP server:

Resources:

- `list_resources`
- `read_resource`

Prompts:

- `list_prompts`
- `get_prompt`

### Disable resources[​](#disable-resources "Direct link to Disable resources")

### Disable prompts[​](#disable-prompts "Direct link to Disable prompts")

### Capability-aware registration[​](#capability-aware-registration "Direct link to Capability-aware registration")

Even when `resources: true` or `prompts: true`, Hermes only registers those utility tools if the MCP session actually exposes the corresponding capability.

So this is normal:

- you enable prompts
- but no prompt utilities appear
- because the server does not support prompts

## `enabled: false`[​](#enabled-false "Direct link to enabled-false")

```yaml
mcp_servers:
legacy:
url:"https://mcp.legacy.internal"
enabled:false
```

Behavior:

- no connection attempt
- no discovery
- no tool registration
- config remains in place for later reuse

## Empty result behavior[​](#empty-result-behavior "Direct link to Empty result behavior")

If filtering removes all server-native tools and no utility tools are registered, Hermes does not create an empty MCP runtime toolset for that server.

## Example configs[​](#example-configs "Direct link to Example configs")

### Safe GitHub allowlist[​](#safe-github-allowlist "Direct link to Safe GitHub allowlist")

```yaml
mcp_servers:
github:
command:"npx"
args:["-y","@modelcontextprotocol/server-github"]
env:
GITHUB_PERSONAL_ACCESS_TOKEN:"***"
tools:
include:[list_issues, create_issue, update_issue, search_code]
resources:false
prompts:false
```

### Stripe blacklist[​](#stripe-blacklist "Direct link to Stripe blacklist")

```yaml
mcp_servers:
stripe:
url:"https://mcp.stripe.com"
headers:
Authorization:"Bearer ***"
tools:
exclude:[delete_customer, refund_payment]
```

### Resource-only docs server[​](#resource-only-docs-server "Direct link to Resource-only docs server")

```yaml
mcp_servers:
docs:
url:"https://mcp.docs.example.com"
tools:
include:[]
resources:true
prompts:false
```

## Reloading config[​](#reloading-config "Direct link to Reloading config")

After changing MCP config, reload servers with:

Server-native MCP tools become:

Examples:

- `mcp_github_create_issue`
- `mcp_filesystem_read_file`
- `mcp_my_api_query_data`

Utility tools follow the same prefixing pattern:

- `mcp_<server>_list_resources`
- `mcp_<server>_read_resource`
- `mcp_<server>_list_prompts`
- `mcp_<server>_get_prompt`

### Name sanitization[​](#name-sanitization "Direct link to Name sanitization")

Hyphens (`-`) and dots (`.`) in both server names and tool names are replaced with underscores before registration. This ensures tool names are valid identifiers for LLM function-calling APIs.

For example, a server named `my-api` exposing a tool called `list-items.v2` becomes:

Keep this in mind when writing `include` / `exclude` filters — use the **original** MCP tool name (with hyphens/dots), not the sanitized version.

## OAuth 2.1 authentication[​](#oauth-21-authentication "Direct link to OAuth 2.1 authentication")

For HTTP servers that require OAuth, set `auth: oauth` on the server entry:

```yaml
mcp_servers:
protected_api:
url:"https://mcp.example.com/mcp"
auth: oauth
```

Behavior:

- Hermes uses the MCP SDK's OAuth 2.1 PKCE flow (metadata discovery, dynamic client registration, token exchange, and refresh)
- On first connect, a browser window opens for authorization
- Tokens are persisted to `~/.hermes/mcp-tokens/<server>.json` and reused across sessions
- Token refresh is automatic; re-authorization only happens when refresh fails
- Only applies to HTTP/StreamableHTTP transport (`url`-based servers)