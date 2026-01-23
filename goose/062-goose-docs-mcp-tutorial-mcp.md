---
title: Tutorial Extension | goose
url: https://block.github.io/goose/docs/mcp/tutorial-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:57.504412171-03:00
rendered_js: true
word_count: 348
summary: This document explains how to use the built-in Tutorial extension in goose to access interactive, step-by-step guidance and hands-on practice for learning goose features.
tags:
    - goose-ai
    - interactive-learning
    - tutorial-extension
    - onboarding
    - mcp-protocol
category: guide
---

The Tutorial extension is a built-in feature of goose that provides interactive, step-by-step guidance for learning various aspects of goose and its capabilities. It's designed to help users get comfortable with goose's features through hands-on practice.

The Tutorial extension serves as an interactive learning tool that:

- Provides structured, step-by-step tutorials
- Allows hands-on practice with goose features
- Offers immediate feedback and guidance

## Configuration[​](#configuration "Direct link to Configuration")

1. Ensure the Tutorial extension is enabled:

<!--THE END-->

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click `Extensions` in the sidebar
3. Toggle `Tutorial` on

## Available Tutorials[​](#available-tutorials "Direct link to Available Tutorials")

Currently, the following tutorials are available:

- **build-mcp-extension**: Learn how to build an extension using the Model Context Protocol (MCP)
- **first-game**: Create your first game with goose

More tutorials are being added regularly to cover additional features and use cases.

## Using the Tutorial Extension[​](#using-the-tutorial-extension "Direct link to Using the Tutorial Extension")

### Starting a Tutorial[​](#starting-a-tutorial "Direct link to Starting a Tutorial")

There are two main ways to interact with tutorials:

1. **Ask goose directly**: You can simply ask about a topic you're interested in, and goose will suggest relevant tutorials.

```
( O)> I'd like to learn how to build an extension for goose
```

2. **Request a specific tutorial**: You can directly request a tutorial by name.

```
( O)> Can you walk me through the first-game tutorial?
```

### During the Tutorial[​](#during-the-tutorial "Direct link to During the Tutorial")

While going through a tutorial:

1. goose will guide you step-by-step through the process
2. You'll receive clear instructions before any actions are taken
3. You can ask questions at any time for clarification
4. You can take breaks and resume later

### Best Practices[​](#best-practices "Direct link to Best Practices")

- **Take your time**: Don't rush through the tutorials. Make sure you understand each step before moving on.
- **Ask questions**: If something isn't clear, ask goose to explain it further.
- **Experiment**: Feel free to try variations of what you're learning.
- **Take notes**: Document any interesting findings or techniques you learn.

## Example Usage[​](#example-usage "Direct link to Example Usage")

### Starting a Tutorial Session[​](#starting-a-tutorial-session "Direct link to Starting a Tutorial Session")

Here's an example of how to start learning about building extensions:

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
I'd like to learn how to build an extension for goose
```

### goose Output[​](#goose-output "Direct link to goose Output")

```
I'll help you learn about building extensions! The "build-mcp-extension" tutorial would be perfect for this. Let me load it and guide you through it.

─── load_tutorial | tutorial ──────────────────────────
name: build-mcp-extension


Before we dive into building your extension, I need to understand a few things to better guide you:

1. Which SDK would you prefer to use? We have three options:
   - Python (beginner-friendly, great for prototyping)
   - TypeScript (great for web-based tools)
   - Kotlin (robust, type-safe, good for complex applications)

2. What type of extension would you like to build? For example:
   - A tool that performs specific actions
   - A resource that provides data to the LLM
   - Or do you have a specific idea in mind?

Let me know your preferences, and I'll help you get started with the appropriate setup and implementation!

For reference, here's what we'll cover:
1. Setting up your development environment
2. Creating the basic MCP server
3. Implementing your specific functionality
4. Testing and debugging

Which SDK would you like to use to get started?
```

## Next Steps[​](#next-steps "Direct link to Next Steps")

After completing tutorials, you can:

- Apply learned concepts to your own projects
- Contribute to the goose community by sharing your experiences
- Suggest new tutorial topics that would be helpful for others

### Need Further Help?[​](#need-further-help "Direct link to Need Further Help?")

If you have questions, run into issues, or just need to brainstorm ideas join the [Discord Community](https://discord.gg/goose-oss)!