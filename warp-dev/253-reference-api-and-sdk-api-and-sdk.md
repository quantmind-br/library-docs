---
title: Oz API & SDK | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/api-and-sdk
source: sitemap
fetched_at: 2026-04-29T15:05:05.400782564-03:00
rendered_js: false
word_count: 757
summary: This document provides an overview of the Oz API and its associated SDKs, which allow users to programmatically execute and manage cloud agent runs. It details core concepts, key REST endpoints, and the benefits of using provided Python and TypeScript SDKs for integration.
tags:
    - oz-api
    - cloud-agents
    - rest-api
    - sdk
    - automation
    - agent-orchestration
category: api
optimized: true
optimized_at: 2026-04-29T19:05:00Z
---
# Oz API & SDK

The Oz API lets you create and inspect [[194-agent-platform-cloud-agents-overview|Cloud Agents]] runs over HTTP from any system (CI, cron, backend services, internal tools), without requiring the Warp desktop app.

**With the API you can:**

- Run an agent by submitting a prompt plus optional config (model, environment, MCP servers, base prompt, etc.)
- Monitor execution by listing runs and tracking state transitions over time (queued → in progress → succeeded/failed)
- Inspect results and provenance by fetching a run's full details, including the original prompt, source/creator metadata, session link, and resolved agent configuration

## Oz Agent SDK

Oz provides official [Python](https://github.com/warpdotdev/oz-sdk-python) and [TypeScript](https://github.com/warpdotdev/oz-sdk-typescript) SDKs that wrap the Oz API with:

- **Typed requests and responses** (editor autocomplete, fewer schema mistakes)
- **Built-in retries and timeouts** (with per-request overrides)
- **Consistent error types** that map to API status codes
- **Helpers for raw responses** when you need headers/status or custom parsing

> [!tip]
> If you're building an integration (CI, Slack bots, internal tooling, orchestrators), the SDKs are typically the quickest and safest starting point.

**SDK vs raw REST**

- Use the SDK when you want strong typing, standardized error handling, and easy concurrency patterns.
- Use raw REST when you want minimal dependencies or full control over your HTTP client (the SDKs also support calling undocumented endpoints when needed).

## Oz API

### REST API Base URL

All endpoints are served over HTTPS.

### Core Concepts

#### Agent runs

An agent run represents a single execution of a cloud agent, created with a prompt and optional configuration. Each run has:

| Field | Description |
|-------|-------------|
| `run_id` | Unique identifier |
| `title` | Human-readable label |
| `prompt` | Instructions for the agent |
| `state` | `QUEUED`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED` |
| `created_at`, `updated_at` | Timestamps |
| `session_id`, `session_link` | Session information (optional) |
| `agent_config` | Resolved configuration (optional) |

See the [[252-reference-api-and-sdk-agent|Agents API]] for details on how runs are created and listed.

#### Agent configuration

You can influence how an agent runs using `AmbientAgentConfig`, including:

| Field | Description |
|-------|-------------|
| `name` | Human-readable label for grouping/filtering. Set automatically from [[196-agent-platform-warp-agents-capabilities-overview-skills|skills]]. Use `name` query parameter on `GET /agent/runs` to filter. |
| `model_id` | LLM selection |
| `base_prompt` | Shape agent behavior |
| `environment_id` | Choose a `CloudEnvironment` |
| `skill_spec` | Use a skill as base prompt (format: `owner/repo:skill-name` or `owner/repo:path/to/SKILL.md`) |
| `mcp_servers` | Enable tools via MCP |

See the [Python SDK](https://github.com/warpdotdev/oz-sdk-python) or [TypeScript SDK](https://github.com/warpdotdev/oz-sdk-typescript) for the full configuration schema.

### Key Endpoints

The Agents API exposes three primary endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/agent/run` | `POST` | Create a new agent run with a prompt and optional config and title. Returns `run_id` and initial state. |
| `/agent/runs` | `GET` | List runs with pagination and filters for state, config_name, model_id, creator, source, and creation time. |
| `/agent/runs/{runId}` | `GET` | Fetch full details for a single run, including session link and resolved configuration. |

All endpoint semantics, query parameters, and error codes are documented on the [[252-reference-api-and-sdk-agent|Agents API]].

#### Models Reference

The API shares a set of reusable models across endpoints. Detailed JSON schemas, types, and enums are available in the SDK repos ([Python](https://github.com/warpdotdev/oz-sdk-python), [TypeScript](https://github.com/warpdotdev/oz-sdk-typescript)).

| Model | Description |
|-------|-------------|
| `RunAgentRequest` | Request to run an agent |
| `RunAgentResponse` | Response from running an agent |
| `ListRunsResponse` | Paginated list of runs |
| `RunItem` | Individual run details |
| `PageInfo` | Pagination metadata |
| `RunStatusMessage` | Status update |
| `RunCreatorInfo` | Creator metadata |
| `RunState` | Run state enum |
| `RunSourceType` | Source type enum |
| `AmbientAgentConfig` | Agent configuration |
| `MCPServerConfig` | MCP server configuration |
| `Error` | Error response |

## Oz Agent SDKs

### Python SDK

The Python SDK is the recommended way to call the Oz API from Python services and scripts. It provides:

- Sync + async clients
- Typed request/response models
- Configurable retries/timeouts and structured errors

See the [Python SDK GitHub repo](https://github.com/warpdotdev/oz-sdk-python) for installation, full API reference (api.md), and up-to-date examples.

### TypeScript SDK

The TypeScript SDK is the recommended way to call the Oz API from Node.js services and modern TS/JS runtimes. It provides:

- Fully typed params/responses
- First-class error handling, retries/timeouts
- Support across common runtimes where fetch is available or polyfilled

See the [TypeScript SDK GitHub repo](https://github.com/warpdotdev/oz-sdk-typescript) for installation, full API reference (api.md), and up-to-date examples.

#api-reference #oz-api #sdk
