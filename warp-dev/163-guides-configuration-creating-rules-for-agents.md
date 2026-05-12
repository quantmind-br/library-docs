---
title: Create Reusable Rules for Your Team | Guides | Warp
url: https://docs.warp.dev/guides/configuration/creating-rules-for-agents
source: sitemap
fetched_at: 2026-04-29T15:06:35.902478988-03:00
rendered_js: false
word_count: 170
summary: This document describes how to use Warp's Agent Mode to create and apply reusable project rules that ensure consistent code and configuration standards across development tasks.
tags:
    - ai-coding-assistant
    - workflow-automation
    - agent-mode
    - code-standards
    - rust-development
    - docker-configuration
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
*Speaker: Maggie — Engineer at Warp*

## 1. Starting with Agent Mode Evals

Adding **Evals** (evaluations) to test a new feature. Warp surfaces helpful context — notebooks and internal docs — written by teammates on how to run Evals, making onboarding fast and collaborative.

## 2. Adding a Rust Syntax Eval

Asking Warp to update the Dockerfile to include Rust. The generated Dockerfile installs Rust differently than desired, and includes `gcc` and `python` via a single `apt-get` line, which doesn't follow internal conventions.

## 3. Stashing Changes & Creating a Rule

Instead of fixing manually every time, stash the changes and create a reusable Rule:

> **Rule Example:** "Always use `apt-get` to install packages and follow the same pattern used for installing Python and GCC."

Future sessions — and teammates — can automatically apply the same standard.

## 4. Applying the Rule

Ask Warp's Agent Mode to try again. Warp re-runs the request, follows the new rule, and correctly adds Rust with the right syntax. The code now matches conventions.
