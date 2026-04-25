---
title: Why Solutioning Matters
url: https://docs.bmad-method.org/explanation/why-solutioning-matters/
source: sitemap
fetched_at: 2026-04-08T11:30:07.505883176-03:00
rendered_js: false
word_count: 205
summary: This document explains the purpose and necessity of 'Solutioning,' which is the phase that translates high-level requirements into concrete technical designs to ensure consistency among multiple implementing agents.
tags:
    - solutioning
    - technical-design
    - architectural-decisions
    - multi-agent-development
    - api-consistency
    - project-workflow
category: guide
---

Phase 3 (Solutioning) translates **what** to build (from Planning) into **how** to build it (technical design). This phase prevents agent conflicts in multi-epic projects by documenting architectural decisions before implementation begins.

## The Problem Without Solutioning

[Section titled “The Problem Without Solutioning”](#the-problem-without-solutioning)

```text

Agent 1 implements Epic 1 using REST API
Agent 2 implements Epic 2 using GraphQL
Result: Inconsistent API design, integration nightmare
```

When multiple agents implement different parts of a system without shared architectural guidance, they make independent technical decisions that may conflict.

## The Solution With Solutioning

[Section titled “The Solution With Solutioning”](#the-solution-with-solutioning)

```text

architecture workflow decides: "Use GraphQL for all APIs"
All agents follow architecture decisions
Result: Consistent implementation, no conflicts
```

By documenting technical decisions explicitly, all agents implement consistently and integration becomes straightforward.

## Solutioning vs Planning

[Section titled “Solutioning vs Planning”](#solutioning-vs-planning)

AspectPlanning (Phase 2)Solutioning (Phase 3)QuestionWhat and Why?How? Then What units of work?OutputFRs/NFRs (Requirements)Architecture + Epics/StoriesAgentPMArchitect → PMAudienceStakeholdersDevelopersDocumentPRD (FRs/NFRs)Architecture + Epic FilesLevelBusiness logicTechnical design + Work breakdown

**Make technical decisions explicit and documented** so all agents implement consistently.

This prevents:

- API style conflicts (REST vs GraphQL)
- Database design inconsistencies
- State management disagreements
- Naming convention mismatches
- Security approach variations

## When Solutioning is Required

[Section titled “When Solutioning is Required”](#when-solutioning-is-required)

TrackSolutioning Required?Quick FlowNo - skip entirelyBMad Method SimpleOptionalBMad Method ComplexYesEnterpriseYes

## The Cost of Skipping

[Section titled “The Cost of Skipping”](#the-cost-of-skipping)

Skipping solutioning on complex projects leads to:

- **Integration issues** discovered mid-sprint
- **Rework** due to conflicting implementations
- **Longer development time** overall
- **Technical debt** from inconsistent patterns