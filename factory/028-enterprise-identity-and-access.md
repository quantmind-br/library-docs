---
title: Identity & Access Management - Factory Documentation
url: https://docs.factory.ai/enterprise/identity-and-access
source: sitemap
fetched_at: 2026-01-13T19:04:02.422976164-03:00
rendered_js: false
word_count: 438
summary: Explains the identity and access management model for Droid, covering SSO integration, role-based permissions for administrators and developers, and how identity controls configuration policies and audit telemetry.
tags:
    - iam
    - rbac
    - sso
    - scim
    - identity-provider
    - access-control
    - security
    - telemetry
category: concept
---

Identity and access management controls **who can run Droid**, in which environments, and under what policies. This page provides an overview of the identity model, roles, and environments; detailed SSO and SCIM setup instructions live in [SSO, IdP & SCIM Provisioning](https://docs.factory.ai/enterprise/identity-sso-and-scim).

* * *

## Identity model

Every Droid run is associated with three dimensions of identity:

* * *

## Org identity and SSO (overview)

Most enterprises integrate Factory with an identity provider (IdP) such as **Okta, Azure AD, or Google Workspace**. At a high level:

- **Org membership** is derived from IdP groups mapped to Factory organizations and teams.
- **SSO sign‑in** gives developers access to both the web platform and Droid using corporate credentials.
- **Role information** (for example, `Owner`, `Admin`, `User`) flows from IdP groups into Factory roles.

For step‑by‑step SSO and SCIM configuration—including setting up the IdP application, mapping attributes, and enabling provisioning—see [SSO, IdP & SCIM Provisioning](https://docs.factory.ai/enterprise/identity-sso-and-scim).

* * *

## Role‑based access control (RBAC)

Factory distinguishes between three broad classes of actors:

- **Org administrators**
  
  - Define org‑level `.factory` configuration, including model policies, global command allow/deny lists, and default telemetry targets.
  - Decide which deployment patterns (cloud, hybrid, airgapped) are supported and where Droid binaries may run.
  - Configure security features such as maximum autonomy level and whether user‑supplied BYOK keys are allowed.
- **Project owners / maintainers**
  
  - Own project‑level `.factory/` folders that live in version control.
  - Provide team‑specific models, droids, commands, and hooks that extend org policy without weakening it.
  - Configure project‑specific policies, for example limiting Droid to certain repositories or directories.
- **Developers**
  
  - Customize personal preferences in `~/.factory/` (for example, default model choice within the allowed set).
  - Run Droid locally, in IDEs, or via team‑provided scripts and CI jobs.
  - Cannot override any setting defined at org or project level.

Role assignment flows from your IdP into Factory; the **hierarchical settings engine** enforces what each role can effectively change. See [Hierarchical Settings & Org Control](https://docs.factory.ai/enterprise/hierarchical-settings-and-org-control) for the exact precedence rules.

* * *

## Devices, environments, and workspace trust

Because Droid is a CLI, it can run in many environments:

- Developer laptops (macOS, Linux, Windows)
- Remote dev servers or workspaces
- CI runners and build agents
- Hardened VMs and devcontainers

Enterprise customers typically combine Droid with **endpoint management** and **workspace trust** controls:

* * *

## How identity flows into policy and telemetry

Identity and environment information are used in two main ways:

1. **Policy evaluation** – hierarchical settings (org → project → folder → user) use identity to determine which configuration bundle applies to a given run.
2. **Telemetry and audit** – Droid emits OTEL metrics, traces, and logs with attributes like `user.id`, `team.id`, `session.id`, and environment tags so you can build per‑org and per‑team dashboards.

For details on how these identities are encoded in telemetry, see [Compliance, Audit & Monitoring](https://docs.factory.ai/enterprise/compliance-audit-and-monitoring).