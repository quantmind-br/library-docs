---
title: VS Code Gray Screen Issue - Zencoder Docs
url: https://docs.zencoder.ai/user-guides/known-issues/vscode-gray-screen
source: crawler
fetched_at: 2026-01-23T09:28:42.749966068-03:00
rendered_js: false
word_count: 284
summary: This document provides troubleshooting steps and workarounds for resolving a visual glitch where the Zencoder chat panel in VS Code appears as a gray, unresponsive screen.
tags:
    - zencoder
    - vs-code
    - troubleshooting
    - gray-screen
    - extension-fix
    - ide-support
category: guide
---

## Zencoder Chat Appears Gray in VS Code

### Problem Description

In rare instances, the Zencoder chat panel in VS Code may display as a gray, unresponsive area instead of the expected chat interface. This is internally known as the “Gray Screen of Death” (GSOD). This prevents normal interaction with Zencoder within the IDE. ![Gray Screen in VS Code Chat](https://mintcdn.com/forgoodaiinc/M05vBYexh9mikig2/images/gray-screen-vs-code.png?fit=max&auto=format&n=M05vBYexh9mikig2&q=85&s=98c5a8733c31d80265c9bda4455ac71a)

## Symptoms

- The Zencoder panel opens but displays only a gray screen
- The chat interface is completely non-responsive
- No content or error messages are visible
- The issue may occur intermittently

## Current Status

We’re aware of this issue and are actively working on a permanent fix. Our engineering team is investigating the root cause to ensure a stable resolution in an upcoming update.

## Workaround

While we work on the permanent fix, here’s how to restore functionality:

1. **Close VS Code completely**
   
   - Save any open work
   - Quit VS Code entirely (not just closing the window)
2. **Terminate the VS Code process**
   
   - On Windows: Use `Task Manager` to end any remaining VS Code processes
   - On macOS: Use `Activity Monitor` to quit any VS Code processes
   - On Linux: Use `pkill code` or your system’s process manager
3. **Restart VS Code**
   
   - Launch VS Code normally
   - The Zencoder chat should now display correctly

## Additional Steps

If the issue persists after restarting:

1. Try disabling and re-enabling the Zencoder extension
2. Clear VS Code’s cache:
   
   - Open Command Palette (`Cmd/Ctrl + Shift + P`)
   - Run `Developer: Reload Window`
3. Check for VS Code and Zencoder extension updates

## Getting Help

If you continue experiencing this issue:

- Collect debug information using our [debug guide](https://docs.zencoder.ai/user-guides/troubleshooting/debug-information)
- Report the frequency and any patterns you notice
- Contact our support team through [Discord](https://discord.gg/YjNYBHg8Vb), [Reddit](https://www.reddit.com/r/zencoder/), or [email](mailto:support@zencoder.ai)

We appreciate your patience as we work to resolve this issue permanently.