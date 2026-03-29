---
title: 'Microsoft SSO: Sync Groups, Members with LiteLLM | liteLLM'
url: https://docs.litellm.ai/docs/tutorials/msft_sso
source: sitemap
fetched_at: 2026-01-21T19:55:40.877339466-03:00
rendered_js: false
word_count: 1080
summary: This document provides instructions for synchronizing Microsoft Entra ID groups and memberships with LiteLLM teams to automate user provisioning and role-based access control. It covers auto-creating teams, syncing members during SSO sign-in, and configuring default parameters for new teams.
tags:
    - microsoft-entra-id
    - azure-ad
    - sso-integration
    - user-provisioning
    - team-sync
    - role-based-access-control
category: tutorial
---

Sync Microsoft SSO Groups, Members with LiteLLM Teams.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- An Azure Entra ID account with administrative access
- A LiteLLM Enterprise App set up in your Azure Portal
- Access to Microsoft Entra ID (Azure AD)

## Overview of this tutorial[​](#overview-of-this-tutorial "Direct link to Overview of this tutorial")

1. Auto-Create Entra ID Groups on LiteLLM Teams
2. Sync Entra ID Team Memberships
3. Set default params for new teams and users auto-created on LiteLLM

## 1. Auto-Create Entra ID Groups on LiteLLM Teams[​](#1-auto-create-entra-id-groups-on-litellm-teams "Direct link to 1. Auto-Create Entra ID Groups on LiteLLM Teams")

In this step, our goal is to have LiteLLM automatically create a new team on the LiteLLM DB when there is a new Group Added to the LiteLLM Enterprise App on Azure Entra ID.

### 1.1 Create a new group in Entra ID[​](#11-create-a-new-group-in-entra-id "Direct link to 1.1 Create a new group in Entra ID")

Navigate to [your Azure Portal](https://portal.azure.com/) &gt; Groups &gt; New Group. Create a new group.

### 1.2 Assign the group to your LiteLLM Enterprise App[​](#12-assign-the-group-to-your-litellm-enterprise-app "Direct link to 1.2 Assign the group to your LiteLLM Enterprise App")

On your Azure Portal, navigate to `Enterprise Applications` &gt; Select your litellm app

Once you've selected your litellm app, click on `Users and Groups` &gt; `Add user/group`

Now select the group you created in step 1.1. And add it to the LiteLLM Enterprise App. At this point we have added `Production LLM Evals Group` to the LiteLLM Enterprise App. The next steps is having LiteLLM automatically create the `Production LLM Evals Group` on the LiteLLM DB when a new user signs in.

### 1.3 Sign in to LiteLLM UI via SSO[​](#13-sign-in-to-litellm-ui-via-sso "Direct link to 1.3 Sign in to LiteLLM UI via SSO")

Sign into the LiteLLM UI via SSO. You should be redirected to the Entra ID SSO page. This SSO sign in flow will trigger LiteLLM to fetch the latest Groups and Members from Azure Entra ID.

### 1.4 Check the new team on LiteLLM UI[​](#14-check-the-new-team-on-litellm-ui "Direct link to 1.4 Check the new team on LiteLLM UI")

On the LiteLLM UI, Navigate to `Teams`, You should see the new team `Production LLM Evals Group` auto-created on LiteLLM.

#### How this works[​](#how-this-works "Direct link to How this works")

When a SSO user signs in to LiteLLM:

- LiteLLM automatically fetches the Groups under the LiteLLM Enterprise App
- It finds the Production LLM Evals Group assigned to the LiteLLM Enterprise App
- LiteLLM checks if this group's ID exists in the LiteLLM Teams Table
- Since the ID doesn't exist, LiteLLM automatically creates a new team with:
  
  - Name: Production LLM Evals Group
  - ID: Same as the Entra ID group's ID

## 2. Sync Entra ID Team Memberships[​](#2-sync-entra-id-team-memberships "Direct link to 2. Sync Entra ID Team Memberships")

In this step, we will have LiteLLM automatically add a user to the `Production LLM Evals` Team on the LiteLLM DB when a new user is added to the `Production LLM Evals` Group in Entra ID.

### 2.1 Navigate to the `Production LLM Evals` Group in Entra ID[​](#21-navigate-to-the-production-llm-evals-group-in-entra-id "Direct link to 21-navigate-to-the-production-llm-evals-group-in-entra-id")

Navigate to the `Production LLM Evals` Group in Entra ID.

### 2.2 Add a member to the group in Entra ID[​](#22-add-a-member-to-the-group-in-entra-id "Direct link to 2.2 Add a member to the group in Entra ID")

Select `Members` &gt; `Add members`

In this stage you should add the user you want to add to the `Production LLM Evals` Team.

### 2.3 Sign in as the new user on LiteLLM UI[​](#23-sign-in-as-the-new-user-on-litellm-ui "Direct link to 2.3 Sign in as the new user on LiteLLM UI")

Sign in as the new user on LiteLLM UI. You should be redirected to the Entra ID SSO page. This SSO sign in flow will trigger LiteLLM to fetch the latest Groups and Members from Azure Entra ID. During this step LiteLLM sync it's teams, team members with what is available from Entra ID

### 2.4 Check the team membership on LiteLLM UI[​](#24-check-the-team-membership-on-litellm-ui "Direct link to 2.4 Check the team membership on LiteLLM UI")

On the LiteLLM UI, Navigate to `Teams`, You should see the new team `Production LLM Evals Group`. Since your are now a member of the `Production LLM Evals Group` in Entra ID, you should see the new team `Production LLM Evals Group` on the LiteLLM UI.

## 3. Set default params for new teams auto-created on LiteLLM[​](#3-set-default-params-for-new-teams-auto-created-on-litellm "Direct link to 3. Set default params for new teams auto-created on LiteLLM")

Since litellm auto creates a new team on the LiteLLM DB when there is a new Group Added to the LiteLLM Enterprise App on Azure Entra ID, we can set default params for new teams created.

This allows you to set a default budget, models, etc for new teams created.

### 3.1 Set `default_team_params` on litellm[​](#31-set-default_team_params-on-litellm "Direct link to 31-set-default_team_params-on-litellm")

Navigate to your litellm config file and set the following params

litellm config with default\_team\_params

```
litellm_settings:
default_team_params:# Default Params to apply when litellm auto creates a team from SSO IDP provider
max_budget:100# Optional[float], optional): $100 budget for the team
budget_duration: 30d           # Optional[str], optional): 30 days budget_duration for the team
models:["gpt-3.5-turbo"]# Optional[List[str]], optional): models to be used by the team
```

### 3.2 Auto-create a new team on LiteLLM[​](#32-auto-create-a-new-team-on-litellm "Direct link to 3.2 Auto-create a new team on LiteLLM")

- In this step you should add a new group to the LiteLLM Enterprise App on Azure Entra ID (like we did in step 1.1). We will call this group `Default LiteLLM Prod Team` on Azure Entra ID.
- Start litellm proxy server with your config
- Sign into LiteLLM UI via SSO
- Navigate to `Teams` and you should see the new team `Default LiteLLM Prod Team` auto-created on LiteLLM
- Note LiteLLM will set the default params for this new team.

## 4. Using Entra ID App Roles for User Permissions[​](#4-using-entra-id-app-roles-for-user-permissions "Direct link to 4. Using Entra ID App Roles for User Permissions")

You can assign user roles directly from Entra ID using App Roles. LiteLLM will automatically read the app roles from the JWT token during SSO sign-in and assign the corresponding role to the user.

### 4.1 Supported Roles[​](#41-supported-roles "Direct link to 4.1 Supported Roles")

LiteLLM supports the following app roles (case-insensitive):

- `proxy_admin` - Admin over the entire LiteLLM platform
- `proxy_admin_viewer` - Read-only admin access (can view all keys and spend)
- `org_admin` - Admin over a specific organization (can create teams and users within their org)
- `internal_user` - Standard user (can create/view/delete their own keys and view their own spend)

### 4.2 Create App Roles in Entra ID[​](#42-create-app-roles-in-entra-id "Direct link to 4.2 Create App Roles in Entra ID")

1. Navigate to your App Registration on [https://portal.azure.com/](https://portal.azure.com/)
2. Go to **App roles** &gt; **Create app role**
3. Configure the app role:
   
   - **Display name**: Proxy Admin (or your preferred display name)
   - **Value**: `proxy_admin` (use one of the supported role values above)
   - **Description**: Administrator access to LiteLLM proxy
   - **Allowed member types**: Users/Groups
4. Click **Apply** to save the role

### 4.3 Assign Users to App Roles[​](#43-assign-users-to-app-roles "Direct link to 4.3 Assign Users to App Roles")

1. Navigate to **Enterprise Applications** on [https://portal.azure.com/](https://portal.azure.com/)
2. Select your LiteLLM application
3. Go to **Users and groups** &gt; **Add user/group**
4. Select the user and assign them to one of the app roles you created

### 4.4 Test the Role Assignment[​](#44-test-the-role-assignment "Direct link to 4.4 Test the Role Assignment")

1. Sign in to LiteLLM UI via SSO as a user with an assigned app role
2. LiteLLM will automatically extract the app role from the JWT token
3. The user will be assigned the corresponding LiteLLM role in the database
4. The user's permissions will reflect their assigned role

**How it works:**

- When a user signs in via Microsoft SSO, LiteLLM extracts the `roles` claim from the JWT `id_token`
- If any of the roles match a valid LiteLLM role (case-insensitive), that role is assigned to the user
- If multiple roles are present, LiteLLM uses the first valid role it finds
- This role assignment persists in the LiteLLM database and determines the user's access level

## Video Walkthrough[​](#video-walkthrough "Direct link to Video Walkthrough")

This walks through setting up sso auto-add for **Microsoft Entra ID**

Follow along this video for a walkthrough of how to set this up with Microsoft Entra ID