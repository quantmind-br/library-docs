---
title: Desktop settings reporting
url: https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/compliance-reporting/
source: llms
fetched_at: 2026-01-24T14:26:40.58882172-03:00
rendered_js: false
word_count: 586
summary: This document explains how administrators use the Desktop settings reporting dashboard to monitor policy compliance across an organization and provides steps for resolving user compliance issues.
tags:
    - docker-desktop
    - compliance-reporting
    - settings-policy
    - administrator-guide
    - business-subscription
    - policy-enforcement
category: guide
---

Table of contents

* * *

Subscription: Business

Availability: Early Access

Requires: Docker Desktop 4.40 and later

For: Administrators

Desktop settings reporting tracks user compliance with Docker Desktop settings policies. Use this feature to monitor policy application across your organization and identify users who need assistance with compliance.

## [Prerequisites](#prerequisites)

Before you can use Docker Desktop settings reporting, make sure you have:

- [Docker Desktop 4.37.1 or later](https://docs.docker.com/desktop/release-notes/) installed across your organization
- [A verified domain](https://docs.docker.com/enterprise/security/single-sign-on/configure/#step-one-add-and-verify-your-domain)
- [Enforced sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) for your organization
- A Docker Business subscription
- At least one settings policy configured

> Warning
> 
> Users on Docker Desktop versions older than 4.40 may appear non-compliant because older versions can't report compliance status. For accurate reporting, update users to Docker Desktop version 4.40 or later.

## [Access the reporting dashboard](#access-the-reporting-dashboard)

To view compliance reporting:

1. Sign in to [Docker Home](https://app.docker.com) and select your organization.
2. Select **Admin Console**, then **Desktop settings reporting**.

The reporting dashboard provides these tools:

- A search field to find users by username or email address
- Filter options to show users assigned to specific policies
- Toggles to hide or un-hide compliant users
- Compliance status indicators
- CSV export option to download compliance data

## [User compliance statuses](#user-compliance-statuses)

Docker Desktop evaluates three types of status to determine overall compliance:

### [Compliance status](#compliance-status)

This is the primary status shown in the dashboard:

Compliance statusWhat it meansCompliantThe user fetched and applied the latest assigned policy.Non-compliantThe user fetched the correct policy, but hasn't applied it.OutdatedThe user fetched a previous version of the policy.No policy assignedThe user does not have any policy assigned to them.Uncontrolled domainThe user's email domain is not verified.

### [Domain status](#domain-status)

Shows how the user's email domain relates to your organization:

Domain statusWhat it meansVerifiedThe user’s email domain is verified.Guest userThe user's email domain is not verified.DomainlessYour organization has no verified domains, and the user's domain is unknown.

### [Settings status](#settings-status)

Indicates the user's policy assignment:

Settings statusWhat it meansGlobal policyThe user is assigned your organization's default policy.User policyThe user is assigned a specific custom policy.No policy assignedThe user is not assigned to any policy.

## [Monitor compliance](#monitor-compliance)

From the **Desktop settings reporting** dashboard, you can:

- Review organization-wide compliance at a glance
- Turn on **Hide compliant users** to focus on issues
- Filter by specific policies to check targeted compliance
- Export compliance data
- Select any user's name for detailed status and resolution steps

When you select a user's name, you'll see their detailed compliance information including current status, domain verification, assigned policy, last policy fetch time, and Docker Desktop version.

## [Resolve compliance issues](#resolve-compliance-issues)

You can select a non-compliant user's name in the dashboard for recommended status resolution steps. The following sections are general resolution steps for non-compliant statuses:

### [Non-compliant or outdated users](#non-compliant-or-outdated-users)

- Ask the user to fully quit and relaunch Docker Desktop
- Verify the user is signed in to Docker Desktop
- Confirm the user has Docker Desktop 4.40 or later

### [Uncontrolled domain users](#uncontrolled-domain-users)

- Verify the user's email domain in your organization settings
- If the domain should be controlled, add and verify it, then wait for verification
- If the user is a guest and shouldn't be controlled, no action is needed

### [No policy assigned users](#no-policy-assigned-users)

- Assign the user to an existing policy
- Create a new user-specific policy for them
- Verify they're included in your organization's default policy scope

After users take corrective action, refresh the reporting dashboard to verify status changes.

## [Policy update timing](#policy-update-timing)

Docker Desktop checks for policy updates:

- At startup
- Every 60 minutes while Docker Desktop is running
- When users restart Docker Desktop

Changes to policies in the Admin Console are available immediately, but users must restart Docker Desktop to apply them.