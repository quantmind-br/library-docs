---
title: Permissions - OpenClaw
url: https://docs.openclaw.ai/platforms/mac/permissions
source: sitemap
fetched_at: 2026-01-30T20:27:16.626415141-03:00
rendered_js: false
word_count: 206
summary: This document explains how macOS Transparency, Consent, and Control (TCC) permissions work and provides guidance for maintaining stable app permissions during development and deployment.
tags:
    - macos
    - permissions
    - tcc
    - security
    - app-signing
    - development
category: guide
---

## macOS permissions (TCC)

macOS permission grants are fragile. TCC associates a permission grant with the app’s code signature, bundle identifier, and on-disk path. If any of those change, macOS treats the app as new and may drop or hide prompts.

## Requirements for stable permissions

- Same path: run the app from a fixed location (for OpenClaw, `dist/OpenClaw.app`).
- Same bundle identifier: changing the bundle ID creates a new permission identity.
- Signed app: unsigned or ad-hoc signed builds do not persist permissions.
- Consistent signature: use a real Apple Development or Developer ID certificate so the signature stays stable across rebuilds.

Ad-hoc signatures generate a new identity every build. macOS will forget previous grants, and prompts can disappear entirely until the stale entries are cleared.

## Recovery checklist when prompts disappear

1. Quit the app.
2. Remove the app entry in System Settings -&gt; Privacy & Security.
3. Relaunch the app from the same path and re-grant permissions.
4. If the prompt still does not appear, reset TCC entries with `tccutil` and try again.
5. Some permissions only reappear after a full macOS restart.

Example resets (replace bundle ID as needed):

```
sudo tccutil reset Accessibility bot.molt.mac
sudo tccutil reset ScreenCapture bot.molt.mac
sudo tccutil reset AppleEvents
```

If you are testing permissions, always sign with a real certificate. Ad-hoc builds are only acceptable for quick local runs where permissions do not matter.