---
title: API & SDK Quickstart | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/quickstart
source: sitemap
fetched_at: 2026-04-29T15:05:06.02816218-03:00
rendered_js: false
word_count: 284
summary: This document provides a quickstart guide for interacting with the Oz API to programmatically create, manage, and monitor cloud agent runs.
tags:
    - oz-api
    - cloud-agents
    - rest-api
    - automation
    - api-authentication
    - workflow-management
category: tutorial
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
The Oz API runs and manages cloud agents from CI/CD pipelines, backend services, scripts, or custom tooling — without the Warp desktop app.

> [!example]
> See [PowerFixer](https://github.com/warpdotdev/power-fixer-setup) — a demo issue triage bot built by the Warp team.

## Prerequisites

- **Warp API key** — Create one at **Settings** > **Cloud platform** > **Oz Cloud API Keys**. See [[031-reference-api-and-sdk-quickstart|API Keys]] for step-by-step instructions.
- **Oz cloud environment** — Agents run inside a configured environment with repos and dependencies. Follow the [[054-agent-platform-cloud-agents-integrations|Cloud Agents Quickstart]] first if needed.

## 1. Set your API key

Export your key so the API authenticates requests automatically. All commands in this guide reference the `WARP_API_KEY` environment variable.

```bash
export WARP_API_KEY=wk-...
```

## 2. Create your first run

Submit a prompt to start an agent run:

```bash
curl https://api.warp.dev/v1/runs \
  -H "Authorization: Bearer $WARP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"environment_id": "<ENV_ID>", "prompt": "Hello, world!"}'
```

Find `<ENV_ID>` with `oz environment list` or in the [Oz web app](https://oz.warp.dev).

The API returns a `run_id` immediately. The agent starts asynchronously — check its status using the run ID.

## 3. Check run status

```bash
curl https://api.warp.dev/v1/runs/<RUN_ID> \
  -H "Authorization: Bearer $WARP_API_KEY"
```

`state` values:

| State | Description |
|-------|-------------|
| `QUEUED` | Waiting to start |
| `INPROGRESS` | Actively running |
| `SUCCEEDED` | Completed successfully |
| `FAILED` | Error — check `status_message` in the response |

List all recent runs:

```bash
curl https://api.warp.dev/v1/runs \
  -H "Authorization: Bearer $WARP_API_KEY"
```

## 4. View the results

Once the run reaches `SUCCEEDED`, the response includes a `session_link` — a direct URL to the full run transcript with commands executed, files changed, and agent output.

Manage runs in the [Oz dashboard](https://oz.warp.dev/runs).

## Next steps

- **Full API reference** — [Oz API](https://docs.warp.dev/reference/api-and-sdk/agent) documents all endpoints, parameters, and response schemas.
- **Real-world example** — [Demo: Sentry monitoring with SDK](https://docs.warp.dev/reference/api-and-sdk/demo-sentry-monitoring-with-sdk) shows how to build a webhook handler that triggers agents from production errors.

#oz-api #cloud-agents #rest-api #automation
