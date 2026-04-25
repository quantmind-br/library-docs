---
title: What Are Skills?
url: https://bmad-builder-docs.bmad-method.org/explanation/what-are-skills/
source: sitemap
fetched_at: 2026-04-08T11:33:11.448318492-03:00
rendered_js: false
word_count: 151
summary: This document explains that Skills serve as the universal packaging format for all outputs from the BMad Builder, adhering to the Agent Skills open standard and detailing the components required within a skill folder.
tags:
    - bmad-builder
    - skill-format
    - agent-skills-standard
    - workflow-structure
    - component-guide
category: reference
---

Skills are the universal packaging format for everything the BMad Builder produces. Agents are skills. Workflows are skills. Simple utilities are skills. The format follows the [Agent Skills open standard](https://agentskills.io/home).

The BMad Builder produces skills that conform to the open standard and adds a few BMad-specific conventions on top.

ComponentPurpose**SKILL.md**The skill’s instructions: persona, capabilities, and behavior rules**resources/**Reference data, templates, and guidance documents**scripts/**Deterministic validation and analysis scripts**templates/**Building blocks for generated output

Not every skill needs all of these. A simple utility might be a single `SKILL.md`. A complex workflow or agent may use the full structure.

## Ready to Use on Build

[Section titled “Ready to Use on Build”](#ready-to-use-on-build)

The builders output a complete skill folder. Place it in your tool’s skills directory (`.claude/skills`, `.codex/skills`, `.agent/skills`, or wherever your tool looks) and it’s immediately usable.

See [What Are Agents](https://bmad-builder-docs.bmad-method.org/explanation/what-are-bmad-agents/) and [What Are Workflows](https://bmad-builder-docs.bmad-method.org/explanation/what-are-workflows/) for how agents and workflows each use this foundation differently.