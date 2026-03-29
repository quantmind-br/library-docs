---
title: Security FAQs
url: https://docs.docker.com/ai/mcp-catalog-and-toolkit/faqs/
source: llms
fetched_at: 2026-01-24T14:13:57.997589307-03:00
rendered_js: false
word_count: 515
summary: This document provides answers to frequently asked questions about the security, verification processes, and credential management for the Docker MCP Catalog and Toolkit.
tags:
    - docker-mcp
    - security-faq
    - credential-management
    - mcp-catalog
    - server-verification
    - mcp-gateway
    - secret-storage
category: reference
---

Docker MCP Catalog and Toolkit is a solution for securely building, sharing, and running MCP tools. This page answers common questions about MCP Catalog and Toolkit security.

### [What process does Docker follow to add a new MCP server to the catalog?](#what-process-does-docker-follow-to-add-a-new-mcp-server-to-the-catalog)

Developers can submit a pull request to the [Docker MCP Registry](https://github.com/docker/mcp-registry) to propose new servers. Docker provides detailed [contribution guidelines](https://github.com/docker/mcp-registry/blob/main/CONTRIBUTING.md) to help developers meet the required standards.

Currently, a majority of the servers in the catalog are built directly by Docker. Each server includes attestations such as:

- Build attestation: Servers are built on Docker Build Cloud.
- Source provenance: Verifiable source code origins.
- Signed SBOMs: Software Bill of Materials with cryptographic signatures.

> When using the images with [Docker MCP gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/), you can verify attestations at runtime using the `docker mcp gateway run --verify-signatures` CLI command.

In addition to Docker-built servers, the catalog includes select servers from trusted registries such as GitHub and HashiCorp. Each third-party server undergoes a verification process that includes:

- Pulling and building the code in an ephemeral build environment.
- Testing initialization and functionality.
- Verifying that tools can be successfully listed.

### [Under what conditions does Docker reject MCP server submissions?](#under-what-conditions-does-docker-reject-mcp-server-submissions)

Docker rejects MCP server submissions that fail automated testing and validation processes during pull request review. Additionally, Docker reviewers evaluate submissions against specific requirements and reject MCP servers that don't meet these criteria.

### [Does Docker take accountability for malicious MCP servers in the Toolkit?](#does-docker-take-accountability-for-malicious-mcp-servers-in-the-toolkit)

Docker’s security measures currently represent a best-effort approach. While Docker implements automated testing, scanning, and metadata extraction for each server in the catalog, these security measures are not yet exhaustive. Docker is actively working to enhance its security processes and expand testing coverage. Enterprise customers can contact their Docker account manager for specific security requirements and implementation details.

### [How are credentials managed for MCP servers?](#how-are-credentials-managed-for-mcp-servers)

Starting with Docker Desktop version 4.43.0, credentials are stored securely in the Docker Desktop VM. The storage implementation depends on the platform (for example, macOS, WSL2). You can manage the credentials using the following CLI commands:

- `docker mcp secret ls` - List stored credentials
- `docker mcp secret rm` - Remove specific credentials
- `docker mcp oauth revoke` - Revoke OAuth-based credentials

In the upcoming versions of Docker Desktop, Docker plans to support pluggable storage for these secrets and additional out-of-the-box storage providers to give users more flexibility in managing credentials.

### [Are credentials removed when an MCP server is uninstalled?](#are-credentials-removed-when-an-mcp-server-is-uninstalled)

No. MCP servers are not technically uninstalled since they exist as Docker containers pulled to your local Docker Desktop. Removing an MCP server stops the container but leaves the image on your system. Even if the container is deleted, credentials remain stored until you remove them manually.

### [Why don't I see remote MCP servers in the catalog?](#why-dont-i-see-remote-mcp-servers-in-the-catalog)

If remote MCP servers aren't visible in the Docker Desktop catalog, your local catalog may be out of date. Remote servers are indicated by a cloud icon and include services like GitHub, Notion, and Linear.

Update your catalog by running:

After the update completes, refresh the **Catalog** tab in Docker Desktop.

- [Get started with MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/get-started/)
- [Open-source MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/)