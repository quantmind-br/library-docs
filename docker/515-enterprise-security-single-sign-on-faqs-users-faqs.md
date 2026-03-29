---
title: User management
url: https://docs.docker.com/enterprise/security/single-sign-on/faqs/users-faqs/
source: llms
fetched_at: 2026-01-24T14:27:10.059268373-03:00
rendered_js: false
word_count: 420
summary: This document addresses frequently asked questions regarding user management through Single Sign-On (SSO), covering topics such as Just-in-Time provisioning, SCIM integration, and authentication requirements.
tags:
    - docker-sso
    - user-management
    - just-in-time-provisioning
    - scim
    - authentication
    - identity-provider
category: reference
---

## SSO user management FAQs

No, you don't need to manually add users to your organization. Just ensure user accounts exist in your IdP. When users sign in to Docker with their domain email address, they're automatically added to the organization after successful authentication.

All users must authenticate using the email domain specified during SSO setup. Users with email addresses that don't match the verified domain can sign in as guests with username and password if SSO isn't enforced, but only if they've been invited.

When SSO is turned on, users are prompted to authenticate through SSO the next time they sign in to Docker Hub or Docker Desktop. The system detects their domain email and prompts them to sign in with SSO credentials instead.

For CLI access, users must authenticate using personal access tokens.

Yes, you can convert existing users to SSO accounts. Ensure users have:

- Company domain email addresses and accounts in your IdP
- Docker Desktop version 4.4.2 or later
- Personal access tokens created to replace passwords for CLI access
- CI/CD pipelines updated to use PATs instead of passwords

For detailed instructions, see [Configure single sign-on](https://docs.docker.com/enterprise/security/single-sign-on/configure/).

Docker SSO provides Just-in-Time (JIT) provisioning by default. Users are provisioned when they authenticate with SSO. If users leave the organization, administrators must manually [remove the user](https://docs.docker.com/admin/organization/members/#remove-a-member-or-invitee) from the organization.

[SCIM](https://docs.docker.com/enterprise/security/provisioning/scim/) provides full synchronization with users and groups. When using SCIM, the recommended configuration is to turn off JIT so all auto-provisioning is handled by SCIM.

Additionally, you can use the [Docker Hub API](https://docs.docker.com/reference/api/hub/latest/) to complete this process.

When JIT is turned off (available with SCIM in the Admin Console), users must be organization members or have pending invitations to access Docker. Users who don't meet these criteria get an "Access denied" error and need administrator invitations.

See [SSO authentication with JIT provisioning disabled](https://docs.docker.com/enterprise/security/provisioning/just-in-time/#sso-authentication-with-jit-provisioning-disabled).

Not without SSO. Joining requires an invite from an organization owner. When SSO is enforced, users with verified domain emails can automatically join the organization when they sign in.

Turning on SCIM doesn't immediately remove or modify existing licensed users. They retain current access and roles, but you'll manage them through your IdP after SCIM is active. If SCIM is later turned off, previously SCIM-managed users remain in Docker but are no longer automatically updated based on your IdP.

All Docker accounts have public profiles associated with their namespace. If you don't want user information (like full names) to be visible, remove those attributes from your SSO and SCIM mappings, or use different identifiers to replace users' full names.