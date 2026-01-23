---
title: ✨ SSO for Admin UI | liteLLM
url: https://docs.litellm.ai/docs/proxy/admin_ui_sso
source: sitemap
fetched_at: 2026-01-21T19:51:08.994230115-03:00
rendered_js: false
word_count: 1114
summary: This document provides instructions for configuring Single Sign-On (SSO) with providers like Okta, Google, and Microsoft, including environment variable setup, UI customization, and troubleshooting.
tags:
    - sso-configuration
    - okta-setup
    - authentication
    - litellm-proxy
    - ui-customization
    - identity-management
category: configuration
---

info

From v1.76.0, SSO is now Free for up to 5 users.

### Usage (Google, Microsoft, Okta, etc.)[​](#usage-google-microsoft-okta-etc "Direct link to Usage (Google, Microsoft, Okta, etc.)")

- Okta SSO
- Google SSO
- Microsoft SSO
- Generic SSO Provider

<!--THE END-->

1. Add Okta credentials to your .env

```
GENERIC_CLIENT_ID = "<your-okta-client-id>"
GENERIC_CLIENT_SECRET = "<your-okta-client-secret>" 
GENERIC_AUTHORIZATION_ENDPOINT = "<your-okta-domain>/authorize" # https://dev-2kqkcd6lx6kdkuzt.us.auth0.com/authorize
GENERIC_TOKEN_ENDPOINT = "<your-okta-domain>/token" # https://dev-2kqkcd6lx6kdkuzt.us.auth0.com/oauth/token
GENERIC_USERINFO_ENDPOINT = "<your-okta-domain>/userinfo" # https://dev-2kqkcd6lx6kdkuzt.us.auth0.com/userinfo
GENERIC_CLIENT_STATE = "random-string" # [OPTIONAL] REQUIRED BY OKTA, if not set random state value is generated
GENERIC_SSO_HEADERS = "Content-Type=application/json, X-Custom-Header=custom-value" # [OPTIONAL] Comma-separated list of additional headers to add to the request - e.g. Content-Type=application/json, etc.
```

You can get your domain specific auth/token/userinfo endpoints at `<YOUR-OKTA-DOMAIN>/.well-known/openid-configuration`

2. Add proxy url as callback\_url on Okta

On Okta, add the 'callback\_url' as `<proxy_base_url>/sso/callback`

### Default Login, Logout URLs[​](#default-login-logout-urls "Direct link to Default Login, Logout URLs")

Some SSO providers require a specific redirect url for login and logout. You can input the following values.

- Login: `<your-proxy-base-url>/sso/key/generate`
- Logout: `<your-proxy-base-url>`

Here's the env var to set the logout url on the proxy

```
PROXY_LOGOUT_URL="https://www.google.com"
```

#### Step 3. Set `PROXY_BASE_URL` in your .env[​](#step-3-set-proxy_base_url-in-your-env "Direct link to step-3-set-proxy_base_url-in-your-env")

Set this in your .env (so the proxy can set the correct redirect url)

```
PROXY_BASE_URL=https://litellm-api.up.railway.app
```

#### Step 4. Test flow[​](#step-4-test-flow "Direct link to Step 4. Test flow")

![](https://docs.litellm.ai/assets/images/litellm_ui_3-5fb4411e4631e35e5641cf40b707312c.gif)

### Restrict Email Subdomains w/ SSO[​](#restrict-email-subdomains-w-sso "Direct link to Restrict Email Subdomains w/ SSO")

If you're using SSO and want to only allow users with a specific subdomain - e.g. (@berri.ai email accounts) to access the UI, do this:

```
export ALLOWED_EMAIL_DOMAINS="berri.ai"
```

This will check if the user email we receive from SSO contains this domain, before allowing access.

### Set Proxy Admin[​](#set-proxy-admin "Direct link to Set Proxy Admin")

Set a Proxy Admin when SSO is enabled. Once SSO is enabled, the `user_id` for users is retrieved from the SSO provider. In order to set a Proxy Admin, you need to copy the `user_id` from the UI and set it in your `.env` as `PROXY_ADMIN_ID`.

#### Step 1: Copy your ID from the UI[​](#step-1-copy-your-id-from-the-ui "Direct link to Step 1: Copy your ID from the UI")

#### Step 2: Set it in your .env as the PROXY\_ADMIN\_ID[​](#step-2-set-it-in-your-env-as-the-proxy_admin_id "Direct link to Step 2: Set it in your .env as the PROXY_ADMIN_ID")

```
export PROXY_ADMIN_ID="116544810872468347480"
```

This will update the user role in the `LiteLLM_UserTable` to `proxy_admin`.

If you plan to change this ID, please update the user role via API `/user/update` or UI (Internal Users page).

#### Step 3: See all proxy keys[​](#step-3-see-all-proxy-keys "Direct link to Step 3: See all proxy keys")

info

If you don't see all your keys this could be due to a cached token. So just re-login and it should work.

### Disable `Default Team` on Admin UI[​](#disable-default-team-on-admin-ui "Direct link to disable-default-team-on-admin-ui")

Use this if you want to hide the Default Team on the Admin UI

The following logic will apply

- If team assigned don't show `Default Team`
- If no team assigned then they should see `Default Team`

Set `default_team_disabled: true` on your litellm config.yaml

```
general_settings:
master_key: sk-1234
default_team_disabled:true# OR you can set env var PROXY_DEFAULT_TEAM_DISABLED="true"
```

### Use Username, Password when SSO is on[​](#use-username-password-when-sso-is-on "Direct link to Use Username, Password when SSO is on")

If you need to access the UI via username/password when SSO is on navigate to `/fallback/login`. This route will allow you to sign in with your username/password credentials.

### Restrict UI Access[​](#restrict-ui-access "Direct link to Restrict UI Access")

You can restrict UI Access to just admins - includes you (proxy\_admin) and people you give view only access to (proxy\_admin\_viewer) for seeing global spend.

**Step 1. Set 'admin\_only' access**

```
general_settings:
ui_access_mode:"admin_only"
```

**Step 2. Invite view-only users**

### Custom Branding Admin UI[​](#custom-branding-admin-ui "Direct link to Custom Branding Admin UI")

Use your companies custom branding on the LiteLLM Admin UI We allow you to

- Customize the UI Logo
- Customize the UI color scheme

#### Set Custom Logo[​](#set-custom-logo "Direct link to Set Custom Logo")

We allow you to pass a local image or a an http/https url of your image

Set `UI_LOGO_PATH` on your env. We recommend using a hosted image, it's a lot easier to set up and configure / debug

Example setting Hosted image

```
UI_LOGO_PATH="https://litellm-logo-aws-marketplace.s3.us-west-2.amazonaws.com/berriai-logo-github.png"
```

Example setting a local image (on your container)

```
UI_LOGO_PATH="ui_images/logo.jpg"
```

#### Or set your logo directly from Admin UI:[​](#or-set-your-logo-directly-from-admin-ui "Direct link to Or set your logo directly from Admin UI:")

#### Set Custom Color Theme[​](#set-custom-color-theme "Direct link to Set Custom Color Theme")

- Navigate to [/enterprise/enterprise\_ui](https://github.com/BerriAI/litellm/blob/main/enterprise/enterprise_ui/_enterprise_colors.json)
- Inside the `enterprise_ui` directory, rename `_enterprise_colors.json` to `enterprise_colors.json`
- Set your companies custom color scheme in `enterprise_colors.json` Example contents of `enterprise_colors.json` Set your colors to any of the following colors: [https://www.tremor.so/docs/layout/color-palette#default-colors](https://www.tremor.so/docs/layout/color-palette#default-colors)

```
{
"brand":{
"DEFAULT":"teal",
"faint":"teal",
"muted":"teal",
"subtle":"teal",
"emphasis":"teal",
"inverted":"teal"
}
}

```

- Deploy LiteLLM Proxy Server

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### "The 'redirect\_uri' parameter must be a Login redirect URI in the client app settings" Error[​](#the-redirect_uri-parameter-must-be-a-login-redirect-uri-in-the-client-app-settings-error "Direct link to \"The 'redirect_uri' parameter must be a Login redirect URI in the client app settings\" Error")

This error commonly occurs with Okta and other SSO providers when the redirect URI configuration is incorrect.

#### Issue[​](#issue "Direct link to Issue")

```
Your request resulted in an error. The 'redirect_uri' parameter must be a Login redirect URI in the client app settings
```

#### Solution[​](#solution "Direct link to Solution")

**1. Ensure you have set PROXY\_BASE\_URL in your .env and it includes protocol**

Make sure your `PROXY_BASE_URL` includes the complete URL with protocol (`http://` or `https://`):

```
# ✅ Correct - includes https://
PROXY_BASE_URL=https://litellm.platform.com

# ✅ Correct - includes http://
PROXY_BASE_URL=http://litellm.platform.com

# ❌ Incorrect - missing protocol
PROXY_BASE_URL=litellm.platform.com
```

**2. For Okta specifically, ensure GENERIC\_CLIENT\_STATE is set**

Okta requires the `GENERIC_CLIENT_STATE` parameter:

```
GENERIC_CLIENT_STATE="random-string" # Required for Okta
```

### Okta PKCE[​](#okta-pkce "Direct link to Okta PKCE")

If your Okta application is configured to require PKCE (Proof Key for Code Exchange), enable it by setting:

```
GENERIC_CLIENT_USE_PKCE="true"
```

This is required when your Okta app settings enforce PKCE for enhanced security. LiteLLM will automatically handle PKCE parameter generation and verification during the OAuth flow.

### Common Configuration Issues[​](#common-configuration-issues "Direct link to Common Configuration Issues")

#### Missing Protocol in Base URL[​](#missing-protocol-in-base-url "Direct link to Missing Protocol in Base URL")

```
# This will cause redirect_uri errors
PROXY_BASE_URL=mydomain.com

# Fix: Add the protocol
PROXY_BASE_URL=https://mydomain.com
```

### Fallback Login[​](#fallback-login "Direct link to Fallback Login")

If you need to access the UI via username/password when SSO is on navigate to `/fallback/login`. This route will allow you to sign in with your username/password credentials.

### Debugging SSO JWT fields[​](#debugging-sso-jwt-fields "Direct link to Debugging SSO JWT fields")

If you need to inspect the JWT fields received from your SSO provider by LiteLLM, follow these instructions. This guide walks you through setting up a debug callback to view the JWT data during the SSO process.

1. Add `/sso/debug/callback` as a redirect URL in your SSO provider

In your SSO provider's settings, add the following URL as a new redirect (callback) URL:

Redirect URL

```
http://<proxy_base_url>/sso/debug/callback
```

2. Navigate to the debug login page on your browser
   
   Navigate to the following URL on your browser:
   
   URL to navigate to
   
   ```
   https://<proxy_base_url>/sso/debug/login
   ```
   
   This will initiate the standard SSO flow. You will be redirected to your SSO provider's login screen, and after successful authentication, you will be redirected back to LiteLLM's debug callback route.
3. View the JWT fields

Once redirected, you should see a page called "SSO Debug Information". This page displays the JWT fields received from your SSO provider (as shown in the image above)

## Advanced[​](#advanced "Direct link to Advanced")

### Manage User Roles via Azure App Roles[​](#manage-user-roles-via-azure-app-roles "Direct link to Manage User Roles via Azure App Roles")

Centralize role management by defining user permissions in Azure Entra ID. LiteLLM will automatically assign roles based on your Azure configuration when users sign in—no need to manually manage roles in LiteLLM.

#### Step 1: Create App Roles on Azure App Registration[​](#step-1-create-app-roles-on-azure-app-registration "Direct link to Step 1: Create App Roles on Azure App Registration")

1. Navigate to your App Registration on [https://portal.azure.com/](https://portal.azure.com/)
2. Go to **App roles** &gt; **Create app role**
3. Configure the app role using one of the [supported LiteLLM roles](https://docs.litellm.ai/docs/proxy/access_control#global-proxy-roles):
   
   - **Display name**: Admin Viewer (or your preferred display name)
   - **Value**: `proxy_admin_viewer` (must match one of the LiteLLM role values exactly)
4. Click **Apply** to save the role
5. Repeat for each LiteLLM role you want to use

**Supported LiteLLM role values** (see [full role documentation](https://docs.litellm.ai/docs/proxy/access_control#global-proxy-roles)):

- `proxy_admin` - Full admin access
- `proxy_admin_viewer` - Read-only admin access
- `internal_user` - Can create/view/delete own keys
- `internal_user_viewer` - Can view own keys (read-only)

* * *

#### Step 2: Assign Users to App Roles[​](#step-2-assign-users-to-app-roles "Direct link to Step 2: Assign Users to App Roles")

1. Navigate to **Enterprise Applications** on [https://portal.azure.com/](https://portal.azure.com/)
2. Select your LiteLLM application
3. Go to **Users and groups** &gt; **Add user/group**
4. Select the user
5. Under **Select a role**, choose the app role you created (e.g., `proxy_admin_viewer`)
6. Click **Assign** to save

* * *

#### Step 3: Sign in and verify[​](#step-3-sign-in-and-verify "Direct link to Step 3: Sign in and verify")

1. Sign in to the LiteLLM UI via SSO
2. LiteLLM will automatically extract the app role from the JWT token
3. The user will be assigned the corresponding role (you can verify this in the UI by checking the user profile dropdown)

**Note:** The role from Entra ID will take precedence over any existing role in the LiteLLM database. This ensures your SSO provider is the authoritative source for user roles.