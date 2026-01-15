---
title: Model Context Protocol (MCP) - Factory Documentation
url: https://docs.factory.ai/cli/configuration/mcp
source: sitemap
fetched_at: 2026-01-13T19:03:48.738727227-03:00
rendered_js: false
word_count: 756
summary: A comprehensive guide on managing Model Context Protocol (MCP) servers in Droid, detailing methods for adding, configuring, and removing servers via the interactive UI, registry, or CLI commands.
tags:
    - mcp
    - server-management
    - droid
    - cli
    - configuration
    - oauth
    - stdio
    - http
category: guide
---

Model Context Protocol (MCP) servers extend droid’s capabilities by providing additional tools and context. Droid offers two ways to manage them: an interactive UI for easy browsing and setup, or CLI commands for scripting and automation.

## Quick Start: Add from Registry

The easiest way to get started is using the built-in registry. Type `/mcp` in droid and select **“Add from Registry”** to browse 40+ pre-configured servers:

ServerDescriptionlinearIssue tracking and project managementsentryError tracking and performance monitoringnotionNotes, docs, and project managementsupabaseCreate and manage Supabase projectsstripePayment processing APIsvercelManage projects and deploymentsplaywrightEnd-to-end browser testinghubspotCRM data managementmongodbDatabase management…and many more

Select a server from the list, authenticate if required (most HTTP servers support OAuth—just follow the browser prompt), and the server is ready to use.

## Interactive Manager (`/mcp`)

Type `/mcp` within droid to open the interactive MCP manager. From here you can:

- **Browse servers** - See all configured servers and their connection status
- **View tools** - Inspect what tools each connected server provides
- **Enable/disable** - Temporarily disable servers without removing them
- **Authenticate** - Connect to OAuth-enabled servers via browser
- **Clear auth** - Remove stored credentials for a server
- **Add from registry** - One-click setup for popular MCP servers
- **Remove servers** - Delete user-configured servers

## Adding Servers via CLI

For scripting and automation, use `droid mcp add`. Droid supports two types of servers: **http** (remote endpoints) and **stdio** (local processes).

### Adding HTTP Servers

HTTP servers are remote MCP endpoints - the recommended way to connect to cloud services and APIs. **Syntax:**

```
droid mcp add <name> <url> --type http [--header "KEY: VALUE"...]
```

**Arguments:**

- `name` - Unique server identifier
- `url` - HTTP/HTTPS URL of the MCP server
- `--type http` - Required flag to specify HTTP transport
- `--header "KEY: VALUE"` - HTTP headers for authentication (can be used multiple times)

### Popular HTTP MCP Servers

#### Development & Testing

**Sentry** - Monitor errors, debug production issues

```
droid mcp add sentry https://mcp.sentry.dev/mcp --type http
```

**Hugging Face** - Access Hugging Face Hub and Gradio AI applications

```
droid mcp add hugging-face https://huggingface.co/mcp --type http
```

**Socket** - Security analysis for dependencies

```
droid mcp add socket https://mcp.socket.dev/ --type http
```

#### Project Management & Documentation

**Notion** - Read docs, update pages, manage tasks

```
droid mcp add notion https://mcp.notion.com/mcp --type http
```

**Linear** - Issue tracking and project management

```
droid mcp add linear https://mcp.linear.app/mcp --type http
```

**Intercom** - Access customer conversations and tickets

```
droid mcp add intercom https://mcp.intercom.com/mcp --type http
```

**Monday** - Manage monday.com boards and items

```
droid mcp add monday https://mcp.monday.com/mcp --type http
```

#### Payments & Commerce

**Stripe** - Payment processing and subscriptions

```
droid mcp add stripe https://mcp.stripe.com --type http
```

**PayPal** - PayPal commerce and payment processing

```
droid mcp add paypal https://mcp.paypal.com/mcp --type http
```

#### Design & Media

**Figma** - Generate code with Figma context

```
droid mcp add figma https://mcp.figma.com/mcp --type http
```

**Canva** - Browse, summarize, and generate Canva designs

```
droid mcp add canva https://mcp.canva.com/mcp --type http
```

**TwelveLabs** - Video analysis, search, and AI-powered insights

```
droid mcp add twelvelabs-mcp https://mcp.twelvelabs.io --type http \
  --header "x-api-key: YOUR_TWELVELABS_API_KEY"
```

#### Infrastructure & DevOps

**Netlify** - Create, deploy, and manage websites

```
droid mcp add netlify https://netlify-mcp.netlify.app/mcp --type http
```

**Vercel** - Manage projects, deployments, and logs

```
droid mcp add vercel https://mcp.vercel.com/ --type http
```

**Stytch** - Configure authentication services

```
droid mcp add stytch http://mcp.stytch.dev/mcp --type http
```

### Adding Stdio Servers

Stdio servers run as local processes on your machine - ideal for tools that need direct system access. **Syntax:**

```
droid mcp add <name> "<command>" [--env KEY=VALUE...]
```

**Arguments:**

- `name` - Unique server identifier
- `command` - Command to start the server (quote if it contains spaces)
- `--env KEY=VALUE` - Environment variables (can be used multiple times)

### Popular Stdio MCP Servers

**Airtable** - Read/write records, manage bases and tables

```
droid mcp add airtable "npx -y airtable-mcp-server" \
  --env AIRTABLE_API_KEY=your_key
```

**ClickUp** - Task management and project tracking

```
droid mcp add clickup "npx -y @hauptsache.net/clickup-mcp" \
  --env CLICKUP_API_KEY=your_key \
  --env CLICKUP_TEAM_ID=your_team_id
```

**HubSpot** - Access and manage CRM data

```
droid mcp add hubspot "npx -y @hubspot/mcp-server" \
  --env HUBSPOT_ACCESS_TOKEN=your_token
```

## Removing Servers

Remove a server from your configuration:

**Example:**

## Managing Servers

Type `/mcp` within droid to open an interactive UI for managing MCP servers.

- See all configured servers with status
- View all tools provided by each server
- Authenticate remote servers that require OAuth authentication
- Add/remove and enable/disable servers

## Configuration

MCP server configurations can be stored at two levels:

LevelLocationPurpose**User**`~/.factory/mcp.json`Your personal servers, available in all projects**Project**`.factory/mcp.json`Shared team servers, committed to the repo

### How Layering Works

User config takes priority over project config. When both levels define the same server, the user-level settings win. **Key behaviors:**

- When you **enable/disable** a project-defined server, a copy is saved to your user config with the new state. The original project config remains unchanged, so your teammates aren’t affected.
- **Project servers cannot be removed** via CLI or the `/mcp` UI. To remove them, edit `.factory/mcp.json` directly.
- Servers you add via `droid mcp add` or the registry always go to your **user config**.

### OAuth Tokens

OAuth tokens are stored globally in your system keyring (or fallback file), **not per-project**. If you authenticate with a server in one project, you’re authenticated everywhere that server is configured. To clear authentication for a server, use the `/mcp` interactive manager and select “Clear Auth”.

### Configuration Schema

Each server entry includes:

- **type**: Server type (`stdio` or `http`)
- **disabled**: Boolean flag to temporarily disable the server (default: `false`)

For **stdio** servers:

- **command**: Executable to run
- **args**: Command-line arguments (array)
- **env**: Environment variables (object)

For **http** servers:

- **url**: HTTP/HTTPS endpoint URL
- **headers**: HTTP headers for authentication (object)

**Example `mcp.json`:**

```
{
  "mcpServers": {
    "linear": {
      "type": "http",
      "url": "https://mcp.linear.app/mcp",
      "disabled": false
    },
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"],
      "disabled": false
    }
  }
}
```

Droid automatically reloads when the configuration file changes, so servers are immediately available after adding them.