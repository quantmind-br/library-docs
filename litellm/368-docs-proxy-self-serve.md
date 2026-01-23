---
title: Internal User Self-Serve | liteLLM
url: https://docs.litellm.ai/docs/proxy/self_serve
source: sitemap
fetched_at: 2026-01-21T19:53:36.433616461-03:00
rendered_js: false
word_count: 712
summary: This document explains how to manage user roles, permissions, and automated team provisioning within the LiteLLM Proxy UI, including SSO integration and budget controls.
tags:
    - litellm-proxy
    - user-management
    - sso-integration
    - access-control
    - budget-management
    - team-configuration
category: guide
---

## Allow users to create their own keys on [Proxy UI](https://docs.litellm.ai/docs/proxy/ui).[​](#allow-users-to-create-their-own-keys-on-proxy-ui "Direct link to allow-users-to-create-their-own-keys-on-proxy-ui")

1. Add user with permissions to a team on proxy

<!--THE END-->

- UI
- API

Go to `Internal Users` -&gt; `+New User`

2. Share invitation link with user

<!--THE END-->

- UI
- API

Copy the invitation link with the user

3. User logs in via email + password auth

<!--THE END-->

4. User can now create their own keys

## Allow users to View Usage, Caching Analytics[​](#allow-users-to-view-usage-caching-analytics "Direct link to Allow users to View Usage, Caching Analytics")

1. Go to Internal Users -&gt; +Invite User

Set their role to `Admin Viewer` - this means they can only view usage, caching analytics

2. Share invitation link with user

<!--THE END-->

3. User logs in via email + password auth

<!--THE END-->

4. User can now view Usage, Caching Analytics

## Available Roles[​](#available-roles "Direct link to Available Roles")

Here's the available UI roles for a LiteLLM Internal User:

**Admin Roles:**

- `proxy_admin`: admin over the platform
- `proxy_admin_viewer`: can login, view all keys, view all spend. **Cannot** create/delete keys, add new users.

**Internal User Roles:**

- `internal_user`: can login, view/create/delete their own keys, view their spend. **Cannot** add new users.
- `internal_user_viewer`: can login, view their own keys, view their own spend. **Cannot** create/delete keys, add new users.

**Team Roles:**

- `admin`: can add new members to the team, can control Team Permissions, can add team-only models (useful for onboarding a team's finetuned models).
- `user`: can login, view their own keys, view their own spend. **Cannot** create/delete keys (controllable via Team Permissions), add new users.

## Auto-add SSO users to teams[​](#auto-add-sso-users-to-teams "Direct link to Auto-add SSO users to teams")

This walks through setting up sso auto-add for **Okta, Google SSO**

### Okta, Google SSO[​](#okta-google-sso "Direct link to Okta, Google SSO")

1. Specify the JWT field that contains the team ids, that the user belongs to.

```
general_settings:
master_key: sk-1234
litellm_jwtauth:
team_ids_jwt_field:"groups"# 👈 CAN BE ANY FIELD
```

This is assuming your SSO token looks like this. **If you need to inspect the JWT fields received from your SSO provider by LiteLLM, follow these instructions [here](#debugging-sso-jwt-fields)**

```
{
  ...,
  "groups": ["team_id_1", "team_id_2"]
}
```

2. Create the teams on LiteLLM

```
curl -X POST '<PROXY_BASE_URL>/team/new' \
-H 'Authorization: Bearer <PROXY_MASTER_KEY>' \
-H 'Content-Type: application/json' \
-D '{
    "team_alias": "team_1",
    "team_id": "team_id_1" # 👈 MUST BE THE SAME AS THE SSO GROUP ID
}'
```

3. Test the SSO flow

Here's a walkthrough of [how it works](https://www.loom.com/share/8959be458edf41fd85937452c29a33f3?sid=7ebd6d37-569a-4023-866e-e0cde67cb23e)

### Microsoft Entra ID SSO group assignment[​](#microsoft-entra-id-sso-group-assignment "Direct link to Microsoft Entra ID SSO group assignment")

Follow this [tutorial for auto-adding sso users to teams with Microsoft Entra ID](https://docs.litellm.ai/docs/tutorials/msft_sso)

### Debugging SSO JWT fields[​](#debugging-sso-jwt-fields "Direct link to Debugging SSO JWT fields")

[**Go Here**](https://docs.litellm.ai/docs/proxy/admin_ui_sso#debugging-sso-jwt-fields)

## Advanced[​](#advanced "Direct link to Advanced")

### Setting custom logout URLs[​](#setting-custom-logout-urls "Direct link to Setting custom logout URLs")

Set `PROXY_LOGOUT_URL` in your .env if you want users to get redirected to a specific URL when they click logout

```
export PROXY_LOGOUT_URL="https://www.google.com"
```

### Set default max budget for internal users[​](#set-default-max-budget-for-internal-users "Direct link to Set default max budget for internal users")

Automatically apply budget per internal user when they sign up. By default the table will be checked every 10 minutes, for users to reset. To modify this, [see this](https://docs.litellm.ai/docs/proxy/users#reset-budgets)

```
litellm_settings:
max_internal_user_budget:10
internal_user_budget_duration:"1mo"# reset every month
```

This sets a max budget of $10 USD for internal users when they sign up.

You can also manage these settings visually in the UI:

This budget only applies to personal keys created by that user - seen under `Default Team` on the UI.

This budget does not apply to keys created under non-default teams.

### Set max budget for teams[​](#set-max-budget-for-teams "Direct link to Set max budget for teams")

[**Go Here**](https://docs.litellm.ai/docs/proxy/team_budgets)

### Default Team[​](#default-team "Direct link to Default Team")

- UI
- YAML

Go to `Internal Users` -&gt; `Default User Settings` and set the default team to the team you just created.

Let's also set the default models to `no-default-models`. This means a user can only create keys within a team.

### Team Member Budgets[​](#team-member-budgets "Direct link to Team Member Budgets")

Set a max budget for a team member.

You can do this when creating a new team, or by updating an existing team.

- UI
- API

### Team Member Rate Limits[​](#team-member-rate-limits "Direct link to Team Member Rate Limits")

Set a default tpm/rpm limit for an individual team member.

You can do this when creating a new team, or by updating an existing team.

- UI
- API

### Set default params for new teams[​](#set-default-params-for-new-teams "Direct link to Set default params for new teams")

When you connect litellm to your SSO provider, litellm can auto-create teams. Use this to set the default `models`, `max_budget`, `budget_duration` for these auto-created teams.

**How it works**

1. When litellm fetches `groups` from your SSO provider, it will check if the corresponding group\_id exists as a `team_id` in litellm.
2. If the team\_id does not exist, litellm will auto-create a team with the default params you've set.
3. If the team\_id already exist, litellm will not apply any settings on the team.

**Usage**

Default Params for new teams

```
litellm_settings:
default_team_params:# Default Params to apply when litellm auto creates a team from SSO IDP provider
max_budget:100# Optional[float], optional): $100 budget for the team
budget_duration: 30d           # Optional[str], optional): 30 days budget_duration for the team
models:["gpt-3.5-turbo"]# Optional[List[str]], optional): models to be used by the team
```

### Restrict Users from creating personal keys[​](#restrict-users-from-creating-personal-keys "Direct link to Restrict Users from creating personal keys")

This is useful if you only want users to create keys under a specific team.

This will also prevent users from using their session tokens on the test keys chat pane.

👉 [**See this**](https://docs.litellm.ai/docs/proxy/virtual_keys#restricting-key-generation)

## **All Settings for Self Serve / SSO Flow**[​](#all-settings-for-self-serve--sso-flow "Direct link to all-settings-for-self-serve--sso-flow")

All Settings for Self Serve / SSO Flow

```
litellm_settings:
max_internal_user_budget:10# max budget for internal users
internal_user_budget_duration:"1mo"# reset every month

default_internal_user_params:# Default Params used when a new user signs in Via SSO
user_role:"internal_user"# one of "internal_user", "internal_user_viewer", "proxy_admin", "proxy_admin_viewer". New SSO users not in litellm will be created as this user
max_budget:100# Optional[float], optional): $100 budget for a new SSO sign in user
budget_duration: 30d           # Optional[str], optional): 30 days budget_duration for a new SSO sign in user
models:["gpt-3.5-turbo"]# Optional[List[str]], optional): models to be used by a new SSO sign in user
teams:# Optional[List[NewUserRequestTeam]], optional): teams to be used by the user
-team_id:"team_id_1"# Required[str]: team_id to be used by the user
max_budget_in_team:100# Optional[float], optional): $100 budget for the team. Defaults to None.
user_role:"user"# Optional[str], optional): "user" or "admin". Defaults to "user"

default_team_params:# Default Params to apply when litellm auto creates a team from SSO IDP provider
max_budget:100# Optional[float], optional): $100 budget for the team
budget_duration: 30d           # Optional[str], optional): 30 days budget_duration for the team
models:["gpt-3.5-turbo"]# Optional[List[str]], optional): models to be used by the team


upperbound_key_generate_params:# Upperbound for /key/generate requests when self-serve flow is on
max_budget:100# Optional[float], optional): upperbound of $100, for all /key/generate requests
budget_duration:"10d"# Optional[str], optional): upperbound of 10 days for budget_duration values
duration:"30d"# Optional[str], optional): upperbound of 30 days for all /key/generate requests
max_parallel_requests:1000# (Optional[int], optional): Max number of requests that can be made in parallel. Defaults to None.
tpm_limit:1000#(Optional[int], optional): Tpm limit. Defaults to None.
rpm_limit:1000#(Optional[int], optional): Rpm limit. Defaults to None.

key_generation_settings:# Restricts who can generate keys. [Further docs](./virtual_keys.md#restricting-key-generation)
team_key_generation:
allowed_team_member_roles:["admin"]
personal_key_generation:# maps to 'Default Team' on UI 
allowed_user_roles:["proxy_admin"]
```

## Further Reading[​](#further-reading "Direct link to Further Reading")

- [Onboard Users for AI Exploration](https://docs.litellm.ai/docs/tutorials/default_team_self_serve)