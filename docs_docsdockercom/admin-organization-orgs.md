---
title: Create your organization
url: https://docs.docker.com/admin/organization/orgs/
source: llms
fetched_at: 2026-01-24T14:13:23.687955814-03:00
rendered_js: false
word_count: 490
summary: This document provides instructions for administrators on how to create, view, and merge Docker organizations, including setup prerequisites and subscription management.
tags:
    - docker-hub
    - organization-management
    - admin-console
    - docker-id
    - subscription-management
    - account-conversion
category: guide
---

Subscription: Team Business

For: Administrators

This page describes how to create an organization.

## [Prerequisites](#prerequisites)

Before you begin creating an organization:

- You need a [Docker ID](https://docs.docker.com/accounts/create-account/)
- Review the [Docker subscriptions and features](https://www.docker.com/pricing/) to determine what subscription to choose for your organization

## [Create an organization](#create-an-organization)

There are multiple ways to create an organization. You can either:

- Create a new organization using the **Create Organization** option in the Admin Console or Docker Hub
- Convert an existing user account to an organization

The following section contains instructions on how to create a new organization. For prerequisites and detailed instructions on converting an existing user account to an organization, see [Convert an account into an organization](https://docs.docker.com/admin/organization/convert-account/).

To create an organization:

01. Sign in to [Docker Home](https://app.docker.com/) and navigate to the bottom of the organization list.
02. Select **Create new organization**.
03. Choose a subscription for your organization, a billing cycle, and specify how many seats you need. See [Docker Pricing](https://www.docker.com/pricing/) for details on the features offered in the Team and Business subscription.
04. Select **Continue to profile**.
05. Select **Create an organization** to create a new one.
06. Enter an **Organization namespace**. This is the official, unique name for your organization in Docker Hub. It's not possible to change the name of the organization after you've created it.
    
    > Note
    > 
    > You can't use the same name for the organization and your Docker ID. If you want to use your Docker ID as the organization name, then you must first [convert your account into an organization](https://docs.docker.com/admin/organization/convert-account/).
07. Enter your **Company name**. This is the full name of your company. Docker displays the company name on your organization page and in the details of any public images you publish. You can update the company name anytime by navigating to your organization's **Settings** page.
08. Select **Continue to billing** to continue.
09. Enter your organization's billing information and select **Continue to payment** to continue to the billing portal.
10. Provide your payment details and select **Purchase**.

You've now created an organization.

## [View an organization](#view-an-organization)

To view an organization in the Admin Console:

1. Sign in to [Docker Home](https://app.docker.com) and select your organization.
2. From the left-hand navigation menu, select **Admin Console**.

The Admin Console contains many options that let you to configure your organization.

## [Merge organizations](#merge-organizations)

> Warning
> 
> If you are merging organizations, it is recommended to do so at the *end* of your billing cycle. When you merge an organization and downgrade another, you will lose seats on your downgraded organization. Docker does not offer refunds for downgrades.

If you have multiple organizations that you want to merge into one, complete the following steps:

1. Based on the number of seats from the secondary organization, [purchase additional seats](https://docs.docker.com/subscription/manage-seats/) for the primary organization account that you want to keep.
2. Manually add users to the primary organization and remove existing users from the secondary organization.
3. Manually move over your data, including all repositories.
4. Once you're done moving all of your users and data, [downgrade](https://docs.docker.com/subscription/change/) the secondary account to a free subscription. Note that Docker does not offer refunds for downgrading organizations mid-billing cycle.

> Tip
> 
> If your organization has a Docker Business subscription with a purchase order, contact Support or your Account Manager at Docker.

## [More resources](#more-resources)

- [Video: Docker Hub Organizations](https://www.youtube.com/watch?v=WKlT1O-4Du8)