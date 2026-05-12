---
title: Security overview | Enterprise | Warp
url: https://docs.warp.dev/enterprise/security-and-compliance/security-overview
source: sitemap
fetched_at: 2026-04-29T15:06:03.515169692-03:00
rendered_js: false
word_count: 1133
summary: This document provides a comprehensive overview of Warp's security architecture, data handling practices, compliance certifications, and administrative controls for enterprise teams.
tags:
    - security-compliance
    - data-privacy
    - zero-data-retention
    - soc-2-compliance
    - telemetry-settings
    - enterprise-security
    - secret-redaction
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp builds security and compliance into its core, keeping **developers in control** while enabling powerful agent workflows.

## Transparency and control

- **Real-time monitoring** — use Warp's [Network Log](https://docs.warp.dev/support-and-community/privacy-and-security/network-log) to monitor all network requests in real time
- **Opt-out controls** — disable telemetry and crash reporting at any time while retaining full functionality
- **Team-level enforcement** — admins can configure telemetry and data collection policies for the entire organization

---

## Telemetry and data collection

### Zero Data Retention (ZDR)

Warp has **Zero Data Retention (ZDR)** agreements with contracted LLM providers (Anthropic, OpenAI, Google)—they do not store or train on your data. ZDR applies across all Warp plans.

| Plan | Data collection default | Team enforcement |
|------|------------------------|------------------|
| Free tier | User-controlled (disable in **Settings** > **Privacy**) | Not available |
| Paid teams | Enabled by default | Team admins can enforce |
| Business and Enterprise | **Disabled by default** | Team admins can enforce |

> [!note]
> Some product features—cloud conversations and Oz runs—require storing conversation data to function. This is separate from analytics or telemetry data collection.

Enterprise subscriptions also include team-level enforcement and [secret redaction](https://docs.warp.dev/support-and-community/privacy-and-security/secret-redaction).

### Telemetry categories

When enabled, Warp collects:
1. **Product usage analytics** — feature adoption and usage patterns (e.g., "Agent Mode was opened")
2. **Performance and stability** — crash reports, error tracking, performance metrics

When disabled, Warp does not collect personally identifiable information beyond user IDs and email addresses, or network traffic/external API calls.

### Disabling telemetry

**Individual users:**
1. Navigate to **Settings** > **Privacy**
2. Toggle off **Help improve Warp** and/or **Send crash reports**

**Team admins:** Enforce telemetry settings organization-wide through the Admin Panel.

---

## Data handling and privacy

### Where your data lives

| Data type | Location |
|-----------|----------|
| Code and files | On your machine unless you explicitly use transmitting features |
| Codebase Context | Sent to Warp's servers for embeddings; raw code not stored |
| Agent requests | Sent to contracted LLM providers with ZDR agreements |
| BYOLLM | Proxied through Warp's servers; inference runs in your cloud infrastructure |

### Encryption

- **In transit** — TLS 1.2 or higher
- **At rest** — AES-256

### Secret redaction

Warp automatically detects and redacts sensitive information before sending data to LLM providers:
- API keys and tokens
- Passwords and secrets
- SSH keys and certificates
- Custom secret patterns (configurable via Admin Panel)

See [Secret Redaction documentation](https://docs.warp.dev/support-and-community/privacy-and-security/secret-redaction).

### Data retention

- **ZDR** — contracted LLM providers do not retain or train on your data
- **Telemetry data** — retained indefinitely for analytics and debugging when collected
- **User accounts** — deletion requests processed securely within 30 days

---

## Compliance and certifications

### SOC 2 Type II

Warp is SOC 2 Type II certified, demonstrating compliance with industry-standard security controls for:
- **Security** — infrastructure protection, access controls, monitoring
- **Availability** — system uptime and disaster recovery
- **Confidentiality** — data protection and privacy controls
- **Processing integrity** — accurate, complete, authorized processing

SOC 2 reports available to Enterprise customers upon request.

---

## Infrastructure security

### Warp-hosted infrastructure

- **Cloud provider** — hosted on GCP with SOC 2 and ISO 27001 certified datacenters
- **Network isolation** — workloads run in isolated VPCs with strict network policies

### Self-hosted deployments

Enterprise teams can self-host Oz cloud agent execution to control where agents run and keep repositories on their own infrastructure.

**Architecture:**
- **Execution plane (customer-hosted)** — repository clones, build artifacts, runtime secrets, and container filesystem state stay on your infrastructure
- **Control plane (Warp-hosted)** — session transcripts, orchestration metadata, and LLM inference route through Warp's servers under ZDR agreements. Warp does not persistently store source code or use it for training

**Deployment modes:**
| Mode | Description |
|------|-------------|
| **Unmanaged** | Use `oz agent run` in your existing orchestrator or CI environment (Linux, macOS, Windows; no Docker dependency) |
| **Managed** | Run `oz-agent-worker` daemon for Oz platform orchestration in isolated Docker containers on your infrastructure |

Both modes require outbound access to Warp's backend services; managed architecture also requires Docker Hub and GitHub.

---

## Access controls and authentication

### Single Sign-On (SSO)

Supports SSO via Okta, Microsoft Entra ID, Google Workspace, OneLogin, and any SAML 2.0 or OpenID Connect (OIDC) compatible provider. Admins can require SSO and enforce MFA through your identity provider.

See [Single Sign-On (SSO)](https://docs.warp.dev/enterprise/security-and-compliance/sso) for setup instructions, SCIM provisioning, and troubleshooting.

### Team permissions

Role-based access control with three roles: Team Owner, Team Admin, and Member. See [User roles and permissions](https://docs.warp.dev/enterprise/getting-started/getting-started-enterprise#user-roles-and-permissions).

Resource sharing in Warp Drive has granular controls for who can view, edit, and share.

### Admin Panel governance

Security-relevant controls include:
- **Privacy** — UGC data collection, cloud conversation storage, enterprise secret redaction
- **Sharing** — direct link sharing restrictions
- **AI** — AI autonomy settings and agent behavior
- **Models** — LLM model availability including AWS Bedrock
- **Platform** — Oz cloud agent access and settings

Settings can be **enforced** (overriding individual preferences) or **respect user setting** (deferring to individual preferences).

---

## Security features for developers

### Bring Your Own LLM (BYOLLM)

Route agent inference through your own cloud infrastructure:
- **Data locality** — inference runs in your AWS account
- **Cloud-native IAM** — authenticate using your existing identity and access management
- **No key storage** — Warp never stores your cloud credentials or API keys
- **Billing control** — inference costs billed directly to your cloud account

See [Bring Your Own LLM](https://docs.warp.dev/enterprise/enterprise-features/bring-your-own-llm).

### Docker Sandboxes

Isolate agent execution in containerized environments:
- **Process isolation** — agents run in separate Docker containers
- **Resource limits** — configure CPU, memory, and disk quotas per sandbox
- **Network controls** — restrict outbound network access
- **Ephemeral environments** — sandboxes destroyed after use

### Agent permissions

Configure what agents can access and execute:
- **Tool restrictions** — enable/disable terminal, code editing, web search, file system access
- **Repository scoping** — limit agents to specific repositories or directories
- **Execution approvals** — require manual approval for sensitive commands
- **Visibility** — agent actions logged with full context when cloud conversation storage is enabled

---

## Incident response and support

### Security issue reporting

1. Include detailed steps to reproduce
2. Do not publicly disclose until Warp has addressed the issue

Warp follows responsible disclosure practices.

### Enterprise support

- **Dedicated channels** — private Slack/Teams channels for security questions
- **Security advisories** — proactive notifications of security updates
- **Incident assistance** — support during security incidents or breach investigations
- **Compliance assistance** — help with compliance questionnaires and audits

---

## Additional resources

- **Trust center** — [trust.warp.dev](https://trust.warp.dev) — security documentation and compliance reports

> [!info]
> For vendor security assessments, compliance questionnaires, or access to SOC 2 reports, contact your account manager or email [security@warp.dev](mailto:security@warp.dev).
