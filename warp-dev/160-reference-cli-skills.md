---
title: Skills | Reference | Warp
url: https://docs.warp.dev/reference/cli/skills
source: sitemap
fetched_at: 2026-04-29T15:05:02.179268009-03:00
rendered_js: false
word_count: 163
summary: This document explains how to utilize reusable skill specifications to define and execute instruction sets for local and cloud-based AI agents.
tags:
    - warp-agents
    - cli-tools
    - automation
    - workflow-management
    - cloud-agents
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
[Skills](https://docs.warp.dev/agent-platform/warp-agents/skills) are reusable instruction sets that teach agents how to perform specific tasks. Use the `--skill` flag to run an agent from a skill in a repository accessible to your environment.

## Skill spec format

```
# Fully qualified (recommended)
oz agent run-cloud -e <ENV_ID> --skill "owner/repo:skill-name" --prompt "deploy to staging"
# With full path
oz agent run-cloud -e <ENV_ID> --skill "warpdotdev/warp-server:.warp/skills/deploy/SKILL.md" --prompt "deploy to staging"
```

Supported formats:
- `owner/repo:skill-name` — skill by name in a specific repository (recommended)
- `owner/repo:path/to/SKILL.md` — skill by full path in a repository
- `repo:skill-name` — skill by name (only works when repo is configured in your environment)

## Using skills with cloud agents

Skills define reusable workflows that run consistently across environments:

```
# Run a deploy skill from a specific repo
oz agent run-cloud \
  --environment SVhg783GBFQHk1OfdPfFU9 \
  --skill "myorg/backend:.warp/skills/deploy/SKILL.md" \
  --prompt "deploy to staging"
# Run a code review skill
oz agent run-cloud \
  --environment SVhg783GBFQHk1OfdPfFU9 \
  --skill "myorg/backend:code-review" \
  --prompt "review the latest PR"
```

> [!tip]
> When you specify a skill, it provides base instructions. The `--prompt` adds context or parameters for that specific run.
> The run `name` is automatically set to the skill name — no need to pass `--name` explicitly.

## Using skills with local agents

For local agent runs, skills from your current repository are automatically discovered. You can also explicitly specify a skill.

For more information about creating and managing skills, see [Skills](https://docs.warp.dev/agent-platform/warp-agents/skills).
