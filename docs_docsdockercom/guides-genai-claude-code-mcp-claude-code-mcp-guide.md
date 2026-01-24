---
title: Generate Docker Compose Files with Claude Code and Docker MCP Toolkit
url: https://docs.docker.com/guides/genai-claude-code-mcp/claude-code-mcp-guide/
source: llms
fetched_at: 2026-01-24T14:04:52.503035788-03:00
rendered_js: false
word_count: 753
---

This guide introduces how to use Claude Code together with Docker MCP Toolkit so Claude can search Docker Hub in real time and generate a complete `docker-compose.yaml` from natural language.

Instead of manually writing YAML or looking for image tags, you describe your stack once — Claude uses the Model Context Protocol (MCP) to query Docker Hub and build a production-ready Compose file.

In this guide, you’ll learn how to:

- Enable Docker MCP Toolkit in Docker Desktop
- Add the Docker Hub MCP server
- Connect Claude Code to the MCP Gateway (GUI or CLI)
- Verify MCP connectivity inside Claude
- Ask Claude to generate and save a Compose file for a Node.js + PostgreSQL app
- Deploy it instantly with `docker compose up`

* * *

- **Setup**: Enable MCP Toolkit → Add Docker Hub MCP server → Connect Claude Code
- **Use Claude**: Describe your stack in plain English
- **Automate**: Claude queries Docker Hub via MCP and builds a complete `docker-compose.yaml`
- **Deploy**: Run `docker compose up` → Node.js + PostgreSQL live on `localhost:3000`
- **Benefit**: Zero YAML authoring. Zero image searching. Describe once → Claude builds it.

**Estimated time**: ~15 minutes

* * *

The goal is simple: use Claude Code together with the Docker MCP Toolkit to search Docker Hub images and generate a complete Docker Compose file for a Node.js and PostgreSQL setup.

The Model Context Protocol (MCP) bridges Claude Code and Docker Desktop, giving Claude real-time access to Docker's tools. Instead of context-switching between Docker, terminal commands, and YAML editors, you describe your requirements once and Claude handles the infrastructure details.

**Why this matters:** This pattern scales to complex multi-service setups, database migrations, networking, security policies — all through conversational prompts.

* * *

Make sure you have:

- Docker Desktop installed
- Enable Docker Desktop updated with [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/get-started/#setup) support
- Claude Code installed

* * *

1. Open **Docker Desktop**
2. Select **MCP Toolkit**
3. Go to the **Catalog** tab
4. Search for **Docker Hub**
5. Select the **Docker Hub**MCP server
6. Add the MCP server, then open the **Configuration** tab
7. Enter your Docker Hub username
8. [Create a read-only personal access token](https://docs.docker.com/security/access-tokens/#create-a-personal-access-token) and enter your access token under **Secrets**
9. Save the configuration

![Docker Hub](https://docs.docker.com/guides/genai-claude-code-mcp/Images/catalog_docker_hub.avif)

Docker Hub

![Docker Hub](https://docs.docker.com/guides/genai-claude-code-mcp/Images/catalog_docker_hub.avif)

Public images work without credentials. For private repositories, you can add your Docker Hub username and token later.

![Docker Hub Secrets](https://docs.docker.com/guides/genai-claude-code-mcp/Images/dockerhub_secrets.avif)

Docker Hub Secrets

![Docker Hub Secrets](https://docs.docker.com/guides/genai-claude-code-mcp/Images/dockerhub_secrets.avif)

* * *

You can connect from Docker Desktop or using the CLI.

### [Option A. Connect with Docker Desktop](#option-a-connect-with-docker-desktop)

1. Open **MCP Toolkit**
2. Go to the **Clients** tab
3. Locate **Claude Code**
4. Select **Connect**

![Docker Connection](https://docs.docker.com/guides/genai-claude-code-mcp/Images/docker-connect-claude.avif)

![Docker Connection](https://docs.docker.com/guides/genai-claude-code-mcp/Images/docker-connect-claude.avif)

### [Option B. Connect using the CLI](#option-b-connect-using-the-cli)

* * *

1. Navigate to your project folder:

<!--THE END-->

1. Start Claude Code:

<!--THE END-->

1. In the input box, type:

You should now see:

- The MCP gateway (for example `MCP_DOCKER`)
- Tools provided by the Docker Hub MCP server

![mcp-docker](https://docs.docker.com/guides/genai-claude-code-mcp/Images/mcp-servers.avif)

![mcp-docker](https://docs.docker.com/guides/genai-claude-code-mcp/Images/mcp-servers.avif)

If not, restart Claude Code or check Docker Desktop to confirm the connection.

* * *

Claude Code generates more accurate Compose files when it can inspect a real project. Set up the application code now so the agent can bind mount it later.

Inside project folder, create a folder named `app`:

Create `index.js`:

Add a start script to `package.json`:

Return to your project root (`cd ..`) once the app is ready.

* * *

Paste this message into Claude Code:

Claude will search images through MCP, inspect the `app` directory, and generate a Compose file that mounts and runs your local code.

* * *

Tell Claude:

You should see something like this:

* * *

From your project root:

Docker will:

- Pull the Node and Postgres images selected through Docker Hub MCP
- Create networks and volumes
- Start the containers

Open your browser:

![Local Host](https://docs.docker.com/guides/genai-claude-code-mcp/Images/Localhost.avif)

![Local Host](https://docs.docker.com/guides/genai-claude-code-mcp/Images/Localhost.avif)

Your Node.js app should now be running.

* * *

By combining Claude Code with the Docker MCP Toolkit, Docker Desktop, and the Docker Hub MCP server, you can describe your stack in natural language and let MCP handle the details. This removes context switching and replaces it with a smooth, guided workflow powered by model context protocol integrations.

* * *

### [Next steps](#next-steps)

- Explore the 220+ MCP servers available in the [Docker MCP catalog](https://hub.docker.com/mcp)
- Connect Claude Code to your databases, internal APIs, and team tools
- Share your MCP setup with your team so everyone works consistently

The future of development is not about switching between tools. It is about tools working together in a simple, safe, and predictable way. The Docker MCP Toolkit brings that future into your everyday workflow.

- **[Explore the MCP Catalog](https://hub.docker.com/mcp):** Discover containerized, security-hardened MCP servers
- **[Get started with MCP Toolkit in Docker Desktop](https://hub.docker.com/open-desktop?url=https%3A%2F%2Fopen.docker.com%2Fdashboard%2Fmcp):** Requires version 4.48 or newer to launch automatically
- **[Read the MCP Horror Stories series](https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/):** Learn about common MCP security pitfalls and how to avoid them