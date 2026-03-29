---
title: May 2025 - Zencoder Docs
url: https://docs.zencoder.ai/changelog/may-2025
source: crawler
fetched_at: 2026-01-23T09:28:23.325449785-03:00
rendered_js: false
word_count: 644
summary: This document outlines the May 2025 launch of the Zen Agents platform, providing details on new features like the MCP Library, Agent Marketplace, and collaborative tools for development teams.
tags:
    - zen-agents
    - mcp-library
    - ai-agents
    - release-notes
    - model-context-protocol
    - ide-integration
category: other
---

## Zen Agents Platform with MCP Library and Marketplace Launch

May 2025 marks a significant milestone in Zencoder’s evolution with the launch of our Zen Agents platform including our MCP Library and Marketplace. Releases from this month transform Zencoder from an individual productivity tool into a collaborative platform empowering entire development teams to create, share, and discover specialized AI agents and tools. Here’s what we’ve been working on:

## New Features

### Zen Agents Platform

Our [AI Agents](https://docs.zencoder.ai/features/ai-agents) (also known as Zen Agents) platform brings powerful customization and sharing capabilities to your development workflow:

- **Agent Sharing** - Users can now share custom agents with all other users in their organization
- **Custom Agent Registry** - We migrated the registry of custom agents to our backend, enabling synchronization across all your devices and IDEs
- **Tool Configuration** - You can now easily configure and save the tools available to custom agents (Zencoder agents use all available tools by default)

[**Learn More About AI Agents**  
\
Explore how to create, customize, and share AI agents with your team](https://docs.zencoder.ai/features/ai-agents)

### MCP Library and Tools Management

We’ve introduced a centralized way to manage and discover Model Context Protocol (MCP) servers and agent tools within Zencoder:

- **Agent Tools Section** - Bringing together all tools used by agents in a dedicated UI for managing all tools
- **MCP Library** - It’s a built-in library currently featuring 100+ of the most useful MCP servers for engineers, ready to enable for your agents (plus you can add your own custom MCPs, as needed)
- **Project-Level Installation** - MCP servers are now installed at the project level by default, simplifying configuration

[**Learn About MCP Library**  
\
Discover how to browse, install, and manage MCP servers through our new Agent Tools interface](https://docs.zencoder.ai/features/integrations-and-mcp#agent-tools-ui-suggested)

### Zen Agents Marketplace

Going beyond the scope of the IDE - we’ve launched an open marketplace where you can discover and share specialized AI agents:

- **Browse Specialized Agents** - Explore 20+ purpose-built agents covering the entire software development lifecycle
- **Community Contributions** - Go ahead and submit your own agents to our [open-source repository](https://github.com/zencoderai/zenagents-library)
- **Available in both IDEs and on the website** - Both IDEs and the website offer access to the same MCP and AI agents lists

### Change Management Improvements

- **Revert and Rollback Changes**: New ability to revert agent changes and review what has been changed - essentially giving you an undo function and more control over the agent output and higher granularity over agent behavior.

## Platform Improvements and Bug Fixes

### Shell and Bash Tool Improvements

- Shell tool command output is now displayed in terminal in most cases
- We’ve also fixed Shell Tool on WSL and resolved Powershell execution issues and stuck commands
- Fixed compatibility issues with the Execute Shell Command tool in some terminals
- Fixed an issue with agents entering an infinite cycle when executing bash tool commands

### Other Enhancements and Fixes

- **UI Refinements** - Various UI improvements for a smoother experience
- **Automatic Reconnection** - We now reconnect automatically if websocket connection is lost
- **BYOK Support** - Added support for Bring Your Own Key (BYOK) Anthropic integration with specialized endpoints
- **Android Studio Compatibility** - To play nice with Android Studio, we’ve fixed notification about the absence of JCEF on the latest Android Studio version

## Documentation Updates

We’ve expanded our documentation to cover all the new features and improvements:

- Updated [AI Agents](https://docs.zencoder.ai/features/ai-agents) page with comprehensive information about the Zen Agents platform, including creation, sharing, and management
- Enhanced [Integrations and MCP](https://docs.zencoder.ai/features/integrations-and-mcp) documentation with details about the new MCP Library and Agent Tools interface
- Updated [FAQ](https://docs.zencoder.ai/faq/general) with new information about fine-tuning options
- Refreshed [Subscription](https://docs.zencoder.ai/get-started/subscription) page with some links and additional details

## Version History

- VS Code
- JetBrains

<!--THE END-->

- 2.6.0 (May 29, 2025)
- 2.4.0 (May 21, 2025)
- 2.2.0 (May 14, 2025)
- 2.0.0 (May 8, 2025)

<!--THE END-->

- 2.2.2 (May 26, 2025)
- 2.2.1 (May 26, 2025)
- 2.2.0 (May 22, 2025)
- 2.1.1 (May 20, 2025)
- 2.1.0 (May 18, 2025)
- 2.0.0 and 2.0.1 (May 9, 2025)