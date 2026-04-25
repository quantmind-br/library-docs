---
title: Scheduled Tasks (Cron) | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
source: crawler
fetched_at: 2026-04-24T17:00:05.60277386-03:00
rendered_js: false
word_count: 1154
summary: This document details the functionalities of Hermes cron jobs, explaining how to schedule one-shot or recurring tasks using natural language or cron expressions. It covers creation methods via chat, CLI, and conversation, as well as advanced features like skill attachment, setting working directories, editing existing jobs, and managing job lifecycles.
tags:
    - cron-scheduling
    - task-automation
    - hermes-jobs
    - nlp-scheduling
    - skill-management
    - cli-tooling
    - lifecycle-actions
category: reference
---

Schedule tasks to run automatically with natural language or cron expressions. Hermes exposes cron management through a single `cronjob` tool with action-style operations instead of separate schedule/list/remove tools.

## What cron can do now[​](#what-cron-can-do-now "Direct link to What cron can do now")

Cron jobs can:

- schedule one-shot or recurring tasks
- pause, resume, edit, trigger, and remove jobs
- attach zero, one, or multiple skills to a job
- deliver results back to the origin chat, local files, or configured platform targets
- run in fresh agent sessions with the normal static tool list

warning

Cron-run sessions cannot recursively create more cron jobs. Hermes disables cron management tools inside cron executions to prevent runaway scheduling loops.

## Creating scheduled tasks[​](#creating-scheduled-tasks "Direct link to Creating scheduled tasks")

### In chat with `/cron`[​](#in-chat-with-cron "Direct link to in-chat-with-cron")

```bash
/cron add 30m "Remind me to check the build"
/cron add"every 2h""Check server status"
/cron add"every 1h""Summarize new feed items"--skill blogwatcher
/cron add"every 1h""Use both skills and combine the result"--skill blogwatcher --skill maps
```

### From the standalone CLI[​](#from-the-standalone-cli "Direct link to From the standalone CLI")

```bash
hermes cron create "every 2h""Check server status"
hermes cron create "every 1h""Summarize new feed items"--skill blogwatcher
hermes cron create "every 1h""Use both skills and combine the result"\
--skill blogwatcher \
--skill maps \
--name"Skill combo"
```

### Through natural conversation[​](#through-natural-conversation "Direct link to Through natural conversation")

Ask Hermes normally:

```text
Every morning at 9am, check Hacker News for AI news and send me a summary on Telegram.
```

Hermes will use the unified `cronjob` tool internally.

## Skill-backed cron jobs[​](#skill-backed-cron-jobs "Direct link to Skill-backed cron jobs")

A cron job can load one or more skills before it runs the prompt.

### Single skill[​](#single-skill "Direct link to Single skill")

```python
cronjob(
    action="create",
    skill="blogwatcher",
    prompt="Check the configured feeds and summarize anything new.",
    schedule="0 9 * * *",
    name="Morning feeds",
)
```

### Multiple skills[​](#multiple-skills "Direct link to Multiple skills")

Skills are loaded in order. The prompt becomes the task instruction layered on top of those skills.

```python
cronjob(
    action="create",
    skills=["blogwatcher","maps"],
    prompt="Look for new local events and interesting nearby places, then combine them into one short brief.",
    schedule="every 6h",
    name="Local brief",
)
```

This is useful when you want a scheduled agent to inherit reusable workflows without stuffing the full skill text into the cron prompt itself.

## Running a job inside a project directory[​](#running-a-job-inside-a-project-directory "Direct link to Running a job inside a project directory")

Cron jobs default to running detached from any repo — no `AGENTS.md`, `CLAUDE.md`, or `.cursorrules` is loaded, and the terminal / file / code-exec tools run from whatever working directory the gateway started in. Pass `--workdir` (CLI) or `workdir=` (tool call) to change that:

```bash
# Standalone CLI
hermes cron create --schedule"every 1d at 09:00"\
--workdir /home/me/projects/acme \
--prompt"Audit open PRs, summarize CI health, and post to #eng"
```

```python
# From a chat, via the cronjob tool
cronjob(
    action="create",
    schedule="every 1d at 09:00",
    workdir="/home/me/projects/acme",
    prompt="Audit open PRs, summarize CI health, and post to #eng",
)
```

When `workdir` is set:

- `AGENTS.md`, `CLAUDE.md`, and `.cursorrules` from that directory are injected into the system prompt (same discovery order as the interactive CLI)
- `terminal`, `read_file`, `write_file`, `patch`, `search_files`, and `execute_code` all use that directory as their working directory (via `TERMINAL_CWD`)
- The path must be an absolute directory that exists — relative paths and missing directories are rejected at create / update time
- Pass `--workdir ""` (or `workdir=""` via the tool) on edit to clear it and restore the old behaviour

Serialization

Jobs with a `workdir` run sequentially on the scheduler tick, not in the parallel pool. This is deliberate — `TERMINAL_CWD` is process-global, so two workdir jobs running at the same time would corrupt each other's cwd. Workdir-less jobs still run in parallel as before.

## Editing jobs[​](#editing-jobs "Direct link to Editing jobs")

You do not need to delete and recreate jobs just to change them.

### Chat[​](#chat "Direct link to Chat")

```bash
/cron edit <job_id>--schedule"every 4h"
/cron edit <job_id>--prompt"Use the revised task"
/cron edit <job_id>--skill blogwatcher --skill maps
/cron edit <job_id> --remove-skill blogwatcher
/cron edit <job_id> --clear-skills
```

### Standalone CLI[​](#standalone-cli "Direct link to Standalone CLI")

```bash
hermes cron edit <job_id>--schedule"every 4h"
hermes cron edit <job_id>--prompt"Use the revised task"
hermes cron edit <job_id>--skill blogwatcher --skill maps
hermes cron edit <job_id> --add-skill maps
hermes cron edit <job_id> --remove-skill blogwatcher
hermes cron edit <job_id> --clear-skills
```

Notes:

- repeated `--skill` replaces the job's attached skill list
- `--add-skill` appends to the existing list without replacing it
- `--remove-skill` removes specific attached skills
- `--clear-skills` removes all attached skills

## Lifecycle actions[​](#lifecycle-actions "Direct link to Lifecycle actions")

Cron jobs now have a fuller lifecycle than just create/remove.

### Chat[​](#chat-1 "Direct link to Chat")

```bash
/cron list
/cron pause <job_id>
/cron resume <job_id>
/cron run <job_id>
/cron remove <job_id>
```

### Standalone CLI[​](#standalone-cli-1 "Direct link to Standalone CLI")

```bash
hermes cron list
hermes cron pause <job_id>
hermes cron resume <job_id>
hermes cron run <job_id>
hermes cron remove <job_id>
hermes cron status
hermes cron tick
```

What they do:

- `pause` — keep the job but stop scheduling it
- `resume` — re-enable the job and compute the next future run
- `run` — trigger the job on the next scheduler tick
- `remove` — delete it entirely

## How it works[​](#how-it-works "Direct link to How it works")

**Cron execution is handled by the gateway daemon.** The gateway ticks the scheduler every 60 seconds, running any due jobs in isolated agent sessions.

```bash
hermes gateway install# Install as a user service
sudo hermes gateway install--system# Linux: boot-time system service for servers
hermes gateway             # Or run in foreground

hermes cron list
hermes cron status
```

### Gateway scheduler behavior[​](#gateway-scheduler-behavior "Direct link to Gateway scheduler behavior")

On each tick Hermes:

1. loads jobs from `~/.hermes/cron/jobs.json`
2. checks `next_run_at` against the current time
3. starts a fresh `AIAgent` session for each due job
4. optionally injects one or more attached skills into that fresh session
5. runs the prompt to completion
6. delivers the final response
7. updates run metadata and the next scheduled time

A file lock at `~/.hermes/cron/.tick.lock` prevents overlapping scheduler ticks from double-running the same job batch.

## Delivery options[​](#delivery-options "Direct link to Delivery options")

When scheduling jobs, you specify where the output goes:

OptionDescriptionExample`"origin"`Back to where the job was createdDefault on messaging platforms`"local"`Save to local files only (`~/.hermes/cron/output/`)Default on CLI`"telegram"`Telegram home channelUses `TELEGRAM_HOME_CHANNEL``"telegram:123456"`Specific Telegram chat by IDDirect delivery`"telegram:-100123:17585"`Specific Telegram topic`chat_id:thread_id` format`"discord"`Discord home channelUses `DISCORD_HOME_CHANNEL``"discord:#engineering"`Specific Discord channelBy channel name`"slack"`Slack home channel`"whatsapp"`WhatsApp home`"signal"`Signal`"matrix"`Matrix home room`"mattermost"`Mattermost home channel`"email"`Email`"sms"`SMS via Twilio`"homeassistant"`Home Assistant`"dingtalk"`DingTalk`"feishu"`Feishu/Lark`"wecom"`WeCom`"weixin"`Weixin (WeChat)`"bluebubbles"`BlueBubbles (iMessage)`"qqbot"`QQ Bot (Tencent QQ)

The agent's final response is automatically delivered. You do not need to call `send_message` in the cron prompt.

### Response wrapping[​](#response-wrapping "Direct link to Response wrapping")

By default, delivered cron output is wrapped with a header and footer so the recipient knows it came from a scheduled task:

```text
Cronjob Response: Morning feeds
-------------

<agent output here>

Note: The agent cannot see this message, and therefore cannot respond to it.
```

To deliver the raw agent output without the wrapper, set `cron.wrap_response` to `false`:

```yaml
# ~/.hermes/config.yaml
cron:
wrap_response:false
```

### Silent suppression[​](#silent-suppression "Direct link to Silent suppression")

If the agent's final response starts with `[SILENT]`, delivery is suppressed entirely. The output is still saved locally for audit (in `~/.hermes/cron/output/`), but no message is sent to the delivery target.

This is useful for monitoring jobs that should only report when something is wrong:

```text
Check if nginx is running. If everything is healthy, respond with only [SILENT].
Otherwise, report the issue.
```

Failed jobs always deliver regardless of the `[SILENT]` marker — only successful runs can be silenced.

## Script timeout[​](#script-timeout "Direct link to Script timeout")

Pre-run scripts (attached via the `script` parameter) have a default timeout of 120 seconds. If your scripts need longer — for example, to include randomized delays that avoid bot-like timing patterns — you can increase this:

```yaml
# ~/.hermes/config.yaml
cron:
script_timeout_seconds:300# 5 minutes
```

Or set the `HERMES_CRON_SCRIPT_TIMEOUT` environment variable. The resolution order is: env var → config.yaml → 120s default.

## Provider recovery[​](#provider-recovery "Direct link to Provider recovery")

Cron jobs inherit your configured fallback providers and credential pool rotation. If the primary API key is rate-limited or the provider returns an error, the cron agent can:

- **Fall back to an alternate provider** if you have `fallback_providers` (or the legacy `fallback_model`) configured in `config.yaml`
- **Rotate to the next credential** in your [credential pool](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#credential-pool-strategies) for the same provider

This means cron jobs that run at high frequency or during peak hours are more resilient — a single rate-limited key won't fail the entire run.

## Schedule formats[​](#schedule-formats "Direct link to Schedule formats")

The agent's final response is automatically delivered — you do **not** need to include `send_message` in the cron prompt for that same destination. If a cron run calls `send_message` to the exact target the scheduler will already deliver to, Hermes skips that duplicate send and tells the model to put the user-facing content in the final response instead. Use `send_message` only for additional or different targets.

### Relative delays (one-shot)[​](#relative-delays-one-shot "Direct link to Relative delays (one-shot)")

```text
30m     → Run once in 30 minutes
2h      → Run once in 2 hours
1d      → Run once in 1 day
```

### Intervals (recurring)[​](#intervals-recurring "Direct link to Intervals (recurring)")

```text
every 30m    → Every 30 minutes
every 2h     → Every 2 hours
every 1d     → Every day
```

### Cron expressions[​](#cron-expressions "Direct link to Cron expressions")

```text
0 9 * * *       → Daily at 9:00 AM
0 9 * * 1-5     → Weekdays at 9:00 AM
0 */6 * * *     → Every 6 hours
30 8 1 * *      → First of every month at 8:30 AM
0 0 * * 0       → Every Sunday at midnight
```

### ISO timestamps[​](#iso-timestamps "Direct link to ISO timestamps")

```text
2026-03-15T09:00:00    → One-time at March 15, 2026 9:00 AM
```

## Repeat behavior[​](#repeat-behavior "Direct link to Repeat behavior")

Schedule typeDefault repeatBehaviorOne-shot (`30m`, timestamp)1Runs onceInterval (`every 2h`)foreverRuns until removedCron expressionforeverRuns until removed

You can override it:

```python
cronjob(
    action="create",
    prompt="...",
    schedule="every 2h",
    repeat=5,
)
```

## Managing jobs programmatically[​](#managing-jobs-programmatically "Direct link to Managing jobs programmatically")

The agent-facing API is one tool:

```python
cronjob(action="create",...)
cronjob(action="list")
cronjob(action="update", job_id="...")
cronjob(action="pause", job_id="...")
cronjob(action="resume", job_id="...")
cronjob(action="run", job_id="...")
cronjob(action="remove", job_id="...")
```

For `update`, pass `skills=[]` to remove all attached skills.

## Job storage[​](#job-storage "Direct link to Job storage")

Jobs are stored in `~/.hermes/cron/jobs.json`. Output from job runs is saved to `~/.hermes/cron/output/{job_id}/{timestamp}.md`.

Jobs may store `model` and `provider` as `null`. When those fields are omitted, Hermes resolves them at execution time from the global configuration. They only appear in the job record when a per-job override is set.

The storage uses atomic file writes so interrupted writes do not leave a partially written job file behind.

## Self-contained prompts still matter[​](#self-contained-prompts-still-matter "Direct link to Self-contained prompts still matter")

Important

Cron jobs run in a completely fresh agent session. The prompt must contain everything the agent needs that is not already provided by attached skills.

**BAD:** `"Check on that server issue"`

**GOOD:** `"SSH into server 192.168.1.100 as user 'deploy', check if nginx is running with 'systemctl status nginx', and verify https://example.com returns HTTP 200."`

## Security[​](#security "Direct link to Security")

Scheduled task prompts are scanned for prompt-injection and credential-exfiltration patterns at creation and update time. Prompts containing invisible Unicode tricks, SSH backdoor attempts, or obvious secret-exfiltration payloads are blocked.