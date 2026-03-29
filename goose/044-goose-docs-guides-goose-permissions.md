---
title: goose Permission Modes | goose
url: https://block.github.io/goose/docs/guides/goose-permissions
source: github_pages
fetched_at: 2026-01-22T22:13:52.074327788-03:00
rendered_js: true
word_count: 261
summary: This document outlines the four permission modes in goose that manage its level of autonomy for file modifications and tool usage. It provides guidance on choosing and configuring the right mode for different development workflows and security needs.
tags:
    - goose
    - permission-modes
    - autonomy-levels
    - security-configuration
    - tool-permissions
    - ai-workflow
category: guide
---

goose’s permissions determine how much autonomy it has when modifying files, using extensions, and performing automated actions. By selecting a permission mode, you have full control over how goose interacts with your development environment.

Permission Modes Video Walkthrough

## Permission Modes[​](#permission-modes "Direct link to Permission Modes")

ModeDescriptionBest For**Completely Autonomous**goose can modify files, use extensions, and delete files **without requiring approval**Users who want **full automation** and seamless integration into their workflow**Manual Approval**goose **asks for confirmation** before using any tools or extensions (supports granular [tool permissions](https://block.github.io/goose/docs/guides/managing-tools/tool-permissions))Users who want to **review and approve** every change and tool usage**Smart Approval**goose uses a risk-based approach to **automatically approve low-risk actions** and **flag others** for approval (supports granular [tool permissions](https://block.github.io/goose/docs/guides/managing-tools/tool-permissions))Users who want a **balanced mix of autonomy and oversight** based on the action’s impact**Chat Only**goose **only engages in chat**, with no extension use or file modificationsUsers who prefer a **conversational AI experience** for analysis, writing, and reasoning tasks without automation

warning

`Autonomous Mode` is applied by default.

## Configuring goose mode[​](#configuring-goose-mode "Direct link to Configuring goose mode")

Here's how to configure:

- goose Desktop
- goose CLI

You can change modes before or during a session and it will take effect immediately.

- In Session
- From Settings

Click the mode button from the bottom menu.

info

In manual and smart approval modes, you will see "Allow" and "Deny" buttons in your session windows during tool calls. goose will only ask for permission for tools that it deems are 'write' tools, e.g. any 'text editor write', 'text editor edit', 'bash - rm, cp, mv' commands.

Read/write approval makes best effort attempt at classifying read or write tools. This is interpreted by your LLM provider.