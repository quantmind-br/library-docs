---
title: Onboard Users for AI Exploration | liteLLM
url: https://docs.litellm.ai/docs/tutorials/default_team_self_serve
source: sitemap
fetched_at: 2026-01-21T19:55:16.350939547-03:00
rendered_js: false
word_count: 315
summary: This document explains how to configure default teams to automatically assign new users, allowing them to create API keys within specific model and budget constraints.
tags:
    - litellm
    - default-teams
    - user-onboarding
    - access-control
    - budget-management
    - api-keys
category: guide
---

v1.73.0 introduces the ability to assign new users to Default Teams. This makes it much easier to enable experimentation with LLMs within your company, by allowing users to sign in and create $10 keys for AI exploration.

### 1. Create a team[​](#1-create-a-team "Direct link to 1. Create a team")

Create a team called `internal exploration` with:

- `models`: access to specific models (e.g. `gpt-4o`, `claude-3-5-sonnet`)
- `max budget`: The team max budget will ensure spend for the entire team never exceeds a certain amount.
- `reset budget`: Set this to monthly. LiteLLM will reset the budget at the start of each month.
- `team member max budget`: The team member max budget will ensure spend for an individual team member never exceeds a certain amount.

### 2. Update team member permissions[​](#2-update-team-member-permissions "Direct link to 2. Update team member permissions")

Click on the team you just created, and update the team member permissions under `Member Permissions`.

This will allow all team members, to create keys.

### 3. Set team as default team[​](#3-set-team-as-default-team "Direct link to 3. Set team as default team")

Go to `Internal Users` -&gt; `Default User Settings` and set the default team to the team you just created.

Let's also set the default models to `no-default-models`. This means a user can only create keys within a team.

### 4. Test it\![​](#4-test-it "Direct link to 4. Test it!")

Let's create a new user and test it out.

#### a. Create a new user[​](#a-create-a-new-user "Direct link to a. Create a new user")

Create a new user with email `test_default_team_user@xyz.com`.

Once you click `Create User`, you will get an invitation link, save it for later.

#### b. Verify user is added to the team[​](#b-verify-user-is-added-to-the-team "Direct link to b. Verify user is added to the team")

Click on the created user, and verify they are added to the team.

We can see the user is added to the team, and has no default models.

#### c. Login as user[​](#c-login-as-user "Direct link to c. Login as user")

Now use the invitation link from 4a. to login as the user.

#### d. Verify you can't create keys without specifying a team[​](#d-verify-you-cant-create-keys-without-specifying-a-team "Direct link to d. Verify you can't create keys without specifying a team")

You should see a message saying you need to select a team.

#### e. Verify you can create a key when specifying a team[​](#e-verify-you-can-create-a-key-when-specifying-a-team "Direct link to e. Verify you can create a key when specifying a team")

Success!

You should now see the created key