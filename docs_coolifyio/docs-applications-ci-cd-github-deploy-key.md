---
title: GitHub Deploy Key
url: https://coolify.io/docs/applications/ci-cd/github/deploy-key.md
source: llms
fetched_at: 2026-02-17T14:39:27.327732-03:00
rendered_js: false
word_count: 519
summary: This document provides step-by-step instructions on how to configure GitHub Deploy Keys to securely grant Coolify read-only access to private repositories.
tags:
    - github
    - deploy-keys
    - ssh-keys
    - private-repositories
    - coolify-deployment
    - security
category: guide
---

# GitHub Deploy Key

Deploy keys allow you to grant read-only access to a single private GitHub repository without using a personal access token or SSH key tied to your account.

When using deploy keys, Coolify can clone and deploy from private repositories securely, ensuring that only the specified repository is accessible.

### Why Use Deploy Keys with Coolify?

1. **Secure Access**: Grant read-only access to a single repository without sharing to many repositories.
2. **Repository-Specific**: Deploy keys are scoped to one repository.
3. **No Account Exposure**: Prevents potential security risks if the key is compromised.
4. **Cannot Install Github App**: Deploy keys can be used when you cannot install a GitHub App to your organization.

### When Not to Use Deploy Keys

1. **Multiple Repositories**: If you need access to multiple private repositories, consider using a GitHub App.

***

::: info Example Data
The following data is used as an example in this guide. Please replace it with your actual data when following the steps:

* **Repository Owner:** `ShadowArcanist`
* **Repository Name:** `coolify-dev`
* **Deploy Key Name:** `Deploy Key Tutorial`
* **SSH URL:** `git@github.com:ShadowArcanist/coolify-dev.git`
  :::

## 1. Create a Private Key on Coolify

1. In your Coolify dashboard, click on **Keys & Tokens** from the sidebar.
2. Click on **Private keys** tab.
3. Click the **+ Add** button to create a new private key.

4) Click **Generate new RSA SSH Key** or **Generate new ED25519 SSH Key** to generate a key pair.

5. Copy the public key.
6. Click **Continue** to save the keys.

::: success TIP
You can also generate a key externally using the `ssh-keygen` command and paste the private key into Coolify:

```sh
ssh-keygen -t rsa -b 4096 -C "coolify-deploy-key"
```

Then, copy the contents of the generated `.pub` file for the next step.
:::

## 2. Add Deploy Key on GitHub

1. Go to your GitHub repository settings.
2. Navigate to **Deploy keys** in the left sidebar.
3. Click **Add deploy key** button.

::: info TIP
You can also access the deploy keys page directly at `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/settings/keys`
:::

4. Enter a title for your deploy key (e.g., `Coolify Deploy Key`).
5. Paste the public key you copied from Coolify.
6. Make sure **Allow write access** is unchecked (deploy keys should be read-only).
7. Click **Add key** to save.

## 3. Copy Repository SSH URL

1. Go to your GitHub repository.
2. Click the **Code** button.
3. Select the **Local** tab.
4. Click the **SSH** tab.
5. Copy the SSH URL (e.g., `git@github.com:ShadowArcanist/coolify-dev.git`).

## 4. Create a New Resource on Coolify

1. Select your project from the Coolify dashboard.
2. Click the **+ New** button to create a new resource.

## 5. Select Private Repository (with Deploy Key) as Resource Type

Select **Private Repository (with Deploy Key)** from the available resource types.

## 6. Choose Your Server

::: warning HEADS UP!
Coolify automatically selects the `localhost` server if you don't have any remote servers connected. In such cases, skip to the next step.
:::

Choose the server where you want to deploy the application.

## 7. Choose Your Deploy Key

Select the private key you created in Coolify from the list of available private keys.

## 8. Configure the Application and Deploy

1. Paste the SSH URL you copied from GitHub (e.g., `git@github.com:ShadowArcanist/coolify-dev.git`).
2. After entering the repository link, configure the buildpack, ports, and other settings. (Refer to our dedicated guide on [builds](/builds/introduction) for more details.)

Once configured, deploy your application.

That's it!