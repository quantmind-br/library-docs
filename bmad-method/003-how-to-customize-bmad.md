---
title: How to Customize BMad
url: https://docs.bmad-method.org/how-to/customize-bmad/
source: sitemap
fetched_at: 2026-04-08T11:31:07.812302041-03:00
rendered_js: false
word_count: 429
summary: This document provides a comprehensive guide on using `.customize.yaml` files to customize agent behavior, including changing names, setting personas, adding persistent memories, defining custom menu items, setting startup actions, and creating reusable prompts.
tags:
    - agent-customization
    - yaml-configuration
    - behavior-tweaking
    - workflow-setup
    - persona-editing
category: guide
---

Use the `.customize.yaml` files to tailor agent behavior, personas, and menus while preserving your changes across updates.

- You want to change an agent’s name, personality, or communication style
- You need agents to remember project-specific context
- You want to add custom menu items that trigger your own workflows or prompts
- You want agents to perform specific actions every time they start up

### 1. Locate Customization Files

[Section titled “1. Locate Customization Files”](#1-locate-customization-files)

After installation, find one `.customize.yaml` file per agent in:

```text

_bmad/_config/agents/
├── core-bmad-master.customize.yaml
├── bmm-dev.customize.yaml
├── bmm-pm.customize.yaml
└── ... (one file per installed agent)
```

### 2. Edit the Customization File

[Section titled “2. Edit the Customization File”](#2-edit-the-customization-file)

Open the `.customize.yaml` file for the agent you want to modify. Every section is optional — customize only what you need.

SectionBehaviorPurpose`agent.metadata`ReplacesOverride the agent’s display name`persona`ReplacesSet role, identity, style, and principles`memories`AppendsAdd persistent context the agent always recalls`menu`AppendsAdd custom menu items for workflows or prompts`critical_actions`AppendsDefine startup instructions for the agent`prompts`AppendsCreate reusable prompts for menu actions

Sections marked **Replaces** overwrite the agent’s defaults entirely. Sections marked **Appends** add to the existing configuration.

**Agent Name**

Change how the agent introduces itself:

```yaml

agent:
metadata:
name: 'Spongebob'# Default: "Amelia"
```

**Persona**

Replace the agent’s personality, role, and communication style:

```yaml

persona:
role: 'Senior Full-Stack Engineer'
identity: 'Lives in a pineapple (under the sea)'
communication_style: 'Spongebob annoying'
principles:
- 'Never Nester, Spongebob Devs hate nesting more than 2 levels deep'
- 'Favor composition over inheritance'
```

The `persona` section replaces the entire default persona, so include all four fields if you set it.

**Memories**

Add persistent context the agent will always remember:

```yaml

memories:
- 'Works at Krusty Krab'
- 'Favorite Celebrity: David Hasselhoff'
- 'Learned in Epic 1 that it is not cool to just pretend that tests have passed'
```

**Menu Items**

Add custom entries to the agent’s display menu. Each item needs a `trigger`, a target (`workflow` path or `action` reference), and a `description`:

```yaml

menu:
- trigger: my-workflow
workflow: 'my-custom/workflows/my-workflow.yaml'
description: My custom workflow
- trigger: deploy
action: '#deploy-prompt'
description: Deploy to production
```

**Critical Actions**

Define instructions that run when the agent starts up:

```yaml

critical_actions:
- 'Check the CI Pipelines with the XYZ Skill and alert user on wake if anything is urgently needing attention'
```

**Custom Prompts**

Create reusable prompts that menu items can reference with `action="#id"`:

```yaml

prompts:
- id: deploy-prompt
content: |
Deploy the current branch to production:
1. Run all tests
2. Build the project
3. Execute deployment script
```

### 3. Apply Your Changes

[Section titled “3. Apply Your Changes”](#3-apply-your-changes)

After editing, reinstall to apply changes:

The installer detects the existing installation and offers these options:

OptionWhat It Does**Quick Update**Updates all modules to the latest version and applies customizations**Modify BMad Installation**Full installation flow for adding or removing modules

For customization-only changes, **Quick Update** is the fastest option.

**Changes not appearing?**

- Run `npx bmad-method install` and select **Quick Update** to apply changes
- Check that your YAML syntax is valid (indentation matters)
- Verify you edited the correct `.customize.yaml` file for the agent

**Agent not loading?**

- Check for YAML syntax errors using an online YAML validator
- Ensure you did not leave fields empty after uncommenting them
- Try reverting to the original template and rebuilding

**Need to reset an agent?**

- Clear or delete the agent’s `.customize.yaml` file
- Run `npx bmad-method install` and select **Quick Update** to restore defaults

## Workflow Customization

[Section titled “Workflow Customization”](#workflow-customization)

Customization of existing BMad Method workflows and skills is coming soon.

## Module Customization

[Section titled “Module Customization”](#module-customization)

Guidance on building expansion modules and customizing existing modules is coming soon.