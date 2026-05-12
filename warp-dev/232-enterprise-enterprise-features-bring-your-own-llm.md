---
title: Bring your own LLM | Enterprise | Warp
url: https://docs.warp.dev/enterprise/enterprise-features/bring-your-own-llm
source: sitemap
fetched_at: 2026-04-29T15:06:07.788927721-03:00
rendered_js: false
word_count: 974
summary: This document explains how enterprise teams can route LLM inference requests from Warp agents through their own AWS Bedrock infrastructure to maintain control over billing, security, and data usage.
tags:
    - byollm
    - aws-bedrock
    - enterprise-security
    - inference-routing
    - iam-authentication
    - cloud-infrastructure
category: configuration
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp supports **Bring Your Own LLM (BYOLLM)** for enterprise teams that need to run inference on their own cloud infrastructure. Route inference through models hosted in your AWS Bedrock environment while keeping your team workflow unchanged.

> [!warning]
> BYOLLM currently supports **AWS Bedrock** only. Azure Foundry and Google Vertex support coming soon.
> BYOLLM applies to interactive Oz agents in the terminal. Oz cloud agents do not yet support BYOLLM routing.

## Key features

- **Cloud-native credentials** — Authenticate using each user's AWS IAM identity. No API key storage.
- **Admin-enforced routing** — Team admins configure available models and can disable non-Bedrock access entirely.
- **Consolidated billing** — Inference costs billed directly to your AWS account.

## How BYOLLM works

1. **Admin configures routing** — Set policies in Warp's admin settings (e.g., "Route Claude Sonnet 4.5 through AWS Bedrock").
2. **Team members authenticate** — Each member authenticates to AWS locally via AWS CLI (`aws login`).
3. **Warp routes requests** — Warp uses short-lived session credentials to authenticate to your AWS Bedrock endpoint.
4. **Inference executes in your cloud** — Model runs in your AWS account. Responses return to Warp client.

### Credential lifecycle

BYOLLM uses cloud-native IAM authentication:

- **Automatic refresh** — Session tokens refresh every ~15 minutes. Enable auto-refresh via **Settings** → search `AWS Bedrock`. Sessions can run up to 12 hours.
- **Per-user credentials** — Not shared across org; AWS CLI credential provider chain provisions them.
- **No storage or logging** — Warp never stores or logs cloud session tokens on its servers.

### Model availability

Only **Claude models** are available through AWS Bedrock. OpenAI and Google models are not on Bedrock. A model must appear on both Warp's supported list and Bedrock's list.

## Enabling BYOLLM

### Prerequisites

- Desired models enabled in AWS Bedrock.
- Admin access to Warp's [Admin Panel](https://docs.warp.dev/enterprise/team-management/admin-panel) and AWS IAM settings.
- AWS CLI installed locally for team members.

### Step 1: Configure routing policies (admin)

1. From the [Admin Panel](https://docs.warp.dev/enterprise/team-management/admin-panel), navigate to BYOLLM or model routing settings.
2. Select models to route through your cloud provider.
3. Optionally disable direct API access to enforce provider-only routing.

### Step 2: Provision IAM roles (cloud admin)

Grant team members necessary permissions using least-privilege IAM policies.

**Example: AWS Bedrock minimum IAM policy**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithConversationTrace"
      ],
      "Resource": [
        "arn:aws:bedrock:*:assistant-runtime:*",
        "arn:aws:bedrock:*:inference-profile:*"
      ]
    }
  ]
}
```

> [!info]
> This policy covers Warp's current usage. Warp uses global inference profiles when available.

### Step 3: Authenticate locally (team member)

Each team member authenticates to AWS using the AWS CLI:

```bash
aws login
```

> [!warning]
> Confirm your AWS environment and region are correctly configured before using Warp.

### Step 4: Validate

Run a test prompt using a model configured for BYOLLM routing. Verify the request completes successfully and logs appear in AWS CloudWatch.

## BYOLLM usage and billing behavior

### Billing

- Warp **does not consume credits** for BYOLLM-routed requests.
- Cloud provider account receives inference costs directly.

### Routing behavior

Warp's agents select the best model while respecting admin routing policies. Configured BYOLLM models route to AWS Bedrock.

### Failover behavior

If a BYOLLM request fails (expired credentials, insufficient permissions, quota limits), Warp attempts to fall back to the next enabled model.

- If a fallback uses direct API, that request consumes Warp credits.
- If no fallback is available, Warp displays a clear error message.

## Security and data handling

### Credential security

- **No long-lived API keys** — Uses cloud-native IAM with short-lived session tokens.
- **Per-user authentication** — Each member authenticates individually.
- **No storage or logging** — Warp never stores or logs cloud session tokens.

### Zero Data Retention (ZDR)

- Warp maintains SOC 2 compliance and has ZDR agreements with contracted LLM providers.
- When using BYOLLM, **your** cloud account settings determine data retention policies.
- Warp cannot enforce ZDR for requests routed through your infrastructure.

### Auditability

- Warp keeps all runs fully steerable and logged within Warp.
- Cloud account retains provider-side logs (usage, latency, errors).

## Troubleshooting

### Common errors

| Error | Solution |
|-------|----------|
| Missing or expired credentials | Re-authenticate with `aws login`. Enable auto-refresh via Settings → AWS Bedrock. |
| Insufficient permissions | Verify IAM policy includes required actions and resources. |
| Region or model mismatch | Confirm model enabled in your AWS region and environment configured for correct region. |
| Provider quota limits | Check AWS Bedrock quota and request increases if needed. |

### Debugging steps

1. Verify local authentication: `aws sts get-caller-identity`
2. Check effective IAM policy for required permissions.
3. Confirm model ID and region match Warp configuration.
4. Inspect AWS CloudWatch logs for request details and errors.

## FAQ

### How is BYOLLM different from BYOK?

**BYOK (Bring Your Own Key)** — Individual users add their own API keys for direct model provider access. Warp stores keys locally on the user's device.

**BYOLLM (Bring Your Own LLM)** — Routes inference through your organization's cloud infrastructure (AWS Bedrock) using cloud-native IAM. Admins configure at admin level, applies to entire team.

### Does BYOLLM work with Auto model selection?

Auto model selection is disabled when your admin disables **any** Direct API model.

If all Direct API models remain enabled and BYOLLM is configured, Auto tries enabled AWS Bedrock models first, falling back to Direct API only if Bedrock fails.

### Where does compute run and who pays?

Inference runs in **your AWS account**. You pay AWS directly. Warp does not consume credits for BYOLLM-routed requests.

### What data does Warp store?

Warp **does not store or log** your cloud session tokens. Credentials are used transiently and never persisted on Warp servers.

Warp stores standard run metadata (timestamps, model used, etc.) but does not retain prompt/response content when using BYOLLM.

### Can admins enforce provider-only routing?

Yes. Admins can configure routing policies to require specific models use BYOLLM and disable direct API access.

#byollm #aws-bedrock #enterprise-security
