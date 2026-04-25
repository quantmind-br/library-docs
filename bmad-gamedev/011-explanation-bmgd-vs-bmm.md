---
title: BMGD vs BMM
url: https://game-dev-studio-docs.bmad-method.org/explanation/bmgd-vs-bmm/
source: sitemap
fetched_at: 2026-04-08T11:34:00.878282804-03:00
rendered_js: false
word_count: 351
summary: This document compares BMMad Method (BMM) with BMGD (BMad Game Development), detailing the specific additions and differences for game development, covering topics like agent roles, planning documents (GDD vs. PRD), narrative support, specialized testing procedures, and production workflows.
tags:
    - bmgd-vs-bmm
    - game-development
    - methodology-comparison
    - gdd
    - agent-roles
    - testing-workflows
category: concept
---

BMGD (BMad Game Development) extends BMM (BMad Method) with game-specific capabilities. This page explains the key differences.

AspectBMMBMGD**Focus**General softwareGame development**Agents**PM, Architect, Dev, SM, TEA, Solo DevGame Designer, Game Dev, Game Architect, Game SM, Game QA, Game Solo Dev**Planning**PRD, Tech SpecGame Brief, GDD**Types**N/A24 game type templates**Narrative**N/AFull narrative workflow**Testing**Web-focusedEngine-specific (Unity, Unreal, Godot)**Production**BMM workflowsBMM workflows with game overrides

## Agent Differences

[Section titled “Agent Differences”](#agent-differences)

- PM (Product Manager)
- Architect
- DEV (Developer)
- SM (Scrum Master)
- TEA (Test Architect)
- Quick Flow Solo Dev

<!--THE END-->

- Game Designer
- Game Developer
- Game Architect
- Game Scrum Master
- Game QA
- Game Solo Dev

BMGD agents understand game-specific concepts like:

- Game mechanics and balance
- Player psychology
- Engine-specific patterns
- Playtesting and QA

## Planning Documents

[Section titled “Planning Documents”](#planning-documents)

- **Product Brief** → **PRD** → **Architecture**
- Focus: Software requirements, user stories, system design

<!--THE END-->

- **Game Brief** → **GDD** → **Architecture**
- Focus: Game vision, mechanics, narrative, player experience

The GDD (Game Design Document) includes:

- Core gameplay loop
- Mechanics and systems
- Progression and balance
- Art and audio direction
- Genre-specific sections

## Game Type Templates

[Section titled “Game Type Templates”](#game-type-templates)

BMGD includes 24 game type templates that auto-configure GDD sections:

- Action, Adventure, Puzzle
- RPG, Strategy, Simulation
- Sports, Racing, Fighting
- Horror, Platformer, Shooter
- And more…

Each template provides:

- Genre-specific GDD sections
- Relevant mechanics patterns
- Testing considerations
- Common pitfalls to avoid

## Narrative Support

[Section titled “Narrative Support”](#narrative-support)

BMGD includes full narrative workflow for story-driven games:

- **Narrative Design** workflow
- Story structure templates
- Character development
- World-building guidelines
- Dialogue systems

BMM has no equivalent for narrative design.

## Testing Differences

[Section titled “Testing Differences”](#testing-differences)

### BMM Testing (TEA)

[Section titled “BMM Testing (TEA)”](#bmm-testing-tea)

- Web-focused (Playwright, Cypress)
- API testing
- E2E for web applications

### BMGD Testing (Game QA)

[Section titled “BMGD Testing (Game QA)”](#bmgd-testing-game-qa)

- Engine-specific frameworks (Unity, Unreal, Godot)
- Gameplay testing
- Performance profiling
- Playtest planning
- Balance validation

## Production Workflow

[Section titled “Production Workflow”](#production-workflow)

BMGD production workflows **inherit from BMM** and add game-specific:

- Checklists
- Templates
- Quality gates
- Engine-specific considerations

This means you get all of BMM’s implementation structure plus game-specific enhancements.

- Building web applications
- Creating APIs and services
- Developing mobile apps (non-game)
- Any general software project

<!--THE END-->

- Building video games
- Creating interactive experiences
- Game prototyping
- Game jams