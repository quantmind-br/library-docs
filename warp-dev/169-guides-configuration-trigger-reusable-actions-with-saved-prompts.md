---
title: Trigger Reusable Actions with Saved Prompts | Guides | Warp
url: https://docs.warp.dev/guides/configuration/trigger-reusable-actions-with-saved-prompts
source: sitemap
fetched_at: 2026-04-29T15:06:37.29217021-03:00
rendered_js: false
word_count: 207
summary: This document outlines how to use Warp's team prompts to automate Git workflows, including commit generation, code review analysis, and pull request creation.
tags:
    - git-automation
    - team-collaboration
    - warp-terminal
    - workflow-optimization
    - pull-requests
    - ai-development-tools
category: guide
optimized: true
optimized_at: 2026-04-29T15:06:37.29217021-03:00
---
Use Warp's saved prompts (Team Prompts) to automate Git workflows: commits, code reviews, and PR creation.

## 1. Automating Commits

Instead of typing long commit messages, use a saved prompt:

- Runs `git diff` and summarizes changes
- Generates a clean commit message
- Pushes automatically to your branch

Access prompts in Warp Drive → Team Prompts. See creator, last used date, and run count. Saved in team drive for reuse.

## 2. Reviewing Code with Prompts

Before creating a PR, run a saved prompt that:

- Reads your current branch
- Reviews diffs
- Highlights logical or stylistic issues
- Suggests improvements

> Example: "Logic bug detected — potential race condition in async handler."

Warp surfaces issues before opening a PR, reducing reviewer back-and-forth.

## 3. Opening a Pull Request Automatically

Trigger the final saved prompt:

- Generates PR title and description
- Pushes the branch
- Opens the PR on GitHub
- Links related issues found in commit messages

## 4. Sharing and Team Usage

All saved prompts live in Team Warp Drive:

- Anyone can discover and run them
- Parameterize or modify as needed
- Usage history and creator info visible

Teams can standardize code reviews, deployments, or build runs.

#git-automation #workflow-optimization #team-collaboration
