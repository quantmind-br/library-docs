---
title: August 2025 - Zencoder Docs
url: https://docs.zencoder.ai/changelog/august-2025
source: crawler
fetched_at: 2026-01-23T09:28:18.103152204-03:00
rendered_js: false
word_count: 1205
summary: This document outlines the August feature releases and platform improvements for Zencoder, detailing new tools like the Analytics Dashboard and Web Dev Agent alongside enhanced model selection and documentation updates.
tags:
    - zencoder
    - product-updates
    - analytics-dashboard
    - web-dev-agent
    - ai-coding
    - developer-tools
    - model-selection
category: other
---

## Analytics Dashboard, Web Dev Agent, and Enhanced Model Selection

August brought three major features to Zencoder: the [Analytics Dashboard](https://docs.zencoder.ai/features/analytics) for organizational insights, the [Web Dev Agent](https://docs.zencoder.ai/features/web-dev-agent) for modern web development workflows, and significant improvements to our [model selection capabilities](https://docs.zencoder.ai/features/models). We added remote and HTTP-based MCP support with OAuth2 authentication for JetBrains IDEs, expanding integration possibilities. We also enhanced [Zen Rules](https://docs.zencoder.ai/rules-context/zen-rules) with custom folder support and UI improvements, added GPT-5 support within 24 hours of OpenAI’s release, and completely rewrote our code completion and docstrings documentation. Additionally, we introduced our [Reddit community](https://reddit.com/r/zencoder) for better engagement and added the [Max plan](https://zencoder.ai/pricing) with priority support and SLA guarantees.

## New Features

### Analytics Dashboard

We’ve introduced a comprehensive Analytics Dashboard that provides organizational insights into how teams use Zencoder. Available for Core plans and above, the dashboard helps engineering managers understand and optimize their team’s development workflow.

- Get **team insights** by tracking daily active users, usage patterns, and adoption trends across your organization
- Monitor **IDE and language analytics** to see which IDEs (VS Code, JetBrains) and programming languages your team uses most
- Track **member activity** with detailed views of each team member’s usage including last active times
- **Search and filter** team members quickly by email domain for better organization

[**Explore Analytics Dashboard**  
\
Learn how to access and use the Analytics Dashboard to gain insights into your team’s Zencoder usage](https://docs.zencoder.ai/features/analytics)

### Web Dev Agent

The Web Dev Agent is our specialized agent for modern web development workflows, built after analyzing common usage patterns. It excels at creating production-ready UIs from specifications and designs, with seamless Figma integration through MCP.

- Go from **design to code** by importing designs directly from Figma using the Figma MCP and converting them to production-ready code
- Validate your UIs with **browser testing integration** that uses browser automation and console log analysis to ensure everything works
- Build with your preferred **framework** including React, Vue, Angular, and vanilla JavaScript
- Generate **E2E tests** automatically to cover your web interface functionality

[**Learn About Web Dev Agent**  
\
Discover how the Web Dev Agent streamlines your web development workflow from design to production](https://docs.zencoder.ai/features/web-dev-agent)

### Enhanced Model Selection and Availability

We’ve significantly improved our model selection capabilities with a new selector interface available to users on new pricing plans. The enhancement includes support for flagship models from multiple providers with transparent cost multipliers.

- Get **GPT-5 support** that we added within 24 hours of OpenAI’s release, available on Starter plans and above
- Use **Gemini 2.5 Pro** at a 0.75× multiplier for the most cost-efficient model option
- Access **Opus 4.1 models**, our most capable models available exclusively on Advanced and Max plans
- Bring your own API keys with **BYOK support** for OpenAI and Anthropic
- See **transparent multipliers** clearly displayed for each model right in the selector

[**Explore Model Options**  
\
Learn about available models, cost multipliers, and plan requirements](https://docs.zencoder.ai/features/models)

### Zen Rules Enhancements

Zen Rules have received major improvements making them more powerful and accessible. You can now leverage rules from other AI tools and create new rules directly from the chat interface.

- Configure **custom rule folders** to read rules from other AI tools like Cursor, Windsurf, Cline, and Continue
- See **currently applied rules** with a badge in the toolbar that shows the count of active rules
- **Create rules from chat** directly without leaving your conversation flow
- Use your **existing rules** from other AI coding assistants without any migration needed
- **Comma-separated globs** are now supported in VS Code for more flexible rule patterns

[**Master Zen Rules**  
\
Learn how to create and manage project-specific AI instructions](https://docs.zencoder.ai/rules-context/zen-rules)

### Chat Interface Improvements

- We’ve added a **right-click context menu** in the chat area so you can easily cut, copy, and paste content
- The **stop icon** has been redesigned for better visibility and user experience
- Fixed an issue where the **continue button** would appear prematurely after using the stop function
- **Informational banners** are now shown less frequently to reduce interruptions

### File Management Enhancements

- You can now **right-click files in the VS Code explorer** to add them directly to your chat context
- **File and image attachments** can now be added from anywhere on your file system, not just the project folder

## Improvements and Bug Fixes

### Agent Experience Enhancements

- We’ve renamed Q&A Agent to [**Ask Agent**](https://docs.zencoder.ai/features/qa-agent) and improved its AI capabilities for better question understanding and responses
- The [**E2E Testing Agent**](https://docs.zencoder.ai/features/e2e-testing) now supports Cypress, Playwright, and Selenium frameworks with improved test generation
- Access the **model selector** quickly using `Cmd+.` (Mac) or `Ctrl+.` (Windows/Linux) for faster model switching
- Attach **context** more easily with an improved interface for adding code, files, and other relevant information to your conversations
- Improved **quick commands for agents** for faster access to agent-specific actions
- Fixed **custom API key settings** to properly support BYOK configurations

### MCP and Integration Improvements

- JetBrains IDEs now support **remote and HTTP-based MCPs** for expanded integration capabilities
- Connect to MCPs with **OAuth2 authentication** support in JetBrains
- Get full support for [**multi-repository**](https://docs.zencoder.ai/features/multi-repo) features across BitBucket, GitLab, and GitHub with improved indexing
- Multi-repository features are now also available on the new [**Max plan**](https://zencoder.ai/pricing)

### User Interface Improvements

- We’ve improved **chat accessibility** by making new chat and chat history more easily accessible for better navigation
- The **model selector** now features an enhanced dropdown interface with clear multiplier display and plan requirements
- See your active **Zen Rules** with an improved selector UI that shows currently applied rules with a badge count
- Find what you need faster with **reorganized navigation** structured for better scalability and discoverability

### Platform Updates

- We’ve introduced the **Max plan**, a new premium tier with priority support and SLA guarantees - check [pricing](https://zencoder.ai/pricing) for details
- Join our growing community on [**Reddit**](https://reddit.com/r/zencoder) for discussions and support
- Find all our [**community resources**](https://docs.zencoder.ai/get-started/community-support) on the enhanced support page with all available channels
- Resolve BYOK issues with our new comprehensive guide for [**OpenAI BYOK troubleshooting**](https://docs.zencoder.ai/user-guides/troubleshooting/openai-byok-issues) including GPT-5 access

## Documentation Updates

This month we made significant improvements to our documentation, with complete rewrites of core features and addition of new comprehensive guides.

### Major Documentation Rewrites

- We completely rewrote the [**Code Completion**](https://docs.zencoder.ai/features/code-completion) documentation with detailed usage instructions, configuration options, and new images for VS Code and JetBrains settings
- The [**Docstrings Generation**](https://docs.zencoder.ai/features/documentation) page now includes a troubleshooting section and visual guides for code lens features
- We significantly improved [**Repo Grokking**](https://docs.zencoder.ai/technologies/repo-grokking) with better explanations of AI context orchestration and production repository understanding

### New Documentation Pages

- Learn how to use the [**Analytics Dashboard**](https://docs.zencoder.ai/features/analytics) with our comprehensive guide for team insights
- Explore the [**Web Dev Agent**](https://docs.zencoder.ai/features/web-dev-agent) documentation covering capabilities, Figma integration, and browser testing features
- Understand model selection with our complete [**Models**](https://docs.zencoder.ai/features/models) guide including cost multipliers and BYOK configuration
- Resolve GPT-5 access issues with our step-by-step [**OpenAI BYOK Troubleshooting**](https://docs.zencoder.ai/user-guides/troubleshooting/openai-byok-issues) guide

### Visual and UI Updates

- We’ve added **10+ new screenshots and diagrams** including model selector, analytics dashboard, and code completion options
- Documentation structure has been **reorganized** for better discoverability and navigation
- **Practical examples** and use cases have been added across multiple documentation pages

## Version History

- VS Code
- JetBrains

<!--THE END-->

- 2.28.0 (August 26, 2025)
- 2.26.0 (August 20, 2025)
- 2.24.0 (August 13, 2025)
- 2.22.0 (August 7, 2025)
- 2.20.0 (August 1, 2025)

<!--THE END-->

- 2.13.0 (August 29, 2025)
- 2.12.1 (August 25, 2025)
- 2.12.0 (August 25, 2025)
- 2.11.1 (August 19, 2025)
- 2.11.0 (August 18, 2025)
- 2.10.3 (August 13, 2025)
- 2.10.2 (August 12, 2025)
- 2.10.1 (August 11, 2025)
- 2.10.0 (August 11, 2025)
- 2.9.0 (August 4, 2025)