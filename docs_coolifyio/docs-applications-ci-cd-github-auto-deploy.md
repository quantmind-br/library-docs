---
title: GitHub Auto Deploy
url: https://coolify.io/docs/applications/ci-cd/github/auto-deploy.md
source: llms
fetched_at: 2026-02-17T14:39:23.520405-03:00
rendered_js: false
word_count: 284
summary: This document explains how to configure automatic deployments in Coolify using GitHub Apps, GitHub Actions, or webhooks. It provides step-by-step instructions for enabling auto-deploy features and setting up the necessary connections between GitHub and Coolify.
tags:
    - coolify
    - github-deploy
    - ci-cd
    - webhooks
    - automation
    - github-app
    - deployment-guide
category: guide
---

# GitHub Auto Deploy

Coolify can automatically deploy new versions of your application whenever you push changes to your GitHub repository.

There are three methods to set up automatic deployments on Coolify:

* [GitHub App](#github-app)
* [GitHub Actions](#github-actions)
* [Webhooks](#webhooks)

## GitHub App

We have a dedicated guide for setting up a GitHub App, which you can follow here: [/github/setup-app](/applications/ci-cd/github/setup-app).

Coolify automatically enables "Auto Deploy" after you set up your GitHub App. If it doesn't, enable it on your application by following these steps:

1. Open your application configuration page.
2. Go to the "Advanced" page.
3. Enable "Auto Deploy" under the general section.

## GitHub Actions

We have a dedicated guide for setting up GitHub Actions, which you can follow here: [/github/setup-app](/applications/ci-cd/github/setup-app).

## Webhooks

### 1. Enable Auto Deploy

1. Open your application configuration page.
2. Go to the "Advanced" page.
3. Enable "Auto Deploy" under the general section.

### 2. Set Up GitHub Webhook Secret

1. Enter a GitHub webhook secret (this must be a random string; you can use tools like [Random String Generator](https://getrandomgenerator.com/string)).
2. Save the webhook URL somewhere safe, we'll need it later.

::: warning IMPORTANT
A webhook secret acts like a password. Coolify only accepts the webhook if the secret matches.
:::

### 3. Set Up Webhook on GitHub

1. Go to your repository settings page.
2. Click on "Webhooks" from the sidebar.
3. Click the "Add webhook" button.

4) Enter the previously copied webhook URL from Coolify in the "Payload URL" field.
5) Enter the webhook secret from Coolify in the "Secret" field.
6) Enable "Enable SSL verification".
7) Select "Just the `push` event".
8) Enable "Active".
9) Click the "Add webhook" button.

After clicking "Add webhook", you'll see a page like the one shown below:

That's it! Coolify will automatically redeploy your application whenever you push changes to your repository.