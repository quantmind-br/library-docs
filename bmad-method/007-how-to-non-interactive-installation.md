---
title: Non-Interactive Installation
url: https://docs.bmad-method.org/how-to/non-interactive-installation/
source: sitemap
fetched_at: 2026-04-08T11:31:15.224737307-03:00
rendered_js: false
word_count: 488
summary: This document provides a comprehensive reference on using command-line flags for non-interactive installation and configuration of BMad, detailing options for directories, modules, tools, and output path resolution. It also covers various installation modes like CI/CD setup and updating existing installations.
tags:
    - bmad-installation
    - cli-flags
    - command-line
    - automation
    - configuration-guide
    - ci-cd
category: guide
---

Use command-line flags to install BMad non-interactively. This is useful for:

- Automated deployments and CI/CD pipelines
- Scripted installations
- Batch installations across multiple projects
- Quick installations with known configurations

### Installation Options

[Section titled “Installation Options”](#installation-options)

FlagDescriptionExample`--directory <path>`Installation directory`--directory ~/projects/myapp``--modules <modules>`Comma-separated module IDs`--modules bmm,bmb``--tools <tools>`Comma-separated tool/IDE IDs (use `none` to skip)`--tools claude-code,cursor` or `--tools none``--action <type>`Action for existing installations: `install` (default), `update`, or `quick-update``--action quick-update`

### Core Configuration

[Section titled “Core Configuration”](#core-configuration)

FlagDescriptionDefault`--user-name <name>`Name for agents to useSystem username`--communication-language <lang>`Agent communication languageEnglish`--document-output-language <lang>`Document output languageEnglish`--output-folder <path>`Output folder path (see resolution rules below)`_bmad-output`

#### Output Folder Path Resolution

[Section titled “Output Folder Path Resolution”](#output-folder-path-resolution)

The value passed to `--output-folder` (or entered interactively) is resolved according to these rules:

Input typeExampleResolved asRelative path (default)`_bmad-output``<project-root>/_bmad-output`Relative path with traversal`../../shared-outputs`Normalized absolute path — e.g. `/Users/me/shared-outputs`Absolute path`/Users/me/shared-outputs`Used as-is — project root is **not** prepended

The resolved path is what agents and workflows use at runtime when writing output files. Using an absolute path or a traversal-based relative path lets you direct all generated artifacts to a directory outside your project tree — useful for shared or monorepo setups.

FlagDescription`-y, --yes`Accept all defaults and skip prompts`-d, --debug`Enable debug output for manifest generation

Available module IDs for the `--modules` flag:

- `bmm` — BMad Method Master
- `bmb` — BMad Builder

Check the [BMad registry](https://github.com/bmad-code-org) for available external modules.

Available tool IDs for the `--tools` flag:

**Preferred:** `claude-code`, `cursor`

Run `npx bmad-method install` interactively once to see the full current list of supported tools, or check the [platform codes configuration](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml).

## Installation Modes

[Section titled “Installation Modes”](#installation-modes)

ModeDescriptionExampleFully non-interactiveProvide all flags to skip all prompts`npx bmad-method install --directory . --modules bmm --tools claude-code --yes`Semi-interactiveProvide some flags; BMad prompts for the rest`npx bmad-method install --directory . --modules bmm`Defaults onlyAccept all defaults with `-y``npx bmad-method install --yes`Without toolsSkip tool/IDE configuration`npx bmad-method install --modules bmm --tools none`

### CI/CD Pipeline Installation

[Section titled “CI/CD Pipeline Installation”](#cicd-pipeline-installation)

```bash

#!/bin/bash
npxbmad-methodinstall\
--directory"${GITHUB_WORKSPACE}"\
--modulesbmm\
--toolsclaude-code\
--user-name"CI Bot"\
--communication-languageEnglish\
--document-output-languageEnglish\
--output-folder_bmad-output\
--yes
```

### Update Existing Installation

[Section titled “Update Existing Installation”](#update-existing-installation)

```bash

npxbmad-methodinstall\
--directory~/projects/myapp\
--actionupdate\
--modulesbmm,bmb,custom-module
```

### Quick Update (Preserve Settings)

[Section titled “Quick Update (Preserve Settings)”](#quick-update-preserve-settings)

```bash

npxbmad-methodinstall\
--directory~/projects/myapp\
--actionquick-update
```

- A fully configured `_bmad/` directory in your project
- Agents and workflows configured for your selected modules and tools
- A `_bmad-output/` folder for generated artifacts

## Validation and Error Handling

[Section titled “Validation and Error Handling”](#validation-and-error-handling)

BMad validates all provided flags:

- **Directory** — Must be a valid path with write permissions
- **Modules** — Warns about invalid module IDs (but won’t fail)
- **Tools** — Warns about invalid tool IDs (but won’t fail)
- **Action** — Must be one of: `install`, `update`, `quick-update`

Invalid values will either:

1. Show an error and exit (for critical options like directory)
2. Show a warning and skip (for optional items)
3. Fall back to interactive prompts (for missing required values)

### Installation fails with “Invalid directory”

[Section titled “Installation fails with “Invalid directory””](#installation-fails-with-invalid-directory)

- The directory path must exist (or its parent must exist)
- You need write permissions
- The path must be absolute or correctly relative to the current directory

<!--THE END-->

- Verify the module ID is correct
- External modules must be available in the registry