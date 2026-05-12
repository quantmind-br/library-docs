---
title: FAQ | Enterprise | Warp
url: https://docs.warp.dev/enterprise/getting-started/faq
source: sitemap
fetched_at: 2026-04-29T15:05:59.843464148-03:00
rendered_js: false
word_count: 275
summary: Troubleshooting steps for common authentication, SSO integration, and administrative access issues in Warp.
tags:
    - sso-troubleshooting
    - account-linking
    - admin-settings
    - access-management
    - user-authentication
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## Login and SSO

### I can't log in with SSO

**Problem:** Error message when trying to log in via SSO.

**Solution:**

1. Select **Continue with SSO** and enter your work email or domain.
2. Complete the linking process.
3. Log out and log back in with **Continue with SSO**.

### I logged in with another method and can't use SSO now

**Problem:** You created a Warp account with email/Google/GitHub, but your organization now requires SSO.

**Solution:**

1. Log in with your original method.
2. Complete the linking process.
3. Log out and log back in with **Continue with SSO**.

### Warp won't open from my SSO provider

**Problem:** Clicking Warp in Okta/Microsoft Entra ID portal shows an error.

**Solution:** This is a known limitation. Warp cannot be launched directly from SSO provider portals.

1. Click **Continue with SSO** instead.
2. Complete authentication.

## Team and Access

### Team invite links not working

**Common causes:**

- Invite link expired or was revoked.
- User's email domain doesn't match configured restrictions.

**Solution:**

1. Generate a new invite link.
2. Verify domain restrictions match the user's email.

### Users can't see new admin settings

**Problem:** You changed a setting in the Admin Panel, but users don't see the change.

**Solution:**

1. Verify the setting is not set to "Respect User Setting."
2. Ask users to restart Warp to force a settings refresh.
3. Confirm users are members of the correct team.
4. Check that users have logged in with SSO (not a personal account).

## Additional Help

- Contact your team admin for organization-specific issues.
- Reach out to Warp support via your team's dedicated Slack/Teams channel.
