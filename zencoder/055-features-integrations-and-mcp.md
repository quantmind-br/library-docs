---
title: Integrations and MCP - Zencoder Docs
url: https://docs.zencoder.ai/features/integrations-and-mcp
source: crawler
fetched_at: 2026-01-23T09:28:07.569444669-03:00
rendered_js: false
word_count: 437
summary: This document outlines the three primary integration paths for Zencoder, including native integrations, a browser extension, and support for the Model Context Protocol (MCP) to connect with external data sources.
tags:
    - zencoder-integration
    - jira-integration
    - chrome-extension
    - model-context-protocol
    - developer-workflow
    - agent-tools
category: guide
---

## Overview

Zencoder doesn’t replace your toolkit—it enhances it by connecting your existing tools in ways that match your workflow. With three flexible integration paths, Zencoder eliminates context switching and brings your entire development ecosystem together, saving you valuable time and maintaining your focus.

## Integration Paths

Zencoder offers three powerful ways to connect with your development tools and workflows:

## Built-in Native Integrations

Our native integrations are built directly into the Zencoder experience, providing seamless connectivity with essential development tools.

### Add Jira Integration

Our first native integration connects Zencoder with Jira, allowing you to:

- Pull ticket details directly into your IDE without tab-juggling
- Access full context right where you’re coding
- Mention Jira tickets in chat to automatically pull in relevant information

## Chrome Extension

Not everything happens in your IDE. Our [Chrome extension](https://chromewebstore.google.com/detail/zencoder/obkkfjgjhdkjnkleopbljciifoefhnbp) connects Zencoder to over 20 development, DevOps, project management, and monitoring tools across your entire workflow.

### Install Chrome Extension

1. Adds a Zencoder button wherever developers work online
2. Captures relevant context when clicked (error stack traces, PR descriptions, etc.)
3. Sends that context directly to your IDE without manual copy/pasting

### Supported Tools

## Model Context Protocol (MCP)

For power users who need even more connectivity, Zencoder supports the Model Context Protocol (MCP)—an open standard that bridges AI assistants with external data sources and tools.

### What is MCP?

MCP is essentially the “USB-C of the AI world”—a universal standard for connecting LLMs to various data sources and tooling. It provides a consistent way to plug an AI model into databases, APIs, and applications, replacing fragmented one-off integrations with a single protocol.

### How Zencoder Uses MCP

In MCP terms, Zencoder acts as an **MCP client** (or host) that can connect to one or more **MCP servers**. These servers are lightweight connectors that expose specific capabilities or data sources through the MCP standard.

### MCP Protocol Support

Zencoder supports multiple MCP connection protocols and approaches to ensure maximum compatibility with different server implementations:

- **Standard stdio communication**: For local MCP servers running as subprocesses
- **Streamable HTTP connections**: For remote MCP servers using HTTP-based communication
- **OAuth2 authentication**: For secure authentication with third-party services requiring OAuth2 flows

This expanded protocol support means you can connect to a wider range of MCP servers, including:

- Cloud-based MCP servers that require OAuth authentication
- Remote MCP servers using HTTP streaming
- Traditional local MCP servers using standard input/output communication
- Enterprise services with secure OAuth2-based authentication requirements

### Managing Agent Tools and MCP Servers

Zencoder now provides a streamlined way to manage your **Agent Tools**, including MCP servers, directly through the **Agent Tools** menu. This new interface makes it easier to discover, install, and manage your tools without having to edit configuration files manually.