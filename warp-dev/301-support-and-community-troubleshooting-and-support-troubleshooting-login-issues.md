---
title: Troubleshooting Login | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/troubleshooting-and-support/troubleshooting-login-issues
source: sitemap
fetched_at: 2026-04-29T15:05:43.270460215-03:00
rendered_js: false
word_count: 454
summary: This document provides troubleshooting steps for resolving common login, signup, and authentication issues encountered when using the Warp application.
tags:
    - troubleshooting
    - authentication
    - login-issues
    - proxy-settings
    - sso
    - web-browser
    - warp-terminal
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## Can't sign up for or log into Warp

Clicking the button should open a signup/login pop-up. If a blank pop-up window appears, your ISP or Firewall may be blocking calls to `*.googleapis.com`.

> [!note]
> In older Ruby development environments, `.dev` domains may not resolve properly. Delete `/etc/resolver/dev` if needed.

## All browsers

An error may occur due to an ad blocker or stale browser cookies (including Firebase auth cookies).

**To fix:**
1. Disable your ad blocker for `app.warp.dev`
2. Clear cookies and cache, or open an incognito/private browser window

## Safari

If you see `Unable to access localStorage` or `Unhandled Promise Rejection: This operation is not supported in the environment...` when clicking "Sign Up":

1. Go to Safari **Preferences** > **Privacy**
2. Uncheck **"Block all cookies"**

## Proxies

When behind a proxy, disable QUIC to fall back to TCP.

| Browser | Steps |
|---|---|
| Chrome/Edge/Opera/Arc | 1. Navigate to `chrome://flags`<br>2. Search "Experimental QUIC protocol"<br>3. Set to "Disabled"<br>4. Relaunch browser |
| Firefox | 1. Navigate to `about:config`<br>2. Search `network.http.http3.enable`<br>3. Double-click to set to `false`<br>4. Restart Firefox |
| Safari | No built-in option — QUIC is default and cannot be disabled |

## SSO login

### Can't open Warp from SSO

When launching Warp from Okta or other SSO providers, you may see "Unable to process request due to missing initial state...". Workaround:

1. Choose "Continue with SSO"
2. Login with your normal SSO credentials

### Previously logged in with another method

1. Login with the original method (email, Google, GitHub)
2. This links your login to SSO
3. Proceed to login with "Continue with SSO"

## Flagged as fraudulent

You failed one or more checks in Warp's fraud detection system. Creating multiple accounts or using throwaway emails increases the chance of triggering this system.

**False positives:** Ad-blockers or Pi-hole may falsely trigger this system. Temporarily disable these and attempt login again.

**Requesting an appeal:**
1. Email [appeals@warp.dev](mailto:appeals@warp.dev)
2. Include the email of the affected account
3. Investigation may take 5-10 days

## How to get an Auth token to login

If the browser doesn't open when clicking "Sign up" or "Sign in":

1. Navigate to [app.warp.dev/signup](https://app.warp.dev/signup) or [app.warp.dev/login](https://app.warp.dev/login)
2. Create account or login
3. Copy the auth token from the "here" link on the logged_in page
4. Paste the token into Warp

> [!warning]
> On Linux and Windows, copy-paste shortcuts are `CTRL+SHIFT+C` and `CTRL+SHIFT+V`. On Linux and WSL, set your default `$BROWSER` to `brave-browser` to workaround copy-paste issues.

If "Take me to Warp" still doesn't work, check for proxy issues or see the [workaround guide](https://embiid.blog/post/WARP-does-not-work-after-submitting-an-invite-code/).

## Get help with login issues

If Sign Up or Login doesn't work after trying these steps, [contact Warp support](https://www.warp.dev/contact).

#troubleshooting #authentication #login-issues
