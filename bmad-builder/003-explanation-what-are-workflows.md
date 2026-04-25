---
title: What Are BMad Workflows?
url: https://bmad-builder-docs.bmad-method.org/explanation/what-are-workflows/
source: sitemap
fetched_at: 2026-04-08T11:33:14.076772892-03:00
rendered_js: false
word_count: 529
summary: This document explains what BMad Workflows are—structured processes designed to achieve a specific, cohesive outcome by guiding users through sequential steps. It details workflow types, interaction modes like progressive disclosure and headless operation, and advises when to use a workflow versus an agent.
tags:
    - bmad-workflows
    - process-design
    - workflow-automation
    - agent-comparison
    - progressive-disclosure
    - headless-mode
category: guide
---

BMad Workflows are skills that guide users through a **structured process** to produce a specific output. They do most of the heavy lifting in the BMad ecosystem. Focused, composable, and generally stateless.

## What Makes a Workflow a Workflow

[Section titled “What Makes a Workflow a Workflow”](#what-makes-a-workflow-a-workflow)

Like agents, workflows are ultimately skill files. The difference is in emphasis: workflows prioritize **getting to an outcome** over maintaining a persistent identity.

TraitWorkflowAgent**Goal**Complete a defined process and produce an artifactBe an ongoing conversational partner**Persona**Minimal, enough to facilitate a good conversationCentral to the experience**Memory**Generally stateless between sessionsPersistent agent memory**Scope**All steps serve one cohesive purposeCan span loosely related capabilities

The BMad Builder classifies workflows into three tiers based on complexity.

TypeDescriptionExample**Simple Utility**A single-purpose tool that does one thing wellValidate a schema, convert a file format**Simple Workflow**A short guided process with a few sequential stepsCreate a quick tech spec**Complex Workflow**A multi-stage process with branching paths, progressive disclosure, and potentially multiple outputsCreate and manage PRDs (covering create, edit, validate, convert, and polish)

## Progressive Disclosure

[Section titled “Progressive Disclosure”](#progressive-disclosure)

Complex workflows use **progressive disclosure** to handle multiple operations within a single skill. Rather than building five separate skills for create, edit, validate, convert, and polish, you build one workflow that detects the user’s intent (from how they talk to it or what arguments they pass) and routes internally to the right path.

This is the same pattern that powers BMad’s own multi-capability agents and workflows. It keeps the user’s experience simple while the skill handles routing behind the scenes.

## YOLO Mode and Guided Mode

[Section titled “YOLO Mode and Guided Mode”](#yolo-mode-and-guided-mode)

Both the Agent Builder and the Workflow Builder support two interaction styles when creating skills.

ModeHow It WorksBest For**YOLO**You brain-dump your idea; the builder guesses its way to a finished skill, asking only when truly stuckQuick prototypes, experienced builders**Guided**The builder walks you through decisions, clarifies ambiguities, and ensures nothing is overlookedProduction workflows, first-time builders

Guided mode is no longer the slow multi-step process of earlier BMad versions. It is conversational and adaptive, but produces significantly better results than YOLO for complex workflows.

## Headless (Autonomous) Mode

[Section titled “Headless (Autonomous) Mode”](#headless-autonomous-mode)

Like agents, workflows can support a **Headless Mode**. When invoked headless (through a scheduler, orchestrator, or another skill) the workflow skips interactive prompts and completes its process end-to-end without waiting for user input.

## When to Build a Workflow vs. an Agent

[Section titled “When to Build a Workflow vs. an Agent”](#when-to-build-a-workflow-vs-an-agent)

Choose a Workflow WhenChoose an Agent WhenThe process has a clear start and endThe user will return to it across sessionsNo need to remember past interactionsRemembering context adds valueAll steps serve one cohesive goalCapabilities are loosely relatedYou want a composable building blockYou want a persistent conversational partner

Workflows are also excellent as the **internal capabilities** of an agent. Build the workflow first, then wrap it in an agent if you need persona and memory on top.

## Building Workflows

[Section titled “Building Workflows”](#building-workflows)

The **BMad Workflow Builder** (`bmad-workflow-builder`) uses the same six-phase conversational discovery as the Agent Builder (intent, classification, requirements, drafting, building, and quality optimization) and produces a ready-to-use skill folder.

See the [Builder Commands Reference](https://bmad-builder-docs.bmad-method.org/reference/builder-commands/) for details on the build process phases and capabilities.