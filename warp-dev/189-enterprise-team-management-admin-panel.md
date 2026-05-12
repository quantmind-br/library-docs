---
title: Admin panel | Enterprise | Warp
url: https://docs.warp.dev/enterprise/team-management/admin-panel
source: sitemap
fetched_at: 2026-04-29T15:06:04.60084983-03:00
rendered_js: false
word_count: 911
summary: This document provides an overview of the Warp Admin Panel, detailing how administrators can configure organizational settings, enforce security policies, and manage team-wide access to AI features.
tags:
    - admin-panel
    - team-management
    - security-policy
    - agent-configuration
    - access-control
    - enterprise-compliance
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
The [Admin Panel](https://app.warp.dev/admin/) provides centralized control over team settings: agent behavior, security policies, codebase indexing, and collaboration features.

## Accessing the Admin Panel

**For team admins:**
- **Direct URL:** Log in with SSO → [app.warp.dev/admin/](https://app.warp.dev/admin/)
- **From Warp:** Profile icon → **Settings** → **Admin Panel** tab

**For team members:**
- Organization-enforced settings appear grayed out with "Your organization has configured this setting"
- Settings marked "Respect User Setting" remain customizable

## Settings enforcement levels

| Level | Behavior |
|---|---|
| **Organization enforced** | Applies to all members; cannot be overridden |
| **Respect user setting** | Users can customize; admins set a default |
| **Tier restricted** | Locked to billing plan; upgrade required to change |

> [!tip]
> Test settings with "Respect User Setting" on a small group before enforcing organization-wide.

## Plan limitations

| Feature | Free | Business | Enterprise |
|---|---|---|---|
| Most settings | Fixed | Configurable | Full control |
| Codebase Context | 2 repos | Enhanced | Unlimited + 200K files/repo |
| BYOLLM | — | — | Supported |
| Self-hosted agents | — | — | Supported |
| Custom secret redaction regex | — | — | Supported |
| Compliance | — | — | SOC 2, HIPAA, custom data agreements |
| Priority support | — | — | Dedicated Slack/Teams channels |

## Admin Panel sections

### AI settings

**General AI settings**

| Setting | Description |
|---|---|
| AI in remote sessions | Toggle agents in SSH sessions (Enterprise only) |
| Prompt summarization caching | Caches summaries for long conversations; covered by Zero Data Retention |

**Autonomy settings**

| Level | Behavior |
|---|---|
| Agent Decides | Acts autonomously when confident; asks when uncertain (recommended) |
| Always Ask | Requires approval for every action |
| Always Allow | Maximum autonomy, no confirmations |
| Respect User Setting | Individual users choose |

Additional controls:
- **Apply code diffs** — whether agents can apply changes without approval
- **Create plans** — whether agents can create `/plan` without approval
- **Execute commands** — manages autonomous command execution
- **Read files** — controls agent access to read files

**Directory and command control**

- **Directory allowlist** — absolute paths where agents can read without restriction (e.g., `~/git/internal-tooling`, `/home/user/repos/public-*`)
- **Command allowlist** — regex for commands agents run without asking (e.g., `grep .*`, `git status`, `which .*`)
- **Command denylist** — regex for commands that **always** require approval (e.g., `rm -rf.*`, `sudo.*`, `curl.*|wget.*`, `.*production.*`)

> [!warning]
> Command denylist takes precedence over allowlist and autonomy settings.

### Privacy settings

| Setting | Options |
|---|---|
| User-generated content data collection | Disabled / Enabled / Respect User Setting |
| Enterprise secret redaction | Auto-detects API keys, passwords, certificates; supports custom regex patterns (Enterprise) |

### Code settings

**Codebase Context** — indexes Git repos for agent context:

- **Disabled** — no indexing
- **Enabled** — team-wide indexing with centralized config (Enterprise: unlimited repos)
- **Respect User Setting** — individual control

### Billing settings

| Setting | Description |
|---|---|
| Usage-based pricing | Pay-as-you-go beyond plan quota; set monthly spending limits |
| Credit allocation | Allocate credit pools across teams/projects (Enterprise) |

### Sharing settings

| Setting | Options |
|---|---|
| Direct link sharing | Enabled / Team only / Disabled |
| Anyone with link sharing | Enabled / Disabled |

### Platform settings

**Enabled GitHub Orgs** — associates your Warp team with GitHub App installations, enabling Oz cloud agents (team API key runs) to clone repos and open PRs via the Oz by Warp GitHub App.

To configure: navigate to **Platform** → select which GitHub organizations the team should access. This setting only affects team API key runs — individual users' runs continue using their personal GitHub tokens.

> [!info]
> Available organizations reflect the Oz by Warp GitHub App installation scope. To change repository access, edit the installation in [GitHub settings](https://github.com/settings/installations). See [[194-agent-platform-cloud-agents-overview|Team GitHub authorization]] for details.

## Multi-admin support

Teams can have multiple admins to prevent single points of failure.

**Promoting/demoting admins:**
1. **Settings** → **Teams** → **Team Members**
2. Find the user → role dropdown → **Admin** or **Member**
3. **Save**

> [!info]
> Recommend at least one admin in addition to the Team Owner. Team Owners can transfer ownership; Admins cannot.

## Common admin workflows

### Initial enterprise setup

1. Configure SSO with your identity provider
2. Enable Codebase Context and index repositories
3. Set agent autonomy levels
4. Apply secret redaction (add custom patterns)
5. Configure BYOLLM (optional)
6. Create shared Warp Drive resources (Workflows, Rules, Prompts)

### Adjusting policies for different teams

1. Create separate Warp teams per group (DevOps, Data, Frontend)
2. Assign team-specific admins
3. Configure different autonomy levels per team
4. Use directory allowlists to scope agent access

### Responding to security incidents

1. Review agent action logs in the affected user's session
2. Add specific commands to the denylist
3. Adjust autonomy settings
4. Check Admin Panel settings for the affected user's team

## Troubleshooting

| Problem | Solution |
|---|---|
| Users don't see new settings | Verify setting is not "Respect User Setting"; have users restart Warp; confirm SSO login with correct team |
| Setting is grayed out | Restricted to higher-tier plan |
| Command allowlist not working | Verify regex; check denylist precedence; confirm autonomy settings allow execution |

#admin-panel #team-management #security-policy #agent-configuration #access-control #enterprise-compliance
