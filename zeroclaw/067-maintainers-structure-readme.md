---
title: ZeroClaw Docs Structure Map
date: 2026-05-05T00:00:00Z
url: https://github.com/openagen/zeroclaw/blob/master/docs/maintainers/structure-README.md
source: git
fetched_at: 2026-05-02T14:51:44.692128623-03:00
rendered_js: false
word_count: 397
summary: This document establishes the organizational standards and directory hierarchy for the ZeroClaw documentation project based on language, content categories, and document intent.
tags:
    - documentation-standards
    - repository-structure
    - internationalization
    - project-management
    - content-guidelines
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# ZeroClaw Docs Structure Map

Defines documentation structure across three axes:

1. Language
2. Part (category)
3. Function (document intent)

Last refreshed: **February 22, 2026**

## 1) By Language

| Language | Entry point | Canonical tree | Notes |
|---|---|---|---|
| English | `docs/README.md` | `docs/` | Source-of-truth runtime behavior docs authored in English first |
| Chinese (`zh-CN`) | `docs/README.zh-CN.md` | `docs/` localized hub + selected docs | Uses localized hub and shared category structure |
| Japanese (`ja`) | `docs/README.ja.md` | `docs/` localized hub + selected docs | Uses localized hub and shared category structure |
| Russian (`ru`) | `docs/README.ru.md` | `docs/` localized hub + selected docs | Uses localized hub and shared category structure |
| French (`fr`) | `docs/README.fr.md` | `docs/` localized hub + selected docs | Uses localized hub and shared category structure |
| Vietnamese (`vi`) | `docs/i18n/vi/README.md` | `docs/i18n/vi/` | Full Vietnamese tree canonical under `docs/i18n/vi/`; `docs/vi/` and `docs/*.vi.md` are compatibility paths |

## 2) By Part (Category)

Primary navigation modules by product area.

- `docs/getting-started/` — initial setup and first-run flows
- `docs/reference/` — command/config/provider/channel reference indexes
- `docs/operations/` — day-2 operations, deployment, troubleshooting entry points
- `docs/security/` — security guidance and security-oriented navigation
- `docs/hardware/` — board/peripheral implementation and hardware workflows
- `docs/contributing/` — contribution and CI/review processes
- `docs/project/` — project snapshots, planning context, status-oriented docs

## 3) By Function (Document Intent)

Use this grouping to decide where new docs belong.

### Runtime Contract (current behavior)

- [[120-reference-cli-commands-reference|Commands Reference]]
- [[121-reference-providers-reference|Providers Reference]]
- [[122-reference-channels-reference|Channels Reference]]
- [[123-reference-config-reference|Config Reference]]
- [[069-ops-operations-runbook|Operations Runbook]]
- [[070-ops-troubleshooting|Troubleshooting]]
- [[001-setup-guides-one-click-bootstrap|One-Click Bootstrap]]

### Setup / Integration Guides

- [[151-contributing-custom-providers|Custom Providers]]
- [[155-contributing-langgraph-integration|LangGraph Integration]]
- [[073-setup-guides-network-deployment|Network Deployment]]
- [[124-setup-guides-matrix-e2ee-guide|Matrix E2EE Guide]]
- [[063-setup-guides-mattermost-setup|Mattermost Setup]]
- [[125-setup-guides-nextcloud-talk-setup|Nextcloud Talk Setup]]

### Policy / Process

- [[157-contributing-pr-workflow|PR Workflow]]
- [[159-contributing-reviewer-playbook|Reviewer Playbook]]
- [[149-contributing-ci-map|CI Map]]
- [[145-contributing-actions-source-policy|Actions Source Policy]]

### Proposals / Roadmaps

- [[076-hardware-hardware-peripherals-design|Hardware Peripherals Design]]
- [[081-i18n-vi-resource-limits|Resource Limits]]
- [[078-i18n-vi-audit-logging|Audit Logging]]
- [[077-i18n-vi-agnostic-security|Agnostic Security]]
- [[079-i18n-vi-frictionless-security|Frictionless Security]]
- [[082-project-security-roadmap|Security Roadmap]]

### Snapshots / Time-Bound Reports

- `docs/project-triage-snapshot-2026-02-18.md`

### Assets / Templates

- `docs/datasheets/`
- [[152-contributing-doc-template|Doc Template]]

## Placement Rules (Quick)

- New runtime behavior docs must be linked from appropriate category index and `docs/SUMMARY.md`
- Navigation changes must preserve locale parity across `docs/README*.md` and `docs/SUMMARY*.md`
- Vietnamese full localization lives in `docs/i18n/vi/`; compatibility files should point to canonical paths

#documentation-standards #repository-structure #internationalization #project-management #content-guidelines
