---
title: Set Tech Stack Preferences with Rules | Guides | Warp
url: https://docs.warp.dev/guides/configuration/how-to-set-tech-stack-preferences-with-rules
source: sitemap
fetched_at: 2026-04-29T15:06:32.01743971-03:00
rendered_js: false
word_count: 118
summary: This document explains how to configure AI rules within Warp to ensure code generation and project scaffolding consistently align with your preferred technology stacks and frameworks.
tags:
    - warp-ai
    - tech-stack
    - configuration
    - ai-assistant
    - project-scaffolding
    - workflow-optimization
category: configuration
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Guide Warp's AI to use your preferred tech stack when scaffolding apps or generating code.

## The Problem

When you ask AI to scaffold a new web app, it often defaults to React and Express, creating friction when your workflow is based on modern tools. Warp solves this by storing stack preferences directly as Rules.

## Rule Setup

Create a Rule that defines your preferred frameworks for each project type.

```markdown
Rule: Tech Stack Preferences
- Use Astro for websites.
- Use SvelteKit for desktop apps.
- Prefer Vite for build tooling.
- Avoid legacy stacks like Create React App or Express.
```

Once added, Warp's AI automatically applies these defaults when generating or updating projects.

> [!tip]
> Think of it as setting a default coding personality for your agent.

## Why It Matters

- Generate **consistent boilerplates**
- Follow your **current tech standards**
- Skip outdated or irrelevant dependencies
