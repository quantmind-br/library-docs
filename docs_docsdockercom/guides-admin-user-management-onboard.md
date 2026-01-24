---
title: Onboarding and managing roles and permissions in Docker
url: https://docs.docker.com/guides/admin-user-management/onboard/
source: llms
fetched_at: 2026-01-24T14:03:10.910910031-03:00
rendered_js: false
word_count: 393
summary: This document provides guidance on onboarding owners and members to a Docker organization, including strategies for automated provisioning and secure authentication.
tags:
    - docker-organization
    - user-onboarding
    - sso
    - scim
    - jit-provisioning
    - group-mapping
    - access-control
category: guide
---

This page guides you through onboarding owners and members, and using tools like SSO and SCIM to future-proof onboarding going forward.

When you create a Docker organization, you automatically become its sole owner. While optional, adding additional owners can significantly ease the process of onboarding and managing your organization by distributing administrative responsibilities. It also ensures continuity and prevents blockers if the primary owner is unavailable.

For detailed information on owners, see [Roles and permissions](https://docs.docker.com/enterprise/security/roles-and-permissions/).

Members are granted controlled access to resources and enjoy enhanced organizational benefits. When you invite members to join your Docker organization, you immediately assign them a role.

### [Benefits of inviting members](#benefits-of-inviting-members)

- Enhanced visibility: Gain insights into user activity, making it easier to monitor access and enforce security policies.
- Streamlined collaboration: Help members collaborate effectively by granting access to shared resources and repositories.
- Improved resource management: Organize and track users within your organization, ensuring optimal allocation of resources.
- Access to enhanced features: Members benefit from organization-wide perks, such as increased pull limits and access to premium Docker features.
- Security control: Apply and enforce security settings at an organizational level, reducing risks associated with unmanaged accounts.

For detailed information, see [Manage organization members](https://docs.docker.com/admin/organization/members/).

A robust, future-proof approach to user management combines automated provisioning, centralized authentication, and dynamic access control. Implementing these practices ensures a scalable, secure, and efficient environment.

### [Secure user authentication with single sign-on (SSO)](#secure-user-authentication-with-single-sign-on-sso)

Integrating Docker with your identity provider streamlines user access and enhances security.

SSO:

- Simplifies sign in, as users sign in with their organizational credentials.
- Reduces password-related vulnerabilities.
- Simplifies onboarding as it works seamlessly with SCIM and group mapping for automated provisioning.

For more information, see the [SSO documentation](https://docs.docker.com/enterprise/security/single-sign-on/).

### [Automate onboarding with SCIM and JIT provisioning](#automate-onboarding-with-scim-and-jit-provisioning)

Streamline user provisioning and role management with [SCIM](https://docs.docker.com/enterprise/security/provisioning/scim/) and [Just-in-Time (JIT) provisioning](https://docs.docker.com/enterprise/security/provisioning/just-in-time/).

With SCIM you can:

- Sync users and roles automatically with your identity provider.
- Automate adding, updating, or removing users based on directory changes.

With JIT provisioning you can:

- Automatically add users upon first sign in based on [group mapping](#simplify-access-with-group-mapping).
- Reduce overhead by eliminating pre-invite steps.

### [Simplify access with group mapping](#simplify-access-with-group-mapping)

Group mapping automates permissions management by linking identity provider groups to Docker roles and teams.

It also:

- Reduces manual errors in role assignments.
- Ensures consistent access control policies.
- Help you scale permissions as teams grow or change.

For more information on how it works, see [Group mapping](https://docs.docker.com/enterprise/security/provisioning/group-mapping/).