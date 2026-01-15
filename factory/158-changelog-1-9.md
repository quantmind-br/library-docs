---
title: Factory Release 1.9 - Factory Documentation
url: https://docs.factory.ai/changelog/1-9
source: sitemap
fetched_at: 2026-01-13T19:04:32.602973552-03:00
rendered_js: false
word_count: 239
summary: This document details the new features in Factory 1.9, including mixed models for using different AI models per phase, customizable subagents for specialized workflows, and a GitHub App for automated PR reviews.
tags:
    - factory-1.9
    - mixed-models
    - custom-subagents
    - github-integration
    - pr-automation
    - ai-workflow
category: reference
---

Factory 1.9 brings mixed models to let you choose the right model for each phase of work, custom subagents you can tailor to your workflow, and automated PR reviews through our new GitHub App.

## Mixed models

Plan complex features with a more capable model, then execute efficiently with a faster one—all in the same session without restarting. Access the `/model` command to configure your spec model separately from execution. Switch between Sonnet 4.5 for architectural planning and Haiku 4.5 for implementation, or test different combinations to optimize for cost and latency.

## Custom subagents

Build specialized Droids for your workflow. Configure tools, models, and behavior. **How it works**

1. Enable Custom Droids in `/settings`
2. Launch `/droids` to open the Droids Manager
3. Create subagents manually or let Factory generate them
4. Configure which tools and models each subagent uses
5. Delegate tasks to your custom Droids mid-session

**Use cases**

- Security specialists for code review and compliance checks
- Codebase explorers for architectural analysis
- Test generators for comprehensive test coverage
- Documentation writers for API and feature docs

## Factory GitHub App for PR reviews

Automate code reviews directly in your pull requests. Factory’s GitHub App provides inline feedback with full context—no manual CLI setup required. [Install Factory Droid Review on GitHub Marketplace →](https://github.com/marketplace/actions/factory-droid-review) Add the app to your repository and configure your workflow with the `Factory-AI/droid-code-review@latest` action. Droids analyze PR changes and leave detailed comments on specific lines, catching issues early and maintaining code quality standards. **Example**

```
- name: Droid Review
  uses: Factory-AI/droid-code-review@latest
```