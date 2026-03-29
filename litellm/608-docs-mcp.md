---
title: MCP Overview | liteLLM
url: https://docs.litellm.ai/docs/mcp
source: sitemap
fetched_at: 2026-01-21T19:45:40.500663191-03:00
rendered_js: false
word_count: 2343
summary: This document explains how to configure and use LiteLLM Proxy as an MCP Gateway to manage tools and servers via various transports and OpenAPI specifications.
tags:
    - litellm-proxy
    - mcp-gateway
    - model-context-protocol
    - openapi-integration
    - oauth-configuration
    - server-management
category: guide
---

LiteLLM Proxy provides an MCP Gateway that allows you to use a fixed endpoint for all MCP tools and control MCP access by Key, Team.

LiteLLM MCP Architecture: Use MCP tools with all LiteLLM supported models

## Overview[​](#overview "Direct link to Overview")

FeatureDescriptionMCP Operations• List Tools  
• Call Tools  
• Prompts  
• ResourcesSupported MCP Transports• Streamable HTTP  
• SSE  
• Standard Input/Output (stdio)LiteLLM Permission Management• By Key  
• By Team  
• By Organization

MCP protocol update

Starting in LiteLLM v1.80.18, the LiteLLM MCP protocol version is `2025-11-25`.  
LiteLLM namespaces multiple MCP servers by prefixing each tool name with its MCP server name, so newly created servers now must use names that comply with SEP-986—noncompliant names cannot be added anymore. Existing servers that still violate SEP-986 only emit warnings today, but future MCP-side rollouts may block those names entirely, so we recommend updating any legacy server names proactively before MCP enforcement makes them unusable.

## Adding your MCP[​](#adding-your-mcp "Direct link to Adding your MCP")

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

To store MCP servers in the database, you need to enable database storage:

**Environment Variable:**

```
export STORE_MODEL_IN_DB=True
```

**OR in config.yaml:**

```
general_settings:
store_model_in_db:true
```

#### Fine-grained Database Storage Control[​](#fine-grained-database-storage-control "Direct link to Fine-grained Database Storage Control")

By default, when `store_model_in_db` is `true`, all object types (models, MCPs, guardrails, vector stores, etc.) are stored in the database. If you want to store only specific object types, use the `supported_db_objects` setting.

**Example: Store only MCP servers in the database**

config.yaml

```
general_settings:
store_model_in_db:true
supported_db_objects:["mcp"]# Only store MCP servers in DB

model_list:
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_key: sk-xxxxxxx
```

**See all available object types:** [Config Settings - supported\_db\_objects](https://docs.litellm.ai/docs/proxy/config_settings#general_settings---reference)

If `supported_db_objects` is not set, all object types are loaded from the database (default behavior).

For diagnosing connectivity problems after setup, see the [MCP Troubleshooting Guide](https://docs.litellm.ai/docs/mcp_troubleshoot).

- LiteLLM UI
- config.yaml

On the LiteLLM UI, Navigate to "MCP Servers" and click "Add New MCP Server".

On this form, you should enter your MCP Server URL and the transport you want to use.

LiteLLM supports the following MCP transports:

- Streamable HTTP
- SSE (Server-Sent Events)
- Standard Input/Output (stdio)

### Add HTTP MCP Server[​](#add-http-mcp-server "Direct link to Add HTTP MCP Server")

This video walks through adding and using an HTTP MCP server on LiteLLM UI and using it in Cursor IDE.

### Add SSE MCP Server[​](#add-sse-mcp-server "Direct link to Add SSE MCP Server")

This video walks through adding and using an SSE MCP server on LiteLLM UI and using it in Cursor IDE.

### Add STDIO MCP Server[​](#add-stdio-mcp-server "Direct link to Add STDIO MCP Server")

For stdio MCP servers, select "Standard Input/Output (stdio)" as the transport type and provide the stdio configuration in JSON format:

### OAuth Configuration & Overrides[​](#oauth-configuration--overrides "Direct link to OAuth Configuration & Overrides")

LiteLLM attempts [OAuth 2.0 Authorization Server Discovery](https://datatracker.ietf.org/doc/html/rfc8414) by default. When you create an MCP server in the UI and set `Authentication: OAuth`, LiteLLM will locate the provider metadata, dynamically register a client, and perform PKCE-based authorization without you providing any additional details.

**Customize the OAuth flow when needed:**

- **Provide explicit client credentials** – If the MCP provider does not offer dynamic client registration or you prefer to manage the client yourself, fill in `client_id`, `client_secret`, and the desired `scopes`.
- **Override discovery URLs** – In some environments, LiteLLM might not be able to reach the provider's metadata endpoints. Use the optional `authorization_url`, `token_url`, and `registration_url` fields to point LiteLLM directly to the correct endpoints.

Sometimes your MCP server needs specific headers on every request. Maybe it's an API key, maybe it's a custom header the server expects. Instead of configuring auth, you can just set them directly.

These headers get sent with every request to the server. That's it.

**When to use this:**

- Your server needs custom headers that don't fit the standard auth patterns
- You want full control over exactly what headers are sent
- You're debugging and need to quickly add headers without changing auth configuration

## Converting OpenAPI Specs to MCP Servers[​](#converting-openapi-specs-to-mcp-servers "Direct link to Converting OpenAPI Specs to MCP Servers")

LiteLLM can automatically convert OpenAPI specifications into MCP servers, allowing you to expose any REST API as MCP tools. This is useful when you have existing APIs with OpenAPI/Swagger documentation and want to make them available as MCP tools.

**Benefits:**

- **Rapid Integration**: Convert existing APIs to MCP tools without writing custom MCP server code
- **Automatic Tool Generation**: LiteLLM automatically generates MCP tools from your OpenAPI spec
- **Unified Interface**: Use the same MCP interface for both native MCP servers and OpenAPI-based APIs
- **Easy Testing**: Test and iterate on API integrations quickly

**Configuration:**

Add your OpenAPI-based MCP server to your `config.yaml`:

config.yaml - OpenAPI to MCP

```
model_list:
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_key: sk-xxxxxxx

mcp_servers:
# OpenAPI Spec Example - Petstore API
petstore_mcp:
url:"https://petstore.swagger.io/v2"
spec_path:"/path/to/openapi.json"
auth_type:"none"

# OpenAPI Spec with API Key Authentication
my_api_mcp:
url:"http://0.0.0.0:8090"
spec_path:"/path/to/openapi.json"
auth_type:"api_key"
auth_value:"your-api-key-here"

# OpenAPI Spec with Bearer Token
secured_api_mcp:
url:"https://api.example.com"
spec_path:"/path/to/openapi.json"
auth_type:"bearer_token"
auth_value:"your-bearer-token"
```

**Configuration Parameters:**

ParameterRequiredDescription`url`YesThe base URL of your API endpoint`spec_path`YesPath or URL to your OpenAPI specification file (JSON or YAML)`auth_type`NoAuthentication type: `none`, `api_key`, `bearer_token`, `basic`, `authorization``auth_value`NoAuthentication value (required if `auth_type` is set)`authorization_url`NoFor `auth_type: oauth2`. Optional override; if omitted LiteLLM auto-discovers it.`token_url`NoFor `auth_type: oauth2`. Optional override; if omitted LiteLLM auto-discovers it.`registration_url`NoFor `auth_type: oauth2`. Optional override; if omitted LiteLLM auto-discovers it.`scopes`NoFor `auth_type: oauth2`. Optional override; if omitted LiteLLM uses the scopes advertised by the server.`description`NoOptional description for the MCP server`allowed_tools`NoList of specific tools to allow (see [MCP Tool Filtering](#mcp-tool-filtering))`disallowed_tools`NoList of specific tools to block (see [MCP Tool Filtering](#mcp-tool-filtering))

### Usage Example[​](#usage-example "Direct link to Usage Example")

Once configured, you can use the OpenAPI-based MCP server just like any other MCP server:

- Python FastMCP
- Cursor IDE
- OpenAI Responses API

Using OpenAPI-based MCP Server

```
from fastmcp import Client
import asyncio

# Standard MCP configuration
config ={
"mcpServers":{
"petstore":{
"url":"http://localhost:4000/petstore_mcp/mcp",
"headers":{
"x-litellm-api-key":"Bearer sk-1234"
}
}
}
}

# Create a client that connects to the server
client = Client(config)

asyncdefmain():
asyncwith client:
# List available tools generated from OpenAPI spec
        tools =await client.list_tools()
print(f"Available tools: {[tool.name for tool in tools]}")

# Example: Get a pet by ID (from Petstore API)
        response =await client.call_tool(
            name="getpetbyid",
            arguments={"petId":"1"}
)
print(f"Response:\n{response}\n")

# Example: Find pets by status
        response =await client.call_tool(
            name="findpetsbystatus",
            arguments={"status":"available"}
)
print(f"Response:\n{response}\n")

if __name__ =="__main__":
    asyncio.run(main())
```

**How It Works**

1. **Spec Loading**: LiteLLM loads your OpenAPI specification from the provided `spec_path`
2. **Tool Generation**: Each API endpoint in the spec becomes an MCP tool
3. **Parameter Mapping**: OpenAPI parameters are automatically mapped to MCP tool parameters
4. **Request Handling**: When a tool is called, LiteLLM converts the MCP request to the appropriate HTTP request
5. **Response Translation**: API responses are converted back to MCP format

**OpenAPI Spec Requirements**

Your OpenAPI specification should follow standard OpenAPI/Swagger conventions:

- **Supported versions**: OpenAPI 3.0.x, OpenAPI 3.1.x, Swagger 2.0
- **Required fields**: `paths`, `info` sections should be properly defined
- **Operation IDs**: Each operation should have a unique `operationId` (this becomes the tool name)
- **Parameters**: Request parameters should be properly documented with types and descriptions

## MCP Oauth[​](#mcp-oauth "Direct link to MCP Oauth")

LiteLLM v 1.77.6 added support for OAuth 2.0 Client Credentials for MCP servers.

You can configure this either in `config.yaml` or directly from the LiteLLM UI (MCP Servers → Authentication → OAuth).

```
mcp_servers:
github_mcp:
url:"https://api.githubcopilot.com/mcp"
auth_type: oauth2
client_id: os.environ/GITHUB_OAUTH_CLIENT_ID
client_secret: os.environ/GITHUB_OAUTH_CLIENT_SECRET
```

[**See Claude Code Tutorial**](https://docs.litellm.ai/docs/tutorials/claude_responses_api#connecting-mcp-servers)

### How It Works[​](#how-it-works "Direct link to How It Works")

**Participants**

- **Client** – The MCP-capable AI agent (e.g., Claude Code, Cursor, or another IDE/agent) that initiates OAuth discovery, authorization, and tool invocations on behalf of the user.
- **LiteLLM Proxy** – Mediates all OAuth discovery, registration, token exchange, and MCP traffic while protecting stored credentials.
- **Authorization Server** – Issues OAuth 2.0 tokens via dynamic client registration, PKCE authorization, and token endpoints.
- **MCP Server (Resource Server)** – The protected MCP endpoint that receives LiteLLM’s authenticated JSON-RPC requests.
- **User-Agent (Browser)** – Temporarily involved so the end user can grant consent during the authorization step.

**Flow Steps**

1. **Resource Discovery**: The client fetches MCP resource metadata from LiteLLM’s `.well-known/oauth-protected-resource` endpoint to understand scopes and capabilities.
2. **Authorization Server Discovery**: The client retrieves the OAuth server metadata (token endpoint, authorization endpoint, supported PKCE methods) through LiteLLM’s `.well-known/oauth-authorization-server` endpoint.
3. **Dynamic Client Registration**: The client registers through LiteLLM, which forwards the request to the authorization server (RFC 7591). If the provider doesn’t support dynamic registration, you can pre-store `client_id`/`client_secret` in LiteLLM (e.g., GitHub MCP) and the flow proceeds the same way.
4. **User Authorization**: The client launches a browser session (with code challenge and resource hints). The user approves access, the authorization server sends the code through LiteLLM back to the client.
5. **Token Exchange**: The client calls LiteLLM with the authorization code, code verifier, and resource. LiteLLM exchanges them with the authorization server and returns the issued access/refresh tokens.
6. **MCP Invocation**: With a valid token, the client sends the MCP JSON-RPC request (plus LiteLLM API key) to LiteLLM, which forwards it to the MCP server and relays the tool response.

See the official [MCP Authorization Flow](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization#authorization-flow-steps) for additional reference.

LiteLLM supports forwarding additional custom headers from MCP clients to backend MCP servers using the `extra_headers` configuration parameter. This allows you to pass custom authentication tokens, API keys, or other headers that your MCP server requires.

**Configuration**

- config.yaml
- Dynamically on Client Side

Configure `extra_headers` in your MCP server configuration to specify which header names should be forwarded:

config.yaml with extra\_headers

```
mcp_servers:
github_mcp:
url:"https://api.githubcopilot.com/mcp"
auth_type:"bearer_token"
auth_value:"ghp_default_token"
extra_headers:["custom_key","x-custom-header","Authorization"]
description:"GitHub MCP server with custom header forwarding"
```

#### Client Usage[​](#client-usage "Direct link to Client Usage")

When connecting from MCP clients, include the custom headers that match the `extra_headers` configuration:

- Python FastMCP
- Cursor IDE
- HTTP Client

FastMCP Client with Custom Headers

```
from fastmcp import Client
import asyncio

# MCP client configuration with custom headers
config ={
"mcpServers":{
"github":{
"url":"http://localhost:4000/github_mcp/mcp",
"headers":{
"x-litellm-api-key":"Bearer sk-1234",
"Authorization":"Bearer gho_token",
"custom_key":"custom_value",
"x-custom-header":"additional_data"
}
}
}
}

# Create a client that connects to the server
client = Client(config)

asyncdefmain():
asyncwith client:
# List available tools
        tools =await client.list_tools()
print(f"Available tools: {tools}")

# Call a tool if available
if tools:
            result =await client.call_tool(tools[0].name,{})
print(f"Tool result: {result}")

# Run the client
asyncio.run(main())
```

#### How It Works[​](#how-it-works-1 "Direct link to How It Works")

1. **Configuration**: Define `extra_headers` in your MCP server config with the header names you want to forward
2. **Client Headers**: Include the corresponding headers in your MCP client requests
3. **Header Forwarding**: LiteLLM automatically forwards matching headers to the backend MCP server
4. **Authentication**: The backend MCP server receives both the configured auth headers and the custom headers

If your stdio MCP server needs per-request credentials, you can map HTTP headers from the client request directly into the environment for the launched stdio process. Reference the header name in the env value using the `${X-HEADER_NAME}` syntax. LiteLLM will read that header from the incoming request and set the env var before starting the command.

Forward X-GITHUB\_PERSONAL\_ACCESS\_TOKEN header to stdio env

```
{
"mcpServers":{
"github":{
"command":"docker",
"args":[
"run",
"-i",
"--rm",
"-e",
"GITHUB_PERSONAL_ACCESS_TOKEN",
"ghcr.io/github/github-mcp-server"
],
"env":{
"GITHUB_PERSONAL_ACCESS_TOKEN":"${X-GITHUB_PERSONAL_ACCESS_TOKEN}"
}
}
}
}
```

In this example, when a client makes a request with the `X-GITHUB_PERSONAL_ACCESS_TOKEN` header, the proxy forwards that value into the stdio process as the `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable.

## Using your MCP with client side credentials[​](#using-your-mcp-with-client-side-credentials "Direct link to Using your MCP with client side credentials")

Use this if you want to pass a client side authentication token to LiteLLM to then pass to your MCP to auth to your MCP.

You can specify MCP auth tokens using server-specific headers in the format `x-mcp-{server_alias}-{header_name}`. This allows you to use different authentication for different MCP servers.

**Benefits:**

- **Server-specific authentication**: Each MCP server can use different auth methods
- **Better security**: No need to share the same auth token across all servers
- **Flexible header names**: Support for different auth header types (authorization, x-api-key, etc.)
- **Clean separation**: Each server's auth is clearly identified

You can also specify your MCP auth token using the header `x-mcp-auth`. This will be forwarded to all MCP servers and is deprecated in favor of server-specific headers.

- OpenAI API
- LiteLLM Proxy
- Cursor IDE
- Streamable HTTP
- Python FastMCP

#### Connect via OpenAI Responses API with Server-Specific Auth[​](#connect-via-openai-responses-api-with-server-specific-auth "Direct link to Connect via OpenAI Responses API with Server-Specific Auth")

Use the OpenAI Responses API and include server-specific auth headers:

cURL Example with Server-Specific Auth

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
            "server_url": "litellm_proxy",
            "require_approval": "never",
            "headers": {
                "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY",
                "x-mcp-github-authorization": "Bearer YOUR_GITHUB_TOKEN",
                "x-mcp-zapier-x-api-key": "YOUR_ZAPIER_API_KEY"
            }
        }
    ],
    "input": "Run available tools",
    "tool_choice": "required"
}'
```

#### Connect via OpenAI Responses API with Legacy Auth[​](#connect-via-openai-responses-api-with-legacy-auth "Direct link to Connect via OpenAI Responses API with Legacy Auth")

Use the OpenAI Responses API and include the `x-mcp-auth` header for your MCP server authentication:

cURL Example with Legacy MCP Auth

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
            "server_url": "litellm_proxy",
            "require_approval": "never",
            "headers": {
                "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY",
                "x-mcp-auth": YOUR_MCP_AUTH_TOKEN
            }
        }
    ],
    "input": "Run available tools",
    "tool_choice": "required"
}'
```

By default, LiteLLM uses `x-mcp-auth` to pass your credentials to MCP servers. You can change this header name in one of the following ways:

1. Set the `LITELLM_MCP_CLIENT_SIDE_AUTH_HEADER_NAME` environment variable

Environment Variable

```
export LITELLM_MCP_CLIENT_SIDE_AUTH_HEADER_NAME="authorization"
```

2. Set the `mcp_client_side_auth_header_name` in the general settings on the config.yaml file

config.yaml

```
model_list:
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_key: sk-xxxxxxx

general_settings:
mcp_client_side_auth_header_name:"authorization"
```

In this example the `authorization` header will be passed to the MCP server for authentication.

cURL with authorization header

```
curl --location '<your-litellm-proxy-base-url>/v1/responses' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $LITELLM_API_KEY" \
--data '{
    "model": "gpt-4o",
    "tools": [
        {
            "type": "mcp",
            "server_label": "litellm",
            "server_url": "litellm_proxy",
            "require_approval": "never",
            "headers": {
                "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY",
                "authorization": "Bearer sk-zapier-token-123"
            }
        }
    ],
    "input": "Run available tools",
    "tool_choice": "required"
}'
```

Works with all providers

This flow is **provider-agnostic**: the same MCP tool definition works for *every* LLM backend behind LiteLLM (OpenAI, Azure OpenAI, Anthropic, Amazon Bedrock, Vertex, self-hosted deployments, etc.).

LiteLLM Proxy also supports MCP-aware tooling on the classic `/v1/chat/completions` endpoint. Provide the MCP tool definition directly in the `tools` array and LiteLLM will fetch and transform the MCP server's tools into OpenAI-compatible function calls. When `require_approval` is set to `"never"`, the proxy automatically executes the returned tool calls and feeds the results back into the model before returning the assistant response.

Chat Completions with MCP Tools

```
curl --location '<your-litellm-proxy-base-url>/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $LITELLM_API_KEY" \
--data '{
  "model": "gpt-4o-mini",
  "messages": [
    {"role": "user", "content": "Summarize the latest open PR."}
  ],
  "tools": [
    {
      "type": "mcp",
      "server_url": "litellm_proxy/mcp/github",
      "server_label": "github_mcp",
      "require_approval": "never"
    }
  ]
}'
```

If you omit `require_approval` or set it to any value other than `"never"`, the MCP tool calls are returned to the client so that you can review and execute them manually, matching the upstream OpenAI behavior.

## LiteLLM Proxy - Walk through MCP Gateway[​](#litellm-proxy---walk-through-mcp-gateway "Direct link to LiteLLM Proxy - Walk through MCP Gateway")

LiteLLM exposes an MCP Gateway for admins to add all their MCP servers to LiteLLM. The key benefits of using LiteLLM Proxy with MCP are:

1. Use a fixed endpoint for all MCP tools
2. MCP Permission management by Key, Team, or User

This video demonstrates how you can onboard an MCP server to LiteLLM Proxy, use it and set access controls.

## LiteLLM Python SDK MCP Bridge[​](#litellm-python-sdk-mcp-bridge "Direct link to LiteLLM Python SDK MCP Bridge")

LiteLLM Python SDK acts as a MCP bridge to utilize MCP tools with all LiteLLM supported models. LiteLLM offers the following features for using MCP

- **List** Available MCP Tools: OpenAI clients can view all available MCP tools
  
  - `litellm.experimental_mcp_client.load_mcp_tools` to list all available MCP tools
- **Call** MCP Tools: OpenAI clients can call MCP tools
  
  - `litellm.experimental_mcp_client.call_openai_tool` to call an OpenAI tool on an MCP server

### 1. List Available MCP Tools[​](#1-list-available-mcp-tools "Direct link to 1. List Available MCP Tools")

In this example we'll use `litellm.experimental_mcp_client.load_mcp_tools` to list all available MCP tools on any MCP server. This method can be used in two ways:

- `format="mcp"` - (default) Return MCP tools
  
  - Returns: `mcp.types.Tool`
- `format="openai"` - Return MCP tools converted to OpenAI API compatible tools. Allows using with OpenAI endpoints.
  
  - Returns: `openai.types.chat.ChatCompletionToolParam`

<!--THE END-->

- LiteLLM Python SDK
- OpenAI SDK + LiteLLM Proxy

MCP Client List Tools

```
# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import os
import litellm
from litellm import experimental_mcp_client


server_params = StdioServerParameters(
    command="python3",
# Make sure to update to the full absolute path to your mcp_server.py file
    args=["./mcp_server.py"],
)

asyncwith stdio_client(server_params)as(read, write):
asyncwith ClientSession(read, write)as session:
# Initialize the connection
await session.initialize()

# Get tools
        tools =await experimental_mcp_client.load_mcp_tools(session=session,format="openai")
print("MCP TOOLS: ", tools)

        messages =[{"role":"user","content":"what's (3 + 5)"}]
        llm_response =await litellm.acompletion(
            model="gpt-4o",
            api_key=os.getenv("OPENAI_API_KEY"),
            messages=messages,
            tools=tools,
)
print("LLM RESPONSE: ", json.dumps(llm_response, indent=4, default=str))
```

### 2. List and Call MCP Tools[​](#2-list-and-call-mcp-tools "Direct link to 2. List and Call MCP Tools")

In this example we'll use

- `litellm.experimental_mcp_client.load_mcp_tools` to list all available MCP tools on any MCP server
- `litellm.experimental_mcp_client.call_openai_tool` to call an OpenAI tool on an MCP server

The first llm response returns a list of OpenAI tools. We take the first tool call from the LLM response and pass it to `litellm.experimental_mcp_client.call_openai_tool` to call the tool on the MCP server.

#### How `litellm.experimental_mcp_client.call_openai_tool` works[​](#how-litellmexperimental_mcp_clientcall_openai_tool-works "Direct link to how-litellmexperimental_mcp_clientcall_openai_tool-works")

- Accepts an OpenAI Tool Call from the LLM response
- Converts the OpenAI Tool Call to an MCP Tool
- Calls the MCP Tool on the MCP server
- Returns the result of the MCP Tool call

<!--THE END-->

- LiteLLM Python SDK
- OpenAI SDK + LiteLLM Proxy

MCP Client List and Call Tools

```
# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import os
import litellm
from litellm import experimental_mcp_client


server_params = StdioServerParameters(
    command="python3",
# Make sure to update to the full absolute path to your mcp_server.py file
    args=["./mcp_server.py"],
)

asyncwith stdio_client(server_params)as(read, write):
asyncwith ClientSession(read, write)as session:
# Initialize the connection
await session.initialize()

# Get tools
        tools =await experimental_mcp_client.load_mcp_tools(session=session,format="openai")
print("MCP TOOLS: ", tools)

        messages =[{"role":"user","content":"what's (3 + 5)"}]
        llm_response =await litellm.acompletion(
            model="gpt-4o",
            api_key=os.getenv("OPENAI_API_KEY"),
            messages=messages,
            tools=tools,
)
print("LLM RESPONSE: ", json.dumps(llm_response, indent=4, default=str))

        openai_tool = llm_response["choices"][0]["message"]["tool_calls"][0]
# Call the tool using MCP client
        call_result =await experimental_mcp_client.call_openai_tool(
            session=session,
            openai_tool=openai_tool,
)
print("MCP TOOL CALL RESULT: ", call_result)

# send the tool result to the LLM
        messages.append(llm_response["choices"][0]["message"])
        messages.append(
{
"role":"tool",
"content":str(call_result.content[0].text),
"tool_call_id": openai_tool["id"],
}
)
print("final messages with tool result: ", messages)
        llm_response =await litellm.acompletion(
            model="gpt-4o",
            api_key=os.getenv("OPENAI_API_KEY"),
            messages=messages,
            tools=tools,
)
print(
"FINAL LLM RESPONSE: ", json.dumps(llm_response, indent=4, default=str)
)
```

## FAQ[​](#faq "Direct link to FAQ")

**Q: How do I use OAuth2 client\_credentials (machine-to-machine) with MCP servers behind LiteLLM?**

At the moment LiteLLM only forwards whatever `Authorization` header/value you configure for the MCP server; it does not issue OAuth2 tokens by itself. If your MCP requires the Client Credentials grant, obtain the access token directly from the authorization server and set that bearer token as the MCP server’s Authorization header value. LiteLLM does not yet fetch or refresh those machine-to-machine tokens on your behalf, but we plan to add first-class client\_credentials support in a future release so the proxy can manage those tokens automatically.

**Q: When I fetch an OAuth token from the LiteLLM UI, where is it stored?**

The UI keeps only transient state in `sessionStorage` so the OAuth redirect flow can finish; the token is not persisted in the server or database.

**Q: I'm seeing MCP connection errors—what should I check?**

Walk through the [MCP Troubleshooting Guide](https://docs.litellm.ai/docs/mcp_troubleshoot) for step-by-step isolation (Client → LiteLLM vs. LiteLLM → MCP), log examples, and verification methods like MCP Inspector and `curl`.