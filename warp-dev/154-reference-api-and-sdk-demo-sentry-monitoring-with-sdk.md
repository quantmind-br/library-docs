---
title: 'Demo: Sentry monitoring with SDK | Reference | Warp'
url: https://docs.warp.dev/reference/api-and-sdk/demo-sentry-monitoring-with-sdk
source: sitemap
fetched_at: 2026-04-29T15:05:09.096890321-03:00
rendered_js: false
word_count: 157
summary: This document outlines how to build a TypeScript-based monitoring service that automatically converts production Sentry errors into actionable draft pull requests using Warp cloud agents.
tags:
    - typescript-sdk
    - sentry-integration
    - automated-debugging
    - webhook-server
    - cloud-agents
    - pull-request-automation
category: tutorial
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
This demo builds a TypeScript "Sentry monitor" service that listens for Sentry alerts (e.g., a Go nil pointer dereference) and triggers a Warp cloud agent to investigate. The server validates webhooks, extracts stack traces, and injects them into an agent run inside a Warp Environment so the agent can inspect the repo and propose a fix.

The result is a draft GitHub pull request for human review — not silent autonomous changes.

## What is covered

- **TypeScript SDK** — trigger agent runs and retrieve run details
- **Task lifecycle** — handle states (queued → running) to reliably fetch a session link
- **Warp Environments** — run agents inside a configured environment so they can inspect real code, run tests, and validate fixes
- **Sentry webhook server** — filter, validate, and route only relevant errors to an agent
- **Draft PRs** — result workflow creates draft pull requests for maintainer review

#typescript-sdk #sentry-integration #automated-debugging #webhook-server #cloud-agents #pull-request-automation
