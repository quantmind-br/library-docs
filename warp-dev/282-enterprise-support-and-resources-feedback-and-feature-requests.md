---
title: Feedback and feature requests | Enterprise | Warp
url: https://docs.warp.dev/enterprise/support-and-resources/feedback-and-feature-requests
source: sitemap
fetched_at: 2026-04-29T15:06:10.915597235-03:00
rendered_js: false
word_count: 294
summary: This document outlines the support channels, bug reporting procedures, and feature request processes specifically available to Warp Enterprise customers.
tags:
    - enterprise-support
    - bug-reporting
    - feature-requests
    - customer-success
    - technical-assistance
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Enterprise customers have dedicated support channels for real-time assistance, bug reports, and feature requests.

## Enterprise support channels

Priority support for Enterprise customers:

- **Dedicated Slack or Teams channel** — shared with Warp engineers for real-time assistance, bug reports, and feature discussions.
- **Account manager** — direct contact for escalations, strategic feature requests, and enterprise-specific questions.

> [!info]
> Use your dedicated Slack/Teams channel for the fastest response. Warp engineers monitor these during business hours.

## Reporting bugs

Include the following in your bug report:

| Field | Description |
|-------|-------------|
| Description | What happened and expected outcome |
| Steps to reproduce | How to trigger the issue |
| Debugging ID (Agent issues) | Right-click the Agent conversation block → **Copy debugging ID**. See [[299-support-and-community-troubleshooting-and-support-known-issues|Sending Feedback & Logs]] for details. |
| Environment | OS, Warp version, relevant configuration |

> [!info]
> Most Enterprise teams have UGC collection disabled, limiting diagnostics from debugging IDs. Logs and reproduction steps are especially important.

### Gathering logs

Warp logs do not contain console input or output.

| Platform | Log path |
|----------|----------|
| macOS | `~/Library/Logs/warp.log*` |
| Windows | `%LOCALAPPDATA%\warp\Warp\data\logs\warp.log*` |
| Linux | `~/.local/state/warp-terminal/warp.log*` |

Open **Command Palette** (`⌘P` / `Ctrl+Shift+P`) and search **View Warp Logs** for in-app access. See [[299-support-and-community-troubleshooting-and-support-known-issues|Sending Feedback & Logs]] for detailed instructions including how to zip logs and capture crash reports.

## Requesting features

- **Enterprise customers** — use your dedicated Slack/Teams channel or account manager to ensure tracking and prioritization.
- **Public requests** — open an issue on [GitHub Issues](https://github.com/warpdotdev/warp/issues/new/choose) for visibility and community discussion.

## Specialized contacts

For security or privacy inquiries, reach the appropriate team directly.

For billing, technical issues, and feature requests — contact your account manager or dedicated Slack/Teams channel.
