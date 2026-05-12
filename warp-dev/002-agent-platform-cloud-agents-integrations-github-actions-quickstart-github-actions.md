---
title: GitHub Actions quickstart | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/integrations/github-actions/quickstart-github-actions
source: sitemap
fetched_at: 2026-04-29T15:04:29.035217095-03:00
rendered_js: false
word_count: 487
summary: This document explains how to integrate Oz agents into GitHub Actions workflows to automate tasks like pull request reviews using Warp's cloud infrastructure.
tags:
    - github-actions
    - oz-agent
    - ci-cd
    - automation
    - warp-integration
    - workflow-configuration
category: tutorial
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Add Oz agents to your GitHub Actions workflows with [`oz-agent-action`](https://github.com/warpdotdev/oz-agent-action). This quickstart walks you through setting up your first GitHub Actions integration: a PR review workflow that automatically analyzes pull requests and posts inline review comments.

## Prerequisites

- **Warp API key** — In the Warp app, click your profile photo, then go to **Settings** > **Cloud platform** > **Oz Cloud API Keys** to create one. Use a personal key if the agent needs to write to your repo. See [API Keys](https://docs.warp.dev/reference/cli/api-keys) for details.
- **A GitHub repository with Actions enabled** — The workflow file will live in `.github/workflows/` in your repo.

## 1. Add your API key as a GitHub Actions secret

Store your Warp API key as a GitHub Actions secret so workflows can authenticate without exposing the key in your code.

1. In your repository on GitHub, go to **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret**.
3. Set the name to `WARP_API_KEY`.
4. Paste your API key into the **Secret** field.
5. Click **Add secret**.

## 2. Create the workflow file

This workflow triggers an Oz agent whenever a PR is opened or marked ready for review. The agent reviews the diff and posts inline comments.

Create `.github/workflows/oz-pr-review.yml` in your repository with the following content:

```yaml
name: Oz PR review
on:
  pull_request:
    types: [opened, ready_for_review]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: warpdotdev/oz-agent-action@v1
        with:
          api-key: ${{ secrets.WARP_API_KEY }}
          prompt: |
            Review the code changes in this pull request. Focus on:
            - Logic errors or potential bugs
            - Security vulnerabilities
            - Performance issues
            - Code style inconsistencies
            Post your feedback as inline review comments on the relevant lines.
```

This workflow listens for pull request events and runs the `oz-agent-action` step, which executes the prompt to review code changes. Commit and push this file to your default branch to activate the workflow.

## 3. Open a pull request

Create a new pull request in your repository to trigger the workflow.

To verify the workflow ran:

1. Go to the **Actions** tab in your repository.
2. Click **Oz PR review** in the list of workflows.
3. Select the most recent run to see the agent's output in the job logs.

## 4. View the run

Each `oz-agent-action` step creates a cloud agent run you can inspect from the Oz dashboard:

- **Warp app** — Open the conversations panel to see the run alongside your other agent activity.

When the run completes, the agent posts feedback as inline review comments on the PR.

> [!tip]
> The agent runs in Warp's cloud infrastructure — not on GitHub's runners — using the workflow's GitHub token for repository access. Each run is isolated, tracked, and auditable, just like any manually triggered cloud agent run.

## Next steps

- **Explore more workflow patterns** — The [oz-agent-action repository](https://github.com/warpdotdev/oz-agent-action) includes ready-to-use consumer workflow templates for responding to `@oz-agent` comments, auto-fixing labeled issues, daily issue summaries, fixing failing CI checks, and suggesting review fixes. Copy any template from `consumer-workflows/` into `.github/workflows/` in your repo.
- **Use skills for reusable behavior** — Replace the inline `prompt` with a `skill` parameter to apply consistent, version-controlled instructions across all your CI workflows. See [Skills](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/skills).
- **Read the full reference** — [GitHub Actions](https://docs.warp.dev/agent-platform/cloud-agents/integrations/github-actions) covers all action inputs, output handling, session sharing for debugging, and troubleshooting.