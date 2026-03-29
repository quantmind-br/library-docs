---
title: July 2025 - Zencoder Docs
url: https://docs.zencoder.ai/changelog/july-2025
source: crawler
fetched_at: 2026-01-23T09:28:20.1843051-03:00
rendered_js: false
word_count: 1324
summary: This document outlines major updates to the Zencoder platform, specifically introducing multi-repository search, project-specific Zen Rules, and enhanced AI agents for codebase analysis and testing.
tags:
    - product-updates
    - multi-repo-search
    - zen-rules
    - ai-agents
    - code-analysis
    - release-notes
category: other
---

## Multi-Repository Search and Zen Rules Platform Update

In July we released two major features: [Multi-Repository Search](https://docs.zencoder.ai/features/multi-repo) and [Zen Rules](https://docs.zencoder.ai/rules-context/zen-rules). These features enable better contextual understanding across complex enterprise codebases by allowing agents to search across multiple repositories and apply project-specific instructions. Multi-repo search addresses the challenge of understanding dependencies and patterns in distributed systems, while Zen Rules provides a mechanism for encoding architectural decisions and coding standards directly into the AI’s context. We also introduced enhanced agents (Repo-Info, Q&A, E2E Testing), universal image attachment support, and numerous platform improvements for better stability and performance.

## New Features

### Multi-Repository Search

We’re excited to introduce [Multi-Repository Search](https://docs.zencoder.ai/features/multi-repo), enabling AI agents to understand and work across your entire organization’s codebase:

- **Index multiple repositories** through the web admin panel at [auth.zencoder.ai](https://auth.zencoder.ai)
- **Cross-repository code understanding** allows agents to find patterns, implementations, and dependencies across all your indexed repositories
- **Automatic context detection** means agents intelligently search relevant repositories when you reference other services or projects

[**Learn More About Multi-Repository Search**  
\
Set up and configure multi-repository indexing to enable AI-powered search across your entire codebase](https://docs.zencoder.ai/features/multi-repo)

### Zen Rules - Project-Specific AI Instructions

Introducing [Zen Rules](https://docs.zencoder.ai/rules-context/zen-rules), our powerful new system for creating custom context and instructions that enhance how AI agents understand your project:

- **Project-level rules** stored in `.zencoder/rules/*.md` files that are committed to your repository for team sharing
- **Conditional application** based on file patterns using glob expressions, or always-on rules for project-wide standards
- **Three-tier hierarchy** combining Zen Rules, personal AI instructions, and repo.md for comprehensive context management
- **@mention support** allows you to manually reference specific rules in your chat for targeted guidance

[**Explore Zen Rules**  
\
Learn how to create custom rules that enforce your team’s coding standards and architectural patterns](https://docs.zencoder.ai/rules-context/zen-rules)

### Enhanced Repo-Info Agent

The [Repo-Info Agent](https://docs.zencoder.ai/features/repo-info-agent) has been significantly improved to provide deeper insights into your codebase:

- **Better project analysis** with more comprehensive understanding of build systems, dependencies, and architectural patterns
- **Optimized context generation** reduces the number of LLM calls needed for subsequent agent requests
- **Automatic migration** moves `repo.md` from the old `/docs` location to the new `.zencoder/rules/` directory
- **Foundation for all agents** as the generated context is automatically included in every agent request

[**Learn About Repo-Info Agent**  
\
Discover how the Repo-Info Agent analyzes your project structure and generates comprehensive context for all other agents](https://docs.zencoder.ai/features/repo-info-agent)

### Q&A Agent

We’ve replaced the legacy basic chat with our new [Q&A Agent](https://docs.zencoder.ai/features/qa-agent), optimized for quick questions and code explanations:

- **Lightweight interface** designed for rapid responses to coding questions
- **Codebase-aware** leveraging Repo Grokking to understand your specific project context
- **Streamlined for simplicity** with limited tool access for faster, focused interactions
- **Easy agent switching** through the new agent selector UI

[**Explore Q&A Agent**  
\
Learn about our streamlined Q&A Agent designed for quick coding questions and explanations](https://docs.zencoder.ai/features/qa-agent)

### Image Attachments for All Users

Visual context is now universally available across both VS Code and JetBrains IDEs:

- **Universal access** means that image attachment functionality is no longer limited and is available for all users across all supported platforms
- **Design-to-code workflow** has been streamlined, allowing you to attach UI mockups or screenshots and ask agents to build matching components with high accuracy
- **Repository images** stored in your project can be referenced for visual context, enabling agents to understand and implement visual designs directly from your codebase assets

### E2E Testing Agent Enhancements

The [E2E Testing Agent](https://docs.zencoder.ai/features/e2e-testing) has evolved to become framework-agnostic:

- **Multi-framework support** now enables you to generate tests for Cypress, Playwright, or Selenium based on your project’s requirements and preferences
- **Flexible test generation** approach means you simply specify your preferred framework in the prompt, and the agent adapts its output accordingly
- **Maintained intelligence** ensures that all the powerful test creation, exploration, and fixing capabilities that made our E2E agent valuable now work seamlessly across all supported frameworks

[**Learn About E2E Testing Agent**  
\
Discover how to generate end-to-end tests using Cypress, Playwright, or Selenium with our intelligent testing agent](https://docs.zencoder.ai/features/e2e-testing)

## Improvements and Bug Fixes

### Agent Experience Enhancements

- **New agent selector UI** provides quick access to different agents with a redesigned dropdown interface
- **Background shell execution** allows agents to run long-running commands without blocking the interface
- **File Diagnostic tool** is now available for custom agents, expanding their capabilities
- **Better file mention suggestions** with improved logic based on user feedback for more intuitive file referencing
- **Expandable code blocks** in chat for better readability with large code snippets
- **Agent continuation** shows an improved message when agents reach max steps with option to continue the request

### User Interface Improvements

- **Redesigned VS Code status bar** with more visible Zencoder icon and better integration
- **Updated sidebar menu** in the admin UI with improved organization and new profile dropdown for easier account management
- **Premium LLM usage display** clearly shows call consumption for users on new pricing plans
- **Better code diff copying** now only copies added lines when copying from diffs, not the entire block
- **Enhanced chat input UI** with cleaner design and better visual hierarchy

### Platform Stability and Performance

- **SSE/HTTP streaming support** for remote MCP servers without OAuth (VS Code, coming to other platforms)
- **Requirements tool functionality** helps agents better understand user needs before proceeding - now with improved UI
- **Less frequent update notifications** reduces interruption while keeping you informed of important updates
- **repo.md migration** automatically moves from deprecated `/docs` to new `/rules` directory structure

### Bash/PowerShell/WSL Improvements

- **PowerShell support** with PS1 files now properly executing shell commands on Windows
- **WSL compatibility** adds support for WSL and other interpreter types on Windows
- **Bash tool stability** fixed job cancellation issues when Kotlin plugin is not installed in JetBrains

### Bug Fixes

- **Shell tool freezing** resolved cases where shell tool would freeze in certain scenarios
- **Shell pagination** now properly avoids pagination in command output for cleaner results
- **Code generation window** fixed size adjustment issues when pasting text in JetBrains
- **Q&A Agent tools** fixed issue where Q&A Agent was using tools it shouldn’t have access to
- **File attachment labels** updated to better reflect actual capabilities and limitations
- **LLM call counter** now properly displays consumption after clicking Stop
- **Various UI glitches** resolved multiple interface inconsistencies across platforms

## Documentation Updates

We’ve significantly expanded and improved our documentation to support the new features and provide better guidance:

### New Documentation Pages

- [**Agents Overview**](https://docs.zencoder.ai/features/agents-overview) serves as the new landing page for all agents, providing a comprehensive guide to accessing and understanding each agent’s capabilities
- [**Q&A Agent documentation**](https://docs.zencoder.ai/features/qa-agent) introduces our new lightweight chat interface, explaining how it differs from the Coding Agent and when to use each
- [**Multi-Repository Search guide**](https://docs.zencoder.ai/features/multi-repo) provides detailed setup instructions, best practices, and examples for indexing and searching across multiple repositories
- [**Zen Rules documentation**](https://docs.zencoder.ai/rules-context/zen-rules) explains the three-tier hierarchy of AI instructions, with practical examples and guidelines for creating effective project-specific rules
- [**Refund Policy FAQ**](https://docs.zencoder.ai/faq/refund-policy) offers clear information about subscription management, cancellations, and our transparent refund policies

### Enhanced Existing Documentation

- [**Repo Grokking documentation**](https://docs.zencoder.ai/technologies/repo-grokking) has been updated to better reflect current capabilities and how it powers our large codebase understanding
- [**Coding Agent guide**](https://docs.zencoder.ai/features/coding-agent) now includes references to the new agent selector UI and improved capabilities
- [**E2E Testing Agent documentation**](https://docs.zencoder.ai/features/e2e-testing) has been enhanced with framework-specific test generation examples for Cypress, Playwright, and Selenium
- [**Repo-Info Agent documentation**](https://docs.zencoder.ai/features/repo-info-agent) updated to reflect the migration from `/docs` to `/rules` directory and its role in the Zen Rules hierarchy
- [**Unit Testing Agent guide**](https://docs.zencoder.ai/features/unit-testing) refreshed with new agent selector images and updated workflow descriptions
- [**Pricing Plans FAQ**](https://docs.zencoder.ai/faq/plans) clarified to better explain the new LLM call-based pricing model and plan comparisons

### New Tutorials and Visual Updates

- [**Generate Codebase Architecture Diagrams tutorial**](https://docs.zencoder.ai/user-guides/tutorials/generate-codebase-diagrams) shows how to create Mermaid diagrams to visualize repository structure and dependencies
- **Image prompts documentation** updated to explain the new universal image attachment capabilities
- **Agent selector images** refreshed across all agent documentation to show the new dropdown UI and improved user experience
- **Multi-repo search guidelines** enhanced with specific examples and best practices for effective cross-repository searches

## Version History

- VS Code
- JetBrains

<!--THE END-->

- 2.17.0 (July 23, 2025)
- 2.16.0 (July 15, 2025)

<!--THE END-->

- 2.8.0 (July 28, 2025)
- 2.7.1 (July 22, 2025)
- 2.7.0 (July 17, 2025)
- 2.6.3 (July 4, 2025)
- 2.6.2 (July 3, 2025)