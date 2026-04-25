---
title: What Are BMad Modules?
url: https://bmad-builder-docs.bmad-method.org/explanation/what-are-modules/
source: sitemap
fetched_at: 2026-04-08T11:33:09.215409701-03:00
rendered_js: false
word_count: 1040
summary: This document details the structure, components, and best practices for building BMad modules, covering topics from distribution formats (plugins) to architectural choices like agent types and memory management.
tags:
    - module-structure
    - bmad-api
    - plugin-development
    - agent-design
    - workflow-patterns
    - skill-registration
category: guide
---

BMad modules package agents and workflows into installable units with shared configuration and help system registration. A module can be a full suite of related skills or a single standalone skill that wants to be discoverable and configurable.

## Distribution: Plugins and Marketplaces

[Section titled “Distribution: Plugins and Marketplaces”](#distribution-plugins-and-marketplaces)

At the distribution level, a BMad module is a **plugin**: a package of skills with a `.claude-plugin/` manifest. How you structure it depends on what you’re shipping:

StructureWhen to UseManifest**Single plugin**One module (standalone or multi-skill)`.claude-plugin/marketplace.json` with one plugin entry**Marketplace**A repo that ships multiple modules`.claude-plugin/marketplace.json` with multiple plugin entries

The `.claude-plugin/` convention originates from Claude Code, but the format works across multiple skills platforms. The BMad installer will support installing custom modules directly from GitHub in an upcoming release. Until then, copy the created skill folder into your tool’s skills directory (`.claude/skills/`, `.agents/skills/`, etc.). You can also use Anthropic’s plugin system if targeting only Claude Code.

The Module Builder generates the appropriate `marketplace.json` during the Create Module (CM) step - but you will want to verify it lists the proper relative paths to the skills you want to deliver with your module.

This also means you can include remote URL skills in your own module to combine them.

## What a Module Contains

[Section titled “What a Module Contains”](#what-a-module-contains)

ComponentMulti-Skill ModuleStandalone Module**Skills**Two or more agents/workflowsA single agent or workflow**Registration**Dedicated `{code}-setup` skillBuilt into the skill itself (`assets/module-setup.md`)**module.yaml**In the setup skill’s `assets/`In the skill’s own `assets/`**module-help.csv**In the setup skill’s `assets/`In the skill’s own `assets/`**Distribution**Plugin with multiple skill foldersPlugin with single skill folder + `marketplace.json`

For multi-skill modules, the setup skill is the glue; it registers all capabilities in one step. For standalone modules, the skill handles its own registration on first run or when the user passes `setup`/`configure`.

## Agent vs. Workflow vs. Both

[Section titled “Agent vs. Workflow vs. Both”](#agent-vs-workflow-vs-both)

The first architecture decision when planning a module is whether to use a single agent, multiple workflows, or a combination.

ArchitectureWhen It FitsTrade-offs**Single agent with capabilities**All capabilities serve the same user journey and benefit from shared contextSimpler to maintain, better memory continuity, seamless UX. Can feel monolithic if capabilities are unrelated**Multiple workflows**Capabilities serve different user journeys or require different toolsEach workflow is focused and composable. Users switch between skills explicitly**Hybrid**Some capabilities need persistent persona/memory while others are proceduralBest of both worlds but more skills to build and maintain

## Multi-Agent Modules and Memory

[Section titled “Multi-Agent Modules and Memory”](#multi-agent-modules-and-memory)

Modules with multiple agents introduce a memory architecture decision. BMad agents exist on a spectrum from stateless (no memory) through memory agents (personal sanctum) to autonomous agents (sanctum + PULSE). In a multi-agent module, you choose both the agent type for each skill and whether agents should share memory across the module.

PatternWhen It Fits**Personal memory only**Agents have distinct domains with minimal overlap**Personal + shared module memory**Agents have their own context but also learn shared things about the user or project**Shared memory only**All agents serve the same domain; consider whether a single agent is the better design**Mixed types**Some agents need memory (coaches, companions) while others are stateless (formatters, validators)

**Example:** A social creative module with a podcast expert, a viral video expert, and a blog expert. Each memory agent maintains its own sanctum with what it has done with the user (episode topics, video formats, blog themes). But they all also contribute to a module-level memory folder that captures the user’s communication style, favorite catchphrases, content preferences, and brand voice.

Each agent should still be self-contained with its own capabilities, even if this means duplicating some common functionality. A podcast expert that can independently handle a full session without needing the blog expert is better than one that depends on shared state to function.

See [**What Are BMad Agents**](https://bmad-builder-docs.bmad-method.org/explanation/what-are-bmad-agents/) for the three agent types, and [**Agent Memory and Personalization**](https://bmad-builder-docs.bmad-method.org/explanation/agent-memory-and-personalization/) for details on how the sanctum architecture works.

## Standalone vs. Expansion Modules

[Section titled “Standalone vs. Expansion Modules”](#standalone-vs-expansion-modules)

TypeDescription**Standalone**Provides complete, independent value. Does not depend on another module being installed**Expansion**Extends an existing module with new capabilities. Should still provide utility even if the parent module is not installed

Expansion modules can reference the parent module’s capabilities in their help CSV ordering (before/after fields). This lets a new capability slot into the parent module’s natural workflow sequence.

Even expansion modules should be designed to work independently. The parent module being absent should degrade gracefully, not break the expansion.

## Configuration and Registration

[Section titled “Configuration and Registration”](#configuration-and-registration)

Modules register with a project through three files in `{project-root}/_bmad/`:

FilePurpose`config.yaml`Shared settings committed to git, module section keyed by module code`config.user.yaml`Personal settings (gitignored), user name, language preferences`module-help.csv`Capability registry, one row per action users can discover

Registration is what makes a module visible to `bmad-help`. Without it, the help system cannot discover, recommend, or track completion of the module’s capabilities.

Not every module needs configuration. If skills work with sensible defaults, registration can focus purely on help entries. See [**Module Configuration**](https://bmad-builder-docs.bmad-method.org/explanation/module-configuration/) for details on when configuration adds value and how the help CSV columns work.

## External Dependencies

[Section titled “External Dependencies”](#external-dependencies)

Some modules depend on tools outside the BMad ecosystem.

Dependency TypeExamples**CLI tools**`docker`, `terraform`, `ffmpeg`**MCP servers**Custom or third-party Model Context Protocol servers**Web services**APIs that require credentials or configuration

When a module has external dependencies, the setup skill should check for their presence and guide users through installation or configuration.

## UI and Visualization

[Section titled “UI and Visualization”](#ui-and-visualization)

Modules can include user interfaces: dashboards, progress views, interactive visualizations, or even full web applications. A UI skill might show shared progress across the module’s capabilities, provide a visual map of how skills relate, or offer an interactive way to navigate the module’s features.

Not every module needs a UI. But for complex modules with many capabilities, a visual layer makes the experience much more accessible.

## Building a Module

[Section titled “Building a Module”](#building-a-module)

The Module Builder (`bmad-module-builder`) provides three capabilities for the module lifecycle:

1. **Ideate Module (IM)**: Brainstorm and plan through creative facilitation
2. **Create Module (CM)**: Package skills as an installable module. Detects whether you have a folder of skills (generates a setup skill) or a single skill (embeds self-registration directly)
3. **Validate Module (VM)**: Verify structural integrity and entry quality for both multi-skill and standalone modules

See the [**Builder Commands Reference**](https://bmad-builder-docs.bmad-method.org/reference/builder-commands/) for detailed documentation on each capability.