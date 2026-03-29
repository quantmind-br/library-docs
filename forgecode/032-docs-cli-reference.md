---
title: ForgeCode
url: https://forgecode.dev/docs/cli-reference/
source: sitemap
fetched_at: 2026-03-29T16:30:33.726812-03:00
rendered_js: false
word_count: 813
summary: This document provides a comprehensive command-line reference for the ForgeCode CLI, detailing available commands, flags, configuration management, and conversation handling.
tags:
    - cli-reference
    - forgecode
    - command-line-interface
    - mcp-management
    - configuration-settings
    - conversation-management
    - automation
category: reference
---

Complete reference for ForgeCode command-line interface, including commands and flags.

CommandDescriptionExample`forge`Start interactive REPL`forge``forge -p "query"`Execute prompt directly, then exit`forge -p "explain this function"``cat file | forge`Process piped content as prompt, then exit`cat logs.txt | forge``forge -c file.txt`Execute commands from file, then continue in interactive mode`forge -c commands.txt``forge --conversation-id <id>`Resume conversation by ID`forge --conversation-id abc123``forge -C /path/to/dir`Change working directory before starting`forge -C ~/projects/myapp``forge --sandbox <name>`Create isolated git worktree`forge --sandbox experiment-1``forge list <resource>`List resources (agents, models, providers, mcp, etc.)`forge list agents``forge config <subcommand>`Manage configuration`forge config get model``forge conversation <subcommand>`Manage conversations`forge conversation list``forge mcp <subcommand>`Manage MCP servers`forge mcp list``forge info`Show current configuration and status`forge info``forge env`Display environment information`forge env``forge banner`Display version and helpful information`forge banner``forge --version`Print version`forge --version`

Customize ForgeCode's behavior with these command-line flags:

FlagDescriptionExample`-p, --prompt`Direct prompt to process without entering interactive mode (mutually exclusive with piping)`forge -p "analyze this code"``-c, --command`Path to file containing initial commands to execute, then continue in interactive mode`forge -c setup.txt``--conversation`Path to JSON file containing conversation to execute`forge --conversation chat.json``--conversation-id`Resume or continue existing conversation by ID`forge --conversation-id abc123``-C, --directory`Working directory to set before starting ForgeCode`forge -C ~/projects``--sandbox`Create isolated git worktree for experimentation`forge --sandbox feature-test``--verbose`Enable verbose output mode`forge --verbose``-r, --restricted`Use restricted shell (rbash) for enhanced security`forge -r``--agent`Agent ID to use for this session`forge --agent sage``-w, --workflow`Path to file containing workflow to execute`forge -w workflow.yaml``-e, --event`Dispatch event to workflow`forge -e '{"name": "fix_issue", "value": "449"}'``-h, --help`Print help information`forge --help``-V, --version`Print version`forge --version`

View available resources in your ForgeCode installation:

CommandDescriptionExample`forge list agents`List all available agents`forge list agents``forge list providers`List all available providers`forge list providers``forge list models`List all available models`forge list models``forge list config`List current configuration values`forge list config``forge list tools <agent>`List all tools for a specific agent`forge list tools sage``forge list mcp`List all MCP servers`forge list mcp``forge list conversation`List all conversations (max controlled by `FORGE_MAX_CONVERSATIONS` env var, defaults to 100)`forge list conversation`

### List Options[​](#list-options "Direct link to List Options")

FlagDescription`--porcelain`Output in machine-readable format

Manage ForgeCode configuration settings:

CommandDescriptionExample`forge config set <field> <value>`Set configuration value`forge config set model gpt-4``forge config get <field>`Get specific configuration value`forge config get provider``forge config list`List all configuration values`forge config list`

### Configuration Fields[​](#configuration-fields "Direct link to Configuration Fields")

FieldDescription`model`AI model to use`provider`AI provider to use

### Configuration Options[​](#configuration-options "Direct link to Configuration Options")

FlagDescription`--porcelain`Output in machine-readable format (tab-separated key-value pairs)

Manage and interact with conversations:

CommandDescriptionExample`forge conversation list`List all conversations (max controlled by `FORGE_MAX_CONVERSATIONS` env var, defaults to 100)`forge conversation list``forge conversation new`Create a new conversation and output its ID`forge conversation new``forge conversation dump <id> [format]`Dump conversation as JSON or HTML`forge conversation dump abc123 html``forge conversation compact <id>`Compact the conversation context`forge conversation compact abc123``forge conversation retry <id>`Retry last command without modifying context`forge conversation retry abc123``forge conversation resume <id>`Resume a conversation (starts interactive mode)`forge conversation resume abc123``forge conversation show <id>`Show last assistant message`forge conversation show abc123``forge conversation info <id>`Show conversation info (ID, title, tasks, completion status, file changes, token usage, cost)`forge conversation info abc123`

### Conversation Options[​](#conversation-options "Direct link to Conversation Options")

FlagDescription`--porcelain`Output in machine-readable format

### Dump Format[​](#dump-format "Direct link to Dump Format")

When using `forge conversation dump`, you can specify the output format:

- **JSON** (default): Omit format argument or specify `json`
- **HTML**: Specify `html` for formatted HTML output

Manage Model Context Protocol (MCP) servers:

CommandDescriptionExample`forge mcp import`Import MCP servers configuration from JSON`forge mcp import``forge mcp list`List all MCP servers`forge mcp list``forge mcp remove <name>`Remove a server by name`forge mcp remove playwright``forge mcp show <name>`Show detailed configuration for a server`forge mcp show playwright``forge mcp reload`Reload MCP servers and rebuild caches`forge mcp reload`

### MCP Options[​](#mcp-options "Direct link to MCP Options")

FlagDescription`--porcelain`Output in machine-readable format

### Working Directory[​](#working-directory "Direct link to Working Directory")

Change the working directory before starting ForgeCode:

### Sandbox Mode[​](#sandbox-mode "Direct link to Sandbox Mode")

Create an isolated git worktree for experimentation without affecting your main branch:

This creates a new git worktree where you can safely test changes.

### Workflow Execution[​](#workflow-execution "Direct link to Workflow Execution")

Execute predefined workflows with custom events:

### Security Mode[​](#security-mode "Direct link to Security Mode")

Run ForgeCode with restricted shell for enhanced security:

This uses rbash (restricted bash) to limit potentially harmful operations.

### Verbose Output[​](#verbose-output "Direct link to Verbose Output")

Enable detailed logging for debugging:

### Agent Selection[​](#agent-selection "Direct link to Agent Selection")

Use a specific agent for your session:

## Piping Content[​](#piping-content "Direct link to Piping Content")

ForgeCode supports piping content from stdin as an alternative to using the `-p` flag. **Note:** Piping and `-p` flag are mutually exclusive - when you use `-p`, the piped content is ignored.

tip

Use piping when you want to process file contents or command output. The piped content will be treated as your prompt to ForgeCode. If you need to provide additional context or instructions, use the `-p` flag instead.

### Resume Conversation[​](#resume-conversation "Direct link to Resume Conversation")

Continue a previous conversation using its ID:

### View Conversation History[​](#view-conversation-history "Direct link to View Conversation History")

List all your conversations:

View specific conversation details:

### Export Conversation[​](#export-conversation "Direct link to Export Conversation")

Export conversations for sharing or archival:

Many commands support `--porcelain` flag for machine-readable output, useful for scripting:

tip

The `--porcelain` flag provides tab-separated or structured output that's easier to parse in scripts and automation tools.

View system and environment details:

### Quick Analysis[​](#quick-analysis "Direct link to Quick Analysis")

### Interactive Session with Setup[​](#interactive-session-with-setup "Direct link to Interactive Session with Setup")

### Resume Previous Work[​](#resume-previous-work "Direct link to Resume Previous Work")

### Sandbox Experimentation[​](#sandbox-experimentation "Direct link to Sandbox Experimentation")

### Workflow Automation[​](#workflow-automation "Direct link to Workflow Automation")

### Verbose Debugging[​](#verbose-debugging "Direct link to Verbose Debugging")

- [Quickstart Guide](https://forgecode.dev/docs/quickstart/) - Getting started with ForgeCode
- [Built-in Commands](https://forgecode.dev/docs/commands/) - Interactive slash commands
- [Operating Agents](https://forgecode.dev/docs/operating-agents/) - Understanding ForgeCode agents
- [MCP Integration](https://forgecode.dev/docs/mcp-integration/) - Model Context Protocol integration
- [Environment Configuration](https://forgecode.dev/docs/environment-configuration/) - Advanced configuration options