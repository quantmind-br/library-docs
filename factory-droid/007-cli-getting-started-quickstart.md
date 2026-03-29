---
title: Quickstart
url: https://docs.factory.ai/cli/getting-started/quickstart.md
source: llms
fetched_at: 2026-02-05T21:41:58.803099112-03:00
rendered_js: false
word_count: 692
summary: This document provides a step-by-step guide to installing and using the Droid CLI to interact with Factory's AI development agent for codebase analysis and automated code changes.
tags:
    - droid-cli
    - installation
    - quickstart
    - ai-coding-assistant
    - factory-ai
    - workflow-integration
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Get productive with droid in 5 minutes using the interactive terminal UI.

This quickstart guide will have you collaborating with Factory's development agent in just a few minutes. You'll experience how droid understands your codebase, makes thoughtful changes, and integrates with your existing workflow.

## Before you begin

Make sure you have:

* A terminal open in a code project
* Git repository (recommended for full workflow demonstration)

## Step 1: Install and start droid

<CodeGroup>
  ```bash macOS/Linux theme={null}
  curl -fsSL https://app.factory.ai/cli | sh
  ```

  ```bash Homebrew theme={null}
  brew install --cask droid
  ```

  ```powershell Windows theme={null}
  irm https://app.factory.ai/cli/windows | iex
  ```
</CodeGroup>

<Note>
  **Linux users:** Ensure `xdg-utils` is installed for proper functionality. Install with: `sudo apt-get install xdg-utils`
</Note>

Then navigate to your project and start the droid CLI.

<CodeGroup>
  ```bash  theme={null}
  # Navigate to your project
  cd /path/to/your/project

  # Start interactive session
  droid
  ```
</CodeGroup>

<img src="https://mintcdn.com/factory/pSQIcJWS0EqHRORW/images/droid_tui_intro.png?fit=max&auto=format&n=pSQIcJWS0EqHRORW&q=85&s=9946098711744d1c1b8fa50445dba229" alt="Droid CLI" height="450" className="rounded-lg" data-og-width="850" data-og-height="720" data-path="images/droid_tui_intro.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/pSQIcJWS0EqHRORW/images/droid_tui_intro.png?w=280&fit=max&auto=format&n=pSQIcJWS0EqHRORW&q=85&s=3a59699f5b22e857e52b6ad03062eb8d 280w, https://mintcdn.com/factory/pSQIcJWS0EqHRORW/images/droid_tui_intro.png?w=560&fit=max&auto=format&n=pSQIcJWS0EqHRORW&q=85&s=6c8d77d47dba40bf917b48b32e49dd8b 560w, https://mintcdn.com/factory/pSQIcJWS0EqHRORW/images/droid_tui_intro.png?w=840&fit=max&auto=format&n=pSQIcJWS0EqHRORW&q=85&s=a1852531473e281acc57585c0365c419 840w, https://mintcdn.com/factory/pSQIcJWS0EqHRORW/images/droid_tui_intro.png?w=1100&fit=max&auto=format&n=pSQIcJWS0EqHRORW&q=85&s=560efceac58250738b3abde63c92bc2b 1100w, https://mintcdn.com/factory/pSQIcJWS0EqHRORW/images/droid_tui_intro.png?w=1650&fit=max&auto=format&n=pSQIcJWS0EqHRORW&q=85&s=f02cefcefe269180798a877c57eaf7d5 1650w, https://mintcdn.com/factory/pSQIcJWS0EqHRORW/images/droid_tui_intro.png?w=2500&fit=max&auto=format&n=pSQIcJWS0EqHRORW&q=85&s=8592a73eb05c1b20b004f7342a27520f 2500w" />

You'll see droid's welcome screen in a full-screen terminal interface. If prompted, sign in via your browser to connect to Factory's development agent.

## Step 2: Explore your codebase

Let's start by having droid understand your project. Try one of these questions:

```

> analyze this codebase and explain the overall architecture

```

```

> what technologies and frameworks does this project use?

```

```

> where are the main entry points and how is testing set up?

```

Droid reads your files contextually and leverages organizational knowledge to provide comprehensive insights about your project structure and conventions.

## Step 3: Make your first code change

Now let's see droid in action with a simple modification:

```

> add comprehensive logging to the main application startup

```

Droid will:

1. Analyze your current logging setup
2. Propose specific changes with a clear plan
3. Show you exactly what will be modified
4. Wait for your approval before making changes

This transparent review process ensures you maintain full control over all code modifications.

## Step 4: Experience enterprise workflows

Try a more complex task that showcases droid's enterprise capabilities:

```

> audit this codebase for security vulnerabilities and create a remediation plan

```

Or provide context from your team's tools by pasting a link:

```

> implement the feature described in this Jira ticket: https://company.atlassian.net/browse/PROJ-123

```

If you've integrated these platforms through Factory's dashboard, droid can automatically read context from Jira, Notion, Slack, and other sources. Droid can also connect to additional tools via MCP integrations for even more capabilities.

## Step 5: Handle version control

Droid makes Git operations conversational and intelligent:

```

> review my uncommitted changes and suggest improvements before I commit

```

```

> create a well-structured commit with a descriptive message following our team conventions

```

```

> analyze the last few commits and identify any potential issues or patterns

```

## Essential controls

Here are the key interactions you'll use daily:

| Action           | What it does                   | How to use                    |
| ---------------- | ------------------------------ | ----------------------------- |
| Send message     | Submit a task or question      | Type and press **Enter**      |
| Multi-line input | Write longer prompts           | **Shift+Enter** for new lines |
| Approve changes  | Accept proposed modifications  | Accept change in the TUI      |
| Reject changes   | Decline proposed modifications | Reject change in the TUI      |
| Switch modes     | Toggle between modes           | **Shift+Tab**                 |
| View shortcuts   | See all available commands     | Press **?**                   |
| Exit session     | Leave droid                    | **Ctrl+C** or type `exit`     |

### Useful slash commands

Quick shortcuts to common actions:

* `/review` - Start AI-powered code review workflow ([learn more](/cli/features/code-review))
* `/settings` - Configure droid behavior, models, and preferences
* `/model` - Switch between AI models mid-session
* `/mcp` - Manage Model Context Protocol servers
* `/account` - Open your Factory account settings in browser
* `/billing` - View and manage your billing settings
* `/help` - See all available commands

[Learn how to create custom slash commands →](/cli/configuration/custom-slash-commands)

## Collaboration best practices

**Be specific with context:**
Instead of: "fix the bug"
Try: "fix the authentication timeout issue where users get logged out after 5 minutes instead of the configured 30 minutes"

**Use spec mode for complex features:**
For larger features, use [Specification Mode](/cli/user-guides/specification-mode) which automatically provides planning before implementation without needing to explicitly request it.

**Leverage organizational knowledge:**

```

> following our team's coding standards, implement the user preferences feature described in ticket PROJ-123

```

**Use the review workflow:**
Always review droid's proposed changes before approval. The transparent diff view helps you understand exactly what will be modified.

## Pro tips for enterprise teams

**Security-first approach:**
Droid automatically considers security implications and will flag potential vulnerabilities during code generation.

**Compliance integration:**
Connect your compliance tools through MCP to ensure all changes meet your organization's standards.

**Team knowledge sharing:**
Droid learns from your organization's patterns and can help maintain consistency across team members and projects.

## What's next?

<CardGroup cols={2}>
  <Card title="Common Use Cases" icon="lightbulb" href="/cli/getting-started/common-use-cases">
    Explore real-world scenarios and workflows
  </Card>

  <Card title="Configuration" icon="gear" href="/cli/configuration/settings">
    Customize droid for your team's workflow
  </Card>

  <Card title="AGENTS.md Guide" icon="file-text" href="/cli/configuration/agents-md">
    Document your project conventions and commands
  </Card>

  <Card title="IDE Integration" icon="code" href="/cli/configuration/ide-integrations">
    Use droid within your favorite editor
  </Card>
</CardGroup>

```
```