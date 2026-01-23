---
title: Configuration - Zencoder Docs
url: https://docs.zencoder.ai/features/autonomous-agents-configuration
source: crawler
fetched_at: 2026-01-23T09:28:13.207469611-03:00
rendered_js: false
word_count: 333
summary: This document provides instructions for setting up autonomous runs via CI/CD platform triggers or webhooks, covering configuration, troubleshooting, and security best practices.
tags:
    - autonomous-runs
    - ci-cd-integration
    - webhook-triggers
    - zencoder-configuration
    - automation-security
    - troubleshooting
category: guide
---

Autonomous runs can start from two trigger types: platform triggers that originate in your CI provider (GitHub Actions, GitLab CI/CD, Bitbucket Pipelines) and webhook triggers that fire when external systems like Jira, Linear, or internal apps hit the Zencoder webhook endpoint. Platform triggers take a few more steps because they require workflow files and provider-specific tokens, but both paths share the same credential setup and secret management. Follow the sections below to wire up the option that fits your automation plan.

## Platform Trigger

Events coming from your CI/CD pipeline—such as pull request creation, branch pushes, or scheduled builds—launch autonomous runs through providers like GitHub, GitLab, or Bitbucket.

- GitHub Actions
- GitLab CI/CD
- Bitbucket Pipelines

## Webhook Trigger

Any app capable of sending an HTTP webhook can start an autonomous workflow, whether it is Jira, Linear, Zendesk, or an internal system that posts to the exposed webhook endpoint.

- GitHub Actions
- GitLab CI/CD
- Bitbucket Pipelines

### Workflow Example

## Custom Models & Private Deployments

Autonomous agents use the same `settings.json` from [Custom Models](https://docs.zencoder.ai/features/custom-models-configuration). Add your local, VPC, or third-party providers there once and they automatically show up when GitHub/GitLab/Bitbucket workflows run—no extra agent work needed. To keep everything inside your network, follow the [Private Deployments](https://docs.zencoder.ai/features/private-deployments) steps (especially “configure custom models from local or VPC endpoints”) and simply load the JSON before the agent runs:

```
      - name: Add config
        run: echo "${{ secrets.CONFIG }}" > ~/.zencoder/settings.json
```

## Troubleshooting

- **Authentication failures:** Confirm client ID and secret values, check token expiration dates, and ensure each platform token has the required repository permissions.
- **Agent not found:** look for the agent name in the workflow, confirm the agent is shared with your organization, and double-check the agent configuration in the Zencoder UI.
- **Webhook not triggering:** Validate the webhook URL, ensure the Jira automation rule is enabled, and confirm any filtering labels (for example `zen-agents-bitbucket`) match exactly.

## Security Considerations

- **Credential management:** Use each platform’s secret manager, rotate tokens regularly, and scope credentials to the minimum permissions needed.
- **Repository access:** Grant the least privilege required, enforce branch protection policies, and require human review before merging agent-generated pull requests.