---
title: June 2025 - Zencoder Docs
url: https://docs.zencoder.ai/changelog/june-2025
source: crawler
fetched_at: 2026-01-23T09:28:22.582444657-03:00
rendered_js: false
word_count: 948
summary: This document details the June 2025 platform updates for Zencoder and Zentester, including the launch of an E2E testing agent, a new LLM call-based pricing model, and enhanced IDE features.
tags:
    - release-notes
    - zentester-platform
    - e2e-testing
    - llm-usage
    - ide-integration
    - automated-testing
category: other
---

## Zentester Platform and Major Platform Enhancements

June 2025 introduces significant new capabilities with the launch of our Zentester platform, a new pricing model, and powerful new features that enhance your development workflow. This release focuses on making Zencoder more intelligent, transparent, and capable of handling complex testing scenarios. Here’s what we’ve been working on:

## New Features

### Zentester Platform with E2E Testing Agent

We’re excited to introduce the [Zentester platform](https://docs.zencoder.ai/features/e2e-testing) with our specialized E2E Testing Agent. This powerful new capability enables you to:

- **Automated E2E test creation** is here and now you can use `/e2e-test` in chat to create comprehensive end-to-end tests in plain English
- **Playwright integration** leverages Playwright for robust browser orchestration and automation
- **Intelligent test recording** means that the agent can explore webpages, record user interactions, and automatically fix failing tests
- **Cross-browser testing** lets you simulate user actions like scrolling, clicking, form filling, and snapshot verification across different browsers

The E2E Testing Agent seamlessly integrates with your development workflow, automatically setting up Playwright if needed and generating tests that can be written for various testing frameworks.

### New Pricing Model: LLM Calls Instead of Token Usage

We’ve completely redesigned our pricing structure to provide better transparency and predictability. Instead of pricing per token usage, we now price per LLM calls, offering:

- **Enhanced visibility** by giving you detailed information about every prompt message and LLM interaction
- **Predictable costs** and clear understanding of usage patterns with call-based pricing
- **Better usage tracking** with Premium LLM call usage now displayed for all new pricing plans in your Zencoder account dashboard

This represents a major shift in how we approach pricing transparency. Check out our updated [Pricing & Plans FAQ](https://docs.zencoder.ai/faq/plans) for complete details about the new pricing structure and plan options.

### /repo-info Agent

Introducing the intelligent `/repo-info` agent that significantly enhances how Zencoder understands your project:

- **Comprehensive project analysis** as the agent now collects detailed information about your repository architecture, dependencies, and build systems
- **Context generation** through the creation of a comprehensive project file (`repo.md`) that serves as context for all subsequent agent requests
- **Performance optimization** leading to a reduced number of LLM calls and speeding up agent responses by using pre-generated context

This agent acts as a foundation for our [Coding agent](https://docs.zencoder.ai/features/coding-agent), providing it with deep project understanding from the start.

### Image Prompts in VS Code

One of the most anticipated features is now available in VS Code. Users can now leverage visual context in their development workflow:

- **Repository image support** lets you use images stored in your project repository as visual prompts
- **Design-to-Code workflow** is as simple as uploading Figma screenshots or design mockups and prompting with:
  
  ```
  Look at the image.png file and build me a component looking as close as possible to it
  ```
- **Visual context understanding** now enables agents to interpret visual designs and translate them into functional code

We’re actively working on bringing this capability to JetBrains IDEs and will continue improving image prompt functionality across all platforms.

## Documentation Updates

We’ve significantly expanded our documentation to better support these new features:

- **Updated pricing FAQ** brings comprehensive updates to our [Pricing & Plans FAQ](https://docs.zencoder.ai/faq/plans) explaining the new LLM call-based pricing model
- **Known issues documentation** now comes with a new [Known Issues index page](https://docs.zencoder.ai/user-guides/known-issues/index) for better problem resolution
- **JetBrains screen fix** is now documented with the solution for the [screen issues in JetBrains IDEs](https://docs.zencoder.ai/issues/jetbrains-screen-issues)
- **E2E testing documentation** is now available with a comprehensive guide for our [E2E Testing Agent](https://docs.zencoder.ai/features/e2e-testing)

## Improvements

### Enhanced Agent Capabilities

- **Code generation enhancement** means that our code generation in the code editor now uses the full Coding Agent for more intelligent and context-aware suggestions
- **Bulk and single change reversion** lets our users now revert the latest changes done by agents in bulk or individually, providing better control over agent modifications
- **Step limit management** means that we’ve added warning messages when agents reach maximum steps, with an option to continue the request

### MCP (Model Context Protocol) enhancements

- **OAuth support** means that MCP servers now support OAuth authentication for secure third-party integrations
- **SSE/HTTP streaming** allows remote MCP servers to support Server-Sent Events (SSE) and HTTP streaming without requiring OAuth
- **Improved error messages** that we’ve added help provide better error handling and user feedback when installing MCP tools

### User Experience improvements

- **Usage visibility** now shows the Premium LLM call usage clearly displayed for users on new pricing plans right after the agent is done with its work
- **Interface refinements** bring general user experience improvements and interface polish across all platforms
- **Stability enhancements** also introduce comprehensive improvements to platform stability and reliability
- **One-click installation** lets you install official and third-party custom agents with a single click within the IDE

## Bug Fixes

### Shell Tool Improvements

- **Stability fixes** have resolved freezing issues that occurred in certain scenarios
- **Pagination handling** is now improved and the Shell tool properly avoids pagination in output for cleaner results
- **UTF-8 encoding** improvements have fixed issues with UTF-8 with BOM encoding that weren’t working properly in some cases

### Additional IDE fixes

- **VS Code fixes**:
  
  - Fixed erroneous diff showing for empty files
  - Resolved cases where code completion wasn’t displayed
  - Fixed rare cases where error screen was shown instead of chat
- **JetBrains fixes**:
  
  - Performance improvements and fixes for IDE freezing
  - Enhanced diff review and single change revert functionality
  - Improved unsaved changes dialog for custom agents

### General platform UX fixes

- **Apply button Fix** - Disabled Apply button for ghost messages to prevent confusion
- **Error handling** - Improved error messages and user feedback across the platform

## Version History

- VS Code
- JetBrains

<!--THE END-->

- 2.14.1 (June 30, 2025)
- 2.14.0 (June 27, 2025)
- 2.12.2 (June 19, 2025)
- 2.10.0 (June 11, 2025)
- 2.8.0 (June 5, 2025)

<!--THE END-->

- 2.6.1 (June 27, 2025)
- 2.6.0 (June 23, 2025)
- 2.5.0 (June 16, 2025)
- 2.4.1 (June 11, 2025)
- 2.4.0 (June 9, 2025)
- 2.3.3 (June 5, 2025)
- 2.3.2 (June 4, 2025)
- 2.3.1 (June 3, 2025)
- 2.3.0 (June 2, 2025)