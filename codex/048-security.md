---
title: Codex Security
url: https://developers.openai.com/codex/security.md
source: llms
fetched_at: 2026-04-30T10:16:03.439646609-03:00
rendered_js: false
word_count: 201
summary: Codex Security is a tool for engineering and security teams designed to detect, validate, and remediate vulnerabilities within connected GitHub repositories using contextual threat modeling.
tags:
    - vulnerability-scanning
    - github-integration
    - code-security
    - threat-modeling
    - remediation
    - security-workflow
category: concept
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Codex Security

Find, validate, and remediate likely vulnerabilities in connected GitHub repositories.

> [!note]
> This page covers the **security scanning product**. For sandboxing, approvals, network controls, and admin settings, see [[041-agent-approvals-security|Agent approvals & security]].

## What it does

1. **Find likely vulnerabilities** — repo-specific threat model + real code context
2. **Reduce noise** — validates findings before you review them
3. **Move toward fixes** — ranked results, evidence, suggested patches

## How it works

Scans connected repositories commit by commit. Builds scan context from your repo, checks likely vulnerabilities against that context, and validates high-signal issues in an isolated environment before surfacing them.

Workflow focuses on:
- repo-specific context instead of generic signatures
- validation evidence to reduce false positives
- suggested fixes you can review in GitHub

## Access

Works with connected GitHub repositories through Codex Web. OpenAI manages access. If you need access or a repository isn't visible, contact your OpenAI account team and confirm the repository is available through your Codex Web workspace.

## Related docs

- [[010-security-setup|Codex Security setup]] — setup, scanning, findings review
- [[073-security-faq|FAQ]] — common product questions
- [[036-security-threat-model|Improving the threat model]] — tune scope, attack surface, criticality assumptions

#security #codex #vulnerability-scanning