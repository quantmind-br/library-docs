---
title: MCP Permissions
url: https://ampcode.com/news/mcp-permissions
source: crawler
fetched_at: 2026-02-06T02:08:33.832361782-03:00
rendered_js: false
word_count: 77
summary: This document explains how to configure rule-based permissions for Model Context Protocol (MCP) servers using the amp.mcpPermissions setting to allow or block specific commands and URLs.
tags:
    - mcp-permissions
    - model-context-protocol
    - security-rules
    - configuration-settings
    - access-control
category: configuration
---

The setting `amp.mcpPermissions` defines rules that block or allow MCP servers.

MCP permissions are evaluated using a rule-based system with the same pattern matching syntax that is used for [tool permissions](https://ampcode.com/manual#permissions). The first matching rule determines the action. If no rules match, the MCP server is allowed by default.

The following configuration would block all MCP servers except locally-executed servers from the `@modelcontextprotocol` npm organization and remote servers from `trusted-service.com`:

```
{
	"amp.mcpPermissions": [
		{
			"matches": { "command": "npx @modelcontextprotocol/server-*" },
			"action": "allow"
		},
		{
			"matches": { "url": "https://trusted-service.com/mcp/*" },
			"action": "allow"
		},
		{
			"matches": { "url": "*" },
			"action": "reject"
		}
		{
			"matches": { "command": "*" },
			"action": "reject"
		}
	]
}
```

Read more about `amp.mcpPermissions` in [the manual.](https://ampcode.com/manual?internal#core-settings)