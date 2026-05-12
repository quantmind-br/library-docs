---
title: environment_setup_failed | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/environment-setup-failed
source: sitemap
fetched_at: 2026-04-29T15:05:22.250290202-03:00
rendered_js: false
word_count: 310
summary: This document explains the causes and resolution steps for the environment_setup_failed error occurring during cloud agent runtime initialization.
tags:
    - cloud-agent
    - error-handling
    - environment-configuration
    - troubleshooting
    - mcp-server
category: reference
optimized: true
optimized_at: 2026-04-29T15:05:22.250290202-03:00
---
The `environment_setup_failed` error occurs when the cloud agent's runtime environment could not be initialized, including repository cloning, setup command execution, working directory resolution, and MCP server startup.

> [!note]
> Although this returns HTTP 500, it is classified as a **user error** (task state → FAILED) because the failure is caused by the environment configuration, not by Warp's infrastructure.

## Details

| Field | Value |
|-------|-------|
| HTTP Status | `500 Internal Server Error` |
| Retryable | No |
| Task State | FAILED |

## When does this occur?

This error is returned when any part of the environment initialization process fails:

- **Git clone failed** — The repository URL is incorrect, the branch does not exist, or the agent lacks repository access
- **Setup command failed** — A command in the environment's setup commands list exited with an error (missing dependencies, script errors)
- **Working directory not found** — The configured working directory does not exist after cloning
- **MCP server startup failed** — An MCP server configured for the environment could not start

The `title` field in the response describes the specific setup failure.

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/environment-setup-failed",
  "title": "Git clone failed: repository not found",
  "status": 500,
  "instance": "/api/v1/agent/tasks",
  "error": "Git clone failed: repository not found",
  "retryable": false
}
```

## How to resolve

1. **Check repository configuration** — Verify the repository URL and branch name in your [environment settings](https://docs.warp.dev/agent-platform/cloud-agents/environments). Ensure the repository exists and is accessible.
2. **Check setup commands** — Run the setup commands locally to confirm they work. Look for missing dependencies, incorrect paths, or syntax errors.
3. **Check working directory** — Ensure the working directory path exists relative to the cloned repository root.
4. **Check MCP server configuration** — Verify MCP server startup commands and that any required dependencies or credentials are available. See [MCP Servers for Agents](https://docs.warp.dev/reference/cli/mcp-for-cloud-agents).
5. **Check secrets** — If setup commands reference environment variables from [secrets](https://docs.warp.dev/agent-platform/cloud-agents/secrets), verify the secrets are configured and in scope.

## Related

- [[264-reference-api-and-sdk-troubleshooting-errors-content-policy-violation|content_policy_violation]]
- [[263-reference-api-and-sdk-troubleshooting-errors-conflict|conflict]]
