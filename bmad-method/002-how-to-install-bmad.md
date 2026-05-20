---
title: How to Install BMad
url: https://docs.bmad-method.org//how-to/install-bmad/
source: llms
fetched_at: 2026-05-19T08:33:03.5681753-03:00
rendered_js: false
word_count: 1271
summary: This document details the usage of the bmad-method command-line tool for installing, upgrading, and managing project modules, including headless configurations for CI environments.
tags:
    - bmad
    - cli
    - package-management
    - ci-cd
    - configuration
    - automation
category: guide
optimized: true
optimized_at: 2026-05-19T11:33:03Z
---
Use `npx bmad-method install` to set up BMad. One command handles first installs, upgrades, channel switching, and scripted CI runs.

## First-time install (the fast path)
BLUF: The interactive flow asks five questions, then installs the latest stable release of every selected module.

1. Installation directory (defaults to current working directory)
2. Which modules to install (checkboxes for core, bmm, bmb, cis, gds, tea)
3. **"Ready to install (all stable)?"** — Yes accepts the latest released tag for every external module
4. Which AI tools/IDEs to integrate with (claude-code, cursor, and others)
5. Per-module config (name, language, output folder)

## Picking a specific version
BLUF: Two independent axes control what ends up on disk: external module channels and installer binary version.

### Axis 1: external module channels

| Channel | What gets installed | Who picks this |
|---------|---------------------|----------------|
| `stable` (default) | Highest released semver tag. Prereleases excluded. | Most users |
| `next` | Main branch HEAD at install time | Contributors, early adopters |
| `pinned` | A specific tag you name | Enterprise installs, CI reproducibility |

Channels are per-module. Mix freely — run bmb on `next` while leaving cis on `stable`.

### Axis 2: installer binary version

| Command | What you get |
|---------|--------------|
| `npx bmad-method install` (`@latest`) | Latest stable installer release |
| `npx bmad-method@next install` | Latest prerelease installer, auto-published on every push to main |

The installer binary determines your **core** and **bmm** versions. Those two modules ship bundled inside the installer package.

### Why core and bmm don't have their own channel
They're stapled to the installer binary:
- `npx bmad-method install` → latest stable core and bmm
- `npx bmad-method@next install` → prerelease core and bmm
- `node /path/to/local-checkout/tools/installer/bmad-cli.js install` → whatever your local checkout has

`--pin bmm=v6.3.0` and `--next=bmm` are silently ineffective against bundled modules. The installer warns when you try. A future release extracts bmm from the installer package; once that ships, bmm gets a proper channel selector.

## Updating an existing install
BLUF: Re-running `npx bmad-method install` in a directory with `_bmad/` gives a menu.

| Choice | What it does |
|--------|--------------|
| **Quick Update** | Re-runs with existing settings. Refreshes files, applies patches and minor stable upgrades, refuses major upgrades. Fast, non-interactive. |
| **Modify Install** | Full interactive flow. Add or remove modules, reconfigure settings, optionally review and switch channels. |

When Modify detects a newer stable tag for a module on `stable`:

| Upgrade type | Example | Default |
|--------------|---------|---------|
| Patch | v1.7.0 → v1.7.1 | Y |
| Minor | v1.7.0 → v1.8.0 | Y |
| Major | v1.7.0 → v2.0.0 | **N** |

Major defaults to N because breaking changes frequently surface as "instability". The prompt includes a GitHub release-notes URL.

Under `--yes`, patch and minor upgrades apply automatically. Majors stay frozen — pass `--pin <code>=<new-tag>` to accept non-interactively.

### Switching a module's channel
**Interactively:** choose Modify → answer **Yes** to "Review channel assignments?" → each external module offers Keep, Switch to stable, Switch to next, or Pin to a tag.

**Via flags:** see Headless CI installs below.

## Headless CI installs
BLUF: Use flags for non-interactive installs in CI, Docker, or enterprise rollouts.

| Flag | Purpose |
|------|---------|
| `--yes`, `-y` | Skip all prompts; accept flag values + defaults |
| `--directory <path>` | Install into this directory (default: current working dir) |
| `--modules <a,b,c>` | Exact module set. Core is auto-added. Not a delta — list everything you want kept. |
| `--tools <a,b>` | IDE/tool selection. Required for fresh `--yes` installs. Run `--list-tools` for valid IDs. |
| `--list-tools` | Print all supported tool/IDE IDs and exit. |
| `--action <type>` | `install`, `update`, or `quick-update`. Defaults based on existing install state. |
| `--custom-source <urls>` | Install custom modules from Git URLs or local paths |
| `--channel <stable\|next>` | Apply to all externals (aliased as `--all-stable` / `--all-next`) |
| `--all-stable` | Alias for `--channel=stable` |
| `--all-next` | Alias for `--channel=next` |
| `--next=<code>` | Put one module on next. Repeatable. |
| `--pin <code>=<tag>` | Pin one module to a specific tag. Repeatable. |
| `--set <module>.<key>=<value>` | Set any module config option non-interactively. Repeatable. |
| `--list-options [module]` | Print every `--set` key for built-in and locally-cached official modules, then exit. |
| `--user-name`, `--communication-language`, `--document-output-language`, `--output-folder` | Legacy shortcuts equivalent to `--set core.<key>=<value>` |

Precedence when flags overlap: `--pin` beats `--next=` beats `--channel` / `--all-*` beats registry default (`stable`).

**Default install — latest stable:**
```bash

npxbmad-methodinstall--yes--modulesbmm,bmb,cis--toolsclaude-code
```

**Enterprise pin — reproducible byte-for-byte:**
```bash

npxbmad-methodinstall--yes\
--modulesbmm,bmb,cis\
--pinbmb=v1.7.0--pincis=v0.2.0\
--toolsclaude-code
```

**Bleeding edge — externals on main HEAD:**
```bash

npxbmad-methodinstall--yes--modulesbmm,bmb--all-next--toolsclaude-code
```

**Add a module to existing install** (keep everything else):
```bash

npxbmad-methodinstall--yes--actionupdate\
--modulesbmm,bmb,gds
```

`--tools` is omitted — `--action update` reuses tools from the first install.

**Mix channels — bmb on next, gds on stable:**
```bash

npxbmad-methodinstall--yes--actionupdate\
--modulesbmm,bmb,cis,gds\
--next=bmb
```

### Module config overrides
BLUF: `--set <module>.<key>=<value>` sets any module config non-interactively, applied as a post-install patch.

**Example — install bmm with explicit project knowledge and skill level:**
```bash

npxbmad-methodinstall--yes\
--modulesbmm\
--toolsclaude-code\
--setbmm.project_knowledge=research\
--setbmm.user_skill_level=expert
```

**Discover available keys:**
```bash

npxbmad-methodinstall--list-optionsbmm
```

`--list-options` (no argument) lists every key the installer can find locally — built-in modules (`core`, `bmm`) plus cached official modules. The cache is per-machine and can be cleared. Community and custom modules aren't enumerated; read the module's `module.yaml` directly.

**How it works:**

- **Routing.** The patch step looks for `[modules.<module>] <key>` (or `[core] <key>`) in `config.user.toml` first; if found, it updates that file. Otherwise it writes to team-scope `config.toml`. User-scope keys (e.g. `core.user_name`, `bmm.user_skill_level`) end up in `config.user.toml`; team-scope keys in `config.toml`.
- **Verbatim values.** The value is written exactly as provided — no `result:` template rendering. To get the rendered form (e.g. `{project-root}/research`), pass it explicitly.
- **Carry-forward, declared keys.** Values for keys declared in `module.yaml` survive subsequent installs because they're also written to `_bmad/<module>/config.yaml`, which the installer reads as the prompt default on the next run.
- **Carry-forward, undeclared keys.** A value for a key not declared in the module's schema lands in `config.toml` for the current install but won't be re-emitted on the next install (the manifest writer drops unknown keys). Re-pass `--set` if you need it sticky, or edit `_bmad/config.toml` directly.
- **No validation.** `single-select` values aren't checked against allowed choices, and unknown keys aren't rejected.
- **Modules not in `--modules`.** Setting a value for an uninstalled module prints a warning and drops the value.

Legacy core shortcuts (`--user-name`, `--output-folder`, etc.) still work, but `--set core.user_name=...` is equivalent.

## What got installed
BLUF: `_bmad/_config/manifest.yaml` records exactly what's on disk after any install.

```yaml

modules:
- name: bmb
  version: v1.7.0          # the tag, or "main" for next
  channel: stable          # stable | next | pinned
  sha: 86033fc9aeae2ca6d52c7cdb675c1f4bf17fc1c1
  source: external
  repoUrl: https://github.com/bmad-code-org/bmad-builder
```

The `sha` field is written for git-backed modules (external, community, and URL-based custom). Bundled modules (core, bmm) and local-path custom modules don't have one.

For cross-machine reproducibility, don't rely on rerunning the same `--modules` command. Stable-channel installs resolve to the highest released tag **at install time**. Convert recorded tags from `manifest.yaml` into explicit `--pin` flags:

```bash

npxbmad-methodinstall--yes--modulesbmb,cis\
--pinbmb=v1.7.0--pincis=v0.4.2--toolsclaude-code
```

### Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| "Could not resolve stable tag" or "API rate limit exceeded" | GitHub's 60/hr anonymous limit | Set `GITHUB_TOKEN` and retry. If already set, it may be expired or rate-limited — try a different token or wait for the hourly reset. |
| "Tag 'vX.Y.Z' not found" | Tag doesn't exist in the module's repo | Check the repo's releases page on GitHub for valid tags. |
| A pinned install keeps upgrading | Shouldn't happen | Verify `_bmad/_config/manifest.yaml` shows `channel: pinned` plus fixed `version` and `sha`. Quick-update only touches `stable` channel. |
| `--pin bmm=X` didn't do anything | bmm is bundled | Use `npx bmad-method@next install` for prerelease core/bmm, or run the installer locally from a bmad-bmm checkout. |

#bmad #cli #package-management #ci-cd #configuration
