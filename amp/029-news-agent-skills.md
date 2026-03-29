---
title: Agent Skills
url: https://ampcode.com/news/agent-skills
source: crawler
fetched_at: 2026-02-06T02:08:19.713006374-03:00
rendered_js: false
word_count: 158
summary: This document introduces Amp agent skills, which allow agents to lazily load specific tool instructions, and outlines the directory structure for skill installation.
tags:
    - amp-agent
    - agent-skills
    - tool-use
    - workspace-configuration
    - skill-management
category: concept
---

Amp supports agent skills. Skills let the agent lazily-load specific instructions on how to use local tools. We like skills because they improve agent tool use performance in a very context efficient way.

Skills are installed to `.agents/skills/` in your workspace by default. Amp also reads from `~/.config/agents/skills/` for user-level skills, and `.claude/skills/` and `~/.claude/skills/` for compatibility with existing skills.

Our team has been doing a ton of experimenting with skills over the past few weeks. Here are a few that we have found particularly useful:

- [**Agent Sandbox**](https://github.com/disler/agent-sandbox-skill): Isolated execution environment for running untrusted code safely.
- [**Agent Skill Creator**](https://github.com/FrancyJGLisboa/agent-skill-creator): Meta-skill for creating Claude agents autonomously with comprehensive skill architecture patterns.
- [**BigQuery**](https://github.com/sourcegraph/amp/blob/main/.agents/skills/bigquery/SKILL.md): Expert use of the bq cli tool for querying BigQuery datasets.
- [**Tmux**](https://github.com/ampcode/amp-contrib/blob/main/.agents/skills/tmux/skill.md): Run servers and long-running tasks in the background.
- [**Web Browser**](https://github.com/mitsuhiko/agent-stuff/blob/main/skills/web-browser/SKILL.md): Interact with web pages via Chrome DevTools Protocol for clicking, filling forms, and navigation.

Read more about how to use skills in our manual [https://ampcode.com/manual#agent-skills](https://ampcode.com/manual#agent-skills)