---
title: MCP Catalog
url: https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/
source: llms
fetched_at: 2026-01-24T14:13:54.458484008-03:00
rendered_js: false
word_count: 519
summary: This document introduces the Docker MCP Catalog, a centralized registry for discovering and running Model Context Protocol (MCP) servers as containerized tools. It details the benefits of using containerized MCP servers, the differences between local and remote servers, and how to contribute to the registry.
tags:
    - docker-mcp-catalog
    - mcp-server
    - model-context-protocol
    - containerization
    - docker-hub
    - ai-tools
category: reference
---

## Docker MCP Catalog

The [Docker MCP Catalog](https://hub.docker.com/mcp) is a centralized, trusted registry for discovering, sharing, and running MCP-compatible tools. Integrated with Docker Hub, it offers verified, versioned, and curated MCP servers packaged as Docker images. The catalog is also available in Docker Desktop.

The catalog solves common MCP server challenges:

- Environment conflicts. Tools often need specific runtimes that might clash with existing setups.
- Lack of isolation. Traditional setups risk exposing the host system.
- Setup complexity. Manual installation and configuration slow adoption.
- Inconsistency across platforms. Tools might behave unpredictably on different operating systems.

With Docker, each MCP server runs as a self-contained container. This makes it portable, isolated, and consistent. You can launch tools instantly using the Docker CLI or Docker Desktop, without worrying about dependencies or compatibility.

- Extensive collection of verified MCP servers in one place.
- Publisher verification and versioned releases.
- Pull-based distribution using Docker infrastructure.
- Tools provided by partners such as New Relic, Stripe, Grafana, and more.

> E2B sandboxes now include direct access to the Docker MCP Catalog, giving developers access to over 200 tools and services to seamlessly build and run AI agents. For more information, see [E2B Sandboxes](https://docs.docker.com/ai/sandboxes/).

Each tool in the MCP Catalog is packaged as a Docker image with metadata.

- Discover tools on Docker Hub under the `mcp/` namespace.
- Connect tools to your preferred agents with simple configuration through the [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/).
- Pull and run tools using Docker Desktop or the CLI.

Each catalog entry displays:

- Tool description and metadata.
- Version history.
- List of tools provided by the MCP server.
- Example configuration for agent integration.

The Docker MCP Catalog supports both local and remote server deployments, each optimized for different use cases and requirements.

### [Local MCP servers](#local-mcp-servers)

Local MCP servers are containerized applications that run directly on your machine. All local servers are built and digitally signed by Docker, providing enhanced security through verified provenance and integrity. These servers run as containers on your local environment and function without internet connectivity once downloaded. Local servers display a Docker icon ![docker whale icon](https://docs.docker.com/desktop/images/whale-x.svg) to indicate they are built by Docker.

Local servers offer predictable performance, complete data privacy, and independence from external service availability. They work well for development workflows, sensitive data processing, and scenarios requiring offline functionality.

### [Remote MCP servers](#remote-mcp-servers)

Remote MCP servers are hosted services that run on the provider's infrastructure and connect to external services like GitHub, Notion, and Linear. Many remote servers use OAuth authentication. When a remote server requires OAuth, the MCP Toolkit handles authentication automatically - you authorize access through your browser, and the Toolkit manages credentials securely. You don't need to manually create API tokens or configure authentication.

Remote servers display a cloud icon in the catalog. For setup instructions, see [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/#oauth-authentication).

To use an MCP server from the catalog, see [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/).

The MCP server registry is available at [https://github.com/docker/mcp-registry](https://github.com/docker/mcp-registry). To submit an MCP server, follow the [contributing guidelines](https://github.com/docker/mcp-registry/blob/main/CONTRIBUTING.md).

When your pull request is reviewed and approved, your MCP server is available within 24 hours on:

- Docker Desktop's [MCP Toolkit feature](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/).
- The [Docker MCP Catalog](https://hub.docker.com/mcp).
- The [Docker Hub](https://hub.docker.com/u/mcp) `mcp` namespace (for MCP servers built by Docker).