---
title: Local environments
url: https://developers.openai.com/codex/app/local-environments.md
source: llms
fetched_at: 2026-04-30T10:15:07.170938867-03:00
rendered_js: false
word_count: 188
summary: This document explains how to configure local development environments in Codex by setting up automated dependency installation scripts and defining custom task actions.
tags:
    - local-environment
    - codex-configuration
    - setup-scripts
    - task-automation
    - workflow-optimization
category: configuration
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Local environments

Configure setup steps for worktrees and common actions for a project through the [Codex app settings](codex://settings) pane. Check the generated file into Git to share with others.

Configuration lives in the `.codex` folder at the project root. If your repository contains multiple projects, open the directory that contains the shared `.codex` folder.

## Setup scripts

Worktrees run in different directories than local tasks, so dependencies or files not checked into Git may be missing. Setup scripts run automatically when Codex creates a new worktree at the start of a thread.

Use them to install dependencies, run builds, or any other required configuration.

Example for a TypeScript project:
```bash
npm install
npm run build
```

Define platform-specific scripts (macOS, Windows, Linux) to override the default when setup differs by platform.

## Actions

Define common tasks like starting a dev server or running tests. Actions appear in the Codex app top bar for quick access and run in the app's integrated terminal.

Example for a Node.js project:
```bash
npm start
```

Define platform-specific scripts (macOS, Windows, Linux) when commands differ by platform. Choose an icon for each action to identify it in the top bar.

#codex #local-environment #configuration