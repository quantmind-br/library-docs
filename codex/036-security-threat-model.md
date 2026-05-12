---
title: Improving the threat model
url: https://developers.openai.com/codex/security/threat-model.md
source: llms
fetched_at: 2026-04-30T10:16:06.806026193-03:00
rendered_js: false
word_count: 224
summary: This document explains how to define and refine a project threat model within Codex Security to improve the accuracy and prioritization of automated security scans.
tags:
    - threat-modeling
    - security-scans
    - code-analysis
    - repository-security
    - vulnerability-management
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Improving the threat model

A threat model is a short security summary of how your repository works. In Codex Security, you edit it as a `project overview`; the system uses it as scan context for future scans, prioritization, and review.

Codex Security creates the first draft from the code. If findings feel off, edit the threat model first.

## What to include

- entry points and untrusted inputs
- trust boundaries and auth assumptions
- sensitive data paths or privileged actions
- areas your team wants reviewed first

Example:

> Public API for account changes. Accepts JSON requests and file uploads. Uses an internal auth service for identity checks and writes billing changes through an internal service. Focus review on auth checks, upload parsing, and service-to-service trust boundaries.

## How to improve

Edit the threat model when findings miss areas you care about or show up where you don't expect. Changes affect future scan context.

Some users copy the current threat model into Codex, improve it based on desired focus areas, then paste the updated version back into the web UI.

### Where to edit

Go to [Codex Security scans](https://chatgpt.com/codex/security/scans), open the repository, and click **Edit**.

## Related docs

- [[010-security-setup|Codex Security setup]] — repository setup and findings review
- [[048-security|Codex Security]] — product overview
- [[073-security-faq|FAQ]] — common questions

#security #threat-model #codex