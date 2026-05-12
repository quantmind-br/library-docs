---
title: Contributing to Warp | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/community/contributing
source: sitemap
fetched_at: 2026-04-29T15:05:39.029167559-03:00
rendered_js: false
word_count: 216
summary: This document outlines the guidelines and resources for contributing to the Warp open-source project, including code submissions, feedback reporting, and security vulnerability disclosures.
tags:
    - open-source
    - contribution-guide
    - bug-reporting
    - warp-terminal
    - community-guidelines
    - security-policy
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp's client is open source under [AGPL v3](https://github.com/warpdotdev/warp/blob/master/LICENSE) at [`warpdotdev/warp`](https://github.com/warpdotdev/warp). Every contribution type is welcome — one-line bug reports, full feature PRs, new themes, or workflows. See [`CONTRIBUTING.md`](https://github.com/warpdotdev/warp/blob/master/CONTRIBUTING.md) for the full code contribution flow.

## Ways to contribute

- **Contribute code** — claim any issue labeled `ready-to-spec` or `ready-to-implement`, then open a spec or code PR. See `CONTRIBUTING.md` for spec format, tests, `./script/presubmit`, and PR template.
- **Publish Warp Drive objects** — share Workflows, Notebooks, Rules, and Prompts publicly from [Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/).
- **Find an issue to pick up** — browse [build.warp.dev](https://build.warp.dev), a live dashboard of work Warp's agents are tackling across `warpdotdev/warp`.

## Send feedback and bug reports

Use the [`/feedback`](https://docs.warp.dev/support-and-community/troubleshooting-and-support/sending-us-feedback#using-feedback-in-warp) slash command inside Warp to draft and file a GitHub issue without leaving the terminal.

Other channels:
- `⌘+Shift+F` (macOS) or `Ctrl+Shift+F` (Windows/Linux) opens the in-app feedback dialog.
- **Send Feedback** in Warp's Help menu (macOS).

For logs, crash reports, CPU samples, and AI debugging IDs, see [[299-support-and-community-troubleshooting-and-support-known-issues|Sending feedback and logs]].

## Reporting security issues

> [!danger]
> Do not file public issues for security vulnerabilities.

Email [security@warp.dev](mailto:security@warp.dev) with reproduction steps, impact, and any proof of concept. See [`CONTRIBUTING.md`](https://github.com/warpdotdev/warp/blob/master/CONTRIBUTING.md#reporting-security-issues) for full guidance.

## Code of conduct

Warp's open source repositories follow the [Contributor Covenant](https://www.contributor-covenant.org/) v2.1. Read the [full text](https://github.com/warpdotdev/warp/blob/master/CODE_OF_CONDUCT.md) or report violations to [warp-coc@warp.dev](mailto:warp-coc@warp.dev).
