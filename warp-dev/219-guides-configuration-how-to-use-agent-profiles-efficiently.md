---
title: Use Agent Profiles Efficiently | Guides | Warp
url: https://docs.warp.dev/guides/configuration/how-to-use-agent-profiles-efficiently
source: sitemap
fetched_at: 2026-04-29T15:06:35.777454846-03:00
rendered_js: false
word_count: 273
summary: This document explains how to configure Agent Profiles to control the behavior, autonomy, and decision-making processes of coding agents.
tags:
    - agent-profiles
    - ai-configuration
    - workflow-optimization
    - coding-agents
    - autonomy-levels
category: concept
optimized: true
optimized_at: 2026-04-29T15:04:00Z
---
Agent Profiles control how your coding agents behave in different contexts. They define what the agent can read, plan, or execute — and how much autonomy it has.

To show how profiles change workflow, we'll build an NFL Predictor App using two profiles:

- Strategic Agent
- YOLO Agent

## Strategic Agent

- **Base Model:** GPT-5
- **Planning Model:** Claude 4 Opus

| Configuration | Value |
|--------------|-------|
| Apply code diffs | *agent decides* |
| Read files | *always allow* |
| Create plans | *always allow* |
| Execute commands | *ask first* |

When run:

1. The agent asks clarifying questions (e.g., *Do you want to scrape players and schedules?*)
2. Builds a detailed 14-step plan
3. Requests user input for environment variables

It's thorough and safe — but pauses often if you miss setup details.

## YOLO Agent

| Configuration | Value |
|--------------|-------|
| Apply code diffs | *always allow* |
| Read files | *always allow* |
| Create plans | *never* |
| Execute commands | *always allow* |

This agent skips long planning. It builds the project quickly, skipping over optional validation and focusing on essentials:

- Data ingestion
- Player stats
- Scoring calculation

It avoids brittle endpoints and produces a working dataset fast — though with fewer checks.

## Comparing the two

| Trait | Strategic Agent | YOLO Agent |
|-------|----------------|------------|
| Planning | Detailed, multi-step | None |
| Autonomy | Pauses for confirmation | Auto-executes |
| Speed | Slower, more thorough | Fast, minimal validation |
| Best for | Production, complex tasks | Rapid prototyping, exploration |