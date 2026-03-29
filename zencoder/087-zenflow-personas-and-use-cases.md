---
title: Personas and Use Cases - Zencoder Docs
url: https://docs.zencoder.ai/zenflow/personas-and-use-cases
source: crawler
fetched_at: 2026-01-23T09:28:04.849295707-03:00
rendered_js: false
word_count: 282
summary: This document outlines user personas and sample workflows for both professional and junior developers using Zenflow's automated agent orchestration.
tags:
    - zenflow
    - developer-personas
    - workflow-automation
    - agent-orchestration
    - software-development-lifecycle
    - user-journeys
category: guide
---

## Personas & Journeys

## Professional developers

Experienced engineers extend their teams with workflow-driven automation while keeping code review-ready.

## Newer to development

Learners lean on Zenflow’s guardrails to ship safely, grasp the steps, and keep the vibe steady.

## Professional Developers

## Sample journey

A senior engineer uses Zenflow to drive a cross-repo feature from spec to merge without micromanaging agents.

Kick off a Spec and Build task

They open the **Spec and Build** card, scope the task, and attach a product brief so Zenflow seeds `plan.md`, `requirements.md`, and `spec.md`.

Tune automation presets

In **Advanced**, they pick a `DEFAULT` Codex preset plus GitHub + MCP integrations so orchestrated agents can run tests, scripts, and verification hooks.

Run automatically

After kicking things off they let Zenflow auto-advance through Spec creation → Implementation Plan → Implementation, only stepping in when checkpoints need review.

Review & merge

Once verifier agents pass, they inspect the **Changes** tab, merge from the Task Overview, and let Zenflow push the branch + PR automatically.

## Newer to Development

## Sample journey

A junior builder fixes a bug with confidence because Zenflow scaffolds the investigation, solution design, and verification.

Start a Fix Bug task

They describe the failing behavior, attach screenshots, and let Zenflow create `investigation.md`, `solution.md`, and `implementation.md`.

Lean on guidance

Inside the right-column chats they keep Plan mode enabled, asking clarifying questions as the investigation step surfaces logs and hypotheses.

Validate before shipping

When agents propose a fix, they review diffs via **Changes**, run the suggested tests with a single click, and watch the telemetry confirm green checks.

Capture learnings

They add a short summary to `implementation.md`, letting future teammates see root cause, fix details, and remaining risks.

[Orchestrating Agents in Zenflow](https://docs.zencoder.ai/zenflow/orchestrating-agents)[Integrations and Settings](https://docs.zencoder.ai/zenflow/integrations-and-settings)