---
title: How to Upgrade to v6
url: https://docs.bmad-method.org/how-to/upgrade-to-v6/
source: sitemap
fetched_at: 2026-04-08T11:31:23.27374748-03:00
rendered_js: false
word_count: 305
summary: This guide provides a step-by-step process for users migrating their development environment from BMad version 4 to version 6. It covers running the installer, handling legacy file structures, cleaning up IDE skills, and migrating planning artifacts and in-progress development work.
tags:
    - bmad-migration
    - v4-to-v6
    - software-upgrade
    - development-workflow
    - artifact-migration
category: guide
---

Use the BMad installer to upgrade from v4 to v6, which includes automatic detection of legacy installations and migration assistance.

- You have BMad v4 installed (`.bmad-method` folder)
- You want to migrate to the new v6 architecture
- You have existing planning artifacts to preserve

### 1. Run the Installer

[Section titled “1. Run the Installer”](#1-run-the-installer)

Follow the [Installer Instructions](https://docs.bmad-method.org/how-to/install-bmad/).

### 2. Handle Legacy Installation

[Section titled “2. Handle Legacy Installation”](#2-handle-legacy-installation)

When v4 is detected, you can:

- Allow the installer to back up and remove `.bmad-method`
- Exit and handle cleanup manually

If you named your bmad method folder something else - you will need to manually remove the folder yourself.

### 3. Clean Up IDE Skills

[Section titled “3. Clean Up IDE Skills”](#3-clean-up-ide-skills)

Manually remove legacy v4 IDE commands/skills - for example if you have Claude Code, look for any nested folders that start with bmad and remove them:

- `.claude/commands/`

The new v6 skills are installed to:

- `.claude/skills/`

### 4. Migrate Planning Artifacts

[Section titled “4. Migrate Planning Artifacts”](#4-migrate-planning-artifacts)

**If you have planning documents (Brief/PRD/UX/Architecture):**

Move them to `_bmad-output/planning-artifacts/` with descriptive names:

- Include `PRD` in filename for PRD documents
- Include `brief`, `architecture`, or `ux-design` accordingly
- Sharded documents can be in named subfolders

**If you’re mid-planning:** Consider restarting with v6 workflows. Use your existing documents as inputs—the new progressive discovery workflows with web search and IDE plan mode produce better results.

### 5. Migrate In-Progress Development

[Section titled “5. Migrate In-Progress Development”](#5-migrate-in-progress-development)

If you have stories created or implemented:

1. Complete the v6 installation
2. Place `epics.md` or `epics/epic*.md` in `_bmad-output/planning-artifacts/`
3. Run the Developer’s `bmad-sprint-planning` workflow
4. Tell the agent which epics/stories are already complete

**v6 unified structure:**

```text

your-project/
├── _bmad/               # Single installation folder
│   ├── _config/         # Your customizations
│   │   └── agents/      # Agent customization files
│   ├── core/            # Universal core framework
│   ├── bmm/             # BMad Method module
│   ├── bmb/             # BMad Builder
│   └── cis/             # Creative Intelligence Suite
└── _bmad-output/        # Output folder (was doc folder in v4)
```

v4 Modulev6 Status`.bmad-2d-phaser-game-dev`Integrated into BMGD Module`.bmad-2d-unity-game-dev`Integrated into BMGD Module`.bmad-godot-game-dev`Integrated into BMGD Module`.bmad-infrastructure-devops`Deprecated — new DevOps agent coming soon`.bmad-creative-writing`Not adapted — new v6 module coming soon

Conceptv4v6**Core**`_bmad-core` was actually BMad Method`_bmad/core/` is universal framework**Method**`_bmad-method``_bmad/bmm/`**Config**Modified files directly`config.yaml` per module**Documents**Sharded or unsharded required setupFully flexible, auto-scanned