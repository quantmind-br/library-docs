---
title: Quickstart
url: https://developers.openai.com/codex/quickstart.md
source: llms
fetched_at: 2026-01-13T18:59:55.571164865-03:00
rendered_js: false
word_count: 60
summary: This document provides a quickstart guide for accessing and installing Codex across different environments, including IDE extensions, the command line interface, and a cloud-based platform.
tags:
    - codex
    - quickstart
    - installation
    - setup
    - cli
    - ide
    - cloud
category: tutorial
---

# Quickstart

Codex is included with ChatGPT Plus, Pro, Business, Edu, and Enterprise plans. Using Codex with your ChatGPT subscription gives you access to the latest Codex models and features.

You can also use Codex with API credits by signing in with an OpenAI API key.

## Setup

<Tabs
  param="setup"
  tabs={[
    { id: "ide", label: "IDE extension", subtitle: "Codex in your IDE" },
    { id: "cli", label: "CLI", subtitle: "Codex in your terminal" },
    { id: "cloud", label: "Cloud", subtitle: "Codex in your browser" },
  ]}
>
  <div slot="ide">
    Install the Codex extension for your IDE:

    - [Download for Visual Studio Code](vscode:extension/openai.chatgpt)
    - [Download for Cursor](cursor:extension/openai.chatgpt)
    - [Download for Windsurf](windsurf:extension/openai.chatgpt)
    - [Download for Visual Studio Code Insiders](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)

    Once installed, the Codex extension appears in the sidebar alongside your other extensions. It may be hidden in the collapsed section. You can move the Codex panel to the right side of the editor if you prefer.

    Sign in with your ChatGPT account or API key to get started.

    Codex starts in Agent mode by default, which lets it read files, run commands, and write changes in your project directory.

    Codex can modify your codebase, so consider creating Git checkpoints before and after each task so you can easily revert changes if needed.

    <CtaPillLink href="/codex/ide" label="Learn more about the Codex IDE extension" class="mt-8" />

  </div>

  <div slot="cli">
    The Codex CLI is supported on macOS, Windows, and Linux.

    Install with your preferred package manager:

```bash
# Install with npm
npm install -g @openai/codex
```

```bash
# Install with Homebrew
brew install codex
```

    Run `codex` in your terminal to get started. You'll be prompted to sign in with your ChatGPT account or an API key.

    Once authenticated, you can ask Codex to perform tasks in the current directory.

    Codex can modify your codebase, so consider creating Git checkpoints before and after each task so you can easily revert changes if needed.

    <CtaPillLink href="/codex/cli" label="Learn more about the Codex CLI" class="mt-8" />

  </div>

  <div slot="cloud">
    To use Codex in the cloud, go to [chatgpt.com/codex](https://chatgpt.com/codex). You can also delegate a task to Codex by tagging `@codex` in a GitHub pull request comment (requires signing in to ChatGPT).

    Before starting your first task, set up an environment for Codex. Open the environment settings at [chatgpt.com/codex](https://chatgpt.com/codex/settings/environments) and follow the steps to connect a GitHub repository.

    Once your environment is ready, launch coding tasks from the [Codex interface](https://chatgpt.com/codex). You can monitor progress in real time by viewing logs, or let tasks run in the background.

    When a task completes, review the proposed changes in the diff view. You can iterate on the results or create a pull request directly in your GitHub repository.

    Codex also provides a preview of the changes. You can accept the PR as is, or check out the branch locally to test the changes:

```bash
git fetch
git checkout <branch-name>
```

    <CtaPillLink href="/codex/cloud" label="Learn more about Codex cloud" class="mt-8" />

  </div>
</Tabs>