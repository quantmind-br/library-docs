---
title: Factory Release 1.9
url: https://docs.factory.ai/changelog/1-9.md
source: llms
fetched_at: 2026-03-03T01:12:23.894306-03:00
rendered_js: false
word_count: 296
summary: This document introduces the features of Factory 1.9, including mixed model workflows, customizable subagents for specific tasks, and automated GitHub pull request reviews.
tags:
    - factory-ai
    - release-notes
    - mixed-models
    - custom-droids
    - github-integration
    - ai-agents
    - code-review
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Factory Release 1.9

> Mixed models, custom subagents, and GitHub PR reviews

Factory 1.9 brings mixed models to let you choose the right model for each phase of work, custom subagents you can tailor to your workflow, and automated PR reviews through our new GitHub App.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/G1mN425ZKZQ" title="Factory 1.9 Release" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Mixed models

Plan complex features with a more capable model, then execute efficiently with a faster one—all in the same session without restarting.

Access the `/model` command to configure your spec model separately from execution. Switch between Sonnet 4.5 for architectural planning and Haiku 4.5 for implementation, or test different combinations to optimize for cost and latency.

<Note>Learn more about [mixed models](/cli/configuration/mixed-models).</Note>

## Custom subagents

Build specialized Droids for your workflow. Configure tools, models, and behavior.

**How it works**

1. Enable Custom Droids in `/settings`
2. Launch `/droids` to open the Droids Manager
3. Create subagents manually or let Factory generate them
4. Configure which tools and models each subagent uses
5. Delegate tasks to your custom Droids mid-session

**Use cases**

* Security specialists for code review and compliance checks
* Codebase explorers for architectural analysis
* Test generators for comprehensive test coverage
* Documentation writers for API and feature docs

<Note>Explore [custom droids](/cli/configuration/custom-droids)</Note>

## Factory GitHub App for PR reviews

Automate code reviews directly in your pull requests. Factory's GitHub App provides inline feedback with full context—no manual CLI setup required.

[Install Factory Droid Review on GitHub Marketplace →](https://github.com/marketplace/actions/factory-droid-review)

Add the app to your repository and configure your workflow with the `Factory-AI/droid-code-review@latest` action. Droids analyze PR changes and leave detailed comments on specific lines, catching issues early and maintaining code quality standards.

**Example**

```yaml  theme={null}
- name: Droid Review
  uses: Factory-AI/droid-code-review@latest
```