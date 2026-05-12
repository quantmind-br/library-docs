---
title: Scheduled agents | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/triggers/scheduled-agents
source: sitemap
fetched_at: 2026-04-29T15:04:23.698441459-03:00
rendered_js: false
word_count: 682
summary: This document explains how to configure and manage automated, recurring cloud agents in Warp using the Oz CLI to perform routine maintenance tasks on a schedule.
tags:
    - cloud-agents
    - cron-scheduling
    - automation
    - maintenance-tasks
    - cli-commands
    - workflow-automation
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Scheduled Agents run cloud agents automatically on a recurring cron-based schedule. Each run starts from a clean session, executes a fixed prompt, and produces its own task and session history.

**Key characteristics:**

- Runs automatically based on a cron expression
- Uses a fixed prompt defined at schedule creation
- Starts a fresh agent session for every run
- Executes in a specific [environment](https://docs.warp.dev/agent-platform/cloud-agents/environments), if provided
- Consumes credits when it runs
- Can be paused, updated, or deleted at any time

## Common use cases

Best suited for maintenance-style workflows, including [[061-agent-platform-cloud-agents-skills-as-agents|skill-based agents]]:

- Dead code or unused feature flag cleanup
- Dependency updates or security scans
- Issue or PR triage on a recurring cadence
- Periodic documentation refreshes
- Repository hygiene (formatting, lint checks)
- Scheduled reporting or audits

## Creating a schedule

Use `oz schedule create` with required flags:

| Flag | Required | Description |
|---|---|---|
| `--name` | Yes | Schedule identifier |
| `--cron` | Yes | Cron expression |
| `--prompt` | Yes | Prompt for the agent |
| `--environment` | No | Environment ID for execution |

**Optional flags:**

| Flag | Description |
|---|---|
| `--skill <SPEC>` | Use a skill as the base prompt (format: `repo:skill_name` or `org/repo:skill_name`) |
| `--host <WORKER_ID>` | Run on a specific self-hosted worker |
| `--mcp <SPEC>` | Attach MCP servers (inline JSON, file path, or UUID) — repeatable |
| `--model <MODEL_ID>` | Override the default model |
| `--file <PATH>` | Load schedule configuration from a YAML or JSON file |

> [!info]
> Environments are optional — without one, the agent runs in a barebones sandbox with no repository access.

**Example:** Run an agent to clean up old feature flags every four days:

```bash
oz schedule create \
  --name "feature-flag-cleanup" \
  --cron "0 10 */4 * *" \
  --prompt "Clean up feature flags that have been enabled in production for more than 90 days." \
  --environment my-env
```

## Cron schedule format

Standard cron syntax with five fields: `minute hour day-of-month month day-of-week`

| Example | Runs at |
|---|---|
| `0 10 * * *` | Every day at 10:00 AM |
| `0 10 */4 * *` | Every four days at 10:00 AM |
| `0 8 1 * *` | 8:00 AM on the first day of every month |

## Listing scheduled agents

```bash
oz schedule list
```

Returns a table with Schedule ID, name, cron schedule, paused status, last run time, next scheduled run, and scope. Completed runs include links to the task and full agent session.

### Viewing a specific schedule

```bash
oz schedule get <schedule-id>
```

Returns full schedule configuration, prompt, model, environment, MCP settings, recent runs, and links to tasks and sessions.

## Pausing and unpausing

```bash
# Pause
oz schedule pause <schedule-id>

# Unpause
oz schedule unpause <schedule-id>
```

When paused, the agent does not run at its scheduled times.

## Editing scheduled agents

```bash
oz schedule update <schedule-id> [flags]
```

Updatable properties: name, cron schedule, prompt, skill, environment, model, MCP configuration, and host.

| Additional update flag | Description |
|---|---|
| `--skill <SPEC>` | Update the skill used as the base prompt |
| `--remove-skill` | Remove the skill from this scheduled agent |
| `--host <WORKER_ID>` | Update the execution host |
| `--mcp <SPEC>` | Add MCP servers |
| `--remove-mcp <SERVER_NAME>` | Remove an MCP server by name |
| `--remove-environment` | Remove the environment from this schedule |

Changes apply only to future runs. Past runs and their session history remain unchanged.

## Deleting a scheduled agent

```bash
oz schedule delete <schedule-id>
```

Deleting stops all future runs. Previous runs and their session history remain accessible.

## Execution model

- Every run starts a fresh session
- No state carries over between runs unless explicitly persisted
- Runs execute automatically without human intervention
- All usage billed to the team's shared credit balance
- Failed runs do not block future runs — each execution is independent

## Permissions and responsibility

By creating a Scheduled Agent, you are responsible for:

- The cron schedule and frequency
- The instructions in the prompt
- The environment and integrations available to the agent
- Credits consumed by scheduled executions

## Scheduled Agents vs triggers

Use Scheduled Agents when work should happen on a predictable cadence. Use [triggered cloud agents](https://docs.warp.dev/agent-platform/cloud-agents/triggers) for event-driven responses (Slack mentions, PR updates, issue changes). Many teams use both: triggers for reactive workflows, Scheduled Agents for proactive maintenance.
