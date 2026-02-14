---
title: Gitea | Dokploy
url: https://docs.dokploy.com/docs/core/gitea
source: crawler
fetched_at: 2026-02-14T14:18:21.417672-03:00
rendered_js: true
word_count: 433
summary: This document provides instructions for connecting Gitea repositories to Dokploy and configuring automated deployments using webhooks and branch-specific settings.
tags:
    - gitea
    - dokploy
    - deployments
    - git-integration
    - webhooks
    - oauth2-configuration
    - continuous-deployment
category: guide
---

Git Sources

Configure Gitea repositories for deployments. This includes setting up access tokens, repository names, and branches.

Dokploy offers a way to connect your Gitea Repository to your Dokploy panel, you can use Organizations or personal accounts.

Go to `Git` and select `Gitea` as the source, then you can use the following options:

- **Application ID**: Select the application ID that you want to connect to Dokploy.
- **Personal Secret**: Select the secret that you want to connect to Dokploy.
- **Organization Name(Optional)**: Select the organization name that you want to connect to Dokploy (Ideal for Gitea Organizations).

Follow the steps to connect your Gitea account to Dokploy:

01. Go to your Gitea instance's settings (e.g., `https://gitea.com/user/settings/applications`) and scroll to the `Create a new OAuth2 Application`.
02. Set Application Name: e.g., `Dokploy-Gitea-App`. Choose any name you want.
03. Redirect URI: Copy the `Redirect URI` from Dokploy. e.g., `https://dokploy.com/api/providers/gitea/callback`.
04. Check Confidential Client
05. Click on `Create Application`.
06. Copy the `Client ID` and `Client Secret` from Gitea and paste them in Dokploy's `Gitea` Modal section.
07. Click on `Configure Gitea App`.
08. That operation will save the Gitea Provider configuration and redirect you to Gitia to authorize Dokploy to have access.
09. Click on `Authorize`.
10. You will be redirected to the `Git` section of Dokploy.
11. Now you can use the repositories from your Gitea Account in `Applications` or `Docker Compose` services.

Dokploy doesn't support Gitea Automatic deployments on each push you make to your repository.

You can configure automatic deployments in Dokploy for the Following Services:

1. **Applications**
2. **Docker Compose**

The steps are the same for both services.

01. Go to either `Applications` or `Docker Compose` and go to `Deployments` Tab.
02. Copy the `Webhook URL`.
03. Go to your Gitea Account and select the repository.
04. In the left menu, select `Settings` and then `Webhooks`.
05. Click on `Add Webhook`.
06. Set the `URL` to the one you copied in the previous step.
07. In the Trigger section, select `Push Events`.
08. Click on `Add Webhook`.
09. Click on `Save`.
10. Now you have automatic deployments enabled for the selected repository.

By default, Dokploy will automatically deploy your application on the Branch you have selected.

e.g., Let's suppose you have an `application` in this way:

Repository: `my-app` Branch: `feature`

If you try to make a push on another branch e.g., `main`, Dokploy will not automatically deploy your application, because your application has selected `feature` as the Branch.

In the case you want to have multiple applications in the same repository, e.g., (development, staging, production), you can create 3 `Applications` in Dokploy and select the branch in each of them.

This is very useful if you want to have multiple environments for the same application.

Normal