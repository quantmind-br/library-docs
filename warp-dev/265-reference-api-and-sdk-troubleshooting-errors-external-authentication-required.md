---
title: external_authentication_required | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/external-authentication-required
source: sitemap
fetched_at: 2026-04-29T15:05:14.310860675-03:00
rendered_js: false
word_count: 351
summary: This document explains the external_authentication_required error, identifying its causes related to unauthorized external services and providing steps to resolve authentication and access issues.
tags:
    - error-handling
    - authentication
    - cloud-agent
    - oauth
    - troubleshooting
    - github-integration
category: reference
optimized: true
optimized_at: 2026-04-29T19:05:00Z
---
# external_authentication_required

The `external_authentication_required` error occurs when a cloud agent task needs access to an external service that the user hasn't authorized, or when the Warp GitHub App doesn't have access to the required repositories.

## Details

| Field | Value |
|-------|-------|
| HTTP Status | `401 Unauthorized` |
| Retryable | No |
| Task State | FAILED |

## When does this occur?

This error is returned when:

- **GitHub not connected** — Your Warp account is not linked to a GitHub account, but the task's environment includes GitHub repositories
- **Repository inaccessible** — The Warp GitHub App is not installed on, or does not have access to, one or more repositories required by the task's environment
- **Account matching failed** — A Slack or Linear user who triggered the task cannot be matched to a Warp account

## Additional metadata fields

| Field | Type | Description |
|-------|------|-------------|
| `provider` | string | The external service name (e.g., `"github"`, `"slack"`, `"linear"`) |
| `auth_url` | string | A URL to complete the authorization flow (when available) |
| `inaccessible_repos` | array | List of repository names the agent cannot access (when applicable) |

## Example responses

### GitHub user not connected

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/external-authentication-required",
  "title": "User is not connected to GitHub",
  "status": 401,
  "instance": "/api/v1/agent/tasks",
  "error": "User is not connected to GitHub. Authorize access here: https://...",
  "retryable": false,
  "provider": "github",
  "auth_url": "https://github.com/login/oauth/authorize?..."
}
```

### Repository inaccessible

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/external-authentication-required",
  "title": "User does not have access to the following repositories in the environment: acme/backend",
  "status": 401,
  "detail": "inaccessible repos: acme/backend",
  "instance": "/api/v1/agent/tasks",
  "error": "User does not have access to the following repositories in the environment: acme/backend (inaccessible repos: acme/backend)",
  "retryable": false,
  "provider": "github",
  "auth_url": "https://github.com/apps/warp-dev/installations/new",
  "inaccessible_repos": ["acme/backend"]
}
```

### Account matching failed (Slack/Linear)

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/external-authentication-required",
  "title": "Unable to locate your Warp account",
  "status": 401,
  "instance": "/api/v1/agent/tasks",
  "error": "Unable to locate your Warp account",
  "retryable": false,
  "provider": "slack"
}
```

## How to resolve

### GitHub not connected

1. Follow the `auth_url` in the response to connect your GitHub account to Warp.
2. Complete the OAuth authorization flow.
3. Retry the task.

### Repository inaccessible

1. Follow the `auth_url` to install or reconfigure the Warp GitHub App.
2. Ensure the app has access to all repositories listed in `inaccessible_repos`.
3. Retry the task.

> [!warning]
> If you are using a **team API key** (service account), ensure the Warp GitHub App is installed on the organization that owns the repositories.

### Account matching failed

1. Ensure your Slack or Linear account is associated with the same email as your Warp account.
2. If using Slack, verify the Warp Slack integration is installed in your workspace.
3. Contact your team admin if the issue persists.

#error-reference #authentication #external-services
