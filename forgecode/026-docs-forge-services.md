---
title: ForgeCode
url: https://forgecode.dev/docs/forge-services/
source: sitemap
fetched_at: 2026-03-29T16:30:40.809393-03:00
rendered_js: false
word_count: 213
summary: This document provides an overview of ForgeCode Services, a runtime layer that enhances agent performance through context retrieval, tool-call validation, and skill management, along with instructions for managing its lifecycle within a project.
tags:
    - runtime-layer
    - context-engine
    - tool-call-guardrails
    - project-indexing
    - agent-configuration
category: guide
---

ForgeCode Services is the runtime layer that helps the model stay on trajectory while it explores, edits, and executes tools.

These are the most visible capabilities, not the full feature set.

- **Context engine**: Beats SOTA across retrieval benchmarks, uses up to 93% fewer tokens, and stays fast while starting the agent in the most relevant files and functions.
- **Tool-call guardrails**: Catches invalid arguments, common tool-call mistakes, then auto-corrects them before they fail.
- **Skill engine**: Assists the model in choosing the right skill for the job, so task-specific guidance is applied at the right time.

**There is nothing to configure here.** After you enable it, it keeps running in the background.

Run:

Then select **ForgeServices** in the provider list and complete browser authentication.

No API key required — sign in with Google or GitHub.

Run:

This indexes your project and enables `sem_search`.

To monitor indexing progress and see which files are being synced, run:

Files can be ignored using [Ignoring Files](https://forgecode.dev/docs/ignoring-files/).

If a file is ignored, ForgeCode Services excludes it from sync, and the context engine cannot use that file for retrieval.

Run:

Look for `sem_search` under `SYSTEM`.

Run:

This signs you out and disables ForgeCode Services.

To enable again later, run `:login`, select **ForgeServices**, then run `:sync` for the project you want indexed.