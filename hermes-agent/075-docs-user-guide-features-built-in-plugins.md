---
title: Built-in Plugins | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/built-in-plugins
source: crawler
fetched_at: 2026-04-24T17:00:24.438097157-03:00
rendered_js: false
word_count: 570
summary: 'This document details the structure and operation of bundled plugins within Hermes, explaining how they are discovered across four potential locations, how they must be explicitly enabled, and provides an in-depth look at a specific built-in plugin: disk-cleanup.'
tags:
    - hermes-plugins
    - plugin-discovery
    - bundled-features
    - opt-in-system
    - disk-cleanup
    - agent-extensions
category: guide
---

Hermes ships a small set of plugins bundled with the repository. They live under `<repo>/plugins/<name>/` and load automatically alongside user-installed plugins in `~/.hermes/plugins/`. They use the same plugin surface as third-party plugins — hooks, tools, slash commands — just maintained in-tree.

See the [Plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins) page for the general plugin system, and [Build a Hermes Plugin](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin) to write your own.

## How discovery works[​](#how-discovery-works "Direct link to How discovery works")

The `PluginManager` scans four sources, in order:

1. **Bundled** — `<repo>/plugins/<name>/` (what this page documents)
2. **User** — `~/.hermes/plugins/<name>/`
3. **Project** — `./.hermes/plugins/<name>/` (requires `HERMES_ENABLE_PROJECT_PLUGINS=1`)
4. **Pip entry points** — `hermes_agent.plugins`

On name collision, later sources win — a user plugin named `disk-cleanup` would replace the bundled one.

`plugins/memory/` and `plugins/context_engine/` are deliberately excluded from bundled scanning. Those directories use their own discovery paths because memory providers and context engines are single-select providers configured through `hermes memory setup` / `context.engine` in config.

## Bundled plugins are opt-in[​](#bundled-plugins-are-opt-in "Direct link to Bundled plugins are opt-in")

Bundled plugins ship disabled. Discovery finds them (they appear in `hermes plugins list` and the interactive `hermes plugins` UI), but none load until you explicitly enable them:

```bash
hermes plugins enable disk-cleanup
```

Or via `~/.hermes/config.yaml`:

```yaml
plugins:
enabled:
- disk-cleanup
```

This is the same mechanism user-installed plugins use. Bundled plugins are never auto-enabled — not on fresh install, not for existing users upgrading to a newer Hermes. You always opt in explicitly.

To turn a bundled plugin off again:

```bash
hermes plugins disable disk-cleanup
# or: remove it from plugins.enabled in config.yaml
```

## Currently shipped[​](#currently-shipped "Direct link to Currently shipped")

### disk-cleanup[​](#disk-cleanup "Direct link to disk-cleanup")

Auto-tracks and removes ephemeral files created during sessions — test scripts, temp outputs, cron logs, stale chrome profiles — without requiring the agent to remember to call a tool.

**How it works:**

HookBehaviour`post_tool_call`When `write_file` / `terminal` / `patch` creates a file matching `test_*`, `tmp_*`, or `*.test.*` inside `HERMES_HOME` or `/tmp/hermes-*`, track it silently as `test` / `temp` / `cron-output`.`on_session_end`If any test files were auto-tracked during the turn, run the safe `quick` cleanup and log a one-line summary. Stays silent otherwise.

**Deletion rules:**

CategoryThresholdConfirmation`test`every session endNever`temp`&gt;7 days since trackedNever`cron-output`&gt;14 days since trackedNeverempty dirs under HERMES\_HOMEalwaysNever`research`&gt;30 days, beyond 10 newestAlways (deep only)`chrome-profile`&gt;14 days since trackedAlways (deep only)files &gt;500 MBnever autoAlways (deep only)

**Slash command** — `/disk-cleanup` available in both CLI and gateway sessions:

```text
/disk-cleanup status                     # breakdown + top-10 largest
/disk-cleanup dry-run                    # preview without deleting
/disk-cleanup quick                      # run safe cleanup now
/disk-cleanup deep                       # quick + list items needing confirmation
/disk-cleanup track <path> <category>    # manual tracking
/disk-cleanup forget <path>              # stop tracking (does not delete)
```

**State** — everything lives at `$HERMES_HOME/disk-cleanup/`:

FileContents`tracked.json`Tracked paths with category, size, and timestamp`tracked.json.bak`Atomic-write backup of the above`cleanup.log`Append-only audit trail of every track / skip / reject / delete

**Safety** — cleanup only ever touches paths under `HERMES_HOME` or `/tmp/hermes-*`. Windows mounts (`/mnt/c/...`) are rejected. Well-known top-level state dirs (`logs/`, `memories/`, `sessions/`, `cron/`, `cache/`, `skills/`, `plugins/`, `disk-cleanup/` itself) are never removed even when empty — a fresh install does not get gutted on first session end.

**Enabling:** `hermes plugins enable disk-cleanup` (or check the box in `hermes plugins`).

**Disabling again:** `hermes plugins disable disk-cleanup`.

## Adding a bundled plugin[​](#adding-a-bundled-plugin "Direct link to Adding a bundled plugin")

Bundled plugins are written exactly like any other Hermes plugin — see [Build a Hermes Plugin](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin). The only differences are:

- Directory lives at `<repo>/plugins/<name>/` instead of `~/.hermes/plugins/<name>/`
- Manifest source is reported as `bundled` in `hermes plugins list`
- User plugins with the same name override the bundled version

A plugin is a good candidate for bundling when:

- It has no optional dependencies (or they're already `pip install .[all]` deps)
- The behaviour benefits most users and is opt-out rather than opt-in
- The logic ties into lifecycle hooks that the agent would otherwise have to remember to invoke
- It complements a core capability without expanding the model-visible tool surface

Counter-examples — things that should stay as user-installable plugins, not bundled: third-party integrations with API keys, niche workflows, large dependency trees, anything that would meaningfully change agent behaviour by default.