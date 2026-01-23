---
title: CI/CD Automation and Autonomous Agents - Zencoder Docs
url: https://docs.zencoder.ai/learn/enterprise-best-practices/ci-cd-automation
source: crawler
fetched_at: 2026-01-23T09:28:27.821791528-03:00
rendered_js: false
word_count: 367
summary: This document explains how the Zencoder multi-repo tool provides AI agents with cross-repository context and outlines the steps for configuring and using it within an IDE.
tags:
    - multi-repo
    - zencoder
    - ai-agents
    - code-indexing
    - repository-management
    - git-integration
category: guide
---

What is a multi-repo project? What’s the benefit?

A multi-repo (polyrepo) project spreads the product across several Git repositories instead of a single monorepo, which gives each service, library, or infrastructure module its own pipelines and permissions. Enterprises lean on it for autonomy: teams ship on their own cadence, guard access per repo, and even share specific repos with vendors or customers without exposing the rest of the codebase.

Why do coding agents struggle to work with multiple repos?

IDE copilots typically ingest only the repo that’s open in the editor. Even multi-root workspaces inherit config (linters, auth, launch files) that assume a single repo, so agents end up blind to adjacent services. Without those sibling repos, they hallucinate APIs, miss cross-repo contracts, and ship brittle changes because they cannot inspect or test the surrounding code.

What’s the Zencoder multi-repo tool?

It’s an indexing system in the dashboard that ingests any GitHub, GitLab, or Bitbucket repo you connect via a scoped token. Once indexed, Zencoder keeps a read-only snapshot plus metadata (owners, last index time, auto- reindex toggle), and agents with the multi-repo tool can list, open, and read those repos even if they’re not the one currently open in the IDE.

How to configure the Zencoder multi-repo tool?

In the web dashboard, start on *Connections* to add GitHub/GitLab/Bitbucket access with a personal access token that scopes exactly which repos the agent should read. Then switch to *Repositories*, add repos one by one, decide whether they auto-reindex on changes, and assign which teammates can use each repo through the tool. The same page shows indexing status so you can trigger manual refreshes later.

How to use the multi-repo tool?

Enable the tool on any agent (built-in or custom) and run your normal chat in the IDE. When the agent needs extra context it calls *listRepos*, jumps into the indexed repo, reads files or docs, and returns to edit the open repo. It’s read-only - changes still land in the workspace you’re editing - but it gives the agent the architectural picture it needs. A quick sanity check is to ask, “What repos can you see through the Multi-Repo tool?” and make sure it lists everything you expect.