---
title: What Are BMad Agents?
url: https://bmad-builder-docs.bmad-method.org/explanation/what-are-bmad-agents/
source: sitemap
fetched_at: 2026-04-08T11:33:07.210816537-03:00
rendered_js: false
word_count: 723
summary: This document explains BMad Agents, which are advanced conversational AI skills combining a persona, defined capabilities, and optional memory to create specialized partners. It details three agent types—Stateless, Memory, and Autonomous—and outlines the architecture of persistent state management using a 'sanctum'.
tags:
    - bmad-agents
    - ai-persona
    - agent-types
    - conversational-ai
    - persistent-memory
    - skill-design
category: reference
---

BMad Agents are AI skills that combine a **persona**, **capabilities**, and optionally **persistent memory** into a conversational partner. They range from focused, stateless experts to evolving companions that remember you across sessions.

## What Makes an Agent an Agent

[Section titled “What Makes an Agent an Agent”](#what-makes-an-agent-an-agent)

Agents are skill files with three additional traits that workflows lack.

TraitWhat It Means**Persona**A defined role and voice (architect, coach, game master, muse) that shapes how the agent communicates**Capabilities**Actions the agent can perform, either as internal prompt commands, scripts, or by calling external skills**Memory**Optional persistent storage where the agent keeps what it learns about you, your preferences, and past interactions

Together, they turn the interaction into a conversation with a specialist who knows your context.

## The Three Agent Types

[Section titled “The Three Agent Types”](#the-three-agent-types)

Agents exist on a spectrum. The builder detects which type fits through natural conversation.

TypeMemoryFirst BreathAutonomousBuild For**Stateless**NoNoNoIsolated sessions, focused experts (code formatter, diagram generator, meeting summarizer)**Memory**YesYesNoOngoing relationships where remembering adds value (code coach, writing partner, domain advisor)**Autonomous**YesYesYesProactive value creation between sessions (idea incubation, project monitoring, content curation)

Everything lives in a single SKILL.md with supporting references. No memory directory, no initialization ceremony. The agent brings a persona and capabilities but treats every session as independent. Pick this type when prior session context wouldn’t change the agent’s behavior.

A lean bootloader SKILL.md (~30 lines) points to a **sanctum**: a set of persistent files the agent reads on every launch to become itself again. The sanctum holds the agent’s identity, values, understanding of its owner, curated knowledge, and capability registry. On first launch, a **First Breath** conversation lets the agent discover who you are and calibrate itself to your needs.

Memory agents treat every session as a rebirth. They don’t fake continuity; they read their sanctum files and become themselves again. If they don’t remember something, they say so and check the files.

### Autonomous Agents

[Section titled “Autonomous Agents”](#autonomous-agents)

Everything a memory agent has, plus a PULSE file that defines what the agent does when no one’s watching. Autonomous agents can wake on a schedule (cron, background task) and perform maintenance, from curating memory to checking on projects to running domain-specific tasks. With a human present, they’re conversational. Headless, they work independently and exit.

## Capabilities: Internal, External, and Scripts

[Section titled “Capabilities: Internal, External, and Scripts”](#capabilities-internal-external-and-scripts)

TypeDescriptionExample**Internal commands**Prompt-driven actions defined inside the agent’s skill fileA Dream Agent’s “Dream Capture” command**External skills**Standalone skills or workflows the agent can invokeCalling the `create-prd` workflow via a PM agent**Scripts**Deterministic operations offloaded from the LLMValidation, data processing, file operations

You choose the mix when you design the agent. Internal commands keep everything self-contained. External skills let you compose agents from shared building blocks, and scripts handle operations where determinism matters more than judgment.

### Evolvable Capabilities

[Section titled “Evolvable Capabilities”](#evolvable-capabilities)

Memory agents can optionally support **evolvable capabilities**. When enabled, the agent gets a capability-authoring reference and a “Learned” section in its capability registry. Users can teach the agent new prompt-based, script-based, or multi-file capabilities that it absorbs into its repertoire over time.

Memory agents store their persistent state in a **sanctum** at `_bmad/memory/<agent-name>/`. The sanctum contains six core files that load on every session:

FilePurpose**PERSONA.md**Identity, communication style, traits, evolution log**CREED.md**Mission, values, standing orders, philosophy, boundaries**BOND.md**Owner understanding, preferences, things to remember/avoid**MEMORY.md**Curated long-term knowledge (kept under 200 lines)**CAPABILITIES.md**Built-in + learned capabilities registry**INDEX.md**Map of the sanctum structure (loaded first on every rebirth)

Sanctum architecture, First Breath, PULSE, and the two-tier memory system are covered in [**Agent Memory and Personalization**](https://bmad-builder-docs.bmad-method.org/explanation/agent-memory-and-personalization/).

## When to Build an Agent vs. a Workflow

[Section titled “When to Build an Agent vs. a Workflow”](#when-to-build-an-agent-vs-a-workflow)

Choose an Agent WhenChoose a Workflow WhenThe user will return to it repeatedlyThe process runs once and produces an outputRemembering context across sessions adds valueStateless execution is fineA strong persona improves the interactionPersonality is secondary to getting the job doneThe skill spans many loosely related capabilitiesAll steps serve a single, focused goal

If you’re unsure, start with a workflow. You can always wrap it inside an agent later.

The **BMad Agent Builder** (`bmad-agent-builder`) runs six phases of conversational discovery. The first phase detects which agent type fits your vision through natural questions, and the remaining phases adapt based on whether you’re creating a stateless expert, a memory-backed companion, or an autonomous agent.

See the [Builder Commands Reference](https://bmad-builder-docs.bmad-method.org/reference/builder-commands/) for details on the build process phases and capabilities.