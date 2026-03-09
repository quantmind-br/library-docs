---
title: Development Tools | Camoufox
url: https://camoufox.com/development/tools/
source: sitemap
fetched_at: 2026-03-09T16:48:12.949167-03:00
rendered_js: false
word_count: 115
summary: This document explains how to use the included developer UI script to create, manage, and modify patches by resetting the workspace and writing changes back to a patch file.
tags:
    - developer-ui
    - patch-management
    - workspace-reset
    - scripting
    - development-workflow
category: guide
---

This repo comes with a developer UI under scripts/developer.py:

Patches can be edited, created, removed, and managed through here.

![](https://camoufox.com/static/dev-gui.png)

* * *

## [#](#how-to-make-a-patch)How to make a patch

1. In the developer UI, click **Reset workspace**.
2. Make changes in the `camoufox-*/` folder as needed. You can test your changes with `make build` and `make run`.
3. After you're done making changes, click **Write workspace to patch** and save the patch file.

## [#](#how-to-work-on-an-existing-patch)How to work on an existing patch

1. In the developer UI, click **Edit a patch**.
2. Select the patch you'd like to edit. Your workspace will be reset to the state of the selected patch.
3. After you're done making changes, hit **Write workspace to patch** and overwrite the existing patch file.