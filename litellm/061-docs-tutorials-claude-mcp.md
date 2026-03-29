---
title: Use Claude Code with MCPs | liteLLM
url: https://docs.litellm.ai/docs/tutorials/claude_mcp
source: sitemap
fetched_at: 2026-01-21T19:55:06.123554678-03:00
rendered_js: false
word_count: 132
summary: This tutorial provides a step-by-step guide on connecting and authenticating Model Context Protocol (MCP) servers with Claude Code using the LiteLLM Proxy.
tags:
    - mcp
    - litellm-proxy
    - claude-code
    - oauth
    - server-integration
    - configuration
category: tutorial
---

This tutorial shows how to connect MCP servers to Claude Code via LiteLLM Proxy.

Note: LiteLLM supports OAuth for MCP servers as well. [Learn more](https://docs.litellm.ai/docs/mcp#mcp-oauth)

## Connecting MCP Servers[​](#connecting-mcp-servers "Direct link to Connecting MCP Servers")

You can also connect MCP servers to Claude Code via LiteLLM Proxy.

1. Add the MCP server to your `config.yaml`

<!--THE END-->

- GitHub MCP
- Atlassian MCP

In this example, we'll add the Github MCP server to our `config.yaml`

config.yaml

```
mcp_servers:
github_mcp:
url:"https://api.githubcopilot.com/mcp"
auth_type: oauth2
client_id: os.environ/GITHUB_OAUTH_CLIENT_ID
client_secret: os.environ/GITHUB_OAUTH_CLIENT_SECRET
```

2. Start LiteLLM Proxy

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

3. Use the MCP server in Claude Code

```
claude mcp add --transport http litellm_proxy http://0.0.0.0:4000/github_mcp/mcp --header "Authorization: Bearer sk-LITELLM_VIRTUAL_KEY"
```

For MCP servers that require dynamic client registration (such as Atlassian), please set `x-litellm-api-key: Bearer sk-LITELLM_VIRTUAL_KEY` instead of using `Authorization: Bearer LITELLM_VIRTUAL_KEY`.

4. Authenticate via Claude Code

a. Start Claude Code

b. Authenticate via Claude Code

c. Select the MCP server

d. Start Oauth flow via Claude Code

```
> 1. Authenticate
 2. Reconnect
 3. Disable             
```

e. Once completed, you should see this success message: