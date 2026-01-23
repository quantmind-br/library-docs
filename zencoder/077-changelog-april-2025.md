---
title: April 2025 - Zencoder Docs
url: https://docs.zencoder.ai/changelog/april-2025
source: crawler
fetched_at: 2026-01-23T09:28:19.118623236-03:00
rendered_js: false
word_count: 482
summary: This document highlights the April product updates for Zencoder, detailing new features such as the Bash tool, Requirements tool, and various chat and search enhancements.
tags:
    - release-notes
    - product-updates
    - zencoder
    - coding-agent
    - ide-extension
    - developer-experience
category: other
---

April brought significant improvements to Zencoder’s functionality and user experience. We’ve focused on adding powerful new tools like the Bash/Shell tool and Requirements tool, enhancing UX, and making many under-the-hood improvements to make your development workflow more efficient. Here’s what we’ve been working on:

### Bash/Shell Tool for Coding Agent

The Bash tool is now available to the coding agent with significant improvements:

- Improved UX for safe commands that can run without confirmation
- Management options including “Don’t ask again” in both VS Code and JetBrains
- Works seamlessly with Coffee Mode for increased productivity and speed
- Enhanced MCP management of environment variables and npx, making it more stable

[**Learn More About Coding Agent**  
\
Explore how the Coding Agent can now leverage shell commands to better assist your development workflow.](https://docs.zencoder.ai/features/coding-agent)

### Requirements Tool

Our new Requirements tool helps the coding agent better understand your needs:

- Automatically asks for clarifications when needed
- Gives you greater control over your project and work
- Better understands prompts and delivers higher-quality results
- Reduces back-and-forth by getting requirements right the first time

### Enhanced Chat Experience

We’ve made several improvements to the chat interface:

- Added support and hints for using slash commands (`/`) and file mentions (`@`) in the chatbox
- New warning system when chats become too long, helping you optimize token usage across multiple chats
- Ability to attach files from outside of the project to provide better context

## Debugging and Support Improvements

We’ve made it easier to get help when you need it:

- Simplified access to Operation IDs and debug settings to help us troubleshoot issues more effectively

## Search and Review Enhancements

- Significant improvements to local (client-side) search functionality
- Enhanced `/review` command is now invoking a pre-built custom agent with the same name, providing more precise and valuable insights
- You can adjust this custom agent’s details in the Custom Agent settings

[**Learn More About Custom Agents**  
\
Discover how to customize the review agent and other specialized agents for your workflow.](https://docs.zencoder.ai/features/custom-agents)

## Documentation Updates

- New descriptions and updated GIFs for documentation on both JetBrains and VS Code marketplaces
- Added detailed [guides on how to collect debug information and Operation IDs](https://docs.zencoder.ai/user-guides/troubleshooting/debug-information) to help with troubleshooting
- Enhanced documentation to make it easier to get support when needed

## Bugs and Fixes

We’ve addressed several user-facing issues:

- Fixed an annoying bug where indexing sometimes gets stuck at “Updating index” after reopening the IDE
- Fixed a problem with cursor positioning above inserted code snippets
- Improvements to Jira authentication flow
- Fixed hanging errors between the bash/shell tool and our internal processing

*Note: We’ve also made many background improvements and fixes that aren’t listed here but contribute to a more stable and reliable experience.*

## Version History

- VS Code
- JetBrains

<!--THE END-->

- 1.28.0 (Apr 28, 2025)
- 1.26.0 (Apr 17, 2025)
- 1.24.0 (Apr 10, 2025)
- 1.22.0 (Apr 2, 2025)

<!--THE END-->

- 1.24.0 (Apr 30, 2025)
- 1.23.1 (Apr 24, 2025)
- 1.23.0 (Apr 22, 2025)
- 1.22.0 (Apr 15, 2025)
- 1.21.0 (Apr 4, 2025)