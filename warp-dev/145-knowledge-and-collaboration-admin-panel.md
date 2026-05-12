---
title: Team Admin Panel | Warp
url: https://docs.warp.dev/knowledge-and-collaboration/admin-panel
source: sitemap
fetched_at: 2026-04-29T15:03:37.70573198-03:00
rendered_js: false
word_count: 717
summary: This document explains the functionality of the Warp Admin Panel, which allows team administrators to manage organization-wide settings, access controls, AI policies, and billing configurations.
tags:
    - admin-panel
    - team-management
    - settings-enforcement
    - access-control
    - billing-management
    - ai-policy
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## What is the Admin Panel?

The [Admin Panel](https://app.warp.dev/admin/) provides team administrators centralized control over organization-wide settings, enforced across all team members.

> [!info]
> Admin Panel access is restricted to team administrators. Currently, only the team creator is designated admin. If admin styles override user preferences, users see a note indicating the setting is admin-configured and cannot control it.

**Key features:**
- **AI Settings** — agent autonomy, permissions, and allowlists
- **Privacy Controls** — data collection and enterprise secret redaction
- **Billing Management** — spending limits and usage-based pricing
- **Code Settings** — codebase indexing and context features
- **Sharing Policies** — link sharing and collaboration permissions

Access at: [https://app.warp.dev/admin/](https://app.warp.dev/admin/)

## How Settings Enforcement Works

### Toggleable vs. Fixed Settings

**Toggleable settings** appear as dropdowns with options like Enabled/Disabled, autonomy levels, or "Respect User Setting."

**Fixed settings** are determined by billing tier — displayed with: "Configuring this setting is not available on your plan."

### Setting Inheritance

| Mode | Behavior |
|---|---|
| **Organization enforced** | Applies to all members regardless of preference |
| **Respect user setting** | Individual team members control the setting |
| **Tier restricted** | Locked to defaults based on billing plan |

### User Experience

> [!info]
> Changes take effect immediately for all team members. Test settings in Warp before applying organization-wide.

When organization settings override preferences:
- Users see personal settings grayed out.
- A message indicates "your organization has configured this setting."
- Users cannot modify enforced settings.

## Plan Limitations

| Feature | Free | Business | Enterprise |
|---|---|---|---|
| Settings toggleability | Most fixed | Most toggleable | Full control |
| Codebase Context | Limited | Enhanced | Full |
| Sharing features | Limited | Advanced | Advanced |
| Secret redaction | — | — | ✅ |
| Custom LLM integration | — | — | ✅ |
| Compliance features | — | — | ✅ |

Visit [warp.dev/pricing](https://www.warp.dev/pricing) for plan details.

## Admin Panel Sections

### AI Settings

#### General AI Settings

**AI in Remote Sessions** — Controls AI availability during SSH and remote connections. Enterprise plans can toggle; Free tier has it enabled by default.

**Prompt Summarization Caching** — Caches conversation summaries at the LLM provider to improve performance when conversations are long.

#### Autonomy Settings

Configure agent independence for actions:

| Setting | Options |
|---|---|
| **Apply Code Diffs** | Agent Decides, Always Ask, Always Allow, Respect User Setting |
| **Create Plans** | Allow agents to create structured task plans without approval |
| **Execute Commands** | Control autonomous terminal command execution |
| **Read Files** | Control agent access to reading codebase files |

### Directory and Command Control

**Directory Allowlist** — Directories where agents can read files without restriction (e.g., `~/git/repo1`).

**Command Allowlist** — Regex patterns for commands agents can execute without permission:

- `grep .*` — text search
- `ls(\s.*)?` — directory listing
- `which .*` — executable locations

**Command Denylist** — Commands always requiring approval (takes precedence over allowlist):

- `rm -rf.*` — recursive deletion
- `sudo.*` — administrative
- `curl.*` — network requests

> [!warning]
> Denylist rules take precedence over allowlist and autonomy settings. Matching a denylist always requires user permission.

### Privacy Settings

**UGC Data Collection** — Controls Warp's collection of user-generated content:
- Disabled, Enabled, Respect User Setting

**Enterprise Secret Redaction** (Enterprise only) — Applies regex patterns to prevent secrets from being sent to Warp or LLM servers. Includes:
- Automatic detection of common secret patterns
- Custom regex patterns for organization-specific secrets
- Applied unconditionally across all team members

### Code Settings

**Codebase Context** — Determines whether Warp indexes team Git repositories for AI context:
- Disabled, Enabled, Respect User Setting

Higher tier plans support more indexed repositories and larger file limits per codebase.

### Billing Settings

**Usage Based Pricing** — Enable pay-as-you-go billing for credits beyond the plan's quota. When enabled, set a **Monthly Spending Limit** for overage.

The system displays current overage usage: total overage credits used and current month's overage costs.

### Sharing Settings

**Direct Link Sharing** — Allow team members to share Notebooks, Workflows, and other objects via direct links.

**Anyone with Link Sharing** — Enable public access — anyone with the link can view without being a team member.
