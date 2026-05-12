---
title: "MCP Integration in ForgeCode"
url: https://forgecode.dev/docs/mcp-integration/
source: sitemap
fetched_at: 2026-04-30T14:09:12.662968235-03:00
rendered_js: false
word_count: 248
summary: "Manage MCP servers in ForgeCode for external tool/API integration, browser automation, and development workflows."
tags:
  - mcp
  - forgecode
  - cli-reference
  - agent-integration
  - server-configuration
category: reference
optimized: true
---
# MCP Integration in ForgeCode

> **TL;DR**
> Use MCP to connect agents to external tools, APIs, and services.

## Key Features
- **External APIs**: Call web services.
- **Browser Automation**: Script UI interactions.
- **Dev Tools**: Integrate databases, schema tools.

## Commands

| Command | Purpose |
|---------|---------|
| `forge mcp import` | Add servers from JSON |
| `forge mcp list` | List configured servers |
| `forge mcp show` | Show server config |
| `forge mcp remove` | Remove a server |
| `forge mcp reload` | Reload after manual edits |

## Configuration

### File Locations
- **Local**: `.mcp.json` (project)
- **User**: Global ForgeCode config

> **Precedence**: Local > User.

### Server Types

#### Command-Based
```json
{
  "name": "browser",
  "type": "command",
  "command": ["playwright", "run-server", "--port=3000"],
  "env": {"PLAYWRIGHT_BROWSERS_PATH": "/opt/browsers"}
}
```

#### URL-Based
```json
{
  "name": "api",
  "type": "url",
  "url": "https://api.example.com/mcp"
}
```

### Disabling Servers
```json
{"disable": true}
```

## Usage

1. **Add Server**:
   ```bash
   forge mcp import '{"name":"api","type":"url","url":"https://api.example.com"}'
   ```

2. **Verify**:
   ```bash
   forge mcp list
   :tools  # In ForgeCode
   ```

3. **Use Tools**: Call MCP tools in agent sessions.

## Common Use Cases

| Use Case | Example |
|----------|---------|
| **Browser Automation** | Playwright, Puppeteer |
| **API Integration** | REST, GraphQL endpoints |
| **Dev Tools** | Database clients, schema tools |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Server connection fails | Check URL/port, network, credentials |
| Command fails | Verify path, args, dependencies |
| Config errors | Validate `.mcp.json` syntax, scope |

## Security
- Use environment variables for secrets.
- Prefer HTTPS for URLs.
- Rotate API keys regularly.

## Next Steps
- Add one server, verify with `forge mcp list`, and test in an agent session.