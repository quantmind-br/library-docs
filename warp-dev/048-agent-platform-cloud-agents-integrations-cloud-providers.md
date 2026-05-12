---
title: AWS, GCP, and other cloud providers | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/integrations/cloud-providers
source: sitemap
fetched_at: 2026-04-29T15:04:34.008616522-03:00
rendered_js: false
word_count: 711
summary: This document provides instructions for configuring Oz cloud agents to securely authenticate with AWS and GCP using OpenID Connect (OIDC) identity federation.
tags:
    - cloud-agents
    - openid-connect
    - oidc
    - iam
    - aws-federation
    - gcp-workload-identity
    - authentication
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Oz cloud agents can securely access cloud providers using short-lived OpenID Connect credentials. Oz has built-in support for AWS and GCP, and works with any provider that supports OIDC tokens.

## Prerequisites

- A cloud provider account

---

## AWS

### Step 1: Create an OIDC identity provider

Configure your AWS account to trust OIDC tokens produced by Oz.

1. In IAM, click **Identity Providers** > **Add provider**
2. Set type to **OpenID Connect**
3. Set **Provider URL** to `https://app.warp.dev`
4. Set **Audience** to `sts.amazonaws.com`
5. Copy the provider ARN: `arn:aws:iam::<account-id>:oidc-provider/app.warp.dev`

> [!note]
> Verify the provider was created correctly by checking the endpoint verification thumbprint: `08745487e891c19e3078c1f2a07e452950ef36f6`

### Step 2: Configure an IAM role

Set up an AWS IAM role with a trust policy linking to the OIDC provider.

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "Federated": "<oidc-provider-arn>" },
    "Action": "sts:AssumeRoleWithWebIdentity",
    "Condition": {
      "StringLike": { "app.warp.dev:sub": "scoped_principal:<team-uid>/*" }
    }
  }]
}
```

Replace:
- `<oidc-provider-arn>` — ARN from Step 1
- `<team-uid>` — last component of your [[145-knowledge-and-collaboration-admin-panel|Admin Panel]] URL (e.g., `abc123def456` from `app.warp.dev/admin/abc123def456`)

The `StringLike` pattern allows any user or automation on your team to assume the role.

To restrict to a specific user, use `StringEquals` with the fully qualified subject:

```json
"StringEquals": { "app.warp.dev:sub": "scoped_principal:xyz789/user:abc123def456" }
```

To allow multiple specific principals:

```json
"StringEquals": {
  "app.warp.dev:sub": [
    "scoped_principal:xyz789/user:abc123def456",
    "scoped_principal:xyz789/service_account:abc123def456"
  ]
}
```

1. Click **Next** and add permissions policies
2. Enter a role name and optional description
3. Click **Create role** and note the role ARN: `arn:aws:iam::<account-id>:role/<role-name>`

### Step 3: Enable AWS federation in your cloud agent environment

1. Create or edit an environment. See [[055-agent-platform-cloud-agents-environments|Environments]]
2. Expand the **AWS** section and enter the role ARN from Step 2
3. Save

> [!warning]
> Currently, AWS federation can only be configured in the Oz web app, not the CLI.

Agents running in this environment automatically assume the configured role when using the `aws` CLI or compatible SDK.

Oz uses **Assume role with web identity** and sets these environment variables:

| Variable | Description |
|----------|-------------|
| `AWS_ROLE_ARN` | ARN of the configured role |
| `AWS_WEB_IDENTITY_TOKEN_FILE` | Path to temporary file with agent's Oz OIDC token |
| `AWS_ROLE_SESSION_NAME` | Derived session name (`Oz_Run_<run-id>`) |

---

## GCP

### Step 1: Create a Workload Identity Pool and Provider

The Oz GCP integration uses [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).

Create a pool:

```bash
gcloud iam workload-identity-pools create <pool-id> \
  --location="global" \
  --description="Oz agent pool"
```

Create a provider within the pool:

```bash
gcloud iam workload-identity-pools providers create <provider-id> \
  --workload-identity-pool=<pool-id> \
  --location="global" \
  --issuer-uri="https://app.warp.dev" \
  --attribute-mapping="google.subject=assertion.sub,attribute.team=assertion.teams[0]"
```

Add an attribute condition to restrict access:

```bash
--attribute-condition="assertion.teams.contains('<team-uid>')"
```

> [!warning]
> If you do not set an attribute condition, **any** Oz agent can use your Workload Identity Federation provider.

### Step 2: Configure IAM policies

Allow Oz agents in the pool to access resources:

```bash
gcloud projects add-iam-policy-binding <project-id> \
  --member="principal://Oz_Run_<run-id>" \
  --role="roles/compute.viewer"
```

See [Workload Identity Federation principal types](https://docs.cloud.google.com/iam/docs/workload-identity-federation#principal-types) for full syntax.

### Step 3: Enable Workload Identity Federation in your environment

1. Create or edit an environment
2. Expand the **GCP** section and enter the project number, pool ID, and provider ID
3. Save

> [!warning]
> Currently, Workload Identity Federation can only be configured in the Oz web app, not the CLI.

Agents automatically configure Application Default Credentials to use the configured pool. Both `GOOGLE_APPLICATION_CREDENTIALS` and `CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE` are set.

---

## Other providers

To authenticate to providers supporting OIDC federation, issue tokens directly:

```bash
oz federate issue-token --audience <provider-endpoint>
```

Optionally add `--duration <duration>` to customize token validity (cannot exceed maximum agent runtime).

Exchange this token for provider-specific credentials.

---

## OIDC token claims

All Oz OIDC tokens include standard claims (`iss`, `iat`) plus:

### Audience (`aud`)

- **AWS:** always `sts.amazonaws.com`
- **GCP:** derived from Workload Identity Federation provider

### Subject (`sub`)

Format: `<principal-type>:<principal-id>`

| Format | Meaning |
|--------|---------|
| `user:abc123def456` | User with ID `abc123def456` |
| `service_account:abc123def456` | Autogenerated team account |

**AWS format** (because AWS trust policies can't match custom OIDC claims):

| Format | Meaning |
|--------|---------|
| `scoped_principal:xyz789/user:abc123def456` | User `abc123def456` on team `xyz789` |
| `scoped_principal:user:abc123def456` | User not on any team |
| `scoped_principal:xyz789/service_account:abc123def456` | Autogenerated account for team `xyz789` |

User tokens also include an `email` claim.

To get user ID values:

```bash
oz whoami
```

Or check past runs via the Oz API.

### Team

Token includes `teams` claim with your team UID (list with single value).

### Oz run

Derived from the agent run:

| Claim | Description |
|-------|-------------|
| `run_id` | Unique identifier for the individual run |
| `environment` | Unique identifier for the agent's [[055-agent-platform-cloud-agents-environments|Environment]] |
| `agent_name` | Name of the [[061-agent-platform-cloud-agents-skills-as-agents|Skill]] invoked |
| `skill_spec` | Canonical identifier (e.g., `github-org/github-repo:.warp/skills/skill-name/SKILL.md`) |
| `host` | `warp` for Warp-hosted, or worker ID for [[210-agent-platform-cloud-agents-self-hosting|self-hosted]] |

### Example token

```json
{
  "iss": "app.warp.dev",
  "aud": "sts.amazonaws.com",
  "sub": "scoped_principal:xyz789/user:abc123def456",
  "email": "user@example.com",
  "teams": ["xyz789"],
  "run_id": "run_abc123",
  "environment": "env_def456",
  "agent_name": "code-review",
  "skill_spec": "github-org/github-repo:.warp/skills/code-review/SKILL.md",
  "host": "warp"
}
``` #cloud-agents #oidc #authentication