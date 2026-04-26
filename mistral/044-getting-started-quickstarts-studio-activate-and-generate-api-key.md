---
title: Activate Studio and generate an API key | Mistral Docs
url: https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key
source: sitemap
fetched_at: 2026-04-26T04:07:24.969026093-03:00
rendered_js: false
word_count: 369
summary: This document provides a step-by-step guide for setting up a Mistral account, activating the free Experiment plan, creating a workspace, and generating a secure API key.
tags:
    - mistral-api
    - api-key-setup
    - account-configuration
    - workspace-management
    - getting-started
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Set up your [Studio](https://console.mistral.ai) account, activate the free Experiment plan, and create an API key to call Mistral models.

**What you get:**
- **Experiment plan**: free API access, no credit card required
- **Workspace-scoped keys**: API keys tied to a workspace for usage tracking and access control
- **Secure key management**: set expiration dates and rotate keys regularly

**Time to complete:** ~10 minutes

**Prerequisites:**
- [Mistral account](https://console.mistral.ai)
- Phone number for verification (one per Experiment plan)

## Step 1: Activate Experiment Plan

1. Go to the [Admin Subscriptions page](https://admin.mistral.ai/subscriptions).
2. Click **Experiment for free**.

![Click Experiment for free to start your plan](https://docs.mistral.ai/assets/quickstarts/studio/experiment-plan-button.png)

3. Review the plan details, accept the Terms of Service and Privacy Policy, then click **Subscribe**.
4. Verify your phone number when prompted.

> [!note]
> You can upgrade to the Scale plan at any time for higher rate limits and frontier model access.
> Experiment plan requests may be used to improve Mistral models. Review the data training policy.

## Step 2: Create a Workspace

Workspaces organize API keys, usage reports, and team access. Each API key belongs to a specific workspace.

1. Open the [Studio console](https://console.mistral.ai).
2. Navigate to **Workspaces** in the left sidebar.
3. Click **Create workspace**.
4. Enter a name (e.g., "Development" or "Production").
5. Click **Create**.

## Step 3: Generate an API Key

1. Open your workspace settings → select the **API Keys** tab.
2. Click **Create new key**.

![Click Create new key](https://docs.mistral.ai/assets/quickstarts/studio/new-key-button.png)

3. Add a **Name** to identify the key (e.g., "First test key").
4. Set an **Expiration** date. Regular rotation improves security.

![Configure the API key with optional name and expiration date](https://docs.mistral.ai/assets/quickstarts/studio/new-key-modal.png)

5. Click **Create new key**.
6. Copy the key immediately and store it in a secure location (password manager or secrets vault).

> [!warning]
> The full key appears only once. You cannot retrieve it after closing the confirmation dialog.

## Test Your Key

```bash
curl -E /path/to/your/certificate.crt \
  --cacert /path/to/your/ca.crt \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  https://api.mistral.ai/v1/models
```

A successful response confirms your key is working.

#mistral-api #api-key-setup #workspace-management