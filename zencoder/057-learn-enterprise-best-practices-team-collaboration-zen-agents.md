---
title: Team Collaboration and Knowledge Sharing with Zen Agents - Zencoder Docs
url: https://docs.zencoder.ai/learn/enterprise-best-practices/team-collaboration-zen-agents
source: crawler
fetched_at: 2026-01-23T09:28:27.940893595-03:00
rendered_js: false
word_count: 375
summary: This document explains the concept of Zen Agents as customizable AI copilots and provides instructions for utilizing the Agents Library to automate and scale engineering workflows.
tags:
    - zen-agents
    - workflow-automation
    - custom-agents
    - zencoder
    - engineering-productivity
category: guide
---

What are Zen Agents? Why are they useful?

Zen Agents are Zencoder’s bespoke copilots: you spin them up on the Agents page, give each one a friendly name plus a CLI alias, and pour in the exact rituals you expect— coding patterns, review rules, release etiquette, reporting beats. Their instructions sit alongside a curated toolbelt, so an observability agent might lean on search and file edit while an SRE tuner ropes in custom MCP actions. Once created they live in the Custom Agents section of the selector, ready for teams to reuse as the canonical way to run that workflow.

How to browse the Agents Library?

The Library lives on a tab inside that same Agents page and acts like an inspiration gallery. Click the tab to see curated agents you have not installed yet, skim their thumbnails, and open any card to study its instructions, tools, and sharing defaults. Because each listing is editable after installation, you can treat the Library like a set of starter kits and choose the ones that match gaps in your team’s workflows.

How to use an agent from the Library?

When a Library agent looks promising, click through to its detail view and hit *Add*. The agent is copied into your Custom Agents list as if you authored it, so you can retune the instructions, swap tools, and decide whether to keep it personal or share it org-wide. From there it behaves like any other agent: select it in the agent picker when starting a conversation, gather feedback from the runs, and keep iterating on its instructions so the entire org benefits from each tweak.

How to identify use cases for new custom agents?

Agents shine when the work is repetitive, high-stakes, or steeped in tribal knowledge. Look for areas where senior engineers keep repeating the same instructions—code review checklists, secure-by-default patterns, release rituals—and translate those expectations into agent prompts instead of reinventing them every run. The more specific the mandate, the better: a deployment hardening agent or a “backend observability sweeper” will always outperform a single generalist. If a workflow is already documented in runbooks or captured in hallway conversations, it is mature enough to crystallize into a custom agent so the expertise scales beyond one person.