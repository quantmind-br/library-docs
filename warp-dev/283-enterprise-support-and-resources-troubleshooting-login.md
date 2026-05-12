---
title: Troubleshooting login | Enterprise | Warp
url: https://docs.warp.dev/enterprise/support-and-resources/troubleshooting-login
source: sitemap
fetched_at: 2026-04-29T15:06:09.593900331-03:00
rendered_js: false
word_count: 442
summary: This document provides troubleshooting steps for common authentication and login issues encountered by Warp users, including SSO configuration, proxy settings, and browser-related errors.
tags:
    - troubleshooting
    - sso
    - authentication
    - enterprise
    - login-issues
    - proxy-settings
    - browser-configuration
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Enterprise login issues stem from SSO configuration, browser settings, proxy issues, or fraud detection — each with specific fixes.

## SSO login issues

### Can't open Warp from your SSO provider

When launching Warp from Okta or another SSO provider's dashboard, you may see "Unable to process request due to missing initial state."

**Fix:**
1. Choose **Continue with SSO**.
2. Log in with your normal SSO credentials.

### Previously logged in with another method

If you created your Warp account with email, Google, or GitHub and now need to use SSO:

1. Log in with your **original** method.
2. Click **Link SSO** to connect your existing account. You can now use **Continue with SSO** going forward.

> [!info]
> IT admins: share these steps during SSO rollout for team members linking accounts.

## Common login issues

### Can't sign up or log in

If clicking sign-up/login opens a blank popup or nothing happens:

- Your ISP/firewall may block `*.googleapis.com`. Try a proxy or allowlist this domain.
- In older Ruby dev environments, `.dev` domains may not resolve. If applicable, delete `/etc/resolver/dev` ([more info](https://superuser.com/questions/1374892/dev-domains-dont-resolve)).

### Browser-specific issues

If authentication errors or blank popups occur across browsers:

1. **Disable ad blockers** for `app.warp.dev`.
2. **Clear cookies and cache**, or try an incognito/private window.

**Safari-specific:** To fix "Unable to access localStorage" errors, go to **Safari Preferences > Privacy** and uncheck **Block all cookies**. Firebase Auth requires cookies for login state.

## Proxy issues

If behind a proxy, QUIC traffic may not pass correctly. Disabling QUIC forces TCP fallback:

| Browser | Steps |
|---------|-------|
| Chrome/Edge/Arc/Opera | Navigate to `chrome://flags` → disable **Experimental QUIC protocol** → relaunch |
| Firefox | Navigate to `about:config` → set `network.http.http3.enable` to `false` → restart |
| Safari | No built-in option to disable QUIC |

## Flagged as fraudulent

If you see "This account has been flagged as fraudulent," your account triggered Warp's fraud detection.

### False positives

Ad blockers or Pi-hole systems can trigger false positives. Disable them temporarily and retry.

### Requesting an appeal

Email [appeals@warp.dev](mailto:appeals@warp.dev) with the affected account email. Appeals may take 5–10 days. Enterprise customers can contact their account manager or dedicated Slack/Teams channel for faster resolution.

## Browser doesn't open when signing in

1. Complete authentication in the browser.
2. On the logged-in page, if "Take me to Warp" doesn't work, click the **here** link to copy the auth token.
3. Paste the token into Warp.

> [!info]
> On Linux and Windows, paste shortcut is `CTRL+SHIFT+V`.

## Getting help

- **Enterprise customers** — Contact your dedicated Slack/Teams channel or account manager.
- **All users** — See [[188-enterprise-security-and-compliance-sso]] for SSO setup guidance.
