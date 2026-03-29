---
title: Universal AI Platform - Zencoder Docs
url: https://docs.zencoder.ai/features/universal-cli-platform
source: crawler
fetched_at: 2026-01-23T09:28:04.864607181-03:00
rendered_js: false
word_count: 847
summary: This document introduces Zencoder, a platform that bridges the gap between AI CLI tools and IDEs, enabling developers to use existing AI subscriptions within a unified enterprise environment.
tags:
    - ai-coding-tools
    - ide-integration
    - cli-platform
    - enterprise-software
    - software-development
    - developer-productivity
category: guide
---

**Breaking the barriers between CLIs, IDEs, and enterprise development** Zencoder brings together the world’s most popular AI coding tools directly inside your favorite IDEs. With nearly a billion global subscribers to leading AI platforms, developers everywhere can now build and modify applications at scale using a unified, powerful interface.

## Why Universal CLI Platform?

Traditional AI coding tools force developers to make difficult choices:

- **CLI tools** offer powerful capabilities but lack IDE integration
- **IDE extensions** provide convenience but often lock you into a single provider
- **Enterprise solutions** are powerful but expensive and complex to deploy

Zencoder eliminates these trade-offs by creating a universal platform that:

- Works with your existing AI subscriptions (ChatGPT, Claude, Gemini)
- Provides seamless IDE integration in VS Code and JetBrains
- Adds enterprise capabilities without complexity
- Lets you switch between AI providers instantly

Currently, Zencoder supports:

- **Zen CLI** - Zencoder’s native runtime
- **Claude Code** from Anthropic - Terminal-based agentic coding tool powered by Sonnet 4, Sonnet 4.5 Parallel Thinking, and Opus models
- **OpenAI Codex** - Command-line interface leveraging GPT-5.1-Codex’s advanced code generation capabilities

Each runtime provides deep integration with Zencoder’s enterprise features while maintaining the unique strengths of their respective AI models. Support for additional CLI tools and runtimes including Gemini CLI is coming soon.

## Setup Instructions

The setup process is straightforward: ensure you have Zencoder installed, install your preferred CLI tool, configure the runtime in Zencoder settings, and you’re ready to start building. Follow the detailed instructions in the tabs below for your chosen CLI tool.

### Connect Your CLI Tool

- Claude Code
- OpenAI Codex
- Others

Claude Code is Anthropic’s terminal-based agentic coding assistant that brings powerful AI capabilities directly to your command line. It uses Claude’s latest Sonnet 4 and Opus 4.1 models to understand your entire codebase, edit files, fix bugs, run tests, and manage Git operations through natural language commands.Unlike traditional chat interfaces, Claude Code takes direct action on your code, following the Unix philosophy of composable, scriptable tools. It integrates seamlessly with CI/CD pipelines.Now you can use your existing Claude Code subscription within Zencoder to get the best of both worlds - terminal power with IDE convenience and enterprise features.

**Prerequisites:**

- Node.js 18 or newer
- Claude subscription with Code access

**Using Claude Code with Zencoder**Once setup is complete, you can use Claude Code just like any other Zencoder runtime. You can select the [coding agent](https://docs.zencoder.ai/features/coding-agent), or use [custom agents](https://docs.zencoder.ai/features/custom-agents) from the [model selector](https://docs.zencoder.ai/features/models).

Claude Code integrates seamlessly with all of Zencoder’s features including access to your tools, multi-repository context, and enterprise capabilities. Continue using Zencoder as you normally would - the only difference is that Claude Code is now powering your AI interactions.

OpenAI Codex is OpenAI’s command-line interface that brings GPT-5.1 and other GPT models’ advanced code generation capabilities directly to your terminal. It leverages OpenAI’s latest Codex models, including GPT-5.1-Codex optimized for agentic coding, to understand context, generate code, and assist with complex programming tasks across dozens of languages.Unlike traditional code completion tools, OpenAI Codex understands natural language instructions and translates them into working code. It excels at generating boilerplate, explaining complex code, suggesting optimizations, and even translating between programming languages.Now you can use your existing ChatGPT Plus or Team subscription within Zencoder to combine OpenAI’s powerful language models with enterprise-grade IDE integration and collaboration features.

**Prerequisites:**

- Node.js 18 or newer
- ChatGPT Plus, Team, or Enterprise subscription

**Using OpenAI Codex with Zencoder**Once setup is complete, you can use OpenAI Codex just like any other Zencoder runtime. You can select the [coding agent](https://docs.zencoder.ai/features/coding-agent), or use [custom agents](https://docs.zencoder.ai/features/custom-agents) from the [model selector](https://docs.zencoder.ai/features/models).OpenAI Codex integrates seamlessly with all of Zencoder’s features including access to your tools, multi-repository context, and enterprise capabilities. Continue using Zencoder as you normally would - the only difference is that OpenAI Codex is now powering your AI interactions.

Gemini CLI and additional runtimes are coming soon.

## Key Benefits

### For Individual Developers

**Use your own subscription** and keep using your existing ChatGPT, Claude, or Gemini subscription with no additional costs for the runtime - just pay for what you already use. Get the **best of both worlds** with the power of CLI tools combined with the convenience of IDE integration, eliminating the need to switch between terminal and editor. Experience **model flexibility** by switching between different AI models instantly - use Claude for complex reasoning, GPT for creative tasks, or Gemini for search-grounded responses. Enjoy a **unified experience** with one interface for all your AI coding needs, without having to learn different tools or remember different commands.

### For Enterprise Teams

Gain **multi-repository intelligence** to understand entire codebases and microservices architectures, giving your AI agent context across all your repositories. Create and share **custom Zen agents** specialized for your team’s specific needs, ensuring consistency across your organization. Apply **enterprise guardrails** through Zen Rules to enforce coding standards, security policies, and compliance requirements automatically. Track AI adoption, measure productivity gains, and demonstrate ROI with comprehensive **analytics and insights** dashboards.

## Coming Soon

## FAQ

## Troubleshooting

[**Windows Installation Issues**  
\
If you encounter PowerShell execution policy errors while installing Claude Code or OpenAI Codex on Windows, check our troubleshooting guide for a quick fix.](https://docs.zencoder.ai/user-guides/troubleshooting/windows-cli-installation)

* * *