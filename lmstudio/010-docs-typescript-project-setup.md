---
title: Project Setup
url: https://lmstudio.ai/docs/typescript/project-setup
source: sitemap
fetched_at: 2026-04-07T21:31:38.6248226-03:00
rendered_js: false
word_count: 95
summary: This document provides instructions on how to integrate and set up the @lmstudio/sdk library into new or existing Node.js projects.
tags:
    - node-js
    - sdk
    - installation
    - npm
    - development-setup
    - library
category: guide
---

`@lmstudio/sdk` is a library published on npm that allows you to use `lmstudio-js` in your own projects. It is open source and it's developed on GitHub. You can find the source code [here](https://github.com/lmstudio-ai/lmstudio-js).

## Creating a New `node` Project[](#creating-a-new-node-project "Link to 'Creating a New ,[object Object], Project'")

Use the following command to start an interactive project setup:

```
lms create node-typescript
```

## Add `lmstudio-js` to an Exiting Project[](#add-lmstudio-js-to-an-exiting-project "Link to 'Add ,[object Object], to an Exiting Project'")

If you have already created a project and would like to use `lmstudio-js` in it, you can install it using npm, yarn, or pnpm.

```
npm install @lmstudio/sdk --save
```