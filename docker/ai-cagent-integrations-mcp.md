---
title: MCP
url: https://docs.docker.com/ai/cagent/integrations/mcp/
source: llms
fetched_at: 2026-01-24T14:13:29.45812904-03:00
rendered_js: false
word_count: 1159
summary: This guide explains how to configure and run cagent in MCP mode to integrate agents as tools within Claude Desktop and other MCP-compatible clients. It provides detailed setup instructions, configuration examples for various platforms, and best practices for agent orchestration.
tags:
    - cagent
    - mcp
    - claude-desktop
    - claude-code
    - tool-integration
    - ai-agents
    - configuration
category: guide
---

## MCP mode

When you run cagent in MCP mode, your agents show up as tools in Claude Desktop and other MCP clients. Instead of switching to a terminal to run your security agent, you ask Claude to use it and Claude calls it for you.

This guide covers setup for Claude Desktop and Claude Code. If you want agents embedded in your editor instead, see [ACP integration](https://docs.docker.com/ai/cagent/integrations/acp/).

You configure Claude Desktop (or another MCP client) to connect to cagent. Your agents appear in Claude's tool list. When you ask Claude to use one, it calls that agent through the MCP protocol.

Say you have a security agent configured. Ask Claude Desktop "Use the security agent to audit this authentication code" and Claude calls it. The agent runs with its configured tools (filesystem, shell, whatever you gave it), then returns results to Claude.

If your configuration has multiple agents, each one becomes a separate tool. A config with `root`, `designer`, and `engineer` agents gives Claude three tools to choose from. Claude might call the engineer directly or use the root coordinator—depends on your agent descriptions and what you ask for.

Docker provides an [MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/) that gives cagent agents access to a catalog of pre-configured MCP servers. Instead of configuring individual MCP servers, agents can use the gateway to access tools like web search, database queries, and more.

Configure MCP toolset with gateway reference:

The `docker:` prefix tells cagent to use the MCP Gateway for this server. See the [MCP Gateway documentation](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/) for available servers and configuration options.

You can also use the [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) to explore and manage MCP servers interactively.

Before configuring MCP integration, you need:

- **cagent installed** - See the [installation guide](https://docs.docker.com/ai/cagent/#installation)
- **Agent configuration** - A YAML file defining your agent. See the [tutorial](https://docs.docker.com/ai/cagent/tutorial/) or [example configurations](https://github.com/docker/cagent/tree/main/examples)
- **MCP client** - Claude Desktop, Claude Code, or another MCP-compatible application
- **API keys** - Environment variables for any model providers your agents use (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc.)

Your MCP client needs to know how to start cagent and communicate with it. This typically involves adding cagent as an MCP server in your client's configuration.

### [Claude Desktop](#claude-desktop)

Add cagent to your Claude Desktop MCP settings file:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Example configuration:

Configuration breakdown:

- `command`: Full path to your `cagent` binary (use `which cagent` to find it)
- `args`: MCP command arguments:
  
  - `mcp`: The subcommand to run cagent in MCP mode
  - `dockereng/myagent`: Your agent configuration (local file path or OCI reference)
  - `--working-dir`: Optional working directory for agent execution
- `env`: Environment variables your agents need:
  
  - Model provider API keys (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc.)
  - Any other environment variables your agents reference

After updating the configuration, restart Claude Desktop. Your agents will appear as available tools.

### [Claude Code](#claude-code)

Add cagent as an MCP server using the `claude mcp add` command:

Command breakdown:

- `claude mcp add`: Claude Code command to register an MCP server
- `--transport stdio`: Use stdio transport (standard for local MCP servers)
- `myagent`: Name for this MCP server in Claude Code
- `--env`: Pass environment variables (repeat for each variable)
- `--`: Separates Claude Code options from the MCP server command
- `cagent mcp /path/to/agent.yml`: The cagent MCP command with the path to your agent configuration
- `--working-dir $(pwd)`: Set the working directory for agent execution

After adding the server, your agents will be available as tools in Claude Code sessions.

### [Other MCP clients](#other-mcp-clients)

For other MCP-compatible clients, you need to:

1. Start cagent with `cagent mcp /path/to/agent.yml --working-dir /project/path`
2. Configure the client to communicate with cagent over stdio
3. Pass required environment variables (API keys, etc.)

Consult your MCP client's documentation for specific configuration steps.

You can specify your agent configuration as a local file path or OCI registry reference:

Use the same syntax in MCP client configurations:

Registry references let your team use the same agent configuration without managing local files. See [Sharing agents](https://docs.docker.com/ai/cagent/sharing-agents/) for details.

MCP clients see each of your agents as a separate tool and can call any of them directly. This changes how you should think about agent design compared to running agents with `cagent run`.

### [Write good descriptions](#write-good-descriptions)

The `description` field tells the MCP client what the agent does. This is how the client decides when to call it. "Analyzes code for security vulnerabilities and compliance issues" is specific. "A helpful security agent" doesn't say what it actually does.

### [MCP clients call agents directly](#mcp-clients-call-agents-directly)

The MCP client can call any of your agents, not just root. If you have `root`, `designer`, and `engineer` agents, the client might call the engineer directly instead of going through root. Design each agent to work on its own:

If an agent needs others to work properly, say so in the description: "Coordinates design and engineering agents to implement complete features."

### [Test each agent on its own](#test-each-agent-on-its-own)

MCP clients call agents individually, so test them that way:

Make sure the agent works without going through root first. Check that it has the right tools and that its instructions make sense when it's called directly.

Verify your MCP integration works:

1. Restart your MCP client after configuration changes
2. Check that cagent agents appear as available tools
3. Invoke an agent with a simple test prompt
4. Verify the agent can access its configured tools (filesystem, shell, etc.)

If agents don't appear or fail to execute, check:

- `cagent` binary path is correct and executable
- Agent configuration file exists and is valid
- All required API keys are set in environment variables
- Working directory path exists and has appropriate permissions
- MCP client logs for connection or execution errors

### [Call specialist agents](#call-specialist-agents)

You have a security agent that knows your compliance rules and common vulnerabilities. In Claude Desktop, paste some authentication code and ask "Use the security agent to review this." The agent checks the code and reports what it finds. You stay in Claude's interface the whole time.

### [Work with agent teams](#work-with-agent-teams)

Your configuration has a coordinator that delegates to designer and engineer agents. Ask Claude Code "Use the coordinator to implement a login form" and the coordinator hands off UI work to the designer and code to the engineer. You get a complete implementation without running `cagent run` yourself.

### [Run domain-specific tools](#run-domain-specific-tools)

You built an infrastructure agent with custom deployment scripts and monitoring queries. Ask any MCP client "Use the infra agent to check production status" and it runs your tools and returns results. Your deployment knowledge is now available wherever you use MCP clients.

Your team keeps agents in an OCI registry. Everyone adds `agentcatalog/security-expert` to their MCP client config. When you update the agent, they get the new version on their next restart. No YAML files to pass around.

- Use the [MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/) to give your agents access to pre-configured MCP servers
- Explore MCP servers interactively with the [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/)
- Review the [configuration reference](https://docs.docker.com/ai/cagent/reference/config/) for advanced agent setup
- Explore the [toolsets reference](https://docs.docker.com/ai/cagent/reference/toolsets/) to learn what tools agents can use
- Add [RAG for codebase search](https://docs.docker.com/ai/cagent/rag/) to your agent
- Check the [CLI reference](https://docs.docker.com/ai/cagent/reference/cli/) for all `cagent mcp` options
- Browse [example configurations](https://github.com/docker/cagent/tree/main/examples) for different agent types