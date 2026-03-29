---
title: Sharing agents
url: https://docs.docker.com/ai/cagent/sharing-agents/
source: llms
fetched_at: 2026-01-24T14:13:46.519020834-03:00
rendered_js: false
word_count: 179
summary: This document explains how to publish agent configurations to OCI-compatible registries and use them across different environments, including ACP and MCP integrations.
tags:
    - agent-registry
    - cagent-cli
    - agent-management
    - oci-registry
    - acp-integration
    - mcp-integration
    - version-control
category: guide
---

Table of contents

* * *

Push your agent to a registry and share it by name. Your teammates reference `agentcatalog/security-expert` instead of copying YAML files around or asking you where your agent configuration lives.

When you update the agent in the registry, everyone gets the new version the next time they pull or restart their client.

## [Prerequisites](#prerequisites)

To push agents to a registry, authenticate first:

For other registries, use their authentication method.

## [Publishing agents](#publishing-agents)

Push your agent configuration to a registry:

```
$ cagent push ./agent.yml myusername/agent-name
```

Push creates the repository if it doesn't exist yet. Use Docker Hub or any OCI-compatible registry.

Tag specific versions:

```
$ cagent push ./agent.yml myusername/agent-name:v1.0.0
$ cagent push ./agent.yml myusername/agent-name:latest
```

## [Using published agents](#using-published-agents)

Pull an agent to inspect it locally:

```
$ cagent pull agentcatalog/pirate
```

This saves the configuration as a local YAML file.

Run agents directly from the registry:

```
$ cagent run agentcatalog/pirate
```

Or reference it directly in integrations:

### [Editor integration (ACP)](#editor-integration-acp)

Use registry references in ACP configurations so your editor always uses the latest version:

```
{
  "agent_servers": {
    "myagent": {
      "command": "cagent",
      "args": ["acp", "agentcatalog/pirate"]
    }
  }
}
```

### [MCP client integration](#mcp-client-integration)

Agents can be exposed as tools in MCP clients:

```
{
  "mcpServers": {
    "myagent": {
      "command": "/usr/local/bin/cagent",
      "args": ["mcp", "agentcatalog/pirate"]
    }
  }
}
```

## [What's next](#whats-next)

- Set up [ACP integration](https://docs.docker.com/ai/cagent/integrations/acp/) with shared agents
- Configure [MCP integration](https://docs.docker.com/ai/cagent/integrations/mcp/) with shared agents
- Browse the [agent catalog](https://hub.docker.com/u/agentcatalog) for examples