---
title: Module Configuration and the Setup Skill
url: https://bmad-builder-docs.bmad-method.org/explanation/module-configuration/
source: sitemap
fetched_at: 2026-04-08T11:33:02.021780238-03:00
rendered_js: false
word_count: 1368
summary: This document explains the methods for module registration within a system, detailing when to use configuration skills versus self-registration, and outlining the structure and purpose of required files like `module-help.csv` and `assets/module.yaml`. It details how registration allows users to discover and manage module capabilities through a help system.
tags:
    - module-registration
    - configuration-skills
    - help-system
    - metadata-management
    - setup-skill
    - workflow-automation
category: guide
---

BMad modules register their capabilities with the help system and optionally collect user preferences. Multi-skill modules use a dedicated **setup skill** for this. Single-skill standalone modules handle registration themselves on first run.

When you create your own module, you can either add a configuration skill or embed the feature in every skill following the standalone pattern. For modules with more than 1-2 skills, a setup skill is the better choice.

## When You Need Configuration

[Section titled “When You Need Configuration”](#when-you-need-configuration)

Most modules should not need configuration at all. Before adding configurable values, consider whether a simpler alternative exists.

ApproachWhen to Use**Sensible defaults**The variable has one clearly correct answer for most users that could be overridden or updated by the specific skill that needs it the first time it runs**Agent memory**Your module follows the agent pattern and the agent can learn preferences through conversation**Configuration**The value genuinely varies across projects and cannot be inferred at runtime

## What Module Registration Does

[Section titled “What Module Registration Does”](#what-module-registration-does)

Module registration serves two purposes:

PurposeWhat Happens**Configuration**Collects user preferences and writes them to shared config files**Help registration**Adds the module’s capabilities to the project-wide help system so users can discover them

### Why Register with the Help System?

[Section titled “Why Register with the Help System?”](#why-register-with-the-help-system)

The `bmad-help` skill reads `module-help.csv` to understand what capabilities are available, detect which ones have been completed (by checking output locations for artifacts), and recommend next steps based on the dependency graph. Without registration, `bmad-help` cannot discover or recommend your module’s capabilities beyond what it knows basically from skill headers. The help system provides richer detail: arguments, relationships to other skills, inputs and outputs, and any other authored metadata. If a skill has multiple capabilities, each one gets its own help entry.

### Two Registration Paths

[Section titled “Two Registration Paths”](#two-registration-paths)

PathWhen to UseHow It Works**Setup skill**Multi-skill modules (2+ skills)A dedicated `{code}-setup` skill handles registration for all skills**Self-registration**Single-skill standalone modulesThe skill itself registers on first run or when user passes `setup`/`configure`

The Module Builder detects which path to use based on what you give it: a folder of skills triggers the setup skill approach, a single skill triggers the standalone approach.

## Configuration Files

[Section titled “Configuration Files”](#configuration-files)

Setup skills write to three files in `{project-root}/_bmad/`:

FileScopeContains`config.yaml`Shared, committed to gitCore settings at root level, plus a section per module with metadata and module-specific values`config.user.yaml`Personal, gitignoredUser-only settings like `user_name` and `communication_language``module-help.csv`Shared, committed to gitOne row per capability the module exposes

Core settings (like `output_folder` and `document_output_language`) live at the root of `config.yaml` and are shared across all modules. Each module also gets its own section keyed by its module code.

## The module.yaml File

[Section titled “The module.yaml File”](#the-moduleyaml-file)

Each module declares its identity and configurable variables in an `assets/module.yaml` file. For multi-skill modules, this lives inside the setup skill. For standalone modules, it lives in the skill’s own `assets/` folder. This file drives both the prompts shown to the user and the values written to config.

```yaml

code: mymod
name: 'My Module'
description: 'What this module does'
module_version: 1.0.0
default_selected: false
module_greeting: >
Welcome message shown after setup completes.
my_output_folder:
prompt: 'Where should output be saved?'
default: '{project-root}/_bmad-output/my-module'
result: '{project-root}/{value}'
```

Variables with a `prompt` field are presented to the user during setup. The `default` value is used when the user accepts defaults. Adding `user_setting: true` to a variable routes it to `config.user.yaml` instead of the shared config.

## Help Registration Without Configuration

[Section titled “Help Registration Without Configuration”](#help-registration-without-configuration)

You may not need any configurable values but still want to register your module with the help system. Registration is still worthwhile when:

- The skill description in SKILL.md frontmatter cannot fully convey what the module offers while staying concise
- You want to express capability sequencing, phase constraints, or other metadata the CSV supports
- An agent has many internal capabilities that users should be able to discover
- Your module has more than about three distinct things it can do

For simpler cases, these alternatives are often sufficient:

AlternativeWhat It Provides**SKILL.md overview section**A concise summary at the top of the skill body; the `--help` system scans this section to present user-facing help, so keep it succinct**Script header comments**Describe purpose, usage, and flags at the top of each script

If these cover your discoverability needs, you can skip the setup skill entirely.

## The module-help.csv File

[Section titled “The module-help.csv File”](#the-module-helpcsv-file)

The CSV registers the module’s capabilities with the help system. Each row describes one capability that users can discover and invoke. The file has 13 columns:

```csv

module,skill,display-name,menu-code,description,action,args,phase,after,before,required,output-location,outputs
```

ColumnPurpose**module**Module display name. Groups entries in help output**skill**Skill folder name (e.g., `bmad-agent-builder`); must match the actual directory name**display-name**User-facing label shown in help menus (e.g., “Build an Agent”)**menu-code**1-3 letter shortcode displayed as `[CODE]` in help, unique across the module, intuitive mnemonic**description**What this capability does. Concise, action-oriented, specific enough for `bmad-help` to route correctly**action**Action name within the skill. Distinguishes capabilities when one skill exposes multiple (e.g., `build-process`, `quality-optimizer`)**args**Arguments the capability accepts (e.g., `[-H] [path]`), shown in help output**phase**When the capability is available: `anytime` or a workflow phase like `1-analysis`, `2-planning`**after**Capabilities that should complete before this one: format `skill-name:action`, comma-separated for multiple**before**Capabilities that should run after this one, same format as `after`**required**`true` if this is a blocking gate for phase progression, `false` otherwise**output-location**Config variable name (e.g., `output_folder`, `bmad_builder_reports`); `bmad-help` resolves from config to scan for completion artifacts**outputs**File patterns `bmad-help` looks for in the output location to detect completion (e.g., “quality report”, “agent skill”)

### How bmad-help Uses These Entries

[Section titled “How bmad-help Uses These Entries”](#how-bmad-help-uses-these-entries)

The `after`/`before` columns create a **dependency graph** that `bmad-help` walks to recommend next steps. `required=true` entries are blocking gates; `bmad-help` will not suggest later-phase capabilities until required gates pass. The `output-location` and `outputs` columns enable **completion detection**: `bmad-help` scans those paths for matching artifacts to determine what’s been done.

```csv

module,skill,display-name,menu-code,description,action,args,phase,after,before,required,output-location,outputs
BMad Builder,bmad-agent-builder,Build an Agent,BA,"Create, edit, convert, or fix an agent skill.",build-process,"[-H] [description | path]",anytime,,bmad-agent-builder:quality-optimizer,false,output_folder,agent skill
```

During registration, these rows are merged into the project-wide `_bmad/module-help.csv`, replacing any existing rows for this module (anti-zombie pattern).

## Anti-Zombie Pattern

[Section titled “Anti-Zombie Pattern”](#anti-zombie-pattern)

Both merge scripts use an anti-zombie pattern: before writing new values for a module, they remove all existing entries for that module’s code. This prevents stale configuration or help entries from persisting across module updates. Running setup a second time is always safe.

## Legacy Directory Cleanup

[Section titled “Legacy Directory Cleanup”](#legacy-directory-cleanup)

After config data is migrated and individual files are cleaned up by the merge scripts, a separate cleanup step removes the installer’s per-module directory trees from `_bmad/`. These directories contain skill files that are already installed in the tool’s skills directory. They are redundant once the config has been consolidated.

Before removing any directory, the cleanup script verifies that every skill it contains exists at the installed location. Directories without skills (like `_config/`) are removed directly. The script is idempotent; running setup again after cleanup is safe.

Configuration is for **basic, project-level settings**: output folders, language preferences, feature toggles. Keep the number of configurable values small.

PatternConfiguration Role**Agent pattern**Prefer agent memory for per-user preferences. Use config only for values that must be shared across the project**Workflow pattern**Use config for output locations and behavior switches that vary across projects**Skill-only pattern**Use config sparingly. If the skill works with sensible defaults, skip config entirely

Extensive workflow customization (step overrides, conditional branching, template selection) is a separate concern and will be covered in a dedicated document.

## Creating a Module with the Module Builder

[Section titled “Creating a Module with the Module Builder”](#creating-a-module-with-the-module-builder)

The **Module Builder** (`bmad-module-builder`) automates module creation. It offers three capabilities:

CapabilityMenu CodeWhat It Does**Ideate Module**IMBrainstorm and plan a module through facilitative discovery; produces a plan document**Create Module**CMPackage skills as an installable BMad module (setup skill or standalone self-registering)**Validate Module**VMCheck that a module’s structure is complete, accurate, and properly registered

**For a folder of skills (multi-skill module):**

1. Run **Ideate Module (IM)** to brainstorm and plan
2. Build each skill using the **Agent Builder (BA)** or **Workflow Builder (BW)**
3. Run **Create Module (CM)**. It generates a dedicated `-setup` skill with `module.yaml`, `module-help.csv`, and merge scripts
4. Run **Validate Module (VM)** to verify everything is wired correctly

**For a single skill (standalone module):**

1. Build the skill using the **Agent Builder (BA)** or **Workflow Builder (BW)**
2. Run **Create Module (CM)** with the skill path. It embeds self-registration directly into the skill (`assets/module-setup.md`, `assets/module.yaml`, `assets/module-help.csv`) and generates a `marketplace.json` for distribution
3. Run **Validate Module (VM)** to verify

The Module Builder auto-detects single vs. multi-skill input and recommends the appropriate approach.

See [**What Are Modules**](https://bmad-builder-docs.bmad-method.org/explanation/what-are-modules/) for concepts and architecture decisions, or the [**Builder Commands Reference**](https://bmad-builder-docs.bmad-method.org/reference/builder-commands/) for detailed capability documentation.