---
title: Build Your First Module
url: https://bmad-builder-docs.bmad-method.org/tutorials/build-your-first-module/
source: sitemap
fetched_at: 2026-04-08T11:33:23.756783606-03:00
rendered_js: false
word_count: 677
summary: This tutorial comprehensively guides users through the process of developing a BMad module, covering everything from initial concept ideation and skill building to final scaffolding, validation, and distribution.
tags:
    - bmad-module
    - skill-building
    - developer-guide
    - module-lifecycle
    - agent-workflows
category: tutorial
---

This tutorial takes you from an initial idea to a working, installable BMad module with help registration and configuration.

## What You’ll Learn

[Section titled “What You’ll Learn”](#what-youll-learn)

- Planning a module with the Ideate Module (IM) capability
- Choosing between a single agent and multiple workflows
- Building individual skills with the Agent and Workflow Builders
- Scaffolding a setup skill with Create Module (CM)
- Validating your module with Validate Module (VM)

## Understanding Modules

[Section titled “Understanding Modules”](#understanding-modules)

A BMad module bundles skills so they’re discoverable and configurable. The Module Builder offers two approaches depending on what you’re building:

ApproachWhen to UseWhat Gets Generated**Setup skill**Folder of 2+ skillsDedicated `{code}-setup` skill with config and help assets**Self-registration**Single standalone skillRegistration embedded in the skill’s own `assets/` folder

Both produce the same registration artifacts: `module.yaml` (identity and config variables) and `module-help.csv` (capability entries), which register with `bmad-help`.

See [**What Are Modules**](https://bmad-builder-docs.bmad-method.org/explanation/what-are-modules/) for the architecture behind these choices.

## Step 1: Plan Your Module

[Section titled “Step 1: Plan Your Module”](#step-1-plan-your-module)

Start with the Ideate Module capability.

The ideation session covers:

TopicWhat You’ll Decide**Vision**Problem space, target users, core value**Architecture**Single agent, multiple workflows, or hybrid**Agent types**For each agent: stateless, memory, or autonomous (see [What Are Agents](https://bmad-builder-docs.bmad-method.org/explanation/what-are-bmad-agents/))**Memory**For multi-agent modules: personal memory, shared module memory, or both**Module type**Standalone or expansion of another module**Skills**Each planned skill’s purpose, capabilities, and relationships**Configuration**Custom install questions and variables**Dependencies**External CLI tools, MCP servers, web services

The output is a **plan document** saved to your reports folder. You’ll reference it when building each skill.

## Step 2: Build Your Skills

[Section titled “Step 2: Build Your Skills”](#step-2-build-your-skills)

Now build each skill individually.

Skill TypeBuilderMenu CodeAgentAgent BuilderBAWorkflow or utilityWorkflow BuilderBW

Share the plan document as context when building each skill so the builder knows how it fits into the module. For agents, the builder will detect the right type (stateless, memory, or autonomous) through conversational discovery and adapt the build process accordingly.

## Step 3: Scaffold the Module

[Section titled “Step 3: Scaffold the Module”](#step-3-scaffold-the-module)

Run Create Module (CM) to package your finished skills.

### Multi-skill modules

[Section titled “Multi-skill modules”](#multi-skill-modules)

The builder generates a dedicated setup skill:

```plaintext

your-skills-folder/
├── {code}-setup/                # Generated setup skill
│   ├── SKILL.md                 # Setup instructions
│   ├── scripts/                 # Config merge and cleanup scripts
│   │   ├── merge-config.py
│   │   ├── merge-help-csv.py
│   │   └── cleanup-legacy.py
│   └── assets/
│       ├── module.yaml          # Module identity and config vars
│       └── module-help.csv      # Capability entries
├── your-agent-skill/
├── your-workflow-skill/
└── ...
```

### Standalone modules

[Section titled “Standalone modules”](#standalone-modules)

The builder embeds registration into the skill itself:

```plaintext

your-skill/
├── SKILL.md                     # Updated with registration check
├── assets/
│   ├── module-setup.md          # Self-registration reference
│   ├── module.yaml              # Module identity and config vars
│   └── module-help.csv          # Capability entries
├── scripts/
│   ├── merge-config.py          # Config merge script
│   └── merge-help-csv.py        # Help CSV merge script
└── ...
```

A `.claude-plugin/marketplace.json` is also generated at the parent level for distribution.

Run Validate Module (VM) to check for structural and quality issues.

Check TypeWhat It Catches**Structural**Missing files, orphan entries, duplicate menu codes, broken references**Quality**Inaccurate descriptions, missing capabilities, poor entry quality

Fix any findings and re-validate until clean.

## What You’ve Built

[Section titled “What You’ve Built”](#what-youve-built)

Your module is ready to distribute. Multi-skill modules install through the setup skill; standalone modules self-register on first run. Either way, capabilities appear in `bmad-help` and configuration is persisted automatically.

CapabilityMenu CodeWhen to UseIdeate ModuleIMPlanning a new module from scratchBuild an AgentBACreating an agent skillBuild a WorkflowBWCreating a workflow or utility skillCreate ModuleCMPackaging skills into an installable moduleValidate ModuleVMChecking completeness and accuracy

### Do I need to ideate before creating?

[Section titled “Do I need to ideate before creating?”](#do-i-need-to-ideate-before-creating)

No. If you already know what your module should contain, skip straight to Create Module (CM). Ideation helps when you’re still shaping the concept.

### Can I add skills to a module later?

[Section titled “Can I add skills to a module later?”](#can-i-add-skills-to-a-module-later)

Yes. Build the new skill and re-run Create Module (CM) on the folder. The anti-zombie pattern ensures the existing setup skill is replaced cleanly.

### What if my module only has one skill?

[Section titled “What if my module only has one skill?”](#what-if-my-module-only-has-one-skill)

The Module Builder handles this automatically. Give it a single skill and it recommends the **standalone self-registering** approach, where registration embeds directly in the skill and triggers on first run or when the user passes `setup`/`configure`.

### Can my module extend another module?

[Section titled “Can my module extend another module?”](#can-my-module-extend-another-module)

Yes. Tell the builder during ideation or creation that your module is an expansion. Your help CSV entries can reference the parent module’s capabilities in their before/after ordering fields.

- [**What Are Modules**](https://bmad-builder-docs.bmad-method.org/explanation/what-are-modules/): Concepts and architecture
- [**Module Configuration**](https://bmad-builder-docs.bmad-method.org/explanation/module-configuration/): Setup skill internals and config patterns
- [**Builder Commands Reference**](https://bmad-builder-docs.bmad-method.org/reference/builder-commands/): All builder capabilities
- [**Discord**](https://discord.gg/gk8jAdXWmj): Community support