---
title: MCP Toolkit
url: https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/
source: llms
fetched_at: 2026-01-24T14:14:08.318870485-03:00
rendered_js: false
word_count: 979
summary: The Docker MCP Toolkit is a management interface in Docker Desktop for deploying and managing containerized Model Context Protocol (MCP) servers and connecting them to AI agents. It provides a secure, zero-setup environment for tool discovery and execution across multiple LLM-based clients.
tags:
    - docker-desktop
    - mcp-protocol
    - ai-agents
    - containerization
    - mcp-server
    - security
    - oauth
category: guide
---

## Docker MCP Toolkit

The Docker MCP Toolkit is a management interface integrated into Docker Desktop that lets you set up, manage, and run containerized MCP servers and connect them to AI agents. It removes friction from tool usage by offering secure defaults, easy setup, and support for a growing ecosystem of LLM-based clients. It is the fastest way from MCP tool discovery to local execution.

- Cross-LLM compatibility: Works with Claude, Cursor, and other MCP clients.
- Integrated tool discovery: Browse and launch MCP servers from the Docker MCP Catalog directly in Docker Desktop.
- Zero manual setup: No dependency management, runtime configuration, or setup required.
- Functions as both an MCP server aggregator and a gateway for clients to access installed MCP servers.

> The MCP Toolkit includes [Dynamic MCP](https://docs.docker.com/ai/mcp-catalog-and-toolkit/dynamic-mcp/), which enables AI agents to discover, add, and compose MCP servers on-demand during conversations, without manual configuration. Your agent can search the catalog and add tools as needed when you connect to the gateway.

MCP introduces two core concepts: MCP clients and MCP servers.

- MCP clients are typically embedded in LLM-based applications, such as the Claude Desktop app. They request resources or actions.
- MCP servers are launched by the client to perform the requested tasks, using any necessary tools, languages, or processes.

Docker standardizes the development, packaging, and distribution of applications, including MCP servers. By packaging MCP servers as containers, Docker eliminates issues related to isolation and environment differences. You can run a container directly, without managing dependencies or configuring runtimes.

Depending on the MCP server, the tools it provides might run within the same container as the server or in dedicated containers for better isolation.

The Docker MCP Toolkit combines passive and active measures to reduce attack surfaces and ensure safe runtime behavior.

### [Passive security](#passive-security)

Passive security refers to measures implemented at build-time, when the MCP server code is packaged into a Docker image.

- Image signing and attestation: All MCP server images under `mcp/` in the [MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/) are built by Docker and digitally signed to verify their source and integrity. Each image includes a Software Bill of Materials (SBOM) for full transparency.

### [Active security](#active-security)

Active security refers to security measures at runtime, before and after tools are invoked, enforced through resource and access limitations.

- CPU allocation: MCP tools are run in their own container. They are restricted to 1 CPU, limiting the impact of potential misuse of computing resources.
- Memory allocation: Containers for MCP tools are limited to 2 GB.
- Filesystem access: By default, MCP Servers have no access to the host filesystem. The user explicitly selects the servers that will be granted file mounts.
- Interception of tool requests: Requests to and from tools that contain sensitive information such as secrets are blocked.

### [OAuth authentication](#oauth-authentication)

Some MCP servers require authentication to access external services like GitHub, Notion, and Linear. The MCP Toolkit handles OAuth authentication automatically. You authorize access through your browser, and the Toolkit manages credentials securely. You don't need to manually create API tokens or configure authentication for each service.

1. In Docker Desktop, go to **MCP Toolkit** and select the **Catalog** tab.
2. Find and add an MCP server that requires OAuth.
3. In the server's **Configuration** tab, select the **OAuth** authentication method. Follow the link to begin the OAuth authorization.
4. Your browser opens the authorization page for the service. Follow the on-screen instructions to complete authentication.
5. Return to Docker Desktop when authentication is complete.

View all authorized services in the **OAuth** tab. To revoke access, select **Revoke** next to the service you want to disconnect.

Enable an MCP server:

If the server requires OAuth, authorize the connection:

Your browser opens the authorization page. Complete the authentication process, then return to your terminal.

View authorized services:

Revoke access to a service:

### [Example: Use the GitHub Official MCP server with Ask Gordon](#example-use-the-github-official-mcp-server-with-ask-gordon)

To illustrate how the MCP Toolkit works, here's how to enable the GitHub Official MCP server and use [Ask Gordon](https://docs.docker.com/ai/gordon/) to interact with your GitHub account:

1. From the **MCP Toolkit** menu in Docker Desktop, select the **Catalog** tab and find the **GitHub Official** server and add it.
2. In the server's **Configuration** tab, authenticate via OAuth.
3. In the **Clients** tab, ensure Gordon is connected.
4. From the **Ask Gordon** menu, you can now send requests related to your GitHub account, in accordance to the tools provided by the GitHub Official server. To test it, ask Gordon:
   
   Make sure to allow Gordon to interact with GitHub by selecting **Always allow** in Gordon's answer.

> The Gordon client is enabled by default, which means Gordon can automatically interact with your MCP servers.

### [Example: Use Claude Desktop as a client](#example-use-claude-desktop-as-a-client)

Imagine you have Claude Desktop installed, and you want to use the GitHub MCP server, and the Puppeteer MCP server, you do not have to install the servers in Claude Desktop. You can simply install these 2 MCP servers in the MCP Toolkit, and add Claude Desktop as a client:

1. From the **MCP Toolkit** menu, select the **Catalog** tab and find the **Puppeteer** server and add it.
2. Repeat for the **GitHub Official** server.
3. From the **Clients** tab, select **Connect** next to **Claude Desktop**. Restart Claude Desktop if it's running, and it can now access all the servers in the MCP Toolkit.
4. Within Claude Desktop, run a test by submitting the following prompt using the Sonnet 3.5 model:

### [Example: Use Visual Studio Code as a client](#example-use-visual-studio-code-as-a-client)

You can interact with all your installed MCP servers in Visual Studio Code:

1. To enable the MCP Toolkit:
   
   1. Insert the following in your Visual Studio Code's User `mcp.json`:
   
   <!--THE END-->
   
   1. In your terminal, navigate to your project's folder.
   2. Run:
      
      > This command creates a `.vscode/mcp.json` file in the current directory. As this is a user-specific file, add it to your `.gitignore` file to prevent it from being committed to the repository.
2. In Visual Studio Code, open a new Chat and select the **Agent** mode:
   
   ![Copilot mode switching](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/copilot-mode.png)
   
   ![Copilot mode switching](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/copilot-mode.png)
3. You can also check the available MCP tools:
   
   ![Displaying tools in VSCode](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/tools.png)
   
   ![Displaying tools in VSCode](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/tools.png)

For more information about the Agent mode, see the [Visual Studio Code documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode).

- [MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/)
- [MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/)