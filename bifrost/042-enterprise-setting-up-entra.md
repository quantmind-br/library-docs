---
title: Setting up Microsoft Entra
url: https://docs.getbifrost.ai/enterprise/setting-up-entra.md
source: llms
fetched_at: 2026-01-21T19:43:32.076679269-03:00
rendered_js: false
word_count: 1569
summary: This document provides step-by-step instructions for configuring Microsoft Entra ID as an identity provider to enable Single Sign-On (SSO) and role-based access control for Bifrost Enterprise.
tags:
    - microsoft-entra-id
    - azure-ad
    - sso-authentication
    - identity-management
    - role-mapping
    - bifrost-enterprise
category: guide
---

# Setting up Microsoft Entra

> Step-by-step guide to configure Microsoft Entra ID (Azure AD) as your identity provider for Bifrost Enterprise SSO authentication.

## Overview

This guide walks you through configuring Microsoft Entra ID (formerly Azure Active Directory) as your identity provider for Bifrost Enterprise. After completing this setup, your users will be able to sign in to Bifrost using their Microsoft credentials, with roles and team memberships automatically synchronized.

## Prerequisites

* A Microsoft Azure account with access to Entra ID (Azure AD)
* Admin access to create app registrations
* Bifrost Enterprise deployed and accessible
* The redirect URI for your Bifrost instance (e.g., `https://your-bifrost-domain.com/login`)

***

## Step 1: Register an Application

1. Sign in to the [Azure Portal](https://portal.azure.com)
2. Navigate to **Microsoft Entra ID** (or **Azure Active Directory**)
3. Go to **App registrations**
4. Click **New registration**

Configure the registration:

| Field                       | Value                                                          |
| --------------------------- | -------------------------------------------------------------- |
| **Name**                    | Bifrost Enterprise                                             |
| **Supported account types** | Accounts in this organizational directory only (Single tenant) |
| **Redirect URI**            | Web: `https://your-bifrost-domain.com/login`                   |

5. Click **Register**

<Tip>
  You can add an app icon to make the application easily recognizable. The Bifrost logo is available at: [https://www.getmaxim.ai/bifrost/bifrost-logo-only.png](https://www.getmaxim.ai/bifrost/bifrost-logo-only.png)
</Tip>

6. After registration, note down the following from the **Overview** page:

<Frame>
  <img src="https://mintcdn.com/bifrost/dz99ORrLhBK1BnEd/media/user-provisioning/entra-app-information.png?fit=max&auto=format&n=dz99ORrLhBK1BnEd&q=85&s=95b12a3d0c1f1748491897cf0cda033d" alt="Entra App Registration Overview" data-og-width="4686" width="4686" data-og-height="2570" height="2570" data-path="media/user-provisioning/entra-app-information.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/dz99ORrLhBK1BnEd/media/user-provisioning/entra-app-information.png?w=280&fit=max&auto=format&n=dz99ORrLhBK1BnEd&q=85&s=1cfd8a5ab9df9a0bf4a234addb6fce73 280w, https://mintcdn.com/bifrost/dz99ORrLhBK1BnEd/media/user-provisioning/entra-app-information.png?w=560&fit=max&auto=format&n=dz99ORrLhBK1BnEd&q=85&s=f673abbfa3ae6d2a12ed74b87fcf49ad 560w, https://mintcdn.com/bifrost/dz99ORrLhBK1BnEd/media/user-provisioning/entra-app-information.png?w=840&fit=max&auto=format&n=dz99ORrLhBK1BnEd&q=85&s=22461eb900227027b70ab02879da2460 840w, https://mintcdn.com/bifrost/dz99ORrLhBK1BnEd/media/user-provisioning/entra-app-information.png?w=1100&fit=max&auto=format&n=dz99ORrLhBK1BnEd&q=85&s=5c18e70332354eea3f9db8e66f231cf8 1100w, https://mintcdn.com/bifrost/dz99ORrLhBK1BnEd/media/user-provisioning/entra-app-information.png?w=1650&fit=max&auto=format&n=dz99ORrLhBK1BnEd&q=85&s=ec44637b510ff4ccf44898baaacd4ff2 1650w, https://mintcdn.com/bifrost/dz99ORrLhBK1BnEd/media/user-provisioning/entra-app-information.png?w=2500&fit=max&auto=format&n=dz99ORrLhBK1BnEd&q=85&s=1c5672e4a12341399aa7ee6ca9121f6f 2500w" />
</Frame>

| Value                       | Where to Find         |
| --------------------------- | --------------------- |
| **Application (client) ID** | Overview → Essentials |
| **Directory (tenant) ID**   | Overview → Essentials |

***

## Step 2: Create App Roles

Configure roles in Entra that map to Bifrost's role hierarchy (Admin, Developer, Viewer).

1. In your app registration, go to **App roles**
2. Click **Create app role**
3. Create the following three roles:

<Frame>
  <img src="https://mintcdn.com/bifrost/uNN-IjBaT-ndAUVL/media/user-provisioning/entra-create-app-roles.png?fit=max&auto=format&n=uNN-IjBaT-ndAUVL&q=85&s=8452f0ab6cc3172347e9265f97f2ab70" alt="Entra App Roles configuration" data-og-width="4006" width="4006" data-og-height="2039" height="2039" data-path="media/user-provisioning/entra-create-app-roles.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/uNN-IjBaT-ndAUVL/media/user-provisioning/entra-create-app-roles.png?w=280&fit=max&auto=format&n=uNN-IjBaT-ndAUVL&q=85&s=3b747408629ce338c8b0526214432a2c 280w, https://mintcdn.com/bifrost/uNN-IjBaT-ndAUVL/media/user-provisioning/entra-create-app-roles.png?w=560&fit=max&auto=format&n=uNN-IjBaT-ndAUVL&q=85&s=ee7b494b2574e6eacc783eec46bd352f 560w, https://mintcdn.com/bifrost/uNN-IjBaT-ndAUVL/media/user-provisioning/entra-create-app-roles.png?w=840&fit=max&auto=format&n=uNN-IjBaT-ndAUVL&q=85&s=426284b162602a061c66bbb6e1ff289d 840w, https://mintcdn.com/bifrost/uNN-IjBaT-ndAUVL/media/user-provisioning/entra-create-app-roles.png?w=1100&fit=max&auto=format&n=uNN-IjBaT-ndAUVL&q=85&s=a05cb459517dacb921c1336090196faa 1100w, https://mintcdn.com/bifrost/uNN-IjBaT-ndAUVL/media/user-provisioning/entra-create-app-roles.png?w=1650&fit=max&auto=format&n=uNN-IjBaT-ndAUVL&q=85&s=f4ede174c5fc6e6257ec867fd00bb911 1650w, https://mintcdn.com/bifrost/uNN-IjBaT-ndAUVL/media/user-provisioning/entra-create-app-roles.png?w=2500&fit=max&auto=format&n=uNN-IjBaT-ndAUVL&q=85&s=79ad9453d71b8271755169b4523328de 2500w" />
</Frame>

### Viewer Role

| Field                    | Value                  |
| ------------------------ | ---------------------- |
| **Display name**         | Viewer                 |
| **Allowed member types** | Users/Groups           |
| **Value**                | `viewer`               |
| **Description**          | Viewer role on Bifrost |
| **State**                | Enabled                |

### Developer Role

| Field                    | Value                     |
| ------------------------ | ------------------------- |
| **Display name**         | Developer                 |
| **Allowed member types** | Users/Groups              |
| **Value**                | `developer`               |
| **Description**          | Developer role on Bifrost |
| **State**                | Enabled                   |

### Admin Role

| Field                    | Value                 |
| ------------------------ | --------------------- |
| **Display name**         | Admin                 |
| **Allowed member types** | Users/Groups          |
| **Value**                | `admin`               |
| **Description**          | Admin role on Bifrost |
| **State**                | Enabled               |

<Note>
  The role **Value** must be lowercase (`admin`, `developer`, `viewer`) to match Bifrost's role resolution logic. Users with multiple roles will be assigned the highest privilege role.
</Note>

***

## Step 3: Enable Assignment Required

To control which users can access Bifrost, enable assignment requirement on the Enterprise Application.

1. Go to **Enterprise applications** (from the main Entra ID menu)
2. Find and select **Bifrost Enterprise**
3. Go to **Properties**

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-enable-assignment.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=6498d6d325a8a19f2f15d03ef0a69154" alt="Entra Enterprise Application Properties" data-og-width="2896" width="2896" data-og-height="2428" height="2428" data-path="media/user-provisioning/entra-enable-assignment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-enable-assignment.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=4e157c6346e66f69e26a503c3e0b493e 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-enable-assignment.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=3aeec92d27c011413ca198d5131c01f4 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-enable-assignment.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=2a48356d4a6124a4e1be78aecfa07311 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-enable-assignment.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=653fa3c1a901e411c1b5b023a86bf251 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-enable-assignment.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=5030ac0e21d62c2543ef52309a7bdf87 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-enable-assignment.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=63eb9ea5033910459b4a60fabe002925 2500w" />
</Frame>

4. Set **Assignment required?** to **Yes**
5. Set **Enabled for users to sign-in?** to **Yes**
6. Click **Save**

***

## Step 4: Create a Client Secret

Bifrost requires a client secret for OAuth authentication.

1. Go back to **App registrations** → **Bifrost Enterprise**
2. Navigate to **Certificates & secrets**
3. Click **New client secret**

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-create-client-secret.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=38f5c6e9884fc89fefb33e63e5a3b3a8" alt="Entra Enterprise Client Secrets" data-og-width="3710" width="3710" data-og-height="1966" height="1966" data-path="media/user-provisioning/entra-create-client-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-create-client-secret.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=eeb74ae3a102a83f25d2a123ecfa74f3 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-create-client-secret.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=a34f22159045fd073f5ae363ac87e0a4 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-create-client-secret.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=2e158dabab1f110ceafc227652a56c74 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-create-client-secret.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=2231b7d7ec44d3eb0c620c1dfb60fa44 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-create-client-secret.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=158363467b6fdbe22f1ab3411c55140a 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-create-client-secret.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=5feb370503b01e3c805900cd13c30ee6 2500w" />
</Frame>

| Field           | Value                                                  |
| --------------- | ------------------------------------------------------ |
| **Description** | Bifrost Enterprise Secret                              |
| **Expires**     | Choose based on your security policy (e.g., 24 months) |

4. Click **Add**
5. **Copy the secret value immediately** - it won't be shown again!

<Warning>
  Store the client secret securely. You'll need it for the Bifrost configuration.
</Warning>

***

## Step 5: Configure API Permissions

Ensure your application has the necessary permissions.

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-api-permissions.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=56c69fa20de78dd4d412f429974e4b19" alt="Entra Enterprise API Permissions" data-og-width="3948" width="3948" data-og-height="2064" height="2064" data-path="media/user-provisioning/entra-api-permissions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-api-permissions.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=dc01b893234af0ec7f05ac6aec844d12 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-api-permissions.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=0c1f1509f412e297491bd46f48f41249 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-api-permissions.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=a8e01ded1671fa176a5053a5a184f6ae 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-api-permissions.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=b5d0a2c4f3e452df83caba6ca8c166ca 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-api-permissions.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=6c704dd5fc4da723dd8b564e09f045ae 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-api-permissions.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=34590acc528d07352992d5d5382fbc0b 2500w" />
</Frame>

1. In your app registration, go to **API permissions**

2. Click **Add a permission**

3. Select **Microsoft Graph**

4. Choose **Delegated permissions**

5. Add the following permissions:
   * `openid`
   * `profile`
   * `email`
   * `offline_access` (for refresh tokens)

6. Click **Add permissions**

7. If required by your organization, click **Grant admin consent for \[Your Organization]**

***

## Step 6: Configure Token Claims (Optional)

By default, Entra includes the `roles` claim when app roles are assigned. To include group memberships for team synchronization:

1. Go to **Token configuration**
2. Click **Add groups claim**
3. Select:
   * **Security groups** or **Groups assigned to the application**
   * For token type, enable **ID** and **Access**
4. Click **Add**

<Note>
  Group IDs from Entra will be used as team IDs in Bifrost. You may want to create groups in Entra that correspond to your teams.
</Note>

***

## Step 7: Assign Users and Roles

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-user-assignments.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=01726e04c0f87dd6a364e988bf3c867e" alt="Entra User Assignments" data-og-width="4552" width="4552" data-og-height="2574" height="2574" data-path="media/user-provisioning/entra-user-assignments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-user-assignments.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=c44c68bcae8a183a45ba041474d4f5d6 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-user-assignments.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=c6dd762b759fcdeff90893139baffb40 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-user-assignments.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=0dd901473fcddf0df5219f8610ed0272 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-user-assignments.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=8722686f9ad06801c15f0c0c52efc429 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-user-assignments.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=8b05afd044b4d96dadc4631e91e33c8c 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/entra-user-assignments.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=b8f0d08f7c9e2946ca401ae5421230b4 2500w" />
</Frame>

1. Go to **Enterprise applications** → **Bifrost Enterprise**
2. Navigate to **Users and groups**
3. Click **Add user/group**
4. Select users or groups
5. Select the appropriate role (Admin, Developer, or Viewer)
6. Click **Assign**

<Tip>
  You can assign roles to groups for easier management. All users in a group will inherit the assigned role.
</Tip>

***

## Step 8: Configure Bifrost

Now configure Bifrost to use Microsoft Entra as the identity provider.

### Using the Bifrost UI

1. Navigate to **Governance** → **User Provisioning** in your Bifrost dashboard
2. Select **Microsoft Entra** as the SCIM Provider
3. Enter the following configuration:

| Field             | Value                                            |
| ----------------- | ------------------------------------------------ |
| **Client ID**     | Application (client) ID from Azure               |
| **Tenant ID**     | Directory (tenant) ID from Azure                 |
| **Client Secret** | The secret you created in Step 4                 |
| **Audience**      | Your Client ID (optional, defaults to Client ID) |
| **App ID URI**    | `api://{client-id}` (optional, for v1.0 tokens)  |

4. Toggle **Enabled** to activate the provider
5. Click **Save Configuration**

<Warning>
  After saving, you'll need to restart your Bifrost server for the changes to take effect.
</Warning>

### Configuration Reference

| Field          | Required | Description                                           |
| -------------- | -------- | ----------------------------------------------------- |
| `tenantId`     | Yes      | Azure Directory (tenant) ID                           |
| `clientId`     | Yes      | Application (client) ID                               |
| `clientSecret` | Yes      | Client secret for OAuth authentication                |
| `audience`     | No       | JWT audience for validation (defaults to clientId)    |
| `appIdUri`     | No       | App ID URI for v1.0 tokens (e.g., `api://{clientId}`) |
| `userIdField`  | No       | JWT claim for user ID (default: `oid`)                |
| `rolesField`   | No       | JWT claim for roles (default: `roles`)                |
| `teamIdsField` | No       | JWT claim for group/team IDs (default: `groups`)      |

***

## Role Mapping

Bifrost automatically maps Entra app roles to its internal role hierarchy:

| Entra Role Value | Bifrost Role | Privilege Level |
| ---------------- | ------------ | --------------- |
| `admin`          | Admin        | Highest         |
| `developer`      | Developer    | Medium          |
| `viewer`         | Viewer       | Lowest          |

**Multiple Roles:** If a user has multiple roles assigned, Bifrost automatically selects the highest privilege role. For example, a user with both `viewer` and `developer` roles will be assigned the Developer role in Bifrost.

**Default Role:** Users without any assigned role will default to the Viewer role.

***

## Testing the Integration

1. Open your Bifrost dashboard in a new browser or incognito window
2. You should be redirected to Microsoft login
3. Log in with an assigned user
4. After successful authentication, you'll be redirected back to Bifrost
5. Verify the user appears in the Bifrost users list with the correct role

***

## Troubleshooting

### User not redirected to Microsoft login

* Verify the SCIM provider is enabled in Bifrost
* Check that the Bifrost server was restarted after configuration
* Ensure the Tenant ID and Client ID are correct

### "AADSTS50011: The reply URL does not match"

* Verify the redirect URI in your app registration exactly matches your Bifrost login URL
* Ensure there are no trailing slashes or protocol mismatches (http vs https)

### "AADSTS7000215: Invalid client secret"

* Regenerate the client secret in Azure
* Ensure you're using the secret **Value**, not the secret ID
* Check for any leading/trailing whitespace when copying

### Roles not appearing in token

* Ensure users are assigned to the Enterprise Application with a role
* Verify app roles are created with the correct lowercase values
* Check that "Assignment required" is enabled

### "AADSTS70011: The provided request includes an invalid scope"

* This usually happens when mixing `.default` scope with other scopes
* Bifrost handles this automatically - ensure you're using the latest version

### Groups not syncing as teams

* Verify the groups claim is configured in Token configuration
* Ensure users are members of the groups
* Check that groups are created and assigned in Entra

### Token validation errors

* Ensure the Tenant ID matches your Azure directory
* Verify the Client ID is correct
* Check that the app registration is in the same tenant as your users

***

## Next Steps

* **[Advanced Governance](./advanced-governance)** - Learn about user budgets and compliance features
* **[Role-Based Access Control](./advanced-governance#role-hierarchy)** - Understand the Admin, Developer, Viewer hierarchy
* **[Audit Logs](./audit-logs)** - Monitor user authentication and activity


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt