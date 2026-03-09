---
title: Quickstart
url: https://docs.factory.ai/web/getting-started/quickstart.md
source: llms
fetched_at: 2026-03-03T01:14:59.384421-03:00
rendered_js: false
word_count: 157
summary: This document provides a step-by-step quickstart guide for downloading, installing, and configuring the Factory App to work with a local codebase using an AI assistant.
tags:
    - quickstart
    - installation
    - factory-app
    - codebase-integration
    - ai-assistant
    - developer-tools
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Get up and running with the Factory App in 5 minutes

<Note>
  **Research Preview**: The Factory App is now available for download on Mac and Windows.
</Note>

## Step 1: Download and Install

<Steps>
  <Step title="Download Factory">
    <CardGroup cols={3}>
      <Card title="Mac (Apple Silicon)" icon="apple" href="https://app.factory.ai/api/desktop?platform=darwin&architecture=arm64">
        M1/M2/M3
      </Card>

      <Card title="Mac (Intel)" icon="apple" href="https://app.factory.ai/api/desktop?platform=darwin&architecture=x64">
        Intel
      </Card>

      <Card title="Windows" icon="windows" href="https://app.factory.ai/api/desktop?platform=win32">
        Windows x64
      </Card>
    </CardGroup>
  </Step>

  <Step title="Install">
    * **Mac**: Open the `.dmg` file and drag Factory to Applications
    * **Windows**: Run the installer
  </Step>

  <Step title="Sign In">
    Launch Factory and sign in with your account.
  </Step>
</Steps>

## Step 2: Connect to Your Codebase

<Steps>
  <Step title="Set Your Working Directory">
    Set your working directory to your project folder. Factory connects directly to your local machine.
  </Step>

  <Step title="Select Your Model">
    Choose your preferred AI model from the model selector. You can change this anytime.
  </Step>
</Steps>

## Step 3: Start Building

<Steps>
  <Step title="Ask Droid Anything">
    Start with something simple:

    ```
    Analyze this codebase and explain the architecture
    ```

    Or jump straight into coding:

    ```
    Add error handling to the user authentication flow
    ```

    Droid will analyze your codebase, propose changes, and show you exactly what will be modified before applying anything.
  </Step>
</Steps>

## Example Workflows

### Feature Development

```
Implement a dark mode toggle following our existing theme patterns
```

### Bug Fixing

```
Fix the authentication timeout issue where users get logged out after 5 minutes
```

### Code Review

```
Review this PR and suggest improvements for error handling and edge cases
```

### Security Audit

```
Audit this codebase for security vulnerabilities and create a remediation plan
```

## Tips

* **Be specific**: Include relevant details like file names, error messages, or ticket numbers
* **Use context**: Reference team tools with '@' mentions or paste links directly
* **Review changes**: Always review Droid's proposed changes before approval

## Next Steps

<CardGroup cols={2}>
  <Card title="Integrations" icon="plug" href="/web/integrations/linear">
    Connect Slack, Linear, and other tools
  </Card>

  <Card title="CLI" icon="terminal" href="/cli/getting-started/overview">
    Use Droid from your terminal
  </Card>
</CardGroup>