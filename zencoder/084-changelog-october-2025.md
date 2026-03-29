---
title: October 2025 - Zencoder Docs
url: https://docs.zencoder.ai/changelog/october-2025
source: crawler
fetched_at: 2026-01-23T09:28:21.058920141-03:00
rendered_js: false
word_count: 609
summary: This document details the October 2025 product updates for Zencoder, highlighting new features such as Haiku 4.5 model support, clipboard image pasting, and various stability improvements across IDE platforms.
tags:
    - product-updates
    - release-notes
    - ai-integration
    - ide-extension
    - feature-enhancements
    - bug-fixes
category: reference
---

## October 2025 Product Updates

This month brings enhanced AI capabilities with Haiku 4.5 model support featuring extended thinking for better reasoning. We’ve streamlined file sharing with clipboard image pasting, improved chat interface responsiveness, and implemented over 20 critical stability improvements across both IDE platforms.

## Clipboard Image and Text Pasting

You can now paste content directly from your clipboard into Zencoder chat, significantly streamlining your workflow when sharing screenshots, error messages, or code snippets: **New capabilities:**

- **Image pasting** supports screenshots, diagrams, and visual content copied to your clipboard
- **Long text handling** allows pasting of extensive code blocks, logs, or documentation without file creation
- **Cross-platform support** works seamlessly in VS Code, JetBrains IDEs, and webview interfaces

This enhancement makes it faster to share context with AI agents, especially when troubleshooting issues or discussing visual elements.

## Additional Updates

### Chat Interface Improvements

- **Code blocks no longer collapse** during streaming, providing better real-time visibility as AI generates code
- **Clickable mentions** enable quick navigation when file paths or context items are referenced in chat
- **Reduced notification interruptions** by fixing recurring popups for Auto+ model and chat history notifications
- **Improved custom agents navigation** with fixes for sluggish menu positioning and response times

### File Management Enhancements

- **Code hunk language detection** now passes language information from the IDE for accurate syntax highlighting
- **Empty diff tracking fix** prevents unnecessary tracking of unchanged files
- **Better file handling** across various diff and change tracking scenarios

### Agent Experience Enhancements

- **Removed deprecated docstrings feature** that was no longer actively maintained, streamlining the codebase
- **Enhanced model configuration** with image support detection for better capability tracking
- **Generate-name command** added for AI-assisted naming of variables, functions, and files
- **Improved error handling** for terminated processes and streaming interruptions

### Integration Updates

- **MCP tool reliability** with fixes for timeout issues and improved permission tool handling
- **CLI streaming enhancements** including moved input handling and better session management
- **Background processes support** enables long-running operations without blocking the CLI
- **Better error messaging** throughout the MCP transport layer and permission validation

### Performance Improvements

- **Enhanced logging** throughout CLI operations with forced logging for user-facing errors and better operation ID tracking
- **HTTP server reliability** with fallback to 127.0.0.1 hostname and improved error logging
- **Optimized chat performance** by increasing the long chat threshold for extended conversations

### Bug Fixes

**API and Error Handling:**

- Fixed API credit and verification errors that prevented some operations
- Resolved “Our AI provider is experiencing high demand” error messages
- Fixed 403, 401, and 429 error handling across various API scenarios

**Chat and Messaging:**

- Resolved “No new user messages found to process” errors
- Fixed chat renaming issues that prevented proper conversation management
- Corrected JSON parsing errors in message handling

**Model and Session:**

- Fixed Auto+ model detection and selection issues
- Improved session ID handling for better conversation continuity
- Resolved model selection problems specific to Auto+ configuration

**Platform-Specific:**

- Enabled Windows ARM64 code signing for ARM architecture support
- Implemented working Apple code signing for macOS distribution
- Fixed JetBrains-specific CI issues and hardBreak deserialization problems
- Resolved feature flags loading without Amplitude on JetBrains platform

## Version History

- VS Code
- JetBrains

<!--THE END-->

- **2.74.0** (October 31, 2025)
- **2.72.0** (October 29, 2025)
- **2.70.0** (October 27, 2025)
- **2.68.0** (October 23, 2025)
- **2.66.0** (October 21, 2025)
- **2.64.0** (October 20, 2025)
- **2.62.0** (October 16, 2025)
- **2.60.0** (October 15, 2025)
- **2.58.0** (October 14, 2025)
- **2.56.0** (October 13, 2025)
- **2.54.0** (October 9, 2025)
- **2.52.0** (October 9, 2025)
- **2.50.0** (October 7, 2025)

<!--THE END-->

- **2.27.0** (October 31, 2025)
- **2.26.0** (October 28, 2025)
- **2.25.0** (October 23, 2025)
- **2.24.0** (October 21, 2025)
- **2.23.0** (October 16, 2025)
- **2.22.0** (October 15, 2025)
- **2.21.0** (October 14, 2025)
- **2.20.0** (October 14, 2025)
- **2.19.0** (October 11, 2025)
- **2.18.0** (October 10, 2025)

* * *

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](https://docs.zencoder.ai/get-started/community-support) page.*