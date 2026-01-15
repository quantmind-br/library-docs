---
title: Video Walkthrough - Factory Documentation
url: https://docs.factory.ai/cli/getting-started/video-walkthrough
source: sitemap
fetched_at: 2026-01-13T19:03:57.697234438-03:00
rendered_js: false
word_count: 744
summary: Comprehensive guide for installing, configuring, and using the Droid CLI tool, covering interface navigation, autonomy modes, slash commands, and system integrations.
tags:
    - cli-installation
    - configuration
    - keyboard-shortcuts
    - autonomy-modes
    - mcp-integrations
    - custom-droids
    - byok-setup
category: guide
---

## Installation & Setup

Get started by installing the Droid CLI in your terminal of choice.

Verify the installation:

Start the Droid CLI:

```
cd /path/to/your/project
droid
```

### First-Time Authentication

On your first run, you’ll see an onboarding screen:

1. Choose to create an account or log in
2. Confirm the authentication code in your browser
3. Return to the terminal to start using droid

## Interface & Shortcuts

Press `Shift + ?` to open the help menu, which shows:

- How to send messages and create new lines
- Available keyboard shortcuts
- Basic navigation commands
- Autonomy mode options

### Essential Keyboard Shortcuts

ShortcutAction `Enter`Send message`\` + `Enter` (or `Shift + Enter`)New line in message`Esc` (double tap)Clear current input`Shift + ?`Open help menu`Shift + Tab`Cycle through autonomy modes`/`Open command menu`Cmd + Shift + H`Show root directory`Cmd + Shift + .`Show hidden files/folders`Ctrl + C` or `exit`Exit droid`Ctrl + V`Paste image

## Autonomy Modes

Cycle through different autonomy levels by pressing `Shift + Tab`: [Learn more about Specification Mode →](https://docs.factory.ai/cli/user-guides/specification-mode)

[Configure autonomy settings →](https://docs.factory.ai/cli/configuration/settings)

## Slash Commands

Press `/` to access the command menu with options for:

- **Account & Billing** - Manage your Factory account
- **Model** - Switch between AI models and set reasoning levels
- **Sessions** - View and navigate previous sessions
- **Settings** - Configure CLI preferences
- **Terminal Setup** - Configure key bindings
- **Custom Commands** - Access your [custom slash commands](https://docs.factory.ai/cli/configuration/custom-slash-commands)
- **Droids** - Manage [custom sub-agents](https://docs.factory.ai/cli/configuration/custom-droids)
- **MCP** - Configure [Model Context Protocol integrations](https://docs.factory.ai/cli/configuration/mcp)

### Switching Models

Access the model menu with `/model`:

1. View available models
2. Switch between models for different tasks
3. Set reasoning level where applicable

[Learn about choosing your model →](https://docs.factory.ai/cli/user-guides/choosing-your-model)

### Sessions Management

Access with `/sessions`:

- View all previous sessions
- Navigate to any past session
- Open sessions in the web interface
- Continue work from where you left off

Cloud sync must be enabled in settings for sessions to appear in the web interface.

## Settings & Configuration

Access settings via `/settings` to customize your experience: [Full settings documentation →](https://docs.factory.ai/cli/configuration/settings)

### Core Settings

### Advanced Settings

### IDE Integration

Install the droid extension for VS Code, Cursor, and other IDEs directly from the settings menu. [Learn more about IDE integration →](https://docs.factory.ai/cli/configuration/ide-integrations)

## Configuration Files

Access your configuration directory by pressing `Cmd + Shift + H` to show your root directory, then `Cmd + Shift + .` to reveal hidden files. Navigate to the `~/.factory/` folder.

### Directory Structure

```
~/.factory/
├── config.json          # Model configuration and BYOK
├── settings.json        # CLI settings and allow/deny lists
├── mcp.json            # MCP integrations
├── droids/             # Custom sub-agents
├── commands/           # Custom slash commands
├── logs/               # Session logs
└── bug-reports/        # Crash reports
```

### config.json - Bring Your Own Key

Configure custom models using your own API keys:

```
{
  "models": [
    {
      "provider": "openrouter",
      "name": "anthropic/claude-3.5-sonnet",
      "apiKey": "your-api-key-here",
      "displayName": "Claude 3.5 Sonnet (OpenRouter)"
    }
  ]
}
```

[See all BYOK providers →](https://docs.factory.ai/cli/byok/overview)

### settings.json - Allow & Deny Lists

Configure which commands require approval in High autonomy mode:

```
{
  "autoModeAllow": [],
  "autoModeDeny": [
    "git push",
    "rm -rf",
    "npm publish"
  ]
}
```

Even in High mode, commands in the `autoModeDeny` list will always require your explicit approval before execution.

### mcp.json - MCP Integrations

Enable or disable MCP tools individually:

```
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-api-key"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-playwright"],
      "disabled": true
    }
  }
}
```

Set `"disabled": true` to temporarily disable an MCP without removing its configuration. [Learn more about MCP configuration →](https://docs.factory.ai/cli/configuration/mcp)

## Custom Droids (Sub-Agents)

Custom droids are specialized AI agents that handle specific tasks. Access the droids menu with `/droids`:

### Managing Droids

- **Import** (`i`) - Import pre-built droids from other agents
- **Create** (`c`) - Create a new custom droid
- **Edit** - Modify existing droid configurations
- **Enable/Disable** - Toggle droids on or off

### Creating a Custom Droid

[Learn more about custom droids →](https://docs.factory.ai/cli/configuration/custom-droids)

### Example Use Cases

- **Code Review Droid** - Automated code reviews for pull requests
- **Documentation Droid** - Generates and maintains documentation
- **Test Generation Droid** - Creates comprehensive test suites
- **Security Audit Droid** - Scans for vulnerabilities and security issues

## MCP Integrations

Model Context Protocol (MCP) allows droid to integrate with external tools and data sources.

### Adding MCPs via CLI

Use the `/mcp add` command:

Then provide the MCP details:

- **Name**: Identifier for the MCP
- **Command**: Executable command (e.g., `npx`, `python`)
- **Args**: Command arguments
- **Environment Variables**: API keys and configuration

### Listing Configured MCPs

This shows all configured MCPs and their enabled/disabled status.

### Adding MCPs via Configuration File

You can also directly edit `~/.factory/mcp.json`:

```
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token-here"
      }
    }
  }
}
```

### Popular MCP Integrations

- **Brave Search** - Web search capabilities
- **Playwright** - Browser automation
- **GitHub** - Repository and issue management
- **Filesystem** - Extended file system access
- **Postgres** - Database queries
- **Slack** - Team communication

[Browse all MCP servers →](https://docs.factory.ai/cli/configuration/mcp)

## Example Workflow: Spec Mode to Implementation

Here’s a complete workflow demonstrating droid’s capabilities:

[Read the full Specification Mode guide →](https://docs.factory.ai/cli/user-guides/specification-mode) [Learn about implementing large features →](https://docs.factory.ai/cli/user-guides/implementing-large-features)

## Summary

You’ve learned how to:

- Install and authenticate with the Droid CLI
- Navigate the interface and use keyboard shortcuts
- Understand and switch between autonomy modes
- Configure settings and preferences
- Add custom models with BYOK
- Create and manage custom droids (sub-agents)
- Integrate external tools via MCP
- Use spec mode for planning before implementation

## Next Steps