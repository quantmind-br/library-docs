---
title: Using Extensions | goose
url: https://block.github.io/goose/docs/getting-started/using-extensions
source: github_pages
fetched_at: 2026-01-22T22:13:25.883351987-03:00
rendered_js: true
word_count: 1289
summary: This document explains how to use and manage extensions in goose, covering built-in tools, installation of custom MCP servers, and various configuration methods.
tags:
    - goose-ai
    - model-context-protocol
    - extension-management
    - mcp-servers
    - software-integration
    - configuration-guide
category: guide
---

Extensions are add-ons that provide a way to extend the functionality of goose by connecting with applications and tools you already use in your workflow. These extensions can be used to add new features, access data and resources, or integrate with other systems.

Extensions are based on the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol), so you can connect goose to a wide ecosystem of capabilities.

goose automatically checks external extensions for known malware before activation. If a malicious package is detected, the [extension will be blocked](https://block.github.io/goose/docs/troubleshooting/known-issues#malicious-package-detected) with a clear error message.

## Built-in Extensions[​](#built-in-extensions "Direct link to Built-in Extensions")

goose includes several built-in extensions you can start using out of the box:

- [Developer](https://block.github.io/goose/docs/mcp/developer-mcp): Provides a set of general development tools that are useful for software development. The Developer extension is **enabled by default**.
- [Computer Controller](https://block.github.io/goose/docs/mcp/computer-controller-mcp): Provides general computer control tools for webscraping, file caching, and automations.
- [Memory](https://block.github.io/goose/docs/mcp/memory-mcp): Teaches goose to remember your preferences as you use it.
- [Tutorial](https://block.github.io/goose/docs/mcp/tutorial-mcp): Provides interactive tutorials for learning about goose.
- [Auto Visualiser](https://block.github.io/goose/docs/mcp/autovisualiser-mcp): Automatically generates graphical data visualizations in conversations.

### Built-in Platform Extensions[​](#built-in-platform-extensions "Direct link to Built-in Platform Extensions")

Platform extensions are built-in extensions that provide global features like conversation search, task tracking, and extension management. These extensions are always available and can be toggled on or off as needed.

- [Chat Recall](https://block.github.io/goose/docs/mcp/chatrecall-mcp): Search conversation content across all your session history
- [Code Execution](https://block.github.io/goose/docs/mcp/code-execution-mcp): Execute JavaScript code for tool discovery and tool calling
- [Extension Manager](https://block.github.io/goose/docs/mcp/extension-manager-mcp): Discover, enable, and disable extensions dynamically during sessions (enabled by default)
- [Skills](https://block.github.io/goose/docs/mcp/skills-mcp): Load and use agent skills from various project and global skill directories (enabled by default)
- [Todo](https://block.github.io/goose/docs/mcp/todo-mcp): Manage task lists and track progress across sessions (enabled by default)

### Toggling Built-in Extensions[​](#toggling-built-in-extensions "Direct link to Toggling Built-in Extensions")

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar.
2. Click the `Extensions` button on the sidebar.
3. Under `Extensions`, you can toggle the built-in extensions on or off.

info

goose's built-in extensions are MCP servers in their own right. If you'd like to use the MCP servers included with goose with any other agent, you are free to do so.

## Discovering Extensions[​](#discovering-extensions "Direct link to Discovering Extensions")

goose provides a [central directory](https://block.github.io/goose/extensions) of extensions that you can install and use.

You can also add any other [MCP Server](#mcp-servers) as a goose extension, even if it's not listed in our directory.

## Adding Extensions[​](#adding-extensions "Direct link to Adding Extensions")

Extensions can be installed directly via the [extensions directory](https://block.github.io/goose/extensions), CLI, or UI.

Airgapped Environments

If you're in a corporate or airgapped environment and extensions fail to activate, see [Airgapped/Offline Environments](https://block.github.io/goose/docs/troubleshooting/known-issues#airgappedoffline-environment-issues) for workarounds.

### MCP Servers[​](#mcp-servers "Direct link to MCP Servers")

You can install any MCP server as a goose extension.

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar.
2. Click the `Extensions` button on the sidebar.
3. Under `Extensions`, click `Add custom extension`.
4. On the `Add custom extension` modal, enter the necessary details
   
   - If adding an environment variable, click `Add` button to the right of the variable
   - The `Timeout` field lets you set how long goose should wait for a tool call from this extension to complete
5. Click `Add` button

#### Example of adding the [Knowledge Graph Memory MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/memory):[​](#example-of-adding-the-knowledge-graph-memory-mcp-server "Direct link to example-of-adding-the-knowledge-graph-memory-mcp-server")

- **Type**: `Standard IO`
- **ID**: `kgm-mcp` (*set this to whatever you want*)
- **Name**: `Knowledge Graph Memory` (*set this to whatever you want*)
- **Description**: `maps and stores complex relationships between concepts` (*set this to whatever you want*)
- **Command**: `npx -y @modelcontextprotocol/server-memory`

### Deeplinks[​](#deeplinks "Direct link to Deeplinks")

Extensions can be installed using goose's deep link protocol. The URL format varies based on the extension type:

- StandardIO
- Streamable HTTP

```
goose://extension?cmd=<command>&arg=<argument>&id=<id>&name=<name>&description=<description>
```

Required parameters:

- `cmd`: The base command to run, one of `jbang`, `npx`, `uvx`, `goosed`, or `docker`
- `arg`: (cmd only) Command arguments (can be repeated for multiple arguments: `&arg=...&arg=...`)
- `timeout`: Maximum time (in seconds) to wait for extension responses
- `id`: Unique identifier for the extension
- `name`: Display name for the extension
- `description`: Brief description of the extension's functionality

A command like `npx -y @modelcontextprotocol/server-github` would be represented as:

```
goose://extension?cmd=npx&arg=-y&arg=%40modelcontextprotocol/server-github&timeout=<timeout>&id=<id>&name=<name>&description=<description>
```

Note that each parameter to the `npx` command is passed as a separate `arg` parameter in the deeplink.

note

All parameters in the deeplink must be URL-encoded. For example, spaces should be replaced with `%20`, and `@` should be replaced with `%40`.

### Config Entry[​](#config-entry "Direct link to Config Entry")

For advanced users, you can also directly edit the config file (`~/.config/goose/config.yaml`) to add, remove, or update an extension:

```
extensions:
github:
name: GitHub
cmd: npx
args:[-y @modelcontextprotocol/server-github]
enabled:true
envs:{"GITHUB_PERSONAL_ACCESS_TOKEN":"<YOUR_TOKEN>"}
type: stdio
timeout:300
```

## Enabling/Disabling Extensions[​](#enablingdisabling-extensions "Direct link to Enabling/Disabling Extensions")

You can enable or disable installed extensions based on your workflow needs.

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar.
2. Click the `Extensions` button on the sidebar.
3. Use the toggle switch next to each extension to enable or disable it.

## Automatically Enabled Extensions[​](#automatically-enabled-extensions "Direct link to Automatically Enabled Extensions")

The Smart Extension Recommendation system in goose automatically identifies and suggests relevant extensions based on your tasks and needs. This section explains how to use this feature effectively and understand its capabilities and limitations.

When you request a task, goose checks its enabled extensions and their tools to determine if it can fulfill the request. If not, it suggests or enables additional extensions as needed. You can also request specific extensions by name.

warning

Any extensions enabled dynamically are only enabled for the current session. To keep extensions enabled between sessions, see [Enabling/Disabling Extensions](#enablingdisabling-extensions).

### Automatic Detection[​](#automatic-detection "Direct link to Automatic Detection")

goose automatically detects when an extension is needed based on your task requirements. Here's an example of how goose identifies and enables a needed extension during a conversation:

- goose Desktop
- goose CLI

#### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
Find all orders with pending status from our production database
```

#### goose Output[​](#goose-output "Direct link to goose Output")

```
I'll help you search for available extensions that might help us interact with PostgreSQL databases.

🔍 Search Available Extensions
└─ Output ▼

 I see there's a PostgreSQL extension available. Let me enable it so we can query your database.

🔧 Manage Extensions
└─ action           enable
   extension_name   postgresql

The extension 'postgresql' has been installed successfully

Great! Now I can help you query the database...
```

### Direct Request[​](#direct-request "Direct link to Direct Request")

goose responds to explicit requests for extensions, allowing users to manually enable specific tools they need. Here's an example of how goose handles a direct request to enable an extension:

- goose Desktop
- goose CLI

#### goose Prompt[​](#goose-prompt-2 "Direct link to goose Prompt")

#### goose Output[​](#goose-output-2 "Direct link to goose Output")

```
I'll help enable the PostgreSQL extension for you.

🔧 Manage Extensions
└─ action           enable
   extension_name   postgresql

The extension 'postgresql' has been installed successfully

The PostgreSQL extension is now ready to use. What would you like to do with it?
```

## Updating Extension Properties[​](#updating-extension-properties "Direct link to Updating Extension Properties")

goose relies on extension properties to determine how to handle an extension. You can edit these properties if you want to change the extension's display settings and behavior, such as the name, timeout, or environment variables.

- goose Desktop
- Config file

<!--THE END-->

1. Click the button in the top-left to open the sidebar.
2. Click the `Extensions` button on the sidebar.
3. Under `Extensions`, click the button on the extension you'd like to edit.
4. In the dialog that appears, edit the extension's properties as needed.
5. Click `Save Changes`.

## Removing Extensions[​](#removing-extensions "Direct link to Removing Extensions")

You can remove installed extensions.

- goose Desktop
- Config file

<!--THE END-->

1. Click the button in the top-left to open the sidebar.
2. Click the `Extensions` button on the sidebar.
3. Under `Extensions`, click the button on the extension you'd like to remove.
4. In the dialog that appears, click `Remove Extension`.

## Starting Session with Extensions[​](#starting-session-with-extensions "Direct link to Starting Session with Extensions")

You can start a tailored goose session with specific extensions directly from the CLI.

Notes

- The extension will not be installed. It will only be enabled for the current session.
- There's no need to do this if you already have the extensions enabled.

### Built-in Extensions[​](#built-in-extensions-1 "Direct link to Built-in Extensions")

To enable a built-in extension while starting a session, run the following command:

```
goose session --with-builtin "{extension_id}"
```

For example, to enable the Developer and Computer Controller extensions and start a session, you'd run:

```
goose session --with-builtin "developer,computercontroller"
```

Or alternatively:

```
goose session --with-builtin developer --with-builtin computercontroller
```

### External Extensions[​](#external-extensions "Direct link to External Extensions")

To enable an extension while starting a session, run the following command:

```
goose session --with-extension "{extension command}" --with-extension "{another extension command}"
```

For example, to start a session with the [Fetch extension](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch), you'd run:

```
goose session --with-extension "uvx mcp-server-fetch"
```

#### Environment Variables[​](#environment-variables "Direct link to Environment Variables")

Some extensions require environment variables. You can include these in your command:

```
goose session --with-extension "VAR=value command arg1 arg2"
```

For example, to start a session with the [GitHub extension](https://github.com/github/github-mcp-server), you'd run:

```
goose session --with-extension "GITHUB_PERSONAL_ACCESS_TOKEN=<YOUR_TOKEN> npx -y @modelcontextprotocol/server-github"
```

info

Note that you'll need [Node.js](https://nodejs.org/) installed on your system to run this command, as it uses `npx`.

### Remote Extensions over Streamable HTTP[​](#remote-extensions-over-streamable-http "Direct link to Remote Extensions over Streamable HTTP")

To enable a remote extension over Streamable HTTP while starting a session, run the following command:

```
goose session --with-streamable-http-extension "{extension URL}" --with-streamable-http-extension "{another extension URL}"
```

For example, to start a session with a Streamable HTTP extension, you'd run:

```
goose session --with-streamable-http-extension "https://example.com/streamable"
```

## Developing Extensions[​](#developing-extensions "Direct link to Developing Extensions")

goose extensions are implemented with MCP, a standard protocol that allows AI models and agents to securely connect with local or remote resources. Learn how to build your own [extension as an MCP server](https://modelcontextprotocol.io/quickstart/server).

**Tutorials:**

- [Building Custom Extensions](https://block.github.io/goose/docs/tutorials/custom-extensions) - Create a Python-based MCP extension
- [Building MCP Apps](https://block.github.io/goose/docs/tutorials/building-mcp-apps) - Create interactive UI apps