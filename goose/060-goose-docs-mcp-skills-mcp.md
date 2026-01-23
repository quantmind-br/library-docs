---
title: Skills Extension | goose
url: https://block.github.io/goose/docs/mcp/skills-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:48.83346019-03:00
rendered_js: true
word_count: 176
summary: This document outlines the mandatory safe deployment procedure and checklist required for moving code from a feature branch to a production environment.
tags:
    - deployment-workflow
    - production-release
    - devops-checklists
    - continuous-delivery
    - deployment-safety
category: guide
---

I'll help you deploy the current branch to production. Let me first load the production deployment skill to follow the safe deployment procedure.

I can see you're on the **`my-feature-branch`** branch with some untracked files. Before proceeding with production deployment, I need to follow the safe deployment procedure.

#### ⚠️ Pre-deployment Confirmation Required[​](#%EF%B8%8F-pre-deployment-confirmation-required "Direct link to ⚠️ Pre-deployment Confirmation Required")

According to the production deployment skill, I need to complete the following checklist:

**Pre-deployment Checklist**

1. **Ensure all tests pass** - Have tests been run?
2. **Check staging environment is stable** - Has this been deployed to staging first?
3. **Notify #deployments channel** - Should I notify the team?

**Deployment Steps (once confirmed)**

1. Create release branch from main
2. Run `npm run build:prod`
3. Deploy to staging first, then production
4. Monitor error rates for 30 minutes

* * *

**Before I proceed, please confirm:**

1. ✅ Have all tests passed for the `my-feature-branch` branch?
2. ✅ Has this been tested on staging?
3. ✅ Should I notify the #deployments channel?
4. ✅ Are you sure you want to deploy the `my-feature-branch` branch (not `main`) to production?

Please confirm these items and I'll proceed with the deployment.