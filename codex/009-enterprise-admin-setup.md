---
number: 9
category: guide
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/enterprise/admin-setup.md
word_count: 819
---
# Admin Setup

> **BLUF:** Step-by-step rollout guide for ChatGPT Enterprise admins to configure Codex (local + cloud), set up RBAC, deploy managed policies, configure Team Config, and establish governance/observability.

## Security & Privacy

| Feature | Detail |
|---------|--------|
| **No training** | Enterprise data not used for model training |
| **Zero data retention** | App/CLI/IDE: code stays in developer environment |
| **Encryption** | AES-256 at rest, TLS 1.2+ in transit |
| **Audit logging** | Via ChatGPT Compliance API |
| **Residency** | Follows ChatGPT Enterprise policies |

## Owner Roles

| Owner | Responsibility |
|-------|----------------|
| **Workspace owner** | Configure Codex settings |
| **Security owner** | Agent permissions |
| **Analytics owner** | Analytics + compliance APIs |

## Step 1: Enable Codex

**Codex local** — enabled by default for new workspaces. Toggle: `Workspace Settings > Settings and Permissions > Allow members to use Codex Local`.

- Enables app, CLI, IDE extension for allowed users
- Error "403 - Unauthorized" if toggle is off
- Enable device code auth for CLI in non-interactive environments

**Codex cloud** — requires GitHub (cloud-hosted) repos. Prerequisites: admin GitHub access to target repos.

Toggle: `Workspace Settings > Settings and Permissions > Allow members to use Codex Cloud`.

- Enable GitHub Connector first
- May take up to 10 minutes to appear in ChatGPT
- Enable Slack integration for task completion notifications
- Internet access: allowlist domains + HTTP methods (default: no internet)

> ⚠️ For on-premises repos or non-GitHub codebases, use the [[021-guides-agents-sdk|Agents SDK]] to build custom cloud workflows.

## Step 2: RBAC

Create custom roles via ChatGPT admin settings. Permissions resolve to most permissive across multiple roles.

### Create a Codex Admin Group

Dedicated group for admins, separate from general users.

| Role | Permission |
|------|------------|
| **Codex Admin** | View analytics, manage policies, manage cloud environments |
| **Codex Users** | Use Codex (app, CLI, IDE) |
| **General users** | No Codex access |

Recommended pattern:
1. Create "Codex Users" group for people using Codex
2. Create "Codex Admin" group for admins managing settings/policies
3. Assign role with **Allow members to administer Codex** only to "Codex Admin" group
4. Back "Codex Admin" group with identity provider via SCIM for auditable membership

## Step 3: Configure Local Requirements

Deploy `requirements.toml` policies from Codex [Policies page](https://chatgpt.com/codex/settings/policies) (Cloud-managed policies apply across all Codex local surfaces).

### Example Policies

**Standard local rollout** — limit web search, sandbox, approvals:
```toml
allowed_web_search_modes = ["disabled", "cached"]
allowed_sandbox_modes = ["workspace-write"]
allowed_approval_policies = ["on-request"]
```

**Disable Browser Use / in-app browser / Computer Use:**
```toml
[features]
browser_use = false
in_app_browser = false
computer_use = false
```

**Restrictive command rule:**
```toml
[rules]
prefix_rules = [
  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating remote history." },
]
```

### Policy Assignment

- Assign to user groups
- Configure default fallback policy for everyone else
- Order group rules carefully — first matching rule applies
- Treat each policy as complete for that group (no field merging from later rules)

Use policy lookup tools to confirm which managed policy applies to a user (by group or email).

For auth restrictions (login method, workspace), see [[012-auth|Authentication]].

## Step 4: Team Config

Standardize Codex across organization via `.codex/` directory in repositories. Codex auto-picks up settings.

| Type | Path | Purpose |
|------|------|---------|
| [[013-config-basic|Config basics]] | `config.toml` | Defaults: sandbox, approvals, model, reasoning |
| [[060-rules|Rules]] | `rules/` | Control commands outside sandbox |
| [[044-skills|Skills]] | `skills/` | Shared team skills |

## Step 5: Cloud Setup

### Connect Repositories

1. Go to [Codex](https://chatgpt.com/codex) → **Get started**
2. Select **Connect to GitHub** → install ChatGPT GitHub Connector
3. Choose installation target → allow target repositories

> For GitHub Enterprise Managed Users (EMU): org owner must install Codex GitHub App before users can connect repos.

### IP Allowlist

If org restricts app IPs, include [egress IP ranges](https://openai.com/chatgpt-agents.json) in allowlist. Ranges can change — consider automated checking.

### Code Review

Go to [Settings → Code review](https://chatgpt.com/codex/settings/code-review) to enable. Configure at repository level. Users can enable auto-review for their PRs. See [[026-integrations-github|GitHub Integration]] for details.

### Codex Security

[[036-security-threat-model|Scan/remediate vulnerabilities]] in connected GitHub repos. Setup guide: [[035-security-setup|Security Setup]]. Integrations: [[029-integrations-slack|Slack]], [[026-integrations-github|GitHub]], [[031-integrations-linear|Linear]].

## Step 6: Governance & Observability

| Tool | Use |
|------|-----|
| **Analytics Dashboard** | Quick self-serve visibility |
| **Analytics API** | Programmatic reporting + BI integration |
| **Compliance API** | Audit + investigation workflows |

### Analytics API Setup

1. Create secret key at [platform.openai.com](https://platform.openai.com/settings/organization/api-keys) → Read only permissions
2. Email support@openai.com to scope key to `codex.enterprise.analytics.read`
3. Find `workspace_id` in [ChatGPT Admin console](https://chatgpt.com/admin)
4. Query: `GET https://api.chatgpt.com/v1/analytics/codex/workspaces/{workspace_id}/usage|code_reviews|code_review_responses`

```bash
curl -H "Authorization: Bearer YOUR_KEY" \
  "https://api.chatgpt.com/v1/analytics/codex/workspaces/WORKSPACE_ID/usage"
```

### Compliance API Setup

1. Create key with All permissions at [platform.openai.com](https://platform.openai.com/settings/organization/api-keys)
2. Email support@openai.com with key details + scope: `read`, `delete`, or both
3. Query: `GET https://api.chatgpt.com/v1/compliance/workspaces/{workspace_id}/logs|codex_tasks|codex_environments`

```bash
curl -L -H "Authorization: Bearer YOUR_KEY" \
  "https://api.chatgpt.com/v1/compliance/workspaces/WORKSPACE_ID/logs?event_type=CODEX_LOG"
```

## Step 7: Verify Setup

- [ ] Users can sign in (ChatGPT or API key)
- [ ] RBAC + toggles produce expected access
- [ ] Managed configuration applies
- [ ] Governance data visible for admins

## Related

- [[012-auth|Authentication]]
- [[041-agent-approvals-security|Agent Approvals & Security]]
- [[018-enterprise-managed-configuration|Managed Configuration]]
- [[019-enterprise-governance|Governance]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/enterprise/admin-setup.md)*