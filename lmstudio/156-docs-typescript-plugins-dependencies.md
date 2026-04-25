---
title: Using `npm` Dependencies
url: https://lmstudio.ai/docs/typescript/plugins/dependencies
source: sitemap
fetched_at: 2026-04-07T21:32:02.651841953-03:00
rendered_js: false
word_count: 125
summary: This document explains how to manage and install necessary npm dependencies for developing plugins compatible with LM Studio, advising developers to use 'npm' exclusively.
tags:
    - plugin-development
    - npm
    - dependencies
    - packagejson
    - lm-studio
    - installation
category: guide
---

## Add dependencies to your plugin with `npm`[](#add-dependencies-to-your-plugin-with-npm "Link to 'Add dependencies to your plugin with ,[object Object]'")

LM Studio plugins supports `npm` packages. You can just install them using `npm install`.

When the plugin is installed, LM Studio will automatically download all the required dependencies that are declared in `package.json` and `package-lock.json`. (The user does not need to have Node.js/npm installed.)

### `postinstall` scripts[](#postinstall-scripts)

For safety reasons, we do **not** run `postinstall` scripts. Thus please make sure you are not using any npm packages that require postinstall scripts to work.

## Using Other Package Managers[](#using-other-package-managers "Link to 'Using Other Package Managers'")

Since we rely on `package-lock.json`, lock files produced by other package managers will not work. Thus we recommend only using `npm` when developing LM Studio plugins.