---
title: December 2025 - Zencoder Docs
url: https://docs.zencoder.ai/changelog/december-2025
source: crawler
fetched_at: 2026-01-23T09:28:20.355658182-03:00
rendered_js: false
word_count: 578
summary: This document outlines the product updates for December 2025, detailing new features such as Spec-Driven Development workflows, enhanced markdown support, and Model Context Protocol configurations.
tags:
    - product-updates
    - release-notes
    - spec-driven-development
    - markdown-support
    - model-context-protocol
    - platform-stability
    - ide-plugins
category: reference
---

## December 2025 Product Updates

December focused on introducing powerful workflow capabilities with Spec-Driven Development (SDD), enhanced content formatting with markdown tables and copy features, and significant platform stability improvements across both VS Code and JetBrains plugins.

## Spec-Driven Development Workflows

Zencoder now supports custom workflows for spec-driven development, making complex tasks more manageable and reliable: **Key capabilities:**

- **Guided development process** walks you through feature creation and bug fixes with a structured approach
- **Custom workflow support** allows you to create and configure workflows tailored to your team’s development process
- **Spec-first approach** ensures clear requirements before implementation begins
- **Improved reliability** through systematic planning and execution of development tasks

This feature brings enterprise-grade development practices to your daily workflow, helping teams maintain consistency and quality across projects.

## Enhanced Markdown Support

We’ve significantly improved how Zencoder handles markdown content in chat: **New capabilities:**

- **Markdown tables rendering** displays tabular data properly formatted in chat responses
- **Copy as Markdown button** makes it easy to export AI-generated content in markdown format
- **Enhanced code blocks** preserve language syntax highlighting information
- **Line break preservation** maintains formatting in user messages and code snippets

These improvements make it easier to work with formatted content and share AI-generated responses with your team.

## Model Context Protocol Enhancements

Model Context Protocol tool configuration now supports project-level customization, giving you more flexibility in how AI agents interact with external services: **What’s improved:**

- **Per-project tool configuration** allows different MCP server setups for different repositories, enabling project-specific integrations
- **Better session management** with improved MCP session lifecycle handling and automatic cleanup on client close
- **Enhanced reliability** through fixes for timeout issues, permission handling, and transport layer error messaging
- **RAG search integration** with automatic MCP configuration for repository search capabilities
- **Improved MCP config parsing** ensures proper tool detection and initialization

This granular control helps teams customize which external tools and services are available to AI agents based on specific project requirements and security policies.

## Platform Stability Improvements

December brings extensive stability improvements across the platform: **Performance enhancements:**

- **Faster agent responses** with optimized request handling and reduced latency
- **Better edge case handling** prevents errors in unusual scenarios
- **Improved memory usage** reduces resource consumption during extended sessions
- **Enhanced long-session reliability** maintains stability during complex, multi-step tasks

**User experience improvements:**

- **Improved file browser behavior** prevents duplicate dialogs when attaching files
- **Better context handling** preserves current-file context settings correctly
- **Enhanced error messaging** with clearer feedback for issues

These improvements create a noticeably smoother experience throughout your development workflow.

## Additional Updates

### Chat and Interface Enhancements

- **Fixed mention duplication** when copying and pasting content in chat
- **Improved keyboard shortcuts** with better keybinding display in the agent menu
- **Unicode filename support** sanitizes pasted image filenames to prevent errors
- **Better custom agent updates** ensure agent details refresh immediately after modifications

### Testing and Development Tools

- **Automatic Playwright installation** for E2E and Web Dev agents eliminates manual setup steps
- **Open file from changes list** allows quick navigation directly to modified files
- **Improved streaming reliability** prevents interruptions when tool errors occur
- **Better diff handling** with enhanced code change tracking and visualization

### Integration and Tool Updates

- **Improved CLI stability** with better error handling and retry logic
- **Background process support** for long-running operations without blocking
- **Enhanced RAG integration** with automatic configuration and better error handling

## Version History

- VS Code
- JetBrains

<!--THE END-->

- **3.20.0** (December 18, 2025)
- **3.18.0** (December 12, 2025)
- **3.16.0** (December 5, 2025)

<!--THE END-->

- **3.7.0** (December 18, 2025)
- **3.6.0** (December 12, 2025)
- **3.5.0** (December 5, 2025)

* * *

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](https://docs.zencoder.ai/get-started/community-support) page.*