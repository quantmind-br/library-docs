---
title: BMGD Workflows Reference
url: https://game-dev-studio-docs.bmad-method.org/reference/workflows/
source: sitemap
fetched_at: 2026-04-08T11:34:14.908984264-03:00
rendered_js: false
word_count: 533
summary: This document serves as a comprehensive reference guide detailing various BMad Game Dev Studio workflows, organized by the development phase—from initial concept to final testing. It outlines specific agents responsible for each task, ensuring developers know which workflow to use at every stage of game creation.
tags:
    - workflow-reference
    - game-development
    - bmgd
    - design-process
    - production-cycle
    - qa-testing
    - prototyping
category: reference
---

## BMGD Workflows Reference

[Section titled “BMGD Workflows Reference”](#bmgd-workflows-reference)

Complete catalog of all BMad Game Dev Studio workflows organized by development phase and purpose.

* * *

## Quick Flow Workflows

[Section titled “Quick Flow Workflows”](#quick-flow-workflows)

Rapid prototyping workflows for solo developers and small teams.

WorkflowAgentPurposePrerequisites**quick-prototype**IndieCreate a rapid game prototype for early validationGame engine installed**quick-dev**IndieQuick development iteration with game-specific guidanceExisting prototype**quick-spec**IndieGenerate a quick game specificationGame concept

**Use when:** You want to test ideas fast, work alone, or need a playable prototype quickly.

* * *

## Preproduction Workflows

[Section titled “Preproduction Workflows”](#preproduction-workflows)

Define your game concept and vision before committing to production.

WorkflowAgentPurposeOutputs**brainstorm-game**Game DesignerGenerate game ideas using specialized techniquesGame concept**game-brief**Game DesignerCreate a project brief capturing vision and positioning`game-brief.md`

**Use when:** You’re starting a new project and need to define what you’re building.

* * *

Create comprehensive game design documentation.

WorkflowAgentPurposeOutputs**create-gdd**Game DesignerCreate a Game Design Document with 24 game type templates`gdd.md`**narrative**Game DesignerDesign narrative elements and story`narrative.md`

**Use when:** You have a game concept and need to document the design.

**Game Type Templates Available:** Action Platformer, Adventure, Card Game, Fighting, Horror, Idle/Incremental, Metroidvania, MOBA, Party Game, Puzzle, Racing, Rhythm, Roguelike, RPG, Sandbox, Shooter, Simulation, Sports, Survival, Strategy, Text-Based, Tower Defense, Turn-Based Tactics, Visual Novel

* * *

## Technical Workflows

[Section titled “Technical Workflows”](#technical-workflows)

Plan your technical architecture and project structure.

WorkflowAgentPurposeOutputs**create-architecture**Game ArchitectCreate game architecture with engine-specific patterns`architecture.md`**generate-project-context**Game ArchitectCreate project context for AI consistency`project-context.md`**correct-course**Game ArchitectCourse correction when implementation is off-trackAnalysis report

**Use when:** You need to plan how to build your game or need to get back on track.

* * *

## Production Workflows

[Section titled “Production Workflows”](#production-workflows)

Plan and track development through sprints and stories.

WorkflowAgentPurposeOutputs**sprint-planning**Game Scrum MasterGenerate sprint status from epic files`sprint-status.yaml`**sprint-status**Game Scrum MasterView sprint progress, risks, and next actionsStatus report**create-story**Game Scrum MasterCreate story with ready-for-dev markingStory file in `stories/`**dev-story**Game DeveloperImplement story tasks with testsCompleted feature**code-review**Game DeveloperPerform clean context QA code reviewReview report**retrospective**Game Scrum MasterFacilitate retrospective after epic completionRetrospective notes

**Use when:** You’re ready to build features, track progress, or review work.

* * *

## Testing Workflows

[Section titled “Testing Workflows”](#testing-workflows)

Set up and run game testing across all phases.

WorkflowAgentPurposeOutputs**test-framework**Game QAInitialize game test framework (Unity/Unreal/Godot)Test project setup**test-design**Game QACreate comprehensive game test scenariosTest plan**automate**Game QAGenerate automated game testsTest suite**e2e-scaffold**Game QAScaffold E2E testing infrastructureE2E test framework**playtest-plan**Game QACreate structured playtesting planPlaytest plan**performance**Game QADesign performance testing strategyPerformance test plan**test-review**Game QAReview test quality and coverageCoverage report

**Use when:** You need to test your game, set up automation, or plan playtesting.

* * *

## Workflow Reference by Agent

[Section titled “Workflow Reference by Agent”](#workflow-reference-by-agent)

### Game Designer (Samus Shepard)

[Section titled “Game Designer (Samus Shepard)”](#game-designer-samus-shepard)

WorkflowPhasePurposebrainstorm-gamePreproductionGenerate and refine game ideasgame-briefPreproductionCreate project briefcreate-gddDesignCreate Game Design DocumentnarrativeDesignDesign story and narrative

### Game Architect (Cloud Dragonborn)

[Section titled “Game Architect (Cloud Dragonborn)”](#game-architect-cloud-dragonborn)

WorkflowPhasePurposecreate-architectureTechnicalCreate technical architecturegenerate-project-contextTechnicalCreate project contextcorrect-courseProductionCourse correction analysis

### Game Developer (Link Freeman)

[Section titled “Game Developer (Link Freeman)”](#game-developer-link-freeman)

WorkflowPhasePurposedev-storyProductionImplement story taskscode-reviewProductionReview code qualityquick-devQuick FlowQuick development iteration

### Game Scrum Master (Max)

[Section titled “Game Scrum Master (Max)”](#game-scrum-master-max)

WorkflowPhasePurposesprint-planningProductionPlan sprints from epicssprint-statusProductionView sprint progresscreate-storyProductionCreate implementation storiesretrospectiveProductionFacilitate retrospective

WorkflowPhasePurposetest-frameworkAnyInitialize test frameworktest-designAnyCreate test scenariosautomateAnyGenerate automated testse2e-scaffoldAnyScaffold E2E testingplaytest-planAnyPlan playtesting sessionsperformanceAnyPerformance testing strategytest-reviewAnyReview test coverage

### Game Solo Dev (Indie)

[Section titled “Game Solo Dev (Indie)”](#game-solo-dev-indie)

WorkflowPhasePurposequick-prototypeQuick FlowCreate rapid prototypequick-devQuick FlowQuick developmentquick-specQuick FlowQuick specification

* * *

- [**Agents Reference**](https://game-dev-studio-docs.bmad-method.org/reference/workflows/agents/) — Learn about all 6 BMGD agents
- [**Quick Flow vs Full Production**](https://game-dev-studio-docs.bmad-method.org/reference/explanation/quick-flow-vs-full/) — Choose your development approach
- [**Game Types Reference**](https://game-dev-studio-docs.bmad-method.org/reference/workflows/game-types/) — All 24 game type templates