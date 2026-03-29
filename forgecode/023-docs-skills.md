---
title: ForgeCode
url: https://forgecode.dev/docs/skills/
source: sitemap
fetched_at: 2026-03-29T14:52:24.14323419-03:00
rendered_js: false
word_count: 228
summary: This document explains how to create and use reusable workflow skills in ForgeCode by writing SKILL.md files that are automatically loaded and applied based on tasks.
tags:
    - skills
    - workflows
    - reusable-tasks
    - skill-md
    - forgecode
    - claude-code
    - automation
category: guide
---

Skills are reusable workflows you teach ForgeCode once. Write the process down in a `SKILL.md` file and place any supporting scripts, examples, or other resources alongside it — ForgeCode will automatically load the right skill whenever the task calls for it.

Skills live in `.forge/skills/<skill-name>/SKILL.md` inside your project. Each skill is a plain markdown file — write it the same way you'd explain the process to a new teammate.

Here's what a release notes skill looks like:

ForgeCode reads all skills at the start of a session and automatically applies the relevant one based on what you're asking it to do — no need to invoke them by name.

The easiest way to create a skill is to ask ForgeCode directly. Describe the workflow — the steps, scripts, and edge cases — and it will generate the `SKILL.md` in the right place:

Review the generated file, adjust anything that doesn't match your setup, and it's ready to use. The more detail you give, the better the skill.

**Skills are fully compatible with [Claude Code](https://code.claude.com/docs/en/skills).** The `SKILL.md` format is identical — no conversion needed.

If you already have skills in a Claude Code project, copy them straight into ForgeCode:

They work without any changes.

To confirm ForgeCode has picked up your skills, run `:skill` in the chat. You'll see a list of all available skills along with their descriptions.