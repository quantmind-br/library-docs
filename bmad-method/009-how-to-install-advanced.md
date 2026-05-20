---
title: How to Install Custom Modules and Upgrade
url: https://docs.bmad-method.org//llms-full.txt
source: llms
fetched_at: 2026-05-19T08:33:05.038451722-03:00
rendered_js: false
summary: Install community and custom modules, and upgrade from v4 to v6.
tags:
    - bmad-method
    - installation
    - modules
    - upgrading
category: guide
optimized: true
optimized_at: 2026-05-19T11:33:05Z
word_count: 656
---
# How to Install Custom Modules and Upgrade

Add modules from the BMad registry, third-party Git repositories, or local paths using the BMad installer.

> [!info] Prerequisites
> Requires [Node.js](https://nodejs.org) v20.12+ and `npx`. Custom and community modules can be selected during a fresh install or added to an existing installation.

## Community Modules

Community modules are curated in the [BMad plugins marketplace](https://github.com/bmad-code-org/bmad-plugins-marketplace), organized by category and pinned to approved commits.

1. Run the installer:
   ```bash
   npx bmad-method install
   ```
2. Browse the catalog — select **Yes** when asked `Would you like to browse community modules?`
3. Pick modules by category. The installer shows descriptions, versions, and trust tiers. Already-installed modules are pre-checked for update.
4. Continue with installation. After community modules, the installer proceeds to custom sources, then tool/IDE configuration.

## Custom Sources (Git URLs and Local Paths)

Install from any Git repository or local directory. The installer resolves the source, analyzes module structure, and installs alongside other modules.

### Interactive Installation

After the community module step, select **Yes** when asked `Would you like to install from a custom source (Git URL or local path)?`, then provide a source:

| Input Type | Example |
| --- | --- |
| HTTPS URL (any host) | `https://github.com/org/repo` |
| HTTP URL (any host) | `http://host/org/repo` |
| HTTPS URL with subdir | `https://github.com/org/repo/tree/main/my-module` |
| SSH URL | `git@github.com:org/repo.git` |
| Local path | `/Users/me/projects/my-module` |
| Local path with tilde | `~/projects/my-module` |

The installer clones (for URLs) or reads from disk (for local paths), then presents discovered modules for selection.

### Non-Interactive Installation

Use `--custom-source` to install from the command line:

```bash
npx bmad-method install \
  --directory . \
  --custom-source /path/to/my-module \
  --tools claude-code \
  --yes
```

When `--custom-source` is provided without `--modules`, only core and custom modules are installed. To include official modules, add `--modules`:

```bash
npx bmad-method install \
  --directory . \
  --modules bmm \
  --custom-source https://gitlab.com/myorg/my-module \
  --tools claude-code \
  --yes
```

Multiple sources can be comma-separated:

```bash
--custom-source /path/one,https://github.com/org/repo,/path/two
```

## Module Discovery

The installer finds installable modules in two modes:

| Mode | Trigger | Behavior |
| --- | --- | --- |
| Discovery | Source contains `.claude-plugin/marketplace.json` | Lists all plugins from the manifest; you pick which to install |
| Direct | No `marketplace.json` found | Scans for skills (subdirectories with `SKILL.md`), resolves as a single module |

Discovery mode is typical for published modules. Direct mode is convenient when pointing at a skills directory during local development.

> [!note] About `.claude-plugin/`
> The `.claude-plugin/marketplace.json` path is a cross-tool convention for plugin discoverability. It does not require Claude, use Claude APIs, or affect which AI tool you use. Any module with this file can be discovered by any installer that follows the convention.

## Local Development Workflow

Install a module under active development with [BMad Builder](https://github.com/bmad-code-org/bmad-builder) directly from your working directory:

```bash
npx bmad-method install \
  --directory ~/my-project \
  --custom-source ~/my-module-repo/skills \
  --tools claude-code \
  --yes
```

Local sources are referenced by path, not copied to cache. Reinstalling picks up the latest changes.

> [!warning] Source Removal
> If you delete the local source directory after installation, the installed module files in `_bmad/` are preserved. The module is skipped during updates until the source path is restored.

## What You Get

After installation, custom modules appear in `_bmad/` alongside official modules:

```text
your-project/
├── _bmad/
│   ├── core/
│   ├── bmm/
│   ├── my-module/
│   │   ├── my-skill/
│   │   │   └── SKILL.md
│   │   └── module-help.csv
│   └── _config/
│       └── manifest.yaml
└── ...
```

The manifest records each custom module's source (`repoUrl` for Git, `localPath` for local) so quick updates can locate it again.

## Updating Custom Modules

Custom modules participate in normal update flows:

- **Quick update** (`--action quick-update`): Refreshes all modules from original sources. Git-based modules are re-fetched; local modules are re-read from their source path.
- **Full update**: Re-runs module selection so you can add or remove custom modules.

## Creating Your Own Modules

Use [BMad Builder](https://github.com/bmad-code-org/bmad-builder) to create installable modules:

1. Run `bmad-module-builder` to scaffold module structure
2. Add skills, agents, and workflows with BMad Builder tools
3. Publish to a Git repository or share the folder collection
4. Others install with `--custom-source <your-repo-url>`

For discovery mode, include `.claude-plugin/marketplace.json` in your repository root. See the [BMad Builder documentation](https://github.com/bmad-code-org/bmad-builder) for the format.

> [!tip] Testing Locally First
> During development, install your module with a local path to iterate quickly before publishing.

#installation #modules #upgrading
