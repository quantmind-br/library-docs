---
title: Integration Ecosystem - Connecting Your Development Workflow - Zencoder Docs
url: https://docs.zencoder.ai/learn/enterprise-best-practices/integration-ecosystem
source: crawler
fetched_at: 2026-01-23T09:28:25.043007172-03:00
rendered_js: false
word_count: 365
summary: This document explains how to integrate and manage Model Context Protocol (MCP) servers within Zencoder, covering library installation, custom configurations, and agent-specific inheritance rules.
tags:
    - mcp
    - zencoder
    - agent-configuration
    - tool-integration
    - authentication
    - custom-mcp
category: guide
---

What is the easiest way to add an MCP in Zencoder, from the library?

Open the three-dot menu → Tools → MCP Library, search the curated list, and pick a server that does not require credentials (like Context7). The detail pane shows the official repo plus the server command, and clicking *Install* adds it to your workspace instantly. Every built-in Zencoder agent (Code, Unit Test, etc.) inherits that MCP by default, so you can call its tools without configuring tokens or custom settings.

How to add a custom MCP in Zencoder?

Go to Tools → Add custom MCP, give the integration a recognizable name, and paste the MCP server config—the same JSON/command snippet the maintainer documents (e.g., the GitHub or Context7 examples). Click *Install* and it joins your custom tools list. Zencoder’s built-in agents automatically inherit it, while custom Zen agents still need you to toggle it on (during creation or afterward) so you can control exactly which bespoke agents get access.

What types of MCP authentication can we find?

Local MCPs simply inherit whatever secrets you have on your machine (env vars, CLI logins, keychains), but remote MCPs put an extra door in front of the server. Some are open (no auth), others expect a static API key or bearer token, and increasingly you will see OAuth/device-code flows where the MCP shows a login link and you sign in before it issues a short-lived token. Enterprise deployments may go further with company SSO, mutual TLS certificates, or signed requests so only managed devices can connect; after that check passes, the MCP uses its own stored credentials (e.g., GitHub or AWS keys) to run the tools.

How are MCPs added differently to Zencoder agents vs. custom agents?

Every MCP you install in Tools flows automatically into the built-in Zencoder agents (Code, Unit Test, etc.) and cannot be removed there—Ask is the lone exception because it stays intentionally lightweight. Custom Zen agents, on the other hand, start with no extra MCPs; you add or remove them one by one in each agent’s tool configuration. Because the defaults inherit everything, it is worth pruning unused MCPs in Tools periodically so those core agents do not become bloated.