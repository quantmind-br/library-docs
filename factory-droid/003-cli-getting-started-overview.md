---
title: Overview
url: https://docs.factory.ai/cli/getting-started/overview.md
source: llms
fetched_at: 2026-03-03T01:13:11.191169-03:00
rendered_js: false
word_count: 364
summary: This document provides an introductory overview of the droid CLI tool, outlining its installation methods, core development features, and enterprise-grade integration capabilities.
tags:
    - droid-cli
    - factory-ai
    - cli-installation
    - ai-development-agent
    - software-automation
    - workflow-integration
category: concept
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Meet `droid` — the power of Factory in your terminal

## Get started in 30 seconds

<CodeGroup>
  ```bash macOS/Linux theme={null}
  curl -fsSL https://app.factory.ai/cli | sh
  ```

  ```powershell Windows theme={null}
  irm https://app.factory.ai/cli/windows | iex
  ```

  ```bash npm theme={null}
  npm install -g droid
  ```
</CodeGroup>

Then navigate to your project and start the droid CLI.

<CodeGroup>
  ```bash  theme={null}
  # Navigate to your project
  cd /path/to/your/project

  # Start interactive session
  droid
  ```
</CodeGroup>

You're now connected to Factory's development agent from your terminal. [Try the 5-minute quickstart →](/cli/getting-started/quickstart)

<Note>
  **Quick tip:** Press `!` to toggle bash mode and run shell commands directly without AI interpretation. Press `Esc` to return to normal mode. See the [CLI Reference](/reference/cli-reference#bash-mode) for details.
</Note>

## What `droid` brings to your workflow

* **End-to-end feature development**: From planning to implementation to testing - droid handles the complete development lifecycle while keeping you in control through transparent review workflows.
* **Deep codebase understanding**: Leverages your organization's shared knowledge across repositories, documentation, and issue tracking to provide contextually aware assistance that improves over time.
* **Engineering system integration**: Connects directly to your existing tools — with native integrations to Jira, Notion, Slack, and many more tools — so development work stays synchronized with your team's processes.
* **Production-ready automation**: Deploy the same workflows locally during development or in CI/CD pipelines, with enterprise security and compliance built-in from day one.

## Why teams choose Factory

* **Built for enterprise**: On-premise deployment options, SOC-2 compliance, and air-gapped environments. We prioritize security and quality over racing to the lowest price point.
* **Your tools, enhanced**: Works within your existing terminal, IDE, and development environment. No need to switch editors or learn new interfaces — droid integrates where you're already productive.
* **Transparent and controllable**: Every decision droid makes is visible and reviewable. You maintain full oversight of code changes with our native diff viewer and approval workflows.
* **Model flexibility**: Not locked into a single AI provider. Factory allows you to route tasks to the best model for each job while maintaining consistent behavior and memory across your organization.

## Next steps

<CardGroup cols={2}>
  <Card title="Quickstart" icon="rocket" href="/cli/getting-started/quickstart">
    See droid in action with practical examples
  </Card>

  <Card title="Common Use Cases" icon="lightbulb" href="/cli/getting-started/common-use-cases">
    Step-by-step guides for common workflows
  </Card>

  <Card title="IDE Integration" icon="code" href="/cli/configuration/ide-integrations">
    Add droid to your IDE
  </Card>

  <Card title="Configuration" icon="gear" href="/cli/configuration/settings">
    Customize droid for your workflow
  </Card>
</CardGroup>

## Additional resources

<CardGroup cols={2}>
  <Card title="AGENTS.md Guide" icon="file-lines" href="/cli/configuration/agents-md">
    Configure project-specific guidance and conventions
  </Card>

  <Card title="CLI Reference" icon="terminal" href="/reference/cli-reference">
    Complete reference for droid commands
  </Card>

  {false && (
      <>
        <Card
          title="CI/CD Integration"
          icon="diagram-project"
          href="/cli/configuration/ci-cd"
        >
          Use droid in your continuous integration pipelines
        </Card>
        <Card
          title="Pricing & Usage"
          icon="credit-card"
          href="/cli/account/tokens-and-pricing"
        >
          Understand usage tracking and billing
        </Card>
      </>
    )}
</CardGroup>

```
```