---
title: Skills as agents | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/skills-as-agents
source: sitemap
fetched_at: 2026-04-29T15:04:38.022334054-03:00
rendered_js: false
word_count: 389
summary: This document explains how to utilize skills to define, discover, and execute agent workflows in both local and cloud environments, including instructions for scheduling and programmatic access.
tags:
    - agent-platform
    - automation
    - skill-discovery
    - workflow-management
    - scheduled-tasks
    - cli-tools
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Skills are reusable instruction sets that start agents from a consistent base prompt, enabling consistent behavior across runs and users. Skills work with both local and cloud agents.

**Use skills when you want:**

- **Consistent behavior** — Same skill produces the same workflow every time, regardless of who triggers it.
- **Repeatable automation** — Run skills on schedules for maintenance tasks (code cleanup, dependency updates, issue triage).
- **Shareable workflows** — Skills live in repositories for team versioning and collaboration.

## Skill discovery

Skill discovery differs by agent type:

### Local agents

For `oz agent run`, Warp scans these directories in order of precedence:

- `.warp/skills/`
- `.agents/skills/`
- `.claude/skills/`
- `.codex/skills/`
- `.cursor/skills/`
- `.gemini/skills/`
- `.copilot/skills/`
- `.factory/skills/`
- `.github/skills/`
- `.opencode/skills/`

Use fully qualified format `owner/repo:skill-name` to specify a skill from any accessible repository.

### Cloud agents

For `oz agent run-cloud`, skills are discovered from repositories configured in your [environments](https://docs.warp.dev/agent-platform/cloud-agents/environments).

1. **Add the repository** to an environment
2. **The skill appears** in the Agents list in the [[056-agent-platform-cloud-agents-oz-web-app|Oz web app]]

> [!info]
> List available skills programmatically using the `GET /agent` endpoint. See the [Oz API](https://docs.warp.dev/reference/api-and-sdk) reference.

## Running skill-based agents

### Oz web app

Browse skills on the **Agents** page, start runs by selecting a skill/environment/prompt, and create scheduled agents.

### CLI

Use the `--skill` flag with the Oz CLI. See [Using skills](https://docs.warp.dev/reference/cli#using-skills) for full CLI documentation.

### API & SDK

Use the `skill_spec` parameter when creating a run. See [Agent configuration](https://docs.warp.dev/reference/api-and-sdk#agent-configuration) in the API reference.

## Running skills on a schedule

Skill-based agents excel as [[063-agent-platform-cloud-agents-triggers-scheduled-agents|Scheduled Agents]] for:

- **Dead code cleanup** — Weekly scans for unused code or stale feature flags
- **Dependency updates** — Daily/weekly security update checks
- **Issue triage** — Regular categorization of open issues
- **Documentation refresh** — Periodic sync with code

Create scheduled skill-based agents via CLI (`oz schedule create --skill <SPEC>`) or the [[056-agent-platform-cloud-agents-oz-web-app|Oz web app]] **New schedule** action.

## Suggested skills

The [[056-agent-platform-cloud-agents-oz-web-app|Oz web app]] displays suggested agents from the public [warpdotdev/oz-skills](https://github.com/warpdotdev/oz-skills) repository. These pre-built skills demonstrate common use cases and serve as starting points.

Suggested skills appear on the Agents page under the **Suggested** filter.

## Related

- [[196-agent-platform-warp-agents-capabilities-overview-skills|Skills]] — Create skills and skill file format
- [[205-agent-platform-cloud-agents-environments|Environments]] — Configure repositories for cloud agents
- [[056-agent-platform-cloud-agents-oz-web-app|Oz Web App]] — Visual interface for managing cloud agents
