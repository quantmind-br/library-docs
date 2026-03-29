---
title: MCP Gateway
url: https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/
source: llms
fetched_at: 2026-01-24T14:14:01.171809698-03:00
rendered_js: false
word_count: 556
summary: The MCP Gateway is a Docker-based orchestration tool designed to manage Model Context Protocol (MCP) servers through centralized proxying and containerized isolation. It simplifies AI tool integration by handling server lifecycles, security configurations, and credential management across different environments.
tags:
    - mcp-gateway
    - model-context-protocol
    - docker-containers
    - ai-tooling
    - orchestration
    - server-lifecycle
category: guide
---

The MCP Gateway is Docker's open source solution for orchestrating Model Context Protocol (MCP) servers. It acts as a centralized proxy between clients and servers, managing configuration, credentials, and access control.

When using MCP servers without the MCP Gateway, you need to configure applications individually for each AI application. With the MCP Gateway, you configure applications to connect to the Gateway. The Gateway then handles server lifecycle, routing, and authentication across all your servers.

> If you use Docker Desktop with MCP Toolkit enabled, the Gateway runs automatically in the background. You don't need to start or configure it manually. This documentation is for users who want to understand how the Gateway works or run it directly for advanced use cases.

> E2B sandboxes now include direct access to the Docker MCP Catalog, giving developers access to over 200 tools and services to seamlessly build and run AI agents. For more information, see [E2B Sandboxes](https://docs.docker.com/ai/sandboxes/).

MCP Gateway runs MCP servers in isolated Docker containers with restricted privileges, network access, and resource usage. It includes built-in logging and call-tracing capabilities to ensure full visibility and governance of AI tool activity.

The MCP Gateway manages the server's entire lifecycle. When an AI application needs to use a tool, it sends a request to the Gateway. The Gateway identifies which server handles that tool and, if the server isn't already running, starts it as a Docker container. The Gateway then injects any required credentials, applies security restrictions, and forwards the request to the server. The server processes the request and returns the result through the Gateway back to the AI application.

The MCP Gateway solves a fundamental problem: MCP servers are just programs that need to run somewhere. Running them directly on your machine means dealing with installation, dependencies, updates, and security risks. By running them as containers managed by the Gateway, you get isolation, consistent environments, and centralized control.

To use the MCP Gateway, you'll need Docker Desktop with MCP Toolkit enabled. Follow the [MCP Toolkit guide](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/) to enable and configure servers through the graphical interface.

### [Manage the MCP Gateway from the CLI](#manage-the-mcp-gateway-from-the-cli)

With MCP Toolkit enabled, you can also interact with the MCP Gateway using the CLI. The `docker mcp` suite of commands lets you manage servers and tools directly from your terminal. You can also manually run Gateways with custom configurations, including security restrictions, server catalogs, and more.

To run an MCP Gateway manually, with customized parameters, use the `docker mcp` suite of commands.

1. Browse the [MCP Catalog](https://hub.docker.com/mcp) for a server that you want to use, and copy the install command from the **Manual installation** section.
   
   For example, run this command in your terminal to install the `duckduckgo` MCP server:
2. Connect a client, like Claude Code:
3. Run the gateway:

Now your MCP gateway is running and you can leverage all the servers set up behind it from Claude Code.

### [Install the MCP Gateway manually](#install-the-mcp-gateway-manually)

For Docker Engine without Docker Desktop, you'll need to download and install the MCP Gateway separately before you can run it.

1. Download the latest binary from the [GitHub releases page](https://github.com/docker/mcp-gateway/releases/latest).
2. Move or symlink the binary to the destination matching your OS:
   
   OSBinary destinationLinux`~/.docker/cli-plugins/docker-mcp`macOS`~/.docker/cli-plugins/docker-mcp`Windows`%USERPROFILE%\.docker\cli-plugins`
3. Make the binaries executable:

You can now use the `docker mcp` command:

For more details on how the MCP Gateway works and available customization options, see the complete documentation [on GitHub](https://github.com/docker/mcp-gateway).