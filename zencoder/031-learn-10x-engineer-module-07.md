---
title: 'Module 7: Working at an Organization - Zencoder Docs'
url: https://docs.zencoder.ai/learn/10x-engineer/module-07
source: crawler
fetched_at: 2026-01-23T09:28:31.390870795-03:00
rendered_js: false
word_count: 158
summary: This document explains how to set up Jira integrations, manage organization-wide custom agents, and configure multi-repository search within Zencoder to enhance team collaboration.
tags:
    - zencoder
    - jira-integration
    - custom-agents
    - multi-repo-search
    - collaboration
    - organization-management
category: tutorial
---

## Intro

Module 7 focuses on collaboration: wiring Jira directly into Zencoder, curating org-shared custom agents, and provisioning multi-repo search so teams tap shared knowledge without friction.

## Video lesson

Preview lesson. The full video is available on Udemy.

## Key takeaways

- Connect Jira within the mentions menu so agents can ingest ticket context via `@Jira` references instead of manual copy/paste.
- Revoke or swap Jira connections from the Integrations pane whenever scopes change.
- When creating custom agents for the org, set sharing to `org`, supply clear instructions/tools, and use the web dashboard to review owners and update configs.
- Check the agent selector’s tags (`org`) to distinguish your personal templates from shared ones and find the teammate responsible for maintenance.
- As an admin, register GitHub/GitLab/Bitbucket connections once, then add repositories with multi-repo search + auto reindex to keep agent lookups current.
- Restrict repo access to specific users if needed; otherwise leave `all users` so every agent session can consult the shared codebases.