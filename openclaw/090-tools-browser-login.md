---
title: Browser login - OpenClaw
url: https://docs.openclaw.ai/tools/browser-login
source: sitemap
fetched_at: 2026-01-30T20:22:38.938141599-03:00
rendered_js: false
word_count: 183
summary: This document provides instructions for securely logging into browsers and posting to X/Twitter using OpenClaw's browser tools, emphasizing manual login practices and host browser usage for avoiding bot detection.
tags:
    - browser-login
    - twitter-posting
    - security
    - automation
    - sandboxing
    - host-browser
category: guide
---

## Browser login + X/Twitter posting

## Manual login (recommended)

When a site requires login, **sign in manually** in the **host** browser profile (the openclaw browser). Do **not** give the model your credentials. Automated logins often trigger anti‑bot defenses and can lock the account. Back to the main browser docs: [Browser](https://docs.openclaw.ai/tools/browser).

## Which Chrome profile is used?

OpenClaw controls a **dedicated Chrome profile** (named `openclaw`, orange‑tinted UI). This is separate from your daily browser profile. Two easy ways to access it:

1. **Ask the agent to open the browser** and then log in yourself.
2. **Open it via CLI**:

```
openclaw browser start
openclaw browser open https://x.com
```

If you have multiple profiles, pass `--browser-profile <name>` (the default is `openclaw`).

## X/Twitter: recommended flow

- **Read/search/threads:** use the **bird** CLI skill (no browser, stable).
  
  - Repo: [https://github.com/steipete/bird](https://github.com/steipete/bird)
- **Post updates:** use the **host** browser (manual login).

## Sandboxing + host browser access

Sandboxed browser sessions are **more likely** to trigger bot detection. For X/Twitter (and other strict sites), prefer the **host** browser. If the agent is sandboxed, the browser tool defaults to the sandbox. To allow host control:

```
{
  agents: {
    defaults: {
      sandbox: {
        mode: "non-main",
        browser: {
          allowHostControl: true
        }
      }
    }
  }
}
```

Then target the host browser:

```
openclaw browser open https://x.com --browser-profile openclaw --target host
```

Or disable sandboxing for the agent that posts updates.