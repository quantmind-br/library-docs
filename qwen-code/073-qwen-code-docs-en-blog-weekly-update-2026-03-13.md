---
title: 'Qwen Code Weekly: Automated Workflows, Better Extension & MCP Management, VS Code Sidebar'
url: https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-03-13
source: github_pages
fetched_at: 2026-04-09T09:05:41.819417967-03:00
rendered_js: true
word_count: 947
summary: This release announcement details several major updates to Qwen Code v0.12.0, introducing features like an automated Hooks system, proactive AI questioning capabilities, and enhanced visual interfaces for extension and MCP management.
tags:
    - release-notes
    - qwen-code
    - new-features
    - workflow-enhancements
    - system-updates
category: reference
---

This week we released **v0.12.0** major version and 2 bugfix releases, bringing Hooks automation system, MCP management enhancements, VS Code sidebar, and more exciting updates.

## ✨ New Features[](#-new-features)

### Hooks System: Let Qwen Code Automatically Execute Your Scripts[](#hooks-system-let-qwen-code-automatically-execute-your-scripts)

Now you can have Qwen Code automatically execute your scripts at specific moments. For example, automatically run tests before committing code, or auto-format after generating code—fully customize your workflow.

The Hooks system allows you to trigger custom commands at key lifecycle events in Qwen Code, such as:

- Auto-inject project context: Automatically inject key project information every time a user asks a question
- Auto-generate work summary logs when AI ends: Automatically save a summary of the conversation to a log file when the AI finishes

**Use Cases:**

- Automatically run tests before committing code to avoid pushing problematic code
- Auto-format after generating code, no need to manually run prettier
- Automatically save work summary at the end of each conversation for easy review

See PR [#1988](https://github.com/QwenLM/qwen-code/pull/1988) 

### AI Proactive Questions: When in Doubt, Ask You[](#ai-proactive-questions-when-in-doubt-ask-you)

Introduced a new `ask_user_question` tool that enables AI agents to ask interactive questions during task execution. This makes workflows more dynamic, allowing agents to collect user preferences in real-time, clarify requirements, and make decisions on implementation approaches.

**Use Cases:**

- AI asks for confirmation before dangerous operations to prevent accidental file deletion
- When requirements are unclear, AI proactively asks follow-up questions to get it right the first time
- Gradually clarify requirements like a conversation, without needing to think through all details at once

See PR [#1828](https://github.com/QwenLM/qwen-code/pull/1828) 

### Extension Management Interactive TUI: Install Extensions Like Browsing an App Store[](#extension-management-interactive-tui-install-extensions-like-browsing-an-app-store)

Installing extensions is as easy as installing apps. Open the visual interface, browse, install, configure, and uninstall with one click—no need to memorize commands.

Extension management integrates list, update, disable, enable, uninstall, and details operations into a unified multi-step interface, supporting keyboard navigation (↑↓), selection (Enter), and back/close (Esc).

**Use Cases:**

- Discover and install new extensions like browsing an app store
- One-click uninstall unused extensions to clean up your environment
- Visually configure extension parameters without digging through documentation

See PR [#2008](https://github.com/QwenLM/qwen-code/pull/2008) 

### MCP Management TUI Enhancement: Toggle On/Off Anytime, No Restart Needed[](#mcp-management-tui-enhancement-toggle-onoff-anytime-no-restart-needed)

Managing MCP servers is now more convenient. No need to restart Qwen Code—you can enable, disable, or configure MCP tools in the visual interface anytime and see which tools are available in real-time.

Enhanced MCP (Model Context Protocol) management TUI with runtime dynamic enable/disable, visual status indicators, scope selection configuration, health monitoring, and auto-reconnect functionality.

**Use Cases:**

- Toggle MCP tools on/off anytime without restarting the program
- See all MCP server status at a glance, know immediately if there’s an issue
- Quickly add new MCP servers, like connecting your own internal tools

See PR [#1831](https://github.com/QwenLM/qwen-code/pull/1831) 

### VS Code Companion Sidebar: Always in Your Workspace[](#vs-code-companion-sidebar-always-in-your-workspace)

Qwen Code can now stay in the VS Code sidebar. View conversation history while coding, more comfortable for dual-screen work, and more flexible layout.

**Use Cases:**

- View previous conversations in the sidebar anytime without switching windows
- Dual-screen work with code on one side and Qwen Code on the other—double your efficiency
- Freely adjust layout to put the conversation in the most convenient position

See PR [#2188](https://github.com/QwenLM/qwen-code/pull/2188) 

![](https://gw.alicdn.com/imgextra/i3/O1CN01y53WOJ1RvkAu7WaBE_!!6000000002174-2-tps-1694-952.png)

### GitHub Workflow Custom QC Commands: Run Directly in CI/CD[](#github-workflow-custom-qc-commands-run-directly-in-cicd)

Run Qwen Code commands directly in CI/CD. Automatically check and fix code when committing—ensuring code quality.

**Use Cases:**

- Automatically run code checks when submitting PRs, flagging issues directly
- Automatically fix simple issues like formatting and typos
- Let AI review first during code review to reduce manual review time

See PR [#2117](https://github.com/QwenLM/qwen-code/pull/2117) 

![](https://gw.alicdn.com/imgextra/i1/O1CN01cySDRP1K6GLSnHpwd_!!6000000001114-1-tps-860-584.gif)

### LS Tool Truncation Support: No More Screen Flooding from Large Directories[](#ls-tool-truncation-support-no-more-screen-flooding-from-large-directories)

Large directories are automatically collapsed when viewing—no more being overwhelmed by screens of file lists. AI responds faster, context is more focused.

**Use Cases:**

- When viewing large directories like node\_modules, no more being flooded by thousands of files
- Save tokens, let AI focus on important files
- Faster response, no need to wait for AI to process lengthy file lists

See PR [#2324](https://github.com/QwenLM/qwen-code/pull/2324) 

**Example truncated output**

```
Listed 150 item(s) in /path/to/dir:
---
[DIR] folder1
file1.txt
file2.txt
...
---
[50 items truncated] ...
```

## 📊 Improvements[](#-improvements)

- **Smoother OAuth Authentication**: Clear feedback after successful authentication, multi-language support, and one-click authorization clearing ([#2327](https://github.com/QwenLM/qwen-code/pull/2327) )
- **Clearer Context Compression Explanation**: Tells you why compression happened and what was compressed—no more confusion ([#2224](https://github.com/QwenLM/qwen-code/pull/2224) )
- **Auto-start After Installation**: No need to manually enter commands, ready to use right after installation ([#2290](https://github.com/QwenLM/qwen-code/pull/2290) )
- **More Recognizable Temp Files**: Prefix changed to `qwen-edit-`, instantly recognizable as Qwen Code generated ([#2045](https://github.com/QwenLM/qwen-code/pull/2045) )
- **Code Highlighting Supports Tab Width**: Display indentation according to your preference for more comfortable code viewing ([#2077](https://github.com/QwenLM/qwen-code/pull/2077) )

## 🔧 Important Fixes[](#-important-fixes)

PRVersionFixImpact[#2268](https://github.com/QwenLM/qwen-code/pull/2268) v0.12.2export command now exports current sessionNo more exporting wrong session when exporting history[#2320](https://github.com/QwenLM/qwen-code/pull/2320) v0.12.2Adapted to DeepSeek API formatNo more errors when using DeepSeek models[#2298](https://github.com/QwenLM/qwen-code/pull/2298) v0.12.2Clearer file operation error messagesKnow the specific reason when file operations fail[#2289](https://github.com/QwenLM/qwen-code/pull/2289) v0.12.1Fixed Windows terminal crashWindows users no longer crash when resizing window[#2221](https://github.com/QwenLM/qwen-code/pull/2221) v0.12.0YOLO mode no longer unexpectedly opens editorNo more interruptions when using YOLO mode[#2212](https://github.com/QwenLM/qwen-code/pull/2212) v0.12.1Fixed MCP OAuth authenticationMore stable MCP server authorization

### Windows Platform Specific Fixes[](#windows-platform-specific-fixes)

PRFixImpact[#2289](https://github.com/QwenLM/qwen-code/pull/2289) Fixed terminal resize crashNo more crashes when dragging window[#2291](https://github.com/QwenLM/qwen-code/pull/2291) Correct prompt when file doesn’t existKnow it’s a path issue when file can’t be found[#2078](https://github.com/QwenLM/qwen-code/pull/2078) Support Windows line endingsMarkdown files created on Windows can now be parsed correctly[#1890](https://github.com/QwenLM/qwen-code/pull/1890) Fixed silent failures caused by CRLFCertain operations no longer fail inexplicably

## 🎈 Other Improvements[](#-other-improvements)

- Added 8 new contributors: [@zy6p](https://github.com/zy6p) , [@lgzzzz](https://github.com/lgzzzz) , [@huww98](https://github.com/huww98) , [@Aayushyaash](https://github.com/Aayushyaash) , [@kkhomej33-netizen](https://github.com/kkhomej33-netizen) , [@Deng-Xian-Sheng](https://github.com/Deng-Xian-Sheng) , [@xieyonn](https://github.com/xieyonn) , [@qqqys](https://github.com/qqqys) , [@ossaidqadri](https://github.com/ossaidqadri)
- Added JSON Schema validation for VS Code settings
- Refactored settings migration to sequential framework with atomic file write support
- Migrated ACP integration to @agentclientprotocol/sdk

**How to Upgrade**: Run `npm i @qwen-code/qwen-code@latest -g` to upgrade to the latest version.

If you have questions or suggestions, feel free to provide feedback on [GitHub Issues](https://github.com/QwenLM/qwen-code/issues) !