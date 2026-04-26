---
title: Packages
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/packages.md
source: git
fetched_at: 2026-04-26T05:48:14.185491339-03:00
rendered_js: false
word_count: 1017
summary: This document provides a comprehensive guide on creating, installing, and managing Pi packages, which bundle extensions, skills, prompt templates, and themes for the Pi platform.
tags:
    - pi-packages
    - package-management
    - npm-integration
    - git-integration
    - configuration
    - extensions
    - skills
category: guide
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# Pi Packages

Pi packages bundle extensions, skills, prompt templates, and themes for sharing via npm or git. Declare resources in `package.json` under the `pi` key or use conventional directories.

## Install and Manage

> [!danger] Pi packages run with full system access. Extensions execute arbitrary code; skills can instruct the model to perform any action including running executables. Review source code before installing third-party packages.

```bash
pi install npm:@foo/bar@1.0.0
pi install git:github.com/user/repo@v1
pi install https://github.com/user/repo  # raw URLs work too
pi install /absolute/path/to/package
pi install ./relative/path/to/package

pi remove npm:@foo/bar
pi list                     # show installed packages from settings
pi update                   # update pi and all non-pinned packages
pi update --extensions      # update all non-pinned packages only
pi update --self            # update pi only
pi update npm:@foo/bar      # update one package
pi update --extension npm:@foo/bar
```

- Default target: global settings (`~/.pi/agent/settings.json`). Use `-l` for project settings (`.pi/settings.json`).
- Project settings can be shared with your team; pi installs missing packages automatically on startup.
- Try without installing with `--extension` / `-e` (temporary directory, current run only):

```bash
pi -e npm:@foo/bar
pi -e git:github.com/user/repo
```

## Package Sources

Three source types accepted in settings and `pi install`.

### npm

```
npm:@scope/pkg@1.2.3
npm:pkg
```

- Versioned specs are pinned — skipped by `pi update` / `pi update --extensions`.
- Global installs use `npm install -g`; project installs go under `.pi/npm/`.
- Set `npmCommand` in `settings.json` to pin npm operations to a wrapper (e.g., `mise`, `asdf`):

```json
{
  "npmCommand": ["mise", "exec", "node@20", "--", "npm"]
}
```

### git

```
git:github.com/user/repo@v1
git:git@github.com:user/repo@v1
https://github.com/user/repo@v1
ssh://git@github.com/user/repo@v1
```

| Aspect | Behavior |
|--------|----------|
| Without `git:` prefix | Only protocol URLs accepted (`https://`, `http://`, `ssh://`, `git://`) |
| With `git:` prefix | Shorthand accepted: `github.com/user/repo`, `git@github.com:user/repo` |
| HTTPS / SSH | Both supported; SSH uses configured keys (respects `~/.ssh/config`) |
| Refs (e.g. `@v1`) | Pin the package — skipped by updates |
| Clone location | `~/.pi/agent/git/<host>/<path>` (global) or `.pi/git/<host>/<path>` (project) |
| Post-clone | Runs `npm install` if `package.json` exists |

> [!tip] For non-interactive runs (CI): set `GIT_TERMINAL_PROMPT=0` to disable credential prompts and `GIT_SSH_COMMAND` (e.g., `ssh -o BatchMode=yes -o ConnectTimeout=5`) to fail fast.

**SSH examples:**

```bash
# git@host:path shorthand (requires git: prefix)
pi install git:git@github.com:user/repo

# ssh:// protocol format
pi install ssh://git@github.com/user/repo

# With version ref
pi install git:git@github.com:user/repo@v1.0.0
```

### Local Paths

```
/absolute/path/to/package
./relative/path/to/package
```

- Added to settings without copying. Relative paths resolve against the settings file they appear in.
- File path loads as a single extension. Directory path loads resources using package rules.

## Creating a Pi Package

Add a `pi` manifest to `package.json` (or use conventional directories). Include `pi-package` keyword for [gallery discoverability](https://pi.dev/packages).

```json
{
  "name": "my-package",
  "keywords": ["pi-package"],
  "pi": {
    "extensions": ["./extensions"],
    "skills": ["./skills"],
    "prompts": ["./prompts"],
    "themes": ["./themes"]
  }
}
```

Paths are relative to package root. Arrays support glob patterns and `!exclusions`.

### Gallery Metadata

Add `video` or `image` to show a preview on the [package gallery](https://pi.dev/packages):

```json
{
  "pi": {
    "extensions": ["./extensions"],
    "video": "https://example.com/demo.mp4",
    "image": "https://example.com/screenshot.png"
  }
}
```

| Field | Format | Behavior |
|-------|--------|----------|
| `video` | MP4 only | Autoplays on hover (desktop); click for fullscreen player |
| `image` | PNG, JPEG, GIF, WebP | Static preview |

If both are set, video takes precedence.

## Package Structure

### Convention Directories

Without a `pi` manifest, pi auto-discovers from:

| Directory | Loads |
|-----------|-------|
| `extensions/` | `.ts` and `.js` files |
| `skills/` | Recursively finds `SKILL.md` folders; top-level `.md` files as skills |
| `prompts/` | `.md` files |
| `themes/` | `.json` files |

## Dependencies

- **Third-party runtime deps:** list in `dependencies` in `package.json`. `npm install` runs automatically on install.
- **Pi core packages** (`@mariozechner/pi-ai`, `@mariozechner/pi-agent-core`, `@mariozechner/pi-coding-agent`, `@mariozechner/pi-tui`, `typebox`): list in `peerDependencies` with `"*"` range — do **not** bundle.
- **Other pi packages:** add to both `dependencies` and `bundledDependencies`, reference resources through `node_modules/` paths. Pi loads packages with separate module roots so installs don't collide.

```json
{
  "dependencies": {
    "shitty-extensions": "^1.0.1"
  },
  "bundledDependencies": ["shitty-extensions"],
  "pi": {
    "extensions": ["extensions", "node_modules/shitty-extensions/extensions"],
    "skills": ["skills", "node_modules/shitty-extensions/skills"]
  }
}
```

## Package Filtering

Filter what a package loads using the object form in settings:

```json
{
  "packages": [
    "npm:simple-pkg",
    {
      "source": "npm:my-package",
      "extensions": ["extensions/*.ts", "!extensions/legacy.ts"],
      "skills": [],
      "prompts": ["prompts/review.md"],
      "themes": ["+themes/legacy.json"]
    }
  ]
}
```

| Syntax | Effect |
|--------|--------|
| Omit key | Load all of that type |
| `[]` | Load none of that type |
| `!pattern` | Exclude matches |
| `+path` | Force-include exact path |
| `-path` | Force-exclude exact path |

Filters layer on top of the manifest — they narrow down what is already allowed.

## Enable and Disable Resources

Use `pi config` to enable or disable extensions, skills, prompt templates, and themes from installed packages and local directories. Works for both global (`~/.pi/agent`) and project (`.pi/`) scopes.

## Scope and Deduplication

Packages can appear in both global and project settings. If the same package appears in both, the project entry wins. Identity is determined by:

- **npm:** package name
- **git:** repository URL without ref
- **local:** resolved absolute path

#pi-packages #package-management #npm-integration #git-integration #extensions #skills
