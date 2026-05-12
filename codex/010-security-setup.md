---
title: Codex Security setup
url: https://developers.openai.com/codex/security/setup.md
source: llms
fetched_at: 2026-04-30T10:16:04.882153735-03:00
rendered_js: false
word_count: 369
summary: This guide provides instructions for setting up Codex Security, covering repository configuration, initiating security scans, managing threat models, and reviewing or remediating findings.
tags:
    - codex-security
    - threat-modeling
    - security-scanning
    - repository-setup
    - vulnerability-remediation
    - github-integration
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Codex Security setup

Walkthrough from initial access to reviewed findings and remediation PRs.

> [!note]
> Confirm you've set up [[016-cloud|Codex Cloud]] first.

## 1. Access and environment

Codex Security scans GitHub repositories connected through [[016-cloud|Codex Cloud]].

- Confirm your workspace has access to Codex Security.
- Confirm the repository you want to scan is available in Codex Cloud.

Go to [Codex environments](https://chatgpt.com/codex/settings/environments) and check whether the repository already has an environment. If not, create one before continuing.

## 2. New security scan

Go to [Create a security scan](https://chatgpt.com/codex/security/scans/new) and choose the repository.

Codex Security scans from newest commits backward to build and refresh scan context.

Configuration steps:
1. Select GitHub organization.
2. Select repository.
3. Select branch to scan.
4. Select environment.
5. Choose a **history window** — longer windows provide more context, but backfill takes longer.
6. Click **Create**.

## 3. Initial backfill

First commit-level security pass across the selected history window. Can take a few hours for larger repositories or longer windows. If findings aren't visible right away, wait for the initial scan to finish before troubleshooting.

## 4. Review scans and improve the threat model

After the initial scan finishes, open the scan and review the generated threat model. Update it to match your architecture, trust boundaries, and business context. This helps Codex Security rank issues for your team.

Keeping the threat model current helps produce better suggestions. For details, see [[036-security-threat-model|Improving the threat model]].

## 5. Review findings and patch

After backfill completes, review findings from the **Findings** view.

| View | Purpose |
|------|---------|
| **Recommended Findings** | Evolving top 10 list of most critical issues |
| **All Findings** | Sortable, filterable table across the repository |

Click a finding to open its detail page, which includes:
- concise issue description
- key metadata (commit details, file paths)
- contextual reasoning about impact
- relevant code excerpts
- call-path or data-flow context when available
- validation steps and output

Review each finding and create a PR directly from the detail page.

## Related docs

- [[048-security|Codex Security]] — product overview
- [[073-security-faq|FAQ]] — common questions
- [[036-security-threat-model|Improving the threat model]] — improve scan context and finding prioritization

#security #setup #codex #github