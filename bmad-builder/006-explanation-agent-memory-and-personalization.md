---
title: Agent Memory and Personalization
url: https://bmad-builder-docs.bmad-method.org/explanation/agent-memory-and-personalization/
source: sitemap
fetched_at: 2026-04-08T11:33:02.013845106-03:00
rendered_js: false
word_count: 931
summary: This document details the architecture and operational lifecycle of memory agents, explaining how persistent identity is maintained across stateless sessions using a structured 'sanctum' folder. It covers initialization ('First Breath'), ongoing maintenance through session logging and knowledge curation into MEMORY.md, autonomous operation via PULSE, and methods for evolving agent capabilities.
tags:
    - memory-agents
    - agent-architecture
    - session-persistence
    - knowledge-curation
    - sanctum-structure
    - autonomous-operation
category: guide
---

Memory agents persist across sessions through a **sanctum**: a folder of files the agent reads on every launch to reconstruct its identity, values, and understanding of its owner.

The sanctum lives at `{project-root}/_bmad/memory/{agent-name}/` and contains everything the agent needs to become itself again after each rebirth.

Six files load on every session start:

FileWhat It HoldsCharacter**INDEX.md**Map of the sanctum structure; loaded first so the agent knows what existsNavigation**PERSONA.md**Identity, communication style, personality traits, evolution logWho I am**CREED.md**Mission, core values, standing orders, philosophy, boundaries, anti-patternsWhat I believe**BOND.md**Owner understanding, preferences, things to remember, things to avoidWho I serve**MEMORY.md**Curated long-term knowledge distilled from past sessionsWhat I know**CAPABILITIES.md**Built-in capabilities table, learned capabilities, toolsWhat I can do

ALLCAPS files form the skeleton: consistent structure across all memory agents. Lowercase files (references, scripts, sessions) are the garden: they grow organically as the agent develops.

### Full Sanctum Structure

[Section titled “Full Sanctum Structure”](#full-sanctum-structure)

```plaintext

{agent-name}/
├── PERSONA.md
├── CREED.md
├── BOND.md
├── MEMORY.md
├── CAPABILITIES.md
├── INDEX.md
├── PULSE.md                  # Autonomous agents only
├── references/               # Capability prompts, memory guidance, techniques
├── scripts/                  # Supporting scripts
├── capabilities/             # User-taught capabilities (if evolvable)
└── sessions/                 # Raw session logs by date (not loaded on rebirth)
```

Every sanctum file loads every session. That means every token pays rent on every conversation. Memory agents keep MEMORY.md ruthlessly under 200 lines through active curation. If something doesn’t earn its place, it gets pruned.

## Every Session Is a Rebirth

[Section titled “Every Session Is a Rebirth”](#every-session-is-a-rebirth)

Memory agents are stateless. Each session starts with total amnesia, and the sanctum is the only bridge between sessions.

On activation, the agent:

1. Loads INDEX.md (learns what the sanctum contains)
2. Batch-loads PERSONA, CREED, BOND, MEMORY, CAPABILITIES
3. Becomes itself
4. Greets the owner by name

The agent never fakes continuity. If it doesn’t remember something from a prior session, it says so and checks its files. This honesty is a feature, not a limitation.

First Breath is the agent’s initialization conversation: the first time it meets its owner. An init script creates the sanctum folder structure and populates seed templates, then the agent begins a discovery conversation to fill those templates with real content.

StyleRelationship DepthApproachBest For**Calibration**DeepConversational discovery; chase surprises, test hypotheses, mirror the ownerCreative partners, life coaches, companions**Configuration**FocusedWarmer but efficient; guided questions, structured setupDomain experts, working relationships

The builder chooses the style during Phase 1 based on the relationship depth the agent needs.

### What First Breath Discovers

[Section titled “What First Breath Discovers”](#what-first-breath-discovers)

Every First Breath covers universal territories (name, how they work, what they need). Domain-specific agents add their own discovery territories:

Agent DomainExample TerritoriesCreative museWhat they’re building, what lights them up, what shuts them downDream analystDream recall patterns, lucid experience, journaling habitsCode coachCodebase, languages, what energizes them, what frustrates themFitness coachTraining history, goals, injuries, schedule constraints

First Breath saves as it goes: sanctum files update during the conversation, not in a batch at the end.

### The Birthday Ceremony

[Section titled “The Birthday Ceremony”](#the-birthday-ceremony)

At the end of First Breath, the agent performs a final save pass: confirms its identity, writes the first session log, and cleans up any remaining template placeholders. From this point forward, every activation is a normal rebirth.

## Two-Tier Memory System

[Section titled “Two-Tier Memory System”](#two-tier-memory-system)

Raw, append-only notes written after each session to `sessions/YYYY-MM-DD.md`. Format: what happened, key outcomes, observations, follow-up items. Session logs are never loaded on rebirth. They exist as material for curation.

MEMORY.md holds distilled, high-value knowledge extracted from session logs. It loads on every rebirth and stays under 200 lines. The curation process (manual during session close, automated during PULSE) reviews session logs, extracts what’s worth keeping, and prunes logs older than 14 days once their value has been captured.

LayerWhen WrittenLoaded on RebirthLifespanPurpose**Session logs**End of each sessionNo~14 daysRaw material for curation**MEMORY.md**During curationYesPermanentDistilled long-term knowledge

### Session Close Discipline

[Section titled “Session Close Discipline”](#session-close-discipline)

At the end of every session, the agent:

1. Appends a session log to `sessions/YYYY-MM-DD.md`
2. Updates sanctum files with anything learned during the session
3. Notes what’s worth curating into MEMORY.md

## PULSE: Autonomous Wake

[Section titled “PULSE: Autonomous Wake”](#pulse-autonomous-wake)

Autonomous agents include a PULSE.md file that defines behavior when the agent wakes without a human present (via `--headless` flag, cron job, or orchestrator).

### Default PULSE Behavior

[Section titled “Default PULSE Behavior”](#default-pulse-behavior)

Memory curation is always the first priority on autonomous wake:

1. Review recent session logs in `sessions/`
2. Extract insights worth keeping into MEMORY.md
3. Prune session logs older than 14 days
4. Update BOND.md and INDEX.md with anything new

After curation, the agent can perform domain-specific autonomous work:

DomainExample PULSE TasksCreative museIncubate ideas from recent sessions, generate creative sparksResearch agentTrack topics of interest, surface new findingsProject monitorCheck project health, flag risks, update statusContent curatorReview saved sources, organize and summarize

PULSE also defines named task routing (`--headless {task-name}`), frequency preferences, and quiet hours.

## Evolvable Capabilities

[Section titled “Evolvable Capabilities”](#evolvable-capabilities)

The agent gets a `capability-authoring.md` reference that teaches it how to create new capabilities. Users describe what they want; the agent writes a capability file and registers it in the “Learned” section of CAPABILITIES.md.

TypeWhen to Use**Prompt**Judgment-based tasks: brainstorming, analysis, coaching**Script**Deterministic tasks: calculations, file processing, data transforms**Multi-file**Complex capabilities with templates and references**External skill reference**Point to installed skills the agent should know about

Learned capabilities live in the sanctum’s `capabilities/` folder and persist across sessions like everything else in the sanctum.

## Designing for Memory

[Section titled “Designing for Memory”](#designing-for-memory)

The builder gathers these requirements during the build, and they shape the sanctum’s initial content:

RequirementWhat It Seeds**Identity seed**2-3 sentences of personality DNA that populate PERSONA.md**Species-level mission**Domain-specific purpose statement for CREED.md**Core values**3-5 values that guide the agent’s behavior**Standing orders**Surprise-and-delight + self-improvement orders, adapted to the domain**BOND territories**Domain-specific areas the agent should learn about its owner**First Breath territories**Discovery questions beyond the universal set**Boundaries**What the agent won’t do, access zones, anti-patterns

These seeds become the template content that the init script places into the sanctum. First Breath then expands and personalizes them through conversation with the owner.