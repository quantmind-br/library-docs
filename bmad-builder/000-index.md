---
description: Auto-generated documentation index for BMad Builder
generated: 2026-04-08T14:40:00Z
source: https://bmad-builder-docs.bmad-method.org/sitemap-0.xml
total_docs: 18
categories: 7
---

# BMad Builder Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://bmad-builder-docs.bmad-method.org/sitemap-0.xml |
| **Generated** | 2026-04-08T14:40:00Z |
| **Total Documents** | 18 |
| **Categories** | Introduction & Overview, What Are... Concepts, Advanced Concepts & Patterns, Module Configuration, Reference, How-To Guides, Tutorials |

---

## Document Index

### 1. Introduction & Overview (001-001)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-index.md` | Welcome | This document introduces BMad Builder, a system designed for creating advanced AI modules with features like persistent memory and composability. It guides users through the process of registering, building, and deploying custom skills or agents within the broader BMad ecosystem. | ai-companion, module-development, workflow-automation, agent-building, skill-creation, bmad-ecosystem |

### 2. What Are... Concepts (002-005)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 002 | `002-explanation-what-are-skills.md` | What Are Skills? | This document explains that Skills serve as the universal packaging format for all outputs from the BMad Builder, adhering to the Agent Skills open standard and detailing the components required within a skill folder. | bmad-builder, skill-format, agent-skills-standard, workflow-structure, component-guide |
| 003 | `003-explanation-what-are-workflows.md` | What Are BMad Workflows? | This document explains what BMad Workflows are—structured processes designed to achieve a specific, cohesive outcome by guiding users through sequential steps. It details workflow types, interaction modes like progressive disclosure and headless operation, and advises when to use a workflow versus an agent. | bmad-workflows, process-design, workflow-automation, agent-comparison, progressive-disclosure, headless-mode |
| 004 | `004-explanation-what-are-modules.md` | What Are BMad Modules? | This document details the structure, components, and best practices for building BMad modules, covering topics from distribution formats (plugins) to architectural choices like agent types and memory management. | module-structure, bmad-api, plugin-development, agent-design, workflow-patterns, skill-registration |
| 005 | `005-explanation-what-are-bmad-agents.md` | What Are BMad Agents? | This document explains BMad Agents, which are advanced conversational AI skills combining a persona, defined capabilities, and optional memory to create specialized partners. It details three agent types—Stateless, Memory, and Autonomous—and outlines the architecture of persistent state management using a 'sanctum'. | bmad-agents, ai-persona, agent-types, conversational-ai, persistent-memory, skill-design |

### 3. Advanced Concepts & Patterns (006-011)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 006 | `006-explanation-agent-memory-and-personalization.md` | Agent Memory and Personalization | This document details the architecture and operational lifecycle of memory agents, explaining how persistent identity is maintained across stateless sessions using a structured 'sanctum' folder. It covers initialization ('First Breath'), ongoing maintenance through session logging and knowledge curation into MEMORY.md, autonomous operation via PULSE, and methods for evolving agent capabilities. | memory-agents, agent-architecture, session-persistence, knowledge-curation, sanctum-structure, autonomous-operation |
| 007 | `007-explanation-progressive-disclosure.md` | Progressive Disclosure in Skills | This document explains progressive disclosure techniques for designing agent skills by introducing four layers of context loading (Frontmatter/Body, On-Demand Resources, Dynamic Routing, and Step Files). It also details the 'document-as-cache' pattern for maintaining state in long workflows. | agent-skill-design, progressive-disclosure, llm-context-management, workflow-structuring, layering-system |
| 008 | `008-explanation-scripts-in-skills.md` | Scripts in Skills | This document outlines the best practice of using external scripts for deterministic tasks within AI skills, allowing Large Language Models (LLMs) to focus on judgment and creativity. It details when to use scripting over LLM prompting, emphasizes Python's benefits over Bash, and describes modern dependency management via PEP 723. | scripting-vs-llm, determinism, python-best-practices, dependency-management, ai-skill-design |
| 009 | `009-explanation-subagent-patterns.md` | Subagent Orchestration Patterns | This document details advanced patterns for orchestrating LLM work using isolated 'subagents' that communicate via a shared filesystem blackboard, emphasizing techniques to prevent the parent context from bloating and maintain efficiency. | llm-orchestration, subagent-patterns, filesystem-blackboard, context-management, ai-architecture |
| 010 | `010-explanation-skill-authoring-best-practices.md` | Skill Authoring Best Practices | This document provides detailed best practices for writing robust and adaptable AI agent instructions, covering core principles like informed autonomy, structuring workflows with soft gates, managing context flow, and designing multi-faceted outputs. | ai-agent-design, prompt-engineering, workflow-guidelines, llm-best-practices, context-management, system-architecture |
| 011 | `011-explanation-module-configuration.md` | Module Configuration and the Setup Skill | This document explains the methods for module registration within a system, detailing when to use configuration skills versus self-registration, and outlining the structure and purpose of required files like `module-help.csv` and `assets/module.yaml`. It details how registration allows users to discover and manage module capabilities through a help system. | module-registration, configuration-skills, help-system, metadata-management, setup-skill, workflow-automation |

### 4. Reference (012-015)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 012 | `012-explanation.md` | BMad Builder (BMB) | This document serves as a comprehensive reference guide explaining the core building blocks—including skills, agents, workflows, and modules—required to create advanced AI systems using the BMad Builder. It covers various architectural patterns and best practices for developing robust, configurable AI workflows. | ai-agents, workflow-design, bmad-builder, skills, module-development, architectural-patterns |
| 013 | `013-reference.md` | Reference | This document serves as a technical reference providing documentation for the BMad Builder's configuration settings, schemas, builder skills, commands, and workflow patterns. | technical-reference, builder-skills, workflow-patterns, schema, bmad-builder |
| 014 | `014-reference-builder-commands.md` | Builder Commands Reference | This document serves as a comprehensive reference for the three BMad Builder skills—Agent, Workflow, and Module Builders—detailing their core capabilities, multi-phase development processes, and specific requirements at each stage of building sophisticated AI agents and workflows. | bmad-builder, agent-builder, workflow-builder, ai-development, skill-design, headless-mode |
| 015 | `015-reference-workflow-patterns.md` | Workflow & Skill Patterns | This document serves as a taxonomy and reference guide detailing how the BMad Builder classifies skills into three types: Simple Utility, Simple Workflow, and Complex Workflow. It outlines the structural patterns, defining signals, and applicable use cases for each skill type. | skill-taxonomy, bmad-builder, workflow-types, skill-structure, headless-mode, simple-utility |

### 5. How-To Guides (016-016)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 016 | `016-how-to-distribute-your-module.md` | Distribute Your Module | This guide details the comprehensive process of packaging and publishing a BMad module to GitHub, covering manifest configuration, repository structuring for single or multiple modules, verification steps, and finally, how users will install the published content. | bmad-module, plugin-manifest, github-publishing, repository-structure, skill-development, marketplace-submission |

### 6. Tutorials (017-018)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 017 | `017-tutorials.md` | Tutorials | This section provides hands-on tutorials designed to help users learn how to build modules using the BMad Builder. | tutorial, bmad-builder, module-building, hands-on |
| 018 | `018-tutorials-build-your-first-module.md` | Build Your First Module | This tutorial comprehensively guides users through the process of developing a BMad module, covering everything from initial concept ideation and skill building to final scaffolding, validation, and distribution. | bmad-module, skill-building, developer-guide, module-lifecycle, agent-workflows |

---

## Quick Reference

### By Topic
| Topic | File Range |
|-------|------------|
| **Skills** | 002, 008, 010 |
| **Agents** | 005, 006 |
| **Modules** | 004, 011, 016, 018 |
| **Workflows** | 003, 015 |
| **Reference** | 012, 013, 014, 015 |
| **Memory & Personalization** | 006 |
| **Best Practices** | 008, 010 |

### By Concept
| Concept | Files |
|---------|-------|
| **Agent Skills Standard** | 002 |
| **Progressive Disclosure** | 007, 003 |
| **Subagent Orchestration** | 009 |
| **Module Configuration** | 011 |
| **Skill Taxonomies** | 015 |
| **GitHub Publishing** | 016 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001** for introduction and overview
- Read files **002-005** to understand the core building blocks: Skills, Workflows, Modules, and Agents

### Level 2: Core Understanding
- Learn memory architecture from file **006**
- Master progressive disclosure techniques from file **007**
- Understand scripting best practices from file **008**

### Level 3: Practical Application
- Study subagent orchestration from file **009**
- Apply skill authoring best practices from file **010**
- Configure modules properly using file **011**

### Level 4: Reference & Tools
- Consult file **012-013** for technical reference
- Use files **014-015** as command and pattern lookup

### Level 5: Hands-On Learning
- Follow the tutorial in file **017** to learn BMad Builder through examples
- Complete file **018** to build your first module from start to finish
- Publish using file **016** to share your module with others

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression adapted to the documentation structure.*
