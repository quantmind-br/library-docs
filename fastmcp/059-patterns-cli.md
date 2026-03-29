---
title: FastMCP CLI - FastMCP
url: https://gofastmcp.com/patterns/cli
source: crawler
fetched_at: 2026-01-22T22:21:53.538415295-03:00
rendered_js: false
word_count: 1738
summary: This document provides a comprehensive overview of the FastMCP command-line interface, detailing commands for running, developing, and installing MCP servers along with their associated options and entrypoints.
tags:
    - fastmcp-cli
    - mcp-server
    - command-line-interface
    - dependency-management
    - server-deployment
    - python-mcp
category: reference
---

FastMCP provides a command-line interface (CLI) that makes it easy to run, develop, and install your MCP servers. The CLI is automatically installed when you install FastMCP.

## Commands Overview

CommandPurposeDependency Management`run`Run a FastMCP server directly**Supports:** Local files, factory functions, URLs, fastmcp.json configs, MCP configs. **Deps:** Uses your local environment directly. With `--python`, `--with`, `--project`, or `--with-requirements`: Runs via `uv run` subprocess. With fastmcp.json: Automatically manages dependencies based on configuration`dev`Run a server with the MCP Inspector for testing**Supports:** Local files and fastmcp.json configs. **Deps:** Always runs via `uv run` subprocess (never uses your local environment); dependencies must be specified or available in a uv-managed project. With fastmcp.json: Uses configured dependencies`install`Install a server in MCP client applications**Supports:** Local files and fastmcp.json configs. **Deps:** Creates an isolated environment; dependencies must be explicitly specified with `--with` and/or `--with-editable`. With fastmcp.json: Uses configured dependencies`inspect`Generate a JSON report about a FastMCP server**Supports:** Local files and fastmcp.json configs. **Deps:** Uses your current environment; you are responsible for ensuring all dependencies are available`project prepare`Create a persistent uv project from fastmcp.json environment config**Supports:** fastmcp.json configs only. **Deps:** Creates a uv project directory with all dependencies pre-installed for reuse with `--project` flag`version`Display version informationN/A

## `fastmcp run`

Run a FastMCP server directly or proxy a remote server.

### Options

OptionFlagDescriptionTransport`--transport`, `-t`Transport protocol to use (`stdio`, `http`, or `sse`)Host`--host`Host to bind to when using http transport (default: 127.0.0.1)Port`--port`, `-p`Port to bind to when using http transport (default: 8000)Path`--path`Path to bind to when using http transport (default: `/mcp/` or `/sse/` for SSE)Log Level`--log-level`, `-l`Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)No Banner`--no-banner`Disable the startup banner displayAuto-Reload`--reload` / `--no-reload`Enable auto-reload on file changes (development mode)Reload Directories`--reload-dir`Directories to watch for changes (can be used multiple times)No Environment`--skip-env`Skip environment setup with uv (use when already in a uv environment)Python Version`--python`Python version to use (e.g., 3.10, 3.11)Additional Packages`--with`Additional packages to install (can be used multiple times)Project Directory`--project`Run the command within the given project directoryRequirements File`--with-requirements`Requirements file to install dependencies from

### Entrypoints

New in version `2.3.5` The `fastmcp run` command supports the following entrypoints:

1. [**Inferred server instance**](#inferred-server-instance): `server.py` - imports the module and looks for a FastMCP server instance named `mcp`, `server`, or `app`. Errors if no such object is found.
2. [**Explicit server entrypoint**](#explicit-server-entrypoint): `server.py:custom_name` - imports and uses the specified server entrypoint
3. [**Factory function**](#factory-function): `server.py:create_server` - calls the specified function (sync or async) to create a server instance
4. [**Remote server proxy**](#remote-server-proxy): `https://example.com/mcp-server` - connects to a remote server and creates a **local proxy server**
5. [**FastMCP configuration file**](#fastmcp-configuration): `fastmcp.json` - runs servers using FastMCP’s declarative configuration format (auto-detects files in current directory)
6. **MCP configuration file**: `mcp.json` - runs servers defined in a standard MCP configuration file

#### Inferred Server Instance

If you provide a path to a file, `fastmcp run` will load the file and look for a FastMCP server instance stored as a variable named `mcp`, `server`, or `app`. If no such object is found, it will raise an error. For example, if you have a file called `server.py` with the following content:

```
from fastmcp import FastMCP

mcp = FastMCP("MyServer")
```

You can run it with:

#### Explicit Server Entrypoint

If your server is stored as a variable with a custom name, or you want to be explicit about which server to run, you can use the following syntax to load a specific server entrypoint:

```
fastmcp run server.py:custom_name
```

For example, if you have a file called `server.py` with the following content:

```
from fastmcp import FastMCP

my_server = FastMCP("CustomServer")

@my_server.tool
def hello() -> str:
    return "Hello from custom server!"
```

You can run it with:

```
fastmcp run server.py:my_server
```

#### Factory Function

New in version `2.11.2` Since `fastmcp run` ignores the `if __name__ == "__main__"` block, you can use a factory function to run setup code before your server starts. Factory functions are called without any arguments and must return a FastMCP server instance. Both sync and async factory functions are supported. The syntax for using a factory function is the same as for an explicit server entrypoint: `fastmcp run server.py:factory_fn`. FastMCP will automatically detect that you have identified a function rather than a server Instance For example, if you have a file called `server.py` with the following content:

```
from fastmcp import FastMCP

async def create_server() -> FastMCP:
    mcp = FastMCP("MyServer")

    @mcp.tool
    def add(x: int, y: int) -> int:
        return x + y

    # Setup that runs with fastmcp run
    tool = await mcp.get_tool("add")
    tool.disable()

    return mcp
```

You can run it with:

```
fastmcp run server.py:create_server
```

#### Remote Server Proxy

FastMCP run can also start a local proxy server that connects to a remote server. This is useful when you want to run a remote server locally for testing or development purposes, or to use with a client that doesn’t support direct connections to remote servers. To start a local proxy, you can use the following syntax:

```
fastmcp run https://example.com/mcp
```

#### FastMCP Configuration

New in version `2.11.4` FastMCP supports declarative configuration through `fastmcp.json` files. When you run `fastmcp run` without arguments, it automatically looks for a `fastmcp.json` file in the current directory:

```
# Auto-detect fastmcp.json in current directory
fastmcp run

# Or explicitly specify a configuration file
fastmcp run my-config.fastmcp.json
```

The configuration file handles dependencies, environment variables, and transport settings. Command-line arguments override configuration file values:

```
# Override port from config file
fastmcp run fastmcp.json --port 8080

# Skip environment setup when already in a uv environment
fastmcp run fastmcp.json --skip-env
```

See [Server Configuration](https://gofastmcp.com/deployment/server-configuration) for detailed documentation on fastmcp.json.

#### MCP Configuration

FastMCP can also run servers defined in a standard MCP configuration file. This is useful when you want to run multiple servers from a single file, or when you want to use a client that doesn’t support direct connections to remote servers. To run a MCP configuration file, you can use the following syntax:

This will run all the servers defined in the file.

## `fastmcp dev`

Run a MCP server with the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) for testing. Auto-reload is enabled by default, so your server automatically restarts when you save changes to source files.

### Options

OptionFlagDescriptionEditable Package`--with-editable`, `-e`Directory containing pyproject.toml to install in editable modeAdditional Packages`--with`Additional packages to install (can be used multiple times)Inspector Version`--inspector-version`Version of the MCP Inspector to useUI Port`--ui-port`Port for the MCP Inspector UIServer Port`--server-port`Port for the MCP Inspector Proxy serverAuto-Reload`--reload` / `--no-reload`Enable/disable auto-reload on file changes (enabled by default)Reload Directories`--reload-dir`Directories to watch for changes (can be used multiple times)Python Version`--python`Python version to use (e.g., 3.10, 3.11)Project Directory`--project`Run the command within the given project directoryRequirements File`--with-requirements`Requirements file to install dependencies from

### Entrypoints

The `dev` command supports local FastMCP server files and configuration:

1. **Inferred server instance**: `server.py` - imports the module and looks for a FastMCP server instance named `mcp`, `server`, or `app`. Errors if no such object is found.
2. **Explicit server entrypoint**: `server.py:custom_name` - imports and uses the specified server entrypoint
3. **Factory function**: `server.py:create_server` - calls the specified function (sync or async) to create a server instance
4. **FastMCP configuration**: `fastmcp.json` - uses FastMCP’s declarative configuration (auto-detects in current directory)

**Examples**

```
# Run dev server with editable mode and additional packages
fastmcp dev server.py -e . --with pandas --with matplotlib

# Run dev server with fastmcp.json configuration (auto-detects)
fastmcp dev

# Run dev server with explicit fastmcp.json file
fastmcp dev dev.fastmcp.json

# Run dev server with specific Python version
fastmcp dev server.py --python 3.11

# Run dev server with requirements file
fastmcp dev server.py --with-requirements requirements.txt

# Run dev server within a specific project directory
fastmcp dev server.py --project /path/to/project
```

## `fastmcp install`

New in version `2.10.3` Install a MCP server in MCP client applications. FastMCP currently supports the following clients:

- **Claude Code** - Installs via Claude Code’s built-in MCP management system
- **Claude Desktop** - Installs via direct configuration file modification
- **Cursor** - Installs via deeplink that opens Cursor for user confirmation
- **MCP JSON** - Generates standard MCP JSON configuration for manual use

```
fastmcp install claude-code server.py
fastmcp install claude-desktop server.py
fastmcp install cursor server.py
fastmcp install mcp-json server.py
```

Note that for security reasons, MCP clients usually run every server in a completely isolated environment. Therefore, all dependencies must be explicitly specified using the `--with` and/or `--with-editable` options (following `uv` conventions) or by attaching them to your server in code via the `dependencies` parameter. You should not assume that the MCP server will have access to your local environment.

### Options

OptionFlagDescriptionServer Name`--server-name`, `-n`Custom name for the server (defaults to server’s name attribute or file name)Editable Package`--with-editable`, `-e`Directory containing pyproject.toml to install in editable modeAdditional Packages`--with`Additional packages to install (can be used multiple times)Environment Variables`--env`Environment variables in KEY=VALUE format (can be used multiple times)Environment File`--env-file`, `-f`Load environment variables from a .env filePython Version`--python`Python version to use (e.g., 3.10, 3.11)Project Directory`--project`Run the command within the given project directoryRequirements File`--with-requirements`Requirements file to install dependencies from

### Entrypoints

The `install` command supports local FastMCP server files and configuration:

1. **Inferred server instance**: `server.py` - imports the module and looks for a FastMCP server instance named `mcp`, `server`, or `app`. Errors if no such object is found.
2. **Explicit server entrypoint**: `server.py:custom_name` - imports and uses the specified server entrypoint
3. **Factory function**: `server.py:create_server` - calls the specified function (sync or async) to create a server instance
4. **FastMCP configuration**: `fastmcp.json` - uses FastMCP’s declarative configuration with dependencies and settings

**Examples**

```
# Auto-detects server entrypoint (looks for 'mcp', 'server', or 'app')
fastmcp install claude-desktop server.py

# Install with fastmcp.json configuration (auto-detects)
fastmcp install claude-desktop

# Install with explicit fastmcp.json file
fastmcp install claude-desktop my-config.fastmcp.json

# Uses specific server entrypoint
fastmcp install claude-desktop server.py:my_server

# With custom name and dependencies
fastmcp install claude-desktop server.py:my_server --server-name "My Analysis Server" --with pandas

# Install in Claude Code with environment variables
fastmcp install claude-code server.py --env API_KEY=secret --env DEBUG=true

# Install in Cursor with environment variables
fastmcp install cursor server.py --env API_KEY=secret --env DEBUG=true

# Install with environment file
fastmcp install cursor server.py --env-file .env

# Install with specific Python version
fastmcp install claude-desktop server.py --python 3.11

# Install with requirements file
fastmcp install claude-code server.py --with-requirements requirements.txt

# Install within a project directory
fastmcp install cursor server.py --project /path/to/project

# Generate MCP JSON configuration
fastmcp install mcp-json server.py --name "My Server" --with pandas

# Copy JSON configuration to clipboard
fastmcp install mcp-json server.py --copy
```

### MCP JSON Generation

The `mcp-json` subcommand generates standard MCP JSON configuration that can be used with any MCP-compatible client. This is useful when:

- Working with MCP clients not directly supported by FastMCP
- Creating configuration for CI/CD environments
- Sharing server configurations with others
- Integration with custom tooling

The generated JSON follows the standard MCP server configuration format used by Claude Desktop, VS Code, Cursor, and other MCP clients, with the server name as the root key:

```
{
  "server-name": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "fastmcp",
      "fastmcp",
      "run",
      "/path/to/server.py"
    ],
    "env": {
      "API_KEY": "value"
    }
  }
}
```

**Options specific to mcp-json:**

OptionFlagDescriptionCopy to Clipboard`--copy`Copy configuration to clipboard instead of printing to stdout

## `fastmcp inspect`

New in version `2.9.0` Inspect a FastMCP server to view summary information or generate a detailed JSON report.

```
# Show text summary
fastmcp inspect server.py

# Output FastMCP JSON to stdout
fastmcp inspect server.py --format fastmcp

# Save MCP JSON to file (format required with -o)
fastmcp inspect server.py --format mcp -o manifest.json
```

### Options

OptionFlagDescriptionFormat`--format`, `-f`Output format: `fastmcp` (FastMCP-specific) or `mcp` (MCP protocol). Required when using `-o`Output File`--output`, `-o`Save JSON report to file instead of stdout. Requires `--format`

### Output Formats

#### FastMCP Format (`--format fastmcp`)

The default and most comprehensive format, includes all FastMCP-specific metadata:

- Server name, instructions, and version
- FastMCP version and MCP version
- Tool tags and enabled status
- Output schemas for tools
- Annotations and custom metadata
- Uses snake\_case field names
- **Use this for**: Complete server introspection and debugging FastMCP servers

#### MCP Protocol Format (`--format mcp`)

Shows exactly what MCP clients will see via the protocol:

- Only includes standard MCP protocol fields
- Matches output from `client.list_tools()`, `client.list_prompts()`, etc.
- Uses camelCase field names (e.g., `inputSchema`)
- Excludes FastMCP-specific fields like tags and enabled status
- **Use this for**: Debugging client visibility and ensuring MCP compatibility

### Entrypoints

The `inspect` command supports local FastMCP server files and configuration:

1. **Inferred server instance**: `server.py` - imports the module and looks for a FastMCP server instance named `mcp`, `server`, or `app`. Errors if no such object is found.
2. **Explicit server entrypoint**: `server.py:custom_name` - imports and uses the specified server entrypoint
3. **Factory function**: `server.py:create_server` - calls the specified function (sync or async) to create a server instance
4. **FastMCP configuration**: `fastmcp.json` - inspects servers defined with FastMCP’s declarative configuration

### Examples

```
# Show text summary (no JSON output)
fastmcp inspect server.py
# Output: 
# Server: MyServer
# Instructions: A helpful MCP server
# Version: 1.0.0
#
# Components:
#   Tools: 5
#   Prompts: 2
#   Resources: 3
#   Templates: 1
#
# Environment:
#   FastMCP: 2.0.0
#   MCP: 1.0.0
#
# Use --format [fastmcp|mcp] for complete JSON output

# Output FastMCP format to stdout
fastmcp inspect server.py --format fastmcp

# Specify server entrypoint
fastmcp inspect server.py:my_server

# Output MCP protocol format to stdout
fastmcp inspect server.py --format mcp

# Save to file (format required)
fastmcp inspect server.py --format fastmcp -o server-manifest.json

# Save MCP format with custom server object
fastmcp inspect server.py:my_server --format mcp -o mcp-manifest.json

# Error: format required with output file
fastmcp inspect server.py -o output.json
# Error: --format is required when using -o/--output
```

## `fastmcp project prepare`

Create a persistent uv project directory from a fastmcp.json file’s environment configuration. This allows you to pre-install all dependencies once and reuse them with the `--project` flag.

```
fastmcp project prepare fastmcp.json --output-dir ./env
```

### Options

OptionFlagDescriptionOutput Directory`--output-dir`**Required.** Directory where the persistent uv project will be created

### Usage Pattern

```
# Step 1: Prepare the environment (installs dependencies)
fastmcp project prepare fastmcp.json --output-dir ./my-env

# Step 2: Run using the prepared environment (fast, no dependency installation)
fastmcp run fastmcp.json --project ./my-env
```

The prepare command creates a uv project with:

- A `pyproject.toml` containing all dependencies from the fastmcp.json
- A `.venv` with all packages pre-installed
- A `uv.lock` file for reproducible environments

This is useful when you want to separate environment setup from server execution, such as in deployment scenarios where dependencies are installed once and the server is run multiple times.

## `fastmcp version`

Display version information about FastMCP and related components.

### Options

OptionFlagDescriptionCopy to Clipboard`--copy`Copy version information to clipboard