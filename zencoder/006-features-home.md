---
title: Overview - Zencoder Docs
url: https://docs.zencoder.ai/features/home
source: crawler
fetched_at: 2026-01-23T09:28:09.802568329-03:00
rendered_js: false
word_count: 323
summary: This document provides an overview of Zencoder's AI-powered development tools, detailing how to use integrated IDE workflows and specialized agents for coding, debugging, and documentation.
tags:
    - zencoder
    - ai-coding-assistant
    - ide-integration
    - developer-workflow
    - custom-workflows
    - ai-agents
    - code-automation
category: guide
---

Zencoder provides a comprehensive set of AI-powered tools designed to enhance your development workflow. This guide organizes features by their function in your development process, helping you quickly find the right tool for your current task.

Set up Zencoder in your development environment to start using all features.

## Guided Workflows in the IDE

Launch common task types without leaving your editor. The IDE panel surfaces guided workflows so every request starts with the right structure instead of an ad-hoc prompt.

### Default workflow options

- **New feature** moves from idea to spec to implementation with built-in checkpoints for planning and verification.
- **Fix bug** front-loads investigation, root-cause capture, and regression testing so bug reports become tested fixes.

![IDE view showing the New feature and Fix bug workflow tiles](https://mintcdn.com/forgoodaiinc/s71iq5-UlTL8fu2h/images/workflows/ide-workflows-default.png?fit=max&auto=format&n=s71iq5-UlTL8fu2h&q=85&s=9a6ae6cdbc17e79cfae4842708abf75f)

### Add custom workflows

Teams can expose domain-specific flows (security reviews, release cut-overs, etc.) right next to the defaults:

1. Create `.zenflow/workflows/<workflow-name>.md` in your repo root (or `~/.zenflow/workflows/` for user-level workflows).
2. Define configuration metadata (Artifacts Path, owners) and write each step as `### [ ] Step: {Name}` with links to artifacts such as `{@artifacts_path}/plan.md`.
3. Commit the file—Zenflow automatically lists it under **Custom workflow** inside the IDE selector.

![IDE selector showing the default workflows plus a custom workflow dropdown](https://mintcdn.com/forgoodaiinc/s71iq5-UlTL8fu2h/images/workflows/ide-workflows-custom.png?fit=max&auto=format&n=s71iq5-UlTL8fu2h&q=85&s=cf2ed771f4f8e4a9107ce95b765c848e)

## AI Agents

Specialized AI agents that automate complex coding tasks and processes.

## Code Assistance, Quality and Understanding

Tools that help you write, improve, and understand code more efficiently.

## Documentation

Tools for creating and maintaining code documentation.

## Feature Usage Tips

- **For project setup**, start with the [Repo-Info Agent](https://docs.zencoder.ai/features/repo-info-agent) to create comprehensive project context that enhances all other agent capabilities.
- **For quick answers**, use the [Ask Agent](https://docs.zencoder.ai/features/qa-agent) to ask questions about your code and get context-aware responses.
- **For new implementations**, use the [Coding Agent](https://docs.zencoder.ai/features/coding-agent) to generate complete solutions that integrate with your existing codebase.
- **For existing code**, apply [Code Refactoring](https://docs.zencoder.ai/features/code-refactoring) and [Code Repair](https://docs.zencoder.ai/features/code-repair) to improve quality and maintainability.
- **For maintenance**, generate [Documentation](https://docs.zencoder.ai/features/documentation) and run the [Unit Testing Agent](https://docs.zencoder.ai/features/unit-testing) to ensure code longevity and reliability.