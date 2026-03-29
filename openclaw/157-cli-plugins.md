---
title: Plugins - OpenClaw
url: https://docs.openclaw.ai/cli/plugins
source: sitemap
fetched_at: 2026-01-30T20:34:52.75498479-03:00
rendered_js: false
word_count: 103
summary: Provides instructions for managing Gateway plugins including installation, enabling, disabling, and updating plugins within the OpenClaw system.
tags:
    - plugin-management
    - gateway
    - cli-commands
    - security
    - installation
    - updates
category: guide
---

Manage Gateway plugins/extensions (loaded in-process). Related:

- Plugin system: [Plugins](https://docs.openclaw.ai/plugin)
- Plugin manifest + schema: [Plugin manifest](https://docs.openclaw.ai/plugins/manifest)
- Security hardening: [Security](https://docs.openclaw.ai/gateway/security)

## Commands

```
openclaw plugins list
openclaw plugins info <id>
openclaw plugins enable <id>
openclaw plugins disable <id>
openclaw plugins doctor
openclaw plugins update <id>
openclaw plugins update --all
```

Bundled plugins ship with OpenClaw but start disabled. Use `plugins enable` to activate them. All plugins must ship a `openclaw.plugin.json` file with an inline JSON Schema (`configSchema`, even if empty). Missing/invalid manifests or schemas prevent the plugin from loading and fail config validation.

### Install

```
openclaw plugins install <path-or-spec>
```

Security note: treat plugin installs like running code. Prefer pinned versions. Supported archives: `.zip`, `.tgz`, `.tar.gz`, `.tar`. Use `--link` to avoid copying a local directory (adds to `plugins.load.paths`):

```
openclaw plugins install -l ./my-plugin
```

### Update

```
openclaw plugins update <id>
openclaw plugins update --all
openclaw plugins update <id> --dry-run
```

Updates only apply to plugins installed from npm (tracked in `plugins.installs`).