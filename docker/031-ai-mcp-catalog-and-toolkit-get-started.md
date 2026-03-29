---
title: Get started
url: https://docs.docker.com/ai/mcp-catalog-and-toolkit/get-started/
source: llms
fetched_at: 2026-01-24T14:13:57.346350139-03:00
rendered_js: false
word_count: 1184
summary: This document provides a guide for setting up and using the Docker MCP Toolkit to manage containerized Model Context Protocol (MCP) servers and connect them to various AI agents and clients.
tags:
    - docker
    - mcp-toolkit
    - model-context-protocol
    - ai-agents
    - docker-desktop
category: tutorial
---

## Get started with Docker MCP Toolkit

The Docker MCP Toolkit makes it easy to set up, manage, and run containerized Model Context Protocol (MCP) servers, and connect them to AI agents. It provides secure defaults and support for a growing ecosystem of LLM-based clients. This page shows you how to get started quickly with the Docker MCP Toolkit.

Before you begin, make sure you meet the following requirements to get started with Docker MCP Toolkit.

1. Download and install the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).
2. Open the Docker Desktop settings and select **Beta features**.
3. Select **Enable Docker MCP Toolkit**.
4. Select **Apply**.

The **Learning center** in Docker Desktop provides walkthroughs and resources to help you get started with Docker products and features. On the **MCP Toolkit** page, the **Get started** walkthrough that guides you through installing an MCP server, connecting a client, and testing your setup.

Alternatively, follow the step-by-step instructions on this page to:

- [Install MCP servers](#install-mcp-servers)
- [Connect clients](#connect-clients)
- [Verify connections](#verify-connections)

<!--THE END-->

1. In Docker Desktop, select **MCP Toolkit** and select the **Catalog** tab.
2. Search for the **GitHub Official** server from the catalog and then select the plus icon to add it.
3. In the **GitHub Official** server page, select the **Configuration** tab and select **OAuth**.
   
   > The type of configuration required depends on the server you select. For the GitHub Official server, you must authenticate using OAuth.
   
   Your browser opens the GitHub authorization page. Follow the on-screen instructions to [authenticate via OAuth](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/#authenticate-via-oauth).
4. Return to Docker Desktop when the authentication process is complete.
5. Search for the **Playwright** server from the catalog and add it.

<!--THE END-->

1. Add the GitHub Official MCP server. Run:
2. Authenticate the server by running the following command:
   
   > The type of configuration required depends on the server you select. For the GitHub Official server, you must authenticate using OAuth.
   
   Your browser opens the GitHub authorization page. Follow the on-screen instructions to [authenticate via OAuth](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/#authenticate-via-oauth).
3. Add the **Playwright** server. Run:

You’ve now successfully added an MCP server. Next, connect an MCP client to use the MCP Toolkit in an AI application.

To connect a client to MCP Toolkit:

1. In Docker Desktop, select **MCP Toolkit** and select the **Clients** tab.
2. Find your application in the list.
3. Select **Connect** to configure the client.

If your client isn't listed, you can connect the MCP Toolkit manually over `stdio` by configuring your client to run the following command:

For example, if your client uses a JSON file to configure MCP servers, you may add an entry like:

Consult the documentation of the application you're using for instructions on how to set up MCP servers manually.

Refer to the relevant section for instructions on how to verify that your setup is working:

- [Claude Code](#claude-code)
- [Claude Desktop](#claude-desktop)
- [OpenAI Codex](#codex)
- [Continue](#continue)
- [Cursor](#cursor)
- [Gemini](#gemini)
- [Goose](#goose)
- [Gordon](#gordon)
- [LM Studio](#lm-studio)
- [OpenCode](#opencode)
- [Sema4.ai](#sema4)
- [Visual Studio Code](#vscode)
- [Zed](#zed)

### [Claude Code](#claude-code)

If you configured the MCP Toolkit for a specific project, navigate to the relevant project directory. Then run `claude mcp list`. The output should show `MCP_DOCKER` with a "connected" status:

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

### [Claude Desktop](#claude-desktop)

Restart Claude Desktop and check the **Search and tools** menu in the chat input. You should see the `MCP_DOCKER` server listed and enabled:

![Claude Desktop](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/claude-desktop.avif)

![Claude Desktop](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/claude-desktop.avif)

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

### [Codex](#codex)

Run `codex mcp list` to view active MCP servers and their statuses. The `MCP_DOCKER` server should appear in the list with an "enabled" status:

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

### [Continue](#continue)

Launch the Continue terminal UI by running `cn`. Use the `/mcp` command to view active MCP servers and their statuses. The `MCP_DOCKER` server should appear in the list with a "connected" status:

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

### [Cursor](#cursor)

Open Cursor. If you configured the MCP Toolkit for a specific project, open the relevant project directory. Then navigate to **Cursor Settings &gt; Tools & MCP**. You should see `MCP_DOCKER` under **Installed MCP Servers**:

![Cursor](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/cursor.avif)

![Cursor](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/cursor.avif)

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

### [Gemini](#gemini)

Run `gemini mcp list` to view active MCP servers and their statuses. The `MCP_DOCKER` should appear in the list with a "connected" status.

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

### [Goose](#goose)

Open the Goose desktop application and select **Extensions** in the sidebar. Under **Enabled Extensions**, you should see an extension named `Mcpdocker`:

![Goose desktop app](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/goose.avif)

![Goose desktop app](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/goose.avif)

Run `goose info -v` and look for an entry named `mcpdocker` under extensions. The status should show `enabled: true`:

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

### [Gordon](#gordon)

Open the **Ask Gordon** view in Docker Desktop and select the toolbox icon in the chat input area. The **MCP Toolkit** tab shows whether MCP Toolkit is enabled and displays all the provided tools:

![MCP Toolkit in the Ask Gordon UI](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/ask-gordon.avif)

![MCP Toolkit in the Ask Gordon UI](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/ask-gordon.avif)

Test the connection by submitting a prompt that invokes one of your installed MCP servers, either directly in Docker Desktop or using the CLI:

### [LM Studio](#lm-studio)

Restart LM Studio and start a new chat. Open the integrations menu and look for an entry named `mcp/mcp-docker`. Use the toggle to enable the server:

![LM Studio](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/lm-studio.avif)

![LM Studio](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/lm-studio.avif)

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

### [OpenCode](#opencode)

The OpenCode configuration file (at `~/.config/opencode/opencode.json` by default) contains the setup for MCP Toolkit:

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

### [Sema4.ai Studio](#sema4)

In Sema4.ai Studio, select **Actions** in the sidebar, then select the **MCP Servers** tab. You should see Docker MCP Toolkit in the list:

![Docker MCP Toolkit in Sema4.ai Studio](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/sema4-mcp-list.avif)

![Docker MCP Toolkit in Sema4.ai Studio](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/sema4-mcp-list.avif)

To use MCP Toolkit with Sema4.ai, add it as an agent action. Find the agent you want to connect to the MCP Toolkit and open the agent editor. Select **Add Action**, enable Docker MCP Toolkit in the list, then save your agent:

![Editing an agent in Sema4.ai Studio](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/sema4-edit-agent.avif)

![Editing an agent in Sema4.ai Studio](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/sema4-edit-agent.avif)

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

### [Visual Studio Code](#vscode)

Open Visual Studio Code. If you configured the MCP Toolkit for a specific project, open the relevant project directory. Then open the **Extensions** pane. You should see the `MCP_DOCKER` server listed under installed MCP servers.

![MCP_DOCKER installed in Visual Studio Code](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/vscode-extensions.avif)

![MCP_DOCKER installed in Visual Studio Code](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/vscode-extensions.avif)

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

### [Zed](#zed)

Launch Zed and open agent settings:

![Opening Zed agent settings from command palette](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/zed-cmd-palette.avif)

![Opening Zed agent settings from command palette](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/zed-cmd-palette.avif)

Ensure that `MCP_DOCKER` is listed and enabled in the MCP Servers section:

![MCP_DOCKER in Zed's agent settings](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/zed-agent-settings.avif)

![MCP_DOCKER in Zed's agent settings](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/zed-agent-settings.avif)

Test the connection by submitting a prompt that invokes one of your installed MCP servers:

- [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/)
- [MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/)
- [MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/)