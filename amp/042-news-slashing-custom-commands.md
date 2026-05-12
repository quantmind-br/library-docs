---
title: Slashing Custom Commands
url: https://ampcode.com/news/slashing-custom-commands
source: crawler
fetched_at: 2026-02-06T02:07:44.439207985-03:00
rendered_js: false
word_count: 133
summary: This document explains the transition from custom commands to agent skills and provides step-by-step instructions for migrating existing commands both automatically and manually.
tags:
    - migration
    - custom-commands
    - agent-skills
    - configuration
    - automation
category: guide
---

We're removing custom commands in favor of [skills](https://ampcode.com/manual#agent-skills). They were two ways of doing the same thing, except that only you could invoke custom commands, and only the agent could invoke skills. Now that [you can invoke skills directly](https://ampcode.com/news/user-invokable-skills), there's no reason to keep custom commands around anymore.

## Migrating Custom Commands to Skills

It's easy and takes just a few minutes.

### Let Amp Do It For You

If you have custom commands in `.agents/commands/` or `~/.config/amp/commands/`, ask Amp to migrate them for you with the following prompt:

```
Migrate my custom commands from .agents/commands/ to skills in .agents/skills.

For each command:
1. Create a new skill directory in .agents/skills/ named after the command
2. If it's a markdown file, rename it to SKILL.md and add frontmatter with name and description
3. If it's an executable, create a SKILL.md that describes when and how to run the script, and move the executable to a scripts/ subdirectory
4. Delete the original command file

Also do this for global custom commands in ~/.config/amp/commands (which should be migrated to skills ~/.config/agents/skills).
```

### Or Do It Manually

**Markdown commands:** Move your `.md` file to a skill directory:

```
# Before
.agents/commands/code-review.md

# After
.agents/skills/code-review/SKILL.md
```

Add frontmatter:

```
---
name: code-review
description: Review code for quality and best practices
---

[Your existing content]
```

**Executable commands:** Move the executable into a `scripts/` subdirectory:

```
# Before
.agents/commands/deploy

# After
.agents/skills/deploy/
├── SKILL.md
└── scripts/
    └── deploy
```

In `SKILL.md`, tell the agent how to use it:

```
---
name: deploy
description: Deploy the application
---

Run `{baseDir}/scripts/deploy` to deploy.
```