---
title: Troubleshoot SSO
url: https://docs.docker.com/enterprise/troubleshoot/troubleshoot-sso/
source: llms
fetched_at: 2026-01-24T14:27:21.415975685-03:00
rendered_js: false
word_count: 1197
summary: This document provides instructions for diagnosing and resolving common Docker single sign-on (SSO) issues related to identity provider configurations, user provisioning, and authentication errors.
tags:
    - docker-sso
    - troubleshooting
    - identity-provider
    - scim-provisioning
    - jit-provisioning
    - error-handling
category: guide
---

## Troubleshoot single sign-on

This page describes common single sign-on (SSO) errors and their solutions. Issues can stem from your identity provider (IdP) configuration or Docker settings.

If you experience SSO issues, check both Docker and your identity provider for errors first.

### [Check Docker error logs](#check-docker-error-logs)

1. Sign in to [Docker Home](https://app.docker.com/) and select your organization from the top-left account drop-down.
2. Select **Admin Console**, then **SSO and SCIM**.
3. In the SSO connections table, select the **Action** menu and then **View error logs**.
4. For more details on specific errors, select **View error details** next to an error message.
5. Note any errors you see on this page for further troubleshooting.

### [Check identity provider errors](#check-identity-provider-errors)

1. Review your IdP’s logs or audit trails for any failed authentication or provisioning attempts.
2. Confirm that your IdP’s SSO settings match the values provided in Docker.
3. If applicable, confirm that you have configured user provisioning correctly and that it is enabled in your IdP.
4. If applicable, verify that your IdP correctly maps Docker's required user attributes.
5. Try provisioning a test user from your IdP and verify if they appear in Docker.

For further troubleshooting, check your IdP's documentation or contact their support team.

### [Error message](#error-message)

When this issue occurs, the following error message is common:

### [Causes](#causes)

- Incorrect group name formatting in your identity provider (IdP): Docker requires groups to follow the format `<organization>:<team>`. If the groups assigned to a user do not follow this format, they will be ignored.
- Non-matching groups between IdP and Docker organization: If a group in your IdP does not have a corresponding team in Docker, it will not be recognized, and the user will be placed in the default organization and team.

### [Affected environments](#affected-environments)

- Docker single sign-on setup using IdPs such as Okta or Azure AD
- Organizations using group-based role assignments in Docker

### [Steps to replicate](#steps-to-replicate)

To replicate this issue:

1. Attempt to sign in to Docker using SSO.
2. The user is assigned groups in the IdP but does not get placed in the expected Docker Team.
3. Review Docker logs or IdP logs to find the error message.

### [Solutions](#solutions)

Update group names in your IdP:

1. Go to your IdP's group management section.
2. Check the groups assigned to the affected user.
3. Ensure each group follows the required format: `<organization>:<team>`
4. Update any incorrectly formatted groups to match this pattern.
5. Save changes and retry signing in with SSO.

### [Error message](#error-message-1)

When this issue occurs, the following error message is common:

### [Causes](#causes-1)

- User is not assigned to the organization: If Just-in-Time (JIT) provisioning is disabled, the user may not be assigned to your organization.
- User is not invited to the organization: If JIT is disabled and you do not want to enable it, the user must be manually invited.
- SCIM provisioning is misconfigured: If you use SCIM for user provisioning, it may not be correctly syncing users from your IdP.

### [Solutions](#solutions-1)

**Enable JIT provisioning**

JIT is enabled by default when you enable SSO. If you have JIT disabled and need to re-enable it:

1. Sign in to [Docker Home](https://app.docker.com/) and select your organization from the top-left account drop-down.
2. Select **Admin Console**, then **SSO and SCIM**.
3. In the SSO connections table, select the **Action** menu and then **Enable JIT provisioning**.
4. Select **Enable** to confirm.

**Manually invite users**

When JIT is disabled, users are not automatically added to your organization when they authenticate through SSO. To manually invite users, see [Invite members](https://docs.docker.com/admin/organization/members/#invite-members)

**Configure SCIM provisioning**

If you have SCIM enabled, troubleshoot your SCIM connection using the following steps:

1. Sign in to [Docker Home](https://app.docker.com/) and select your organization from the top-left account drop-down.
2. Select **Admin Console**, then **SSO and SCIM**.
3. In the SSO connections table, select the **Action** menu and then **View error logs**. For more details on specific errors, select **View error details** next to an error message. Note any errors you see on this page.
4. Navigate back to the **SSO and SCIM** page of the Admin Console and verify your SCIM configuration:
   
   - Ensure that the SCIM Base URL and API Token in your IdP match those provided in the Docker Admin Console.
   - Verify that SCIM is enabled in both Docker and your IdP.
5. Ensure that the attributes being synced from your IdP match Docker's [supported attributes](https://docs.docker.com/enterprise/security/provisioning/scim/#supported-attributes) for SCIM.
6. Test user provisioning by trying to provision a test user through your IdP and verify if they appear in Docker.

### [Error message](#error-message-2)

When this issue occurs, the following error message is common:

### [Causes](#causes-2)

Docker does not support an IdP-initiated SAML flow. This error occurs when a user attempts to authenticate from your IdP, such as using the Docker SSO app tile on the sign in page.

### [Solutions](#solutions-2)

**Authenticate from Docker apps**

The user must initiate authentication from Docker applications (Hub, Desktop, etc). The user needs to enter their email address in a Docker app and they will get redirected to the configured SSO IdP for their domain.

**Hide the Docker SSO app**

You can hide the Docker SSO app from users in your IdP. This prevents users from attempting to start authentication from the IdP dashboard. You must hide and configure this in your IdP.

### [Error message](#error-message-3)

When this issue occurs, the following error message is common:

### [Causes](#causes-3)

This error occurs when the organization has no available seats for the user when provisioning via Just-in-Time (JIT) provisioning or SCIM.

### [Solutions](#solutions-3)

**Add more seats to the organization**

Purchase additional Docker Business subscription seats. For details, see [Manage subscription seats](https://docs.docker.com/subscription/manage-seats/).

**Remove users or pending invitations**

Review your organization members and pending invitations. Remove inactive users or pending invitations to free up seats. For more details, see [Manage organization members](https://docs.docker.com/admin/organization/members/).

## [Domain is not verified for SSO connection](#domain-is-not-verified-for-sso-connection)

### [Error message](#error-message-4)

When this issue occurs, the following error message is common:

### [Causes](#causes-4)

This error occurs if the IdP authenticated a user through SSO and the User Principal Name (UPN) returned to Docker doesn’t match any of the verified domains associated to the SSO connection configured in Docker.

### [Solutions](#solutions-4)

**Verify UPN attribute mapping**

Ensure that the IdP SSO connection is returning the correct UPN value in the assertion attributes.

**Add and verify all domains**

Add and verify all domains and subdomains used as UPN by your IdP and associate them with your Docker SSO connection. For details, see [Configure single sign-on](https://docs.docker.com/enterprise/security/single-sign-on/configure/).

### [Error message](#error-message-5)

When this issue occurs, the following error message is common:

### [Causes](#causes-5)

The following causes may create this issue:

- The user pressed the back or refresh button during authentication.
- The authentication flow lost track of the initial request, preventing completion.

### [Solutions](#solutions-5)

**Do not disrupt the authentication flow**

Do not press the back or refresh button during sign-in.

**Restart authentication**

Close the browser tab and restart the authentication flow from the Docker application (Desktop, Hub, etc).

### [Error message](#error-message-6)

When this issue occurs, the following error message is common:

### [Causes](#causes-6)

The following causes may create this issue:

- The IdP sends a Name ID (UPN) that does not comply with the email format required by Docker.
- Docker SSO requires the Name ID to be the primary email address of the user.

### [Solutions](#solutions-6)

In your IdP, ensure the Name ID attribute format is correct:

1. Verify that the Name ID attribute format in your IdP is set to `EmailAddress`.
2. Adjust your IdP settings to return the correct Name ID format.