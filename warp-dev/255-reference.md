---
title: "Technical reference"
url: https://docs.warp.dev/reference
source: sitemap
fetched_at: 2026-04-29T15:04:58-03:00
rendered_js: false
word_count: 184
summary: This document provides an overview of the programmatic interfaces for managing Oz agents, including the command-line interface, API, and language-specific SDKs.
tags:
    - cli
    - agent-management
    - api-integration
    - automation
    - sdk
    - ci-cd-pipelines
category: reference
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Technical Reference

Programmatic interfaces for running and managing Oz agents in CI pipelines, scripts, backend services, and custom tooling.

## CLI

The [Oz CLI](https://docs.warp.dev/reference/cli/cli) runs and configures agents from any environment — locally, in CI, or on remote machines.

- [[157-reference-cli-api-keys|API Keys]] — Create and manage API keys for CLI authentication (ideal for CI pipelines, headless servers, containers)
- [[156-reference-cli-agent-profiles|Agent Profiles]] — Control what agents can access, how they behave, and where they act
- [[159-reference-cli-mcp-servers|MCP Servers]] — Pass MCP server configuration via `--mcp` flag (UUID, inline JSON, or file path)
- [[160-reference-cli-skills|Skills]] — Run agents from reusable instruction sets in repositories using `--skill`
- [[161-reference-cli-warp-drive|Warp Drive Context]] — Reference saved prompts, notebooks, workflows, and rules from Warp Drive
- [[153-reference-cli-integration-setup|Integration Setup]] — Configure environments and connect tools (Slack, Linear) to trigger agents externally
- [[278-reference-cli-troubleshooting|Troubleshooting]] — Solutions for authentication issues, agent failures, environment problems, Docker image issues

## API & SDK

The [Oz API](https://docs.warp.dev/reference/api-and-sdk/agent) creates and monitors cloud agent runs over HTTP. Official SDKs provide typed clients with built-in retries and error handling:

- [Python SDK](https://github.com/warpdotdev/oz-sdk-python)
- [TypeScript SDK](https://github.com/warpdotdev/oz-sdk-typescript)

#reference #cli #sdk
