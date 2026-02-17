---
title: GitHub App
url: https://coolify.io/docs/applications/ci-cd/github/setup-app.md
source: llms
fetched_at: 2026-02-17T14:39:30.426908-03:00
rendered_js: false
word_count: 925
summary: This document explains how to integrate GitHub Apps with Coolify to manage access to private repositories using both automated and manual installation methods. It details the steps for configuring webhooks, setting up repository permissions, and deploying applications through the GitHub integration.
tags:
    - github-app
    - coolify
    - ci-cd
    - private-repositories
    - webhook-setup
    - deployment-guide
category: guide
---

# GitHub App

Github app allows you to grant access to a single or multiple private repositories from your either personal github account or your organization on github.

### Why use github app with Coolify?

Scoped Access: The GitHub app lets you grant Coolify access to a specific repository, a selected group of repositories, or even all of your repositories. This gives you flexibility and better control over what Coolify can access.

### When Not to Use github app with Coolify?

Lack of Permission: If you don't have the necessary permissions to install the GitHub app, or if you prefer not to install it, then it’s best not to use it with Coolify.

## Installation Methods

There are two ways to install Github App on Coolify:

* [Automated Installation](/applications/ci-cd/github/setup-app#automated-installation) (Recommended)
* [Manual Installation](/applications/ci-cd/github/setup-app#manual-installation)
  We highly recommend the Automated Installation method as it automates the process and reduces the chance of errors.

::: info Example Data
The following data is used as an example in this guide. Please replace it with your actual data when following the steps:

* **GitHub App Name on Coolify:** `Github App Tutorial`
* **GitHub App Name on Github:** `coolify-github-app-tutorial`
* **Webhook Endpoint:** `https://coolboxy.shadowarcanist.internal`
  :::

## Automated Installation

### 1. Create a Github App on Coolify

::: info

1. If you are using Selfhost or Enterprise version of Github then you can enter your github details on the Selhost/Enterprise github section.
2. The "System wide" option allows all teams you have on your coolify instance to use this specific github app, if you only want the current team to use the github app then leave this option unchecked.
   ::: warning
   Coolify cloud users won't see the option "System wide" because this option will enable your github app to all Cloud users so this option is disabled on Coolify Cloud
   :::

### 2. Set Webhook Endpoint

1. Select the endpoint for github to send Webhook when a event (commit, pr) happens on github. If this endpoint is not reachable then automatic deployments won't work so if you decide to close port 8000 on your server you have to set the webhook endpoint as your Coolify dashboard domain

### 3. Create Github App on Github

### 4. Allow Github app access to repositories

### 5. Create a New Resource on Coolify

1. Select your project from the Coolify dashboard.
2. Click the **+ New** button to create a new resource.

### 6. Select Private Repository (with Github App) as Resource Type

### 6. Choose Your Server

::: warning HEADS UP!
Coolify automatically selects the `localhost` server if you don't have any remote servers connected. In such cases, skip to the next step.
:::

Choose the server where you want to deploy the application.

### 7. Choose Your Github App

Select the Github App you created in Coolify from the list of available Apps.

### 8. Configure the Application and Deploy

1. Choose Repository and click on "Load Repository" button.

Once configured, deploy your application.

That's it!

***

::: danger HEADS UP!
**The Automated installation guide ends here. If you’ve followed the steps above, you can start using Github Apps now. The guide below is for those who want to manually install and set up Github App.**
:::

## Manual Installation

### 1. Create a Github App on Coolify

::: info

1. If you are using Selfhost or Enterprise version of Github then you can enter your github details on the Selhost/Enterprise github section.
2. The "System wide" option allows all teams you have on your coolify instance to use this specific github app, if you only want the current team to use the github app then leave this option unchecked.
   ::: warning
   Coolify cloud users won't see the option "System wide" because this option will enable your github app to all Cloud users so this option is disabled on Coolify Cloud
   :::

We will need the following data to setup the github app:

* App ID
* Installation ID
* Client ID
* Client Secret
* Webhook Secret
* SSH Key

We will get these data in the next few steps.

### 2. Create a App on Github

Creating apps on github slightly varies for personal accounts and organizations so choose the correct one from the below section

:::tabs
\== Personal Account


1. Go to your github account settings
2. On the sidebar scroll down till you see "developer settings" and click on it

\== Organization


1. Go to your github Organization settings
2. On the sidebar scroll down till you see "**developer settings**" and click on it
3. Click on "Github Apps"
4. Click the "New github app" button

:::

### 3. Setup the Github App on Github

5. Enable the option `Redirect on Update`
6. Enter Webhook URL: `https://coolboxy.shadowarcanist.internal/webhooks/source/github/events`

::: info
You have to replace `https://coolboxy.shadowarcanist.internal` with your Coolify dashboard url and replace `a8000cg0g0ogcc0ggkk8ow4k` with the Source ID [Step 1](#_1-create-a-github-app-on-coolify-1)
:::

7. Enter Webhook Secret (this has to be a random string, you can use tools like [Random String Generator](https://getrandomgenerator.com/string))
8. Enable the option `Enable SSL verification`

::: warning HEADS Up!
On the screenshot above for permissions section we have hidden lot of Permission and only shown the Permission needed to setup Github app for Coolify.
:::

### 4. Add Private keys on Coolify

### 5. Create a New Resource on Coolify

1. Select your project from the Coolify dashboard.
2. Click the **+ New** button to create a new resource.

### 6. Select Private Repository (with Github App) as Resource Type

### 6. Choose Your Server

::: warning HEADS UP!
Coolify automatically selects the `localhost` server if you don't have any remote servers connected. In such cases, skip to the next step.
:::

Choose the server where you want to deploy the application.

### 7. Choose Your Github App

Select the Github App you created in Coolify from the list of available Apps.

### 8. Configure the Application and Deploy

1. Choose Repository and click on "Load Repository" button.

Once configured, deploy your application.

That's it!