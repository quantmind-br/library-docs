---
title: Create Project Rules | Guides | Warp
url: https://docs.warp.dev/guides/configuration/how-to-create-project-rules-for-an-existing-project-astro-+-typescript-+-tailwind
source: sitemap
fetched_at: 2026-04-29T15:06:31.52975147-03:00
rendered_js: false
word_count: 147
summary: This document explains how to create and manage a Warp.md file to provide AI agents with consistent project context, setup instructions, and structural guidelines.
tags:
    - warp-md
    - ai-onboarding
    - project-documentation
    - context-management
    - developer-workflow
    - prompt-engineering
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
> [!info]
> This educational module shows how to create and maintain a `Warp.md` file so Warp agents understand your project's setup, commands, architecture, and structure.

A **Project Rules** file (`Warp.md`) acts as your project's AI onboarding guide. Document your setup once and Warp will always have that context.

The demo walks through:
1. Creating the file
2. Opening it in a side editor
3. Organizing it with standard Markdown headings for clear sections

> [!warning]
> Run **verbatim** prompts in Warp to create and verify your rules file, then open it in the editor.

> [!tip]
> If the file grows large (e.g., **500+ lines**), run it through a **prompt optimizer** to catch duplication, remove overlaps, and slim it down.

For large repos, generate localized rule files in sub-trees. Navigate into a subfolder and run `/init` again to create a **directory-scoped** `Warp.md` tailored to that area.
