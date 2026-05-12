---
title: Getting started - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/firectl
source: sitemap
fetched_at: 2026-04-27T20:17:11.516948571-03:00
rendered_js: false
word_count: 39
summary: This document outlines various ways to install the Firectl tool and provides essential command-line instructions for managing its state, including signing into a Fireworks account, verifying the current session, checking the installed version, and upgrading.
tags:
    - firectl-installation
    - account-signing
    - cli-commands
    - version-check
    - upgrading
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
## Installation

Install via Homebrew:

```bash
brew tap fw-ai/firectl
brew install firectl

# If you encounter a failed SHA256 check, try first running
brew update
```

## Sign into Fireworks account

```bash
firectl signin
```

If you have set up [[021-accounts-sso|Custom SSO]], also pass your account ID:

```bash
firectl signin <ACCOUNT_ID>
```

## Check you have signed in

```bash
firectl whoami
```

## Check your installed version

```bash
firectl version
```

## Upgrade to the latest version

```bash
sudo firectl upgrade
```
