---
title: GitHub App - Factory Documentation
url: https://docs.factory.ai/integrations/github-app
source: sitemap
fetched_at: 2026-01-13T19:04:26.126853767-03:00
rendered_js: false
word_count: 439
summary: This guide explains how to use the /install-gh-app command to configure the Factory GitHub App, enabling automated code reviews and @droid interactions within GitHub Actions workflows.
tags:
    - github-app
    - code-review
    - github-actions
    - setup
    - automation
    - cli
    - permissions
category: guide
---

## Overview

The `/install-gh-app` command provides a guided workflow for installing the Factory GitHub App and configuring GitHub Actions workflows. This enables Droid to respond to @droid mentions in issues and PR comments, and optionally provide automated code reviews on new pull requests. When you run `/install-gh-app`, droid guides you through verifying prerequisites, selecting a repository, installing the GitHub App, and creating workflow files via a pull request.

## Quick start

## Prerequisites

Before running `/install-gh-app`, ensure you have the GitHub CLI installed and authenticated.

### Install GitHub CLI

- macOS (Homebrew)
- macOS (MacPorts)
- Linux/WSL
- Windows

```
type -p curl >/dev/null || (sudo apt update && sudo apt install curl -y)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh -y
```

```
winget install --id GitHub.cli
```

### Authenticate with GitHub

### Verify required scopes

The CLI needs `repo` and `read:org` scopes. If missing, refresh your authentication:

```
gh auth refresh -s repo,read:org
```

## Available workflows

### @Droid workflow

Enables Droid to respond when you tag `@droid` in:

- Issue comments
- Pull request comments
- Pull request reviews
- Issue descriptions and titles

**Triggers:**

- `issue_comment` - When a comment contains @droid
- `pull_request_review_comment` - When a PR review comment contains @droid
- `pull_request_review` - When a PR review body contains @droid
- `issues` - When an issue body or title contains @droid

**Use cases:**

- Ask Droid to implement features described in issues
- Request code changes in PR comments
- Get help understanding code in reviews

### Droid Review workflow

Provides automated code review on new pull requests. **Triggers:**

- `pull_request` - When a PR is opened, reopened, or marked ready for review

**Use cases:**

- Automatic first-pass review on all PRs
- Catch common issues before human review
- Consistent review coverage across the team

## Setup steps after installation

After the `/install-gh-app` workflow completes, you need to:

## Permissions

### Repository admin permissions

For the smoothest setup, you should have admin access to the repository. If you don’t have admin permissions, you’ll see a warning but can still proceed. You may need a repository admin to:

- Approve the GitHub App installation
- Add the `FACTORY_API_KEY` secret
- Merge the workflow PR

### GitHub App permissions

The Factory Droid GitHub App requires these permissions:

- **Contents:** Read and write (to push workflow files and make code changes)
- **Pull requests:** Read and write (to create PRs and post reviews)
- **Issues:** Read and write (to respond to issue comments)
- **Actions:** Read (to monitor workflow runs)

## Tips and best practices

## Example usage

```
cd my-project
droid

> /install-gh-app
```

After completing the guided flow, Droid creates a PR with workflow files. Here’s what the generated Droid Review workflow looks like:

Generated Droid Review Workflow

```
name: Droid Code Review

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

concurrency:
  group: droid-review-${{ github.event.pull_request.number }}
  cancel-in-progress: true

permissions:
  pull-requests: write
  contents: read
  issues: write

jobs:
  code-review:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    if: github.event.pull_request.draft == false

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          ref: ${{ github.event.pull_request.head.sha }}

      - name: Install Droid CLI
        run: |
          curl -fsSL https://app.factory.ai/cli | sh
          echo "$HOME/.local/bin" >> $GITHUB_PATH

      - name: Configure git identity
        run: |
          git config user.name "Droid Agent"
          git config user.email "droidagent@factory.ai"

      - name: Perform automated code review
        env:
          FACTORY_API_KEY: ${{ secrets.FACTORY_API_KEY }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          droid exec --auto high --model claude-sonnet-4-5-20250929 -f prompt.txt
```

To customize the workflow after installation, see the [Automated Code Review guide](https://docs.factory.ai/guides/droid-exec/code-review#customizing-the-workflow).

## See also

- [Automated Code Review](https://docs.factory.ai/guides/droid-exec/code-review) - Customizing the code review workflow
- [Factory GitHub App](https://github.com/apps/factory-droid) - Direct link to install the app
- [API keys](https://app.factory.ai/settings/api-keys) - Generate your Factory API key
- [Code Review](https://docs.factory.ai/cli/features/code-review) - Local code review with `/review` command
- [Droid Exec GitHub Actions](https://docs.factory.ai/guides/droid-exec/github-actions) - More GitHub Actions automation examples