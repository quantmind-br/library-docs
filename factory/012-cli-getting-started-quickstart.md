---
title: Quickstart - Factory Documentation
url: https://docs.factory.ai/cli/getting-started/quickstart
source: sitemap
fetched_at: 2026-01-13T19:03:44.502542707-03:00
rendered_js: false
word_count: 526
summary: This quickstart guide instructs users on how to install and interact with the droid CLI to perform codebase analysis, implement changes, and manage version control.
tags:
    - quickstart
    - cli
    - ai-agent
    - git-integration
    - code-review
    - developer-tools
category: tutorial
---

This quickstart guide will have you collaborating with Factory’s development agent in just a few minutes. You’ll experience how droid understands your codebase, makes thoughtful changes, and integrates with your existing workflow.

## Before you begin

Make sure you have:

- A terminal open in a code project
- Git repository (recommended for full workflow demonstration)

## Step 1: Install and start droid

Then navigate to your project and start the droid CLI.

![Droid CLI](https://mintcdn.com/factory/pSQIcJWS0EqHRORW/images/droid_tui_intro.png?fit=max&auto=format&n=pSQIcJWS0EqHRORW&q=85&s=9946098711744d1c1b8fa50445dba229) You’ll see droid’s welcome screen in a full-screen terminal interface. If prompted, sign in via your browser to connect to Factory’s development agent.

## Step 2: Explore your codebase

Let’s start by having droid understand your project. Try one of these questions:

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

Now let’s see droid in action with a simple modification:

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

Try a more complex task that showcases droid’s enterprise capabilities:

```

> audit this codebase for security vulnerabilities and create a remediation plan

```

Or provide context from your team’s tools by pasting a link:

```

> implement the feature described in this Jira ticket: https://company.atlassian.net/browse/PROJ-123

```

If you’ve integrated these platforms through Factory’s dashboard, droid can automatically read context from Jira, Notion, Slack, and other sources. Droid can also connect to additional tools via MCP integrations for even more capabilities.

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

Here are the key interactions you’ll use daily:

ActionWhat it doesHow to useSend messageSubmit a task or questionType and press **Enter**Multi-line inputWrite longer prompts**Shift+Enter** for new linesApprove changesAccept proposed modificationsAccept change in the TUIReject changesDecline proposed modificationsReject change in the TUISwitch modesToggle between modes**Shift+Tab**View shortcutsSee all available commandsPress **?**Exit sessionLeave droid**Ctrl+C** or type `exit`

### Useful slash commands

Quick shortcuts to common actions:

- `/review` - Start AI-powered code review workflow ([learn more](https://docs.factory.ai/cli/features/code-review))
- `/settings` - Configure droid behavior, models, and preferences
- `/model` - Switch between AI models mid-session
- `/mcp` - Manage Model Context Protocol servers
- `/account` - Open your Factory account settings in browser
- `/billing` - View and manage your billing settings
- `/help` - See all available commands

[Learn how to create custom slash commands →](https://docs.factory.ai/cli/configuration/custom-slash-commands)

## Collaboration best practices

**Be specific with context:** Instead of: “fix the bug” Try: “fix the authentication timeout issue where users get logged out after 5 minutes instead of the configured 30 minutes” **Use spec mode for complex features:** For larger features, use [Specification Mode](https://docs.factory.ai/cli/user-guides/specification-mode) which automatically provides planning before implementation without needing to explicitly request it. **Leverage organizational knowledge:**

```

> following our team's coding standards, implement the user preferences feature described in ticket PROJ-123

```

**Use the review workflow:** Always review droid’s proposed changes before approval. The transparent diff view helps you understand exactly what will be modified.

## Pro tips for enterprise teams

**Security-first approach:** Droid automatically considers security implications and will flag potential vulnerabilities during code generation. **Compliance integration:** Connect your compliance tools through MCP to ensure all changes meet your organization’s standards. **Team knowledge sharing:** Droid learns from your organization’s patterns and can help maintain consistency across team members and projects.

## What’s next?