---
title: 'Demo: Issue triage bot | Agents | Warp'
url: https://docs.warp.dev/agent-platform/cloud-agents/integrations/demo-issue-triage-bot
source: sitemap
fetched_at: 2026-04-29T15:04:34.869810193-03:00
rendered_js: false
word_count: 183
summary: This document explains how to automate the triage and resolution of GitHub issues using the Warp coding agent within a GitHub Actions workflow.
tags:
    - github-actions
    - warp-agent
    - issue-triage
    - automation
    - pull-requests
    - bug-reporting
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
This demo shows how to trigger Warp's coding agent from a GitHub Action to automate bug report handling as issues hit your repository.

The workflow acts as a maintainer-first "front door" for bugs: it evaluates whether a report is actionable, asks for missing details when it isn't, and escalates directly into a draft pull request when it is.

## Triage phase

- The agent reads the issue (and optionally your bug report template) and returns a `ready` / `not-ready` decision.
- If the report is missing key context (description, reproduction steps), the workflow posts a friendly comment requesting the missing info and applies a `needs-info` label.

## Investigation + fix phase

When a report has sufficient detail, the agent:
1. Investigates the codebase
2. Implements a fix
3. Adds tests
4. Runs verification
5. Returns a PR-ready summary

The GitHub Action then commits the changes and opens a draft PR that follows the repo's pull request template, linking back to the original issue.

> [!tip]
> See [Environments](https://docs.warp.dev/agent-platform/cloud-agents/environments) for setting up the agent environment used by this workflow.

#github-actions #warp-agent #issue-triage #automation #pull-requests
