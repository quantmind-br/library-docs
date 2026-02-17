---
title: Switch GitHub Apps
url: https://coolify.io/docs/applications/ci-cd/github/switch-apps.md
source: llms
fetched_at: 2026-02-17T14:39:30.424838-03:00
rendered_js: false
word_count: 226
summary: This document provides instructions on how to change the GitHub App associated with deployed applications in Coolify, useful for repository transfers or updating access permissions.
tags:
    - coolify
    - github-apps
    - git-source
    - repository-migration
    - deployment-configuration
category: guide
---

# Switch GitHub Apps

Switching GitHub Apps allows you to change the GitHub App associated with your deployed applications, for example, when moving repositories to a new organization or account.

### Why Switch GitHub Apps?

1. **Organization Changes**: You've moved repositories to a new GitHub organization that requires a different GitHub App.
2. **Access Management**: You want to use a GitHub App with different permissions or repository access.

::: warning IMPORTANT
This feature is introduced in **Coolify v4.0.0-beta.408**. To follow this guide, you **must** be using Coolify v4.0.0-beta.408 or a higher version.
:::

## 1. Move Repositories (Optional)

If your goal is to move a repository to a different account or organization, go ahead and transfer it on GitHub.

If you just want to use a different GitHub App without changing repositories, you can skip this step.

## 2. Add New GitHub App to Coolify

We have a dedicated guide for setting up a GitHub App, which you can follow here: [/applications/ci-cd/github/setup-app](/applications/ci-cd/github/setup-app). Follow that guide and come back here.

## 3. Set Up Repository Access

After adding the new GitHub App, verify that it has access to the correct repositories by following these steps:

## 4. Switch Git Source on Coolify

## 5. Update Repository Name (If Applicable)

You can skip this step if you didn't move your repository.

## 6. Redeploy the Application

To apply the new GitHub App to your application, redeploy it by clicking the **Redeploy** button.

That's it!