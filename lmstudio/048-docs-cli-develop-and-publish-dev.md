---
title: '`lms dev` (Beta)'
url: https://lmstudio.ai/docs/cli/develop-and-publish/dev
source: sitemap
fetched_at: 2026-04-07T21:27:56.173952742-03:00
rendered_js: false
word_count: 99
summary: This document explains how to use the `lms dev` command within a plugin project to start a local development server that automatically rebuilds and reloads upon file changes for LM Studio plugins.
tags:
    - dev-server
    - plugin-development
    - local-testing
    - lm-studio
    - typescript
    - coding-guide
category: tutorial
---

Use `lms dev` inside a plugin project to run a local dev server that rebuilds and reloads on file changes.

This feature is a part of LM Studio [Plugins](https://lmstudio.ai/docs/typescript/plugins), currently in private beta.

### Run the dev plugin server[](#run-the-dev-plugin-server)


This verifies `manifest.json`, installs dependencies if needed, and starts a watcher that rebuilds the plugin on changes. Supported runners: Node/ECMAScript and Deno.

### Install the plugin instead of running dev[](#install-the-plugin-instead-of-running-dev)


### Flags[](#flags)

-i, --install (optional) : flag

Install the plugin into LM Studio instead of running the dev server

--no-notify (optional) : flag

Do not show the "Plugin started" notification in LM Studio