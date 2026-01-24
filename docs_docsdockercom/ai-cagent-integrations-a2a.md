---
title: A2A
url: https://docs.docker.com/ai/cagent/integrations/a2a/
source: llms
fetched_at: 2026-01-24T14:13:27.862091595-03:00
rendered_js: false
word_count: 371
summary: This document explains how to run a cagent agent as an HTTP server using A2A mode to enable discovery and interaction between different agents or systems. It provides instructions for starting the server, using JSON-RPC endpoints, and configuring multi-agent workflows.
tags:
    - cagent
    - a2a-mode
    - http-server
    - multi-agent-systems
    - json-rpc
    - agent-discovery
    - api-integration
category: guide
---

## A2A mode

Table of contents

* * *

A2A mode runs your cagent agent as an HTTP server that other systems can call using the Agent-to-Agent protocol. This lets you expose your agent as a service that other agents or applications can discover and invoke over the network.

Use A2A when you want to make your agent callable by other systems over HTTP. For editor integration, see [ACP integration](https://docs.docker.com/ai/cagent/integrations/acp/). For using agents as tools in MCP clients, see [MCP integration](https://docs.docker.com/ai/cagent/integrations/mcp/).

## [Prerequisites](#prerequisites)

Before starting an A2A server, you need:

- cagent installed - See the [installation guide](https://docs.docker.com/ai/cagent/#installation)
- Agent configuration - A YAML file defining your agent. See the [tutorial](https://docs.docker.com/ai/cagent/tutorial/)
- API keys configured - If using cloud model providers (see [Model providers](https://docs.docker.com/ai/cagent/model-providers/))

## [Starting an A2A server](#starting-an-a2a-server)

Basic usage:

```
$ cagent a2a ./agent.yaml
```

Your agent is now accessible via HTTP. Other A2A systems can discover your agent's capabilities and call it.

Custom port:

```
$ cagent a2a ./agent.yaml --port 8080
```

Specific agent in a team:

```
$ cagent a2a ./agent.yaml --agent engineer
```

From OCI registry:

```
$ cagent a2a agentcatalog/pirate --port 9000
```

## [HTTP endpoints](#http-endpoints)

When you start an A2A server, it exposes two HTTP endpoints:

### [Agent card: `/.well-known/agent-card`](#agent-card-well-knownagent-card)

The agent card describes your agent's capabilities:

```
$ curl http://localhost:8080/.well-known/agent-card
```

```
{
  "name": "agent",
  "description": "A helpful coding assistant",
  "skills": [
    {
      "id": "agent_root",
      "name": "root",
      "description": "A helpful coding assistant",
      "tags": ["llm", "cagent"]
    }
  ],
  "preferredTransport": "jsonrpc",
  "url": "http://localhost:8080/invoke",
  "capabilities": {
    "streaming": true
  },
  "version": "0.1.0"
}
```

### [Invoke endpoint: `/invoke`](#invoke-endpoint-invoke)

Call your agent by sending a JSON-RPC request:

```
$ curl -X POST http://localhost:8080/invoke \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": "req-1",
    "method": "message/send",
    "params": {
      "message": {
        "role": "user",
        "parts": [
          {
            "kind": "text",
            "text": "What is 2+2?"
          }
        ]
      }
    }
  }'
```

The response includes the agent's reply:

```
{
  "jsonrpc": "2.0",
  "id": "req-1",
  "result": {
    "artifacts": [
      {
        "parts": [
          {
            "kind": "text",
            "text": "2+2 equals 4."
          }
        ]
      }
    ]
  }
}
```

## [Example: Multi-agent workflow](#example-multi-agent-workflow)

Here's a concrete scenario where A2A is useful. You have two agents:

1. A general-purpose agent that interacts with users
2. A specialized code review agent with access to your codebase

Run the specialist as an A2A server:

```
$ cagent a2a ./code-reviewer.yaml --port 8080
Listening on 127.0.0.1:8080
```

Configure your main agent to call it:

```
agents:root:model:anthropic/claude-sonnet-4-5instruction:You are a helpful assistanttoolsets:- type:a2aurl:http://localhost:8080name:code-reviewer
```

Now when users ask the main agent about code quality, it can delegate to the specialist. The main agent sees `code-reviewer` as a tool it can call, and the specialist has access to the codebase tools it needs.

## [Calling other A2A agents](#calling-other-a2a-agents)

Your cagent agents can call remote A2A agents as tools. Configure the A2A toolset with the remote agent's URL:

```
agents:root:toolsets:- type:a2aurl:http://localhost:8080name:specialist
```

The `url` specifies where the remote agent is running, and `name` is an optional identifier for the tool. Your agent can now delegate tasks to the remote specialist agent.

If the remote agent requires authentication or custom headers:

```
agents:root:toolsets:- type:a2aurl:http://localhost:8080name:specialistremote:headers:Authorization:Bearer token123X-Custom-Header:value
```

## [What's next](#whats-next)

- Review the [CLI reference](https://docs.docker.com/ai/cagent/reference/cli/#a2a) for all `cagent a2a` options
- Learn about [MCP mode](https://docs.docker.com/ai/cagent/integrations/mcp/) to expose agents as tools in MCP clients
- Learn about [ACP mode](https://docs.docker.com/ai/cagent/integrations/acp/) for editor integration
- Share your agents with [OCI registries](https://docs.docker.com/ai/cagent/sharing-agents/)