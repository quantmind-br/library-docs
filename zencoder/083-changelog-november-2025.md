---
title: November 2025 - Zencoder Docs
url: https://docs.zencoder.ai/changelog/november-2025
source: crawler
fetched_at: 2026-01-23T09:28:17.041819085-03:00
rendered_js: false
word_count: 544
summary: This document outlines the November 2025 product updates for Zencoder, detailing new features such as custom model support, developer productivity metrics, and dynamic model switching within IDE plugins.
tags:
    - product-updates
    - custom-models
    - analytics-api
    - ide-plugins
    - performance-optimization
    - model-management
    - zencoder
category: other
---

## November 2025 Product Updates

This month marks a significant infrastructure milestone with the complete ZenCLI rollout, enabling custom model support and bringing your privately deployed models into Zencoder. We’ve also introduced Lines of Code metrics for better usage tracking, dynamic model switching mid-conversation, and major improvements to both VS Code and JetBrains plugins.

## Custom Models in Zencoder Plugins

Zencoder now supports custom model configurations across plugins and CLI, giving you complete control over your AI infrastructure: **Key capabilities:**

- **Private model deployments** let you connect Zencoder to your organization’s internally hosted LLMs
- **Unsupported providers** can now be integrated, expanding beyond our native model catalog
- **Custom model configurations** preserve all Zencoder features including context awareness, tool usage, and multi-step reasoning
- **Enterprise flexibility** enables compliance with strict data governance and security policies

This feature is available through [ZenCLI and plugin configurations](https://docs.zencoder.ai/features/custom-models-configuration), making it accessible whether you’re working in the IDE or command line. [Learn more about Custom Models →](https://docs.zencoder.ai/features/custom-models-configuration)

## Lines of Code Metrics

We’ve introduced two new metrics to help you measure Zencoder’s impact on your development workflow: **New metrics:**

- **Lines of code generated** shows the total output from all AI agents across your organization
- **Lines of code accepted** tracks what developers actually keep and commit, giving you a true measure of AI contribution
- Both metrics are available in the **web admin panel** under usage analytics for visual tracking
- The [**Analytics API**](https://docs.zencoder.ai/features/analytics-api) now exposes LoC data for custom reporting and integration with your existing tools

These metrics help quantify developer productivity gains and justify AI tooling investments with concrete data. [Explore Analytics API →](https://docs.zencoder.ai/features/analytics-api)

## Performance Enhancements

This month brings substantial performance improvements throughout the platform: **What you’ll notice:**

- **Faster agent responses** with optimized request handling reducing latency across all operations
- **Better resource management** improving memory usage and system performance during extended sessions
- **Enhanced reliability** through improved error handling and session management
- **Smoother long-running sessions** with better stability when working on complex, multi-step tasks

These improvements create a noticeably faster and more stable experience, especially during intensive coding sessions.

## Dynamic Model Switching

You can now switch models dynamically during an active chat session: **How it works:**

- Use the **model selector** at any point in your conversation
- **Context preservation** ensures the new model has full visibility into previous messages
- **Compare approaches** by trying different models on the same problem without context switching
- **Optimize costs** by starting with a faster model and upgrading only when needed

This flexibility lets you match model capabilities to specific subtasks within a larger workflow.

## Model Catalog Updates

We’ve expanded and refined our model offerings this month: **New additions:**

- **GPT-5.1-Codex** - Updated variant with improved code generation and reasoning
- **Gemini Pro 3.0** - Google’s latest model with enhanced multi-turn conversation capabilities

**Removed models:**

- **Sonnet 4 PT** - Replaced by newer Sonnet variants
- **GPT-5** - Superseded by GPT-5.1-Codex with better performance

[View all available models →](https://docs.zencoder.ai/features/models)

## Version History

- VS Code
- JetBrains

<!--THE END-->

- **3.6** (November 26, 2025)
- **3.4** (November 21, 2025)
- **3.2** (November 17, 2025)
- **3.0** (November 10, 2025)
- **2.80.0** (November 5, 2025)
- **2.78.0** (November 5, 2025)
- **2.76.0** (November 4, 2025)

<!--THE END-->

- **3.2.1** (November 27, 2025)
- **3.2.0** (November 27, 2025)
- **3.1.0** (November 24, 2025)
- **3.0.0** (November 11, 2025)
- **2.28.0** (November 6, 2025)

* * *

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](https://docs.zencoder.ai/get-started/community-support) page.*