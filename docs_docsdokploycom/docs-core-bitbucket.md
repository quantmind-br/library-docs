---
title: Bitbucket | Dokploy
url: https://docs.dokploy.com/docs/core/bitbucket
source: crawler
fetched_at: 2026-02-14T14:12:55.482941-03:00
rendered_js: true
word_count: 460
summary: This document provides step-by-step instructions for connecting Bitbucket repositories to Dokploy and setting up automatic deployments using webhooks.
tags:
    - bitbucket
    - git-integration
    - deployment-automation
    - dokploy
    - webhooks
    - repository-configuration
category: guide
---

Git Sources

Configure your Bitbucket repositories for deployments. This includes setting up access tokens, repository names, and branches.

Dokploy offer a way to connect your Bitbucket Repository to your Dokploy panel, you can use Groups Names or personal accounts.

Go to `Git` and select `Bitbucket` as the source, then you can use the following options:

- **Bitbucket Username**: Set the username that you want to connect to Dokploy.
- **App Password**: Set the app password you've created.
- **Workspace(Optional)**: Assign a workspace name, this is useful if you want to connect to another workspace.

Follow the steps to connect your Bitbucket account to Dokploy.

01. Go to `https://bitbucket.org/account/settings/app-passwords/new` .
02. Set Label: eg. `Dokploy-Bitbucket-App`. you can choose any name that you want.
03. In permissions make sure to select `Account: Read`, `Workspace membership: Read`, `Projects: Read` , `Repositories: Read` `Pull requests: Read` and `Webhooks: Read and write`.
04. Click on `Create`.
05. Copy the `App Password` and paste it in Dokploy `Bitbucket` Modal section.
06. Set your `Bitbucket Username`.
07. (Optional) If you want to use Workspaces, go to `https://bitbucket.org/account/workspaces/`, eg. If you have `dokploy-workspace` copy and paste it in Workspace Name, please make sure to use the slugified name, if you use names like Dokploy Workspace in this field can cause issues.
08. Click on `Configure Bitbucket`.
09. If everything is correct, you can update enter to the Update Icon, and click on `Test Connection` to make sure everything is working.
10. Now you can use the repositories from your Gitlab Account in `Applications` or `Docker Compose` services.

Dokploy doesn't support Bitbucket Automatic deployments on each push you make to your repository.

You can configure automatic deployments in Dokploy for the Following Services:

1. **Applications**
2. **Docker Compose**

The steps are the same for both services.

1. Go to either `Applications` or `Docker Compose` and go to `Deployments` Tab.
2. Copy the `Webhook URL`.
3. Go to your Bitbucket Account and select the repository.
4. In the left menu, select `Repository Settings` and then `Webhooks`.
5. Click on `Add Webhook`.
6. Set any `Title` and the `URL` to the one you copied in the previous step.
7. In the Trigger section, select `Push Events`.
8. Click on `Add Webhook`.
9. Now you have automatic deployments enabled for the selected repository.

By default, Dokploy will automatically deploy your application on the Branch you have selected.

eg. Let's suppose you have a `application` in this way:

Repository: `my-app` Branch: `feature`

If you try to make a push on another branch eg. `main`, Dokploy will not automatically deploy your application, because your application have selected `feature` as the Branch.

In the case you want to have multiple applications in the same repository, eg. (development, staging, production), you can create 3 `Applications` in Dokploy and select the branch in each of them.

This is very usefull if you want to have multiple environments for the same application.