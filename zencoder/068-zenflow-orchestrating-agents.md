---
title: Orchestrating Agents in Zenflow - Zencoder Docs
url: https://docs.zencoder.ai/zenflow/orchestrating-agents
source: crawler
fetched_at: 2026-01-23T09:28:03.004008883-03:00
rendered_js: false
word_count: 526
summary: This document explains the Zenflow orchestration architecture, detailing how projects, tasks, and subtasks structure AI agent workflows for reliable software engineering.
tags:
    - zenflow
    - ai-orchestration
    - multi-agent-systems
    - workflow-management
    - task-automation
    - agent-verification
category: concept
---

## Why Orchestrate Agents?

Modern AI coding isn’t about a single prompt—it’s about **systems** that keep agents aligned, verified, and fast. Zenflow combines workflow orchestration, spec discipline, and multi-agent verification so you get the speed of AI with production-grade reliability.

> Orchestration is how AI transitions from a clever assistant to a **reliable engineering system**. Zenflow provides the structure, verification, and parallelism required to scale output safely.

## Zenflow’s Orchestration Map

Think of Zenflow in three levels of abstraction—**projects**, **tasks**, and **subtasks/chats**. Each level has its own UI surface and orchestration responsibility.

## Projects: Launching Orchestrated Work

Projects define the scope, repository, and automation presets used across tasks. The left column gives you:

- **Project switcher & quick menu** – Jump between recent projects, open the current workspace in your IDE, edit metadata, or delete unused initiatives.
- **List ↔ Board toggle** – Move between a stacked list and Kanban board. Both surfaces support sorting by Status, Creation date, or Last updated.
- **Task cards with rich controls** – Status indicators track each workflow stage and every card exposes Edit, Open in IDE, Duplicate, Archive, or Delete actions.
- **Rapid creation** – The global **+** icon and **New task** buttons launch the workflow-aware creation modal; in Board view you can add cards directly inside **To Do**.

## Tasks: Where Workflows Execute

Open any task and the middle column (Task Overview) becomes the orchestration cockpit:

- **Context header** – Shows title, dedicated branch, a status dropdown, and the primary **Merge** button when code is ready to ship.
- **Steps tab** – Surfaces `plan.md` so you can edit steps, add new ones, or toggle **Auto-start steps** for hands-free execution.
- **Changes tab** – Presents diffs from the task branch so you can review what agents changed before committing or merging.
- **Commits tab** – Lists every commit created in the task workspace and highlights when none exist yet.
- **Task menu (⋯)** – Gives access to Edit, Open in IDE, Duplicate, Archive, or Delete.

## Subtasks & Chats: Directing Multi-Agent Runs

The right column represents the live agent context:

- **Step-aware tabs** – Tabs such as Requirements, Technical Specification, or Implementation mirror your plan so each phase has its own chat log and instructions.
- **Live telemetry** – Zenflow streams the active step, shell commands, file reads, and reasoning effort so you can watch agents think and act.
- **Interactive composer** – Reference files with `@`, switch execution modes (DEFAULT, APPROVALS, PLAN), attach artefacts, and inject new guidance mid-run.
- **Add tab / All Tabs controls** – Spin up additional chat contexts for new subtasks or quickly switch between existing ones when agents run in parallel.

## From Projects to Verified Output

1. **Start inside Projects** – Choose the project, open the creation modal, and pick the workflow (Quick Change, Fix Bug, Spec and Build, or Full SDD) that sets the orchestration plan.
2. **Drive Tasks through steps** – Use the Steps tab to define `plan.md`, enable Auto-start, and watch Changes/Commits as artifacts materialize.
3. **Guide Subtasks via chat** – Monitor the right column to see what each agent is doing, offer clarifications, and let verifier agents run after builders.
4. **Parallelize intentionally** – Spin up multiple tasks per project or multiple step-specific chats so planning, implementation, docs, and verification happen simultaneously.