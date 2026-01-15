---
title: GitHub Integration Security - Factory Documentation
url: https://docs.factory.ai/enterprise/github-integration-security
source: sitemap
fetched_at: 2026-01-13T19:04:36.008310528-03:00
rendered_js: false
word_count: 702
summary: This document outlines the security architecture, data flows, access controls, and audit capabilities of the Factory Droid GitHub Action.
tags:
    - security
    - github-actions
    - permissions
    - data-privacy
    - audit-logging
    - api-key
category: configuration
---

The Factory Droid GitHub Action enables automated code review and PR assistance directly within your GitHub workflows. This page explains the security architecture, data flows, and controls that govern how the integration operates.

* * *

## Overview

The Droid GitHub Action (`Factory-AI/droid-action`) runs **entirely inside GitHub Actions** using your own runners. It does not require a separate hosted service or persistent connection to Factory infrastructure beyond standard API authentication.

* * *

## Architecture and data flows

When a workflow runs, the following sequence occurs:

1. **Trigger detection** – The action detects `@droid` mentions in PR comments, descriptions, or review comments.
2. **Permission verification** – Before executing, the action verifies the triggering user has write access to the repository.
3. **Context gathering** – Droid collects PR metadata, changed files, and existing comments from the checked‑out repository.
4. **Droid Exec** – The CLI runs with GitHub MCP tools pre‑registered, allowing it to interact with the PR via GitHub APIs.
5. **LLM requests** – Prompts are sent to your configured model providers through Factory’s standard routing.
6. **Results** – Droid posts inline comments or updates the PR description directly via GitHub APIs.
7. **Token revocation** – GitHub App tokens are automatically revoked at the end of the workflow.

### Data boundaries

Data typeWhere it flowsRetentionSource codeGitHub runner (transient checkout)Discarded after workflowPR metadataGitHub APIsGitHub’s retention policiesPrompts and contextConfigured LLM providersPer your model provider agreementsWorkflow logsGitHub ActionsYour repository’s log retention settingsDebug artifactsGitHub Actions artifacts7 days (configurable)

* * *

### Factory API key

The action requires a Factory API key (`FACTORY_API_KEY`) stored as a GitHub secret. This key:

- Authenticates Droid Exec sessions with Factory’s API.
- Is subject to your org’s model allowlists, rate limits, and policies.
- Should be rotated regularly following your organization’s key management practices.

### GitHub App tokens

When using the Factory Droid GitHub App:

- The app requests an installation token scoped to the specific repository.
- Tokens are short‑lived and automatically revoked after the workflow completes.
- The app only requests permissions necessary for its operation (contents, pull requests, issues).

If you prefer not to use the GitHub App, you can provide a custom `github_token` input with appropriate permissions.

### User permission verification

Before executing any `@droid` command, the action verifies:

1. The triggering user has **write access** to the repository.
2. The user is not a bot (unless explicitly allowed via `allowed_bots` input).
3. The comment or trigger matches the expected format.

This prevents unauthorized users from invoking Droid.

* * *

## Security controls

### Permission scoping

The action requests only the GitHub permissions it needs:

```
permissions:
  contents: write # Read code, write for fixes
  pull-requests: write # Comment on and update PRs
  issues: write # Comment on issues
  id-token: write # OIDC token for secure auth
  actions: read # Read workflow run metadata
```

You can further restrict permissions in your workflow file based on your security requirements.

### Bot and user filtering

Control who can trigger the action:

InputPurpose`allowed_bots`Comma‑separated list of bot usernames allowed to trigger, or `*` for all. Default: none.`allowed_non_write_users`Usernames to allow without write permissions. Use with extreme caution.

### Network restrictions (experimental)

For enhanced security, you can restrict network access during Droid execution:

```
- uses: Factory-AI/droid-action@v1
  with:
    factory_api_key: ${{ secrets.FACTORY_API_KEY }}
    experimental_allowed_domains: |
      api.factory.ai
      api.anthropic.com
      api.openai.com
```

This limits outbound connections to only the specified domains.

### Secrets protection

The action follows security best practices for secrets handling:

- API keys are passed via environment variables from GitHub secrets.
- The `show_full_output` option is disabled by default to prevent accidental exposure of sensitive data in logs.
- Debug artifacts are retained for only 7 days by default.

* * *

## Audit and monitoring

### Workflow logs

All Droid activity is logged in GitHub Actions workflow runs, providing:

- Timestamps for all operations.
- Command inputs and outputs (unless containing sensitive data).
- Success/failure status for each step.
- Links to any comments or changes made.

### Debug artifacts

The action uploads debug artifacts including:

- Droid session logs.
- Console output.
- Session metadata.

These artifacts are retained for 7 days by default and can be used for troubleshooting or audit purposes.

### Integration with Factory telemetry

If your organization uses Factory’s OTEL telemetry, Droid Exec sessions from GitHub Actions are included in your telemetry data, providing:

- Session metrics tagged with repository and workflow context.
- LLM usage and cost attribution.
- Tool invocation tracking.

See [Compliance, Audit & Monitoring](https://docs.factory.ai/enterprise/compliance-audit-and-monitoring) for details on Factory’s telemetry capabilities.

* * *

## Deployment recommendations

* * *

## Comparison with other deployment patterns

AspectGitHub ActionCLI on developer machineDroid Exec in CIExecution environmentGitHub runnersLocal workstationYour CI runnersCode accessTransient checkoutFull local accessTransient checkoutAuthenticationFactory API keyFactory API keyFactory API keyTriggerPR events, commentsManual invocationCI pipeline eventsAudit trailGitHub Actions logsLocal + Factory telemetryCI logs + Factory telemetry

All deployment patterns use the same underlying Droid Exec runtime and are subject to the same Factory org policies.